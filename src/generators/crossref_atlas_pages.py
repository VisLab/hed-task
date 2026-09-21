"""Generate the Atlas mapping table fragments in docs/source/_generated/ from data/mappings/.

The hand-written pages docs/source/atlas/task_mapping.md and process_mapping.md carry
the prose and pull these fragments in with an include directive, so that the tables
stay current while the explanation around them stays editable. The TSVs are the source
of record; the fragments are one view of them and hold no judgements of their own.

Fragments written (each one Markdown table, one run of headed tables, or one sentence):

- atlas_task_forward.md            one row per task: its primary Atlas counterpart
- atlas_task_matched.md            one row per Atlas task entry with a counterpart
- atlas_task_unmatched.md          Atlas task entries with no counterpart, grouped by
                                   why (### heading per group)
- mapping_task_matched_line.md     one sentence with the matched-entry counts
- atlas_process_forward.md         one row per process: its primary Atlas concept
- atlas_process_matched.md         one row per Atlas concept with a counterpart
- atlas_process_unmatched.md       Atlas concepts with no counterpart
- mapping_process_matched_line.md  one sentence with the matched-concept counts

Rows are rendered in full rather than summarized, so that a reader can look up any
single task, process, Atlas entry or Atlas concept without opening the data files.
Links inside a fragment are relative to the including page (docs/source/atlas/), as
MyST parses an included fragment as part of the including document.
"""

from __future__ import annotations

import collections
from pathlib import Path

from generators.utils import cell as _cell
from generators.utils import read_tsv as _read
from generators.utils import table as _table
from generators.utils import write_page

MATCH_ORDER = {"exact": 0, "close": 1, "related": 2, "none": 3}

# Atlas record pages. An entry or concept name in a table links to its record, which is
# where the identifier lives; the identifier is not shown as a column of its own.
ATLAS_TASK_URL = "https://www.cognitiveatlas.org/task/id/"
ATLAS_CONCEPT_URL = "https://www.cognitiveatlas.org/concept/id/"

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
    "paradigm": "Experimental paradigms not in the Catalog",
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


def _atlas_link(name: str, atlas_id: str, base_url: str) -> str:
    """Return the Atlas entry or concept name linked to its record, or "-" when there is none.

    One Atlas task record has an identifier but a blank name; the identifier is the label
    then, so the row stays identifiable.
    """
    if not atlas_id:
        return "-"
    label = _cell(name, empty=f"`{atlas_id}`")
    return f"[{label}]({base_url}{atlas_id})"


def _plural(n: int, noun: str) -> str:
    return f"{n} {noun}{'' if n == 1 else 's'}"


# ---------------------------------------------------------------------------


def _task_fragments(maps: Path) -> dict[str, str]:
    """Return the task-axis fragments keyed by file name."""
    forward = _read(maps / "hed_task_to_atlas.tsv")
    reverse = _read(maps / "atlas_task_to_hed.tsv")

    forward_rows = [
        [
            _task_link(r["hedtsk_id"], r["hed_task_name"]),
            f"`{r['match_type']}`",
            _atlas_link(r["atlas_name"], r["atlas_id"], ATLAS_TASK_URL),
            _cell(r["notes"]),
        ]
        for r in sorted(forward, key=lambda r: r["hed_task_name"].lower())
    ]

    matched = [r for r in reverse if r["match_type"] != "none"]
    matched.sort(key=lambda r: (r["hed_task_name"].lower(), MATCH_ORDER[r["match_type"]], r["atlas_name"].lower()))
    matched_rows = [
        [
            _atlas_link(r["atlas_name"], r["atlas_id"], ATLAS_TASK_URL),
            f"`{r['match_type']}`",
            _task_link(r["hedtsk_id"], r["hed_task_name"]),
            _cell(r["hed_variation_name"]),
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
            [
                _atlas_link(r["atlas_name"], r["atlas_id"], ATLAS_TASK_URL),
                _cell(r["atlas_def_chars"]),
                _cell(r["atlas_concept_count"]),
            ]
            for r in group
        ]
        sections.append(
            f"### {SCOPE_HEADINGS[scope]} ({len(group)})\n\n" + _table(["Atlas entry", "Definition chars", "Concepts"], rows)
        )

    variations = len({r["hed_variation_id"] for r in reverse if r["hed_variation_id"]})
    covered = len({r["hedtsk_id"] for r in reverse if r["hedtsk_id"]})
    matched_line = (
        f"{_plural(len(matched), 'Atlas entry').replace('entrys', 'entries')} correspond to something in the "
        f"Catalog, covering {covered} of its {len(forward)} tasks; {variations} of them resolve to a named "
        "variation rather than to the task itself, which is how the Atlas's habit of registering each "
        "implementation separately is absorbed."
    )

    return {
        "atlas_task_forward.md": _table(["Task", "Match", "Atlas entry", "Notes"], forward_rows),
        "atlas_task_matched.md": _table(["Atlas entry", "Match", "Task", "Variation", "Notes"], matched_rows),
        "atlas_task_unmatched.md": "\n\n".join(sections),
        "mapping_task_matched_line.md": matched_line,
    }


def _process_fragments(maps: Path) -> dict[str, str]:
    """Return the process-axis fragments keyed by file name."""
    forward = _read(maps / "hed_process_to_atlas.tsv")
    reverse = _read(maps / "atlas_concept_to_hed.tsv")
    category_of = {r["hed_process_id"]: r["hed_category_id"] for r in forward}

    forward_rows = [
        [
            _process_link(r["hed_process_id"], r["hed_process_name"], r["hed_category_id"]),
            f"`{r['match_type']}`",
            _atlas_link(r["atlas_concept_name"], r["atlas_concept_id"], ATLAS_CONCEPT_URL),
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
            _atlas_link(r["atlas_concept_name"], r["atlas_concept_id"], ATLAS_CONCEPT_URL),
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
            _atlas_link(r["atlas_concept_name"], r["atlas_concept_id"], ATLAS_CONCEPT_URL),
            _cell(CONCEPT_CLASSES.get(r["atlas_concept_class"], r["atlas_concept_class"])),
            _cell(r["atlas_task_count"]),
            _cell(r["relation_count"]),
        ]
        for r in unmatched
    ]

    n_matched_procs = sum(1 for r in forward if r["match_type"] != "none")
    matched_line = (
        f"{len(matched)} Atlas concepts correspond to a process in the Catalog, and between them they serve "
        f"{n_matched_procs} matched processes, because several processes resolve to the same Atlas concept: "
        "both metacognitive processes resolve to `metacognition`, for example."
    )

    return {
        "atlas_process_forward.md": _table(
            ["Process", "Match", "Atlas concept", "Atlas class", "Atlas tasks", "Notes"], forward_rows
        ),
        "atlas_process_matched.md": _table(["Atlas concept", "Match", "Process", "Atlas tasks", "Relations"], matched_rows),
        "atlas_process_unmatched.md": _table(["Atlas concept", "Atlas class", "Atlas tasks", "Relations"], unmatched_rows),
        "mapping_process_matched_line.md": matched_line,
    }


def generate(docs_dir: Path, working_dir: Path) -> int:
    """Write the Atlas mapping fragments to docs/source/_generated/. Returns the number written."""
    maps = working_dir / "mappings"
    out = docs_dir / "_generated"
    fragments = {**_task_fragments(maps), **_process_fragments(maps)}
    for name, body in fragments.items():
        write_page(out / name, body.rstrip("\n") + "\n")
    return len(fragments)
