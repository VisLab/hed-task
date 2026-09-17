"""Generate docs/criteria/index.md, task_criteria.md, and process_criteria.md."""

from __future__ import annotations

import re
from pathlib import Path

from generators.utils import write_page

# ---------------------------------------------------------------------------
# Regex patterns for stripping internal file references
# ---------------------------------------------------------------------------

# Pattern 1: parenthetical like (see `.status_2/criteria_review_2026-04-17.md` section 2.5)
_RE_SEE_PARENTHETICAL = re.compile(
    r"\(see\s+`[^`]+\.status_2/[^`]+`[^)]*\)",
    re.IGNORECASE,
)

# Pattern 2: backtick references to .status_2/ files
_RE_STATUS2_FILE = re.compile(r"`[^`]*.status_2/[^`]+`")

# Pattern 3: "documented in detail in `.status_2/decisions_log.md`, `.status_2/umbrella_decisions.md`, and `.status_2/side_findings_resolutions.md`"
_RE_DOCUMENTED_IN = re.compile(
    r"documented in detail in\s+`[^`]+decisions_log[^`]+`[^.]*"
    r"(?:,\s*`[^`]+`)*(?:\s*and\s*`[^`]+`)?",
    re.IGNORECASE,
)

# Pattern 4: "The variation audit (`.status_2/variation_audit.md`, applied YYYY-MM-DD)" -> keep date
_RE_VARIATION_AUDIT = re.compile(
    r"\(`\.status_2/variation_audit\.md`,\s*",
    re.IGNORECASE,
)

# Pattern 5: backtick `original_3/` directory references
_RE_ORIGINAL3 = re.compile(r"`original_3/[^`]*`")

# Pattern 6: Script references
_RE_SCRIPT = re.compile(r"`outputs/regenerate_derived_files\.py`")

# Pattern 7: `process_reference.md` and `process_categories.md` have been archived to `original_3/` ...
_RE_ARCHIVED_LINE = re.compile(
    r"`process_reference\.md`\s*and\s*`process_categories\.md`\s*have been archived to\s*`original_3/`[^.]*\.",
    re.IGNORECASE,
)

# Pattern 8: Verified against `process_reference.md` before archival.
_RE_VERIFIED_AGAINST = re.compile(
    r"Verified against\s*`process_reference\.md`\s*before archival\.",
    re.IGNORECASE,
)

# Pattern 9: See `.status_2/working_memory_updating_rename_2026-04-17.md`.
_RE_SEE_FILE_SENTENCE = re.compile(
    r"See\s+`[^`]+\.status_2/[^`]+`\.",
    re.IGNORECASE,
)

# Pattern 10: remaining bare `process_reference.md` or `process_categories.md` references
_RE_PROCESS_REF_MD = re.compile(r"`process_reference\.md`", re.IGNORECASE)
_RE_PROCESS_CAT_MD = re.compile(r"`process_categories\.md`", re.IGNORECASE)


def _clean_criteria(text: str) -> str:
    """Apply all substitutions to strip internal file references."""

    # Order matters: do more specific replacements first.

    # "documented in detail in ..." -> "documented in the project's decision records"
    text = _RE_DOCUMENTED_IN.sub("documented in the project's decision records", text)

    # "The prior reference and categories documents have been archived"
    text = _RE_ARCHIVED_LINE.sub("The prior reference and categories documents have been archived.", text)

    # Verified against `process_reference.md` before archival.
    text = _RE_VERIFIED_AGAINST.sub("Verified against the prior reference document before archival.", text)

    # (see `.status_2/criteria_review_2026-04-17.md` section 2.5) -> ""
    text = _RE_SEE_PARENTHETICAL.sub("", text)

    # See `.status_2/...`. -> ""  (sentence-ending)
    text = _RE_SEE_FILE_SENTENCE.sub("", text)

    # The variation audit (`.status_2/variation_audit.md`, applied -> (applied
    text = _RE_VARIATION_AUDIT.sub("(", text)

    # Any remaining .status_2/ backtick refs
    text = _RE_STATUS2_FILE.sub("", text)

    # `original_3/...` references
    text = _RE_ORIGINAL3.sub("", text)

    # Script references
    text = _RE_SCRIPT.sub("", text)

    # `process_reference.md` -> "the prior reference document"
    text = _RE_PROCESS_REF_MD.sub("the prior reference document", text)

    # `process_categories.md` -> "the prior categories document"
    text = _RE_PROCESS_CAT_MD.sub("the prior categories document", text)

    # Clean up doubled spaces / leading spaces within lines left by removals
    # But do not collapse intentional blank lines.
    lines = text.split("\n")
    cleaned = []
    for line in lines:
        # Collapse multiple internal spaces (but not leading indentation)
        stripped = line.rstrip()
        # Collapse runs of 2+ spaces that aren't at the start
        inner = re.sub(r"(?<=\S) {2,}", " ", stripped)
        cleaned.append(inner)
    return "\n".join(cleaned)


def generate(docs_dir: Path, working_dir: Path) -> int:
    """Write docs/criteria/index.md, task_criteria.md, process_criteria.md.

    Returns the number of files written.
    """
    criteria_dir = docs_dir / "criteria"
    count = 0

    # --- index.md ---
    index_content = """\
# Criteria and methodology

These documents describe the criteria used to select and define the tasks
and cognitive processes in the HED catalog.

```{toctree}
:maxdepth: 2

task_criteria
process_criteria
```
"""
    write_page(criteria_dir / "index.md", index_content)
    count += 1

    # --- task_criteria.md ---
    src_task = working_dir / "tasks_criteria.md"
    raw_task = src_task.read_text(encoding="utf-8")
    cleaned_task = _clean_criteria(raw_task)
    write_page(criteria_dir / "task_criteria.md", cleaned_task)
    count += 1

    # --- process_criteria.md ---
    src_proc = working_dir / "process_criteria.md"
    raw_proc = src_proc.read_text(encoding="utf-8")
    cleaned_proc = _clean_criteria(raw_proc)
    write_page(criteria_dir / "process_criteria.md", cleaned_proc)
    count += 1

    return count
