"""Generate docs/processes/index.md and docs/processes/{category_id}.md (x19)."""

from __future__ import annotations

import re
from pathlib import Path

from generators.utils import truncate, write_page


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

    # Build per-category process lists
    processes_by_category: dict[str, list[dict]] = {}
    for proc in processes:
        cat_id = proc["category_id"]
        processes_by_category.setdefault(cat_id, []).append(proc)

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
    total_procs = sum(len(v) for v in processes_by_category.values())
    n_cats = len(sorted_categories)

    lines: list[str] = [
        "# Process catalog\n",
        "\n",
        f"This catalog defines {total_procs} cognitive processes organized into {n_cats} categories.\n",
        "Each process has a definition, references, and links to the tasks that engage it.\n",
        "Of the 172 processes, 152 are linked to at least one task in the task catalog.\n",
        "\n",
        "## Categories\n",
        "\n",
        "| Category | Processes | Description |\n",
        "|----------|-----------|-------------|\n",
    ]

    for cat in sorted_categories:
        cat_id = cat["category_id"]
        name = cat["name"]
        # Publish-clean the scope before truncating: truncation would otherwise hide
        # change-log text just past the cut, or expose it just before.
        scope = _publish(
            cat.get("scope", ""),
            (cat_id, "scope"),
            _PUBLISHED_CATEGORY_FIELDS,
            f"scope for category {cat_id!r}",
        )
        scope = truncate(scope, 100)
        scope = scope.replace("|", "\\|")
        n_procs = len(processes_by_category.get(cat_id, []))
        lines.append(f"| [{name}]({cat_id}.md) | {n_procs} | {scope} |\n")

    lines.append("\n")
    lines.append("```{toctree}\n")
    lines.append(":hidden:\n")
    lines.append(":maxdepth: 1\n")
    lines.append("\n")
    for cat in sorted_categories:
        lines.append(f"{cat['category_id']}\n")
    lines.append("```\n")

    write_page(procs_dir / "index.md", "".join(lines))
    return 1


# Text in the source data that records when something changed rather than what is true.
# A published page states the current state, so these fields are republished from the
# table below instead of verbatim. The source in .working/ is never edited - it is
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


def _publish(value: str, key, table, what: str) -> str:
    """Return the text to publish for one source field.

    Falls back to the source verbatim when it carries no change-log language. Raises if
    new history appears with no entry in the table, so it cannot ship unnoticed.
    """
    if key in table:
        return table[key]
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
            note = _publish(
                alias.get("note", ""),
                name,
                _PUBLISHED_ALIAS_NOTES,
                f"alias note for {name!r}",
            )
            if note:
                parts.append(f"**{name}** \u2014 {note}")
            else:
                parts.append(name)
        else:
            parts.append(str(alias))
    return "; ".join(parts)


def _write_category_page(
    procs_dir: Path,
    category: dict,
    cat_procs: list[dict],
) -> int:
    """Write docs/processes/{category_id}.md."""
    cat_id = category["category_id"]
    name = category["name"]
    scope = _publish(
        category.get("scope", ""),
        (cat_id, "scope"),
        _PUBLISHED_CATEGORY_FIELDS,
        f"scope for category {cat_id!r}",
    )
    out_of_scope = _publish(
        category.get("out_of_scope", ""),
        (cat_id, "out_of_scope"),
        _PUBLISHED_CATEGORY_FIELDS,
        f"out_of_scope for category {cat_id!r}",
    )
    issues = _publish(
        category.get("issues", ""),
        (cat_id, "issues"),
        _PUBLISHED_CATEGORY_FIELDS,
        f"issues for category {cat_id!r}",
    )
    process_count = len(cat_procs)

    parts: list[str] = []

    parts.append(f"# {name}\n\n")
    parts.append(f"**Scope:** {scope}\n\n")

    if out_of_scope:
        parts.append(f"**Out of scope:** {out_of_scope}\n\n")

    if issues:
        parts.append(":::{note}\n")
        parts.append(f"**Open issues:** {issues}\n")
        parts.append(":::\n\n")

    # The `history` field in the source data is a change log for the category - what was
    # merged, dropped or renamed, with dates. A published page states what is true now,
    # so it is deliberately not rendered. The field is left in the source untouched.

    parts.append(f"This category contains {process_count} processes.\n\n")
    parts.append("---\n\n")

    sorted_procs = sorted(cat_procs, key=lambda p: p["process_name"])

    for proc in sorted_procs:
        proc_id = proc["process_id"]
        proc_name = proc["process_name"]
        definition = proc.get("definition", "")
        aliases = proc.get("aliases", [])
        tasks = proc.get("tasks", [])
        fund_refs = proc.get("fundamental_references", [])
        recent_refs = proc.get("recent_references", [])

        # Explicit anchor target for deep linking
        # Use hyphens so the Sphinx label registry entry matches the HTML id
        # (Sphinx normalises label underscores->hyphens in rendered HTML IDs).
        parts.append(f"({proc_id.replace('_', '-')})=\n")
        parts.append(f"## {proc_name}\n\n")
        parts.append(f"**Process ID:** `{proc_id}`\n\n")

        if aliases:
            parts.append(f"**Also known as:** {_format_aliases(aliases)}\n\n")

        parts.append(f"{definition}\n\n")

        if tasks:
            sorted_tasks = sorted(tasks, key=lambda t: t["canonical_name"])
            parts.append("### Tasks\n\n")
            parts.append("The following tasks engage this process:\n\n")
            for task in sorted_tasks:
                tid = task["hedtsk_id"]
                tname = task["canonical_name"]
                parts.append(f"- [{tname}](../tasks/{tid}.md)\n")
            parts.append("\n")
        else:
            parts.append("*No tasks in the current catalog are linked to this process.*\n\n")

        if fund_refs:
            parts.append("### Fundamental references\n\n")
            for ref in fund_refs:
                citation = ref.get("citation_string", "")
                if citation:
                    parts.append(f"- {citation}\n")
            parts.append("\n")

        if recent_refs:
            parts.append("### Recent references\n\n")
            for ref in recent_refs:
                citation = ref.get("citation_string", "")
                if citation:
                    parts.append(f"- {citation}\n")
            parts.append("\n")

        if proc is not sorted_procs[-1]:
            parts.append("---\n\n")

    write_page(procs_dir / f"{cat_id}.md", "".join(parts))
    return 1
