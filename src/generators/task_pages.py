"""Generate the task section of the site.

Files written:

- docs/tasks/index.md            the task landing page: what a task page holds, the
                                 families at a glance, and the two ways in
- docs/tasks/tasks_by_family.md        the catalog grouped by task family, one section
                                 per family; its toctree nests the family pages
- docs/tasks/families/<id>.md    one page per family, whose toctree nests its tasks
- docs/tasks/tasks_alphabetically.md   every task in name order; its toctree lists every
                                 task
- docs/tasks/hedtsk_*.md         one page per task: a "Game model" block for the
                                 standard form, the inclusion test, and the variants

The vocabulary page and the by-game-type and by-facet listings under docs/tasks/ are
written by vocabulary_pages.py; the task index's toctree lists them.

The document tree is Tasks > Tasks by family > family > task, and Tasks >
Tasks alphabetically > task. Each task page sits in two toctrees, which Sphinx allows
(it picks the first as the parent for prev/next links). The left sidebar shows only the
first two levels; a rule in docs/source/_static/custom.css hides the family and task
entries, and the right-hand contents menu of the two listing pages takes over from
there. Listing headings and sidebar labels drop a trailing "Task", "tasks" or "tests"
from a name; page titles keep it. See `_short_name`.

Families are defined in data/task_family_defs.tsv and each task lists its memberships; see
data/README.md. The assignment is validated in generate_docs.py before anything is
written, so this module can assume every task has exactly one known family.
"""

from __future__ import annotations

import html
import sys
from pathlib import Path
from urllib.parse import quote

from generators.utils import (
    REVIEW_NOTE,
    cell,
    citation_line,
    count_phrase,
    facet_label,
    pop_card,
    primary_category,
    primary_family,
    primary_membership,
    process_anchor,
    process_link,
    secondary_memberships,
    split_references,
    table,
    vocab_anchor,
    vocab_label,
    vocab_link,
    write_page,
)

ATLAS_TASK_URL = "https://www.cognitiveatlas.org/task/id/"
# A CogPO class is readable online only on the CogPO wiki, whose TLS certificate is
# invalid, so the link is plain http.
COGPO_WIKI_URL = "http://www.wiki.cogpo.org/index.php?title="


def generate(
    docs_dir: Path,
    tasks: list[dict],
    processes_by_id: dict[str, dict],
    families: list[dict],
    atlas_map: dict[str, dict] | None = None,
    cogpo_map: dict[str, dict] | None = None,
    atlas_variant_map: dict[str, list[dict]] | None = None,
    game_defs: dict | None = None,
) -> int:
    """Write the task index, the family pages, the alphabetical list and the task pages.

    Parameters:
        docs_dir: The docs/source/ root.
        tasks: Task records from data/task_details.json, each with its `families`.
        processes_by_id: Process records keyed by process_id.
        families: Rows of data/task_family_defs.tsv, already sorted by `order`.
        atlas_map: Rows of data/mappings/hed_task_to_atlas.tsv keyed by hedtsk_id.
        cogpo_map: Rows of data/mappings/hed_task_to_cogpo.tsv keyed by hedtsk_id, each
            with a `cogpo_wiki_title` added for the link target.
        atlas_variant_map: Rows of data/mappings/atlas_task_to_hed.tsv matched exact or
            close at the variant level, keyed by hed_variant_id.
        game_defs: data/task_game_defs.json, for the questions the "Game model" block
            and the Variants table ask.

    Returns the number of files written.
    """
    tasks_dir = docs_dir / "tasks"
    sorted_tasks = sorted(tasks, key=lambda t: t["canonical_name"])
    family_of = {t["hedtsk_id"]: primary_family(t) for t in tasks}
    family_by_id = {f["family_id"]: f for f in families}
    tasks_by_family: dict[str, list[dict]] = {f["family_id"]: [] for f in families}
    # Secondary memberships, keyed by the family they cross-list into.
    also_by_family: dict[str, list[tuple[dict, dict]]] = {f["family_id"]: [] for f in families}
    for task in sorted_tasks:
        tasks_by_family[family_of[task["hedtsk_id"]]].append(task)
        for member in secondary_memberships(task, "families"):
            also_by_family[member["family_id"]].append((task, member))
    n_review = sum(1 for t in tasks for m in t["families"] if m.get("confidence") == "review")
    task_names = {t["hedtsk_id"]: t["canonical_name"] for t in tasks}

    count = 0
    count += _write_task_index(tasks_dir, families, tasks_by_family, also_by_family, n_review)
    count += _write_by_family(tasks_dir, families, tasks_by_family, also_by_family, processes_by_id, family_by_id)
    for fam in families:
        fid = fam["family_id"]
        count += _write_family_page(tasks_dir, fam, tasks_by_family[fid], also_by_family[fid], family_by_id, processes_by_id)
    count += _write_alphabetical(tasks_dir, sorted_tasks, family_by_id, processes_by_id)
    for task in sorted_tasks:
        fam = family_by_id[family_of[task["hedtsk_id"]]]
        count += _write_task_page(
            tasks_dir,
            task,
            fam,
            family_by_id,
            processes_by_id,
            atlas_map or {},
            cogpo_map or {},
            atlas_variant_map or {},
            game_defs or {},
            task_names,
        )
    return count


