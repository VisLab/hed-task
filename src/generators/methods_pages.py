"""Generate docs/methods/ - how the catalog was scoped, selected and mapped.

Three pages:

- task_criteria.md and process_criteria.md are republished from the working documents
  `.working/tasks_criteria.md` and `.working/process_criteria.md`, with internal file
  references, dated change-log language and the working registers of open questions
  stripped, and headings normalised to sentence case. The source is never edited; it is
  produced elsewhere and an edit here would be lost on the next import.
- atlas_mapping.md documents the method behind `.working/mappings/`: where the data comes
  from, what the match vocabulary means, how variations are identified, and what is and
  is not verified. Counts are read from the mapping tables so the page cannot drift.
"""

from __future__ import annotations

import collections
import re
from pathlib import Path

from generators.utils import read_tsv, table, write_page

# ---------------------------------------------------------------------------
# Criteria pages: strip internal references and history
# ---------------------------------------------------------------------------

# Pattern 1: parenthetical like (see `.status_2/criteria_review_2026-04-17.md` section 2.5)
_RE_SEE_PARENTHETICAL = re.compile(r"\(see\s+`[^`]+\.status_2/[^`]+`[^)]*\)", re.IGNORECASE)

# Pattern 2: backtick references to .status_2/ files. The dot must be escaped: unescaped,
# it matches a backtick, which lets the pattern span from an unrelated code span all the
# way to the next .status_2/ reference and delete every heading and paragraph in between.
_RE_STATUS2_FILE = re.compile(r"`[^`]*\.status_2/[^`]+`")

# Pattern 3: "documented in detail in `a`, `b`, and `c`". Matches the whole run of
# backticked references so no orphan backtick is left behind.
_RE_DOCUMENTED_IN = re.compile(
    r"documented in detail in\s+`[^`]+`(?:\s*,\s*(?:and\s+)?`[^`]+`)*(?:\s+and\s+`[^`]+`)?",
    re.IGNORECASE,
)

# Pattern 4: "The variation audit (`.status_2/variation_audit.md`, applied YYYY-MM-DD)"
_RE_VARIATION_AUDIT = re.compile(r"\(`\.status_2/variation_audit\.md`,\s*", re.IGNORECASE)

# Pattern 5: `original_3/` directory references
_RE_ORIGINAL3 = re.compile(r"`original_3/[^`]*`")

# Pattern 6: script references
_RE_SCRIPT = re.compile(r"`outputs/regenerate_derived_files\.py`")

# Pattern 7: the archived-documents sentence in the process criteria header
_RE_ARCHIVED_LINE = re.compile(
    r"`process_reference\.md`\s*and\s*`process_categories\.md`\s*have been archived to\s*`original_3/`[^.]*\.",
    re.IGNORECASE,
)

# Pattern 8: "Verified against `process_reference.md` before archival."
_RE_VERIFIED_AGAINST = re.compile(r"Verified against\s*`process_reference\.md`\s*before archival\.", re.IGNORECASE)

# Pattern 9: "See `.status_2/...`."
_RE_SEE_FILE_SENTENCE = re.compile(r"See\s+`[^`]+\.status_2/[^`]+`\.", re.IGNORECASE)

# Pattern 10: remaining bare references to the archived working documents
_RE_PROCESS_REF_MD = re.compile(r"`process_reference\.md`", re.IGNORECASE)
_RE_PROCESS_CAT_MD = re.compile(r"`process_categories\.md`", re.IGNORECASE)

# The companion-document sentence in the process criteria header points at the working
# file name; on the site the companion is a page.
_RE_COMPANION = re.compile(r"Companion to\s+`tasks_criteria\.md`\s*\(task-side criteria\)\.", re.IGNORECASE)
_RE_EDITORIAL_NOTES = re.compile(
    r"Per-category editorial notes \(scope, out-of-scope, issues, history\) are now in\s+`process_details\.json`;\s*",
    re.IGNORECASE,
)

# The issues-and-policy-questions section is a register of resolved and open working
# questions - project history, not reference material, so it is cut from the published
# page. The open questions it held are tracked as GitHub issues instead.
_RE_ISSUES_SECTION = re.compile(
    r"\n#{2,3}\s*\d*\.?\s*Known Issues and Policy Questions.*?(?=\n## |\Z)",
    re.DOTALL | re.IGNORECASE,
)

