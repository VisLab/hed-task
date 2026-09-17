"""Archive the Cognitive Atlas into .cog_data/ as byte-exact API responses.

This is a faithful archive, not an analysis. Every file is the raw body the server
returned, written unparsed: no pretty-printing, no re-encoding, no key reordering, no
field selection, no aggregation. That fidelity matters for this source in particular,
because the published data contains double-encoded UTF-8, raw HTML entities such as
`&#39;`, and definitions that are the literal string `None`. Re-serializing would
normalize away the very defects an analysis may need to see.

The API exposes three enumerable entity types. Everything else it models -- contrasts,
conditions, indicators, implementations, external datasets, batteries, citations,
concept classes, relationships, external links -- exists only nested inside detail
records, so fetching every detail is the only way to capture them, and it captures all
of them.

    python src/fetch_cog_data.py                 # full archive, resumable
    python src/fetch_cog_data.py --limit 5       # smoke test
    python src/fetch_cog_data.py --refresh       # re-fetch what is already stored

Layout::

    .cog_data/
        MANIFEST.json          one record per HTTP request
        README.md              provenance and refresh instructions
        listings/<kind>.json   raw body of GET /<kind>
        <kind>/<id>.json       raw body of GET /<kind>?id=<id>
"""

from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import time
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

API = "http://cognitiveatlas.org/api/v-alpha"
USER_AGENT = "hed-task-research/1.0 (+https://github.com/hed-standard/hed-task)"

# The three endpoints that can be enumerated. Probing found every other candidate
# (contrast, battery, theory, collection, assertion, citation, conceptclass, ...)
# returns HTTP 404 as a top-level resource.
KINDS = ("concept", "task", "disorder")

# Entity ids are opaque strings from the API. Refuse anything that is not a plain
# identifier rather than writing it to an unexpected path.
_SAFE_ID = re.compile(r"^[A-Za-z0-9_.-]+$")

DEFAULT_OUT = Path(__file__).parent.parent / ".cog_data"


def fetch(url: str, timeout: int = 60, retries: int = 4, pause: float = 2.0) -> tuple[bytes, int]:
    """GET a URL and return (raw body bytes, HTTP status), retrying transient failures."""
    last: Exception | None = None
    for attempt in range(retries):
        try:
            request = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.read(), response.status
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


