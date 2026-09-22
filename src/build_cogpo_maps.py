"""Build and refresh the HED-to-CogPO paradigm mapping tables in data/mappings/.

Two TSV files, each keyed by a unique id:

    hed_task_to_cogpo.tsv        one row per HED task              (key hedtsk_id)
    cogpo_paradigm_to_hed.tsv    one row per CogPO paradigm class  (key cogpo_id)

CogPO, the Cognitive Paradigm Ontology, has one paradigm layer and no process layer, so
there is one pair of tables rather than the Atlas's two. The forward table records each
task's primary CogPO class; the reverse table records every CogPO paradigm class and the
task or variation it maps to. Several tasks may point at one CogPO class (Stroop and
Emotional Stroop both at `Stroop Task Paradigm`) and the reverse table says which one is
primary in its notes.

The reverse table covers the 83 paradigm classes in the OWL release and the three
paradigms that exist only on the CogPO wiki (Delayed Match To Sample, Sleep, Tower of
London). The `cogpo_source` column says which (`owl` or `wiki`); a wiki-only row's id is
its wiki title, since it has no `COGPO_` id.

Input is `data/cogpo_summary.json`, written by `src/build_cogpo_data.py`, not the raw
archive, so this script runs without `.cog_data/`.

This script is NON-DESTRUCTIVE, with the same contract as `build_atlas_maps.py`. On a
first run it writes candidate rows from automated name and alias matching. On later runs
it refreshes only the columns derived from the summary (labels, definition lengths,
parents), leaves the curated columns (`match_type`, `match_level`, `scope_class`, the
mapped ids and `notes`) exactly as found, and reports paradigm classes that appeared or
disappeared. Candidates are a starting point; every row is checked by hand.

    python src/build_cogpo_maps.py                # create or refresh both tables
    python src/build_cogpo_maps.py --report       # show drift and curation progress only
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

from build_atlas_maps import best_candidate, build_index, normalize, read_tsv, write_tsv

REPO = Path(__file__).parent.parent
DEFAULT_DATA = REPO / "data"
MAP_DIR_NAME = "mappings"

# Columns the curator owns. A refresh never overwrites these.
CURATED = {"match_type", "match_level", "scope_class", "cogpo_id", "hedtsk_id", "hed_variation_id", "notes"}

MATCH_TYPES = ("exact", "close", "related", "none", "")

# What an unmatched CogPO class is, as a first guess from its name. The curator's
# verdict replaces it. `paradigm` is the default and means "a task-shaped class".
SCOPE_RULES = [
    ("physiological", r"\b(acupuncture|breath|chewing|swallowing|eating|drinking|micturition|stimulation|sleep|pain)\b"),
    ("motor_act", r"\b(flexion|extension|grasping|pointing|drawing|writing|whistling|isometric)\b"),
    ("imaging_protocol", r"\b(checkerboard)\b"),
]

FORWARD_FIELDS = [
    "hedtsk_id",
    "hed_task_name",
    "match_type",
    "cogpo_id",
    "cogpo_label",
    "cogpo_source",
    "cogpo_def_chars",
    "cogpo_entry_count",
    "notes",
]

REVERSE_FIELDS = [
    "cogpo_id",
    "cogpo_label",
    "cogpo_source",
    "cogpo_parent",
    "cogpo_def_chars",
    "scope_class",
    "match_type",
    "match_level",
    "hedtsk_id",
    "hed_task_name",
    "hed_variation_id",
    "hed_variation_name",
    "notes",
]


def load_paradigms(summary: dict) -> list[dict]:
    """Return every CogPO paradigm as {id, label, source, parent, definition}.

    The OWL classes come first, in the summary's order; the wiki-only paradigms follow.
    """
    rows = [
        {
            "id": p["id"],
            "label": p["label"],
            "source": "owl",
            "parent": p["parent_label"],
            "definition": p["definition"],
        }
        for p in summary["paradigms"]
    ]
    for p in summary["paradigm_comparison"]["wiki_only"]:
        rows.append(
            {
                "id": p["title"],
                "label": p["label"],
                "source": "wiki",
                "parent": p["parent"],
                "definition": p["definition"],
            }
        )
    return rows


def scope_class(label: str) -> str:
    lowered = (label or "").lower()
    for name, pattern in SCOPE_RULES:
        if re.search(pattern, lowered):
            return name
    return "paradigm"


def merge(existing: dict[str, dict], candidates: list[dict], key_field: str, rederive) -> tuple[list[dict], dict]:
    """Overlay fresh derived columns onto curated rows. Returns (rows, drift)."""
    rows = []
    for candidate in candidates:
        prior = existing.get(candidate[key_field])
        if prior:
            merged = dict(candidate)
            for field in CURATED:
                if field in prior:
                    merged[field] = prior[field]
            rederive(merged)
            rows.append(merged)
        else:
            rows.append(candidate)
    drift = {
        "added": sorted({c[key_field] for c in candidates} - set(existing)),
        "removed": sorted(set(existing) - {c[key_field] for c in candidates}),
    }
    return rows, drift


def build_tables(hed_tasks: list[dict], paradigms: list[dict]) -> tuple[list[dict], list[dict]]:
    cogpo_index = build_index([{"name": p["label"], "alias": ""} | {"cogpo": p} for p in paradigms])
    hed_index = build_index(
        [{"name": t["canonical_name"], "alias": ";".join(t.get("aliases") or [])} | {"hed": t} for t in hed_tasks]
    )

    forward = []
    for task in sorted(hed_tasks, key=lambda t: t["canonical_name"]):
        names = [task["canonical_name"], *(task.get("aliases") or [])]
        candidate, match_type = best_candidate(names, cogpo_index)
        paradigm = candidate["cogpo"] if candidate else None
        forward.append(
            {
                "hedtsk_id": task["hedtsk_id"],
                "hed_task_name": task["canonical_name"],
                "match_type": match_type,
                "cogpo_id": paradigm["id"] if paradigm else "",
                "cogpo_label": paradigm["label"] if paradigm else "",
                "cogpo_source": paradigm["source"] if paradigm else "",
                "cogpo_def_chars": len(paradigm["definition"]) if paradigm else "",
                "cogpo_entry_count": "",
                "notes": "",
            }
        )

    variation_index: dict[str, list[dict]] = collections.defaultdict(list)
    for task in hed_tasks:
        for variation in task.get("variations") or []:
            key = normalize(variation.get("name", ""))
            if key:
                variation_index[key].append({"task": task, "variation": variation})

    reverse = []
    for paradigm in paradigms:
        names = [paradigm["label"]]
        keys = sorted({normalize(n) for n in names if normalize(n)})
        task_hit = next((k for k in keys if k in hed_index), None)
        hit = None
        if task_hit is None:
            for key in keys:
                if key in variation_index:
                    hit = variation_index[key][0]
                    break
        if hit:
            match_type, match_level = "exact", "variation"
            hedtsk_id = hit["task"]["hedtsk_id"]
            hed_task_name = hit["task"]["canonical_name"]
            variation_id = hit["variation"].get("variation_id", "")
            variation_name = hit["variation"].get("name", "")
        else:
            candidate, match_type = best_candidate(names, hed_index)
            hed = candidate["hed"] if candidate else None
            match_level = "task" if hed else ""
            hedtsk_id = hed["hedtsk_id"] if hed else ""
            hed_task_name = hed["canonical_name"] if hed else ""
            variation_id = variation_name = ""
        reverse.append(
            {
                "cogpo_id": paradigm["id"],
                "cogpo_label": paradigm["label"],
                "cogpo_source": paradigm["source"],
                "cogpo_parent": paradigm["parent"],
                "cogpo_def_chars": len(paradigm["definition"]),
                "scope_class": scope_class(paradigm["label"]) if not hedtsk_id else "paradigm",
                "match_type": match_type,
                "match_level": match_level,
                "hedtsk_id": hedtsk_id,
                "hed_task_name": hed_task_name,
                "hed_variation_id": variation_id,
                "hed_variation_name": variation_name,
                "notes": "",
            }
        )
    return forward, reverse


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--data", type=Path, default=DEFAULT_DATA, help="the data/ directory")
    parser.add_argument("--report", action="store_true", help="report only, write nothing")
    args = parser.parse_args()

    map_dir = args.data / MAP_DIR_NAME
    hed_tasks = json.loads((args.data / "task_details.json").read_text(encoding="utf-8"))
    summary_path = args.data / "cogpo_summary.json"
    if not summary_path.exists():
        raise SystemExit(f"Missing {summary_path}. Run src/build_cogpo_data.py first.")
    paradigms = load_paradigms(json.loads(summary_path.read_text(encoding="utf-8")))

    forward, reverse = build_tables(hed_tasks, paradigms)

    paradigm_by_id = {p["id"]: p for p in paradigms}
    task_by_id = {t["hedtsk_id"]: t for t in hed_tasks}
    variation_by_id = {
        v["variation_id"]: (t, v) for t in hed_tasks for v in (t.get("variations") or []) if v.get("variation_id")
    }

    def rederive_forward(row: dict) -> None:
        paradigm = paradigm_by_id.get(row.get("cogpo_id") or "")
        if row.get("cogpo_id") and not paradigm:
            raise SystemExit(f"hed_task_to_cogpo.tsv: row {row['hedtsk_id']} names unknown CogPO id {row['cogpo_id']!r}.")
        row["cogpo_label"] = paradigm["label"] if paradigm else ""
        row["cogpo_source"] = paradigm["source"] if paradigm else ""
        row["cogpo_def_chars"] = len(paradigm["definition"]) if paradigm else ""

    def rederive_reverse(row: dict) -> None:
        hed = task_by_id.get(row.get("hedtsk_id") or "")
        if row.get("hedtsk_id") and not hed:
            raise SystemExit(f"cogpo_paradigm_to_hed.tsv: row {row['cogpo_id']} names unknown task {row['hedtsk_id']!r}.")
        row["hed_task_name"] = hed["canonical_name"] if hed else ""
        vid = row.get("hed_variation_id") or ""
        if vid:
            found = variation_by_id.get(vid)
            if not found:
                raise SystemExit(f"cogpo_paradigm_to_hed.tsv: row {row['cogpo_id']} references unknown variation id {vid!r}.")
            parent, variation = found
            if parent["hedtsk_id"] != row.get("hedtsk_id"):
                raise SystemExit(
                    f"cogpo_paradigm_to_hed.tsv: row {row['cogpo_id']} maps to variation {vid!r} "
                    f"but names task {row.get('hedtsk_id')!r}, whose parent is {parent['hedtsk_id']!r}."
                )
            row["hed_variation_name"] = variation.get("name", "")
        else:
            row["hed_variation_name"] = ""
        if row.get("match_type") not in MATCH_TYPES:
            raise SystemExit(f"cogpo_paradigm_to_hed.tsv: row {row['cogpo_id']} has match_type {row['match_type']!r}.")

    tables = [
        ("hed_task_to_cogpo.tsv", FORWARD_FIELDS, forward, "hedtsk_id", rederive_forward),
        ("cogpo_paradigm_to_hed.tsv", REVERSE_FIELDS, reverse, "cogpo_id", rederive_reverse),
    ]
    merged: dict[str, list[dict]] = {}
    for filename, _fields, candidates, key_field, rederive in tables:
        existing = read_tsv(map_dir / filename)
        rows, drift = merge(existing, candidates, key_field, rederive)
        merged[filename] = rows
        status = "create" if not existing else "refresh"
        curated = sum(1 for r in rows if (r.get("notes") or "").strip())
        counts = collections.Counter(r["match_type"] for r in rows)
        print(f"{filename}: {status}, {len(rows)} rows, {curated} with curator notes, {dict(counts)}")
        if drift["added"]:
            print(f"  added since last run ({len(drift['added'])}): {drift['added'][:6]}")
        if drift["removed"]:
            print(f"  removed since last run ({len(drift['removed'])}): {drift['removed'][:6]}")

    # How many CogPO classes point at each task, from the curated reverse rows.
    entry_counts = collections.Counter(r["hedtsk_id"] for r in merged["cogpo_paradigm_to_hed.tsv"] if r["hedtsk_id"])
    for row in merged["hed_task_to_cogpo.tsv"]:
        row["cogpo_entry_count"] = entry_counts.get(row["hedtsk_id"], 0)

    if args.report:
        print("\n--report given; nothing written.")
        return
    for filename, fields, _, _, _ in tables:
        write_tsv(map_dir / filename, fields, merged[filename])


if __name__ == "__main__":
    main()