# Likewise the "Resolved Decisions" summary: a dated log of what was merged, dropped or
# renamed. A published page states the current criteria, not how they were arrived at.
_RE_DECISIONS_SECTION = re.compile(
    r"\n#{2,3}\s*\d*\.?\s*Resolved Decisions.*?(?=\n## |\Z)",
    re.DOTALL | re.IGNORECASE,
)

_DATE = r"\d{4}-\d{2}-\d{2}"

# Dates record when a rule changed; the rule itself is what the page is for. These run
# in order so that a date is removed together with whatever introduces it.
_DATE_SUBSTITUTIONS = [
    (re.compile(r"^\*\*Date:\*\*[^\n]*\n", re.MULTILINE), ""),
    (re.compile(r"\bAs of\s+" + _DATE + r",\s*", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*RESOLVED\s*\(?" + _DATE + r"\)?", re.IGNORECASE), ""),
    (re.compile(r"\s*[—-]\s*RESOLVED\b", re.IGNORECASE), ""),
    (re.compile(r"\s*\((?:refined|updated)\s+" + _DATE + r"\)"), ""),
    (re.compile(r"\s*\(" + _DATE + r"\)"), ""),
    (re.compile(r"\s+on\s+" + _DATE + r"\b"), ""),
    (re.compile(r"\s+" + _DATE + r"\b"), ""),
    (re.compile(r"\s*\((?:applied|updated|refined)\)"), ""),
]

_DROP_LINE_SUBSTITUTIONS = [
    # An orphaned sentence about where a superseded working document went.
    (re.compile(r"^[^\n]*previously held this content[^\n]*\n", re.MULTILINE), ""),
    # The schema bullet for the `history` field, which the pages deliberately do not render.
    (re.compile(r"^- \*\*`history`\*\*[^\n]*\n", re.MULTILINE), ""),
]

_TIDY_SUBSTITUTIONS = [
    # Only matches where a removal left a gap ("archived to ."), never legitimate prose.
    (re.compile(r"\s+(?:to|in|at|from)\s+([.,;])"), r"\1"),
    (re.compile(r"\(\s*\)"), ""),
    (re.compile(r"[ \t]+([.,;:])"), r"\1"),
    (re.compile(r"([.,;:])\1+"), r"\1"),
    # Sphinx rejects a document that ends on a transition.
    (re.compile(r"\n+(?:-{3,}|_{3,})\s*$"), "\n"),
]

# Words that keep their capitals when a heading is put into sentence case: acronyms,
# identifiers, and the emphasis capitals the source uses for rule names.
_KEEP_CAPS = {"HED", "IDs", "ID", "NOT", "DROP", "EMOT", "MEAS", "DESG", "JSON", "BIDS", "Cognitive", "Atlas"}

# Horizontal whitespace only: \s would swallow the blank line after the heading.
_HEADING = re.compile(r"^(#{1,6})[ \t]+(.*?)[ \t]*$", re.MULTILINE)


def _sentence_case(text: str) -> str:
    """Lower-case the Title Case words of a heading, leaving the first word, acronyms and
    listed proper nouns alone. Numbering such as "5.1" is passed through."""
    out: list[str] = []
    seen_first = False
    for word in text.split(" "):
        core = word.strip("()?:,.")
        if not any(ch.isalpha() for ch in core):
            out.append(word)
            continue
        if not seen_first:
            out.append(word)
            seen_first = True
            continue
        if core in _KEEP_CAPS or core.isupper() or "-" in core and any(p.isupper() for p in core.split("-")[1:]):
            out.append(word)
            continue
        if core[0].isupper() and core[1:].islower():
            idx = word.index(core[0])
            out.append(word[:idx] + core[0].lower() + word[idx + 1 :])
        else:
            out.append(word)
    return " ".join(out)


def _sentence_case_headings(text: str) -> str:
    return _HEADING.sub(lambda m: f"{m.group(1)} {_sentence_case(m.group(2))}", text)


def _clean_criteria(text: str) -> str:
    """Apply all substitutions to strip internal file references and history."""
    text = _RE_ISSUES_SECTION.sub("\n", text)
    text = _RE_DECISIONS_SECTION.sub("\n", text)
    text = _RE_DOCUMENTED_IN.sub("documented in the project's decision records", text)
    text = _RE_ARCHIVED_LINE.sub("The prior reference and categories documents have been archived.", text)
    text = _RE_VERIFIED_AGAINST.sub("Verified against the prior reference document before archival.", text)
    text = _RE_COMPANION.sub("Companion to the [task selection criteria](task_criteria.md).", text)
    text = _RE_EDITORIAL_NOTES.sub(
        "Per-category scope, out-of-scope and open-issue notes appear on each category page. ", text
    )
    text = _RE_SEE_PARENTHETICAL.sub("", text)
    text = _RE_SEE_FILE_SENTENCE.sub("", text)
    text = _RE_VARIATION_AUDIT.sub("(", text)
    text = _RE_STATUS2_FILE.sub("", text)
    text = _RE_ORIGINAL3.sub("", text)
    text = _RE_SCRIPT.sub("", text)
    text = _RE_PROCESS_REF_MD.sub("the prior reference document", text)
    text = _RE_PROCESS_CAT_MD.sub("the prior categories document", text)
    for pattern, replacement in _DATE_SUBSTITUTIONS:
        text = pattern.sub(replacement, text)
    for pattern, replacement in _DROP_LINE_SUBSTITUTIONS:
        text = pattern.sub(replacement, text)
    for pattern, replacement in _TIDY_SUBSTITUTIONS:
        text = pattern.sub(replacement, text)
    text = _sentence_case_headings(text)

    # Collapse runs of internal spaces left by removals, without touching indentation.
    lines = [re.sub(r"(?<=\S) {2,}", " ", line.rstrip()) for line in text.split("\n")]
    return "\n".join(lines)


# ---------------------------------------------------------------------------
# Atlas mapping method
# ---------------------------------------------------------------------------


def _mapping_page(working: Path) -> str:
    maps = working / "mappings"
    forward = read_tsv(maps / "hed_task_to_atlas.tsv")
    reverse = read_tsv(maps / "atlas_task_to_hed.tsv")
    proc_forward = read_tsv(maps / "hed_process_to_atlas.tsv")
    concept_reverse = read_tsv(maps / "atlas_concept_to_hed.tsv")

    fwd_types = collections.Counter(r["match_type"] for r in forward)
    rev_types = collections.Counter(r["match_type"] for r in reverse)
    rev_levels = collections.Counter(r["match_level"] for r in reverse if r["match_level"])
    scope = collections.Counter(r["scope_class"] for r in reverse if r["match_type"] == "none")
    kinds = ("exact", "close", "related", "none")

    fwd_table = table(
        ["Match type", "Tasks", "Share"],
        [[k, fwd_types[k], f"{round(100 * fwd_types[k] / len(forward))}%"] for k in kinds],
    )
    rev_table = table(
        ["Match type", "Atlas entries", "Share"],
        [[k, rev_types[k], f"{round(100 * rev_types[k] / len(reverse))}%"] for k in kinds],
    )
    level_table = table(
        ["Mapped to", "Atlas entries"],
        [["A HED task", rev_levels["task"]], ["A named variation of a HED task", rev_levels["variation"]]],
    )
    scope_table = table(
        ["Why no counterpart", "Atlas entries"],
        [
            [f"Experimental paradigm not in the {len(forward)}-task catalog", scope["paradigm"]],
            ["Self-report instrument", scope["questionnaire"]],
            ["Standardized test battery", scope["battery"]],
            ["Imaging protocol label", scope["imaging_protocol"]],
            ["Physiological procedure", scope["physiological"]],
        ],
    )

    proc_types = collections.Counter(r["match_type"] for r in proc_forward)
    concept_types = collections.Counter(r["match_type"] for r in concept_reverse)
    proc_table = table(
        ["Match type", "Processes", "Share"],
        [[k, proc_types[k], f"{round(100 * proc_types[k] / len(proc_forward))}%"] for k in kinds],
    )
    concept_table = table(
        ["Match type", "Atlas concepts", "Share"],
        [[k, concept_types[k], f"{round(100 * concept_types[k] / len(concept_reverse))}%"] for k in kinds],
    )
    concepts_used = len({r["atlas_concept_id"] for r in proc_forward if r["atlas_concept_id"]})
    matched_processes = proc_types["exact"] + proc_types["close"] + proc_types["related"]

    covered = len({r["hedtsk_id"] for r in reverse if r["hedtsk_id"]})
    variations_matched = len({r["hed_variation_id"] for r in reverse if r["hed_variation_id"]})

    meaning_table = table(
        ["Match type", "Meaning"],
        [
            ["`exact`", "The same paradigm or construct, under the same or an aliased name"],
            ["`close`", "The same family, but the Atlas entry is a variant, is broader, or is narrower"],
            ["`related`", "The Atlas has entries in the same area but none that corresponds"],
            ["`none`", "Nothing in the Atlas corresponds"],
        ],
    )
    verified_table = table(
        ["Table", "Rows", "State"],
        [
            ["`hed_task_to_atlas.tsv`", len(forward), "Every row checked against the archived Atlas record"],
            ["`atlas_task_to_hed.tsv`", len(reverse), "Every row assigned a match type; every matched row checked"],
            ["`hed_process_to_atlas.tsv`", len(proc_forward), "Every row checked against the archived concept definition"],
            ["`atlas_concept_to_hed.tsv`", len(concept_reverse), "Every row assigned a match type"],
        ],
    )

    return f"""\
# Mapping the catalog to the Cognitive Atlas

This page describes how the correspondence between this catalog and the
[Cognitive Atlas](https://www.cognitiveatlas.org/) was established, so that a reader
can judge how much weight each mapping carries. The row-by-row results are on the
[task mapping tables](../atlas/task_mapping.md) and
[process mapping tables](../atlas/process_mapping.md) pages.

## Source data

Every figure derives from a byte-exact archive of the Atlas REST API, taken in a single
snapshot covering both layers in full: {len(reverse)} tasks and {len(concept_reverse)}
concepts, with the detail record for each. Pulling the concept endpoint directly
matters, because a harvest taken from the task endpoint alone reaches a concept only
when some task asserts it, which hides about half the concept layer.

The mappings live in four tab-separated tables under `.working/mappings/` rather than
in these pages, so that any view can be generated from them. Each table has one row per
entity and a unique key.

## What a match type means

{meaning_table}

`close` and `related` carry real information and should not be read as weak versions of
`exact`. `close` says a counterpart exists but its boundaries differ, so a researcher
looking for the canonical paradigm will find something usable. `related` says the
search will turn up neighbours only.

## Matching at two levels

The Atlas frequently registers a specific implementation as its own entry rather than
recording it under the parent paradigm: eight separate Stroop entries, eight n-back,
six fluency. Many of those correspond not to a task in this catalog but to a *named
variation* of one.

Each mapping row therefore records whether it resolves to a task or to a variation.

{level_table}

Variations are addressed by a stable identifier of the form
`hedvar_<parent slug>__<variation slug>`, for example
`hedvar_stroop_color_word__counting_stroop`. The prefix types the identifier the same
way `hedtsk_` marks a task and `hed_` marks a process. The identifier is what makes a
variation referenceable: without one, a reference would have to name the variation, and
would break silently if that name were edited. The generator fails if a mapping row
names a variation that does not exist, or one whose parent task disagrees with the row.

## How the tables were built

Candidate matches come from normalized name and alias comparison, with an exact
task-name match taking precedence over a variation-name match. That precedence is not
cosmetic: the Atlas entry `2-stage decision task` matches the Two-Stage Decision Task
by name while also matching a variation listed under another task, and only the first
reading is correct.

**Automated matching decides nothing on its own.** On this data it produces false
positives and false negatives in both directions. `Judgment-of-Learning` matched
`Judgment of Line Orientation` because both abbreviate to "JOL". `Heartbeat Detection`
matched `visual pursuit/tracking`. `Trail Making` matched nothing although the Atlas
carries `Trail Making Test A and B`. Every row was therefore checked against the
archived Atlas record before being accepted.

## Coverage, catalog to Atlas

One row per task in this catalog, recording its primary Atlas counterpart.

{fwd_table}

## Coverage, Atlas to catalog

One row per Atlas task entry. {covered} of the catalog's tasks have at least one Atlas
entry pointing at them, and {variations_matched} named variations are matched by an
Atlas entry of their own.

{rev_table}

Most Atlas entries have no counterpart here, which is expected rather than a gap: this
catalog admits only event-producing experimental paradigms, while the Atlas mixes those
with instruments of several other kinds.

{scope_table}

The kind assigned to an unmatched entry is derived from its name by rule and is a
heuristic, not a hand-checked judgement. The `none` verdict itself was reviewed.

## Reading the two directions together

The directions answer different questions and can differ without contradiction. The
catalog-to-Atlas table asks whether the Atlas contains a given paradigm; the
Atlas-to-catalog table asks, for each Atlas entry, whether this catalog covers it.

Three tasks are `none` in the first table yet appear in the second with `related` rows:
Self-Paced Reading, Sentence Comprehension and Virtual Radial Arm Maze. The Atlas has
no entry that *is* any of those paradigms, but it does hold adjacent entries
(`Eye tracking paradigms`, `syntactic task`, `Porteus maze test`). Both statements are
true.

## Coverage, processes and concepts

The same method was applied to the second axis: {len(proc_forward)} cognitive processes
against {len(concept_reverse)} Atlas concepts. This mapping was built from nothing. The
process catalog carries no Atlas concept identifier of any kind, so there was no prior
linkage to correct, only to construct.

{proc_table}

{concept_table}

{concepts_used} distinct Atlas concepts are used by the {matched_processes}
matched processes, because several processes share one Atlas record: both metacognitive
processes resolve to `metacognition`, for example.

The `related` verdict does most of the interesting work here. It marks the cases where
the Atlas carries only a broader parent: `Affective priming` against `priming`,
`Social perception` against `perception`, `Fine motor control` against `motor control`.
Recording those as `close` would overstate what the Atlas offers.

The `none` verdicts fall into two groups. Some are constructs the Atlas never
registered as concepts even though it registers them as tasks, such as `Antisaccade` and
`Reversal learning`. Others are vocabulary that post-dates the Atlas's curation, notably
`Model-based learning`, `Model-free learning` and the general form of reward prediction
error, for which the Atlas has only `monetary reward prediction error`.

Definitions, not names, decided these. The Atlas concept named `acoustic processing`
looks like an exact match for the process of the same name, but its definition describes
"signals propagated undersea, in the atmosphere" -- sonar, not audition -- so it is
recorded as `close` with that noted. `Perspective taking` matched `worldview` by name
alone and was reassigned to `theory of mind`.

## What is verified

{verified_table}

Two things in these tables are not hand-checked. The `scope_class` on an unmatched Atlas
task is derived from its name by rule. And the `none` verdicts on the reverse tables
assert only that no counterpart exists in a catalog of {len(forward)} tasks and
{len(proc_forward)} processes, which is the expected answer for most of an
{len(reverse)}-entry and {len(concept_reverse)}-concept corpus.

## Reproducing this

    python src/fetch_cog_data.py        # refresh the API archive in .cog_data/
    python src/build_atlas_maps.py      # refresh the mapping tables

The second command is non-destructive. It never overwrites a match type, a mapped id,
or a curator note. It refreshes the descriptive columns, re-deriving them from
whichever id the curator chose rather than from the automated candidate, and reports
entities that have appeared in or disappeared from the Atlas since the last run.
Running it twice leaves the tables byte-identical.
"""


def generate(docs_dir: Path, working_dir: Path) -> int:
    """Write docs/methods/task_criteria.md, process_criteria.md and atlas_mapping.md.

    Returns the number of files written.
    """
    methods_dir = docs_dir / "methods"
    raw_task = (working_dir / "tasks_criteria.md").read_text(encoding="utf-8")
    write_page(methods_dir / "task_criteria.md", _clean_criteria(raw_task))
    raw_proc = (working_dir / "process_criteria.md").read_text(encoding="utf-8")
    write_page(methods_dir / "process_criteria.md", _clean_criteria(raw_proc))
    write_page(methods_dir / "atlas_mapping.md", _mapping_page(working_dir))
    return 3
