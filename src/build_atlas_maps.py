"""Build and refresh the HED-to-Cognitive-Atlas mapping tables in data/mappings/.

Four TSV files, each keyed by a unique entity id, two per axis:

    hed_task_to_atlas.tsv        one row per HED task        (key hedtsk_id)
    atlas_task_to_hed.tsv        one row per Atlas task      (key atlas_id)
    hed_process_to_atlas.tsv     one row per HED process     (key hed_process_id)
    atlas_concept_to_hed.tsv     one row per Atlas concept   (key atlas_concept_id)

A HED task often corresponds to several Atlas entries. The forward table records the
primary match; the reverse table records every Atlas entry and which HED entity it maps
to, so the fan-out is preserved there. Filtering the reverse table by `hedtsk_id` gives
all Atlas entries for one HED task.

This script is NON-DESTRUCTIVE. On a first run it writes candidate rows from automated
name and alias matching. On later runs it refreshes only the columns derived from the
Atlas archive (names, counts, classes, scope classes), leaves the curated columns
(`match_type`, the mapped id, and `notes`) exactly as found, and reports entities that
have appeared in or disappeared from the Atlas since the last run.

Candidate matches are a starting point, not an answer. Automated name matching on this
data produces both false positives (`Judgment-of-Learning` and `Judgment of Line
Orientation` share the abbreviation "JOL") and false negatives, so every row needs
checking by hand before the mapping is trusted.

    python src/build_atlas_maps.py                # create or refresh all four tables
    python src/build_atlas_maps.py --report       # show drift and curation progress only
"""

from __future__ import annotations

import argparse
import collections
import csv
import json
import re
from pathlib import Path

REPO = Path(__file__).parent.parent
DEFAULT_ARCHIVE = REPO / ".cog_data"
DEFAULT_DATA = REPO / "data"
MAP_DIR_NAME = "mappings"

# Columns the curator owns. A refresh never overwrites these.
CURATED = {
    "match_type",
    "match_level",
    "atlas_id",
    "hedtsk_id",
    "hed_variation_id",
    "atlas_concept_id",
    "hed_process_id",
    "notes",
}

MATCH_TYPES = ("exact", "close", "related", "none", "")

# Rule-derived classification of what an Atlas task entry is. Applied in order.
# This is a heuristic on the entry name, not a hand-checked judgement.
SCOPE_RULES = [
    ("questionnaire", r"\b(scale|questionnaire|inventory|survey|checklist|self-?report|index)\b"),
    ("battery", r"\b(wechsler|wais|wisc|wms|battery|nih toolbox|subtest|cantab|penn)\b"),
    ("imaging_protocol", r"\b(fmri|localizer|resting|checkerboard|retinotopic)\b"),
    ("physiological", r"\b(stimulation|pain|heat|cold pressor|acupuncture|thermal|shock)\b"),
]


# ---------------------------------------------------------------------------
# Loading
# ---------------------------------------------------------------------------


def _load_listing(archive: Path, kind: str) -> list[dict]:
    path = archive / "listings" / f"{kind}.json"
    if not path.exists():
        raise SystemExit(f"Missing {path}. Run src/fetch_cog_data.py first.")
    return json.loads(path.read_text(encoding="utf-8"))


def _load_details(archive: Path, kind: str, keep: set[str]) -> dict[str, dict]:
    """Load detail records for `kind`, restricted to ids in the current listing.

    The archive is additive, so a detail file survives an entity leaving the Atlas.
    Filtering against the listing keeps stale records out of the mapping tables.
    """
    out: dict[str, dict] = {}
    directory = archive / kind
    if not directory.exists():
        return out
    for file in sorted(directory.glob("*.json")):
        record = json.loads(file.read_text(encoding="utf-8"))
        if isinstance(record, list):
            record = record[0] if record else {}
        if record.get("id") and record["id"] in keep:
            out[record["id"]] = record
    return out


# ---------------------------------------------------------------------------
# Name normalization and candidate matching
# ---------------------------------------------------------------------------


