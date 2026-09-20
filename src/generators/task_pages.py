"""Generate the task section of the site.

Files written:

- docs/tasks/index.md            the task landing page: what a task page holds, the
                                 families at a glance, and the two ways in
- docs/tasks/by_family.md        the catalog grouped by paradigm family, one section
                                 per family; its toctree nests the family pages
- docs/tasks/families/<id>.md    one page per family, whose toctree nests its tasks
- docs/tasks/alphabetically.md   every task in name order; its toctree lists every
                                 task
- docs/tasks/hedtsk_*.md         one page per task

The document tree is Tasks > Tasks by paradigm family > family > task, and Tasks >
Tasks alphabetically > task. Each task page sits in two toctrees, which Sphinx allows
(it picks the first as the parent for prev/next links). The left sidebar shows only the
first two levels; a rule in docs/source/_static/custom.css hides the family and task
entries, and the right-hand contents menu of the two listing pages takes over from
there. Listing headings and sidebar labels drop a trailing "Task", "tasks" or "tests"
from a name; page titles keep it. See `_short_name`.

Families come from data/task_families.tsv and data/task_family_defs.tsv; see
data/README.md. The assignment is validated in generate_docs.py before anything is
written, so this module can assume every task has exactly one known family.
"""

from __future__ import annotations

import sys
from pathlib import Path

from generators.utils import cell, citation_line, process_link, split_references, table, write_page

ATLAS_TASK_URL = "https://www.cognitiveatlas.org/task/id/"


def generate(
    docs_dir: Path,
    tasks: list[dict],
    processes_by_id: dict[str, dict],
    families: list[dict],
    family_rows: list[dict],
    atlas_map: dict[str, dict] | None = None,
) -> int:
    """Write the task index, the family pages, the alphabetical list and the task pages.

    Parameters:
        docs_dir: The docs/source/ root.
        tasks: Task records from data/task_details.json.
        processes_by_id: Process records keyed by process_id.
        families: Rows of data/task_family_defs.tsv, already sorted by `order`.
        family_rows: Rows of data/task_families.tsv.
        atlas_map: Rows of data/mappings/hed_task_to_atlas.tsv keyed by hedtsk_id.

    Returns the number of files written.
    """
    tasks_dir = docs_dir / "tasks"
    sorted_tasks = sorted(tasks, key=lambda t: t["canonical_name"])
    family_of = {r["hedtsk_id"]: r["family_id"] for r in family_rows}
    confidence_of = {r["hedtsk_id"]: r["confidence"] for r in family_rows}
    family_by_id = {f["family_id"]: f for f in families}
    tasks_by_family: dict[str, list[dict]] = {f["family_id"]: [] for f in families}
    for task in sorted_tasks:
        tasks_by_family[family_of[task["hedtsk_id"]]].append(task)

    count = 0
    count += _write_task_index(tasks_dir, families, tasks_by_family, confidence_of)
    count += _write_by_family(tasks_dir, families, tasks_by_family)
    for fam in families:
        count += _write_family_page(tasks_dir, fam, tasks_by_family[fam["family_id"]], family_rows)
    count += _write_alphabetical(tasks_dir, sorted_tasks, family_of, family_by_id)
    for task in sorted_tasks:
        fam = family_by_id[family_of[task["hedtsk_id"]]]
        count += _write_task_page(tasks_dir, task, fam, processes_by_id, atlas_map or {})
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


def _task_sections(fam_tasks: list[dict], link_prefix: str, level: int) -> str:
    """Return one short section per task: a linked heading, the full short definition,
    and the number of processes the task engages.

    The family listings used to be tables, which truncated the short definitions. A
    section per task shows the whole definition and puts every task in the page's
    right-hand contents menu.

    Parameters:
        fam_tasks: The tasks to list, in display order.
        link_prefix: Path prefix from the page being written to the task pages.
        level: Markdown heading level for each task.
    """
    parts: list[str] = []
    for task in fam_tasks:
        name = _short_name(task["canonical_name"])
        n_procs = len(task.get("hed_process_ids", []))
        engages = "no process links (pseudo task)" if n_procs == 0 else f"{n_procs} process{'es' if n_procs != 1 else ''}"
        parts.append(f"{'#' * level} [{name}]({link_prefix}{task['hedtsk_id']}.md)\n\n")
        parts.append(f"{task.get('short_definition', '').strip()} Engages {engages}.\n\n")
    return "".join(parts)


