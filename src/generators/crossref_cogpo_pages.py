"""Generate the CogPO fragments in docs/source/_generated/ from data/mappings/ and data/facet_defs.tsv.

The hand-written pages under docs/source/cogpo/ carry the prose and pull these fragments
in with an include directive, so that the tables stay current while the explanation
around them stays editable. The TSVs are the source of record; the fragments are one
view of them and hold no judgements of their own.

Fragments written (each one Markdown table, one run of headed tables, or one sentence):

- cogpo_task_forward.md          one row per task: its primary CogPO paradigm class
- cogpo_paradigm_matched.md      one row per CogPO class with a counterpart in the Catalog
- cogpo_paradigm_unmatched.md    CogPO classes with no counterpart, grouped by what the
                                 class is (### heading per group)
- mapping_cogpo_forward.md       tasks by match type of their CogPO class
- mapping_cogpo_reverse.md       CogPO classes by match type of their counterpart
- mapping_cogpo_reverse_scope.md unmatched CogPO classes by kind
- mapping_cogpo_level.md         matched CogPO classes resolved to a task or a variation
- cogpo_matched_line.md          one sentence with the matched-class counts
- cogpo_dimension_<facet>.md     one table per facet: value, CogPO term, definition, HED tags
- cogpo_dimension_coverage.md    per facet, how many values come from where and how many
                                 have a HED tag
- cogpo_hed_line.md              one sentence on how many CogPO values have a HED tag

Rows are rendered in full rather than summarized, so that a reader can look up any
single task or CogPO class without opening the data files. Links inside a fragment are
relative to the including page (docs/source/cogpo/), as MyST parses an included
fragment as part of the including document.
"""

from __future__ import annotations

import collections
import urllib.parse
from pathlib import Path

from generators.utils import cell as _cell
from generators.utils import load_json, write_page
from generators.utils import read_tsv as _read
from generators.utils import table as _table

MATCH_ORDER = {"exact": 0, "close": 1, "related": 2, "none": 3}

# A CogPO class name links to its page on the CogPO wiki, which is the only place the
# class can be read online: the OWL file has no per-class page. The wiki's TLS
# certificate is invalid, so the link is plain http.
WIKI_URL = "http://www.wiki.cogpo.org/index.php?title="

# Order and wording for the groups of unmatched CogPO classes.
SCOPE_LABELS = [
    ("paradigm", "Paradigms the Catalog does not list"),
    ("broad_class", "Broad classes with no single counterpart"),
    ("physiological", "Physiological procedures and interventions"),
    ("motor_act", "Motor acts"),
    ("imaging_protocol", "Imaging protocol"),
    ("pseudo_task", "Pseudo tasks"),
]

FACETS = [
    ("stimulus_modality", "Stimulus modality"),
    ("stimulus_kind", "Stimulus kind"),
    ("stimulus_role", "Stimulus role"),
    ("response_modality", "Response modality"),
    ("response_kind", "Response kind"),
    ("instructions", "Instructions"),
]

SOURCE_LABELS = {
    "cogpo": "CogPO (OWL)",
    "cogpo_wiki": "CogPO (wiki only)",
    "hed": "HED schema",
    "catalog": "Catalog addition",
}


def _match_sort(row: dict) -> tuple:
    return (MATCH_ORDER.get(row["match_type"], 9), row.get("cogpo_label", row.get("hed_task_name", "")).lower())


def _task_link(row: dict) -> str:
    return f"[{_cell(row['hed_task_name'])}](../tasks/{row['hedtsk_id']}.md)"


def _cogpo_link(cogpo_id: str, label: str, wiki_titles: dict[str, str]) -> str:
    title = wiki_titles.get(cogpo_id)
    if not title:
        return _cell(label)
    return f"[{_cell(label)}]({WIKI_URL}{urllib.parse.quote(title, safe='')})"


