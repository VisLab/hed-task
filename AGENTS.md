# hed-task

Purpose: a catalog of standard cognitive and behavioral neuroscience tasks and the cognitive processes they engage, published as a Sphinx website. Not in scope: HED tooling, schema definitions, and the validation test suite - those live in `hed-python`, `hed-schemas`, and `hed-tests`.

## Commands

Test framework: unittest. Never convert the suite to pytest style as a side effect of other work. The `tests/` directory is currently empty; there is no suite to run yet.

Always run in the virtual environment - the system interpreter does not have the docs dependencies installed.

- Install dev env: `pip install -e ".[dev,docs]"`
- Lint: `python -m ruff check .`
- Format check: `python -m ruff format --check .`
- Generate the docs pages: `python src/generate_docs.py`
- Build the site: `python -m sphinx -b html docs docs/_build/html`

Local development uses `pip`; GitHub Actions uses `uv`. Do not use `uv` locally unless asked.

## Layout

- `src/` - the generators. `generate_docs.py` is the entry point; `src/generators/` holds one module per page family.
- `docs/` - Sphinx sources. **Generated output** - edit the generator, not these files.
- `.working/` - the imported task and process catalog. **Read-only here**; the work that produces it happens elsewhere, and edits would be lost on the next import.
- `tests/` - unit tests.
- `.status/` - working notes. Gitignored; local to each machine.

## Conventions that differ from defaults

- **ASCII only** in prose, code, comments, and filenames: `-` not em or en dashes, `->` not arrows, `...` not an ellipsis character, straight quotes. Exception: genuine data - author names, dataset titles, recorded API responses - keeps whatever characters it actually contains.
- **Sentence case for every markdown heading**: capitalize the first word and proper nouns or acronyms (HED, BIDS, JSON, AI) only. `## Task structure overview`, not `## Task Structure Overview`. This applies to generated pages too, so it is a property of the generator output.
- Google-style docstrings, with `Parameters:` rather than `Args:`.
- `snake_case.py` for Python, `snake_case.md` or `.rst` for documentation.
- Use `pathlib` and relative paths; never hardcode an absolute path.

## Rules that are easy to get wrong

- `docs/` is generated. `src/generate_docs.py` rewrites all of it in one pass, so running it as a "does this work" check will show up as a large diff. Run it only when regeneration is the intended change.
- `mdformat` must not be run over `docs/`. It rewrites the generated MyST directives into a form Sphinx cannot parse. The CI check is scoped to the repository root for this reason.
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
