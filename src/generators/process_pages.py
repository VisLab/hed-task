"""Generate the process section of the site.

Files written:

- docs/processes/index.md           the process landing page: what a process is, the
                                    categories at a glance, and the two ways in
- docs/processes/by_category.md     one section per category with its scope, and under
                                    it one short section per process; its toctree nests
                                    the category pages
- docs/processes/alphabetically.md  every process in name order, each with its category
- docs/processes/{category_id}.md   one page per category: scope, out of scope, open
                                    issues, then one section per process

Processes have no page of their own. A process lives as a section on its category page,
and every link to a process (from task pages, the listing pages, the cross-reference)
points at that section's anchor; see `process_anchor` in utils. The per-process
sub-lists (tasks, references) are run-in bold labels rather than headings, so that a
category page's contents menu lists the processes and nothing else.

The document tree is Cognitive processes > Processes by category > category, and the
left sidebar shows only the first two levels (a rule in docs/source/_static/custom.css
hides deeper entries); the right-hand contents menu of the listing pages takes over from
there, in the same arrangement as the task section.
"""

from __future__ import annotations

import re
from pathlib import Path

from generators.utils import citation_line, process_anchor, split_references, table, task_link, write_page


def generate(
    docs_dir: Path,
    processes: list[dict],
    categories: list[dict],
    tasks_by_id: dict[str, dict],
) -> int:
    """Write the process index page and all category pages.

    Returns the number of files written.
    """
    procs_dir = docs_dir / "processes"

    processes_by_category: dict[str, list[dict]] = {}
    for proc in processes:
        processes_by_category.setdefault(proc["category_id"], []).append(proc)

    sorted_categories = sorted(categories, key=lambda c: c["name"])

    count = 0
    count += _write_process_index(procs_dir, sorted_categories, processes_by_category)
    count += _write_by_category(procs_dir, sorted_categories, processes_by_category)
    count += _write_alphabetical(procs_dir, sorted_categories, processes)
    for cat in sorted_categories:
        cat_procs = processes_by_category.get(cat["category_id"], [])
        count += _write_category_page(procs_dir, cat, cat_procs)
    return count


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


def _engaged_by(proc: dict) -> str:
    """Return the closing phrase of a listing entry: how many tasks engage the process."""
    n = len(proc.get("tasks", []))
    if n == 0:
        return "engaged by no task in the current Catalog"
    return f"engaged by {n} task{'s' if n != 1 else ''}"


def _process_sections(cat_id: str, procs: list[dict], level: int) -> str:
    """Return one short section per process: a heading linked to the process's anchor on
    its category page, then the full definition and the task count.

    Parameters:
        cat_id: The category whose page holds the processes.
        procs: The processes to list, in display order.
        level: Markdown heading level for each process.
    """
    parts: list[str] = []
    for proc in procs:
        parts.append(f"{'#' * level} [{proc['process_name']}]({cat_id}.md#{process_anchor(proc['process_id'])})\n\n")
        engaged = _engaged_by(proc)
        parts.append(f"{proc.get('definition', '').strip()} {engaged[0].upper()}{engaged[1:]}.\n\n")
    return "".join(parts)