# ---------------------------------------------------------------------------
# Index and family pages
# ---------------------------------------------------------------------------


def _short_name(name: str) -> str:
    """Return the short display form of a task or family name.

    The short form drops a trailing " Task" (canonical task names), " tasks" or
    " tests" (family names). It is used for sidebar labels and for the headings of the
    task listings, where the page already says these are tasks. A
    name that ends some other way is left alone. Page titles,
    aliases and prose always use the full canonical name.

    Parameters:
        name: The canonical task name or the family name.
    """
    for suffix in (" Task", " tasks", " tests"):
        if name.endswith(suffix):
            return name[: -len(suffix)]
    return name


def _toctree(entries: list[tuple[str, str]], maxdepth: int) -> str:
    """Return a hidden toctree whose entries carry explicit sidebar titles.

    Parameters:
        entries: (sidebar title, document path) pairs.
        maxdepth: The toctree's maxdepth option.
    """
    lines = ["```{toctree}", ":hidden:", f":maxdepth: {maxdepth}", ""]
    lines += [f"{title} <{doc}>" for title, doc in entries]
    lines.append("```")
    return "\n".join(lines) + "\n"


def _entry_details(
    task: dict,
    link_prefix: str,
    processes_by_id: dict[str, dict],
    family_by_id: dict[str, dict],
    with_family: bool,
) -> str:
    """Return the one-sentence detail line of a listing entry, with pop-up counts.

    "Engages N processes. N aliases, N variants, also filed under N other families."
    Each count opens a card listing the items: processes and families as links, aliases
    as text, variants as links to the task page's Variants section.

    Parameters:
        task: The task record.
        link_prefix: Path prefix from the page being written to the task pages.
        processes_by_id: Process records keyed by process_id, for names and anchors.
        family_by_id: Family definitions keyed by id.
        with_family: Whether to open with "Filed under <family>" (the alphabetical page).
    """
    tid = task["hedtsk_id"]
    proc_ids = task.get("hed_process_ids", [])
    proc_items = []
    for pid in proc_ids:
        proc = processes_by_id.get(pid)
        if proc is None:
            proc_items.append(html.escape(pid))
        else:
            href = f"{link_prefix}../processes/{primary_category(proc)}.html#{process_anchor(pid)}"
            proc_items.append(f'<a href="{href}">{html.escape(proc["process_name"])}</a>')
    engages = pop_card(count_phrase(len(proc_ids), "process", "processes"), proc_items)

    aliases = task.get("aliases", [])
    alias_part = (
        pop_card(count_phrase(len(aliases), "alias", "aliases"), [html.escape(a) for a in aliases])
        if aliases
        else "no aliases"
    )
    variants = task.get("variants", [])
    var_items = [f'<a href="{link_prefix}{tid}.html#variants">{html.escape(v["name"])}</a>' for v in variants]
    var_part = pop_card(count_phrase(len(variants), "variant"), var_items) if variants else "no variants"
    also_items = [
        f'<a href="{link_prefix}families/{m["family_id"]}.html">{html.escape(family_by_id[m["family_id"]]["name"])}</a>'
        for m in secondary_memberships(task, "families")
    ]

    lead = ""
    if with_family:
        fam = family_by_id[primary_family(task)]
        lead = f"Filed under [{fam['name']}]({link_prefix}families/{fam['family_id']}.md). "
    sentence = f"{lead}Engages {engages}. {alias_part[0].upper()}{alias_part[1:]}, {var_part}"
    if also_items:
        sentence += (
            f", also filed under {pop_card(count_phrase(len(also_items), 'other family', 'other families'), also_items)}"
        )
    return sentence + "."


