"""Archive CogPO, the Cognitive Paradigm Ontology, into .cog_data/cogpo/ byte for byte.

This is a faithful archive, not an analysis. Every file is the raw body the server
returned, written unparsed: no pretty-printing, no re-encoding, no reordering. The
summary that the site consumes is derived from it by `src/build_cogpo_data.py`.

CogPO has two public faces and this archives both:

- The OWL release, `CogPOver1.owl` (version 1.0, November 2010), which is the ontology
  proper. It declares two imports. `CogPOexternalVer1.owl` lives in the same directory
  and is fetched too, although the server returns the main file's bytes for that URL
  as well (the manifest records the identical hash). The IAO import lives at the OBO
  Foundry and is not CogPO content, so it is listed in the manifest but not fetched.
- The wiki at `www.wiki.cogpo.org`, a MediaWiki whose main page links every term. Each
  term page is stored as raw wikitext (`action=raw`), which is the curated text without
  the skin. The wiki carries a few terms and definitions the OWL does not (for example
  the Stimulus Role values), so the builder reports the two against each other.

Neither CogPO host serves https (`www.cogpo.org` refuses the connection; the wiki host
answers https with its hosting company's certificate and a 404), so everything is fetched
over plain http and the transfer cannot be trusted on its own. The OWL release is a
static file whose SHA-256 is pinned in `src/build_cogpo_data.py`; this script warns when
the downloaded file differs from that pin, and the builder refuses to use it. The wiki
pages have no pin: they are supplementary, and their effect on the summary (a few extra
terms, curation dates) is reviewable in the committed `data/cogpo_summary.json`.

    python src/fetch_cogpo_data.py                 # full archive, resumable
    python src/fetch_cogpo_data.py --limit 5       # smoke test: five wiki pages
    python src/fetch_cogpo_data.py --refresh       # re-fetch what is already stored
    python src/fetch_cogpo_data.py --no-wiki       # the OWL files only

Layout::

    .cog_data/cogpo/
        MANIFEST.json              one record per HTTP request
        README.md                  provenance and refresh instructions
        owl/<name>.owl             raw body of each OWL file
        wiki/Main_Page.html        rendered main page, the source of the term list
        wiki/pages/<title>.wiki    raw wikitext of one term page, title percent-encoded
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import html
import json
import re
import time
import urllib.error
import urllib.parse
import urllib.request
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path

OWL_URL = "http://www.cogpo.org/ontologies/CogPOver1.owl"
OWL_DIR = "http://www.cogpo.org/ontologies/"
WIKI = "http://www.wiki.cogpo.org/index.php"
USER_AGENT = "hed-task-research/1.0 (+https://github.com/hed-standard/hed-task)"

_OWL_NS = "{http://www.w3.org/2002/07/owl#}"
_RDF_RESOURCE = "{http://www.w3.org/1999/02/22-rdf-syntax-ns#}resource"

# Term links on the rendered main page. Titles are taken as the wiki spells them.
_TITLE_LINK = re.compile(r'href="/index\.php\?title=([^"&#]+)"')

DEFAULT_OUT = Path(__file__).parent.parent / ".cog_data" / "cogpo"

# The pinned hash lives with the builder, which is what enforces it.
from build_cogpo_data import EXPECTED_OWL_SHA256  # noqa: E402


def fetch(url: str, timeout: int = 60, retries: int = 4, pause: float = 2.0) -> tuple[bytes, int]:
    """GET a URL and return (raw body bytes, HTTP status), retrying transient failures.

    A 404 is returned as a status, not raised, so the caller can record it: a wiki
    title that is linked but has no page is a fact about the source worth keeping.
    """
    last: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read(), response.status
        except urllib.error.HTTPError as exc:
            if exc.code == 404:
                return b"", 404
            last = exc
        except (urllib.error.URLError, TimeoutError) as exc:
            last = exc
        if attempt < retries - 1:
            time.sleep(pause * (attempt + 1))
    raise RuntimeError(f"failed after {retries} attempts: {url} ({last})")


def record(url: str, body: bytes, status: int, path: Path, root: Path) -> dict:
    """Describe one stored response for the manifest."""
    return {
        "url": url,
        "status": status,
        "path": path.relative_to(root).as_posix(),
        "bytes": len(body),
        "sha256": hashlib.sha256(body).hexdigest(),
        "retrieved_on": datetime.now(timezone.utc).isoformat(timespec="seconds"),
    }


def from_disk(url: str, path: Path, root: Path) -> dict:
    """Describe a file archived by an earlier run so the manifest covers every file."""
    entry = record(url, path.read_bytes(), 200, path, root)
    entry["retrieved_on"] = "(earlier run)"
    return entry


def owl_imports(body: bytes) -> list[str]:
    """Return the owl:imports targets declared in an OWL/RDF-XML body.

    Parsed only to enumerate; the stored bytes are untouched.
    """
    root = ET.fromstring(body)
    ontology = root.find(_OWL_NS + "Ontology")
    if ontology is None:
        return []
    return [imp.get(_RDF_RESOURCE, "") for imp in ontology.findall(_OWL_NS + "imports") if imp.get(_RDF_RESOURCE)]


def wiki_titles(main_page: bytes) -> list[str]:
    """Return the term titles linked from the rendered main page, in page order.

    Namespaced pages (`Special:`, `CogPOwiki:`, `Talk:`) are the wiki's own furniture
    and are skipped; everything else the main page links is a term or a project page.
    """
    seen: list[str] = []
    for raw in _TITLE_LINK.findall(main_page.decode("utf-8")):
        title = urllib.parse.unquote(html.unescape(raw))
        if ":" in title or title == "Main_Page" or title in seen:
            continue
        seen.append(title)
    return seen


def page_filename(title: str) -> str:
    """Percent-encode a title so that a slash or an apostrophe in it cannot reach the filesystem."""
    return urllib.parse.quote(title, safe="") + ".wiki"


def check_name_collisions(names: list[str]) -> None:
    """Refuse names that would collide on a case-insensitive filesystem."""
    seen: dict[str, list[str]] = collections.defaultdict(list)
    for name in names:
        seen[name.lower()].append(name)
    clashes = {k: v for k, v in seen.items() if len(v) > 1}
    if clashes:
        raise SystemExit(f"wiki titles differ only by case and cannot be separate files on Windows: {clashes}")


def archive_owl(root: Path, manifest: dict, refresh: bool) -> None:
    """Store the main OWL file and every same-directory import it declares."""
    owl_dir = root / "owl"
    owl_dir.mkdir(parents=True, exist_ok=True)

    queue = [OWL_URL]
    done: set[str] = set()
    while queue:
        url = queue.pop(0)
        if url in done:
            continue
        done.add(url)
        name = url.rsplit("/", 1)[-1]
        dest = owl_dir / name
        if dest.exists() and not refresh:
            body = dest.read_bytes()
            entry = from_disk(url, dest, root)
            print(f"  {name}: already stored ({len(body)} bytes)")
        else:
            print(f"Fetching {url} ...")
            body, status = fetch(url)
            if status != 200 or not body:
                manifest["failures"].append({"kind": "owl", "url": url, "status": status})
                print(f"  FAILED {url}: HTTP {status}")
                continue
            dest.write_bytes(body)
            entry = record(url, body, status, dest, root)
            print(f"  {name}: {len(body)} bytes")
        if entry["sha256"] != EXPECTED_OWL_SHA256:
            print(
                f"  WARNING: {name} has SHA-256 {entry['sha256']}, not the pinned value in "
                "src/build_cogpo_data.py. The file was fetched over plain http; the builder will refuse it "
                "until the pin is updated or --allow-unverified is given."
            )
        manifest["owl"][name] = entry

        for target in owl_imports(body):
            if target.startswith(OWL_DIR):
                queue.append(target)
            elif target not in manifest["imports_not_archived"]:
                manifest["imports_not_archived"].append(target)

    # The server answers the external-import URL with the main file. Say so in the
    # manifest rather than leaving two identical files to be discovered by hand.
    hashes: dict[str, list[str]] = collections.defaultdict(list)
    for name, entry in manifest["owl"].items():
        hashes[entry["sha256"]].append(name)
    for names in hashes.values():
        if len(names) > 1:
            for name in names:
                manifest["owl"][name]["identical_to"] = [n for n in names if n != name]
            print(f"  note: identical bytes served for {', '.join(names)}")


def archive_wiki(root: Path, manifest: dict, refresh: bool, limit: int, delay: float) -> None:
    """Store the rendered main page and the raw wikitext of every term it links."""
    wiki_dir = root / "wiki"
    pages_dir = wiki_dir / "pages"
    pages_dir.mkdir(parents=True, exist_ok=True)

    main_url = f"{WIKI}?title=Main_Page"
    main_dest = wiki_dir / "Main_Page.html"
    print(f"Fetching {main_url} ...")
    body, status = fetch(main_url)
    if status != 200 or not body:
        manifest["failures"].append({"kind": "wiki", "url": main_url, "status": status})
        print(f"  FAILED main page: HTTP {status}; wiki layer skipped")
        return
    main_dest.write_bytes(body)
    manifest["wiki"]["main_page"] = record(main_url, body, status, main_dest, root)

    titles = wiki_titles(body)
    check_name_collisions([page_filename(t) for t in titles])
    manifest["wiki"]["titles_linked"] = len(titles)
    targets = titles[:limit] if limit else titles
    print(f"  {len(titles)} term pages linked; fetching {len(targets)} as raw wikitext ...")

    stored: dict[str, dict] = {}
    fetched = skipped = missing = 0
    for i, title in enumerate(targets, 1):
        dest = pages_dir / page_filename(title)
        url = f"{WIKI}?title={urllib.parse.quote(title, safe='/()')}&action=raw"
        if dest.exists() and not refresh:
            stored[title] = from_disk(url, dest, root)
            skipped += 1
            continue
        try:
            body, status = fetch(url)
        except RuntimeError as exc:
            manifest["failures"].append({"kind": "wiki", "title": title, "url": url, "error": str(exc)})
            print(f"  [{i}/{len(targets)}] FAILED {title}: {exc}")
            continue
        if status == 404:
            manifest["failures"].append({"kind": "wiki", "title": title, "url": url, "status": 404})
            missing += 1
            print(f"  [{i}/{len(targets)}] no page: {title}")
            continue
        dest.write_bytes(body)
        stored[title] = record(url, body, status, dest, root)
        fetched += 1
        if fetched % 50 == 0:
            print(f"  [{i}/{len(targets)}] fetched {fetched}, skipped {skipped}")
        time.sleep(delay)

    manifest["wiki"]["pages"] = {"fetched": fetched, "skipped": skipped, "missing": missing, "stored": stored}
    print(f"  wiki: fetched {fetched}, skipped {skipped}, missing {missing}")


def write_readme(root: Path, manifest: dict) -> None:
    owl_rows = []
    for name, entry in manifest["owl"].items():
        same = f" (same bytes as {', '.join(entry['identical_to'])})" if entry.get("identical_to") else ""
        owl_rows.append(f"| `owl/{name}` | {entry['bytes']} | `{entry['sha256'][:12]}...`{same} |")
    pages = manifest["wiki"].get("pages", {})
    page_count = len(pages.get("stored", {}))
    not_archived = "\n".join(f"- `{url}`" for url in manifest["imports_not_archived"]) or "- (none)"
    (root / "README.md").write_text(
        f"""# CogPO archive

