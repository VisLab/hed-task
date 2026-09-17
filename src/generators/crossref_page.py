"""Generate docs/crossref.md - bidirectional cross-reference."""

from __future__ import annotations

from pathlib import Path

from generators.utils import write_page


def generate(
    docs_dir: Path,
    tasks: list[dict],
    processes: list[dict],
    categories: list[dict],
) -> int:
    """Write docs/crossref.md.

    Returns the number of files written.
    """
    # Build lookup structures
    processes_by_id: dict[str, dict] = {p["process_id"]: p for p in processes}
    processes_by_category: dict[str, list[dict]] = {}
    for proc in processes:
        processes_by_category.setdefault(proc["category_id"], []).append(proc)

    sorted_categories = sorted(categories, key=lambda c: c["name"])
    sorted_tasks = sorted(tasks, key=lambda t: t["canonical_name"])

    parts: list[str] = []
    parts.append("# Cross-reference: tasks and processes\n\n")
    parts.append(
        "This page provides bidirectional cross-references between the 103 tasks\nand 172 processes in the HED catalog.\n\n"
    )

    # --- Section 1: Processes by Category -> Tasks ---
    parts.append("## Processes by category \u2192 tasks\n\n")

    for cat in sorted_categories:
        cat_id = cat["category_id"]
        cat_name = cat["name"]
        cat_procs = sorted(
            processes_by_category.get(cat_id, []),
            key=lambda p: p["process_name"],
        )

        parts.append(f"### {cat_name}\n\n")

        for proc in cat_procs:
            proc_id = proc["process_id"]
            proc_name = proc["process_name"]
            linked_tasks = proc.get("tasks", [])
            sorted_linked = sorted(linked_tasks, key=lambda t: t["canonical_name"])

            parts.append(f"**{proc_name}** (`{proc_id}`)\n")
            if sorted_linked:
                task_links = ", ".join(f"[{t['canonical_name']}](tasks/{t['hedtsk_id']}.md)" for t in sorted_linked)
                parts.append(f": {task_links}\n\n")
            else:
                parts.append(": *No tasks linked.*\n\n")

    # --- Section 2: Tasks -> Processes ---
    parts.append("## Tasks \u2192 processes\n\n")

    for task in sorted_tasks:
        hedtsk_id = task["hedtsk_id"]
        canonical_name = task["canonical_name"]
        hed_process_ids = task.get("hed_process_ids", [])

        parts.append(f"**{canonical_name}** (`{hedtsk_id}`)\n")
        if hed_process_ids:
            proc_links = []
            for pid in hed_process_ids:
                proc = processes_by_id.get(pid)
                if proc:
                    pname = proc["process_name"]
                    cat_id = proc["category_id"]
                    anchor = pid.replace("_", "-")
                    proc_links.append(f"[{pname}](processes/{cat_id}.md#{anchor})")
                else:
                    proc_links.append(pid)
            parts.append(f": {', '.join(proc_links)}\n\n")
        else:
            parts.append(": *No processes linked.*\n\n")

    write_page(docs_dir / "crossref.md", "".join(parts))
    return 1
