"""Generate the task vocabulary page and the two listings built on it.

Files written, all under docs/source/tasks/ (a generated path):

- vocabulary.md     every term a task page uses to describe a task: the game types, the
                    rules of each game type with their defaults and values, the
                    motivation questions, the phases, the settings, the ways of combining
                    games, and the nine facets with their values, definitions and HED tags
- by_game_type.md   one section per game type, listing the tasks whose standard form is
                    that game
- by_facet.md       one section per facet, one line per value: the tasks whose standard
                    form carries the value, then the variants that state it

The vocabulary comes from data/task_game_defs.json and data/task_facet_defs.json. Every
value on vocabulary.md has one stable anchor, from `vocab_anchor` in utils.py; the task
pages link to it. The task index's toctree (task_pages.py) lists the three pages.
"""

from __future__ import annotations

import html
from pathlib import Path

from generators.utils import (
    cell,
    count_phrase,
    facet_label,
    load_json,
    table,
    vocab_anchor,
    vocab_link,
    write_page,
)


def generate(docs_dir: Path, data_dir: Path, tasks: list[dict]) -> int:
    """Write vocabulary.md, by_game_type.md and by_facet.md under docs/source/tasks/.

    Parameters:
        docs_dir: The docs/source/ root.
        data_dir: The data/ directory, for the two vocabulary files.
        tasks: Task records from data/task_details.json.

    Returns:
        The number of files written.
    """
    games = load_json(data_dir / "task_game_defs.json")
    facets = load_json(data_dir / "task_facet_defs.json")["facets"]
    tasks_dir = docs_dir / "tasks"
    by_name = sorted(tasks, key=lambda t: t["canonical_name"])
    write_page(tasks_dir / "vocabulary.md", _vocabulary(games, facets))
    write_page(tasks_dir / "by_game_type.md", _by_game_type(games, by_name))
    write_page(tasks_dir / "by_facet.md", _by_facet(facets, by_name))
    return 3


def _target(anchor: str, value: str) -> str:
    """Return a table cell that carries a value's anchor and shows the value."""
    return f'<span id="{anchor}"></span>`{value}`'


def _vocabulary(games: dict, facets: list[dict]) -> str:
    """Return the Markdown of vocabulary.md."""
    parts = [
        "# Task vocabulary\n\n",
        "The terms the task pages use to describe a task. A task's standard form is one\n"
        "**game type**; it states the **rules** of that game on which it departs from the\n"
        "default, why the player tries (**motivation**), and one or more values of each\n"
        "**facet** that applies. It may also name its **phases**, the **settings** a study\n"
        "chooses, and other games it is **combined** with. A variant states only what it\n"
        "changes. Each value below has its own anchor, which the task pages link to. The source\n"
        "files are `data/task_game_defs.json` and `data/task_facet_defs.json`.\n\n",
        "## Game types\n\n",
    ]
    rows = [
        [
            _target(vocab_anchor("game", g["game_type"]), g["game_type"]),
            cell(g["name"]),
            cell(g["what_the_player_does"]),
            cell(g.get("boundary")),
        ]
        for g in games["game_types"]
    ]
    parts.append(table(["Game type", "Name", "What the player does", "Boundary"], rows) + "\n\n")

    parts.append("## Rules\n\n")
    no_rules = [g["name"] for g in games["game_types"] if not g.get("rules")]
    parts.append(
        "Each game type has its own rules. A rule a task does not state takes its default; a\n"
        "task states a rule only to give another answer. "
        f"{count_phrase(len(no_rules), 'game type')} have no rules: {', '.join(no_rules)}.\n\n"
    )
    for g in games["game_types"]:
        if not g.get("rules"):
            continue
        parts.append(f"### {g['name']}\n\n")
        parts.append(f"Rules of the game type `{g['game_type']}`.\n\n")
        for r in g["rules"]:
            parts.append(
                f'<span id="{vocab_anchor("rule", g["game_type"], r["rule"])}"></span>'
                f"**{r['question']}** Rule `{r['rule']}`, default `{r['default']}`.\n\n"
            )
            rows = [
                [_target(vocab_anchor("rule", g["game_type"], r["rule"], v["value"]), v["value"]), cell(v["definition"])]
                for v in r["values"]
            ]
            parts.append(table(["Value", "Definition"], rows) + "\n\n")

    parts.append("## Motivation\n\n")
    parts.append("Why the player tries. Every task answers the first question; the others are answered where they apply.\n\n")
    for m in games["motivation"]:
        required = " Every task answers it." if m.get("required") else ""
        parts.append(
            f'<span id="{vocab_anchor("motivation", m["key"])}"></span>**{m["question"]}** Key `{m["key"]}`.{required}\n\n'
        )
        rows = [
            [_target(vocab_anchor("motivation", m["key"], v["value"]), v["value"]), cell(v["definition"])] for v in m["values"]
        ]
        parts.append(table(["Value", "Definition"], rows) + "\n\n")

    for heading, intro, items, key, column in (
        ("Phases", "Named parts of a task that a study reports separately.", games["phases"], "phase", "Phase"),
        ("Settings", "Quantities a study chooses when it runs the task.", games["settings"], "setting", "Setting"),
        ("Ways of combining", "How a second game is played alongside the task's own.", games["combinations"], "how", "Way"),
    ):
        parts.append(f"## {heading}\n\n{intro}\n\n")
        rows = [[_target(vocab_anchor(key, i[key]), i[key]), cell(i["definition"])] for i in items]
        parts.append(table([column, "Definition"], rows) + "\n\n")

    parts.append("## Facets\n\n")
    parts.append(
        "What the participant sees, uses and is, recorded as values that are present (there are\n"
        f"no 'none' values). There are {len(facets)} facets. The HED tags column gives the tags a\n"
        "value corresponds to.\n\n"
    )
    for f in facets:
        parts.append(f"### {facet_label(f['facet'])}\n\n")
        parts.append(f'<span id="{vocab_anchor("facet", f["facet"])}"></span>**{f["question"]}** Facet `{f["facet"]}`.\n\n')
        parts.append(f"{f['description']}\n\n")
        rows = []
        for v in f["values"]:
            tags = ", ".join(f"`{t}`" for t in v.get("hed_tags") or [])
            note = v.get("hed_note") or ""
            rows.append(
                [
                    _target(vocab_anchor("facet", f["facet"], v["value"]), v["value"]),
                    cell(v["definition"]),
                    cell(f"{tags} {note}".strip()),
                ]
            )
        parts.append(table(["Value", "Definition", "HED tags"], rows) + "\n\n")
    return "".join(parts).rstrip("\n") + "\n"