def _write_process_index(
    procs_dir: Path,
    sorted_categories: list[dict],
    processes_by_category: dict[str, list[dict]],
) -> int:
    """Write docs/processes/index.md: the landing page, nesting the two listing pages."""
    all_procs = [p for procs in processes_by_category.values() for p in procs]
    total_procs = len(all_procs)
    n_linked = sum(1 for p in all_procs if p.get("tasks"))
    n_cats = len(sorted_categories)

    rows = [
        [f"[{cat['name']}]({cat['category_id']}.md)", str(len(processes_by_category.get(cat["category_id"], [])))]
        for cat in sorted_categories
    ]
    content = (
        "# Cognitive processes\n\n"
        f"The Catalog defines {total_procs} cognitive processes organized into {n_cats} categories.\n"
        "A process is a mental operation hypothesized to occur during a trial, with an\n"
        "identifiable onset, an eliciting condition and a measurable signature; the\n"
        "[process selection criteria](../methods/process_criteria/index.md) say what qualifies and\n"
        "what does not. Each process has a definition, references, and links to the tasks that\n"
        f"engage it. {n_linked} of the {total_procs} processes are engaged by at least one task in the\n"
        "Catalog; the rest are kept because the Catalog may grow a task for them.\n\n"
        "Categories group processes by research tradition for browsing. They are organizational\n"
        "labels, not ontological commitments: a process belongs to the category whose scope best\n"
        "describes where it is studied, and categories imply no inheritance.\n\n"
        "Two ways in:\n\n"
        "- [Processes by category](by_category.md) lists every process under its category, with\n"
        "  the category's scope statement.\n"
        "- [Processes alphabetically](alphabetically.md) lists every process in name order, for\n"
        "  when you know the name and not the category.\n\n"
        "## Categories at a glance\n\n"
        + table(["Category", "Processes"], rows)
        + "\n\n"
        + _toctree([("Processes by category", "by_category"), ("Processes alphabetically", "alphabetically")], 2)
    )
    write_page(procs_dir / "index.md", content)
    return 1


def _write_by_category(
    procs_dir: Path,
    sorted_categories: list[dict],
    processes_by_category: dict[str, list[dict]],
) -> int:
    """Write docs/processes/by_category.md: one section per category, nesting the category pages."""
    parts: list[str] = [
        "# Processes by category\n\n",
        f"The {len(sorted_categories)} categories, each with its scope statement and the processes filed\n"
        "under it. Every process is in exactly one category. The category pages add what is out\n"
        "of scope, open issues, and each process's aliases, tasks and references. The\n"
        "[alphabetical list](alphabetically.md) has the same processes in name order.\n\n",
        # The right-hand contents menu is this page's navigation: the categories are always
        # listed, and a category's processes unfold while that category is the current
        # section. Furo's scroll-spy marks the current heading's entry and its ancestors
        # with scroll-current, so a click on a category opens it. Page-specific, hence inline.
        "<style>\n"
        ".toc-tree li li > ul { display: none; }\n"
        ".toc-tree li li.scroll-current > ul { display: block; }\n"
        "</style>\n\n",
    ]
    for cat in sorted_categories:
        cat_id = cat["category_id"]
        scope = _publish(cat.get("scope", ""), (cat_id, "scope"), _PUBLISHED_CATEGORY_FIELDS, f"scope for category {cat_id!r}")
        procs = sorted(processes_by_category.get(cat_id, []), key=lambda p: p["process_name"])
        parts.append(f"## [{cat['name']}]({cat_id}.md)\n\n")
        parts.append(f"{scope}\n\n")
        parts.append(_process_sections(cat_id, procs, 3))

    parts.append(_toctree([(cat["name"], cat["category_id"]) for cat in sorted_categories], 1))
    write_page(procs_dir / "by_category.md", "".join(parts))
    return 1


def _write_alphabetical(procs_dir: Path, sorted_categories: list[dict], processes: list[dict]) -> int:
    """Write docs/processes/alphabetically.md: one short section per process, in name order."""
    cat_name = {c["category_id"]: c["name"] for c in sorted_categories}
    parts: list[str] = [
        "# Processes alphabetically\n\n",
        f"All {len(processes)} processes in name order, each with the category it is filed under.\n"
        "[Processes by category](by_category.md) presents the same processes grouped by category.\n\n",
    ]
    for proc in sorted(processes, key=lambda p: p["process_name"]):
        cat_id = proc["category_id"]
        parts.append(f"## [{proc['process_name']}]({cat_id}.md#{process_anchor(proc['process_id'])})\n\n")
        parts.append(
            f"{proc.get('definition', '').strip()} Filed under\n[{cat_name[cat_id]}]({cat_id}.md); {_engaged_by(proc)}.\n\n"
        )
    write_page(procs_dir / "alphabetically.md", "".join(parts))
    return 1


