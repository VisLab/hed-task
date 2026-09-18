"""CLI entry point: generate the catalog pages under docs/source/.

Inputs:
    .working/   the imported task and process catalog and the Atlas mapping tables
                (read-only in this repository)
    data/       the curated presentation tables owned by this repository, currently the
                paradigm families (see data/README.md)

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

Usage (from repo root, with venv active):
    python src/generate_docs.py
"""

from __future__ import annotations

import shutil
import sys
from pathlib import Path

# Ensure the src/ directory is on the Python path so `generators` can be imported.
_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

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
    working_dir = repo_root / ".working"
    data_dir = repo_root / "data"
    docs_dir = repo_root / "docs" / "source"

    # ------------------------------------------------------------------
    # Load and validate
    # ------------------------------------------------------------------
    print("Loading task_details.json ...")
    tasks: list[dict] = load_json(working_dir / "task_details.json")

    print("Loading process_details.json ...")
    proc_data: dict = load_json(working_dir / "process_details.json")
    categories: list[dict] = proc_data["categories"]
    processes: list[dict] = proc_data["processes"]

    print("Loading data/task_families.tsv ...")
    families, family_rows = load_families(data_dir, tasks)

    # The curated Atlas mapping drives the Atlas link on each task page and is the only
    # Atlas cross-reference. Task records used to carry their own atlas_id, but 18 of its
    # 64 populated values were dead or pointed at a different paradigm, so the field was
    # removed rather than left to drift from the mapping again.
    atlas_map = {r["hedtsk_id"]: r for r in read_tsv(working_dir / "mappings" / "hed_task_to_atlas.tsv")}

    tasks_by_id: dict[str, dict] = {t["hedtsk_id"]: t for t in tasks}
    processes_by_id: dict[str, dict] = {p["process_id"]: p for p in processes}

    # ------------------------------------------------------------------
    # Generate
    # ------------------------------------------------------------------
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
    total += crossref_atlas_pages.generate(docs_dir, working_dir)

    print("Generating docs/source/_generated/ fragments ...")
    total += fragments.generate(docs_dir, working_dir, tasks, processes, categories, families)

    print(f"\nDone. {total} files written to {docs_dir}. Narrative pages were not touched.")


if __name__ == "__main__":
    main()
