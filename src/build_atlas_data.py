"""Recompute data/atlas_summary.json from the .cog_data archive.

`.cog_data/` is a byte-exact archive of the Cognitive Atlas REST API, written by
`src/fetch_cog_data.py` and untracked. This script reads it and writes a small JSON
summary that the documentation generators consume, so that `python src/generate_docs.py`
and the CI docs build need only the committed summary, never the archive.

Run it by hand whenever the archive is refreshed:

    python src/fetch_cog_data.py        # refresh .cog_data/
    python src/build_atlas_data.py      # recompute data/atlas_summary.json

Expected archive layout::

    <archive>/MANIFEST.json            provenance for every stored response
    <archive>/listings/concept.json    bulk concept listing
    <archive>/listings/task.json       bulk task listing
    <archive>/concept/<id>.json        per-concept detail
    <archive>/task/<id>.json           per-task detail

Both layers must come from the same archive run. The concept layer matters: a harvest
taken from the task endpoint alone reaches a concept only when some task asserts it,
which hides roughly half the concepts and all of the concept-to-concept relations.

This module reads the archive but never rewrites it. Statistics belong here, not there.
"""

from __future__ import annotations

import argparse
import collections
import json
import re
import statistics
from pathlib import Path

DEFAULT_ARCHIVE = Path(__file__).parent.parent / ".cog_data"

# The ten top-level concept classes of the Cognitive Atlas ontology.
CONCEPT_CLASSES = {
    "ctp_C1": "Perception",
    "ctp_C2": "Attention",
    "ctp_C3": "Reasoning and Decision Making",
    "ctp_C4": "Executive/Cognitive Control",
    "ctp_C5": "Learning and Memory",
    "ctp_C6": "Language",
    "ctp_C7": "Action",
    "ctp_C8": "Emotion",
    "ctp_C9": "Social Function",
    "ctp_C10": "Motivation",
    "": "(no class assigned)",
}

# A definition that is absent, or serialized from a null, or left as a curation
# placeholder. The API returns Python's ``None`` as the four-character string
# "None" for records whose definition field is empty in the bulk listing.
_MISSING = re.compile(r"^\s*(none|null|n/?a|-|\.)?\s*$", re.IGNORECASE)
_PLACEHOLDER = re.compile(r"add definition here|write definition here|disambiguation", re.IGNORECASE)

# Name-based classification of what kind of thing a task entry is. Applied in order;
# an entry is counted once, under the first pattern it matches. This is a lower
# bound -- it catches entries whose name declares the type, not every instance.
_ENTRY_TYPES = [
    (
        "Rating scale, questionnaire, or inventory",
        r"\b(scale|questionnaire|inventory|survey|checklist|self-?report|index)\b",
    ),
    (
        "Standardized test or battery",
        r"\b(wechsler|wais|wisc|wms|battery|nih toolbox|subtest|cantab|penn)\b",
    ),
    (
        "Imaging protocol or localizer label",
        r"\b(fmri|localizer|resting|rest|checkerboard|retinotopic)\b",
    ),
    (
        "Stimulation or physiological procedure",
        r"\b(stimulation|pain|heat|cold pressor|acupuncture|thermal|shock)\b",
    ),
]

# Paradigm families reported as evidence of variant fragmentation.
_FAMILIES = [
    "sternberg",
    "stroop",
    "n-back",
    "span",
    "fluency",
    "naming",
    "stop signal",
    "oddball",
    "weather prediction",
    "continuous performance",
    "bandit",
]


def _definition(record: dict) -> str:
    """Return the record's definition, or "" when it is absent or a placeholder."""
    text = (record.get("definition_text") or "").strip()
    if _MISSING.match(text) or _PLACEHOLDER.search(text):
        return ""
    return text


def _bucket(counter: collections.Counter, order: list[str], total: int) -> list[dict]:
    """Render a counter as an ordered list of {label, count, percent} rows."""
    return [{"label": label, "count": counter[label], "percent": round(100 * counter[label] / total, 1)} for label in order]