def normalize(text: str) -> str:
    """Reduce a task or concept name to a comparable key."""
    value = (text or "").lower()
    value = value.replace("&amp;", "and").replace("&#39;", "'").replace("&#34;", '"')
    value = re.sub("[\u2010-\u2015]", "-", value)  # dash variants
    value = re.sub("[\u2018\u2019]", "'", value)  # curly apostrophes
    value = re.sub(r"\(.*?\)", " ", value)  # parenthetical abbreviations
    value = re.sub(r"\b(task|test|paradigm|tasks|tests)\b", " ", value)
    value = re.sub(r"[^a-z0-9]+", " ", value)
    return " ".join(value.split())


def _keys(*names: str) -> set[str]:
    out = set()
    for name in names:
        for part in re.split(r"[;,]", name or ""):
            key = normalize(part)
            if key:
                out.add(key)
    return out


def build_index(entries: list[dict]) -> dict[str, list[dict]]:
    """Map every normalized name and alias to the entries carrying it."""
    index: dict[str, list[dict]] = collections.defaultdict(list)
    for entry in entries:
        for key in _keys(entry.get("name", ""), entry.get("alias", "")):
            index[key].append(entry)
    return index


def best_candidate(source_names: list[str], index: dict[str, list[dict]]) -> tuple[dict | None, str]:
    """Return (candidate entry, suggested match_type) for a set of source names."""
    keys = _keys(*source_names)

    # An exact hit on any name or alias.
    for key in sorted(keys):
        if key in index:
            return index[key][0], "exact"

    # Otherwise the highest Jaccard overlap above a deliberately low bar, so that
    # plausible pairs surface for review rather than being silently dropped.
    best: tuple[float, dict] | None = None
    for key in keys:
        left = set(key.split())
        if not left:
            continue
        for candidate_key, entries in index.items():
            right = set(candidate_key.split())
            if not right:
                continue
            score = len(left & right) / len(left | right)
            if score >= 0.5 and (best is None or score > best[0]):
                best = (score, entries[0])
    if best:
        return best[1], "close"
    return None, "none"


def scope_class(name: str) -> str:
    lowered = (name or "").lower()
    for label, pattern in SCOPE_RULES:
        if re.search(pattern, lowered):
            return label
    return "paradigm"


def _definition_length(record: dict) -> int:
    return len((record.get("definition_text") or "").strip())


# ---------------------------------------------------------------------------
# TSV read / write with curation preserved
# ---------------------------------------------------------------------------


def read_tsv(path: Path) -> dict[str, dict]:
    """Read an existing table, keyed by its first column. Empty if absent."""
    if not path.exists():
        return {}
    with path.open(encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle, delimiter="\t")
        key_field = reader.fieldnames[0] if reader.fieldnames else None
        if not key_field:
            return {}
        return {row[key_field]: row for row in reader if row.get(key_field)}


