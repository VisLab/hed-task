# HED to Cognitive Atlas mappings

Four TSV tables, each keyed by a unique entity id, generated and refreshed by `src/build_atlas_maps.py` from the `.cog_data/` archive.

| File                       | Rows | Key                | Direction                    |
| -------------------------- | ---- | ------------------ | ---------------------------- |
| `hed_task_to_atlas.tsv`    | 110  | `hedtsk_id`        | HED task -> Atlas task       |
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

`match_level` in `atlas_task_to_hed.tsv` and `cogpo_paradigm_to_hed.tsv` is `task` or `variant`. A `variant` row resolves to a variant of a HED task rather than the task itself, identified by `hed_variant_id` (for example `hedvar_stroop_color_word__counting_stroop`), with the variant's name in `hed_variant_name`. `src/build_atlas_maps.py` and `src/build_cogpo_maps.py` fail if that id is not a variant in `data/task_details.json` or if its parent task disagrees with `hedtsk_id`. A row whose form is now a manipulation or the standard form of a task, rather than a variant, is a `task` row and says so in `notes`.

`scope_class` in `atlas_task_to_hed.tsv` is rule-derived from the entry name (`paradigm`, `questionnaire`, `battery`, `imaging_protocol`, `physiological`). It is a heuristic, not a hand-checked judgement.

Atlas names are reproduced exactly as the API returns them, so a few contain a curly apostrophe or an en dash.

## Curation state

All four tables are curated. Every row carries a `match_type`, every matched row was checked against the archived Atlas record, and every `none` row carries a reason.

| Table                      | Rows | exact | close | related | none |
| -------------------------- | ---- | ----- | ----- | ------- | ---- |
| `hed_task_to_atlas.tsv`    | 110  | 73    | 14    | 4       | 19   |
| `atlas_task_to_hed.tsv`    | 857  | 98    | 189   | 24      | 546  |
| `hed_process_to_atlas.tsv` | 172  | 102   | 14    | 23      | 33   |
| `atlas_concept_to_hed.tsv` | 918  | 102   | 14    | 16      | 786  |

The two reverse tables hold fewer distinct matches than their forward counterparts because several HED entries share one Atlas record: both metacognitive processes map to `metacognition`, for instance. That is a property of the Atlas, not an error.

`scope_class` on unmatched Atlas task rows remains rule-derived. The `none` verdict itself was reviewed in every case.

## Editing

The TSVs are hand-editable and are the authoritative source for any generated view. `src/build_atlas_maps.py` never overwrites `match_type`, the mapped id, or `notes`. It refreshes the descriptive columns from the archive, re-deriving them from whichever id the curator chose, and reports entities added to or removed from the Atlas since the last run.

## HED to CogPO mapping

Two more tables, built and refreshed by `src/build_cogpo_maps.py` from `data/cogpo_summary.json`, map the Catalog's tasks to CogPO, the Cognitive Paradigm Ontology (Turner and Laird, 2012). CogPO has one paradigm layer and no process layer, so there is one pair of tables.

| File                        | Rows | Key         | Direction                  |
| --------------------------- | ---- | ----------- | -------------------------- |
| `hed_task_to_cogpo.tsv`     | 110  | `hedtsk_id` | HED task -> CogPO paradigm |
| `cogpo_paradigm_to_hed.tsv` | 86   | `cogpo_id`  | CogPO paradigm -> HED task |

The reverse table holds the 83 paradigm classes of the OWL release plus the three paradigms that exist only on the CogPO wiki (Delayed Match To Sample, Sleep, Tower of London); `cogpo_source` says which (`owl` or `wiki`), and a wiki-only row's id is its wiki title. `cogpo_id` is the last segment of the class IRI: `COGPO_00092` for most classes, a name such as `Naming_(Overt)_Paradigm` for the ten whose IRI is a name.

`match_type` and `match_level` mean what they mean in the Atlas tables. `scope_class` describes the CogPO class itself and is curated, not rule-derived: `paradigm` (a specific task-shaped paradigm), `broad_class` (a class of tasks, such as Encoding or Reward Task), `physiological` (stimulation, consumption, breath holding, sleep), `motor_act` (grasping, pointing, writing) and `imaging_protocol` (the flashing checkerboard). A `paradigm` row with `match_type` `none` is a task the Catalog could add.

### Curation state

Both tables were hand-checked on 2026-09-22 against the CogPO definitions. Every row carries a `match_type` and a note.

| Table                       | Rows | exact | close | related | none |
| --------------------------- | ---- | ----- | ----- | ------- | ---- |
| `hed_task_to_cogpo.tsv`     | 110  | 24    | 22    | 26      | 38   |
| `cogpo_paradigm_to_hed.tsv` | 86   | 26    | 16    | 8       | 36   |

Of the 36 unmatched CogPO classes, 15 are task-shaped paradigms the Catalog lacks (Braille reading, deception, counting or calculation, film viewing, motor and visual imagery, music, olfactory discrimination, overt reading, recitation, video games, word-stem completion, divided auditory attention), 11 are physiological procedures, 6 are motor acts, 3 are broad perceptual classes and 1 is an imaging protocol. Three reverse rows resolve to a Catalog variant rather than a task (Visual Oddball, Saccades, Word Generation (Covert)); Auditory Oddball and Delayed Non Match To Sample are task rows, because their forms are now the Oddball Task's standard form and a manipulation of Delayed Match-to-Sample.

## NEMAR task labels to HED tasks (preliminary)

`nemar_task_to_hed.tsv` is **preliminary and unchecked**. Do not rely on it. It is the output of an automatic first pass, written by `src/match_nemar_tasks.py` from an inventory of the NEMAR dataset repositories (`src/build_nemar_inventory.py`), and is kept here as a starting point for curation. Nothing on the site is generated from it and `src/generate_docs.py` does not validate it.

It has one row per dataset and BIDS task label (2946 rows over 900 datasets, mirror of 2026-10-13). A row is matched when the label, the dataset title or a keyword coincides with a task name, an alias or a variant name in the Catalog; no match has been read by a person.

| `match_type` | Rows | Meaning at this stage                                      |
| ------------ | ---- | ---------------------------------------------------------- |
| `task`       | 383  | A name coincidence with a HED task, `confidence` `review`  |
| `variant`    | 1    | A name coincidence with a variant, `confidence` `review`   |
| `unresolved` | 2562 | No automatic match; says nothing about whether a task fits |

The columns `differs` and `proposal` are empty; they are reserved for curation. How the table will be curated, and whether task labels and short descriptions are enough evidence for it, is not yet decided.
