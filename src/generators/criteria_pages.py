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
# The dot must be escaped: unescaped, it matches a backtick, which lets the pattern span
# from an unrelated code span all the way to the next .status_2/ reference and delete
# every heading and paragraph in between.
_RE_STATUS2_FILE = re.compile(r"`[^`]*\.status_2/[^`]+`")

# Pattern 3: "documented in detail in `.status_2/decisions_log.md`, `.status_2/umbrella_decisions.md`, and `.status_2/side_findings_resolutions.md`"
# Matches the whole comma-and-"and" separated run of backticked references. The previous
# form used `[^.]*` between them, which stopped at the "." inside ".status_2/" and so
# consumed the next reference's opening backtick - leaving an orphan backtick that the
# pattern above then spanned from, deleting every heading in between.
_RE_DOCUMENTED_IN = re.compile(
    r"documented in detail in\s+`[^`]+`(?:\s*,\s*(?:and\s+)?`[^`]+`)*"
    r"(?:\s+and\s+`[^`]+`)?",
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


# The issues-and-policy-questions section is a register of resolved and open working
# questions - project history, not reference material, so it is cut from the published
# page. The open questions it held are tracked as GitHub issues instead. Anchored on the
# heading rather than a line number so it survives edits to the source document.
_RE_ISSUES_SECTION = re.compile(
    r"\n#{2,3}\s*\d*\.?\s*Known Issues and Policy Questions.*?(?=\n## |\Z)",
    re.DOTALL | re.IGNORECASE,
)

# Likewise the "Resolved Decisions" summary: a dated log of what was merged, dropped or
# renamed. Same reasoning - a published page states the current criteria, not how they
# were arrived at.
_RE_DECISIONS_SECTION = re.compile(
    r"\n#{2,3}\s*\d*\.?\s*Resolved Decisions.*?(?=\n## |\Z)",
    re.DOTALL | re.IGNORECASE,
)

_DATE = r"\d{4}-\d{2}-\d{2}"

# Dates record when a rule changed; the rule itself is what the page is for. These run in
# order so that a date is removed together with whatever introduces it, rather than
# leaving "retired on ." or "As of , 19 of 172 processes".
_DATE_SUBSTITUTIONS = [
    # A "**Date:** 2026-04-18 (updated)" line in the document header.
    (re.compile(r"^\*\*Date:\*\*[^\n]*\n", re.MULTILINE), ""),
    # "As of 2026-04-19, 19 of 172 processes ..." -> "19 of 172 processes ..."
    (re.compile(r"\bAs of\s+" + _DATE + r",\s*", re.IGNORECASE), ""),
    # Heading suffixes: "- RESOLVED 2026-04-18", "- REVIEWED", "(2026-04-18)".
    (re.compile(r"\s*[—-]\s*RESOLVED\s*\(?" + _DATE + r"\)?", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*RESOLVED\b", re.IGNORECASE), ""),
    (re.compile(r"\s*\((?:refined|updated)\s+" + _DATE + r"\)"), ""),
    (re.compile(r"\s*\(" + _DATE + r"\)"), ""),
    # "retired on 2026-04-17" -> "retired"; "applied 2026-04-18" -> "applied".
    (re.compile(r"\s+on\s+" + _DATE + r"\b"), ""),
    (re.compile(r"\s+" + _DATE + r"\b"), ""),
    # The file-reference strip above turns "(`...variation_audit.md`, applied <date>)"
    # into "(applied)" once the date goes; drop the now-empty parenthetical.
    (re.compile(r"\s*\((?:applied|updated|refined)\)"), ""),
]

# Removing a file reference can leave a preposition pointing at nothing, or a space
# floating before punctuation. These repair the sentence rather than leaving the seam
# visible on the published page.
_DROP_LINE_SUBSTITUTIONS = [
    # An orphaned sentence about where a superseded working document went. Once its file
    # reference is stripped it says nothing at all.
    (re.compile(r"^[^\n]*previously held this content[^\n]*\n", re.MULTILINE), ""),
    # The schema bullet for the `history` field. The field still exists in the source
    # data, but the pages deliberately do not render it, so advertising it here would
    # send a reader looking for something that is not on any page.
    (re.compile(r"^- \*\*`history`\*\*[^\n]*\n", re.MULTILINE), ""),
]

_TIDY_SUBSTITUTIONS = [
    # The \s+ before the punctuation is what makes this safe: it only matches where a
    # removal left a gap ("archived to ."), never legitimate prose that ends on a
    # preposition ("what it all adds up to.").
    (re.compile(r"\s+(?:to|in|at|from)\s+([.,;])"), r"\1"),
    (re.compile(r"\(\s*\)"), ""),
    (re.compile(r"[ \t]+([.,;:])"), r"\1"),
    (re.compile(r"([.,;:])\1+"), r"\1"),
    # Removing a trailing section can leave the separator that preceded it as the last
    # thing in the file; Sphinx rejects a document that ends on a transition.
    (re.compile(r"\n+(?:-{3,}|_{3,})\s*$"), "\n"),
]


def _clean_criteria(text: str) -> str:
    """Apply all substitutions to strip internal file references."""

    # Order matters: do more specific replacements first.

    # Drop the working registers entirely: open/resolved issues and the decisions log.
    text = _RE_ISSUES_SECTION.sub("\n", text)
    text = _RE_DECISIONS_SECTION.sub("\n", text)

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

    # Dates last, so they also catch anything the reference strips above left behind,
    # and so the empty-parenthetical cleanup runs after the text that creates one.
    for pattern, replacement in _DATE_SUBSTITUTIONS:
        text = pattern.sub(replacement, text)

    # Drop lines that say nothing once their file references are gone.
    for pattern, replacement in _DROP_LINE_SUBSTITUTIONS:
        text = pattern.sub(replacement, text)

    # Finally, repair punctuation stranded by a removal: "archived to ." -> "archived."
    for pattern, replacement in _TIDY_SUBSTITUTIONS:
        text = pattern.sub(replacement, text)

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
