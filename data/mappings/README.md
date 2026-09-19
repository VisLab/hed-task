# HED to Cognitive Atlas mappings

Four TSV tables, each keyed by a unique entity id, generated and refreshed by `src/build_atlas_maps.py` from the `.cog_data/` archive.

| File                       | Rows | Key                | Direction                    |
| -------------------------- | ---- | ------------------ | ---------------------------- |
| `hed_task_to_atlas.tsv`    | 103  | `hedtsk_id`        | HED task -> Atlas task       |
| `atlas_task_to_hed.tsv`    | 857  | `atlas_id`         | Atlas task -> HED task       |
| `hed_process_to_atlas.tsv` | 172  | `hed_process_id`   | HED process -> Atlas concept |
| `atlas_concept_to_hed.tsv` | 918  | `atlas_concept_id` | Atlas concept -> HED process |

A HED task often corresponds to several Atlas entries. The forward table holds the primary match; the reverse table holds every Atlas entry and the HED entity it maps to, so the fan-out lives there. Filter the reverse table by `hedtsk_id` to get all Atlas entries for one HED task.

## Columns

`match_type` is one of `exact`, `close`, `related`, `none`, or empty.

- `exact` - the same paradigm or construct under the same or an aliased name
- `close` - the same family, but the Atlas entry is a variant, is broader, or is narrower than the HED entry
- `related` - the Atlas has entries in the same area but none that corresponds
- `none` - nothing in the Atlas corresponds
- empty - not yet reviewed

`match_level` in `atlas_task_to_hed.tsv` is `task` or `variation`. A `variation` row resolves to a named variation of a HED task rather than the task itself, identified by `hed_variation_id` (for example `hedvar_stroop_color_word__counting_stroop`). The generator fails if that id does not exist or if its parent task disagrees with `hedtsk_id`.

`scope_class` in `atlas_task_to_hed.tsv` is rule-derived from the entry name (`paradigm`, `questionnaire`, `battery`, `imaging_protocol`, `physiological`). It is a heuristic, not a hand-checked judgement.

Atlas names are reproduced exactly as the API returns them, so a few contain a curly apostrophe or an en dash.

## Curation state

All four tables are curated. Every row carries a `match_type`, every matched row was checked against the archived Atlas record, and every `none` row carries a reason.

| Table                      | Rows | exact | close | related | none |
| -------------------------- | ---- | ----- | ----- | ------- | ---- |
| `hed_task_to_atlas.tsv`    | 103  | 70    | 11    | 4       | 18   |
| `atlas_task_to_hed.tsv`    | 857  | 86    | 73    | 24      | 674  |
| `hed_process_to_atlas.tsv` | 172  | 102   | 14    | 23      | 33   |
| `atlas_concept_to_hed.tsv` | 918  | 102   | 14    | 16      | 786  |

The two reverse tables hold fewer distinct matches than their forward counterparts because several HED entries share one Atlas record: both metacognitive processes map to `metacognition`, for instance. That is a property of the Atlas, not an error.

`scope_class` on unmatched Atlas task rows remains rule-derived. The `none` verdict itself was reviewed in every case.

## Editing

The TSVs are hand-editable and are the authoritative source for any generated view. `src/build_atlas_maps.py` never overwrites `match_type`, the mapped id, or `notes`. It refreshes the descriptive columns from the archive, re-deriving them from whichever id the curator chose, and reports entities added to or removed from the Atlas since the last run.
