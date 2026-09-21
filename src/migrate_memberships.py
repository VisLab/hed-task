"""One-time migration for GitHub issue 28: put family and category membership on the records.

Kept as the record of what was done on 2026-09-21; it refuses to run a second time.

Before: a task's family was one row in data/task_families.tsv (hedtsk_id, family_id,
confidence, rationale) and a process's category was the `category_id` field on its record.
Both were one-to-one.

After: each task record carries `families` and each process record `categories`, a list
of memberships {family_id | category_id, role, confidence, rationale}. Exactly one has role
"primary" (where the record is filed); the rest are "secondary" cross-listings. The
vocabularies (data/task_family_defs.tsv, the `categories` array) are unchanged.

The fifteen `review` rows of the TSV are read as follows (plan: .status/plans/
family_membership.md, section 2, checked by Kay): where the rationale names an alternative
family, the task gets a secondary membership in it with confidence `review` and the
rationale, and the primary is reset to `high`; where the rationale states a doubt with no
alternative, the primary keeps `review` and the rationale.

Run from the repository root:

    python src/migrate_memberships.py

It writes data/task_details.json and data/process_details.json and deletes
data/task_families.tsv. Run src/generate_docs.py afterwards to validate and regenerate.
"""

from __future__ import annotations

import csv
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# hedtsk_id -> family_id of the secondary membership to add, for the review rows whose
# rationale names an alternative. Review rows absent from this table keep `review` on
# the primary.
SECONDARY_FROM_REVIEW = {
    "hedtsk_navon": "perceptual_judgment",
    "hedtsk_weapons_identification": "social_cognition_and_games",
    "hedtsk_sustained_attention_to_response": "oddball_and_vigilance",
    "hedtsk_attention_network": "conflict_and_interference",
    "hedtsk_contextual_cueing": "conditioning_and_reinforcement",
    "hedtsk_rapid_serial_visual_presentation": "visual_search_and_tracking",
    "hedtsk_cambridge_face_memory": "perceptual_judgment",
    "hedtsk_serial_reaction_time": "motor_performance",
    "hedtsk_trail_making": "motor_performance",
    "hedtsk_remote_associates": "language",
    "hedtsk_affective_priming": "conflict_and_interference",
    "hedtsk_mental_rotation": "perceptual_judgment",
}


def _dump(path: Path, data) -> None:
    path.write_text(json.dumps(data, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def _insert_before(record: dict, key: str, value, before: str) -> dict:
    """Return a copy of record with key inserted before `before` (or appended)."""
    out: dict = {}
    placed = False
    for k, v in record.items():
        if k == before and not placed:
            out[key] = value
            placed = True
        out[k] = v
    if not placed:
        out[key] = value
    return out


def migrate_tasks(tasks: list[dict], rows: list[dict]) -> list[dict]:
    by_task = {r["hedtsk_id"]: r for r in rows}
    out = []
    for task in tasks:
        if "families" in task:
            sys.exit(f"{task['hedtsk_id']} already has families; the migration has run")
        row = by_task[task["hedtsk_id"]]
        primary = {"family_id": row["family_id"], "role": "primary", "confidence": row["confidence"]}
        members = [primary]
        secondary_family = SECONDARY_FROM_REVIEW.get(task["hedtsk_id"])
        if secondary_family:
            primary["confidence"] = "high"
            members.append(
                {
                    "family_id": secondary_family,
                    "role": "secondary",
                    "confidence": "review",
                    "rationale": row["rationale"],
                }
            )
        elif row["rationale"]:
            primary["rationale"] = row["rationale"]
        out.append(_insert_before(task, "families", members, "hed_process_ids"))
    return out


def migrate_processes(processes: list[dict]) -> list[dict]:
    out = []
    for proc in processes:
        if "categories" in proc or "category_id" not in proc:
            sys.exit(f"{proc['process_id']} has no category_id or already has categories; the migration has run")
        members = [{"category_id": proc["category_id"], "role": "primary", "confidence": "high"}]
        rebuilt = {}
        for k, v in proc.items():
            if k == "category_id":
                rebuilt["categories"] = members
            else:
                rebuilt[k] = v
        out.append(rebuilt)
    return out


def main() -> None:
    tsv = DATA / "task_families.tsv"
    if not tsv.exists():
        sys.exit("data/task_families.tsv is gone; the migration has run")
    with tsv.open(encoding="utf-8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    tasks = json.loads((DATA / "task_details.json").read_text(encoding="utf-8"))
    proc_data = json.loads((DATA / "process_details.json").read_text(encoding="utf-8"))

    # The TSV must name every catalog task exactly once and nothing else; a duplicate
    # or stray row would otherwise migrate silently and the source would then be deleted.
    row_ids = [r["hedtsk_id"] for r in rows]
    duplicates = sorted({i for i in row_ids if row_ids.count(i) > 1})
    if duplicates:
        sys.exit(f"task_families.tsv lists these tasks more than once: {duplicates}")
    task_ids = {t["hedtsk_id"] for t in tasks}
    missing = task_ids - set(row_ids)
    if missing:
        sys.exit(f"tasks without a family row: {sorted(missing)}")
    stray = set(row_ids) - task_ids
    if stray:
        sys.exit(f"task_families.tsv rows for tasks not in the catalog: {sorted(stray)}")
    unknown = set(SECONDARY_FROM_REVIEW) - {r["hedtsk_id"] for r in rows if r["confidence"] == "review"}
    if unknown:
        sys.exit(f"SECONDARY_FROM_REVIEW names tasks that are not review rows: {sorted(unknown)}")

    new_tasks = migrate_tasks(tasks, rows)
    proc_data["processes"] = migrate_processes(proc_data["processes"])
    _dump(DATA / "task_details.json", new_tasks)
    _dump(DATA / "process_details.json", proc_data)
    tsv.unlink()

    n_secondary = sum(1 for t in new_tasks for m in t["families"] if m["role"] == "secondary")
    n_review = sum(1 for t in new_tasks for m in t["families"] if m["confidence"] == "review")
    print(f"{len(new_tasks)} tasks: {len(new_tasks)} primary, {n_secondary} secondary, {n_review} review memberships")
    print(f"{len(proc_data['processes'])} processes: category_id -> categories (one primary each)")
    print("deleted data/task_families.tsv; run src/generate_docs.py to validate and regenerate")


if __name__ == "__main__":
    main()