def _share_table(rows: list[dict], label: str) -> str:
    counts = collections.Counter(r["match_type"] for r in rows)
    return _table(
        ["Match type", label, "Share"],
        [[k, counts[k], f"{round(100 * counts[k] / len(rows))}%"] for k in ("exact", "close", "related", "none")],
    )


def _forward_table(forward: list[dict], wiki_titles: dict[str, str]) -> str:
    rows = []
    for r in sorted(forward, key=lambda r: r["hed_task_name"].lower()):
        rows.append(
            [
                _task_link(r),
                r["match_type"],
                _cogpo_link(r["cogpo_id"], r["cogpo_label"], wiki_titles) if r["cogpo_id"] else "-",
                _cell(r["notes"]),
            ]
        )
    return _table(["Task", "Match", "CogPO paradigm class", "Note"], rows)


def _matched_table(matched: list[dict], wiki_titles: dict[str, str]) -> str:
    rows = []
    for r in sorted(matched, key=_match_sort):
        target = _task_link(r)
        if r["hed_variation_id"]:
            target += f" (variation: {_cell(r['hed_variation_name'])})"
        rows.append(
            [
                _cogpo_link(r["cogpo_id"], r["cogpo_label"], wiki_titles),
                r["match_type"],
                r["match_level"],
                target,
                _cell(r["notes"]),
            ]
        )
    return _table(["CogPO paradigm class", "Match", "Level", "Catalog task", "Note"], rows)


def _unmatched_tables(unmatched: list[dict], definitions: dict[str, str], wiki_titles: dict[str, str]) -> str:
    parts = []
    for scope, heading in SCOPE_LABELS:
        group = sorted((r for r in unmatched if r["scope_class"] == scope), key=lambda r: r["cogpo_label"].lower())
        if not group:
            continue
        rows = [
            [
                _cogpo_link(r["cogpo_id"], r["cogpo_label"], wiki_titles),
                _cell(definitions.get(r["cogpo_id"], "")),
                _cell(r["notes"]),
            ]
            for r in group
        ]
        parts.append(f"### {heading}\n\n" + _table(["CogPO paradigm class", "CogPO definition", "Note"], rows))
    return "\n\n".join(parts)


def _dimension_table(rows: list[dict], wiki_titles: dict[str, str]) -> str:
    out = []
    for r in rows:
        if r["source"] in ("cogpo", "cogpo_wiki"):
            term = _cogpo_link(
                r["cogpo_id"],
                r["cogpo_id"] if r["cogpo_id"].startswith(("COGPO_", "FMA_")) else r["cogpo_id"].replace("_", " "),
                wiki_titles,
            )
        else:
            term = "-"
        tags = _cell(r["hed_tags"]) if r["hed_tags"].strip() else "(none)"
        out.append(
            [
                f"`{r['value']}`",
                _cell(r["label"]),
                term,
                _cell(r["definition"]),
                tags,
                _cell(r["hed_note"]),
                SOURCE_LABELS.get(r["source"], r["source"]),
            ]
        )
    return _table(["Value", "Label", "CogPO term", "Definition", "HED 8.4.0 tags", "HED note", "Source"], out)


def _coverage_table(defs: list[dict]) -> str:
    rows = []
    for facet, label in FACETS:
        group = [r for r in defs if r["facet"] == facet]
        by_source = collections.Counter(r["source"] for r in group)
        cogpo = [r for r in group if r["source"] in ("cogpo", "cogpo_wiki")]
        rows.append(
            [
                label,
                len(group),
                by_source["cogpo"] + by_source["cogpo_wiki"],
                by_source["hed"],
                by_source["catalog"],
                sum(1 for r in cogpo if r["hed_tags"].strip()),
                sum(1 for r in cogpo if r["hed_note"].startswith("Exact tag")),
            ]
        )
    return _table(
        [
            "Facet",
            "Values",
            "From CogPO",
            "Added from HED",
            "Added by the Catalog",
            "CogPO values with a HED tag",
            "of which an exact tag",
        ],
        rows,
    )


