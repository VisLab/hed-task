"""Generate docs/methodology/ -- how the catalog's derived artifacts are produced.

`atlas_mapping.md` documents the method behind `.working/mappings/`: where the data
comes from, what the match vocabulary means, how variations are identified, and what
is and is not verified. Counts are read from the mapping tables so the page cannot
drift from them.
"""

from __future__ import annotations

import collections
import csv
from pathlib import Path

from generators.utils import write_page


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


def _index_page() -> str:
    return """\
# Methodology

How the catalog's derived artifacts are produced, and what has been verified by hand
rather than generated automatically.

```{toctree}
:maxdepth: 2

atlas_mapping
```
"""


def _mapping_page(working: Path) -> str:
    maps = working / "mappings"
    forward = _read(maps / "hed_task_to_atlas.tsv")
    reverse = _read(maps / "atlas_task_to_hed.tsv")
    proc_forward = _read(maps / "hed_process_to_atlas.tsv")
    concept_reverse = _read(maps / "atlas_concept_to_hed.tsv")

    fwd_types = collections.Counter(r["match_type"] for r in forward)
    rev_types = collections.Counter(r["match_type"] for r in reverse)
    rev_levels = collections.Counter(r["match_level"] for r in reverse if r["match_level"])
    scope = collections.Counter(r["scope_class"] for r in reverse if r["match_type"] == "none")

    fwd_table = _table(
        ["Match type", "Tasks", "Share"],
        [[k, fwd_types[k], f"{round(100 * fwd_types[k] / len(forward))}%"] for k in ("exact", "close", "related", "none")],
    )
    rev_table = _table(
        ["Match type", "Atlas entries", "Share"],
        [[k, rev_types[k], f"{round(100 * rev_types[k] / len(reverse))}%"] for k in ("exact", "close", "related", "none")],
    )
    level_table = _table(
        ["Mapped to", "Atlas entries"],
        [["A HED task", rev_levels["task"]], ["A named variation of a HED task", rev_levels["variation"]]],
    )
    scope_table = _table(
        ["Why no counterpart", "Atlas entries"],
        [
            ["Experimental paradigm not in the 103-task catalog", scope["paradigm"]],
            ["Self-report instrument", scope["questionnaire"]],
            ["Standardized test battery", scope["battery"]],
            ["Imaging protocol label", scope["imaging_protocol"]],
            ["Physiological procedure", scope["physiological"]],
        ],
    )

    proc_types = collections.Counter(r["match_type"] for r in proc_forward)
    concept_types = collections.Counter(r["match_type"] for r in concept_reverse)
    proc_table = _table(
        ["Match type", "Processes", "Share"],
        [
            [k, proc_types[k], f"{round(100 * proc_types[k] / len(proc_forward))}%"]
            for k in ("exact", "close", "related", "none")
        ],
    )
    concept_table = _table(
        ["Match type", "Atlas concepts", "Share"],
        [
            [k, concept_types[k], f"{round(100 * concept_types[k] / len(concept_reverse))}%"]
            for k in ("exact", "close", "related", "none")
        ],
    )
    concepts_used = len({r["atlas_concept_id"] for r in proc_forward if r["atlas_concept_id"]})

    covered = len({r["hedtsk_id"] for r in reverse if r["hedtsk_id"]})
    variations_matched = len({r["hed_variation_id"] for r in reverse if r["hed_variation_id"]})

    return f"""\
# Mapping the catalog to the Cognitive Atlas

This page describes how the correspondence between this catalog and the
[Cognitive Atlas](https://www.cognitiveatlas.org/) was established, so that a reader
can judge how much weight each mapping carries.

## Source data

Every figure derives from a byte-exact archive of the Atlas REST API, taken in a single
snapshot covering both layers in full: {len(reverse)} tasks and {len(concept_reverse)}
concepts, with the detail record for each. Pulling the concept endpoint directly
matters, because a harvest taken from the task endpoint alone reaches a concept only
when some task asserts it, which hides about half the concept layer.

The mappings live in four tab-separated tables under `.working/mappings/` rather than
in these pages, so that any view can be generated from them. Each table has one row per
entity and a unique key. The [task crossref](../atlas/task_crossref.md) and
[process crossref](../atlas/process_crossref.md) pages render all four in full.

## What a match type means

{
        _table(
            ["Match type", "Meaning"],
            [
                ["`exact`", "The same paradigm or construct, under the same or an aliased name"],
                ["`close`", "The same family, but the Atlas entry is a variant, is broader, or is narrower"],
                ["`related`", "The Atlas has entries in the same area but none that corresponds"],
                ["`none`", "Nothing in the Atlas corresponds"],
            ],
        )
    }

`close` and `related` carry real information and should not be read as weak versions of
`exact`. `close` says a counterpart exists but its boundaries differ, so a researcher
looking for the canonical paradigm will find something usable. `related` says the
search will turn up neighbours only.

## Matching at two levels

The Atlas frequently registers a specific implementation as its own entry rather than
recording it under the parent paradigm: eight separate Stroop entries, eight n-back,
six fluency. Many of those correspond not to a task in this catalog but to a *named
variation* of one.

Each mapping row therefore records whether it resolves to a task or to a variation.

{level_table}

Variations are addressed by a stable identifier of the form
`hedvar_<parent slug>__<variation slug>`, for example
`hedvar_stroop_color_word__counting_stroop`. The prefix types the identifier the same
way `hedtsk_` marks a task and `hed_` marks a process. These ids were introduced for
this mapping: variations previously had a name and nothing else, so any reference to
one would have broken silently if the name were edited. The generator now fails if a
mapping row names a variation that no longer exists, or one whose parent task
disagrees with the row.

## How the tables were built

Candidate matches come from normalized name and alias comparison, with an exact
task-name match taking precedence over a variation-name match. That precedence is not
cosmetic: the Atlas entry `2-stage decision task` matches the Two-Stage Decision Task
by name while also matching a variation listed under another task, and only the first
reading is correct.

**Automated matching decides nothing on its own.** On this data it produces false
positives and false negatives in both directions. `Judgment-of-Learning` matched
`Judgment of Line Orientation` because both abbreviate to "JOL". `Heartbeat Detection`
matched `visual pursuit/tracking`. `Trail Making` matched nothing although the Atlas
carries `Trail Making Test A and B`. Every row was therefore checked against the
archived Atlas record before being accepted.

## Coverage, catalog to Atlas

One row per task in this catalog, recording its primary Atlas counterpart.

{fwd_table}

## Coverage, Atlas to catalog

One row per Atlas task entry. {covered} of the catalog's tasks have at least one Atlas
entry pointing at them, and {variations_matched} named variations are matched by an
Atlas entry of their own.

{rev_table}

Most Atlas entries have no counterpart here, which is expected rather than a gap: this
catalog admits only event-producing experimental paradigms, while the Atlas mixes those
with instruments of several other kinds.

{scope_table}

The kind assigned to an unmatched entry is derived from its name by rule and is a
heuristic, not a hand-checked judgement. The `none` verdict itself was reviewed.

## Reading the two directions together

The directions answer different questions and can differ without contradiction. The
catalog-to-Atlas table asks whether the Atlas contains a given paradigm; the
Atlas-to-catalog table asks, for each Atlas entry, whether this catalog covers it.

Three tasks are `none` in the first table yet appear in the second with `related` rows:
Self-Paced Reading, Sentence Comprehension and Virtual Radial Arm Maze. The Atlas has
no entry that *is* any of those paradigms, but it does hold adjacent entries
(`Eye tracking paradigms`, `syntactic task`, `Porteus maze test`). Both statements are
true.

## Coverage, processes and concepts

The same method was applied to the second axis: {len(proc_forward)} cognitive processes
against {len(concept_reverse)} Atlas concepts. This mapping was built from nothing. The
process catalog carries no Atlas concept identifier of any kind, so there was no prior
linkage to correct, only to construct.

{proc_table}

{concept_table}

{concepts_used} distinct Atlas concepts are used by the {proc_types["exact"] + proc_types["close"] + proc_types["related"]}
matched processes, because several processes share one Atlas record: both metacognitive
processes resolve to `metacognition`, for example.

The `related` verdict does most of the interesting work here. It marks the cases where
the Atlas carries only a broader parent: `Affective priming` against `priming`,
`Social perception` against `perception`, `Fine motor control` against `motor control`.
Recording those as `close` would overstate what the Atlas offers.

The `none` verdicts fall into two groups. Some are constructs the Atlas never
registered as concepts even though it registers them as tasks, such as `Antisaccade` and
`Reversal learning`. Others are vocabulary that post-dates the Atlas's curation, notably
`Model-based learning`, `Model-free learning` and the general form of reward prediction
error, for which the Atlas has only `monetary reward prediction error`.

Definitions, not names, decided these. The Atlas concept named `acoustic processing`
looks like an exact match for the process of the same name, but its definition describes
"signals propagated undersea, in the atmosphere" -- sonar, not audition -- so it is
recorded as `close` with that noted. `Perspective taking` matched `worldview` by name
alone and was reassigned to `theory of mind`.

## What is verified

{
        _table(
            ["Table", "Rows", "State"],
            [
                ["`hed_task_to_atlas.tsv`", len(forward), "Every row checked against the archived Atlas record"],
                ["`atlas_task_to_hed.tsv`", len(reverse), "Every row assigned a match type; every matched row checked"],
                ["`hed_process_to_atlas.tsv`", len(proc_forward), "Every row checked against the archived concept definition"],
                ["`atlas_concept_to_hed.tsv`", len(concept_reverse), "Every row assigned a match type"],
            ],
        )
    }

Two things in these tables are not hand-checked. The `scope_class` on an unmatched Atlas
task is derived from its name by rule. And the `none` verdicts on the reverse tables
assert only that no counterpart exists in a catalog of {len(forward)} tasks and
{len(proc_forward)} processes, which is the expected answer for most of an
{len(reverse)}-entry and {len(concept_reverse)}-concept corpus.

## Reproducing this

    python src/fetch_cog_data.py        # refresh the API archive in .cog_data/
    python src/build_atlas_maps.py      # refresh the mapping tables

The second command is non-destructive. It never overwrites a match type, a mapped id,
or a curator note. It refreshes the descriptive columns, re-deriving them from
whichever id the curator chose rather than from the automated candidate, and reports
entities that have appeared in or disappeared from the Atlas since the last run.
Running it twice leaves the tables byte-identical.
"""


def generate(docs_dir: Path, working_dir: Path) -> int:
    """Write docs/methodology/index.md and docs/methodology/atlas_mapping.md."""
    directory = docs_dir / "methodology"
    write_page(directory / "index.md", _index_page())
    write_page(directory / "atlas_mapping.md", _mapping_page(working_dir))
    return 2