# Text in the catalog data that records when something changed rather than what is true.
# A published page states the current state, so these fields are republished from the
# table below instead of verbatim. The better fix is to reword the field in
# data/process_details.json itself (it is edited here by pull request) and delete the
# entry below; the table exists for text that has not been rewritten yet.
#
# Rewriting each one by hand, rather than stripping clauses with a regex, is deliberate.
# The history is frequently *inside* a live sentence ("Trust as a process (vs. trust as
# a trait) was discussed during the reframe but no dedicated row was added"), so any
# mechanical clause removal either keeps the history or leaves an ungrammatical fragment.
#
# An empty string means the field was nothing but history and is not published at all.
_HISTORY_MARKER = re.compile(
    r"20\d{2}-\d{2}-\d{2}"
    r"|\bpre-reframe\b|\bpre-20\d{2}\b|\breframe\b"
    r"|\brenamed\b|\bwas merged\b|\bwere merged\b|\bmerged from\b"
    r"|\bdropped as separate\b|\bduplicate entry\b|\bwas discussed\b"
    r"|\bwas moved out\b|\bresolved 20\d{2}\b|\babsorbed as\b",
    re.IGNORECASE,
)

# Keyed by (category_id, field).
_PUBLISHED_CATEGORY_FIELDS = {
    ("associative_learning_and_reinforcement", "issues"): "",
    ("cognitive_flexibility_and_higher_order_executive_function", "out_of_scope"): (
        "Fluid intelligence (an individual-difference construct, not a process); "
        "working-memory updating (in Short-Term and Working Memory); "
        '"cognitive flexibility" as a capacity-level umbrella (alias on '
        "`hed_set_shifting`)."
    ),
    ("emotion_perception_and_regulation", "issues"): (
        "Coverage of appraisal-stage processes is thin - expected to grow if paradigms "
        "that specifically target appraisal are added."
    ),
    ("inhibitory_control_and_conflict_monitoring", "issues"): (
        "The proactive/reactive control split is paradigm-bound (AX-CPT-style designs); "
        "retained but worth revisiting if the Catalog adds paradigms that dissociate "
        "other control modes."
    ),
    ("language_comprehension_and_production", "issues"): (
        "Reading as a process versus reading as a behavior is still somewhat conflated in `hed_reading` - an open question."
    ),
    ("social_cognition_and_strategic_social_choice", "scope"): (
        "Theory of mind (canonical: `hed_perspective_taking`), self-other distinction, "
        "joint attention, imitation, in-group/out-group processing, stereotyping, "
        "social decision-making, social perception, cooperation, competition, "
        "reciprocity."
    ),
    ("social_cognition_and_strategic_social_choice", "issues"): (
        "Trust as a process (versus trust as a trait) has no dedicated row; if a Trust "
        "Game process row becomes warranted, it fits here."
    ),
    ("short_term_and_working_memory", "out_of_scope"): (
        "Working memory **load** (task parameter, not process); working memory "
        "**capacity** (individual difference); long-term memory; bare "
        '"maintenance" (the canonical row is `hed_active_maintenance`).'
    ),
}

# Keyed by alias name.
_PUBLISHED_ALIAS_NOTES = {
    "Operant conditioning": ("Skinnerian terminology; emphasizes the operant response and reinforcement schedules."),
    "Cognitive flexibility": (
        "Broader construct encompassing set shifting, perspective-taking, and adaptive "
        "strategy use; it fails the single-answer inclusion test, and set shifting is "
        "its primary experimental operationalization."
    ),
    "Gustation": "",
    "Somatosensation": "",
    "Logical reasoning": (
        "Broader term encompassing deductive and inductive forms; its definition is a "
        "union of the two, and the Wason Selection Task links here."
    ),
    "Maintenance": (
        "Generic term for holding information over a delay; active maintenance "
        "emphasizes the volitional, attention-demanding character."
    ),
    "Updating": 'Plain "Updating" is memory-context-underspecified.',
    "Updating (WM)": "",
    "Mentalizing": "Process verb; more common in the neuroimaging literature.",
}