def _task_sections(
    fam_tasks: list[dict],
    link_prefix: str,
    level: int,
    processes_by_id: dict[str, dict],
    family_by_id: dict[str, dict],
) -> str:
    """Return one short section per task: a linked heading, the full short definition,
    and a detail line whose counts pop up the items (see `_entry_details`).

    The family listings used to be tables, which truncated the short definitions. A
    section per task shows the whole definition and puts every task in the page's
    right-hand contents menu.

    Parameters:
        fam_tasks: The tasks to list, in display order.
        link_prefix: Path prefix from the page being written to the task pages.
        level: Markdown heading level for each task.
        processes_by_id: Process records keyed by process_id.
        family_by_id: Family definitions keyed by id.
    """
    parts: list[str] = []
    for task in fam_tasks:
        name = _short_name(task["canonical_name"])
        parts.append(f"{'#' * level} [{name}]({link_prefix}{task['hedtsk_id']}.md)\n\n")
        details = _entry_details(task, link_prefix, processes_by_id, family_by_id, with_family=False)
        parts.append(f"{task.get('short_definition', '').strip()} {details}\n\n")
    return "".join(parts)


def _write_task_index(
    tasks_dir: Path,
    families: list[dict],
    tasks_by_family: dict[str, list[dict]],
    also_by_family: dict[str, list[tuple[dict, dict]]],
    n_review: int,
) -> int:
    """Write docs/tasks/index.md."""
    all_tasks = [t for v in tasks_by_family.values() for t in v]
    n_tasks = len(all_tasks)
    n_also = len({t["hedtsk_id"] for pairs in also_by_family.values() for t, _ in pairs})

    parts: list[str] = [
        "# Tasks\n\n",
        f"The task catalog holds {n_tasks} traditional cognitive and behavioral neuroscience tasks, the\n"
        "starting point of the HED task models. They were drawn from the Cognitive Atlas, with gaps\n"
        "filled from the literature, and each is modeled as a game. Each task page gives the canonical\n"
        "name and aliases, a description, the game model of the standard form of the task (its game\n"
        "type, rules, motivators, phases and facets, in the terms of the\n"
        "[game vocabulary](vocabulary.md)), the inclusion test that decides whether an experiment is\n"
        "an instance of the task, its variants, the cognitive processes it engages, and references.\n"
        "[The task model](../task_model.md) explains the parts.\n\n",
        f"Tasks are filed under {len(families)} **task families** by what the participant does,\n"
        "not by which process the task is thought to measure. The list of cognitive processes covers that\n"
        "other axis, and the two cross-link. Families are organizational, not a hierarchy. Every\n"
        "task has one **primary** family, where its page is filed, and may be cross-listed under\n"
        f"others as a **secondary** member; {n_also} tasks are cross-listed at present. The\n"
        "assignments are curation decisions and are expected to change as the task catalog grows;\n"
        f"{n_review} memberships are marked `review`. The\n"
        "[task family assignment rules](../methods/task_criteria/06_task_family_assignment.md)\n"
        "say how families are assigned.\n\n",
        REVIEW_NOTE.format(unit="family") + "\n",
        "Ways in:\n\n",
        "- [Tasks by family](tasks_by_family.md) lists every task under its family, with the\n  family's scope statement.\n",
        "- [Tasks alphabetically](tasks_alphabetically.md) lists every task in name order, for when you\n"
        "  know the name and not the family.\n",
        "- [Tasks by game type](by_game_type.md) lists the tasks under the game their standard form is.\n",
        "- [Tasks by facet](by_facet.md) lists, for each facet value, the tasks and variants that carry it.\n",
        "- The [game vocabulary](vocabulary.md) defines every game type, rule, motivator, phase and facet\n"
        "  value used on the task pages, with the settings and the ways of combining games.\n\n",
        "## Families at a glance\n\n",
    ]

    rows = [
        [
            f"[{fam['name']}](families/{fam['family_id']}.md)",
            str(len(tasks_by_family[fam["family_id"]])),
            str(len(also_by_family[fam["family_id"]])) if also_by_family[fam["family_id"]] else "-",
        ]
        for fam in families
    ]
    parts.append(table(["Family", "Tasks filed", "Cross-listed"], rows))
    parts.append("\n\n")
    parts.append(
        _toctree(
            [
                ("Tasks by family", "tasks_by_family"),
                ("Tasks alphabetically", "tasks_alphabetically"),
                ("Tasks by game type", "by_game_type"),
                ("Tasks by facet", "by_facet"),
                ("Game vocabulary", "vocabulary"),
            ],
            3,
        )
    )

    write_page(tasks_dir / "index.md", "".join(parts))
    return 1


