# hed-task

Purpose: a catalog of standard cognitive and behavioral neuroscience tasks and the cognitive processes they engage, published as a Sphinx website. Not in scope: HED tooling, schema definitions, and the validation test suite - those live in `hed-python`, `hed-schemas`, and `hed-tests`.

## Commands

Test framework: unittest. Never convert the suite to pytest style as a side effect of other work. The `tests/` directory is currently empty; there is no suite to run yet.

Always run in the virtual environment - the system interpreter does not have the docs dependencies installed.

- Install dev env: `pip install -e ".[dev,docs]"`
- Lint: `python -m ruff check .`
- Format check: `python -m ruff format --check .`
- Audit reference identifiers against their citations: `python src/check_references.py` (prints; does not fail)
- Generate the docs pages: `python src/generate_docs.py`
- Build the site: `python -m sphinx -b html docs/source docs/_build/html`. After a toctree change build clean (`-E -a`); an incremental build leaves the old sidebar on pages whose source did not change.

Local development uses `pip`; GitHub Actions uses `uv`. Do not use `uv` locally unless asked.

## Layout

- `src/` - the generators. `generate_docs.py` is the entry point; `src/generators/` holds one module per page family.
- `docs/source/` - Sphinx sources, built into `docs/_build/`. Two kinds of page: **narrative pages** (`index.md`, `introduction.md`, `how_to_use_the_catalog.md`, `atlas/what_is_the_cognitive_atlas.md`, `atlas/the_catalog_vs_the_atlas.md`, `atlas/task_mapping.md`, `atlas/process_mapping.md`, everything under `cogpo/` and `methods/`) are hand-written Markdown, edited directly, each marked by a comment at the top; **catalog pages** (`tasks/`, `processes/`, `task_process_links.md`, `_generated/`) are generated - edit the generator or the data, not these files. `generate_docs.py` lists the generated paths in `GENERATED_PATHS` and touches nothing else.
- `data/` - the Catalog: `task_details.json`, `process_details.json`, `schemas/`, `mappings/`, `atlas_summary.json`, `cogpo_summary.json`, and the paradigm-family definitions. Edited here by pull request; `generate_docs.py` validates all of it before writing. See `data/README.md`.
- `tests/` - unit tests.
- `.status/` - working notes. Gitignored; local to each machine.

## Conventions that differ from defaults

- **ASCII only** in prose, code, comments, and filenames: `-` not em or en dashes, `->` not arrows, `...` not an ellipsis character, straight quotes. Exception: genuine data - author names, dataset titles, recorded API responses - keeps whatever characters it actually contains.
- **Sentence case for every markdown heading**: capitalize the first word and proper nouns or acronyms (HED, BIDS, JSON, AI) only. `## Task structure overview`, not `## Task Structure Overview`. This applies to generated pages too, so it is a property of the generator output.
- Google-style docstrings, with `Parameters:` rather than `Args:`.
- `snake_case.py` for Python, `snake_case.md` or `.rst` for documentation.
- Use `pathlib` and relative paths; never hardcode an absolute path.

## Rules that are easy to get wrong

- The catalog pages under `docs/source/` are generated. `src/generate_docs.py` deletes and rewrites them in one pass, so running it as a "does this work" check will show up as a large diff. Run it only when regeneration is the intended change. Narrative pages are never generated; do not add prose to `src/generators/`.
- The criteria documents are the hand-maintained pages under `docs/source/methods/`. `src/import_catalog.py` is the record of the one-time 2026-09-18 import from the task-research workspace, not part of the workflow; do not point it at anything without asking.
- `mdformat` must not be run over `docs/source/`. It rewrites the generated MyST directives into a form Sphinx cannot parse. The CI check is scoped to the repository root for this reason.
- Lint config lives in `pyproject.toml`. Do not restate the rule list anywhere else, and never let an autofix reorder an `__init__.py` - their import order is curated to avoid circular imports.

## Where the thinking lives

`.status/` is gitignored - local to this machine, absent from clones and worktrees.

- `.status/README.md` - the index. Read this first; it lists what is active.
- `.status/decisions.md` - why things are the way they are. Read before proposing structural changes. Append entries; never rewrite one.
- `.status/plans/*.md` - active plans. Check the `Status:` header and the `[ ]` markers before starting work.
- IMPORTANT: do not read `.status/archive/` or `.status/notes/` unless I name a file. Do not delete or rewrite anything under `.status/` without asking.

## Working agreements

- Lead with the conclusion. Three or four sentences of takeaway, then the detail.
- Show evidence, not assertions: the command you ran and its real output. For catalog work, include counts and a sample of records.
- Give the file name and the line number when reporting a finding or a change.
- Temporary scripts, experiments, and one-off test files go in `.status/scratch/` - never the repository root.
- Say so explicitly when you are guessing about an external API or data format.
