"""Generate docs/crossref.md - the task-process links in both directions.

Two tables: processes to tasks, one section per category, and tasks to processes. Every
figure is computed so the prose cannot drift from the data.
"""

from __future__ import annotations

from pathlib import Path

from generators.utils import process_link, table, task_link, write_page


def generate(
    docs_dir: Path,
    tasks: list[dict],
    processes: list[dict],
    categories: list[dict],
) -> int:
    """Write docs/crossref.md. Returns the number of files written."""
    processes_by_id = {p["process_id"]: p for p in processes}
    processes_by_category: dict[str, list[dict]] = {}
    for proc in processes:
        processes_by_category.setdefault(proc["category_id"], []).append(proc)

    sorted_categories = sorted(categories, key=lambda c: c["name"])
    sorted_tasks = sorted(tasks, key=lambda t: t["canonical_name"])
    n_links = sum(len(t.get("hed_process_ids", [])) for t in tasks)
    n_unlinked = sum(1 for p in processes if not p.get("tasks"))

    parts: list[str] = []
    parts.append("# Task-process links\n\n")
    parts.append(
        f"Every link between the {len(tasks)} tasks and {len(processes)} processes in the catalog, in both\n"
        f"directions: {n_links} links in all. A task is linked to a process when its inclusion test\n"
        "engages that process; the [process criteria](methods/process_criteria.md) say when a\n"
        "link is justified. The same links appear on the individual task and process pages;\n"
        "this page is the single place to see the whole matrix.\n\n"
    )

    parts.append("## Processes to tasks\n\n")
    parts.append(
        f"One section per category. {n_unlinked} processes are engaged by no task in the current\ncatalog and are marked as such.\n\n"
    )
    for cat in sorted_categories:
        cat_procs = sorted(processes_by_category.get(cat["category_id"], []), key=lambda p: p["process_name"])
        parts.append(f"### {cat['name']}\n\n")
        rows = []
        for proc in cat_procs:
            linked = sorted(proc.get("tasks", []), key=lambda t: t["canonical_name"])
            links = ", ".join(task_link(t["hedtsk_id"], t["canonical_name"]) for t in linked) or "*none*"
            rows.append([process_link(proc["process_id"], proc["process_name"], cat["category_id"]), links])
        parts.append(table(["Process", "Tasks"], rows))
        parts.append("\n\n")

    parts.append("## Tasks to processes\n\n")
    rows = []
    for task in sorted_tasks:
        links = []
        for pid in task.get("hed_process_ids", []):
            proc = processes_by_id.get(pid)
            links.append(process_link(pid, proc["process_name"], proc["category_id"]) if proc else f"`{pid}`")
        rows.append([task_link(task["hedtsk_id"], task["canonical_name"]), ", ".join(links) or "*none*"])
    parts.append(table(["Task", "Processes"], rows))
    parts.append("\n")

    write_page(docs_dir / "crossref.md", "".join(parts))
    return 1