def _publish(value: str, key, table_, what: str) -> str:
    """Return the text to publish for one source field.

    Falls back to the source verbatim when it carries no change-log language. Raises if
    new history appears with no entry in the table, so it cannot ship unnoticed.
    """
    if key in table_:
        return table_[key]
    if value and _HISTORY_MARKER.search(value):
        raise ValueError(
            f"{what} contains change-log language but has no entry in the published-text "
            f"table in src/generators/process_pages.py: {value!r}. Add a rewritten "
            f"version (or an empty string to drop it), or update _HISTORY_MARKER."
        )
    return value


def _format_aliases(aliases: list) -> str:
    """Format a list of aliases (strings or dicts with name/note)."""
    parts = []
    for alias in aliases:
        if isinstance(alias, dict):
            name = alias.get("name", "")
            note = _publish(alias.get("note", ""), name, _PUBLISHED_ALIAS_NOTES, f"alias note for {name!r}")
            parts.append(f"**{name}** - {note}" if note else name)
        else:
            parts.append(str(alias))
    return "; ".join(parts)


def _citations(refs: list[dict]) -> list[str]:
    return [citation_line(r) for r in refs if r.get("citation_string")]


def _write_category_page(procs_dir: Path, category: dict, cat_procs: list[dict]) -> int:
    """Write docs/processes/{category_id}.md."""
    cat_id = category["category_id"]
    name = category["name"]
    scope = _publish(
        category.get("scope", ""), (cat_id, "scope"), _PUBLISHED_CATEGORY_FIELDS, f"scope for category {cat_id!r}"
    )
    out_of_scope = _publish(
        category.get("out_of_scope", ""),
        (cat_id, "out_of_scope"),
        _PUBLISHED_CATEGORY_FIELDS,
        f"out_of_scope for category {cat_id!r}",
    )
    issues = _publish(
        category.get("issues", ""), (cat_id, "issues"), _PUBLISHED_CATEGORY_FIELDS, f"issues for category {cat_id!r}"
    )
    sorted_procs = sorted(cat_procs, key=lambda p: p["process_name"])

    parts: list[str] = []
    parts.append(f"({cat_id})=\n")
    parts.append(f"# {name}\n\n")
    parts.append(f"**Scope:** {scope}\n\n")
    if out_of_scope:
        parts.append(f"**Out of scope:** {out_of_scope}\n\n")
    if issues:
        parts.append(f":::{{note}}\n**Open issues:** {issues}\n:::\n\n")

    # The `history` field in the source data is a change log for the category - what was
    # merged, dropped or renamed, with dates. A published page states what is true now,
    # so it is deliberately not rendered. The field is left in the source untouched.

    # No summary table here: the sections below carry the full definitions, and the
    # right-hand contents menu lists the processes.
    parts.append(f"This category contains {len(sorted_procs)} processes.\n\n")

    for proc in sorted_procs:
        proc_id = proc["process_id"]
        # Explicit anchor target for deep linking. Hyphens, so the Sphinx label registry
        # entry matches the HTML id (Sphinx normalises label underscores to hyphens).
        parts.append(f"({process_anchor(proc_id)})=\n")
        parts.append(f"## {proc['process_name']}\n\n")
        parts.append(f"**Process ID:** `{proc_id}`\n\n")
        if proc.get("aliases"):
            parts.append(f"**Also known as:** {_format_aliases(proc['aliases'])}\n\n")
        parts.append(f"{proc.get('definition', '')}\n\n")

        tasks = sorted(proc.get("tasks", []), key=lambda t: t["canonical_name"])
        if tasks:
            links = ", ".join(task_link(t["hedtsk_id"], t["canonical_name"], "processes") for t in tasks)
            parts.append(f"**Tasks that engage this process:** {links}\n\n")
        else:
            parts.append("**Tasks that engage this process:** none in the current Catalog.\n\n")

        fund_refs, further_refs = split_references(proc)
        fund = _citations(fund_refs)
        if fund:
            parts.append("**Fundamental references**\n\n")
            parts.extend(f"- {c}\n" for c in fund)
            parts.append("\n")
        further = _citations(further_refs)
        if further:
            parts.append("**Further references**\n\n")
            parts.extend(f"- {c}\n" for c in further)
            parts.append("\n")

    write_page(procs_dir / f"{cat_id}.md", "".join(parts))
    return 1
