"""CLI entry point: validate the catalog in data/ and generate the catalog pages.

Inputs, all under data/ and all edited in this repository by pull request:

    task_details.json        the tasks (top level is a bare array)
    process_details.json     the processes and their categories
    mappings/*.tsv           the curated correspondence with the Cognitive Atlas
    task_family_defs.tsv     the task families (membership is on each task record)
    schemas/*.schema.json    JSON Schemas for the two catalog files

Two kinds of page live under docs/source/. This script writes only the catalog pages,
which are tabular views of the data:

    tasks/**                     task index, family pages, alphabetical list, task pages
    processes/**                 process index, category pages
    task_process_links.md        task-process links
    _generated/*.md              table fragments that narrative pages include, among
                                 them the full Atlas mapping tables

Those paths are deleted and rewritten on every run, so a page dropped from the
generators cannot linger. Every other file under docs/source/ - the landing page, the
overview pages, the Atlas essays, the Methods documents, conf.py, _static/, _templates/ -
is hand-maintained and is never touched here.

Nothing is written until the whole catalog validates: schema shape, unique identifiers,
every cross-reference resolving, derived fields agreeing with their sources, reference
roles from the allowed vocabulary, and every task filed under a family. A failure names
the record, so a pull request that edits the data gets a precise message from CI.

Usage (from repo root, with venv active):
    python src/generate_docs.py
"""

from __future__ import annotations

import collections
import re
import shutil
import sys
from pathlib import Path

# Ensure the src/ directory is on the Python path so `generators` can be imported.
_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from add_variation_ids import variation_id  # noqa: E402
from generators import (  # noqa: E402
    crossref_atlas_pages,
    crossref_cogpo_pages,
    crossref_page,
    fragments,
    process_pages,
    task_pages,
)
from generators.utils import load_json, primary_category, primary_family, read_tsv  # noqa: E402

# Everything the generator owns, relative to docs/source/. Nothing outside this list is
# ever deleted or written.
GENERATED_PATHS = [
    "tasks",
    "processes",
    "task_process_links.md",
    "_generated",
]

_VALID_CONFIDENCE = {"high", "review"}

# The one family a pseudo task (task_kind == "pseudo_task") may belong to.
PSEUDO_FAMILY = "pseudo_tasks"


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def _schema_check(instance, schema_path: Path, label: str, problems: list[str]) -> dict:
    """Validate `instance` against a JSON Schema; return the loaded schema."""
    try:
        import jsonschema
    except ImportError:
        sys.exit('jsonschema is not installed; run: pip install -e ".[docs]"')
    schema = load_json(schema_path)
    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.path)):
        where = "/".join(str(p) for p in err.path) or "(root)"
        problems.append(f"{label} at {where}: {err.message[:200]}")
    return schema


def _reference_roles(schema: dict) -> set[str]:
    """The allowed `roles` values, read from the schema so they are defined once."""
    role_def = schema.get("definitions", {}).get("reference_role", {})
    return set(role_def.get("enum", []))


def _check_memberships(records: list[dict], field: str, id_key: str, known: set[str], ident: str, problems: list[str]) -> None:
    """Check a record's family or category memberships (issue 28).

    Exactly one primary, no repeated ids, every id known, confidence in the vocabulary, a
    rationale on every secondary and on every review entry. The JSON Schema checks the
    shape of one membership; these rules span the list, so they live here.

    Parameters:
        records: Task or process records.
        field: "families" or "categories".
        id_key: "family_id" or "category_id".
        known: The vocabulary of ids.
        ident: The record's identifier field, for messages.
        problems: The list to append messages to.
    """
    for r in records:
        members = r.get(field, [])
        label = f"{r[ident]}: {field}"
        primaries = [m for m in members if m.get("role") == "primary"]
        if len(primaries) != 1:
            problems.append(f"{label} has {len(primaries)} primary memberships; exactly one is required")
        ids = [m.get(id_key) for m in members]
        for value, n in collections.Counter(ids).items():
            if n > 1:
                problems.append(f"{label} lists {value!r} {n} times")
        for m in members:
            if m.get(id_key) not in known:
                problems.append(f"{label} names unknown {id_key} {m.get(id_key)!r}")
            if m.get("confidence", "high") not in _VALID_CONFIDENCE:
                problems.append(f"{label} {m.get(id_key)}: confidence {m.get('confidence')!r}, expected high or review")
            needs_rationale = m.get("role") == "secondary" or m.get("confidence") == "review"
            if needs_rationale and not m.get("rationale"):
                problems.append(f"{label} {m.get(id_key)}: a secondary or review membership needs a rationale")


