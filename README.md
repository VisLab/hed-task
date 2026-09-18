# hed-task

[![Deploy documentation](https://github.com/hed-standard/hed-task/actions/workflows/docs.yaml/badge.svg)](https://github.com/hed-standard/hed-task/actions/workflows/docs.yaml) [![Ruff](https://github.com/hed-standard/hed-task/actions/workflows/ruff.yaml/badge.svg)](https://github.com/hed-standard/hed-task/actions/workflows/ruff.yaml) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A curated catalog of standard cognitive and behavioral neuroscience tasks and the cognitive processes they engage, developed as part of the [HED (Hierarchical Event Descriptors)](https://www.hedtags.org/) standardization effort. Its purpose is to provide a controlled vocabulary for tagging datasets with what their participants were asked to do, so that repositories can be searched by task or by process and datasets can be compared across laboratories.

The catalog currently covers **103 tasks** in **18 paradigm families**, **172 cognitive processes** in **19 categories**, and **486 task-process links**. Each task has a canonical definition, an inclusion test, named variations, verified references and a mapping to the Cognitive Atlas. The catalog is a work in progress; suggestions, corrections and proposals are welcome as [GitHub issues](https://github.com/hed-standard/hed-task/issues).

The catalog is published as a searchable website at **<https://www.hedtags.org/hed-task/>**.

## Contents

| Section                                                                        | Description                                                                                |
| ------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------ |
| [Introduction](https://www.hedtags.org/hed-task/introduction.html)             | What the catalog is made of, its identifiers, and where it came from                       |
| [How to use the catalog](https://www.hedtags.org/hed-task/how_to_use.html)     | Reading a task page, tagging a dataset, proposing a change                                 |
| [Tasks](https://www.hedtags.org/hed-task/tasks/index.html)                     | 103 tasks in 18 paradigm families, each with inclusion test, variations and process links  |
| [Cognitive processes](https://www.hedtags.org/hed-task/processes/index.html)   | 172 processes in 19 categories, each with definition, references and linked tasks          |
| [Task-process links](https://www.hedtags.org/hed-task/crossref.html)           | The whole task-to-process matrix in both directions                                        |
| [Methods](https://www.hedtags.org/hed-task/methods/task_criteria.html)         | Task and process selection criteria; how the Cognitive Atlas mapping was built             |
| [Cognitive Atlas](https://www.hedtags.org/hed-task/atlas/cognitive_atlas.html) | What the Atlas contains, how this catalog relates to it, and the row-by-row mapping tables |

## Repository structure

```
hed-task/
|-- src/                    # Documentation generators (Python)
|   |-- generate_docs.py    # Entry point: regenerates docs/source/ from .working/ and data/
|   |-- build_atlas_data.py # Recomputes .working/atlas_summary.json from the Atlas harvest
|   |-- build_atlas_maps.py # Refreshes .working/mappings/*.tsv, preserving curation
|   |-- fetch_cog_data.py   # Rebuilds the Atlas API archive in .cog_data/
|   |-- generators/         # One module per page family
|-- data/                   # Curated presentation tables owned by this repo (task families)
|-- docs/
|   |-- source/             # Sphinx source: hand-written narrative pages plus generated catalog pages
|   |-- _build/             # Build output (gitignored)
|-- .working/               # Imported catalog: task/process details, atlas_summary.json, mappings/
|-- tests/                  # Unit tests
|-- pyproject.toml
```

Two kinds of page live in `docs/source/`. The narrative pages (landing page, introduction, how to use, the two Cognitive Atlas essays, and the three Methods documents) are hand-written Markdown: edit them directly. The catalog pages (`tasks/`, `processes/`, `crossref.md`, the two Atlas mapping tables, and the table fragments in `_generated/`) are generated from the JSON data in `.working/` and the TSV tables in `data/` by the scripts in `src/`, and are never edited by hand. Each hand-written page says so in a comment at its top. See [Regenerating the site](#regenerating-the-site) below.

`.working/` is the imported catalog and is not edited in this repository. `data/` holds curation that lives here: currently the paradigm families that group the tasks on the site (`data/task_families.tsv`, `data/task_family_defs.tsv`; see `data/README.md`). The family assignment is expected to be revised iteratively.

## Local development

**Prerequisites:** Python 3.10 or later.

```bash
# Clone and set up
git clone https://github.com/hed-standard/hed-task.git
cd hed-task
python -m venv .venv

# Activate (Windows)
.venv\Scripts\activate
# Activate (Linux / macOS)
source .venv/bin/activate

# Install dependencies
pip install -e ".[dev,docs]"
```

### Regenerating the site

Whenever the data in `.working/` or `data/` changes, run both steps below. Editing a narrative page needs only step 2.

**Step 1 - regenerate the Markdown source:**

```bash
python src/generate_docs.py
```

This reads `task_details.json`, `process_details.json` and `mappings/*.tsv` from `.working/` and the family tables from `data/`, deletes the generated paths under `docs/source/` (`tasks/`, `processes/`, `crossref.md`, the two Atlas mapping tables, `_generated/`), and rewrites them. It never touches a narrative page. It refuses to run if a task has no family, a family has no tasks, or a family id is unknown.

`atlas_summary.json` and `mappings/*.tsv` are derived from a byte-exact archive of the [Cognitive Atlas](https://www.cognitiveatlas.org/) REST API kept in `.cog_data/`, which is untracked. Only the derived files are committed, so the docs build never needs the archive. To refresh, run:

```bash
python src/fetch_cog_data.py      # rebuild .cog_data/ from the Atlas API (resumable)
python src/build_atlas_data.py    # recompute .working/atlas_summary.json
python src/build_atlas_maps.py    # refresh the mapping tables, preserving curation
```

`build_atlas_data.py` and `build_atlas_maps.py` both take `--archive` if the archive is not at `.cog_data/`.

**Step 2 - build the HTML:**

```bash
sphinx-build -b html docs/source docs/_build/html
```

Then open `docs/_build/html/index.html` in a browser to preview. A clean build emits no warnings.

Narrative pages can use a few live counts from the data, written as `{{ n_tasks }}`, `{{ n_processes }}`, `{{ n_categories }}`, `{{ n_families }}`, `{{ n_variations }}`, `{{ n_links }}` or `{{ n_linked }}`; `docs/source/conf.py` defines them at build time. A table that follows the data is pulled in from `docs/source/_generated/` with an include directive.

Do not run `mdformat` over `docs/source/`. It rewrites the generated MyST directives into a form Sphinx cannot parse. The `mdformat` CI check is scoped to the hand-written Markdown at the repository root for that reason:

```bash
python -m mdformat --check --wrap no --number *.md
```

### Run tests

```bash
python -m unittest discover -s tests -v
```

### Lint and format

```bash
ruff check .
ruff format --check .
```

## CI/CD

| Workflow        | Trigger             | Purpose                                   |
| --------------- | ------------------- | ----------------------------------------- |
| `docs.yaml`     | Push / PR to `main` | Build and deploy the site to GitHub Pages |
| `ruff.yaml`     | Push / PR to `main` | Lint and format checks                    |
| `mdformat.yaml` | Push / PR to `main` | Markdown formatting of the root files     |
| `links.yaml`    | Push / PR to `main` | Broken link detection                     |

## Related resources

- [HED homepage](https://www.hedtags.org/)
- [HED resources](https://www.hedtags.org/hed-resources/)
- [HED specification](https://github.com/hed-standard/hed-specification)
- [HED Python tools](https://github.com/hed-standard/hed-python)
- [HED schemas](https://github.com/hed-standard/hed-schemas)
- [Cognitive Atlas](https://www.cognitiveatlas.org/)

## License

This project is licensed under the [MIT License](LICENSE).
