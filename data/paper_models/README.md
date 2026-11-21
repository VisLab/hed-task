# Task models of papers

One JSON file per paper. Each file models the tasks the paper runs as games, in the same terms as the task catalog, and says how each relates to a catalog task. The site page [The modeling process](https://www.hedtags.org/hed-task/modeling_process.html) explains the steps; this file says how to fill the template in.

This is a first version of the template (`template_version` 0.1). No paper has been modeled with it yet, and it is expected to change.

| File                                      | What it is                                                        |
| ----------------------------------------- | ----------------------------------------------------------------- |
| `template.json`                           | The blank template, written by `python src/paper_models.py new`   |
| `../schemas/paper_task_model.schema.json` | The JSON Schema of a filled-in file (shape only)                  |
| `<first_author>_<year>_<short_slug>.json` | One paper, for example `stroop_1935_serial_verbal_reactions.json` |

## Starting a file

```bash
# Blank, when the game type is not yet known (this is template.json):
python src/paper_models.py new --out data/paper_models/<name>.json

# With every rule question of a game type, answered with its default:
python src/paper_models.py new respond_to_rule --out data/paper_models/<name>.json

# With the answers of the standard form of a catalog task, to confirm or change:
python src/paper_models.py new --from hedtsk_stroop_color_word --out data/paper_models/<name>.json
```

A paper with several tasks has one entry per task in `tasks`; copy the entry, or run `new` again and paste its entry in.

## Filling it in

Work through the entry in the order of the steps on the site.

01. `task_label`, `experiment`, `summary` - the name the paper gives the task, which experiment or session it belongs to, and one or two plain sentences on what the participant did.
02. `game_type` - one of the ten game types of `data/task_game_defs.json`.
03. `rules` - one answer for every rule question of that game type, defaults included. A game type with no rule questions has `{}`.
04. `motivators` - `drive` always; `sign`, `earned_by`, `what` and `real` only when something is won, lost or delivered. Payment for taking part in the study is not a motivator.
05. `phases` - phase names in order, or an empty list.
06. `task_facets` - for each of the nine facets, the values that are present. An empty list means the facet has nothing to say.
07. `settings` - each quantity the study chose, with its `value` and `unit` as the paper gives them. `material` - one sentence. `combined_with` - a second job, as a `game_type` or a catalog `task`, with `how` it is combined.
08. `procedure`, `manipulations`, `measurements` - in the form of a catalog inclusion test: ordered steps; one variable per item with its levels; one measure per item.
09. `catalog_match` - `hedtsk_id` of the catalog task whose procedure this matches, `hedvar_id` if it is one of its variants, and the `relation`: `standard_form`, `variant`, `new_variant`, `new_task` or `unclear`.
10. `processes` - a process id of `data/process_details.json` and its `source`: `authors` (the paper says so), `catalog` (linked to the matched catalog task) or `coder` (your inference).
11. `participants`, `recording` - in the paper's own words.
12. `not_in_vocabulary` - anything the vocabulary could not say: the `part` it belongs to, a `proposed` name, a `description` and the passage. Do not force the nearest value.

Every answer under `game_type`, `rules`, `motivators`, `phases` and `task_facets` has three keys:

- `value` - a value, or a list of values, from the vocabulary.
- `basis` - `stated` (the paper says it), `inferred` (it follows from what the paper says) or `assumed` (the paper is silent, and the default or the usual form was taken). `new` writes `assumed` on everything it fills in.
- `evidence` - a short quotation, or where the passage is: "Methods, Procedure, paragraph 2".

A list of objects starts with one blank row that shows its keys. Fill it in or leave it blank; the checker skips a blank row.

## Checking

```bash
python src/paper_models.py check data/paper_models/
```

The checker validates each file against the schema and the vocabulary, and reports for each task:

- **problems**, which make the file invalid: a value that is not in the vocabulary, a rule question left out, an unknown task or process id;
- **notes**: how many answers are still `assumed`, a `stated` answer with no evidence, a setting that is not in the vocabulary;
- **the differences from the catalog**: each part on which the task differs from the standard form of the catalog task it names, or from the variant it names. A `standard_form` or `variant` relation with differences is flagged.

The differences are computed, so they are never typed into the file.
