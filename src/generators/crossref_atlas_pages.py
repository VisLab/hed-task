"""Generate the Atlas mapping-table pages from data/mappings/.

Two reference pages, one per axis, each rendering both directions in full. The TSVs are
the source of record; these pages are one view of them and hold no judgements of their
own.

Rows are rendered in full rather than summarized, so that a reader can look up any
single task, process, Atlas entry or Atlas concept without opening the data files. The
unmatched side of each reverse table is grouped by why no counterpart exists, which
keeps several hundred rows navigable.
"""

from __future__ import annotations

import collections
from pathlib import Path

from generators.utils import cell as _cell
from generators.utils import read_tsv as _read
from generators.utils import table as _table
from generators.utils import write_page

MATCH_ORDER = {"exact": 0, "close": 1, "related": 2, "none": 3}

# The ten top-level concept classes of the Cognitive Atlas ontology.
CONCEPT_CLASSES = {
    "ctp_C1": "Perception",
    "ctp_C2": "Attention",
    "ctp_C3": "Reasoning and Decision Making",
    "ctp_C4": "Executive/Cognitive Control",
    "ctp_C5": "Learning and Memory",
    "ctp_C6": "Language",
    "ctp_C7": "Action",
    "ctp_C8": "Emotion",
    "ctp_C9": "Social Function",
    "ctp_C10": "Motivation",
    "": "(none)",
}

SCOPE_HEADINGS = {
    "paradigm": "Experimental paradigms not in the task catalog",
    "questionnaire": "Rating scales, questionnaires and inventories",
    "battery": "Standardized tests and batteries",
    "imaging_protocol": "Imaging protocol labels",
    "physiological": "Physiological procedures",
}


def _task_link(hedtsk_id: str, name: str) -> str:
    if not hedtsk_id:
        return "-"
    return f"[{_cell(name)}](../tasks/{hedtsk_id}.md)"


def _process_link(process_id: str, name: str, category_id: str) -> str:
    if not process_id:
        return "-"
    anchor = process_id.replace("_", "-")
    return f"[{_cell(name)}](../processes/{category_id}.md#{anchor})"


def _counts_line(rows: list[dict]) -> str:
    counts = collections.Counter(r["match_type"] for r in rows)
    parts = [f"{counts[k]} {k}" for k in ("exact", "close", "related", "none") if counts[k]]
    return ", ".join(parts)


# ---------------------------------------------------------------------------


def _task_page(maps: Path) -> str:
    forward = _read(maps / "hed_task_to_atlas.tsv")
    reverse = _read(maps / "atlas_task_to_hed.tsv")

    forward_rows = [
        [
            _task_link(r["hedtsk_id"], r["hed_task_name"]),
            f"`{r['match_type']}`",
            _cell(r["atlas_name"]),
            f"`{r['atlas_id']}`" if r["atlas_id"] else "-",
            _cell(r["atlas_def_chars"]),
            _cell(r["atlas_concept_count"]),
            _cell(r["notes"]),
        ]
        for r in sorted(forward, key=lambda r: r["hed_task_name"].lower())
    ]

    matched = [r for r in reverse if r["match_type"] != "none"]
    matched.sort(key=lambda r: (r["hed_task_name"].lower(), MATCH_ORDER[r["match_type"]], r["atlas_name"].lower()))
    matched_rows = [
        [
            _cell(r["atlas_name"]),
            f"`{r['atlas_id']}`",
            f"`{r['match_type']}`",
            _task_link(r["hedtsk_id"], r["hed_task_name"]),
            f"`{r['hed_variation_id']}`" if r["hed_variation_id"] else "-",
            _cell(r["notes"]),
        ]
        for r in matched
    ]

    unmatched = [r for r in reverse if r["match_type"] == "none"]
    by_scope: dict[str, list[dict]] = collections.defaultdict(list)
    for row in unmatched:
        by_scope[row["scope_class"]].append(row)

    sections = []
    for scope in ("paradigm", "questionnaire", "battery", "imaging_protocol", "physiological"):
        group = sorted(by_scope.get(scope, []), key=lambda r: r["atlas_name"].lower())
        if not group:
            continue
        rows = [
            [_cell(r["atlas_name"]), f"`{r['atlas_id']}`", _cell(r["atlas_def_chars"]), _cell(r["atlas_concept_count"])]
            for r in group
        ]
        sections.append(
            f"### {SCOPE_HEADINGS[scope]} ({len(group)})\n\n"
            + _table(["Atlas entry", "Atlas ID", "Definition chars", "Concepts"], rows)
        )

    variations = len({r["hed_variation_id"] for r in reverse if r["hed_variation_id"]})
    covered = len({r["hedtsk_id"] for r in reverse if r["hedtsk_id"]})

    return f"""\
# Task mapping tables

Every correspondence between the {len(forward)} tasks in this catalog and the
{len(reverse)} task entries in the Cognitive Atlas, in both directions. The
[methodology](../methods/atlas_mapping/index.md) page explains what the match types mean
and how each row was decided.

The source of record is `data/mappings/`, not this page.

Atlas entry names are reproduced exactly as the API returns them. A few carry a curly
apostrophe or an en dash, and one (`Penn` + a mis-encoded apostrophe + `s Logical
Reasoning Test`) carries a double-encoding defect present in the Atlas itself. These are
left uncorrected so that a name here matches the source byte for byte.

## Catalog to Atlas

One row per task in this catalog: {_counts_line(forward)}.

{
        _table(
            ["Task", "Match", "Atlas entry", "Atlas ID", "Definition chars", "Concepts", "Notes"],
            forward_rows,
        )
    }

## Atlas to catalog, matched entries

{len(matched)} Atlas entries correspond to something in this catalog, covering
{covered} of its {len(forward)} tasks. {variations} of them resolve to a named variation
rather than to the task itself, which is how the Atlas's habit of registering each
implementation separately is absorbed.

{
        _table(
            ["Atlas entry", "Atlas ID", "Match", "Task", "Variation", "Notes"],
            matched_rows,
        )
    }

## Atlas to catalog, entries with no counterpart

The remaining {len(unmatched)} Atlas entries have no counterpart here. Most are not
experimental paradigms at all; the rest are paradigms this catalog does not cover. The
grouping below is derived from each entry's name by rule, so treat it as an aid to
navigation rather than a classification.

{chr(10).join(sections)}
"""


