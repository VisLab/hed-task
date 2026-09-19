"""One-time migration: import the catalog from the task-research workspace into data/.

task-research (``Claude-research/`` in that private repository) was the preliminary step
that found citations for the tasks and processes. Its two catalog files were imported
here on 2026-09-18; since then data/ is the catalog's home and changes arrive by pull
request to this repository. The script is kept as the record of how the research shape
was projected onto the published shape, and in case a bulk refresh from that workspace
is ever wanted again.

What it does, in order:

1. Reads ``task_details.json`` and ``process_details.json`` from ``--source``.
2. Validates both against the JSON Schemas in ``<source>/schemas/`` when the
   ``jsonschema`` package is available (it is in the dev extras); otherwise warns.
3. Strips fields that belong to the literature pipeline and are not published:
   ``pdf_locations``, ``local_artifacts``, ``pub_id`` on every reference, and
   ``atlas_id`` on every task. The Atlas correspondence lives in the curated tables under
   ``data/mappings/``; the field on the record produced dead and wrong links and was
   removed from this repository deliberately.
4. Assigns ``variation_id`` to every variation with the same rule as
   ``add_variation_ids.py``, and refuses if a variation already carries a different id.
5. Writes the two files to ``data/`` with LF line endings, and removes, if present, the
   derived files this repository never read (``task_names.json``, ``process_task_index.json``,
   ``process_task_crossref.md``, ``tasks_criteria.md``, ``process_criteria.md``).

Then run ``python src/generate_docs.py`` and build the site.

Usage (from the repo root, with the venv active)::

    python src/import_catalog.py --source <path to task-research>/Claude-research --check
    python src/import_catalog.py --source <path to task-research>/Claude-research
"""

from __future__ import annotations

import argparse
import collections
import json
import sys
from pathlib import Path

_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from add_variation_ids import variation_id  # noqa: E402

REPO_ROOT = _HERE.parent
DATA = REPO_ROOT / "data"

REFERENCE_FIELDS_DROPPED = ("pdf_locations", "local_artifacts", "pub_id")
TASK_FIELDS_DROPPED = ("atlas_id",)
UNUSED_DERIVED_FILES = (
    "task_names.json",
    "process_task_index.json",
    "process_task_crossref.md",
    "tasks_criteria.md",
    "process_criteria.md",
)


def _validate(instance, schema_path: Path, label: str) -> None:
    try:
        import jsonschema
    except ImportError:
        print(f"  WARNING: jsonschema not installed; {label} not validated against {schema_path.name}")
        return
    if not schema_path.exists():
        print(f"  WARNING: {schema_path} not found; {label} not validated")
        return
    schema = json.loads(schema_path.read_text(encoding="utf-8"))
    errors = sorted(jsonschema.Draft7Validator(schema).iter_errors(instance), key=lambda e: list(e.path))
    if errors:
        for err in errors[:20]:
            print(f"  schema error in {label} at {'/'.join(str(p) for p in err.path)}: {err.message[:160]}")
        sys.exit(f"{label} fails {schema_path.name} ({len(errors)} errors); nothing written.")
    print(f"  {label}: valid against {schema_path.name}")


def _project_reference(ref: dict) -> dict:
    return {k: v for k, v in ref.items() if k not in REFERENCE_FIELDS_DROPPED}


def _project_tasks(tasks: list[dict]) -> tuple[list[dict], collections.Counter]:
    stats: collections.Counter = collections.Counter()
    out = []
    for task in tasks:
        t = {k: v for k, v in task.items() if k not in TASK_FIELDS_DROPPED}
        stats["atlas_id_dropped"] += "atlas_id" in task
        t["references"] = [_project_reference(r) for r in task.get("references", [])]
        stats["references"] += len(t["references"])
        for var in t.get("variations", []):
            new_id = variation_id(task["hedtsk_id"], var["name"])
            existing = var.get("variation_id")
            if existing and existing != new_id:
                sys.exit(f"{task['hedtsk_id']}: variation {var['name']!r} carries id {existing!r}, not the derived {new_id!r}")
            var["variation_id"] = new_id
            stats["variation_ids"] += 1
        out.append(t)
    return out, stats


def _project_processes(data: dict) -> tuple[dict, collections.Counter]:
    stats: collections.Counter = collections.Counter()
    out = dict(data)
    out["processes"] = []
    for proc in data["processes"]:
        p = dict(proc)
        p["references"] = [_project_reference(r) for r in proc.get("references", [])]
        stats["references"] += len(p["references"])
        out["processes"].append(p)
    return out, stats


def _roles(records: list[dict]) -> collections.Counter:
    return collections.Counter(role for r in records for ref in r.get("references", []) for role in ref.get("roles", []))


def _write(path: Path, data) -> None:
    text = json.dumps(data, indent=2, ensure_ascii=False) + "\n"
    path.write_bytes(text.encode("utf-8"))


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--source", type=Path, required=True, help="path to task-research's Claude-research/ directory")
    ap.add_argument("--check", action="store_true", help="validate and report; write nothing")
    args = ap.parse_args()

    src = args.source
    tasks_src, procs_src = src / "task_details.json", src / "process_details.json"
    for p in (tasks_src, procs_src):
        if not p.exists():
            sys.exit(f"not found: {p}")

    print(f"Reading {src} ...")
    tasks = json.loads(tasks_src.read_text(encoding="utf-8"))
    procs = json.loads(procs_src.read_text(encoding="utf-8"))
    _validate(tasks, src / "schemas" / "task_details.schema.json", "task_details.json")
    _validate(procs, src / "schemas" / "process_details.schema.json", "process_details.json")

    # Cross-check: every process id a task names must exist.
    known = {p["process_id"] for p in procs["processes"]}
    missing = sorted({pid for t in tasks for pid in t.get("hed_process_ids", []) if pid not in known})
    if missing:
        sys.exit(f"tasks reference unknown processes: {missing}")

    new_tasks, t_stats = _project_tasks(tasks)
    new_procs, p_stats = _project_processes(procs)

    print(
        f"  tasks {len(new_tasks)}, references {t_stats['references']}, variation ids {t_stats['variation_ids']}, atlas_id dropped from {t_stats['atlas_id_dropped']}"
    )
    print(
        f"  processes {len(new_procs['processes'])}, categories {len(new_procs['categories'])}, references {p_stats['references']}"
    )
    print(f"  task reference roles: {dict(_roles(new_tasks))}")
    print(f"  process reference roles: {dict(_roles(new_procs['processes']))}")

    if args.check:
        old = DATA / "task_details.json"
        if old.exists():
            old_tasks = json.loads(old.read_text(encoding="utf-8"))
            old_ids = {v["variation_id"] for t in old_tasks for v in t.get("variations", []) if "variation_id" in v}
            new_ids = {v["variation_id"] for t in new_tasks for v in t.get("variations", [])}
            print(f"  variation ids: {len(new_ids)} new, {len(old_ids)} current, unchanged {len(new_ids & old_ids)}")
        print("check only: nothing written")
        return 0

    _write(DATA / "task_details.json", new_tasks)
    _write(DATA / "process_details.json", new_procs)
    print("Wrote data/task_details.json and data/process_details.json")
    for name in UNUSED_DERIVED_FILES:
        p = DATA / name
        if p.exists():
            p.unlink()
            print(f"  removed unused {p.relative_to(REPO_ROOT)}")
    print("Now run: python src/generate_docs.py")
    return 0


if __name__ == "__main__":
    sys.exit(main())
