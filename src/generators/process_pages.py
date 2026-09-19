"""Generate docs/processes/index.md and docs/processes/{category_id}.md (one per category).

A category page opens with the category's scope, what is out of scope, any open issue,
and a summary table of its processes, then gives one section per process. The per-process
sub-lists (tasks, references) are run-in bold labels rather than headings, so that the
page's table of contents lists the processes and nothing else.
"""

from __future__ import annotations

import re
from pathlib import Path

from generators.utils import cell, citation_line, process_anchor, split_references, table, task_link, truncate, write_page


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
    for cat in sorted_categories:
        cat_procs = processes_by_category.get(cat["category_id"], [])
        count += _write_category_page(procs_dir, cat, cat_procs)
    return count


def _write_process_index(
    procs_dir: Path,
    sorted_categories: list[dict],
    processes_by_category: dict[str, list[dict]],
) -> int:
    """Write docs/processes/index.md."""
    all_procs = [p for procs in processes_by_category.values() for p in procs]
    total_procs = len(all_procs)
    n_linked = sum(1 for p in all_procs if p.get("tasks"))
    n_cats = len(sorted_categories)

    rows = []
    for cat in sorted_categories:
        cat_id = cat["category_id"]
        # Publish-clean the scope before truncating: truncation would otherwise hide
        # change-log text just past the cut, or expose it just before.
        scope = _publish(cat.get("scope", ""), (cat_id, "scope"), _PUBLISHED_CATEGORY_FIELDS, f"scope for category {cat_id!r}")
        rows.append(
            [
                f"[{cat['name']}]({cat_id}.md)",
                str(len(processes_by_category.get(cat_id, []))),
                cell(truncate(scope, 110)),
            ]
        )

    content = (
        "# Cognitive processes\n\n"
        f"The catalog defines {total_procs} cognitive processes organized into {n_cats} categories.\n"
        "A process is a mental operation hypothesized to occur during a trial, with an\n"
        "identifiable onset, an eliciting condition and a measurable signature; the\n"
        "[process selection criteria](../methods/process_criteria/index.md) say what qualifies and\n"
        "what does not. Each process has a definition, references, and links to the tasks that\n"
        f"engage it. {n_linked} of the {total_procs} processes are engaged by at least one task in the\n"
        "catalog; the rest are kept because the catalog may grow a task for them.\n\n"
        "Categories group processes by research tradition for browsing. They are organizational\n"
        "labels, not ontological commitments: a process belongs to the category whose scope best\n"
        "describes where it is studied, and categories imply no inheritance.\n\n"
        "## Categories\n\n" + table(["Category", "Processes", "Scope"], rows) + "\n\n"
        "```{toctree}\n:hidden:\n:maxdepth: 1\n\n" + "".join(f"{cat['category_id']}\n" for cat in sorted_categories) + "```\n"
    )
    write_page(procs_dir / "index.md", content)
    return 1


# Text in the source data that records when something changed rather than what is true.
# A published page states the current state, so these fields are republished from the
# table below instead of verbatim. The source in data/ is never edited - it is
# produced elsewhere and an edit here would be lost on the next import.
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
        "retained but worth revisiting if the catalog adds paradigms that dissociate "
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

    parts.append(f"This category contains {len(sorted_procs)} processes.\n\n")
    rows = [
        [
            f"[{p['process_name']}](#{process_anchor(p['process_id'])})",
            cell(truncate(p.get("definition", ""), 120)),
            str(len(p.get("tasks", []))),
        ]
        for p in sorted_procs
    ]
    parts.append(table(["Process", "Definition", "Tasks"], rows))
    parts.append("\n\n")

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
            parts.append("**Tasks that engage this process:** none in the current catalog.\n\n")

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