def _write_by_family(
    tasks_dir: Path,
    families: list[dict],
    tasks_by_family: dict[str, list[dict]],
    also_by_family: dict[str, list[tuple[dict, dict]]],
    processes_by_id: dict[str, dict],
    family_by_id: dict[str, dict],
) -> int:
    """Write docs/tasks/tasks_by_family.md: one section per family, nesting the family pages.

    A family's section lists the tasks filed under it in full, then the tasks cross-listed
    into it as a short "Also filed here" list, each naming its own family and the reason.
    """
    parts: list[str] = [
        "# Tasks by family\n\n",
        f"The {len(families)} task families, each with its scope statement and the tasks filed\n"
        "under it. Every task is in exactly one family. The family pages repeat these entries\n"
        "and add the assignments marked for review. The [alphabetical list](tasks_alphabetically.md)\n"
        "has the same tasks in name order.\n\n",
        # The right-hand contents menu is this page's navigation: the families are always
        # listed, and a family's tasks unfold while that family is the current section.
        # Furo's scroll-spy marks the current heading's entry and its ancestors with
        # scroll-current, so a click on a family opens it. Page-specific, hence inline.
        "<style>\n"
        ".toc-tree li li > ul { display: none; }\n"
        ".toc-tree li li.scroll-current > ul { display: block; }\n"
        "</style>\n\n",
    ]
    for fam in families:
        fam_tasks = tasks_by_family[fam["family_id"]]
        parts.append(f"## [{fam['name']}](families/{fam['family_id']}.md)\n\n")
        parts.append(f"{fam['scope']}\n\n")
        parts.append(_task_sections(fam_tasks, "", 3, processes_by_id, family_by_id))
        also = also_by_family[fam["family_id"]]
        if also:
            parts.append("### Also filed here\n\n")
            for t, m in also:
                home = family_by_id[primary_family(t)]
                parts.append(
                    f"- [{_short_name(t['canonical_name'])}]({t['hedtsk_id']}.md), filed under "
                    f"[{home['name']}](families/{home['family_id']}.md): {m.get('rationale', '')}\n"
                )
            parts.append("\n")

    parts.append(_toctree([(_short_name(fam["name"]), f"families/{fam['family_id']}") for fam in families], 2))
    write_page(tasks_dir / "tasks_by_family.md", "".join(parts))
    return 1


