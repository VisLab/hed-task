# Curated presentation data

Hand-edited tables that the documentation generators read alongside the imported catalog in `.working/`. Unlike `.working/`, these files are owned by this repository and are meant to be edited here.

| File                   | Rows | Key         | Purpose                                               |
| ---------------------- | ---- | ----------- | ----------------------------------------------------- |
| `task_family_defs.tsv` | 18   | `family_id` | The paradigm families: display order, name, and scope |
| `task_families.tsv`    | 103  | `hedtsk_id` | Which family each task is filed under, and why        |

## Task families

A family groups tasks by what the participant does, not by which cognitive process the task is thought to measure. That is the same principle the task criteria use to decide whether two experiments are the same task: procedure first. The process catalog covers the other axis, so the two views cross-link rather than duplicate one another.

Every task is filed under exactly one family, which is what lets the site's sidebar nest the task pages. The assignment is a curation decision, and it is expected to change as the catalog grows. When a task genuinely spans two families the `rationale` column names the alternative.

### Columns

`task_family_defs.tsv`

- `family_id` - snake_case identifier, used in page paths and anchors
- `order` - display order on the task index and in the sidebar
- `name` - display name, sentence case
- `scope` - one or two sentences saying what procedure the family covers and what is measured

`task_families.tsv`

- `hedtsk_id` - the task, as in `.working/task_details.json`
- `family_id` - must exist in `task_family_defs.tsv`
- `confidence` - `high` when the filing is uncontroversial, `review` when a reasonable reader could file it elsewhere; the generator publishes `review` rows normally but the task index notes how many there are
- `rationale` - one line saying why the task is in this family, naming the alternative when `confidence` is `review`

### Rules the generator enforces

`src/generate_docs.py` fails, rather than publishing a partial site, if:

- a task in `.working/task_details.json` has no row in `task_families.tsv`
- a row in `task_families.tsv` names a task that is not in the catalog
- a `family_id` is not defined in `task_family_defs.tsv`
- a family in `task_family_defs.tsv` has no tasks

### Editing

Edit the TSVs directly, keep them ASCII, then regenerate the docs with `python src/generate_docs.py`. The 15 rows marked `review` in the first draft (2026-09-18) are the ones most worth a second look.
