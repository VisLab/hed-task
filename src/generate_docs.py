"""CLI entry point: generate all Sphinx documentation pages from .working/ data.

Usage (from repo root, with venv active):
    python src/generate_docs.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

# Ensure the src/ directory is on the Python path so `generators` can be imported.
_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from generators import (  # noqa: E402
    atlas_pages,
    criteria_pages,
    crossref_atlas_pages,
    crossref_page,
    index_page,
    methodology_pages,
    process_pages,
    relationship_page,
    task_pages,
)
from generators.utils import load_json  # noqa: E402


def main() -> None:
    repo_root = _HERE.parent
    working_dir = repo_root / ".working"
    docs_dir = repo_root / "docs"

    # ------------------------------------------------------------------
    # Load authoritative data sources
    # ------------------------------------------------------------------
    print("Loading task_details.json ...")
    tasks: list[dict] = load_json(working_dir / "task_details.json")

    print("Loading process_details.json ...")
    proc_data: dict = load_json(working_dir / "process_details.json")
    categories: list[dict] = proc_data["categories"]
    processes: list[dict] = proc_data["processes"]

    # Derived from the external Cognitive Atlas harvest by src/build_atlas_data.py.
    print("Loading atlas_summary.json ...")
    atlas_data: dict = load_json(working_dir / "atlas_summary.json")

    # ------------------------------------------------------------------
    # Build lookup dicts
    # ------------------------------------------------------------------
    tasks_by_id: dict[str, dict] = {t["hedtsk_id"]: t for t in tasks}
    processes_by_id: dict[str, dict] = {p["process_id"]: p for p in processes}
    {c["category_id"]: c for c in categories}
    processes_by_category: dict[str, list[dict]] = {}
    for proc in processes:
        processes_by_category.setdefault(proc["category_id"], []).append(proc)

    # ------------------------------------------------------------------
    # Run generators
    # ------------------------------------------------------------------
    total_files = 0

    print("Generating docs/index.md ...")
    index_page.generate(docs_dir, tasks, processes, categories)
    total_files += 1

    print("Generating docs/tasks/ ...")
    # The curated Atlas mapping drives the Atlas link on each task page and is the
    # only Atlas cross-reference. Task records used to carry their own atlas_id, but
    # 18 of its 64 populated values were dead or pointed at a different paradigm, so
    # the field was removed rather than left to drift from the mapping again.
    atlas_map: dict[str, dict] = {}
    map_path = working_dir / "mappings" / "hed_task_to_atlas.tsv"
    if map_path.exists():
        with map_path.open(encoding="utf-8", newline="") as handle:
            atlas_map = {r["hedtsk_id"]: r for r in csv.DictReader(handle, delimiter="	")}

    n = task_pages.generate(docs_dir, tasks, processes_by_id, atlas_map)
    total_files += n
    print(f"  Wrote {n} task files (1 index + {n - 1} task pages).")

    print("Generating docs/processes/ ...")
    n = process_pages.generate(docs_dir, processes, categories, tasks_by_id)
    total_files += n
    print(f"  Wrote {n} process files (1 index + {n - 1} category pages).")

    print("Generating docs/crossref.md ...")
    crossref_page.generate(docs_dir, tasks, processes, categories)
    total_files += 1

    print("Generating docs/atlas/ ...")
    n = atlas_pages.generate(docs_dir, atlas_data)
    total_files += n
    print(f"  Wrote {n} atlas files.")

    print("Generating docs/atlas/ crossref pages ...")
    n = crossref_atlas_pages.generate(docs_dir, working_dir)
    total_files += n
    print(f"  Wrote {n} atlas crossref files.")

    print("Generating docs/atlas/relationship.md ...")
    total_files += relationship_page.generate(docs_dir, working_dir, atlas_data)

    print("Generating docs/methodology/ ...")
    n = methodology_pages.generate(docs_dir, working_dir)
    total_files += n
    print(f"  Wrote {n} methodology files.")

    print("Generating docs/criteria/ ...")
    n = criteria_pages.generate(docs_dir, working_dir)
    total_files += n
    print(f"  Wrote {n} criteria files.")

    # ------------------------------------------------------------------
    # Delete docs/index.rst if it still exists (replaced by index.md)
    # ------------------------------------------------------------------
    index_rst = docs_dir / "index.rst"
    if index_rst.exists():
        index_rst.unlink()
        print("Deleted docs/index.rst (replaced by index.md).")

    print(f"\nDone. {total_files} files written to {docs_dir}.")


if __name__ == "__main__":
    main()