def _write_family_page(
    tasks_dir: Path,
    fam: dict,
    fam_tasks: list[dict],
    also: list[tuple[dict, dict]],
    family_by_id: dict[str, dict],
    processes_by_id: dict[str, dict],
) -> int:
    """Write docs/tasks/families/<family_id>.md.

    Parameters:
        fam: The family definition.
        fam_tasks: Tasks filed under it (primary membership), in name order.
        also: (task, membership) pairs cross-listed here (secondary membership).
        family_by_id: Family definitions keyed by id, for naming a task's own family.
    """
    fid = fam["family_id"]

    def link(t: dict) -> str:
        return f"[{_short_name(t['canonical_name'])}](../{t['hedtsk_id']}.md)"

    review_rows: list[list[str]] = []
    for t in fam_tasks:
        m = primary_membership(t, "families")
        if m.get("confidence") == "review":
            review_rows.append([link(t), "filed here", cell(m.get("rationale", ""))])
    for t, m in also:
        if m.get("confidence") == "review":
            review_rows.append([link(t), "cross-listed", cell(m.get("rationale", ""))])

    summary = f"This family contains {len(fam_tasks)} tasks"
    summary += f" and cross-lists {len(also)} more.\n\n" if also else ".\n\n"
    parts: list[str] = [
        f"({fid})=\n",
        f"# {fam['name']}\n\n",
        f"{fam['scope']}\n\n",
        summary,
        _task_sections(fam_tasks, "../", 2, processes_by_id, family_by_id),
    ]

    if also:
        parts.append("## Also filed here\n\n")
        parts.append("These tasks are filed under another family and cross-listed here; the note says why.\n\n")
        rows = [
            [link(t), f"[{family_by_id[primary_family(t)]['name']}]({primary_family(t)}.md)", cell(m.get("rationale", ""))]
            for t, m in also
        ]
        parts.append(table(["Task", "Filed under", "Note"], rows))
        parts.append("\n\n")

    if review_rows:
        parts.append("## Marked for review\n\n")
        parts.append(REVIEW_NOTE.format(unit="family") + "\n")
        parts.append(table(["Task", "Membership", "Note"], review_rows))
        parts.append("\n\n")

    parts.append(_toctree([(_short_name(t["canonical_name"]), f"../{t['hedtsk_id']}") for t in fam_tasks], 1))

    write_page(tasks_dir / "families" / f"{fid}.md", "".join(parts))
    return 1


def _write_alphabetical(
    tasks_dir: Path,
    sorted_tasks: list[dict],
    family_by_id: dict[str, dict],
    processes_by_id: dict[str, dict],
) -> int:
    """Write docs/tasks/tasks_alphabetically.md: one short section per task, in name order.

    Like the family listings, each task is a linked heading followed by its full short
    definition, so the right-hand contents menu lists every task under the page title.
    Here the detail line also names the family the task is filed under.
    """
    parts: list[str] = [
        "# Tasks alphabetically\n\n",
        f"All {len(sorted_tasks)} tasks in name order, each with the task family it is filed\n"
        "under. [Tasks by family](tasks_by_family.md) presents the same tasks grouped by\n"
        "family.\n\n",
    ]
    for task in sorted_tasks:
        parts.append(f"## [{_short_name(task['canonical_name'])}]({task['hedtsk_id']}.md)\n\n")
        details = _entry_details(task, "", processes_by_id, family_by_id, with_family=True)
        parts.append(f"{task.get('short_definition', '').strip()} {details}\n\n")
    parts.append(_toctree([(_short_name(t["canonical_name"]), t["hedtsk_id"]) for t in sorted_tasks], 1))
    write_page(tasks_dir / "tasks_alphabetically.md", "".join(parts))
    return 1


# ---------------------------------------------------------------------------
# Task pages
# ---------------------------------------------------------------------------


def _references(parts: list[str], heading: str, refs: list[dict]) -> None:
    citations = [citation_line(r) for r in refs if r.get("citation_string")]
    if not citations:
        return
    parts.append(f"## {heading}\n\n")
    for citation in citations:
        parts.append(f"- {citation}\n")
    parts.append("\n")


def _items_cell(items: list[str] | None, ordered: bool = False) -> str:
    """Render an inclusion-test list inside a list-table cell.

    One item is a line of text; several are a nested numbered list (procedure steps are
    ordered) or bulleted list, indented so that MyST keeps them inside the cell.
    """
    items = [i for i in (items or []) if i]
    if not items:
        return ""
    if len(items) == 1:
        return items[0]
    lines = [f"{n}. {item}" if ordered else f"- {item}" for n, item in enumerate(items, 1)]
    return "\n    ".join(lines)