def generate(docs_dir: Path, data_dir: Path) -> int:
    """Write every CogPO fragment. Returns the number of files written."""
    out = docs_dir / "_generated"
    maps = data_dir / "mappings"
    forward = _read(maps / "hed_task_to_cogpo.tsv")
    reverse = _read(maps / "cogpo_paradigm_to_hed.tsv")
    defs = _read(data_dir / "facet_defs.tsv")
    summary = load_json(data_dir / "cogpo_summary.json")

    # Wiki page titles by CogPO id, for links; definitions by id, for the unmatched tables.
    wiki_titles: dict[str, str] = {}
    definitions: dict[str, str] = {}
    for p in summary["paradigms"]:
        definitions[p["id"]] = p["definition"]
        if p.get("wiki"):
            wiki_titles[p["id"]] = p["wiki"]["title"]
    for p in summary["paradigm_comparison"]["wiki_only"]:
        definitions[p["title"]] = p["definition"]
        wiki_titles[p["title"]] = p["title"]
    for dim in summary["dimensions"].values():
        for v in dim["values"]:
            if v.get("wiki"):
                wiki_titles[v["id"]] = v["wiki"]["title"]
        for v in dim["wiki_only"]:
            wiki_titles[v["title"]] = v["title"]

    matched = [r for r in reverse if r["match_type"] in ("exact", "close", "related")]
    unmatched = [r for r in reverse if r["match_type"] == "none"]
    counts = collections.Counter(r["match_type"] for r in reverse)
    variation_rows = sum(1 for r in matched if r["match_level"] == "variation")
    cogpo_values = [r for r in defs if r["source"] in ("cogpo", "cogpo_wiki")]
    tagged = sum(1 for r in cogpo_values if r["hed_tags"].strip())
    exact_tagged = sum(1 for r in cogpo_values if r["hed_note"].startswith("Exact tag"))

    fragments = {
        "cogpo_task_forward.md": _forward_table(forward, wiki_titles),
        "cogpo_paradigm_matched.md": _matched_table(matched, wiki_titles),
        "cogpo_paradigm_unmatched.md": _unmatched_tables(unmatched, definitions, wiki_titles),
        "mapping_cogpo_forward.md": _share_table(forward, "Tasks"),
        "mapping_cogpo_reverse.md": _share_table(reverse, "CogPO classes"),
        "mapping_cogpo_reverse_scope.md": _table(
            ["What the class is", "CogPO classes"],
            [
                [label, sum(1 for r in unmatched if r["scope_class"] == scope)]
                for scope, label in SCOPE_LABELS
                if scope != "pseudo_task"
            ],
        ),
        "mapping_cogpo_level.md": _table(
            ["Mapped to", "CogPO classes"],
            [
                ["A Catalog task", sum(1 for r in matched if r["match_level"] == "task")],
                ["A named variation of a Catalog task", variation_rows],
            ],
        ),
        "cogpo_matched_line.md": (
            f"Of the {len(reverse)} CogPO paradigm classes, {len(matched)} have a counterpart in the Catalog "
            f"({counts['exact']} exact, {counts['close']} close, {counts['related']} related) and "
            f"{counts['none']} have none; {variation_rows} of the matched classes resolve to a named variation "
            f"rather than a task."
        ),
        "cogpo_dimension_coverage.md": _coverage_table(defs),
        "cogpo_hed_line.md": (
            f"Of the {len(cogpo_values)} CogPO dimension values, {tagged} have a HED 8.4.0 tag and "
            f"{exact_tagged} of those are an exact tag, the same concept under the same or an equivalent name; "
            f"the rest have a nearest parent tag or none."
        ),
    }
    for facet, _label in FACETS:
        fragments[f"cogpo_dimension_{facet}.md"] = _dimension_table([r for r in defs if r["facet"] == facet], wiki_titles)

    for name, body in fragments.items():
        write_page(out / name, body + "\n")
    return len(fragments)
