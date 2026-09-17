"""Generate docs/processes/index.md and docs/processes/{category_id}.md (x19)."""

from __future__ import annotations

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


def _format_aliases(aliases: list) -> str:
    """Format a list of aliases (strings or dicts with name/note)."""
    parts = []
    for alias in aliases:
        if isinstance(alias, dict):
            name = alias.get("name", "")
            note = alias.get("note", "")
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
    out_of_scope = category.get("out_of_scope", "")
    issues = category.get("issues", "")
    history = category.get("history", "")
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

    if history:
        parts.append(":::{admonition} Category history\n")
        parts.append(":class: dropdown\n\n")
        parts.append(f"{history}\n")
        parts.append(":::\n\n")

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