def _write_task_index(
    tasks_dir: Path,
    families: list[dict],
    tasks_by_family: dict[str, list[dict]],
    confidence_of: dict[str, str],
) -> int:
    """Write docs/tasks/index.md."""
    all_tasks = [t for v in tasks_by_family.values() for t in v]
    n_pseudo = sum(1 for t in all_tasks if t.get("task_kind") == "pseudo_task")
    n_tasks = len(all_tasks) - n_pseudo
    n_review = sum(1 for c in confidence_of.values() if c == "review")

    parts: list[str] = [
        "# Tasks\n\n",
        f"The catalog defines {n_tasks} standard cognitive and behavioral neuroscience tasks, and\n"
        f"{n_pseudo} pseudo tasks (rest, fixation and questionnaire blocks) that set up or hold a state\n"
        "rather than eliciting a process.\n"
        "Each task page gives the canonical name and aliases, a description, the inclusion\n"
        "test that decides whether an experiment is an instance of the task, its named\n"
        "variations, the cognitive processes it engages, and references.\n\n",
        f"Tasks are filed under {len(families)} **paradigm families** by what the participant does,\n"
        "not by which process the task is thought to measure. The process catalog covers that\n"
        "other axis, and the two cross-link. A family is a browsing aid; every task is in\n"
        "exactly one, the assignment is a curation decision, and it is expected to change as\n"
        f"the catalog grows. {n_review} of the {n_tasks} assignments are marked for review in the\n"
        "source table because a reasonable reader could file the task elsewhere; the family\n"
        "pages say which.\n\n",
        "Two ways in:\n\n",
        "- [Tasks by paradigm family](by_family.md) lists every task under its family, with the\n  family's scope statement.\n",
        "- [Tasks alphabetically](alphabetically.md) lists every task in name order, for when you\n"
        "  know the name and not the family.\n\n",
        "## Families at a glance\n\n",
    ]

    rows = [
        [f"[{fam['name']}](families/{fam['family_id']}.md)", str(len(tasks_by_family[fam["family_id"]]))] for fam in families
    ]
    parts.append(table(["Family", "Tasks"], rows))
    parts.append("\n\n")
    parts.append(_toctree([("Tasks by paradigm family", "by_family"), ("Tasks alphabetically", "alphabetically")], 3))

    write_page(tasks_dir / "index.md", "".join(parts))
    return 1


def _write_by_family(tasks_dir: Path, families: list[dict], tasks_by_family: dict[str, list[dict]]) -> int:
    """Write docs/tasks/by_family.md: one section per family, nesting the family pages."""
    parts: list[str] = [
        "# Tasks by paradigm family\n\n",
        f"The {len(families)} paradigm families, each with its scope statement and the tasks filed\n"
        "under it. Every task is in exactly one family. The family pages repeat these entries\n"
        "and add the assignments marked for review. The [alphabetical list](alphabetically.md)\n"
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
        parts.append(_task_sections(fam_tasks, "", 3))

    parts.append(_toctree([(_short_name(fam["name"]), f"families/{fam['family_id']}") for fam in families], 2))
    write_page(tasks_dir / "by_family.md", "".join(parts))
    return 1


def _write_family_page(tasks_dir: Path, fam: dict, fam_tasks: list[dict], family_rows: list[dict]) -> int:
    """Write docs/tasks/families/<family_id>.md."""
    fid = fam["family_id"]
    by_task = {r["hedtsk_id"]: r for r in family_rows if r["family_id"] == fid}
    review = [t for t in fam_tasks if by_task[t["hedtsk_id"]]["confidence"] == "review"]

    parts: list[str] = [
        f"({fid})=\n",
        f"# {fam['name']}\n\n",
        f"{fam['scope']}\n\n",
        f"This family contains {len(fam_tasks)} tasks.\n\n",
        _task_sections(fam_tasks, "../", 2),
    ]

    if review:
        parts.append("## Marked for review\n\n")
        parts.append(
            "The filing of these tasks is a judgement call; the note says why they are here and\nwhere else they could go.\n\n"
        )
        rows = [
            [f"[{_short_name(t['canonical_name'])}](../{t['hedtsk_id']}.md)", cell(by_task[t["hedtsk_id"]]["rationale"])]
            for t in review
        ]
        parts.append(table(["Task", "Note"], rows))
        parts.append("\n\n")

    parts.append(_toctree([(_short_name(t["canonical_name"]), f"../{t['hedtsk_id']}") for t in fam_tasks], 1))

    write_page(tasks_dir / "families" / f"{fid}.md", "".join(parts))
    return 1


def _write_alphabetical(
    tasks_dir: Path,
    sorted_tasks: list[dict],
    family_of: dict[str, str],
    family_by_id: dict[str, dict],
) -> int:
    """Write docs/tasks/alphabetically.md: one short section per task, in name order.

    Like the family listings, each task is a linked heading followed by its full short
    definition, so the right-hand contents menu lists every task under the page title.
    Here the closing sentence also names the family the task is filed under.
    """
    parts: list[str] = [
        "# Tasks alphabetically\n\n",
        f"All {len(sorted_tasks)} tasks in name order, each with the paradigm family it is filed\n"
        "under. [Tasks by paradigm family](by_family.md) presents the same tasks grouped by\n"
        "family.\n\n",
    ]
    for task in sorted_tasks:
        fam = family_by_id[family_of[task["hedtsk_id"]]]
        n_procs = len(task.get("hed_process_ids", []))
        engages = "no process links (pseudo task)" if n_procs == 0 else f"{n_procs} process{'es' if n_procs != 1 else ''}"
        parts.append(f"## [{_short_name(task['canonical_name'])}]({task['hedtsk_id']}.md)\n\n")
        parts.append(
            f"{task.get('short_definition', '').strip()} Filed under\n"
            f"[{fam['name']}](families/{fam['family_id']}.md); engages {engages}.\n\n"
        )
    parts.append(_toctree([(_short_name(t["canonical_name"]), t["hedtsk_id"]) for t in sorted_tasks], 1))
    write_page(tasks_dir / "alphabetically.md", "".join(parts))
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
    parts.append(f"**Family:** [{fam['name']}](families/{fam['family_id']}.md)\n\n")
    if is_pseudo:
        parts.append(
            ":::{note}\n"
            "**Pseudo task.** A block that establishes or holds a state, or collects a self-report,\n"
            "rather than eliciting a cognitive process through a trial structure. It is in the catalog\n"
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
                parts.append(f"- {process_link(pid, proc['process_name'], proc['category_id'], 'tasks')}\n")
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
