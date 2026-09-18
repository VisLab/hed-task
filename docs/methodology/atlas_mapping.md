# Mapping the catalog to the Cognitive Atlas

This page describes how the correspondence between this catalog and the
[Cognitive Atlas](https://www.cognitiveatlas.org/) was established, so that a reader
can judge how much weight each mapping carries.

## Source data

Every figure derives from a byte-exact archive of the Atlas REST API, taken in a single
snapshot covering both layers in full: 857 tasks and 918
concepts, with the detail record for each. Pulling the concept endpoint directly
matters, because a harvest taken from the task endpoint alone reaches a concept only
when some task asserts it, which hides about half the concept layer.

The mappings live in four tab-separated tables under `.working/mappings/` rather than
in these pages, so that any view can be generated from them. Each table has one row per
entity and a unique key. The [task crossref](../atlas/task_crossref.md) and
[process crossref](../atlas/process_crossref.md) pages render all four in full.

## What a match type means

| Match type | Meaning |
|---|---|
| `exact` | The same paradigm or construct, under the same or an aliased name |
| `close` | The same family, but the Atlas entry is a variant, is broader, or is narrower |
| `related` | The Atlas has entries in the same area but none that corresponds |
| `none` | Nothing in the Atlas corresponds |

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

| Mapped to | Atlas entries |
|---|---|
| A HED task | 163 |
| A named variation of a HED task | 20 |

Variations are addressed by a stable identifier of the form
`hedvar_<parent slug>__<variation slug>`, for example
`hedvar_stroop_color_word__counting_stroop`. The prefix types the identifier the same
way `hedtsk_` marks a task and `hed_` marks a process. The identifier is what makes a
variation referenceable: without one, a reference would have to name the variation, and
would break silently if that name were edited. The generator fails if a mapping row
names a variation that does not exist, or one whose parent task disagrees with the row.

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

| Match type | Tasks | Share |
|---|---|---|
| exact | 70 | 68% |
| close | 11 | 11% |
| related | 4 | 4% |
| none | 18 | 17% |

## Coverage, Atlas to catalog

One row per Atlas task entry. 88 of the catalog's tasks have at least one Atlas
entry pointing at them, and 17 named variations are matched by an
Atlas entry of their own.

| Match type | Atlas entries | Share |
|---|---|---|
| exact | 86 | 10% |
| close | 73 | 9% |
| related | 24 | 3% |
| none | 674 | 79% |

Most Atlas entries have no counterpart here, which is expected rather than a gap: this
catalog admits only event-producing experimental paradigms, while the Atlas mixes those
with instruments of several other kinds.

| Why no counterpart | Atlas entries |
|---|---|
| Experimental paradigm not in the 103-task catalog | 481 |
| Self-report instrument | 107 |
| Standardized test battery | 41 |
| Imaging protocol label | 26 |
| Physiological procedure | 19 |

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

The same method was applied to the second axis: 172 cognitive processes
against 918 Atlas concepts. This mapping was built from nothing. The
process catalog carries no Atlas concept identifier of any kind, so there was no prior
linkage to correct, only to construct.

| Match type | Processes | Share |
|---|---|---|
| exact | 102 | 59% |
| close | 14 | 8% |
| related | 23 | 13% |
| none | 33 | 19% |

| Match type | Atlas concepts | Share |
|---|---|---|
| exact | 102 | 11% |
| close | 14 | 2% |
| related | 16 | 2% |
| none | 786 | 86% |

132 distinct Atlas concepts are used by the 139
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

| Table | Rows | State |
|---|---|---|
| `hed_task_to_atlas.tsv` | 103 | Every row checked against the archived Atlas record |
| `atlas_task_to_hed.tsv` | 857 | Every row assigned a match type; every matched row checked |
| `hed_process_to_atlas.tsv` | 172 | Every row checked against the archived concept definition |
| `atlas_concept_to_hed.tsv` | 918 | Every row assigned a match type |

Two things in these tables are not hand-checked. The `scope_class` on an unmatched Atlas
task is derived from its name by rule. And the `none` verdicts on the reverse tables
assert only that no counterpart exists in a catalog of 103 tasks and
172 processes, which is the expected answer for most of an
857-entry and 918-concept corpus.

## Reproducing this

    python src/fetch_cog_data.py        # refresh the API archive in .cog_data/
    python src/build_atlas_maps.py      # refresh the mapping tables

The second command is non-destructive. It never overwrites a match type, a mapped id,
or a curator note. It refreshes the descriptive columns, re-deriving them from
whichever id the curator chose rather than from the automated candidate, and reports
entities that have appeared in or disappeared from the Atlas since the last run.
Running it twice leaves the tables byte-identical.
