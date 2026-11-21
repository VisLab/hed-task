"""Generate docs/source/_generated/ - table fragments for the hand-written pages.

Narrative pages are plain Markdown that people edit directly. Where one of them needs a
table whose contents follow the data (the counts, the five tables of the game model, the Atlas mapping
coverage), the table is written here as a fragment and the page pulls it in with

    ```{include} ../../_generated/mapping_task_forward.md
    ```

so that the prose around the table stays editable and the table stays current. Each
fragment is one Markdown table, or one sentence carrying live counts, and nothing else.
The full Atlas mapping tables are written here too, by crossref_atlas_pages.py. The
directory is excluded from the Sphinx document tree in conf.py; only includes read it.
"""

from __future__ import annotations

import collections
from pathlib import Path

from generators.utils import cell, facet_label, load_json, read_tsv, table, vocab_anchor, write_page

KINDS = ("exact", "close", "related", "none")


def _share_table(rows: list[dict], label: str) -> str:
    counts = collections.Counter(r["match_type"] for r in rows)
    return table(
        ["Match type", label, "Share"],
        [[k, counts[k], f"{round(100 * counts[k] / len(rows))}%"] for k in KINDS],
    )


def _vocab(text: str, anchor: str) -> str:
    """Return an inline-HTML link from a page at the docs root to the game vocabulary page."""
    return f'<a href="tasks/vocabulary.html#{anchor}">{text}</a>'


def _game_model_fragments(games: dict, facets: list[dict], tasks: list[dict]) -> dict[str, str]:
    """Return the tables of the game model, for the narrative pages at the docs root.

    One table for each of the five parts of the model: game types, game rules (the
    questions, not the values), game motivators, game phases, game facets. Links go to
    tasks/vocabulary.md, where the values are defined.

    Parameters:
        games: The loaded data/task_game_defs.json.
        facets: The facets of data/task_facet_defs.json.
        tasks: Task records, for the counts.
    """
    by_type = collections.Counter(t["game_type"] for t in tasks)
    answered = collections.Counter(key for t in tasks for key in t.get("motivators") or {})
    with_phase = collections.Counter(p for t in tasks for p in t.get("phases") or [])
    with_facet = collections.Counter(f for t in tasks for f in t.get("task_facets") or {})
    return {
        "game_types_table.md": table(
            ["Game type", "What the player does", "How to tell", "Rules", "Tasks"],
            [
                [
                    _vocab(g["name"], vocab_anchor("game", g["game_type"])),
                    cell(g["what_the_player_does"]),
                    cell(g.get("boundary")),
                    len(g["rules"]) or "-",
                    by_type[g["game_type"]],
                ]
                for g in games["game_types"]
            ],
        ),
        "game_rules_table.md": table(
            ["Game type", "Rule question", "Default answer", "Other answers"],
            [
                [
                    g["name"],
                    _vocab(r["question"], vocab_anchor("rule", g["game_type"], r["rule"])),
                    f"`{r['default']}`",
                    ", ".join(f"`{v['value']}`" for v in r["values"] if v["value"] != r["default"]),
                ]
                for g in games["game_types"]
                for r in g["rules"]
            ],
        ),
        "game_motivators_table.md": table(
            ["Question", "Key", "Answers", "Tasks that answer it"],
            [
                [
                    _vocab(m["question"], vocab_anchor("motivator", m["key"])),
                    f"`{m['key']}`",
                    ", ".join(f"`{v['value']}`" for v in m["values"]),
                    answered[m["key"]],
                ]
                for m in games["motivators"]
            ],
        ),
        "game_phases_table.md": table(
            ["Phase", "Definition", "Tasks whose standard form names it"],
            [
                [
                    _vocab(f"`{p['phase']}`", vocab_anchor("phase", p["phase"])),
                    cell(p["definition"]),
                    with_phase[p["phase"]] or "-",
                ]
                for p in games["phases"]
            ],
        ),
        "game_facets_table.md": table(
            ["Facet", "Question", "Values", "Tasks that state it"],
            [
                [
                    _vocab(facet_label(f["facet"]), vocab_anchor("facet", f["facet"])),
                    cell(f["question"]),
                    len(f["values"]),
                    with_facet[f["facet"]],
                ]
                for f in facets
            ],
        ),
    }