def validate_catalog(data_dir: Path, tasks: list[dict], proc_data: dict) -> None:
    """Check the two catalog files against their schemas and against each other.

    Exits with every problem found, so that a contributor sees the whole list at once
    rather than one failure per run.
    """
    problems: list[str] = []
    task_schema = _schema_check(tasks, data_dir / "schemas" / "task_details.schema.json", "task_details.json", problems)
    proc_schema = _schema_check(
        proc_data, data_dir / "schemas" / "process_details.schema.json", "process_details.json", problems
    )
    roles = _reference_roles(task_schema) | _reference_roles(proc_schema)

    processes = proc_data["processes"]
    categories = proc_data["categories"]

    # Unique identifiers and names.
    for field, records, label in (
        ("hedtsk_id", tasks, "task"),
        ("canonical_name", tasks, "task"),
        ("process_id", processes, "process"),
        ("process_name", processes, "process"),
        ("category_id", categories, "category"),
    ):
        for value, n in collections.Counter(r[field] for r in records).items():
            if n > 1:
                problems.append(f"{label} {field} {value!r} appears {n} times")

    # Cross-references.
    process_ids = {p["process_id"] for p in processes}
    category_ids = {c["category_id"] for c in categories}
    task_ids = {t["hedtsk_id"] for t in tasks}
    for t in tasks:
        for pid in t.get("hed_process_ids", []):
            if pid not in process_ids:
                problems.append(f"{t['hedtsk_id']}: hed_process_ids names unknown process {pid!r}")
        # The inclusion test is three lists (data/README.md, "Editing a task or process"):
        # procedure steps are sentences, the other two are fragments. The schema checks
        # the shape; the text rules are here.
        test = t.get("inclusion_test") or {}
        for step in test.get("procedure") or []:
            if step != step.strip() or not step.endswith((".", "!", "?")):
                problems.append(f"{t['hedtsk_id']}: procedure step must be a trimmed sentence ending in a period: {step!r}")
        for field in ("manipulations", "measurements"):
            for item in test.get(field) or []:
                # No capital-letter rule: an item may begin with an initialism (fMRI) or
                # a conventionally lowercase term (d-prime).
                if item != item.strip() or not item or item.endswith((";", ".")) or not (item[0].isalnum() or item[0] == "("):
                    problems.append(
                        f"{t['hedtsk_id']}: {field} item must be trimmed, begin with a letter, digit or parenthesis "
                        f"and carry no final period or semicolon: {item!r}"
                    )
        # A task engages at least one process; a pseudo task (task criteria, "Pseudo tasks") engages none
        # by definition, so the two kinds are checked in opposite directions.
        is_pseudo = t.get("task_kind", "task") == "pseudo_task"
        if not t.get("hed_process_ids") and not is_pseudo:
            problems.append(f"{t['hedtsk_id']}: hed_process_ids is empty but task_kind is not pseudo_task")
        if t.get("hed_process_ids") and is_pseudo:
            problems.append(
                f"{t['hedtsk_id']}: a pseudo task carries no process links, but hed_process_ids is {t['hed_process_ids']}"
            )
    _check_memberships(processes, "categories", "category_id", category_ids, "process_id", problems)
    primary_cats = {primary_category(p) for p in processes if any(m.get("role") == "primary" for m in p.get("categories", []))}
    for cid in sorted(category_ids - primary_cats):
        problems.append(f"category {cid}: no process is filed under it")

    # Derived fields must agree with their sources: a process's tasks[] with the tasks
    # that name it, task_count with tasks[], and the category and header counts.
    derived: dict[str, list[str]] = collections.defaultdict(list)
    for t in tasks:
        for pid in t.get("hed_process_ids", []):
            derived[pid].append(t["hedtsk_id"])
    for p in processes:
        listed = [x["hedtsk_id"] for x in p.get("tasks", [])]
        expected = sorted(derived.get(p["process_id"], []))
        if sorted(listed) != expected:
            problems.append(
                f"{p['process_id']}: tasks[] lists {sorted(listed)} but the task records name it from {expected}; "
                "update tasks[] and task_count on the process"
            )
        if p.get("task_count", len(listed)) != len(listed):
            problems.append(f"{p['process_id']}: task_count {p.get('task_count')} but tasks[] has {len(listed)}")
        for x in p.get("tasks", []):
            if x["hedtsk_id"] not in task_ids:
                problems.append(f"{p['process_id']}: tasks[] names unknown task {x['hedtsk_id']!r}")
    per_category = collections.Counter(
        primary_category(p) for p in processes if any(m.get("role") == "primary" for m in p.get("categories", []))
    )
    for c in categories:
        if c.get("process_count") != per_category[c["category_id"]]:
            problems.append(
                f"category {c['category_id']}: process_count {c.get('process_count')} but "
                f"{per_category[c['category_id']]} processes are filed under it"
            )
    for key, actual in (
        ("total_processes", len(processes)),
        ("total_categories", len(categories)),
        ("total_tasks", len(tasks)),
        ("total_processes_used_by_tasks", sum(1 for p in processes if derived.get(p["process_id"]))),
    ):
        if key in proc_data and proc_data[key] != actual:
            problems.append(f"process_details.json header {key} is {proc_data[key]} but the data has {actual}")

    # Reference roles from the vocabulary; no new reference should be left `unknown`.
    for records, idf in ((tasks, "hedtsk_id"), (processes, "process_id")):
        for r in records:
            for i, ref in enumerate(r.get("references", [])):
                bad = [role for role in ref.get("roles", []) if role not in roles]
                if bad:
                    problems.append(f"{r[idf]}: reference {i} has roles {bad} not in {sorted(roles)}")

    # Variation ids are derived from the parent id and the name; they must match.
    seen_var: set[str] = set()
    for t in tasks:
        for v in t.get("variations", []):
            expected_id = variation_id(t["hedtsk_id"], v["name"])
            if v.get("variation_id") != expected_id:
                problems.append(
                    f"{t['hedtsk_id']}: variation {v['name']!r} has id {v.get('variation_id')!r}, expected {expected_id!r}"
                )
            if expected_id in seen_var:
                problems.append(f"{t['hedtsk_id']}: duplicate variation id {expected_id!r}")
            seen_var.add(expected_id)

    if problems:
        sys.exit(f"Catalog data is inconsistent ({len(problems)} problems); nothing written.\n  " + "\n  ".join(problems))


