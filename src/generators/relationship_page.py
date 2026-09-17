"""Generate docs/atlas/relationship.md -- how this catalog stands to the Atlas.

The short interpretive page. The per-row detail lives on the crossref pages and in
`.working/mappings/`; this one says what the correspondence adds up to. Every figure is
computed at generation time so the prose cannot drift from the data.
"""

from __future__ import annotations

import csv
import json
from pathlib import Path

from generators.utils import write_page

# Tasks added to the catalog by the 2026-04 gap analysis against the Atlas.
GAP_ANALYSIS_ADDITIONS = [
    "hedtsk_multi_armed_bandit",
    "hedtsk_two_stage_decision",
    "hedtsk_random_dot_kinematogram",
    "hedtsk_remember_know",
    "hedtsk_directed_forgetting",
    "hedtsk_think_no_think",
    "hedtsk_ravens_progressive_matrices",
    "hedtsk_artificial_grammar_learning",
    "hedtsk_contextual_cueing",
    "hedtsk_implicit_association",
    "hedtsk_false_belief",
    "hedtsk_sustained_attention_to_response",
    "hedtsk_psychological_refractory_period",
    "hedtsk_navon",
    "hedtsk_biological_motion_perception",
]


def _read(path: Path) -> list[dict]:
    if not path.exists():
        return []
    with path.open(encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def _table(headers: list[str], rows: list[list]) -> str:
    out = ["| " + " | ".join(headers) + " |", "|" + "|".join("---" for _ in headers) + "|"]
    for row in rows:
        out.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(out)


def _page(working: Path, atlas: dict) -> str:  # noqa: PLR0914 - many named figures
    maps = working / "mappings"
    forward = _read(maps / "hed_task_to_atlas.tsv")
    reverse = _read(maps / "atlas_task_to_hed.tsv")
    proc_forward = _read(maps / "hed_process_to_atlas.tsv")
    concept_reverse = _read(maps / "atlas_concept_to_hed.tsv")

    tasks = json.loads((working / "task_details.json").read_text(encoding="utf-8"))
    process_data = json.loads((working / "process_details.json").read_text(encoding="utf-8"))
    processes = process_data["processes"]

    n_tasks, n_processes = len(tasks), len(processes)
    n_categories = len(process_data["categories"])
    links = sum(len(t.get("hed_process_ids") or []) for t in tasks)
    mean_links = links / n_tasks
    variations = sum(len(t.get("variations") or []) for t in tasks)

    fwd_none = sum(1 for r in forward if r["match_type"] == "none")
    fwd_matched = n_tasks - fwd_none
    proc_none = sum(1 for r in proc_forward if r["match_type"] == "none")
    proc_matched = n_processes - proc_none

    matched_entries = [r for r in reverse if r["match_type"] != "none"]
    matched_counts = [int(r["atlas_concept_count"] or 0) for r in matched_entries]
    matched_mean = sum(matched_counts) / len(matched_counts)
    matched_zero = sum(1 for c in matched_counts if c == 0)

    rev_none = sum(1 for r in reverse if r["match_type"] == "none")
    rev_none_paradigm = sum(1 for r in reverse if r["match_type"] == "none" and r["scope_class"] == "paradigm")
    concept_none = sum(1 for r in concept_reverse if r["match_type"] == "none")

    atlas_tasks = atlas["tasks"]["total"]
    atlas_concepts = atlas["concepts"]["total"]
    atlas_mean = atlas["tasks"]["concept_link_mean"]
    atlas_orphans = atlas["concepts"]["orphans"]["total"]
    atlas_relations = atlas["concepts"]["relation_total"]
    contrasts = next(f for f in atlas["tasks"]["fields"] if f["label"] == "Contrasts")
    atlas_cited = atlas["tasks"]["cited"]
    atlas_cited_pct = atlas["tasks"]["cited_percent"]
    atlas_uncited = atlas["tasks"]["uncited"]

    by_id = {r["hedtsk_id"]: r for r in forward}
    gap_rows = [by_id[g] for g in GAP_ANALYSIS_ADDITIONS if g in by_id]
    gap_matched = sum(1 for r in gap_rows if r["match_type"] != "none")

    scale_table = _table(
        ["", "This catalog", "Cognitive Atlas"],
        [
            ["Experimental paradigms", n_tasks, atlas_tasks],
            ["Cognitive processes or concepts", n_processes, atlas_concepts],
            ["Links between the two", links, atlas["tasks"]["concept_link_total"]],
            ["Mean processes or concepts per paradigm", f"{mean_links:.2f}", f"{atlas_mean:.2f}"],
            ["Named variations", variations, "not modelled"],
            ["Mean named variations per paradigm", f"{variations / n_tasks:.1f}", "not modelled"],
        ],
    )

    coverage_table = _table(
        ["Direction", "Has a counterpart", "Does not"],
        [
            [
                f"[Tasks to Atlas](task_crossref.md) ({n_tasks})",
                fwd_matched,
                fwd_none,
            ],
            [
                f"[Processes to Atlas](process_crossref.md) ({n_processes})",
                proc_matched,
                proc_none,
            ],
            [
                f"[Atlas tasks to catalog](task_crossref.md) ({atlas_tasks})",
                len(matched_entries),
                rev_none,
            ],
            [
                f"[Atlas concepts to catalog](process_crossref.md) ({atlas_concepts})",
                len(concept_reverse) - concept_none,
                concept_none,
            ],
        ],
    )

    return f"""\
# This catalog and the Cognitive Atlas

The [Cognitive Atlas](https://www.cognitiveatlas.org/) was the starting corpus for this
catalog, and the two overlap heavily. They are not, however, the same kind of thing, and
reading one as a subset of the other gets the relationship wrong.

[What is in the Cognitive Atlas](cognitive_atlas.md) describes the Atlas on its own
terms. The [task](task_crossref.md) and [process](process_crossref.md) crossref pages
give the correspondence row by row, and the
[methodology](../methodology/atlas_mapping.md) page explains how each row was decided.
This page says what it all adds up to.

## Two resources doing different jobs

The Atlas is an open ontology covering the breadth of cognitive neuroscience, and it
admits anything a contributor thought worth recording: experimental paradigms alongside
rating scales, neuropsychological batteries, imaging protocol labels and physiological
procedures, all filed under the single heading "task".

This catalog admits only paradigms that produce event-structured data, because its
purpose is HED annotation of experimental events. That is a narrower and more specific
test, set out in the [task criteria](../criteria/task_criteria.md).

The difference in scale follows from the difference in purpose.

{scale_table}

Size is the least interesting difference. What matters is the density and the shape.
This catalog links each paradigm to {mean_links:.1f} processes on average against the
Atlas's {atlas_mean:.2f}, and it models named variations at {variations / n_tasks:.1f}
per paradigm, which the Atlas does not model at all: it registers each implementation as
a separate top-level entry instead.

## How much overlaps

{coverage_table}

Read down the first two rows for what the Atlas can tell you about this catalog, and the
last two for what this catalog covers of the Atlas.

The two large "does not" figures are not a gap. {rev_none} Atlas entries have no
counterpart here, but only {rev_none_paradigm} of those are experimental paradigms at
all; the rest are instruments this catalog deliberately excludes. Likewise
{concept_none} Atlas concepts have no process here, and about half the Atlas concept
layer ({atlas_orphans} of {atlas_concepts}) is asserted by no Atlas task either.

## What this catalog adds

For the {len(matched_entries)} Atlas entries that do correspond to something here, the
Atlas records on average {matched_mean:.2f} concepts each, and {matched_zero} of them
record none at all. Against that, every task in this catalog carries:

- an inclusion test stating procedure, manipulation and measurement, so that membership
  is decidable rather than a matter of name
- a curated list of named variations, each with a justification for why it is a
  variation and not a separate task
- verified references
- links to {n_processes} defined processes in {n_categories} categories, at
  {mean_links:.1f} per task

The Atlas carries citations on {atlas_cited} of its {atlas_tasks} task entries
({atlas_cited_pct}%), so references are not absent, but they are contributed rather than
curated: the remaining {atlas_uncited} entries have none, and nothing records how any of
them was checked. Inclusion tests and variations have no Atlas equivalent at all.

## What the Atlas has that this catalog does not

The traffic runs both ways, and the Atlas holds several things worth keeping in view.

- **Breadth.** {atlas_tasks} task entries and {atlas_concepts} concepts against
  {n_tasks} and {n_processes} here. For a construct this catalog does not cover, the
  Atlas usually has something.
- **A concept relation graph.** {atlas_relations} `KINDOF` and `PARTOF` edges between
  concepts. This catalog groups processes into categories but asserts no relations
  between them.
- **Stable, citable identifiers** for every entry, which this catalog now references
  directly in its mapping tables.
- **Contrasts.** {contrasts["entries"]} contrast definitions across
  {contrasts["tasks"]} tasks, the most reusable structured content the Atlas holds after
  the concept links.

## How the Atlas shaped this catalog

The influence is concrete. A gap analysis against the Atlas in April 2026 added
{len(gap_rows)} paradigms that the catalog had been missing, among them the multi-armed
bandit, the two-stage decision task, the random dot kinematogram, remember/know, and
Raven's Progressive Matrices. All {gap_matched} now map to an Atlas entry.

The reverse also holds. {fwd_none} tasks here have no Atlas counterpart at all, and
several are heavily used paradigms the Atlas simply never registered: the Mismatch
Negativity paradigm, the Dictator Game, Reading the Mind in the Eyes, Multiple Object
Tracking, and the Weapons Identification Task among them. The
[task crossref](task_crossref.md) lists all {fwd_none}.

Mismatch Negativity is the starkest: thousands of published studies, a candidate
clinical biomarker, and no Atlas entry at all.

## What the Atlas cannot be used for unchecked

The mapping could not be built by matching names, and the reason matters for anyone
planning to consume the Atlas programmatically. Names agree while meanings do not.
`Judgment-of-Learning` and `Judgment of Line Orientation` share an abbreviation. The
Atlas concept `acoustic processing` is defined as the propagation of signals "undersea,
in the atmosphere". `Perspective taking` matches `worldview` on word overlap alone.

Names also disagree while meanings agree: `Trail Making` finds nothing until you look
for `Trail Making Test A and B`, and `Navon` is filed as `global-local task`.

Every row in these mappings was therefore checked against the archived Atlas record.
That is the practical conclusion of the whole exercise: the Atlas is an excellent source
of candidate terms and stable identifiers, and a poor source of automatic answers.
"""


def generate(docs_dir: Path, working_dir: Path, atlas_data: dict) -> int:
    """Write docs/atlas/relationship.md."""
    write_page(docs_dir / "atlas" / "relationship.md", _page(working_dir, atlas_data))
    return 1