class _Questions:
    """The questions of data/task_game_defs.json, looked up by key.

    Parameters:
        game_defs: The loaded data/task_game_defs.json.
    """

    def __init__(self, game_defs: dict) -> None:
        self.rules = {
            (g["game_type"], r["rule"]): r["question"] for g in game_defs.get("game_types", []) for r in g.get("rules", [])
        }
        self.motivators = {m["key"]: m["question"] for m in game_defs.get("motivators", [])}
        self.game_names = {g["game_type"]: g["name"] for g in game_defs.get("game_types", [])}
        self.games_with_rules = {g["game_type"] for g in game_defs.get("game_types", []) if g.get("rules")}


def _values(values, anchor_of) -> str:
    """Return vocabulary values as comma-separated links to the vocabulary page.

    Parameters:
        values: One value or a list of values.
        anchor_of: A function from a value to its anchor (see `vocab_anchor`).
    """
    values = values if isinstance(values, list) else [values]
    return ", ".join(vocab_link(v, anchor_of(v)) for v in values)


def _combined_line(c: dict, task_names: dict[str, str]) -> str:
    """Return one combined game as "<how>, <game type or linked task>", then its note.

    Parameters:
        c: One entry of `combined_with`.
        task_names: Task id -> canonical name, for an entry that names a task.
    """
    how = vocab_link(c["how"], vocab_anchor("how", c["how"]))
    if "task" in c:
        other = f"[{task_names.get(c['task'], c['task'])}]({c['task']}.md)"
    else:
        other = vocab_link(c.get("game_type", ""), vocab_anchor("game", c.get("game_type", "")))
    note = f" ({c['note'].rstrip('.')})" if c.get("note") else ""
    return f"{how}, {other}{note}"


def _game_model(task: dict, questions: _Questions, task_names: dict[str, str]) -> str:
    """Return the "Game model" block: the standard form in the terms of the vocabulary.

    The five parts of the model come first and are always shown, in a fixed order: game
    type, game rules (the ones the record states, question and answer), game motivators,
    game phases, game facets (one line per facet). Settings, material and combined games
    follow, each only when the record has it. `candidates` are a working register and
    are never shown.

    Parameters:
        task: The task record.
        questions: The rule and motivator questions, and the game type names.
        task_names: Task id -> canonical name, for combined games that name a task.
    """
    gt = task["game_type"]
    name = questions.game_names.get(gt, vocab_label(gt))
    lines = [f'- **Game type:** <a href="vocabulary.html#{vocab_anchor("game", gt)}">{name}</a> (`{gt}`)']
    rules = task.get("rules") or {}
    if rules:
        lines.append("- **Game rules:** the answers that differ from the defaults of the game type")
        for rule, value in rules.items():
            question = questions.rules.get((gt, rule), vocab_label(rule))
            lines.append(f"  - *{question}* {_values(value, lambda v, r=rule: vocab_anchor('rule', gt, r, v))}")
    elif gt in questions.games_with_rules:
        lines.append("- **Game rules:** every rule takes the default of the game type")
    else:
        lines.append("- **Game rules:** none are defined for this game type")
    lines.append("- **Game motivators:**")
    for key, answer in (task.get("motivators") or {}).items():
        question = questions.motivators.get(key, vocab_label(key))
        lines.append(f"  - *{question}* {_values(answer, lambda v, k=key: vocab_anchor('motivator', k, v))}")
    if task.get("phases"):
        lines.append(f"- **Game phases:** {_values(task['phases'], lambda v: vocab_anchor('phase', v))}")
    else:
        lines.append("- **Game phases:** none beyond the game's own structure")
    lines.append("- **Game facets:**")
    for facet, values in (task.get("task_facets") or {}).items():
        lines.append(f"  - {facet_label(facet)}: {_values(values, lambda v, f=facet: vocab_anchor('facet', f, v))}")
    if task.get("settings"):
        lines.append(f"- **Settings:** {_values(task['settings'], lambda v: vocab_anchor('setting', v))}")
    if task.get("material"):
        lines.append(f"- **Material:** {task['material']}")
    for c in task.get("combined_with") or []:
        lines.append(f"- **Combined with:** {_combined_line(c, task_names)}")
    return (
        "## Game model\n\n"
        "The standard form of the task, the one the inclusion test defines, as a game, in the terms\n"
        "of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the\n"
        "parts. A variant states only what it changes.\n\n" + "\n".join(lines) + "\n\n"
    )