def check_id_collisions(kind: str, ids: list[str]) -> None:
    """Refuse ids that would collide on a case-insensitive filesystem."""
    seen: dict[str, list[str]] = collections.defaultdict(list)
    for entity_id in ids:
        seen[entity_id.lower()].append(entity_id)
    clashes = {k: v for k, v in seen.items() if len(v) > 1}
    if clashes:
        raise SystemExit(f"{kind}: ids differ only by case and cannot be separate files on Windows: {clashes}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=DEFAULT_OUT)
    parser.add_argument("--limit", type=int, default=0, help="stop after N details per kind")
    parser.add_argument("--refresh", action="store_true", help="re-fetch details already stored")
    parser.add_argument("--delay", type=float, default=0.25, help="seconds between requests")
    args = parser.parse_args()

    root: Path = args.out
    (root / "listings").mkdir(parents=True, exist_ok=True)

    manifest: dict = {
        "source": API,
        "client": USER_AGENT,
        "started_on": datetime.now(timezone.utc).isoformat(timespec="seconds"),
        "note": ("Every file is the raw response body, byte for byte. Nothing is parsed, reformatted, filtered, or derived."),
        "listings": {},
        "entities": {},
        "failures": [],
    }

    for kind in KINDS:
        url = f"{API}/{kind}"
        print(f"Fetching listing {url} ...")
        body, status = fetch(url)
        listing_path = root / "listings" / f"{kind}.json"
        listing_path.write_bytes(body)

        # Parsed only to enumerate ids. The stored bytes are untouched.
        entries = json.loads(body.decode("utf-8"))
        ids = [e["id"] for e in entries if e.get("id")]
        check_id_collisions(kind, ids)
        for entity_id in ids:
            if not _SAFE_ID.match(entity_id):
                raise SystemExit(f"{kind}: unsafe id for a filename: {entity_id!r}")

        manifest["listings"][kind] = record(url, body, status, listing_path, root)
        manifest["listings"][kind]["entities_listed"] = len(entries)
        manifest["listings"][kind]["ids_usable"] = len(ids)
        print(f"  {len(entries)} {kind} entries, {len(body)} bytes")

        kind_dir = root / kind
        kind_dir.mkdir(parents=True, exist_ok=True)
        targets = ids[: args.limit] if args.limit else ids
        stored: dict[str, dict] = {}
        fetched = skipped = 0

        print(f"Fetching {len(targets)} {kind} detail records ...")
        for i, entity_id in enumerate(targets, 1):
            dest = kind_dir / f"{entity_id}.json"
            detail_url = f"{API}/{kind}?id={entity_id}"
            if dest.exists() and not args.refresh:
                # Already archived by an earlier run. Describe it from disk so the
                # manifest covers every stored file, not only this run's fetches.
                body = dest.read_bytes()
                entry = record(detail_url, body, 200, dest, root)
                entry["retrieved_on"] = "(earlier run)"
                stored[entity_id] = entry
                skipped += 1
                continue
            try:
                body, status = fetch(detail_url)
            except RuntimeError as exc:
                manifest["failures"].append({"kind": kind, "id": entity_id, "error": str(exc)})
                print(f"  [{i}/{len(targets)}] FAILED {entity_id}: {exc}")
                continue
            dest.write_bytes(body)
            stored[entity_id] = record(detail_url, body, status, dest, root)
            fetched += 1
            if fetched % 100 == 0:
                print(f"  [{i}/{len(targets)}] fetched {fetched}, skipped {skipped}")
            time.sleep(args.delay)

        manifest["entities"][kind] = {
            "fetched": fetched,
            "skipped": skipped,
            "stored": stored,
        }
        print(f"  {kind}: fetched {fetched}, skipped {skipped}")

    manifest["finished_on"] = datetime.now(timezone.utc).isoformat(timespec="seconds")
    (root / "MANIFEST.json").write_text(
        json.dumps(manifest, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )

    counts = "\n".join(
        f"| `{kind}` | {manifest['listings'][kind]['entities_listed']} | "
        f"{len(manifest['entities'][kind]['stored']) or manifest['entities'][kind]['skipped']} |"
        for kind in KINDS
    )
    (root / "README.md").write_text(
        f"""# Cognitive Atlas archive

Byte-exact archive of the [Cognitive Atlas](https://www.cognitiveatlas.org/) REST API
at `{API}`, taken {manifest["started_on"][:10]}.

Every file here is the raw response body as the server returned it. Nothing is parsed,
reformatted, filtered, or derived, so the archive preserves the source exactly,
including its double-encoded UTF-8, raw HTML entities, and definitions that are the
literal string `None`.

| Endpoint | Entities listed | Detail records stored |
|---|---|---|
{counts}

`contrast`, `battery`, `theory`, `collection`, `assertion`, `citation` and
`conceptclass` are not enumerable as top-level resources (all return HTTP 404). Those
objects appear only nested inside the detail records archived here.

## Layout

    MANIFEST.json          one record per HTTP request: url, status, bytes, sha256
    listings/<kind>.json   raw body of GET /<kind>
    <kind>/<id>.json       raw body of GET /<kind>?id=<id>

## Verifying

Each stored file has a `sha256` in `MANIFEST.json` covering the exact bytes on disk.

## Refreshing

    python src/fetch_cog_data.py            # resumable; skips what is already stored
    python src/fetch_cog_data.py --refresh  # re-fetch everything

This directory is untracked. It is not in git and has no backup.
""",
        encoding="utf-8",
        newline="\n",
    )

    total = sum(len(v["stored"]) for v in manifest["entities"].values())
    print(f"\nDone. {total} detail records stored in {root}. {len(manifest['failures'])} failed.")


if __name__ == "__main__":
    main()