def write_tsv(path: Path, fieldnames: list[str], rows: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fieldnames, delimiter="\t", lineterminator="\n", extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            for field in fieldnames:
                value = str(row.get(field, "") or "")
                if "\t" in value or "\n" in value or "\r" in value:
                    raise SystemExit(f"{path.name}: field {field!r} contains a tab or newline: {value!r}")
                row[field] = value
            writer.writerow(row)


def merge(
    existing: dict[str, dict],
    candidates: list[dict],
    key_field: str,
    rederive=None,
) -> tuple[list[dict], dict]:
    """Overlay fresh derived columns onto curated rows. Returns (rows, drift).

    Where a curated row exists, its curated fields win. The descriptive columns are
    then re-derived from the curated target id, never from the automated candidate --
    otherwise a refresh would leave a row whose `atlas_name` describes a different
    record from its `atlas_id`.
    """
    rows = []
    for candidate in candidates:
        key = candidate[key_field]
        prior = existing.get(key)
        if prior:
            merged = dict(candidate)
            for field in CURATED:
                if field in prior:
                    merged[field] = prior[field]
            if rederive is not None:
                rederive(merged)
            rows.append(merged)
        else:
            rows.append(candidate)
    drift = {
        "added": sorted({c[key_field] for c in candidates} - set(existing)),
        "removed": sorted(set(existing) - {c[key_field] for c in candidates}),
    }
    return rows, drift


# ---------------------------------------------------------------------------
# Table builders
# ---------------------------------------------------------------------------

TASK_FORWARD_FIELDS = [
    "hedtsk_id",
    "hed_task_name",
    "match_type",
    "atlas_id",
    "atlas_name",
    "atlas_def_chars",
    "atlas_concept_count",
    "atlas_entry_count",
    "notes",
]

TASK_REVERSE_FIELDS = [
    "atlas_id",
    "atlas_name",
    "atlas_def_chars",
    "atlas_concept_count",
    "scope_class",
    "match_type",
    "match_level",
    "hedtsk_id",
    "hed_task_name",
    "hed_variation_id",
    "hed_variation_name",
    "notes",
]

PROCESS_FORWARD_FIELDS = [
    "hed_process_id",
    "hed_process_name",
    "hed_category_id",
    "match_type",
    "atlas_concept_id",
    "atlas_concept_name",
    "atlas_concept_class",
    "atlas_task_count",
    "atlas_concept_matches",
    "notes",
]

CONCEPT_REVERSE_FIELDS = [
    "atlas_concept_id",
    "atlas_concept_name",
    "atlas_concept_class",
    "atlas_task_count",
    "relation_count",
    "match_type",
    "hed_process_id",
    "hed_process_name",
    "notes",
]


def build_task_tables(
    hed_tasks: list[dict], atlas_tasks: list[dict], atlas_details: dict[str, dict]
) -> tuple[list[dict], list[dict]]:
    atlas_index = build_index(atlas_tasks)
    hed_index = build_index(
        [{"name": t["canonical_name"], "alias": ";".join(t.get("aliases") or [])} | {"hed": t} for t in hed_tasks]
    )

    def detail(atlas_id: str) -> dict:
        return atlas_details.get(atlas_id, {})

    forward = []
    for task in sorted(hed_tasks, key=lambda t: t["canonical_name"]):
        names = [task["canonical_name"], *(task.get("aliases") or [])]
        candidate, match_type = best_candidate(names, atlas_index)
        atlas_id = candidate["id"] if candidate else ""
        record = detail(atlas_id)
        forward.append(
            {
                "hedtsk_id": task["hedtsk_id"],
                "hed_task_name": task["canonical_name"],
                "match_type": match_type,
                "atlas_id": atlas_id,
                "atlas_name": candidate["name"] if candidate else "",
                "atlas_def_chars": _definition_length(record) if record else "",
                "atlas_concept_count": len(record.get("concepts") or []) if record else "",
                "atlas_entry_count": "",
                "notes": "",
            }
        )

    # Atlas entries are often a named variant of a paradigm rather than the paradigm
    # itself, so a variation name is tried before falling back to a task name.
    variation_index: dict[str, list[dict]] = collections.defaultdict(list)
    for task in hed_tasks:
        for variation in task.get("variations") or []:
            key = normalize(variation.get("name", ""))
            if key:
                variation_index[key].append({"task": task, "variation": variation})

    reverse = []
    for entry in sorted(atlas_tasks, key=lambda e: (e.get("name") or "").lower()):
        record = detail(entry["id"])
        names = [entry.get("name", ""), entry.get("alias", "")]

        # Precedence matters. An Atlas entry that names a HED task outright is a
        # task-level match even when some other task lists a variation by that name:
        # `2-stage decision task` is the Two-Stage Decision Task, not a variation of
        # Instrumental Conditioning. Only when no task name matches is a variation
        # name considered.
        keys = sorted(_keys(*names))
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
                "atlas_id": entry["id"],
                "atlas_name": entry.get("name", ""),
                "atlas_def_chars": _definition_length(record),
                "atlas_concept_count": len(record.get("concepts") or []),
                "scope_class": scope_class(entry.get("name", "")),
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


def build_process_tables(
    processes: list[dict],
    concepts: list[dict],
    concept_details: dict[str, dict],
    task_counts: collections.Counter,
) -> tuple[list[dict], list[dict]]:
    concept_index = build_index(concepts)
    process_index = build_index([{"name": p["process_name"], "alias": ""} | {"hed": p} for p in processes])

    def concept_class(entry: dict) -> str:
        return entry.get("id_concept_class") or ""

    forward = []
    for process in sorted(processes, key=lambda p: p["process_name"]):
        candidate, match_type = best_candidate([process["process_name"]], concept_index)
        forward.append(
            {
                "hed_process_id": process["process_id"],
                "hed_process_name": process["process_name"],
                # The category the process is filed under (its primary membership).
                "hed_category_id": next(m["category_id"] for m in process["categories"] if m["role"] == "primary"),
                "match_type": match_type,
                "atlas_concept_id": candidate["id"] if candidate else "",
                "atlas_concept_name": candidate["name"] if candidate else "",
                "atlas_concept_class": concept_class(candidate) if candidate else "",
                "atlas_task_count": task_counts.get(candidate["id"], 0) if candidate else "",
                "atlas_concept_matches": "",
                "notes": "",
            }
        )

    reverse = []
    for entry in sorted(concepts, key=lambda e: (e.get("name") or "").lower()):
        record = concept_details.get(entry["id"], {})
        candidate, match_type = best_candidate([entry.get("name", ""), entry.get("alias", "")], process_index)
        hed = candidate["hed"] if candidate else None
        reverse.append(
            {
                "atlas_concept_id": entry["id"],
                "atlas_concept_name": entry.get("name", ""),
                "atlas_concept_class": concept_class(entry),
                "atlas_task_count": task_counts.get(entry["id"], 0),
                "relation_count": len(record.get("relationships") or []),
                "match_type": match_type,
                "hed_process_id": hed["process_id"] if hed else "",
                "hed_process_name": hed["process_name"] if hed else "",
                "notes": "",
            }
        )

    return forward, reverse


# ---------------------------------------------------------------------------


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument(
        "--data", type=Path, default=DEFAULT_DATA, help="the data/ directory holding the catalog and mappings/"
    )
    parser.add_argument("--report", action="store_true", help="report only, write nothing")
    args = parser.parse_args()

    map_dir = args.data / MAP_DIR_NAME

    hed_tasks = json.loads((args.data / "task_details.json").read_text(encoding="utf-8"))
    process_data = json.loads((args.data / "process_details.json").read_text(encoding="utf-8"))
    processes = process_data["processes"]

    atlas_tasks = _load_listing(args.archive, "task")
    atlas_concepts = _load_listing(args.archive, "concept")
    task_details = _load_details(args.archive, "task", {t["id"] for t in atlas_tasks if t.get("id")})
    concept_details = _load_details(args.archive, "concept", {c["id"] for c in atlas_concepts if c.get("id")})

    # Atlas task counts per concept, from the task side.
    concept_task_counts: collections.Counter = collections.Counter()
    for record in task_details.values():
        for concept in record.get("concepts") or []:
            concept_task_counts[concept.get("concept_id") or concept.get("id")] += 1

    task_forward, task_reverse = build_task_tables(hed_tasks, atlas_tasks, task_details)
    proc_forward, proc_reverse = build_process_tables(processes, atlas_concepts, concept_details, concept_task_counts)

    # Re-derivation rules: rebuild the descriptive columns from whatever id the
    # curator settled on, so a row can never describe a record it does not point at.
    atlas_task_by_id = {t["id"]: t for t in atlas_tasks}
    atlas_concept_by_id = {c["id"]: c for c in atlas_concepts}
    hed_task_by_id = {t["hedtsk_id"]: t for t in hed_tasks}
    process_by_id = {p["process_id"]: p for p in processes}

    def rederive_task_forward(row: dict) -> None:
        entry = atlas_task_by_id.get(row.get("atlas_id") or "")
        detail = task_details.get(row.get("atlas_id") or "", {})
        row["atlas_name"] = entry.get("name", "") if entry else ""
        row["atlas_def_chars"] = _definition_length(detail) if entry else ""
        row["atlas_concept_count"] = len(detail.get("concepts") or []) if entry else ""

    variation_by_id = {
        v["variation_id"]: (t, v) for t in hed_tasks for v in (t.get("variations") or []) if v.get("variation_id")
    }

    def rederive_task_reverse(row: dict) -> None:
        hed = hed_task_by_id.get(row.get("hedtsk_id") or "")
        row["hed_task_name"] = hed["canonical_name"] if hed else ""
        vid = row.get("hed_variation_id") or ""
        if vid:
            found = variation_by_id.get(vid)
            if not found:
                raise SystemExit(
                    f"atlas_task_to_hed.tsv: row {row['atlas_id']} references unknown "
                    f"variation id {vid!r}. Rerun src/add_variation_ids.py or fix the row."
                )
            parent, variation = found
            if parent["hedtsk_id"] != row.get("hedtsk_id"):
                raise SystemExit(
                    f"atlas_task_to_hed.tsv: row {row['atlas_id']} maps to variation {vid!r} "
                    f"but names task {row.get('hedtsk_id')!r}, whose parent is "
                    f"{parent['hedtsk_id']!r}."
                )
            row["hed_variation_name"] = variation.get("name", "")
        else:
            row["hed_variation_name"] = ""

    def rederive_process_forward(row: dict) -> None:
        entry = atlas_concept_by_id.get(row.get("atlas_concept_id") or "")
        row["atlas_concept_name"] = entry.get("name", "") if entry else ""
        row["atlas_concept_class"] = (entry.get("id_concept_class") or "") if entry else ""
        row["atlas_task_count"] = concept_task_counts.get(row["atlas_concept_id"], 0) if entry else ""

    def rederive_concept_reverse(row: dict) -> None:
        process = process_by_id.get(row.get("hed_process_id") or "")
        row["hed_process_name"] = process["process_name"] if process else ""

    tables = [
        ("hed_task_to_atlas.tsv", TASK_FORWARD_FIELDS, task_forward, "hedtsk_id", rederive_task_forward),
        ("atlas_task_to_hed.tsv", TASK_REVERSE_FIELDS, task_reverse, "atlas_id", rederive_task_reverse),
        ("hed_process_to_atlas.tsv", PROCESS_FORWARD_FIELDS, proc_forward, "hed_process_id", rederive_process_forward),
        ("atlas_concept_to_hed.tsv", CONCEPT_REVERSE_FIELDS, proc_reverse, "atlas_concept_id", rederive_concept_reverse),
    ]

    merged: dict[str, list[dict]] = {}
    for filename, _fields, candidates, key_field, rederive in tables:
        path = map_dir / filename
        existing = read_tsv(path)
        rows, drift = merge(existing, candidates, key_field, rederive)
        merged[filename] = rows
        status = "create" if not existing else "refresh"
        curated = sum(1 for r in rows if (r.get("notes") or "").strip())
        print(f"{filename}: {status}, {len(rows)} rows, {curated} with curator notes")
        if drift["added"]:
            print(f"  added since last run ({len(drift['added'])}): {drift['added'][:6]}")
        if drift["removed"]:
            print(f"  removed since last run ({len(drift['removed'])}): {drift['removed'][:6]}")

    # Cross-table counts, computed from the merged rows so that a refresh reflects
    # curated mappings rather than the automated candidates they replaced.
    entry_counts = collections.Counter(r["hedtsk_id"] for r in merged["atlas_task_to_hed.tsv"] if r["hedtsk_id"])
    for row in merged["hed_task_to_atlas.tsv"]:
        row["atlas_entry_count"] = entry_counts.get(row["hedtsk_id"], 0)
    concept_matches = collections.Counter(
        r["hed_process_id"] for r in merged["atlas_concept_to_hed.tsv"] if r["hed_process_id"]
    )
    for row in merged["hed_process_to_atlas.tsv"]:
        row["atlas_concept_matches"] = concept_matches.get(row["hed_process_id"], 0)

    if not args.report:
        for filename, fields, _, _, _ in tables:
            write_tsv(map_dir / filename, fields, merged[filename])

    if args.report:
        print("\n--report given; nothing written.")


if __name__ == "__main__":
    main()
