"""Generate docs/processes/index.md and docs/processes/{category_id}.md (x19)."""

from __future__ import annotations

import re
from pathlib import Path

from generators.utils import truncate, write_page


def generate(
    docs_dir: Path,
    processes: list[dict],
    categories: list[dict],
    tasks_by_id: dict[str, dict],
) -> int:
    """Write the process index page and all category pages.

    Returns the number of files written.
    """
    procs_dir = docs_dir / "processes"

    # Build per-category process lists
    processes_by_category: dict[str, list[dict]] = {}
    for proc in processes:
        cat_id = proc["category_id"]
        processes_by_category.setdefault(cat_id, []).append(proc)

    sorted_categories = sorted(categories, key=lambda c: c["name"])

    count = 0
    count += _write_process_index(procs_dir, sorted_categories, processes_by_category)
    for cat in sorted_categories:
        cat_procs = processes_by_category.get(cat["category_id"], [])
        count += _write_category_page(procs_dir, cat, cat_procs)
    return count


def _write_process_index(
    procs_dir: Path,
    sorted_categories: list[dict],
    processes_by_category: dict[str, list[dict]],
) -> int:
    """Write docs/processes/index.md."""
    total_procs = sum(len(v) for v in processes_by_category.values())
    n_cats = len(sorted_categories)

    lines: list[str] = [
        "# Process catalog\n",
        "\n",
        f"This catalog defines {total_procs} cognitive processes organized into {n_cats} categories.\n",
        "Each process has a definition, references, and links to the tasks that engage it.\n",
        "Of the 172 processes, 152 are linked to at least one task in the task catalog.\n",
        "\n",
        "## Categories\n",
        "\n",
        "| Category | Processes | Description |\n",
        "|----------|-----------|-------------|\n",
    ]

    for cat in sorted_categories:
        cat_id = cat["category_id"]
        name = cat["name"]
        scope = truncate(cat.get("scope", ""), 100)
        scope = scope.replace("|", "\\|")
        n_procs = len(processes_by_category.get(cat_id, []))
        lines.append(f"| [{name}]({cat_id}.md) | {n_procs} | {scope} |\n")

    lines.append("\n")
    lines.append("```{toctree}\n")
    lines.append(":hidden:\n")
    lines.append(":maxdepth: 1\n")
    lines.append("\n")
    for cat in sorted_categories:
        lines.append(f"{cat['category_id']}\n")
    lines.append("```\n")

    write_page(procs_dir / "index.md", "".join(lines))
    return 1


# Clauses in an alias note that record when something changed rather than what is true.
# A published page states the current state, so these are dropped; the source data in
# .working/ keeps them.
_RE_HISTORY_CLAUSE = re.compile(
    r"20\d{2}-\d{2}-\d{2}"
    r"|\bpre-reframe\b|\bpre-20\d{2}\b|\breframe\b"
    r"|\brenamed\b|\bmerged\b|\bdropped as separate\b|\bduplicate entry\b",
    re.IGNORECASE,
)


def _strip_history(note: str) -> str:
    """Remove dated or change-log clauses from an alias note, keeping the rest verbatim.

    Returns an empty string when the note was nothing but history.
    """
    if not note:
        return ""
    pieces = re.split(r"(?<=[.;])\s+", note.strip())
    kept = [p for p in pieces if not _RE_HISTORY_CLAUSE.search(p)]
    if len(kept) == len(pieces):
        return note
    if not kept:
        return ""
    repaired = []
    for i, piece in enumerate(kept):
        nxt = kept[i + 1] if i + 1 < len(kept) else None
        # A clause that ended mid-sentence now ends one, or leads a new one.
        if piece.endswith(";") and (nxt is None or nxt[:1].isupper()):
            piece = piece[:-1] + "."
        repaired.append(piece)
    text = " ".join(repaired).strip()
    text = text[0].upper() + text[1:]
    if not text.endswith("."):
        text += "."
    return text


_RE_BARE_DATE = re.compile(r"\s+(?:on\s+)?\d{4}-\d{2}-\d{2}\b")


