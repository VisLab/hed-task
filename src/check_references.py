"""Report references whose identifiers appear to belong to a different publication.

Every reference in the catalog carries a human-written ``citation_string`` and, when an
identifier was resolved, the bibliographic record that identifier points at (``title``,
``journal``, ``volume``, ``pages``, ``year``). When the two disagree, the identifier was
attached to the wrong work and the published DOI and PubMed links lead somewhere else.

The check is a heuristic and prints, it does not fail the build:

- task references are written in APA form and include the title, so the record's title
  words are expected to appear in the citation string;
- process references are short ("Zacks (2008) *Journal of Cognitive Neuroscience* 20:1-19"),
  so the record's journal, volume and first page are expected to appear instead;
- a record whose venue is a test database, a book series or a chapter while the citation
  is a journal article (or the reverse) is reported as well.

Usage (from the repo root, with the venv active)::

    python src/check_references.py            # human-readable report
    python src/check_references.py --json out.json

Exit status is 0 whether or not anything is reported. Run it after adding or changing a
reference, and before trusting a DOI that a tool filled in.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

REPO_ROOT = Path(__file__).parent.parent
DATA = REPO_ROOT / "data"

_STOP = {
    "the",
    "of",
    "and",
    "in",
    "a",
    "an",
    "for",
    "on",
    "to",
    "with",
    "from",
    "by",
    "at",
    "as",
    "is",
    "its",
    "into",
    "or",
    "not",
    "are",
    "than",
    "that",
    "this",
    "their",
    "toward",
    "towards",
    "between",
    "during",
    "journal",
    "review",
    "reviews",
    "research",
    "study",
    "studies",
    "effects",
    "effect",
    "role",
}


def _norm(text: str | None) -> str:
    text = unicodedata.normalize("NFKD", text or "").encode("ascii", "ignore").decode()
    return re.sub(r"[^a-z0-9]+", " ", text.lower()).strip()


def _words(text: str | None) -> list[str]:
    return [w for w in _norm(text).split() if len(w) > 3 and w not in _STOP]


def _first_page(pages: str | None) -> str:
    m = re.match(r"^\s*([A-Za-z]?\d+)", str(pages or ""))
    return m.group(1).lower() if m else ""


def _suspect(ref: dict, apa: bool) -> str:
    """Return a reason string if the record disagrees with the citation, else ''."""
    ids = ref.get("ids") or {}
    if not (ids.get("doi") or ids.get("pmid")):
        return ""
    cite = _norm(ref.get("citation_string"))
    if not cite:
        return ""
    reasons = []

    title_words = _words(ref.get("title"))
    if apa and title_words:
        hit = sum(1 for w in title_words if w in cite) / len(title_words)
        if hit < 0.5:
            reasons.append(f"title overlap {hit:.0%}")

    journal = ref.get("journal") or ""
    j_words = _words(journal)
    if j_words and not any(w in cite for w in j_words):
        # Allow common abbreviations: JEP for Journal of Experimental Psychology, etc.
        initials = "".join(w[0] for w in _norm(journal).split() if w not in {"of", "the", "and", "in"})
        if initials not in cite.replace(" ", ""):
            reasons.append(f"journal {journal!r} not in citation")

    # Online-first and print years differ by one for many articles; tolerate that.
    year = ref.get("year")
    if year:
        cited_years = [int(y) for y in re.findall(r"\b(1[6-9]\d\d|20\d\d)\b", cite)]
        if cited_years and not any(abs(y - int(year)) <= 1 for y in cited_years):
            reasons.append(f"year {year} not in citation")

    # A short citation is checked on volume and first page only when it gives them
    # ("22:1-75"); a chapter cited without pages offers nothing to compare.
    if not apa and re.search(r"\b\d+:\s*[a-z]?\d+", cite):
        first = _first_page(ref.get("pages"))
        vol = str(ref.get("volume") or "")
        if first and first not in cite:
            reasons.append(f"first page {first} not in citation")
        elif vol and not re.search(rf"\b{re.escape(vol)}\b", cite):
            reasons.append(f"volume {vol} not in citation")

    venue_type = (ref.get("venue_type") or "").lower()
    if journal.lower().startswith("psyctests") or venue_type in {"dataset"}:
        reasons.append(f"record is a {journal or venue_type} entry")

    return "; ".join(reasons)


def audit() -> list[dict]:
    tasks = json.loads((DATA / "task_details.json").read_text(encoding="utf-8"))
    procs = json.loads((DATA / "process_details.json").read_text(encoding="utf-8"))["processes"]
    out = []
    for kind, records, idf, apa in (("task", tasks, "hedtsk_id", True), ("process", procs, "process_id", False)):
        for rec in records:
            for i, ref in enumerate(rec.get("references", [])):
                reason = _suspect(ref, apa)
                doi = (ref.get("ids") or {}).get("doi") or ""
                if doi.startswith("10.1037//"):
                    reason = (reason + "; " if reason else "") + "double-slash DOI"
                if reason:
                    out.append(
                        {
                            "kind": kind,
                            "record": rec[idf],
                            "index": i,
                            "citation": ref.get("citation_string", ""),
                            "title": ref.get("title"),
                            "journal": ref.get("journal"),
                            "year": ref.get("year"),
                            "volume": ref.get("volume"),
                            "pages": ref.get("pages"),
                            "ids": ref.get("ids"),
                            "reason": reason,
                        }
                    )
    return out


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--json", type=Path, help="also write the findings to this file")
    args = ap.parse_args()
    findings = audit()
    for f in findings:
        print(f"{f['kind']} {f['record']} #{f['index']}: {f['reason']}")
        print(f"    cite : {f['citation'][:110]}")
        print(
            f"    rec  : {str(f['title'])[:60]!r} | {f['journal']} {f['volume']}:{f['pages']} ({f['year']}) | doi={f['ids'].get('doi')}"
        )
    print(f"\n{len(findings)} suspicious references")
    if args.json:
        args.json.write_text(json.dumps(findings, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    return 0


if __name__ == "__main__":
    sys.exit(main())