def load_families(data_dir: Path, tasks: list[dict]) -> list[dict]:
    """Read data/task_family_defs.tsv and validate every task's `families` against it.

    Raises SystemExit with a list of every problem found, so that a partial site is never
    published from an inconsistent assignment. Returns the family definitions sorted by
    display order.
    """
    defs = read_tsv(data_dir / "task_family_defs.tsv")
    problems: list[str] = []

    if not defs:
        problems.append("data/task_family_defs.tsv is missing or empty")

    family_ids = [d["family_id"] for d in defs]
    if len(family_ids) != len(set(family_ids)):
        problems.append("duplicate family_id in task_family_defs.tsv")
    known = set(family_ids)

    _check_memberships(tasks, "families", "family_id", known, "hedtsk_id", problems)
    with_primary = [t for t in tasks if any(m.get("role") == "primary" for m in t.get("families", []))]
    used = {primary_family(t) for t in with_primary}
    for fid in sorted(known - used):
        problems.append(f"task_family_defs.tsv: no task is filed under family {fid}")

    # Pseudo tasks and the pseudo-task family belong together, in both directions, and a
    # pseudo task is not cross-listed elsewhere.
    for t in with_primary:
        kind = t.get("task_kind", "task")
        listed = {m["family_id"] for m in t["families"]}
        if kind == "pseudo_task" and (primary_family(t) != PSEUDO_FAMILY or listed != {PSEUDO_FAMILY}):
            problems.append(f"{t['hedtsk_id']}: a pseudo task belongs to {PSEUDO_FAMILY!r} only")
        if kind != "pseudo_task" and PSEUDO_FAMILY in listed:
            problems.append(f"{t['hedtsk_id']}: is in {PSEUDO_FAMILY!r} but its task_kind is not pseudo_task")

    if problems:
        sys.exit("Family data is inconsistent; nothing written.\n  " + "\n  ".join(problems))

    defs.sort(key=lambda d: int(d["order"]))
    return defs