def _strip_dates(text: str) -> str:
    """Remove date stamps but keep the surrounding clause.

    Used where the text is not sentence-shaped - a parenthetical inside `Out of scope`,
    for instance - and splitting it into clauses would break the punctuation.
    """
    return _RE_BARE_DATE.sub("", text) if text else text


def _format_aliases(aliases: list) -> str:
    """Format a list of aliases (strings or dicts with name/note)."""
    parts = []
    for alias in aliases:
        if isinstance(alias, dict):
            name = alias.get("name", "")
            note = _strip_history(alias.get("note", ""))
            if note:
                parts.append(f"**{name}** \u2014 {note}")
            else:
                parts.append(name)
        else:
            parts.append(str(alias))
    return "; ".join(parts)


def _write_category_page(
    procs_dir: Path,
    category: dict,
    cat_procs: list[dict],
) -> int:
    """Write docs/processes/{category_id}.md."""
    cat_id = category["category_id"]
    name = category["name"]
    scope = category.get("scope", "")
    out_of_scope = _strip_dates(category.get("out_of_scope", ""))
    # The issues field mixes live caveats with resolved-issue records; keep the caveats.
    issues = _strip_history(category.get("issues", ""))
    process_count = len(cat_procs)

    parts: list[str] = []

    parts.append(f"# {name}\n\n")
    parts.append(f"**Scope:** {scope}\n\n")

    if out_of_scope:
        parts.append(f"**Out of scope:** {out_of_scope}\n\n")

    if issues:
        parts.append(":::{note}\n")
        parts.append(f"**Open issues:** {issues}\n")
        parts.append(":::\n\n")

    # The `history` field in the source data is a change log for the category - what was
    # merged, dropped or renamed, with dates. A published page states what is true now,
    # so it is deliberately not rendered. The field is left in the source untouched.

    parts.append(f"This category contains {process_count} processes.\n\n")
    parts.append("---\n\n")

    sorted_procs = sorted(cat_procs, key=lambda p: p["process_name"])

    for proc in sorted_procs:
        proc_id = proc["process_id"]
        proc_name = proc["process_name"]
        definition = proc.get("definition", "")
        aliases = proc.get("aliases", [])
        tasks = proc.get("tasks", [])
        fund_refs = proc.get("fundamental_references", [])
        recent_refs = proc.get("recent_references", [])

        # Explicit anchor target for deep linking
        # Use hyphens so the Sphinx label registry entry matches the HTML id
        # (Sphinx normalises label underscores->hyphens in rendered HTML IDs).
        parts.append(f"({proc_id.replace('_', '-')})=\n")
        parts.append(f"## {proc_name}\n\n")
        parts.append(f"**Process ID:** `{proc_id}`\n\n")

        if aliases:
            parts.append(f"**Also known as:** {_format_aliases(aliases)}\n\n")

        parts.append(f"{definition}\n\n")

        if tasks:
            sorted_tasks = sorted(tasks, key=lambda t: t["canonical_name"])
            parts.append("### Tasks\n\n")
            parts.append("The following tasks engage this process:\n\n")
            for task in sorted_tasks:
                tid = task["hedtsk_id"]
                tname = task["canonical_name"]
                parts.append(f"- [{tname}](../tasks/{tid}.md)\n")
            parts.append("\n")
        else:
            parts.append("*No tasks in the current catalog are linked to this process.*\n\n")

        if fund_refs:
            parts.append("### Fundamental references\n\n")
            for ref in fund_refs:
                citation = ref.get("citation_string", "")
                if citation:
                    parts.append(f"- {citation}\n")
            parts.append("\n")

        if recent_refs:
            parts.append("### Recent references\n\n")
            for ref in recent_refs:
                citation = ref.get("citation_string", "")
                if citation:
                    parts.append(f"- {citation}\n")
            parts.append("\n")

        if proc is not sorted_procs[-1]:
            parts.append("---\n\n")

    write_page(procs_dir / f"{cat_id}.md", "".join(parts))
    return 1
