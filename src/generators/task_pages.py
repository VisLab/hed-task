"""Generate the task section of the site.

Files written:

- docs/tasks/index.md            the task landing page: what a task page holds, the
                                 families at a glance, and the two ways in
- docs/tasks/tasks_by_paradigm_family.md        the catalog grouped by paradigm family, one section
                                 per family; its toctree nests the family pages
- docs/tasks/families/<id>.md    one page per family, whose toctree nests its tasks
- docs/tasks/tasks_alphabetically.md   every task in name order; its toctree lists every
                                 task
- docs/tasks/hedtsk_*.md         one page per task

The document tree is Tasks > Tasks by paradigm family > family > task, and Tasks >
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

from generators.utils import (
    REVIEW_NOTE,
    cell,
    citation_line,
    primary_category,
    primary_family,
    primary_membership,
    process_anchor,
    process_link,
    secondary_memberships,
    split_references,
    table,
    write_page,
)

ATLAS_TASK_URL = "https://www.cognitiveatlas.org/task/id/"


def generate(
    docs_dir: Path,
    tasks: list[dict],
    processes_by_id: dict[str, dict],
    families: list[dict],
    atlas_map: dict[str, dict] | None = None,
) -> int:
    """Write the task index, the family pages, the alphabetical list and the task pages.

    Parameters:
        docs_dir: The docs/source/ root.
        tasks: Task records from data/task_details.json, each with its `families`.
        processes_by_id: Process records keyed by process_id.
        families: Rows of data/task_family_defs.tsv, already sorted by `order`.
        atlas_map: Rows of data/mappings/hed_task_to_atlas.tsv keyed by hedtsk_id.

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

    count = 0
    count += _write_task_index(tasks_dir, families, tasks_by_family, also_by_family, n_review)
    count += _write_by_family(tasks_dir, families, tasks_by_family, also_by_family, processes_by_id, family_by_id)
    for fam in families:
        fid = fam["family_id"]
        count += _write_family_page(tasks_dir, fam, tasks_by_family[fid], also_by_family[fid], family_by_id, processes_by_id)
    count += _write_alphabetical(tasks_dir, sorted_tasks, family_by_id, processes_by_id)
    for task in sorted_tasks:
        fam = family_by_id[family_of[task["hedtsk_id"]]]
        count += _write_task_page(tasks_dir, task, fam, family_by_id, processes_by_id, atlas_map or {})
    return count


# ---------------------------------------------------------------------------
# Index and family pages
# ---------------------------------------------------------------------------