# The facet vocabulary in data/facet_defs.tsv. Nothing on a task record uses it yet; it
# is validated here so that an edit to the vocabulary is caught before the pages that
# render it are written.
FACETS = ("stimulus_modality", "stimulus_kind", "stimulus_role", "response_modality", "response_kind", "instructions")
FACET_SOURCES = ("cogpo", "cogpo_wiki", "hed", "catalog")
FACET_COLUMNS = ("facet", "value", "label", "definition", "source", "cogpo_id", "hed_tags", "hed_note")
_FACET_VALUE = re.compile(r"^[a-z][a-z0-9_]*$")


def load_facet_defs(data_dir: Path) -> list[dict]:
    """Read and validate data/facet_defs.tsv. Exits, naming the row, on any problem.

    A `cogpo` row must name a dimension value that exists in data/cogpo_summary.json. A
    `cogpo_wiki` row names a wiki page title, which the summary does not list when the
    page has no term template (the body parts), so only its presence is checked.
    """
    path = data_dir / "facet_defs.tsv"
    rows = read_tsv(path)
    problems: list[str] = []
    if not rows:
        sys.exit("data/facet_defs.tsv is missing or empty; nothing written.")
    missing = [c for c in FACET_COLUMNS if c not in rows[0]]
    if missing:
        sys.exit(f"data/facet_defs.tsv lacks columns {missing}; nothing written.")

    summary = load_json(data_dir / "cogpo_summary.json")
    owl_ids = {v["id"] for d in summary["dimensions"].values() for v in d["values"]}

    seen: set[tuple[str, str]] = set()
    for row in rows:
        label = f"facet_defs.tsv {row['facet']}/{row['value']}"
        if row["facet"] not in FACETS:
            problems.append(f"{label}: facet not in {FACETS}")
        if not _FACET_VALUE.match(row["value"]):
            problems.append(f"{label}: value must be lowercase snake_case")
        if (row["facet"], row["value"]) in seen:
            problems.append(f"{label}: duplicate value")
        seen.add((row["facet"], row["value"]))
        if row["source"] not in FACET_SOURCES:
            problems.append(f"{label}: source {row['source']!r} not in {FACET_SOURCES}")
        if row["source"] == "cogpo" and row["cogpo_id"] not in owl_ids:
            problems.append(f"{label}: cogpo_id {row['cogpo_id']!r} is not a CogPO dimension value in cogpo_summary.json")
        if row["source"] == "cogpo_wiki" and not row["cogpo_id"]:
            problems.append(f"{label}: a cogpo_wiki row needs the wiki page title in cogpo_id")
        if row["source"] in ("hed", "catalog") and row["cogpo_id"]:
            problems.append(f"{label}: a {row['source']} row must not carry a cogpo_id")
        if row["source"] == "hed" and not row["hed_tags"].strip():
            problems.append(f"{label}: a hed row needs hed_tags")
        if not row["label"].strip() or not row["definition"].strip():
            problems.append(f"{label}: label and definition are required")
        if any(ord(ch) > 127 for ch in "\t".join(row.values())):
            problems.append(f"{label}: non-ASCII character")

    if problems:
        sys.exit("Facet vocabulary is inconsistent; nothing written.\n  " + "\n  ".join(problems))
    return rows


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------