def _task_md(t: dict) -> str:
    return f"[{t['canonical_name']}]({t['hedtsk_id']}.md)"


def _by_game_type(games: dict, tasks: list[dict]) -> str:
    """Return the Markdown of by_game_type.md."""
    parts = [
        "# Tasks by game type\n\n",
        "Every task under the game its standard form is. The game types are defined on the\n"
        "[task vocabulary](vocabulary.md) page; a task's own rules are on its page, under\n"
        '"At a glance".\n\n',
    ]
    for g in games["game_types"]:
        members = [t for t in tasks if t["game_type"] == g["game_type"]]
        parts.append(f"## {g['name']}\n\n")
        link = vocab_link(g["game_type"], vocab_anchor("game", g["game_type"]))
        parts.append(f"{g['what_the_player_does']} Game type {link}; {count_phrase(len(members), 'task')}.\n\n")
        for t in members:
            parts.append(f"- {_task_md(t)}\n")
        parts.append("\n")
    return "".join(parts).rstrip("\n") + "\n"


def _by_facet(facets: list[dict], tasks: list[dict]) -> str:
    """Return the Markdown of by_facet.md."""
    parts = [
        "# Tasks by facet\n\n",
        "For each facet value, the tasks whose standard form carries it and, after them, the\n"
        "variants that state it (a variant inherits the standard form's values for every facet\n"
        "it does not state). The values are defined on the [task vocabulary](vocabulary.md)\n"
        "page.\n\n",
    ]
    for f in facets:
        fid = f["facet"]
        parts.append(f"## {facet_label(fid)}\n\n{f['question']}\n\n")
        for v in f["values"]:
            value = v["value"]
            std = [_task_md(t) for t in tasks if value in (t.get("task_facets") or {}).get(fid, [])]
            var = [
                f'<a href="{t["hedtsk_id"]}.html#variants">{html.escape(t["canonical_name"])}: {html.escape(x["name"])}</a>'
                for t in tasks
                for x in t.get("variants") or []
                if value in (x.get("task_facets") or {}).get(fid, [])
            ]
            line = f"- {vocab_link(value, vocab_anchor('facet', fid, value))}: "
            line += ", ".join(std) if std else "no task's standard form"
            if var:
                line += f"; variants: {', '.join(var)}"
            parts.append(line + "\n")
        parts.append("\n")
    return "".join(parts).rstrip("\n") + "\n"