def generate(
    docs_dir: Path, working_dir: Path, tasks: list[dict], processes: list[dict], categories: list[dict], families: list[dict]
) -> int:
    """Write every fragment. Returns the number of files written."""
    out = docs_dir / "_generated"
    maps = working_dir / "mappings"
    forward = read_tsv(maps / "hed_task_to_atlas.tsv")
    reverse = read_tsv(maps / "atlas_task_to_hed.tsv")
    proc_forward = read_tsv(maps / "hed_process_to_atlas.tsv")
    concept_reverse = read_tsv(maps / "atlas_concept_to_hed.tsv")

    linked = {pid for t in tasks for pid in t.get("hed_process_ids", [])}
    games = load_json(working_dir / "task_game_defs.json")
    facets = load_json(working_dir / "task_facet_defs.json")["facets"]
    fragments = {
        **_game_model_fragments(games, facets, tasks),
        "counts_table.md": table(
            ["What", "Count", "Where"],
            [
                ["Tasks", len(tasks), "[Tasks](tasks/index.md)"],
                ["Task families the tasks are filed under", len(families), "[Tasks](tasks/index.md)"],
                ["Task variants", sum(len(t.get("variants", [])) for t in tasks), "on each task page"],
                ["Game types", len(games["game_types"]), "[Game vocabulary](tasks/vocabulary.md)"],
                [
                    "Game rules, over the game types that have them",
                    sum(len(g["rules"]) for g in games["game_types"]),
                    "[Game vocabulary](tasks/vocabulary.md)",
                ],
                [
                    "Game facets, and their values",
                    f"{len(facets)}, {sum(len(f['values']) for f in facets)}",
                    "[Game vocabulary](tasks/vocabulary.md)",
                ],
                ["Cognitive processes", len(processes), "[Cognitive processes](processes/index.md)"],
                ["Process categories", len(categories), "[Cognitive processes](processes/index.md)"],
                [
                    "Task-to-process links",
                    sum(len(t.get("hed_process_ids", [])) for t in tasks),
                    "[Task-process links](task_process_links.md)",
                ],
                [
                    "Processes engaged by at least one task",
                    sum(1 for p in processes if p["process_id"] in linked),
                    "[Task-process links](task_process_links.md)",
                ],
            ],
        ),
        "mapping_level.md": table(
            ["Mapped to", "Atlas entries"],
            [
                ["A HED task", sum(1 for r in reverse if r["match_level"] == "task")],
                ["A variant of a HED task", sum(1 for r in reverse if r["match_level"] == "variant")],
            ],
        ),
        "mapping_task_forward.md": _share_table(forward, "Tasks"),
        "mapping_task_reverse.md": _share_table(reverse, "Atlas entries"),
        "mapping_task_reverse_scope.md": table(
            ["Why no counterpart", "Atlas entries"],
            [
                [label, sum(1 for r in reverse if r["match_type"] == "none" and r["scope_class"] == scope)]
                for scope, label in (
                    ("paradigm", "Experimental paradigm not in the Catalog"),
                    ("questionnaire", "Self-report instrument"),
                    ("battery", "Standardized test battery"),
                    ("imaging_protocol", "Imaging protocol label"),
                    ("physiological", "Physiological procedure"),
                )
            ],
        ),
        "mapping_process_forward.md": _share_table(proc_forward, "Processes"),
        "mapping_process_reverse.md": _share_table(concept_reverse, "Atlas concepts"),
        "mapping_verified.md": table(
            ["Table", "Rows", "State"],
            [
                ["`hed_task_to_atlas.tsv`", len(forward), "Every row checked against the archived Atlas record"],
                ["`atlas_task_to_hed.tsv`", len(reverse), "Every row assigned a match type; every matched row checked"],
                ["`hed_process_to_atlas.tsv`", len(proc_forward), "Every row checked against the archived concept definition"],
                ["`atlas_concept_to_hed.tsv`", len(concept_reverse), "Every row assigned a match type"],
            ],
        ),
    }

    for name, body in fragments.items():
        write_page(out / name, body + "\n")
    return len(fragments)