Byte-exact archive of CogPO, the Cognitive Paradigm Ontology (Turner and Laird,
Neuroinformatics 2012), taken {manifest["started_on"][:10]} from `{OWL_URL}` and the
wiki at `{WIKI}`.

Every file here is the raw response body as the server returned it. Nothing is parsed,
reformatted, filtered, or derived. `src/build_cogpo_data.py` reads this directory and
writes the tracked summary `data/cogpo_summary.json`.

| File | Bytes | SHA-256 |
|---|---|---|
{chr(10).join(owl_rows)}

Wiki: `wiki/Main_Page.html` (rendered; the source of the term list) and
{page_count} term pages as raw wikitext under `wiki/pages/`, one per title linked
from the main page, filename percent-encoded from the title.

Imports declared by the OWL file that are not CogPO content and are not archived:

{not_archived}

## Layout

    MANIFEST.json              one record per HTTP request: url, status, bytes, sha256
    owl/<name>.owl             raw body of each OWL file
    wiki/Main_Page.html        rendered main page
    wiki/pages/<title>.wiki    raw wikitext of one term page (index.php?title=...&action=raw)

## Verifying

Each stored file has a `sha256` in `MANIFEST.json` covering the exact bytes on disk.

## Refreshing

    python src/fetch_cogpo_data.py            # resumable; skips what is already stored
    python src/fetch_cogpo_data.py --refresh  # re-fetch everything