def _short_name(name: str) -> str:
    """Return the short display form of a task or family name.

    The short form drops a trailing " Task" (canonical task names), " tasks" or
    " tests" (family names). It is used for sidebar labels and for the headings of the
    task listings, where the page already says these are tasks. A
    name that ends some other way ("Pseudo tasks: ...") is left alone. Page titles,
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


def _pop(label: str, items: list[str]) -> str:
    """Return `label` as a pop-up trigger whose card lists `items` (HTML strings).

    The card is plain inline HTML that MyST passes through; the stylesheet (custom.css,
    `.pop`) shows it on hover, tap or keyboard focus. Links inside it are written as
    `.html` hrefs relative to the page, because Markdown is not parsed inside raw HTML.
    With no items the label is returned as plain text.
    """
    if not items:
        return label
    card = "".join(f"<span>{item}</span>" for item in items)
    return f'<span class="pop" tabindex="0">{label}<span class="pop-card">{card}</span></span>'


def _count(n: int, singular: str, plural: str | None = None) -> str:
    return f"{n} {singular if n == 1 else (plural or singular + 's')}"


def _entry_details(
    task: dict,
    link_prefix: str,
    processes_by_id: dict[str, dict],
    family_by_id: dict[str, dict],
    with_family: bool,
) -> str:
    """Return the one-sentence detail line of a listing entry, with pop-up counts.

    "Engages N processes. N aliases, N variations, also filed under N other families."
    Each count opens a card listing the items: processes and families as links, aliases
    as text, variations as links to the task page's Variations section.

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
    engages = (
        "no process links (pseudo task)" if not proc_ids else _pop(_count(len(proc_ids), "process", "processes"), proc_items)
    )

    aliases = task.get("aliases", [])
    alias_part = _pop(_count(len(aliases), "alias", "aliases"), [html.escape(a) for a in aliases]) if aliases else "no aliases"
    variations = task.get("variations", [])
    var_items = [f'<a href="{link_prefix}{tid}.html#variations">{html.escape(v["name"])}</a>' for v in variations]
    var_part = _pop(_count(len(variations), "variation"), var_items) if variations else "no variations"
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
        sentence += f", also filed under {_pop(_count(len(also_items), 'other family', 'other families'), also_items)}"
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
    n_pseudo = sum(1 for t in all_tasks if t.get("task_kind") == "pseudo_task")
    n_tasks = len(all_tasks) - n_pseudo
    n_also = len({t["hedtsk_id"] for pairs in also_by_family.values() for t, _ in pairs})

    parts: list[str] = [
        "# Tasks\n\n",
        f"The Catalog defines {n_tasks} standard cognitive and behavioral neuroscience tasks, and\n"
        f"{n_pseudo} pseudo tasks (rest, fixation and questionnaire blocks) that set up or hold a state\n"
        "rather than eliciting a process.\n"
        "Each task page gives the canonical name and aliases, a description, the inclusion\n"
        "test that decides whether an experiment is an instance of the task, its named\n"
        "variations, the cognitive processes it engages, and references.\n\n",
        f"Tasks are filed under {len(families)} **paradigm families** by what the participant does,\n"
        "not by which process the task is thought to measure. The Catalog's process list covers that\n"
        "other axis, and the two cross-link. Families are organizational, not a hierarchy. Every\n"
        "task has one **primary** family, where its page is filed, and may be cross-listed under\n"
        f"others as a **secondary** member; {n_also} tasks are cross-listed at present. The\n"
        "assignments are curation decisions and are expected to change as the Catalog grows;\n"
        f"{n_review} memberships are marked `review`. The\n"
        "[task family assignment rules](../methods/task_criteria/06_task_family_assignment.md)\n"
        "say how families are assigned.\n\n",
        REVIEW_NOTE.format(unit="family") + "\n",
        "Two ways in:\n\n",
        "- [Tasks by paradigm family](tasks_by_paradigm_family.md) lists every task under its family, with the\n  family's scope statement.\n",
        "- [Tasks alphabetically](tasks_alphabetically.md) lists every task in name order, for when you\n"
        "  know the name and not the family.\n\n",
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
            [("Tasks by paradigm family", "tasks_by_paradigm_family"), ("Tasks alphabetically", "tasks_alphabetically")], 3
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
    """Write docs/tasks/tasks_by_paradigm_family.md: one section per family, nesting the family pages.

    A family's section lists the tasks filed under it in full, then the tasks cross-listed
    into it as a short "Also filed here" list, each naming its own family and the reason.
    """
    parts: list[str] = [
        "# Tasks by paradigm family\n\n",
        f"The {len(families)} paradigm families, each with its scope statement and the tasks filed\n"
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
    write_page(tasks_dir / "tasks_by_paradigm_family.md", "".join(parts))
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
        f"All {len(sorted_tasks)} tasks in name order, each with the paradigm family it is filed\n"
        "under. [Tasks by paradigm family](tasks_by_paradigm_family.md) presents the same tasks grouped by\n"
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


def _write_task_page(
    tasks_dir: Path,
    task: dict,
    fam: dict,
    family_by_id: dict[str, dict],
    processes_by_id: dict[str, dict],
    atlas_map: dict[str, dict],
) -> int:
    """Write an individual task page docs/tasks/{hedtsk_id}.md."""
    hedtsk_id = task["hedtsk_id"]
    canonical_name = task["canonical_name"]
    aliases = task.get("aliases", [])
    inclusion = task.get("inclusion_test", {})
    variations = task.get("variations", [])
    hed_process_ids = task.get("hed_process_ids", [])
    is_pseudo = task.get("task_kind") == "pseudo_task"

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
    if is_pseudo:
        parts.append(
            ":::{note}\n"
            "**Pseudo task.** A block that establishes or holds a state, or collects a self-report,\n"
            "rather than eliciting a cognitive process through a trial structure. It is in the Catalog\n"
            "so that such blocks can be labelled with the same vocabulary as the tasks around them.\n"
            "See [Pseudo tasks](../methods/task_criteria/01_task_selection_criteria.md#task-criteria-1-3) in the task criteria.\n"
            ":::\n\n"
        )
    if aliases:
        parts.append(f"**Also known as:** {', '.join(aliases)}\n\n")
    parts.append(f"{task.get('short_definition', '')}\n\n")

    parts.append("## Description\n\n")
    parts.append(f"{task.get('description', '')}\n\n")

    parts.append("## Inclusion test\n\n")
    parts.append(
        "An experiment is an instance of this task when its procedure matches, it manipulates at\n"
        "least one of the listed variables, and it records at least one of the listed measures.\n\n"
    )
    parts.append("```{list-table}\n:widths: 15 85\n:header-rows: 0\n\n")
    parts.append(f"* - **Procedure**\n  - {inclusion.get('procedure', '')}\n")
    parts.append(f"* - **Manipulation**\n  - {inclusion.get('manipulation', '')}\n")
    parts.append(f"* - **Measurement**\n  - {inclusion.get('measurement', '')}\n")
    parts.append("```\n\n")

    if variations:
        parts.append("## Variations\n\n")
        parts.append(
            "Named versions that change what the participant experiences or does. The identifier\n"
            "of a variation is `hedvar_<task>__<variation>`.\n\n"
        )
        parts.append("```{list-table}\n:widths: 25 40 35\n:header-rows: 1\n\n")
        parts.append("* - Variation\n  - Description\n  - Justification\n")
        for var in variations:
            var_id = var.get("variation_id", "")
            parts.append(f"* - {var.get('name', '')}\n")
            if var_id:
                # A second paragraph inside the cell, so the id sits under the name.
                parts.append(f"\n    `{var_id}`\n")
            parts.append(f"  - {var.get('description', '')}\n")
            parts.append(f"  - {var.get('justification', '')}\n")
        parts.append("```\n\n")

    if is_pseudo and not hed_process_ids:
        parts.append("## Cognitive processes\n\n")
        parts.append(
            "None by design. A pseudo task sets up or holds a state rather than probing a process;\n"
            "the processes engaged during the block are whatever the participant brings to it.\n\n"
        )
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

    if atlas_id:
        label = atlas_name or "Cognitive Atlas entry"
        qualifier = f" ({atlas_match} match)" if atlas_match and atlas_match != "exact" else ""
        parts.append("## External links\n\n")
        parts.append(f"- Cognitive Atlas: [{label}]({ATLAS_TASK_URL}{atlas_id}){qualifier}\n\n")

    write_page(tasks_dir / f"{hedtsk_id}.md", "".join(parts))
    return 1
