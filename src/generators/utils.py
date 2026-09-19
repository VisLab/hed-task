"""Shared utility functions for the HED task catalog documentation generators."""

from __future__ import annotations

import csv
import json
from pathlib import Path


def load_json(path: Path) -> dict | list:
    """Load a JSON file with UTF-8 encoding."""
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def read_tsv(path: Path) -> list[dict]:
    """Read a tab-separated file with a header row into a list of dicts.

    Returns an empty list if the file does not exist.
    """
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_page(path: Path, content: str) -> None:
    """Write a UTF-8 text file, creating parent dirs as needed."""
    path.parent.mkdir(parents=True, exist_ok=True)
    # newline="" suppresses the Windows CRLF translation that would otherwise
    # conflict with the eol=lf policy in .gitattributes.
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(content)


def table(headers: list[str], rows: list[list]) -> str:
    """Render a GitHub-style Markdown table.

    Cells are converted with str(); callers escape pipes themselves where the
    content can contain them (see cell()).
    """
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(c) for c in row) + " |")
    return "\n".join(out)


def cell(value: str | None, empty: str = "-") -> str:
    """Escape a value for a Markdown table cell, substituting `empty` for blanks."""
    return (value or "").replace("|", "\\|").strip() or empty


def truncate(text: str, max_len: int = 100) -> str:
    """Truncate text to max_len characters, appending three dots if needed.

    Three ASCII dots rather than an ellipsis character: the generator writes ASCII
    only, and the truncated text is prose we produce, not recorded data.
    """
    if len(text) <= max_len:
        return text
    return text[:max_len].rstrip() + "..."


def split_references(record: dict) -> tuple[list[dict], list[dict]]:
    """Return (key, further) reference lists for a task or process record.

    The catalog stores one `references` list per record; a reference whose `roles`
    include `historical` is a paradigm-defining or foundational one and is published
    under "Key references" (tasks) or "Fundamental references" (processes). The rest are
    "Further references". Records in the older two-list shape (`key_references` or
    `fundamental_references` plus `recent_references`) are split the same way so that a
    catalog exported before the roles field existed still renders.
    """
    if "references" in record:
        refs = record.get("references") or []
        key = [r for r in refs if "historical" in (r.get("roles") or [])]
        further = [r for r in refs if "historical" not in (r.get("roles") or [])]
        return key, further
    key = list(record.get("key_references") or record.get("fundamental_references") or [])
    return key, list(record.get("recent_references") or [])


def citation_line(ref: dict) -> str:
    """Render one reference as its citation string followed by DOI and PubMed links.

    Identifiers are read from the `ids` block when present and from flat `doi` and
    `pmid` fields otherwise. The citation string is reproduced exactly as the source
    supplies it, since it is recorded bibliographic data.
    """
    citation = (ref.get("citation_string") or "").strip()
    ids = ref.get("ids") or {}
    doi = ids.get("doi") or ref.get("doi")
    pmid = ids.get("pmid") or ref.get("pmid")
    links = []
    if doi:
        links.append(f"[DOI](https://doi.org/{doi})")
    if pmid:
        links.append(f"[PubMed](https://pubmed.ncbi.nlm.nih.gov/{pmid}/)")
    return citation + (f" ({', '.join(links)})" if links else "")


def process_anchor(process_id: str) -> str:
    """Return the HTML anchor for a process on its category page.

    Sphinx normalises label underscores to hyphens in rendered HTML ids, so the label
    written into the category page and the anchor used in links must both use hyphens.
    """
    return process_id.replace("_", "-")


def task_link(hedtsk_id: str, name: str, from_dir: str = "") -> str:
    """Return a Markdown link to a task page.

    `from_dir` is the directory of the page containing the link, relative to docs/:
    "" for the docs root, "tasks" for a sibling task page, "processes" or "atlas" for
    pages one level down.
    """
    prefix = _prefix_to_root(from_dir)
    return f"[{name}]({prefix}tasks/{hedtsk_id}.md)"


def process_link(process_id: str, name: str, category_id: str, from_dir: str = "") -> str:
    """Return a Markdown link to a process anchor on its category page."""
    prefix = _prefix_to_root(from_dir)
    return f"[{name}]({prefix}processes/{category_id}.md#{process_anchor(process_id)})"


def _prefix_to_root(from_dir: str) -> str:
    depth = len([p for p in from_dir.split("/") if p])
    return "../" * depth