def _load_listing(path: Path) -> list[dict]:
    if not path.exists():
        raise SystemExit(f"Missing listing: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def _load_details(directory: Path, keep: set[str]) -> dict[str, dict]:
    """Load archived detail records in directory, keyed by record id.

    Only ids present in `keep`, the current bulk listing, are returned. The archive is
    additive: `fetch_cog_data.py` does not delete a detail file when an entity leaves
    the Atlas, so globbing the directory would otherwise fold records for entities that
    no longer exist into the statistics.

    A detail response is a one-element list wrapping the record, so unwrap it.
    """
    out: dict[str, dict] = {}
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
# Tasks
# ---------------------------------------------------------------------------


def _task_stats(tasks: list[dict]) -> dict:
    total = len(tasks)

    defs: collections.Counter = collections.Counter()
    for task in tasks:
        length = len(_definition(task))
        if length == 0:
            defs["Missing or placeholder"] += 1
        elif length < 50:
            defs["Under 50 characters"] += 1
        elif length < 200:
            defs["50 to 199"] += 1
        elif length < 500:
            defs["200 to 499"] += 1
        elif length < 1000:
            defs["500 to 999"] += 1
        else:
            defs["1000 or more"] += 1
    def_order = [
        "Missing or placeholder",
        "Under 50 characters",
        "50 to 199",
        "200 to 499",
        "500 to 999",
        "1000 or more",
    ]
    real_lengths = [len(_definition(t)) for t in tasks if _definition(t)]

    links: collections.Counter = collections.Counter()
    for task in tasks:
        n = len(task.get("concepts") or [])
        if n == 0:
            links["0 concepts"] += 1
        elif n == 1:
            links["1 concept"] += 1
        elif n <= 3:
            links["2 to 3"] += 1
        elif n <= 7:
            links["4 to 7"] += 1
        else:
            links["8 or more"] += 1
    link_order = ["0 concepts", "1 concept", "2 to 3", "4 to 7", "8 or more"]
    total_links = sum(len(t.get("concepts") or []) for t in tasks)

    cited = sum(1 for t in tasks if t.get("citation"))
    citations = [c for t in tasks for c in (t.get("citation") or [])]
    with_pmid = sum(1 for c in citations if (c.get("citation_pmid") or "").strip())

    fields = []
    for field, label in [
        ("contrasts", "Contrasts"),
        ("indicators", "Indicators"),
        ("conditions", "Conditions"),
        ("batteries", "Batteries"),
        ("external_datasets", "External datasets"),
        ("implementations", "Implementations"),
        ("disorders", "Disorders"),
    ]:
        n = sum(1 for t in tasks if t.get(field))
        fields.append(
            {
                "label": label,
                "tasks": n,
                "percent": round(100 * n / total, 1),
                "entries": sum(len(t.get(field) or []) for t in tasks),
            }
        )

    return {
        "total": total,
        "definitions": _bucket(defs, def_order, total),
        "definition_mean": round(statistics.mean(real_lengths)),
        "definition_median": round(statistics.median(real_lengths)),
        "definition_max": max(real_lengths),
        "definition_real_count": len(real_lengths),
        "concept_links": _bucket(links, link_order, total),
        "concept_link_total": total_links,
        "concept_link_mean": round(total_links / total, 2),
        "concept_link_max": max(len(t.get("concepts") or []) for t in tasks),
        "cited": cited,
        "cited_percent": round(100 * cited / total, 1),
        "uncited": total - cited,
        "uncited_percent": round(100 * (total - cited) / total, 1),
        "citation_total": len(citations),
        "citation_with_pmid": with_pmid,
        "complete": sum(1 for t in tasks if t.get("citation") and (t.get("concepts") or []) and _definition(t)),
        "no_citation_no_concepts": sum(1 for t in tasks if not t.get("citation") and not (t.get("concepts") or [])),
        "no_definition_no_concepts": sum(1 for t in tasks if not _definition(t) and not (t.get("concepts") or [])),
        "fields": fields,
    }


# ---------------------------------------------------------------------------
# Concepts
# ---------------------------------------------------------------------------


def _concept_stats(concepts: list[dict], details: dict[str, dict], task_links: collections.Counter) -> dict:
    total = len(concepts)
    by_id = {c["id"]: c for c in concepts if c.get("id")}
    linked_ids = {cid for cid in task_links if cid in by_id}
    orphan_ids = set(by_id) - linked_ids

    defs: collections.Counter = collections.Counter()
    for concept in concepts:
        length = len(_definition(concept))
        if length == 0:
            defs["Missing or placeholder"] += 1
        elif length < 30:
            defs["Under 30 characters"] += 1
        elif length < 150:
            defs["30 to 149"] += 1
        else:
            defs["150 or more"] += 1
    def_order = ["Missing or placeholder", "Under 30 characters", "30 to 149", "150 or more"]

    spread: collections.Counter = collections.Counter()
    for cid in by_id:
        n = task_links.get(cid, 0)
        if n == 0:
            spread["0 tasks"] += 1
        elif n == 1:
            spread["1 task"] += 1
        elif n == 2:
            spread["2 tasks"] += 1
        elif n <= 9:
            spread["3 to 9 tasks"] += 1
        else:
            spread["10 or more tasks"] += 1
    spread_order = ["0 tasks", "1 task", "2 tasks", "3 to 9 tasks", "10 or more tasks"]

    by_class: collections.Counter = collections.Counter()
    for concept in concepts:
        by_class[concept.get("id_concept_class") or ""] += 1
    classes = [
        {
            "label": CONCEPT_CLASSES.get(key, key),
            "concepts": count,
            "percent": round(100 * count / total, 1),
        }
        for key, count in by_class.most_common()
    ]

    def profile(ids: set) -> dict:
        group = [by_id[i] for i in ids]
        if not group:
            return {"total": 0}
        no_def = sum(1 for c in group if not _definition(c))
        no_class = sum(1 for c in group if not (c.get("id_concept_class") or ""))
        lengths = [len(_definition(c)) for c in group if _definition(c)]
        return {
            "total": len(group),
            "percent": round(100 * len(group) / total, 1),
            "no_definition": no_def,
            "no_definition_percent": round(100 * no_def / len(group), 1),
            "no_class": no_class,
            "no_class_percent": round(100 * no_class / len(group), 1),
            "definition_median": round(statistics.median(lengths)) if lengths else 0,
        }

    top = [{"name": by_id[cid]["name"], "tasks": n} for cid, n in task_links.most_common() if cid in by_id][:15]

    unclassified = sorted(
        (
            {"name": by_id[cid]["name"], "tasks": task_links.get(cid, 0)}
            for cid in by_id
            if not (by_id[cid].get("id_concept_class") or "")
        ),
        key=lambda row: (-row["tasks"], row["name"]),
    )

    # Relations and citations come from the per-concept detail records.
    relations: collections.Counter = collections.Counter()
    with_relations = with_citations = 0
    citation_total = 0
    for record in details.values():
        rels = record.get("relationships") or []
        if rels:
            with_relations += 1
        for rel in rels:
            relations[rel.get("relationship") or "(unlabelled)"] += 1
        cits = record.get("citations") or []
        if cits:
            with_citations += 1
        citation_total += len(cits)

    detail_n = len(details) or 1
    names = collections.Counter((c.get("name") or "").strip().lower() for c in concepts)

    return {
        "total": total,
        "definitions": _bucket(defs, def_order, total),
        "task_spread": _bucket(spread, spread_order, total),
        "classes": classes,
        "unclassified": by_class[""],
        "unclassified_percent": round(100 * by_class[""] / total, 1),
        "linked": profile(linked_ids),
        "orphans": profile(orphan_ids),
        "top_concepts": top,
        "top_unclassified": unclassified[:12],
        "placeholder_names": sorted(c["name"] for c in concepts if not _definition(c)),
        "duplicate_names": sorted(k for k, v in names.items() if v > 1),
        "detail_records": len(details),
        "relations": [{"label": label, "count": count} for label, count in relations.most_common()],
        "relation_total": sum(relations.values()),
        "with_relations": with_relations,
        "with_relations_percent": round(100 * with_relations / detail_n, 1),
        "with_citations": with_citations,
        "with_citations_percent": round(100 * with_citations / detail_n, 1),
        "citation_total": citation_total,
    }


# ---------------------------------------------------------------------------
# Cross-cutting
# ---------------------------------------------------------------------------


def _hygiene(tasks: list[dict], concepts: list[dict]) -> dict:
    entities = re.compile(r"&#\d+;|&[a-z]{2,6};")
    mojibake = re.compile(r"[\u00c2\u00c3\u00e2][\u0080-\u00bf]")

    def count(records, pattern):
        return sum(1 for r in records if pattern.search(r.get("definition_text") or ""))

    task_names = collections.Counter((t.get("name") or "").strip().lower() for t in tasks if (t.get("name") or "").strip())
    return {
        "task_entities": count(tasks, entities),
        "task_mojibake": count(tasks, mojibake),
        "concept_entities": count(concepts, entities),
        "concept_mojibake": count(concepts, mojibake),
        "duplicate_task_names": sorted(k for k, v in task_names.items() if v > 1),
        "unnamed_tasks": [t["id"] for t in tasks if not (t.get("name") or "").strip()],
        "null_definition_tasks": sum(1 for t in tasks if (t.get("definition_text") or "").strip() == "None"),
        "null_definition_concepts": sum(1 for c in concepts if (c.get("definition_text") or "").strip() == "None"),
    }


def _entry_types(tasks: list[dict]) -> list[dict]:
    counts: collections.Counter = collections.Counter()
    assigned = set()
    for task in tasks:
        name = (task.get("name") or "").lower()
        for label, pattern in _ENTRY_TYPES:
            if re.search(pattern, name):
                counts[label] += 1
                assigned.add(task["id"])
                break
    rows = [{"label": label, "count": counts[label]} for label, _ in _ENTRY_TYPES]
    rows.append({"label": "Not matched (largely experimental paradigms)", "count": len(tasks) - len(assigned)})
    return rows


def _fragmentation(tasks: list[dict]) -> list[dict]:
    rows = []
    for family in _FAMILIES:
        hits = [t for t in tasks if family in (t.get("name") or "").lower()]
        if len(hits) < 2:
            continue
        best = max(hits, key=lambda h: len(h.get("concepts") or []))
        rows.append(
            {
                "family": family,
                "entries": len(hits),
                "zero_concept_entries": sum(1 for h in hits if not (h.get("concepts") or [])),
                "best_entry": best.get("name"),
                "best_concepts": len(best.get("concepts") or []),
            }
        )
    rows.sort(key=lambda r: -r["entries"])
    return rows


def _tiers(tasks: list[dict]) -> list[dict]:
    counts: collections.Counter = collections.Counter()
    for task in tasks:
        length = len(_definition(task))
        n = len(task.get("concepts") or [])
        if length < 50 or n == 0:
            counts["Skeletal"] += 1
        elif length >= 300 and n >= 4:
            counts["Well annotated"] += 1
        elif length >= 100 and n >= 1:
            counts["Adequate"] += 1
        else:
            counts["Minimal"] += 1
    return _bucket(counts, ["Well annotated", "Adequate", "Minimal", "Skeletal"], len(tasks))


def _years(tasks: list[dict], concepts: list[dict]) -> list[dict]:
    def tally(records):
        counter: collections.Counter = collections.Counter()
        for record in records:
            stamp = record.get("event_stamp") or ""
            counter[stamp[:4] if len(stamp) >= 4 else "(none)"] += 1
        return counter

    task_years = tally(tasks)
    concept_years = tally(concepts)
    years = sorted(set(task_years) | set(concept_years))
    return [{"year": y, "tasks": task_years.get(y, 0), "concepts": concept_years.get(y, 0)} for y in years]


# ---------------------------------------------------------------------------


def build(archive: Path) -> dict:
    concepts = _load_listing(archive / "listings" / "concept.json")
    task_listing = _load_listing(archive / "listings" / "task.json")
    task_ids = {t["id"] for t in task_listing if t.get("id")}
    concept_ids = {c["id"] for c in concepts if c.get("id")}
    task_details = _load_details(archive / "task", task_ids)
    concept_details = _load_details(archive / "concept", concept_ids)

    if not task_details:
        raise SystemExit(f"No task detail records under {archive / 'task'}. Run src/fetch_cog_data.py first.")

    # Statistics come from detail records only. A listing record carries no concepts,
    # contrasts or citations, so substituting one for a missing detail would silently
    # understate those counts; a missing detail reduces the denominator instead, and
    # the inventory reports listed against retrieved so the shortfall is visible.
    missing = sorted(task_ids - set(task_details))
    if missing:
        print(
            f"WARNING: {len(missing)} listed tasks have no detail record and are "
            f"excluded from the statistics: {missing[:5]}"
            f"{' ...' if len(missing) > 5 else ''}. Run src/fetch_cog_data.py to complete the archive."
        )
    tasks = [task_details[t["id"]] for t in task_listing if t.get("id") in task_details]

    task_links: collections.Counter = collections.Counter()
    for task in tasks:
        for concept in task.get("concepts") or []:
            task_links[concept.get("concept_id") or concept.get("id")] += 1

    manifest_path = archive / "MANIFEST.json"
    manifest = json.loads(manifest_path.read_text(encoding="utf-8")) if manifest_path.exists() else {}

    return {
        "archive_name": archive.name,
        "harvested_on": manifest.get("started_on", ""),
        "inventory": {
            "tasks_listed": len(task_listing),
            "task_records": len(task_details),
            "concepts_listed": len(concepts),
            "concept_records": len(concept_details),
        },
        "tasks": _task_stats(tasks),
        "concepts": _concept_stats(concepts, concept_details, task_links),
        "hygiene": _hygiene(tasks, concepts),
        "entry_types": _entry_types(tasks),
        "fragmentation": _fragmentation(tasks),
        "tiers": _tiers(tasks),
        "years": _years(tasks, concepts),
    }


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--archive", type=Path, default=DEFAULT_ARCHIVE)
    parser.add_argument(
        "--out",
        type=Path,
        default=Path(__file__).parent.parent / "data" / "atlas_summary.json",
    )
    args = parser.parse_args()

    if not args.archive.exists():
        raise SystemExit(f"Archive not found: {args.archive}. Run src/fetch_cog_data.py first.")

    summary = build(args.archive)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(
        json.dumps(summary, indent=2, ensure_ascii=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    print(f"Wrote {args.out} ({summary['tasks']['total']} tasks, {summary['concepts']['total']} concepts).")


if __name__ == "__main__":
    main()
