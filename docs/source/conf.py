# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html
#
# Two kinds of page live under docs/source/. Narrative pages (the landing page, the
# overview pages, the Atlas essays and the Methods documents) are hand-written Markdown,
# edited directly. Catalog pages (tasks/, processes/, task_process_links.md) and the table
# fragments in _generated/ (including the full Atlas mapping tables) are written by
# src/generate_docs.py from the data in data/, and are never edited by hand.

import csv
import json
from datetime import date
from pathlib import Path

# -- Project information -----------------------------------------------------

project = "HED Task Catalog"
copyright = f"2026-{date.today().year}, HED Working Group"
author = "HED Working Group"
release = "1.0.0"

# -- General configuration ---------------------------------------------------

extensions = [
    "myst_parser",
    "sphinx_copybutton",
    "sphinx_design",
]

templates_path = ["_templates"]
# _generated/ holds table fragments that narrative pages pull in with an include
# directive; they are not documents of their own.
exclude_patterns = ["_build", "_templates", "_generated", "Thumbs.db", ".DS_Store"]
source_suffix = {".md": "markdown"}
master_doc = "index"

# -- Options for HTML output -------------------------------------------------

html_theme = "furo"
html_title = "HED Task Catalog"
html_static_path = ["_static"]
html_css_files = ["custom.css"]
html_js_files = ["gh_icon_fix.js", "pop_cards.js"]
html_logo = "_static/images/croppedWideLogo.png"

# There is no Python domain content, so py-modindex.html would be empty.
html_domain_indices = False

html_theme_options = {
    # The brand template in _templates/sidebar/brand.html prints the site name under
    # the logo, so Furo's own copy is hidden.
    "sidebar_hide_name": True,
    "light_css_variables": {
        "color-brand-primary": "#0969da",
        "color-brand-content": "#0969da",
    },
    "dark_css_variables": {
        "color-brand-primary": "#58a6ff",
        "color-brand-content": "#58a6ff",
    },
    "source_repository": "https://github.com/hed-standard/hed-task/",
    "source_branch": "main",
    "source_directory": "docs/source/",
}

# Development banner shown at the top of the middle panel on every page, by the page
# template in _templates/page.html. Edit the text here; delete the key to remove the banner.
html_context = {
    "dev_banner": (
        "The HED Task Catalog is under development. IDs are not stable until formal release. "
        'Comments are welcome at <a href="https://github.com/hed-standard/hed-task/issues">'
        "github.com/hed-standard/hed-task/issues</a>."
    ),
}

# Same sidebar composition as hed-resources: brand, search, navigation, quick links.
html_sidebars = {
    "**": [
        "sidebar/brand.html",
        "sidebar/search.html",
        "sidebar/scroll-start.html",
        "sidebar/navigation.html",
        "quicklinks.html",
        "sidebar/ethical-ads.html",
        "sidebar/scroll-end.html",
    ]
}

# -- MyST parser settings ----------------------------------------------------

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "html_admonition",
    "html_image",
    "linkify",
    "replacements",
    "smartquotes",
    "substitution",
    "tasklist",
]

# Process pages use (hed-xxx)= Sphinx labels as anchor targets for deep links from
# task pages, which render correctly in HTML as <span id="hed-xxx">. MyST's link
# validator does not recognise MyST labels as valid local IDs (it only checks
# myst_heading_anchors slugs), so it reports myst.xref_missing even though browser
# navigation works.
suppress_warnings = ["myst.xref_missing"]

# -- Live counts for narrative pages ------------------------------------------
#
# A hand-written page can write {{ n_tasks }} and get the current figure. The counts are
# read from the same data the generator uses, so they cannot disagree with the catalog
# pages. Everything else in a narrative page is plain text that its author maintains.


def _catalog_counts() -> dict[str, int]:
    root = Path(__file__).resolve().parents[2]
    tasks = json.loads((root / "data" / "task_details.json").read_text(encoding="utf-8"))
    proc_data = json.loads((root / "data" / "process_details.json").read_text(encoding="utf-8"))
    processes = proc_data["processes"]
    with (root / "data" / "task_family_defs.tsv").open(encoding="utf-8", newline="") as handle:
        families = list(csv.DictReader(handle, delimiter="\t"))
    linked = {pid for t in tasks for pid in t.get("hed_process_ids", [])}
    pseudo = [t for t in tasks if t.get("task_kind") == "pseudo_task"]
    return {
        # n_tasks counts ordinary tasks; pseudo tasks (rest, fixation, questionnaire
        # blocks) are counted separately so that the headline figure stays honest.
        "n_tasks": len(tasks) - len(pseudo),
        "n_pseudo_tasks": len(pseudo),
        "n_processes": len(processes),
        "n_categories": len(proc_data["categories"]),
        "n_families": len(families),
        "n_variations": sum(len(t.get("variations", [])) for t in tasks),
        "n_links": sum(len(t.get("hed_process_ids", [])) for t in tasks),
        "n_linked": sum(1 for p in processes if p["process_id"] in linked),
    }


myst_substitutions = {key: str(value) for key, value in _catalog_counts().items()}
