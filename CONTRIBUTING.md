# Guide to contributing to the hed-task project

The HED task catalog is curated continuously and depends on its users to grow. This guide says how to propose a change, how the site is regenerated, and which checks a pull request must pass.

## Proposing a change

Open an issue at <https://github.com/hed-standard/hed-task/issues>. The [how to use the catalog](https://www.hedtags.org/hed-task/how_to_use.html) page says what each kind of proposal should contain; in brief:

- **A new task.** Canonical name and aliases; a procedure, a manipulation and a measurement in the form the inclusion tests use; the processes it engages; one or two references; and why it is not a variation of an existing task.
- **A new variation.** The parent task, what changes in what the participant experiences or does, and why that change is not one of the excluded kinds (measurement modality, analysis method, population, stimulus swap, and so on).
- **A new process.** When in a trial it happens, what elicits it, how it is measured, which category it belongs in, and why it is not an alias of an existing process.
- **A different family for a task.** Name the task, the family you would move it to, and the procedural reason. The current assignments and their rationales are in `data/task_families.tsv`.
- **A correction.** Quote the page and the text that is wrong.
- **A disagreement with a rule.** The criteria pages state the rules as they stand; arguments for changing one are welcome.

## What lives where

The site is generated. Corrections are applied to the data, never to the pages.

| Content                                                            | Where it lives                                                           | Who edits it                                                      |
| ------------------------------------------------------------------ | ------------------------------------------------------------------------ | ----------------------------------------------------------------- |
| Task and process records, criteria documents, Atlas mapping tables | `.working/`                                                              | Imported from the curation project; not edited in this repository |
| Paradigm families that group tasks on the site                     | `data/task_families.tsv`, `data/task_family_defs.tsv`                    | Edited here by pull request; see `data/README.md`                 |
| Page layout and wording                                            | `src/generators/`                                                        | Edited here by pull request                                       |
| Sphinx configuration, styling, templates                           | `docs/source/conf.py`, `docs/source/_static/`, `docs/source/_templates/` | Edited here by pull request                                       |
| Generated pages                                                    | `docs/source/**/*.md`                                                    | Never by hand; regenerated and committed                          |

A change to a task's definition, references or process links therefore starts as an issue, because the record it would change is imported. A change to a family assignment, to page wording, or to the site configuration can be a pull request directly.

## Making a pull request

1. Fork the repository and create a branch from `main`.
2. Set up the environment:
   ```bash
   python -m venv .venv
   # Windows: .venv\Scripts\activate    Linux / macOS: source .venv/bin/activate
   pip install -e ".[dev,docs]"
   ```
3. Make the change in `data/`, `src/`, or `docs/source/conf.py` and the static files.
4. Regenerate the pages if anything under `data/` or `src/` changed. The script deletes every generated page and rewrites the current set, so the diff will be large; commit it with the change that caused it.
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
   ```
   Do not run `mdformat` over `docs/source/`; it rewrites the generated MyST directives into a form Sphinx cannot parse.
7. Open the pull request against `main`. Say what changed and why; for a family change, quote the rationale you put in the table.

## Conventions

- ASCII only in prose, code, comments and filenames: `-` rather than an em or en dash, `->` rather than an arrow glyph, `...` rather than an ellipsis character, straight quotes. Genuine data such as author names and recorded Atlas entry names keep whatever characters they contain.
- Sentence case for every Markdown heading, including generated ones.
- Identifiers: `hedtsk_<slug>` for tasks, `hedvar_<task>__<variation>` for variations, `hed_<slug>` for processes. They are provisional while the catalog is being curated.
- Published pages state what is true now. Dates, change logs and resolved-issue notes belong in issues and commit messages, not on the site.

## Where to ask

Questions that are not proposals are also welcome as issues. The HED project's wider resources are at <https://www.hedtags.org/hed-resources/>.