def _process_page(maps: Path) -> str:
    forward = _read(maps / "hed_process_to_atlas.tsv")
    reverse = _read(maps / "atlas_concept_to_hed.tsv")
    category_of = {r["hed_process_id"]: r["hed_category_id"] for r in forward}

    forward_rows = [
        [
            _process_link(r["hed_process_id"], r["hed_process_name"], r["hed_category_id"]),
            f"`{r['match_type']}`",
            _cell(r["atlas_concept_name"]),
            f"`{r['atlas_concept_id']}`" if r["atlas_concept_id"] else "-",
            _cell(CONCEPT_CLASSES.get(r["atlas_concept_class"], r["atlas_concept_class"])),
            _cell(r["atlas_task_count"]),
            _cell(r["notes"]),
        ]
        for r in sorted(forward, key=lambda r: r["hed_process_name"].lower())
    ]

    matched = [r for r in reverse if r["match_type"] != "none"]
    matched.sort(key=lambda r: (r["hed_process_name"].lower(), r["atlas_concept_name"].lower()))
    matched_rows = [
        [
            _cell(r["atlas_concept_name"]),
            f"`{r['atlas_concept_id']}`",
            f"`{r['match_type']}`",
            _process_link(r["hed_process_id"], r["hed_process_name"], category_of.get(r["hed_process_id"], "")),
            _cell(r["atlas_task_count"]),
            _cell(r["relation_count"]),
        ]
        for r in matched
    ]

    unmatched = sorted(
        (r for r in reverse if r["match_type"] == "none"),
        key=lambda r: r["atlas_concept_name"].lower(),
    )
    unmatched_rows = [
        [
            _cell(r["atlas_concept_name"]),
            f"`{r['atlas_concept_id']}`",
            _cell(CONCEPT_CLASSES.get(r["atlas_concept_class"], r["atlas_concept_class"])),
            _cell(r["atlas_task_count"]),
            _cell(r["relation_count"]),
        ]
        for r in unmatched
    ]

    used = len({r["atlas_concept_id"] for r in forward if r["atlas_concept_id"]})

    return f"""\
# Process mapping tables

Every correspondence between the {len(forward)} cognitive processes in this catalog and
the {len(reverse)} concepts in the Cognitive Atlas, in both directions. The
[methodology](../methods/atlas_mapping/index.md) page explains what the match types mean
and how each row was decided.

The source of record is `data/mappings/`, not this page.

## Catalog to Atlas

One row per process in this catalog: {_counts_line(forward)}. `Atlas tasks` counts the
Atlas task entries that assert the matched concept, which is a rough measure of how
much use the Atlas makes of it.

{
        _table(
            ["Process", "Match", "Atlas concept", "Concept ID", "Atlas class", "Atlas tasks", "Notes"],
            forward_rows,
        )
    }

## Atlas to catalog, matched concepts

{len(matched)} Atlas concepts correspond to a process here, drawn on by {used} distinct
concept records. The count is lower than the number of matched processes because
several processes resolve to the same Atlas concept.

{
        _table(
            ["Atlas concept", "Concept ID", "Match", "Process", "Atlas tasks", "Relations"],
            matched_rows,
        )
    }

## Atlas to catalog, concepts with no counterpart

{len(unmatched)} Atlas concepts have no process in this catalog. Roughly half of the
Atlas concept layer is asserted by no task either, so a concept appearing here is not
evidence that it matters to anyone.

{
        _table(
            ["Atlas concept", "Concept ID", "Atlas class", "Atlas tasks", "Relations"],
            unmatched_rows,
        )
    }
"""


def generate(docs_dir: Path, working_dir: Path) -> int:
    """Write docs/atlas/task_mapping.md and docs/atlas/process_mapping.md."""
    maps = working_dir / "mappings"
    atlas_dir = docs_dir / "atlas"
    write_page(atlas_dir / "task_mapping.md", _task_page(maps))
    write_page(atlas_dir / "process_mapping.md", _process_page(maps))
    return 2
