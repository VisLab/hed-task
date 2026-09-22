# Guide to contributing to the hed-task project

The HED Task Catalog is curated continuously and depends on its users to grow. This guide says how to propose a change, how the site is regenerated, and which checks a pull request must pass.

## Proposing a change

Open an issue at <https://github.com/hed-standard/hed-task/issues>. The [how to use the Catalog](https://www.hedtags.org/hed-task/how_to_use_the_catalog.html) page says what each kind of proposal should contain; in brief:

- **A new task.** Canonical name and aliases; a procedure, a manipulation and a measurement in the form the inclusion tests use; the processes it engages; one or two references; and why it is not a variation of an existing task.
- **A new variation.** The parent task, what changes in what the participant experiences or does, and why that change is not one of the excluded kinds (measurement modality, analysis method, population, stimulus swap, and so on).
- **A new process.** When in a trial it happens, what elicits it, how it is measured, which category it belongs in, and why it is not an alias of an existing process.
- **A different family for a task, or a second one.** Name the task, the family you would move it to or cross-list it under, and the procedural reason. The current memberships and their rationales are the `families` list on each task record in `data/task_details.json`.
- **A correction.** Quote the page and the text that is wrong.
- **A disagreement with a rule.** The criteria pages state the rules as they stand; arguments for changing one are welcome.

## What lives where

The catalog pages are generated. Corrections to a task or process are applied to the data, never to the pages.

| Content                                                                                     | Where it lives                                                                                                                                                                                                                 | Who edits it                                                                             |
| ------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------------------- |
| Task and process records                                                                    | `data/task_details.json`, `data/process_details.json`                                                                                                                                                                          | Edited here by pull request; see `data/README.md` for the record shape and the checks    |
| Atlas mapping tables                                                                        | `data/mappings/*.tsv`                                                                                                                                                                                                          | Edited here by pull request; `src/build_atlas_maps.py` refreshes the descriptive columns |
| Paradigm families that group tasks on the site                                              | `families` on each task record, `data/task_family_defs.tsv`                                                                                                                                                                    | Edited here by pull request                                                              |
| Narrative pages: landing, introduction, how to use, the Atlas essays, the Methods documents | `docs/source/*.md`, `docs/source/atlas/what_is_the_cognitive_atlas.md`, `docs/source/atlas/the_catalog_vs_the_atlas.md`, `docs/source/atlas/task_mapping.md`, `docs/source/atlas/process_mapping.md`, `docs/source/methods/**` | Edited here by pull request, directly in Markdown                                        |
| Layout and wording of the catalog pages                                                     | `src/generators/`                                                                                                                                                                                                              | Edited here by pull request                                                              |
| Sphinx configuration, styling, templates                                                    | `docs/source/conf.py`, `docs/source/_static/`, `docs/source/_templates/`                                                                                                                                                       | Edited here by pull request                                                              |
| Generated catalog pages                                                                     | `docs/source/tasks/`, `processes/`, `task_process_links.md`, `_generated/`                                                                                                                                                     | Never by hand; regenerated and committed                                                 |

Any of these can be a pull request directly. An issue first is welcome when the change is a judgement call (a new task, a new process, a re-filed family) so that the reasoning is discussed before the edit. Every hand-written page carries a comment at the top saying so; a page without that comment is generated.

## Making a pull request

1. Fork the repository and create a branch from `main`.
2. Set up the environment:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate    Linux / macOS: source .venv/bin/activate
   pip install -e ".[dev,docs]"
   ```
3. Make the change: a record in `data/task_details.json` or `data/process_details.json` (see `data/README.md`, including which `roles` a new reference gets), a table in `data/`, a narrative page under `docs/source/`, a generator in `src/`, or `docs/source/conf.py` and the static files.
4. Regenerate the catalog pages if anything under `data/` or `src/` changed (a narrative-page edit needs no regeneration). The generator validates the data first and names any record that fails; CI runs the same step and fails the PR if the committed pages are out of date. The script deletes every generated page and rewrites the current set, so the diff will be large; commit it with the change that caused it.
   ```bash
   python src/generate_docs.py
   ```
5. Build the site and open `docs/_build/html/index.html`. A clean build emits no warnings.
   ```bash
   sphinx-build -b html docs/source docs/_build/html
   ```
6. Run the checks that CI runs:
   ```bash
   ruff check .
   ruff format --check .
   python -m mdformat --check --wrap no --number *.md
   python src/check_references.py   # if you touched a reference
   ```
   Do not run `mdformat` over `docs/source/`; it rewrites the generated MyST directives into a form Sphinx cannot parse.
7. Open the pull request against `main`. Say what changed and why; for a family change, quote the rationale you put in the table.

## Conventions

- ASCII only in prose, code, comments and filenames: `-` rather than an em or en dash, `->` rather than an arrow glyph, `...` rather than an ellipsis character, straight quotes. Genuine data such as author names and recorded Atlas entry names keep whatever characters they contain.
- Sentence case for every Markdown heading, including generated ones.
- Identifiers: `hedtsk_<slug>` for tasks, `hedvar_<task>__<variation>` for variations, `hed_<slug>` for processes. They are provisional while the Catalog is being curated.
- Published pages state what is true now. Dates, change logs and resolved-issue notes belong in issues and commit messages, not on the site.

## Where to ask

Questions that are not proposals are also welcome as issues. The HED project's wider resources are at <https://www.hedtags.org/hed-resources/>.
