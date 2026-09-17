"""Generate docs/tasks/index.md and docs/tasks/hedtsk_*.md (one per task)."""

from __future__ import annotations

import sys
from pathlib import Path

from generators.utils import truncate, write_page


def generate(
    docs_dir: Path,
    tasks: list[dict],
    processes_by_id: dict[str, dict],
    atlas_map: dict[str, dict] | None = None,
) -> int:
    """Write the task index page and all individual task pages.

    Returns the number of files written.
    """
    tasks_dir = docs_dir / "tasks"
    sorted_tasks = sorted(tasks, key=lambda t: t["canonical_name"])

    count = 0
    count += _write_task_index(tasks_dir, sorted_tasks)
    for task in sorted_tasks:
        count += _write_task_page(tasks_dir, task, processes_by_id, atlas_map or {})
    return count


def _write_task_index(tasks_dir: Path, sorted_tasks: list[dict]) -> int:
    """Write docs/tasks/index.md."""
    lines = [
        "# Task catalog\n",
        "\n",
        f"This catalog contains {len(sorted_tasks)} standard cognitive and behavioral neuroscience tasks.\n",
        "Each task has a canonical definition, inclusion criteria, named variations,\n",
        "and links to the cognitive processes it engages.\n",
        "\n",
        "## Tasks\n",
        "\n",
        "| Task | Short Definition | Processes |\n",
        "|------|-----------------|----------|\n",
    ]

    for task in sorted_tasks:
        hedtsk_id = task["hedtsk_id"]
        name = task["canonical_name"]
        short_def = truncate(task.get("short_definition", ""), 100)
        # Escape pipe characters in cell text
        short_def = short_def.replace("|", "\\|")
        n_procs = len(task.get("hed_process_ids", []))
        lines.append(f"| [{name}]({hedtsk_id}.md) | {short_def} | {n_procs} |\n")

    lines.append("\n")
    lines.append("```{toctree}\n")
    lines.append(":hidden:\n")
    lines.append(":maxdepth: 1\n")
    lines.append("\n")
    for task in sorted_tasks:
        lines.append(f"{task['hedtsk_id']}\n")
    lines.append("```\n")

    write_page(tasks_dir / "index.md", "".join(lines))
    return 1


def _write_task_page(
    tasks_dir: Path,
    task: dict,
    processes_by_id: dict[str, dict],
    atlas_map: dict[str, dict],
) -> int:
    """Write an individual task page docs/tasks/{hedtsk_id}.md."""
    hedtsk_id = task["hedtsk_id"]
    canonical_name = task["canonical_name"]
    aliases = task.get("aliases", [])
    short_def = task.get("short_definition", "")
    description = task.get("description", "")
    inclusion = task.get("inclusion_test", {})
    variations = task.get("variations", [])
    hed_process_ids = task.get("hed_process_ids", [])
    key_refs = task.get("key_references", [])
    recent_refs = task.get("recent_references", [])
    # The curated mapping in .working/mappings/ is the authoritative Atlas
    # cross-reference. The legacy atlas_id on the task record is not used: several
    # of its values point at a different paradigm or at an id the Atlas no longer
    # has, which produced dead links on these pages.
    atlas_row = atlas_map.get(hedtsk_id) or {}
    atlas_id = atlas_row.get("atlas_id") or ""
    atlas_name = atlas_row.get("atlas_name") or ""
    atlas_match = atlas_row.get("match_type") or ""

    parts: list[str] = []

    # Cross-reference target + title
    parts.append(f"({hedtsk_id})=\n")
    parts.append(f"# {canonical_name}\n\n")

    parts.append(f"**HED Task ID:** `{hedtsk_id}`\n\n")

    if aliases:
        parts.append(f"**Also known as:** {', '.join(aliases)}\n\n")

    parts.append(f"{short_def}\n\n")

    # Description
    parts.append("## Description\n\n")
    parts.append(f"{description}\n\n")

    # Inclusion Test
    proc_text = inclusion.get("procedure", "")
    manip_text = inclusion.get("manipulation", "")
    meas_text = inclusion.get("measurement", "")

    parts.append("## Inclusion test\n\n")
    parts.append("```{list-table}\n")
    parts.append(":widths: 15 85\n")
    parts.append(":header-rows: 0\n")
    parts.append("\n")
    parts.append("* - **Procedure**\n")
    parts.append(f"  - {proc_text}\n")
    parts.append("* - **Manipulation**\n")
    parts.append(f"  - {manip_text}\n")
    parts.append("* - **Measurement**\n")
    parts.append(f"  - {meas_text}\n")
    parts.append("```\n\n")

    # Variations
    if variations:
        parts.append("## Variations\n\n")  # single word — already sentence case
        parts.append("```{list-table}\n")
        parts.append(":widths: 25 40 35\n")
        parts.append(":header-rows: 1\n")
        parts.append("\n")
        parts.append("* - Variation\n")
        parts.append("  - Description\n")
        parts.append("  - Justification\n")
        for var in variations:
            var_name = var.get("name", "")
            var_desc = var.get("description", "")
            var_just = var.get("justification", "")
            parts.append(f"* - {var_name}\n")
            parts.append(f"  - {var_desc}\n")
            parts.append(f"  - {var_just}\n")
        parts.append("```\n\n")

    # Cognitive processes
    if hed_process_ids:
        parts.append("## Cognitive processes\n\n")
        parts.append("This task engages the following cognitive processes:\n\n")
        for pid in hed_process_ids:
            proc = processes_by_id.get(pid)
            if proc is None:
                print(
                    f"WARNING: process '{pid}' referenced by task '{hedtsk_id}' not found in process_details.json",
                    file=sys.stderr,
                )
                parts.append(f"- {pid}\n")
            else:
                pname = proc["process_name"]
                cat_id = proc["category_id"]
                anchor = pid.replace("_", "-")
                parts.append(f"- [{pname}](../processes/{cat_id}.md#{anchor})\n")
        parts.append("\n")

    # Key references
    if key_refs:
        parts.append("## Key references\n\n")
        for ref in key_refs:
            parts.append(f"- {ref}\n")
        parts.append("\n")

    # Recent references
    if recent_refs:
        parts.append("## Recent references\n\n")
        for ref in recent_refs:
            parts.append(f"- {ref}\n")
        parts.append("\n")

    # External links
    if atlas_id:
        label = atlas_name or "Cognitive Atlas entry"
        qualifier = f" ({atlas_match} match)" if atlas_match and atlas_match != "exact" else ""
        parts.append("## External links\n\n")
        parts.append(f"- Cognitive Atlas: [{label}](https://www.cognitiveatlas.org/task/id/{atlas_id}){qualifier}\n")
        parts.append("\n")

    write_page(tasks_dir / f"{hedtsk_id}.md", "".join(parts))
    return 1
