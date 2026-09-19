"""Generate docs/source/_generated/ - table fragments for the hand-written pages.

Narrative pages are plain Markdown that people edit directly. Where one of them needs a
table whose contents follow the data (the landing-page counts, the Atlas mapping
coverage), the table is written here as a fragment and the page pulls it in with

    ```{include} ../../_generated/mapping_task_forward.md
    ```

so that the prose around the table stays editable and the table stays current. Each
fragment is one Markdown table and nothing else. The directory is excluded from the
Sphinx document tree in conf.py; only includes read it.
"""

from __future__ import annotations

import collections
from pathlib import Path

from generators.utils import read_tsv, table, write_page

KINDS = ("exact", "close", "related", "none")


def _share_table(rows: list[dict], label: str) -> str:
    counts = collections.Counter(r["match_type"] for r in rows)
    return table(
        ["Match type", label, "Share"],
        [[k, counts[k], f"{round(100 * counts[k] / len(rows))}%"] for k in KINDS],
    )


def generate(
    docs_dir: Path, working_dir: Path, tasks: list[dict], processes: list[dict], categories: list[dict], families: list[dict]
) -> int:
    """Write every fragment. Returns the number of files written."""
    out = docs_dir / "_generated"
    maps = working_dir / "mappings"
    forward = read_tsv(maps / "hed_task_to_atlas.tsv")
    reverse = read_tsv(maps / "atlas_task_to_hed.tsv")
    proc_forward = read_tsv(maps / "hed_process_to_atlas.tsv")
    concept_reverse = read_tsv(maps / "atlas_concept_to_hed.tsv")

    linked = {pid for t in tasks for pid in t.get("hed_process_ids", [])}
    fragments = {
        "counts_table.md": table(
            ["What", "Count", "Where"],
            [
                ["Tasks", sum(1 for t in tasks if t.get("task_kind", "task") != "pseudo_task"), "[Tasks](tasks/index.md)"],
                [
                    "Pseudo tasks (rest, fixation and questionnaire blocks)",
                    sum(1 for t in tasks if t.get("task_kind") == "pseudo_task"),
                    "[Tasks](tasks/families/pseudo_tasks.md)",
                ],
                ["Paradigm families the tasks are filed under", len(families), "[Tasks](tasks/index.md)"],
                ["Named task variations", sum(len(t.get("variations", [])) for t in tasks), "on each task page"],
                ["Cognitive processes", len(processes), "[Cognitive processes](processes/index.md)"],
                ["Process categories", len(categories), "[Cognitive processes](processes/index.md)"],
                [
                    "Task-to-process links",
                    sum(len(t.get("hed_process_ids", [])) for t in tasks),
                    "[Task-process links](crossref.md)",
                ],
                [
                    "Processes engaged by at least one task",
                    sum(1 for p in processes if p["process_id"] in linked),
                    "[Task-process links](crossref.md)",
                ],
            ],
        ),
        "mapping_level.md": table(
            ["Mapped to", "Atlas entries"],
            [
                ["A HED task", sum(1 for r in reverse if r["match_level"] == "task")],
                ["A named variation of a HED task", sum(1 for r in reverse if r["match_level"] == "variation")],
            ],
        ),
        "mapping_task_forward.md": _share_table(forward, "Tasks"),
        "mapping_task_reverse.md": _share_table(reverse, "Atlas entries"),
        "mapping_task_reverse_scope.md": table(
            ["Why no counterpart", "Atlas entries"],
            [
                [label, sum(1 for r in reverse if r["match_type"] == "none" and r["scope_class"] == scope)]
                for scope, label in (
                    ("paradigm", f"Experimental paradigm not in the {len(forward)}-task catalog"),
                    ("questionnaire", "Self-report instrument"),
                    ("battery", "Standardized test battery"),
                    ("imaging_protocol", "Imaging protocol label"),
                    ("physiological", "Physiological procedure"),
                )
            ],
        ),
        "mapping_process_forward.md": _share_table(proc_forward, "Processes"),
        "mapping_process_reverse.md": _share_table(concept_reverse, "Atlas concepts"),
        "mapping_verified.md": table(
            ["Table", "Rows", "State"],
            [
                ["`hed_task_to_atlas.tsv`", len(forward), "Every row checked against the archived Atlas record"],
                ["`atlas_task_to_hed.tsv`", len(reverse), "Every row assigned a match type; every matched row checked"],
                ["`hed_process_to_atlas.tsv`", len(proc_forward), "Every row checked against the archived concept definition"],
                ["`atlas_concept_to_hed.tsv`", len(concept_reverse), "Every row assigned a match type"],
            ],
        ),
    }

    for name, body in fragments.items():
        write_page(out / name, body + "\n")
    return len(fragments)