def clear_generated(docs_dir: Path) -> int:
    """Delete the generated paths under docs/source/. Returns the number of files removed."""
    removed = 0
    for rel in GENERATED_PATHS:
        path = docs_dir / rel
        if path.is_dir():
            removed += sum(1 for p in path.rglob("*") if p.is_file())
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()
            removed += 1
    return removed


def main() -> None:
    repo_root = _HERE.parent
    data_dir = repo_root / "data"
    docs_dir = repo_root / "docs" / "source"

    print("Loading data/task_details.json and data/process_details.json ...")
    tasks: list[dict] = load_json(data_dir / "task_details.json")
    proc_data: dict = load_json(data_dir / "process_details.json")
    categories: list[dict] = proc_data["categories"]
    processes: list[dict] = proc_data["processes"]

    print("Validating the catalog ...")
    validate_catalog(data_dir, tasks, proc_data)
    families = load_families(data_dir, tasks)
    print(
        f"  {len(tasks)} tasks, {len(processes)} processes, {len(categories)} categories, {len(families)} families: consistent"
    )
    facet_defs = load_facet_defs(data_dir)
    print(f"  {len(facet_defs)} facet values in {len({r['facet'] for r in facet_defs})} facets: consistent")

    # The curated mapping drives the Atlas link on each task page and is the only Atlas
    # cross-reference; task records carry no atlas_id of their own.
    atlas_map = {r["hedtsk_id"]: r for r in read_tsv(data_dir / "mappings" / "hed_task_to_atlas.tsv")}

    # The CogPO mapping drives the CogPO link on each task page the same way. A class
    # links to its page on the CogPO wiki, whose title the summary records; the two
    # Oddball subclasses have no wiki page and get no link.
    cogpo_summary = load_json(data_dir / "cogpo_summary.json")
    wiki_titles = {p["id"]: p["wiki"]["title"] for p in cogpo_summary["paradigms"] if p.get("wiki")}
    wiki_titles.update({p["title"]: p["title"] for p in cogpo_summary["paradigm_comparison"]["wiki_only"]})
    cogpo_map = {}
    for row in read_tsv(data_dir / "mappings" / "hed_task_to_cogpo.tsv"):
        row["cogpo_wiki_title"] = wiki_titles.get(row["cogpo_id"], "")
        cogpo_map[row["hedtsk_id"]] = row

    tasks_by_id: dict[str, dict] = {t["hedtsk_id"]: t for t in tasks}
    processes_by_id: dict[str, dict] = {p["process_id"]: p for p in processes}

    removed = clear_generated(docs_dir)
    print(f"Removed {removed} previously generated files.")
    total = 0

    print("Generating docs/source/tasks/ ...")
    n = task_pages.generate(docs_dir, tasks, processes_by_id, families, atlas_map, cogpo_map)
    total += n
    print(
        f"  Wrote {n} task files (index, tasks_by_family, {len(families)} family pages, tasks_alphabetically, {len(tasks)} task pages)."
    )

    print("Generating docs/source/processes/ ...")
    n = process_pages.generate(docs_dir, processes, categories, tasks_by_id)
    total += n
    print(f"  Wrote {n} process files (index, processes_by_category, processes_alphabetically, {n - 3} category pages).")

    print("Generating docs/source/task_process_links.md ...")
    total += crossref_page.generate(docs_dir, tasks, processes, categories)

    print("Generating docs/source/_generated/ fragments ...")
    total += crossref_atlas_pages.generate(docs_dir, data_dir)
    total += crossref_cogpo_pages.generate(docs_dir, data_dir)
    total += fragments.generate(docs_dir, data_dir, tasks, processes, categories, families)

    print(f"\nDone. {total} files written to {docs_dir}. Narrative pages were not touched.")


if __name__ == "__main__":
    main()
