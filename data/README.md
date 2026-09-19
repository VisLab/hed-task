# The catalog data

Everything the site is generated from lives here and is edited here, by pull request.

| File                    | What it holds                                                                                                  | Edited how                                                                                     |
| ----------------------- | -------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- |
| `task_details.json`     | The tasks: identifiers, names and aliases, definitions, inclusion tests, variations, process links, references | By hand, in a PR; validated by the schema and by `src/generate_docs.py`                        |
| `process_details.json`  | The processes and their categories: definitions, aliases, references, linked tasks                             | Same                                                                                           |
| `schemas/*.schema.json` | JSON Schemas (draft-07) for the two files above; editors that understand them flag shape errors as you type    | Rarely; when the record shape changes                                                          |
| `mappings/*.tsv`        | The curated correspondence with the Cognitive Atlas, one row per entity; see `mappings/README.md`              | By hand; `src/build_atlas_maps.py` refreshes the descriptive columns without touching curation |
| `atlas_summary.json`    | Statistics about the Cognitive Atlas snapshot, for the Atlas essays                                            | Recomputed by `src/build_atlas_data.py` from the archive                                       |
| `task_family_defs.tsv`  | The paradigm families: display order, name, scope                                                              | By hand                                                                                        |
| `task_families.tsv`     | Which family each task is filed under, and why                                                                 | By hand                                                                                        |

The two JSON files began as an export from the research workspace that found the citations (see `src/import_catalog.py`, kept as the record of that one-time migration). Since 2026-09-19 this directory is their home.

## Editing a task or process

1. Edit the JSON. Keep the file ASCII except inside recorded data (author names, titles), keep two-space indentation, and keep records in their existing order.
2. Run `python src/generate_docs.py`. It validates before writing: schema shape, unique identifiers, every `hed_process_ids` entry resolving to a process, every process's `tasks` list agreeing with the tasks that name it, `task_count` and the header counts, reference `roles` from the allowed vocabulary, and every variation carrying its derived `variation_id`. A failure names the record and writes nothing.
3. Commit the data and the regenerated pages together. CI regenerates and fails the PR if they disagree.

### Linking a task to a process

Add the process id to the task's `hed_process_ids`, and add the task to the process's `tasks` list (`{"hedtsk_id": ..., "canonical_name": ...}`) and bump its `task_count`. The validator checks that both sides agree.

### Adding a variation

Add `{name, description, justification}` to the task's `variations`, then run `python src/add_variation_ids.py` to assign the `variation_id` (or write it by hand as `hedvar_<task slug>__<variation slug>`; the validator will tell you the expected value).

### Adding a reference

A reference carries bibliographic fields, an `ids` block (`doi`, `pmid`, `openalex_id`, `pmcid`, `s2_id`, `arxiv_id`, any may be null), `oa_status`, a `citation_string`, and `roles`. Give every new reference a real role:

- `historical` for a paradigm-defining or foundational paper; it is published under "Key references" (tasks) or "Fundamental references" (processes)
- `review` for a review or meta-analysis, `experiment` for an empirical paper, `dataset` for a dataset paper, `other` when none fits

`unknown` is the legacy value on references imported before roles were curated; do not use it for new entries.

## Task families

A family groups tasks by what the participant does, not by which cognitive process the task is thought to measure. That is the same principle the task criteria use to decide whether two experiments are the same task: procedure first. The process catalog covers the other axis, so the two views cross-link rather than duplicate one another.

Every task is filed under exactly one family, which is what lets the site's sidebar nest the task pages. The assignment is a curation decision, and it is expected to change as the catalog grows. When a task genuinely spans two families the `rationale` column names the alternative.

`task_family_defs.tsv`

- `family_id` - snake_case identifier, used in page paths and anchors
- `order` - display order on the task index and in the sidebar
- `name` - display name, sentence case
- `scope` - one or two sentences saying what procedure the family covers and what is measured

`task_families.tsv`

- `hedtsk_id` - the task, as in `task_details.json`
- `family_id` - must exist in `task_family_defs.tsv`
- `confidence` - `high` when the filing is uncontroversial, `review` when a reasonable reader could file it elsewhere; the task index notes how many there are
- `rationale` - one line saying why the task is in this family, naming the alternative when `confidence` is `review`

`src/generate_docs.py` fails if a task has no family, a row names an unknown task or family, or a family has no tasks.
