"""CLI entry point: validate the catalog in data/ and generate the catalog pages.

Inputs, all under data/ and all edited in this repository by pull request:

    task_details.json        the tasks (top level is a bare array)
    process_details.json     the processes and their categories
    mappings/*.tsv           the curated correspondence with the Cognitive Atlas
    task_families.tsv        which paradigm family each task is filed under
    task_family_defs.tsv     the families themselves
    schemas/*.schema.json    JSON Schemas for the two catalog files

Two kinds of page live under docs/source/. This script writes only the catalog pages,
which are tabular views of the data:

    tasks/**                     task index, family pages, alphabetical list, task pages
    processes/**                 process index, category pages
    crossref.md                  task-process links
    atlas/task_mapping.md        Atlas mapping tables
    atlas/process_mapping.md
    _generated/*.md              table fragments that narrative pages include

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
    crossref_page,
    fragments,
    process_pages,
    task_pages,
)
from generators.utils import load_json, read_tsv  # noqa: E402

# Everything the generator owns, relative to docs/source/. Nothing outside this list is
# ever deleted or written.
GENERATED_PATHS = [
    "tasks",
    "processes",
    "crossref.md",
    "atlas/task_mapping.md",
    "atlas/process_mapping.md",
    "_generated",
]

_VALID_CONFIDENCE = {"high", "review"}


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
    for p in processes:
        if p["category_id"] not in category_ids:
            problems.append(f"{p['process_id']}: unknown category {p['category_id']!r}")

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
    per_category = collections.Counter(p["category_id"] for p in processes)
    for c in categories:
        if c.get("process_count") != per_category[c["category_id"]]:
            problems.append(
                f"category {c['category_id']}: process_count {c.get('process_count')} but {per_category[c['category_id']]} processes"
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


def load_families(data_dir: Path, tasks: list[dict]) -> tuple[list[dict], list[dict]]:
    """Read and validate data/task_family_defs.tsv and data/task_families.tsv.

    Raises SystemExit with a list of every problem found, so that a partial site is never
    published from an inconsistent assignment.
    """
    defs = read_tsv(data_dir / "task_family_defs.tsv")
    rows = read_tsv(data_dir / "task_families.tsv")
    problems: list[str] = []

    if not defs:
        problems.append("data/task_family_defs.tsv is missing or empty")
    if not rows:
        problems.append("data/task_families.tsv is missing or empty")

    family_ids = [d["family_id"] for d in defs]
    if len(family_ids) != len(set(family_ids)):
        problems.append("duplicate family_id in task_family_defs.tsv")
    known = set(family_ids)

    task_ids = {t["hedtsk_id"] for t in tasks}
    seen: set[str] = set()
    used: set[str] = set()
    for row in rows:
        tid = row["hedtsk_id"]
        if tid in seen:
            problems.append(f"task_families.tsv: {tid} appears more than once")
        seen.add(tid)
        if tid not in task_ids:
            problems.append(f"task_families.tsv: {tid} is not a task in the catalog")
        if row["family_id"] not in known:
            problems.append(f"task_families.tsv: {tid} names unknown family {row['family_id']!r}")
        used.add(row["family_id"])
        if row["confidence"] not in _VALID_CONFIDENCE:
            problems.append(f"task_families.tsv: {tid} has confidence {row['confidence']!r}, expected high or review")
    for tid in sorted(task_ids - seen):
        problems.append(f"task_families.tsv: catalog task {tid} has no family")
    for fid in sorted(known - used):
        problems.append(f"task_family_defs.tsv: family {fid} has no tasks")

    if problems:
        sys.exit("Family data is inconsistent; nothing written.\n  " + "\n  ".join(problems))

    defs.sort(key=lambda d: int(d["order"]))
    return defs, rows


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
    families, family_rows = load_families(data_dir, tasks)
    print(
        f"  {len(tasks)} tasks, {len(processes)} processes, {len(categories)} categories, {len(families)} families: consistent"
    )

    # The curated mapping drives the Atlas link on each task page and is the only Atlas
    # cross-reference; task records carry no atlas_id of their own.
    atlas_map = {r["hedtsk_id"]: r for r in read_tsv(data_dir / "mappings" / "hed_task_to_atlas.tsv")}

    tasks_by_id: dict[str, dict] = {t["hedtsk_id"]: t for t in tasks}
    processes_by_id: dict[str, dict] = {p["process_id"]: p for p in processes}

    removed = clear_generated(docs_dir)
    print(f"Removed {removed} previously generated files.")
    total = 0

    print("Generating docs/source/tasks/ ...")
    n = task_pages.generate(docs_dir, tasks, processes_by_id, families, family_rows, atlas_map)
    total += n
    print(f"  Wrote {n} task files (index, {len(families)} family pages, all_tasks, {len(tasks)} task pages).")

    print("Generating docs/source/processes/ ...")
    n = process_pages.generate(docs_dir, processes, categories, tasks_by_id)
    total += n
    print(f"  Wrote {n} process files (1 index + {n - 1} category pages).")

    print("Generating docs/source/crossref.md ...")
    total += crossref_page.generate(docs_dir, tasks, processes, categories)

    print("Generating docs/source/atlas/ mapping tables ...")
    total += crossref_atlas_pages.generate(docs_dir, data_dir)

    print("Generating docs/source/_generated/ fragments ...")
    total += fragments.generate(docs_dir, data_dir, tasks, processes, categories, families)

    print(f"\nDone. {total} files written to {docs_dir}. Narrative pages were not touched.")


if __name__ == "__main__":
    main()