def _what_differs(variant: dict, game_type: str, task_names: dict[str, str]) -> str:
    """Return the "What differs" cell of a variant: one short phrase per key it states.

    Built from the variant's own `task_facets`, `rules`, `motivators`, `phases` and
    `combined_with`; an empty facet list reads "<facet>: none" (the facet does not apply
    to this form). A variant that states none of them is a named form.

    Parameters:
        variant: The variant record.
        game_type: The task's game type, for the rule anchors.
        task_names: Task id -> canonical name, for combined games that name a task.
    """
    phrases = []
    for facet, values in (variant.get("task_facets") or {}).items():
        label = facet_label(facet).lower().replace("i/o", "I/O")
        shown = _values(values, lambda v, f=facet: vocab_anchor("facet", f, v)) if values else "none"
        phrases.append(f"{label}: {shown}")
    for rule, value in (variant.get("rules") or {}).items():
        phrases.append(f"{vocab_label(rule)}: {_values(value, lambda v, r=rule: vocab_anchor('rule', game_type, r, v))}")
    for key, answer in (variant.get("motivators") or {}).items():
        phrases.append(f"{vocab_label(key)}: {_values(answer, lambda v, k=key: vocab_anchor('motivator', k, v))}")
    if variant.get("phases"):
        phrases.append(f"phases: {_values(variant['phases'], lambda v: vocab_anchor('phase', v))}")
    for c in variant.get("combined_with") or []:
        phrases.append(f"combined with: {_combined_line(c, task_names)}")
    return "; ".join(phrases) if phrases else "named form"