Everything is fetched over plain http: the wiki's TLS certificate is invalid. This
directory is untracked. It is not in git and has no backup.
""",
        encoding="utf-8",
        newline="\n",
    )


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--limit", type=int, default=0, help="stop after N wiki pages")
    parser.add_argument("--refresh", action="store_true", help="re-fetch files already stored")
    parser.add_argument("--no-wiki", action="store_true", help="archive the OWL files only")
    parser.add_argument("--delay", type=float, default=0.25, help="seconds between wiki requests")
    args = parser.parse_args()

    root: Path = args.out
    root.mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "source": {"owl": OWL_URL, "wiki": WIKI},
        "client": USER_AGENT,
        "started_on": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note": "Every file is the raw response body, byte for byte. Nothing is parsed, reformatted, filtered, or derived.",
        "owl": {},
        "imports_not_archived": [],
        "wiki": {},
        "failures": [],
    }

    archive_owl(root, manifest, args.refresh)
    if not args.no_wiki:
        archive_wiki(root, manifest, args.refresh, args.limit, args.delay)

    manifest["finished_on"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (root / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    write_readme(root, manifest)

    pages = len(manifest["wiki"].get("pages", {}).get("stored", {}))
    print(
        f"\nDone. {len(manifest['owl'])} OWL files and {pages} wiki pages stored in {root}. {len(manifest['failures'])} failed."
    )


if __name__ == "__main__":
    main()