def _write_task_page(
    tasks_dir: Path,
    task: dict,
    fam: dict,
    family_by_id: dict[str, dict],
    processes_by_id: dict[str, dict],
    atlas_map: dict[str, dict],
    cogpo_map: dict[str, dict] | None = None,
    atlas_variant_map: dict[str, list[dict]] | None = None,
    game_defs: dict | None = None,
    task_names: dict[str, str] | None = None,
) -> int:
    """Write an individual task page docs/tasks/{hedtsk_id}.md."""
    hedtsk_id = task["hedtsk_id"]
    canonical_name = task["canonical_name"]
    aliases = task.get("aliases", [])
    inclusion = task.get("inclusion_test", {})
    variants = task.get("variants", [])
    hed_process_ids = task.get("hed_process_ids", [])
    questions = _Questions(game_defs or {})

    # The curated mapping in data/mappings/ is the only Atlas cross-reference. Task
    # records no longer carry an atlas_id of their own; that field produced dead links
    # and links to the wrong paradigm, and was removed.
    atlas_row = atlas_map.get(hedtsk_id) or {}
    atlas_id = atlas_row.get("atlas_id") or ""
    atlas_name = atlas_row.get("atlas_name") or ""
    atlas_match = atlas_row.get("match_type") or ""

    parts: list[str] = []
    parts.append(f"({hedtsk_id})=\n")
    parts.append(f"# {canonical_name}\n\n")
    parts.append(f"**HED task ID:** `{hedtsk_id}`\n\n")
    family_line = f"**Family:** [{fam['name']}](families/{fam['family_id']}.md)"
    also = [family_by_id[m["family_id"]] for m in secondary_memberships(task, "families")]
    if also:
        family_line += " (also " + ", ".join(f"[{f['name']}](families/{f['family_id']}.md)" for f in also) + ")"
    parts.append(family_line + "\n\n")
    if aliases:
        parts.append(f"**Also known as:** {', '.join(aliases)}\n\n")
    parts.append(f"{task.get('short_definition', '')}\n\n")

    parts.append("## Description\n\n")
    parts.append(f"{task.get('description', '')}\n\n")

    parts.append(_game_model(task, questions, task_names or {}))

    parts.append("## Inclusion test\n\n")
    parts.append(
        "An experiment is an instance of this task when its procedure matches, it manipulates at\n"
        "least one of the listed variables, and it records at least one of the listed measures.\n\n"
    )
    parts.append("```{list-table}\n:widths: 15 85\n:header-rows: 0\n\n")
    parts.append(f"* - **Procedure**\n  - {_items_cell(inclusion.get('procedure'), ordered=True)}\n")
    parts.append(f"* - **Manipulations**\n  - {_items_cell(inclusion.get('manipulations'))}\n")
    parts.append(f"* - **Measurements**\n  - {_items_cell(inclusion.get('measurements'))}\n")
    parts.append("```\n\n")

    if variants:
        parts.append("## Variants\n\n")
        parts.append(
            "Attested forms of the task. Each states only what differs from the standard form\n"
            "above and inherits the rest; a named form differs in name only. The identifier of a\n"
            "variant is `hedvar_<task>__<variant>`.\n\n"
        )
        parts.append("```{list-table}\n:widths: 22 33 15 30\n:header-rows: 1\n\n")
        parts.append("* - Variant\n  - What differs\n  - Processes added\n  - Note\n")
        for var in variants:
            var_id = var["variant_id"]
            # The id and any Atlas entries are further paragraphs in the name's cell.
            parts.append(f"* - {var['name']}\n\n    `{var_id}`\n")
            atlas_links = [
                f"[{r['atlas_name']}]({ATLAS_TASK_URL}{r['atlas_id']})"
                + (f" ({r['match_type']} match)" if r["match_type"] != "exact" else "")
                for r in (atlas_variant_map or {}).get(var_id, [])
            ]
            if atlas_links:
                parts.append(f"\n    Cognitive Atlas: {', '.join(atlas_links)}\n")
            parts.append(f"  - {_what_differs(var, task['game_type'], task_names or {})}\n")
            added = []
            for pid in var.get("hed_process_ids") or []:
                proc = processes_by_id.get(pid)
                added.append(process_link(pid, proc["process_name"], primary_category(proc), "tasks") if proc else f"`{pid}`")
            parts.append(f"  - {', '.join(added) if added else '-'}\n")
            parts.append(f"  - {var.get('note', '')}\n")
        parts.append("```\n\n")

    if hed_process_ids:
        parts.append("## Cognitive processes\n\n")
        parts.append("This task is designed to engage the following processes:\n\n")
        for pid in hed_process_ids:
            proc = processes_by_id.get(pid)
            if proc is None:
                print(
                    f"WARNING: process '{pid}' referenced by task '{hedtsk_id}' not found in process_details.json",
                    file=sys.stderr,
                )
                parts.append(f"- `{pid}`\n")
            else:
                parts.append(f"- {process_link(pid, proc['process_name'], primary_category(proc), 'tasks')}\n")
        parts.append("\n")

    key_refs, further_refs = split_references(task)
    _references(parts, "Key references", key_refs)
    _references(parts, "Further references", further_refs)

    # The CogPO row is used only when it names a class: a `related` row points at a
    # broad class the task merely falls under, which is a comparison-page fact, not a
    # link a reader of the task page needs.
    cogpo_row = (cogpo_map or {}).get(hedtsk_id) or {}
    cogpo_id = cogpo_row.get("cogpo_id") or ""
    cogpo_match = cogpo_row.get("match_type") or ""
    cogpo_line = ""
    if cogpo_id and cogpo_match in ("exact", "close"):
        label = cogpo_row.get("cogpo_label") or "CogPO paradigm class"
        title = cogpo_row.get("cogpo_wiki_title") or ""
        target = f"[{label}]({COGPO_WIKI_URL}{quote(title, safe='')})" if title else label
        qualifier = f" ({cogpo_match} match)" if cogpo_match != "exact" else ""
        cogpo_line = f"- CogPO: {target}{qualifier}\n\n"

    if atlas_id or cogpo_line:
        parts.append("## External links\n\n")
    if atlas_id:
        label = atlas_name or "Cognitive Atlas entry"
        qualifier = f" ({atlas_match} match)" if atlas_match and atlas_match != "exact" else ""
        parts.append(f"- Cognitive Atlas: [{label}]({ATLAS_TASK_URL}{atlas_id}){qualifier}\n\n")
    parts.append(cogpo_line)

    write_page(tasks_dir / f"{hedtsk_id}.md", "".join(parts))
    return 1
