"""One-time migration: the inclusion test becomes three lists.

Kept as the record of what was done on 2026-09-23; it refuses to run a second time.

Before: `inclusion_test` on a task record was three strings, `procedure`, `manipulation`
and `measurement`. The second and third were, in almost every record, several clauses
joined by semicolons; the first was one or two sentences.

After: three lists, `procedure` (ordered steps, each a sentence), `manipulations` and
`measurements` (unordered items, each a fragment with a capital and no final period).
Plan: .status/plans/inclusion_test_lists.md, approved by Kay 2026-09-23 with procedure
as a list.

The split is mechanical and then checked by hand. Manipulations and measurements split
on a semicolon outside parentheses. A procedure splits on a semicolon outside
parentheses and on a sentence boundary (a period, question mark or exclamation mark
followed by a space and a capital letter), except after the abbreviations e.g., i.e.,
vs., etc., cf. and a single capital letter. An item's first letter is capitalized only
when its first word is an ordinary lowercase word, so initialisms such as `fMRI` and
conventionally lowercase terms such as `d-prime` keep their case. Every record whose
result looks doubtful is printed so that it can be read: an item under 12 characters,
unbalanced parentheses in an item, a procedure of more than four steps, an item ending in
a colon, or a manipulation or measurement item that still contains a comma outside
parentheses (a list the semicolon rule could not see).

The comma lists and the few splits the rules got wrong are corrected by `HAND_FIXES`,
applied after the mechanical split, so that running this script on the pre-migration
file reproduces the committed data exactly. Items with commas that name one measure
("Accuracy and RT for action identification, direction discrimination, or detection")
are left whole; only lists of distinct measures were split.

Run from the repository root on the file as it was before the migration (commit 3f5effd):

    git show 3f5effd:data/task_details.json > original.json
    python src/migrate_inclusion_tests.py --source original.json --out data/task_details.json
    python src/migrate_inclusion_tests.py --source original.json --dry-run   # report only

Run src/generate_docs.py afterwards to validate and regenerate.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"

# A sentence boundary: end punctuation, space, capital letter. Abbreviations that end in
# a period are handled separately in _split_sentences.
_SENTENCE = re.compile(r"(?<=[.!?])\s+(?=[A-Z(\"'])")
_ABBREVIATIONS = ("e.g.", "i.e.", "vs.", "etc.", "cf.", "approx.")
# A first word that may be capitalized: lowercase letters, optionally hyphenated, whose
# first segment has at least two letters. This leaves `fMRI`, `eCorsi`, `d-prime` and
# `d'` alone.
_PLAIN_WORD = re.compile(r"^[a-z]{2,}(?:-[a-z]+)*$")

# Record-specific corrections applied after the mechanical split: comma lists of distinct
# measures or variables, and the sentence the splitter left starting with "May". Keyed by
# hedtsk_id, then field; the value replaces that field's list.
HAND_FIXES: dict[str, dict[str, list[str]]] = {
    "hedtsk_attention_network": {
        "manipulations": [
            "Cue type (no cue, center cue, double cue, spatial cue)",
            "Flanker congruency (congruent, incongruent)",
        ],
        "measurements": [
            "Alerting network score (double-cue minus no-cue RT)",
            "Orienting network score (center-cue minus spatial-cue RT)",
            "Executive network score (incongruent minus congruent RT)",
        ],
    },
    "hedtsk_self_paced_reading": {
        "manipulations": [
            "Syntactic ambiguity at the critical region (reduced relative clause, garden-path)",
            "Semantic plausibility (plausible vs. implausible continuation)",
            "Discourse coherence (coherent vs. incoherent continuation)",
            "Anaphor type (pronoun, repeated name, definite NP)",
            "Word predictability (high vs. low cloze probability)",
            "Syntactic complexity (embedded clause, long-distance dependency)",
        ],
    },
    "hedtsk_affective_picture_viewing": {
        "procedure": [
            "Participants view emotionally valenced images (e.g., IAPS) presented for several seconds each.",
            "Participants may rate valence and arousal or simply view while physiological signals are recorded.",
        ],
        "measurements": [
            "Subjective valence and arousal ratings (SAM)",
            "Skin conductance",
            "Startle reflex magnitude",
            "Corrugator and zygomatic EMG",
            "ERP components (LPP)",
            "fMRI amygdala/PFC activation",
        ],
    },
    "hedtsk_continuous_performance": {
        "measurements": [
            "Hit rate",
            "False alarm rate",
            "d-prime (sensitivity)",
            "RT and RT variability",
            "Omission and commission errors",
        ],
    },
    "hedtsk_n_back": {
        "measurements": ["Hit rate", "False alarm rate", "d-prime", "RT", "Load-dependent accuracy decline"],
    },
    "hedtsk_old_new_recognition_memory": {
        "measurements": [
            "Hit rate",
            "False alarm rate",
            "d-prime (discriminability)",
            "Criterion (response bias)",
            "Confidence ratings",
            "ROC curves",
            "ERP old/new effects (FN400, LPC)",
            "RT",
        ],
    },
    "hedtsk_virtual_morris_water_maze": {
        "measurements": [
            "Path length and latency to reach the hidden platform",
            "Probe trial time in target quadrant",
            "Probe trial proximity to platform location",
            "Learning curve across trials",
            "Heading error",
        ],
    },
}
# A first word that may be capitalized: lowercase letters, optionally hyphenated, whose
# first segment has at least two letters. This leaves `fMRI`, `eCorsi`, `d-prime` and
# `d'` alone.
_PLAIN_WORD = re.compile(r"^[a-z]{2,}(?:-[a-z]+)*$")

# Record-specific corrections applied after the mechanical split: comma lists of distinct
# measures or variables, and the sentence the splitter left starting with "May". Keyed by
# hedtsk_id, then field; the value replaces that field's list.
HAND_FIXES: dict[str, dict[str, list[str]]] = {
    "hedtsk_attention_network": {
        "manipulations": [
            "Cue type (no cue, center cue, double cue, spatial cue)",
            "Flanker congruency (congruent, incongruent)",
        ],
        "measurements": [
            "Alerting network score (double-cue minus no-cue RT)",
            "Orienting network score (center-cue minus spatial-cue RT)",
            "Executive network score (incongruent minus congruent RT)",
        ],
    },
    "hedtsk_self_paced_reading": {
        "manipulations": [
            "Syntactic ambiguity at the critical region (reduced relative clause, garden-path)",
            "Semantic plausibility (plausible vs. implausible continuation)",
            "Discourse coherence (coherent vs. incoherent continuation)",
            "Anaphor type (pronoun, repeated name, definite NP)",
            "Word predictability (high vs. low cloze probability)",
            "Syntactic complexity (embedded clause, long-distance dependency)",
        ],
    },
    "hedtsk_affective_picture_viewing": {
        "procedure": [
            "Participants view emotionally valenced images (e.g., IAPS) presented for several seconds each.",
            "Participants may rate valence and arousal or simply view while physiological signals are recorded.",
        ],
        "measurements": [
            "Subjective valence and arousal ratings (SAM)",
            "Skin conductance",
            "Startle reflex magnitude",
            "Corrugator and zygomatic EMG",
            "ERP components (LPP)",
            "fMRI amygdala/PFC activation",
        ],
    },
    "hedtsk_continuous_performance": {
        "measurements": [
            "Hit rate",
            "False alarm rate",
            "d-prime (sensitivity)",
            "RT and RT variability",
            "Omission and commission errors",
        ],
    },
    "hedtsk_n_back": {
        "measurements": ["Hit rate", "False alarm rate", "d-prime", "RT", "Load-dependent accuracy decline"],
    },
    "hedtsk_old_new_recognition_memory": {
        "measurements": [
            "Hit rate",
            "False alarm rate",
            "d-prime (discriminability)",
            "Criterion (response bias)",
            "Confidence ratings",
            "ROC curves",
            "ERP old/new effects (FN400, LPC)",
            "RT",
        ],
    },
    "hedtsk_virtual_morris_water_maze": {
        "measurements": [
            "Path length and latency to reach the hidden platform",
            "Probe trial time in target quadrant",
            "Probe trial proximity to platform location",
            "Learning curve across trials",
            "Heading error",
        ],
    },
}


def _split_top_level(text: str) -> list[str]:
    """Split on semicolons that are not inside parentheses."""
    parts, depth, start = [], 0, 0
    for i, ch in enumerate(text):
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif ch == ";" and depth == 0:
            parts.append(text[start:i])
            start = i + 1
    parts.append(text[start:])
    return [p.strip() for p in parts if p.strip()]


def _split_sentences(text: str) -> list[str]:
    """Split a procedure clause into sentences, keeping abbreviations intact."""
    out, buffer = [], ""
    for piece in _SENTENCE.split(text):
        candidate = (buffer + " " + piece).strip() if buffer else piece
        lowered = candidate.lower()
        # Keep accumulating while the candidate ends in an abbreviation or a single
        # capital letter with a period (an initial), which is not a sentence end.
        if lowered.endswith(_ABBREVIATIONS) or re.search(r"(?:^|\s)[A-Z]\.$", candidate):
            buffer = candidate
            continue
        out.append(candidate)
        buffer = ""
    if buffer:
        out.append(buffer)
    return [s.strip() for s in out if s.strip()]


def _capitalize(item: str) -> str:
    """Capitalize the first letter when the first word is an ordinary lowercase word."""
    first = item.split(" ", 1)[0] if item else ""
    if _PLAIN_WORD.match(first):
        return item[:1].upper() + item[1:]
    return item


def _fragment(item: str) -> str:
    """Normalize a manipulation or measurement item: capital first letter, no final period."""
    return _capitalize(item.strip().rstrip(".").strip())


def _sentence(item: str) -> str:
    """Normalize a procedure step: capital first letter, ends in a period."""
    item = _capitalize(item.strip())
    if not item:
        return item
    return item if item.endswith((".", "!", "?")) else item + "."


def _top_level_comma(text: str) -> bool:
    """True when a comma sits outside every pair of parentheses."""
    depth = 0
    for ch in text:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        elif ch == "," and depth == 0:
            return True
    return False


def split_procedure(text: str) -> list[str]:
    steps = []
    for clause in _split_top_level(text):
        steps.extend(_sentence(s) for s in _split_sentences(clause))
    return steps


def split_items(text: str) -> list[str]:
    return [_fragment(p) for p in _split_top_level(text)]


def doubts(hedtsk_id: str, test: dict) -> list[str]:
    """Return the reasons a migrated record should be read by hand."""
    found = []
    for field, items in test.items():
        for item in items:
            if len(item) < 12:
                found.append(f"{field}: short item {item!r}")
            if item.count("(") != item.count(")"):
                found.append(f"{field}: unbalanced parentheses in {item!r}")
            if item.endswith(":"):
                found.append(f"{field}: item ends in a colon {item!r}")
        if field == "procedure" and len(items) > 4:
            found.append(f"procedure: {len(items)} steps")
        if field != "procedure":
            for item in items:
                if _top_level_comma(item):
                    found.append(f"{field}: comma outside parentheses, a list or one measure? {item!r}")
    return found


def migrate(tasks: list[dict]) -> tuple[list[dict], dict[str, list[str]]]:
    report: dict[str, list[str]] = {}
    for task in tasks:
        old = task["inclusion_test"]
        if "manipulations" in old:
            sys.exit(f"{task['hedtsk_id']}: already migrated; refusing to run twice.")
        new = {
            "procedure": split_procedure(old["procedure"]),
            "manipulations": split_items(old["manipulation"]),
            "measurements": split_items(old["measurement"]),
        }
        for field, items in new.items():
            if not items:
                sys.exit(f"{task['hedtsk_id']}: {field} split to nothing from {old!r}")
        for field, items in HAND_FIXES.get(task["hedtsk_id"], {}).items():
            new[field] = list(items)
        for field, items in HAND_FIXES.get(task["hedtsk_id"], {}).items():
            new[field] = list(items)
        task["inclusion_test"] = new
        found = doubts(task["hedtsk_id"], new)
        if found:
            report[task["hedtsk_id"]] = found
    return tasks, report


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--source", type=Path, default=DATA / "task_details.json")
    parser.add_argument("--out", type=Path, default=None, help="write here instead of over the source")
    parser.add_argument("--dry-run", action="store_true", help="print the report, write nothing")
    args = parser.parse_args()

    tasks = json.loads(args.source.read_text(encoding="utf-8"))
    tasks, report = migrate(tasks)

    counts = {
        "procedure": sum(len(t["inclusion_test"]["procedure"]) for t in tasks),
        "manipulations": sum(len(t["inclusion_test"]["manipulations"]) for t in tasks),
        "measurements": sum(len(t["inclusion_test"]["measurements"]) for t in tasks),
    }
    print(
        f"{len(tasks)} records: {counts['procedure']} procedure steps, {counts['manipulations']} manipulations, {counts['measurements']} measurements."
    )
    print(f"{len(report)} records to read by hand:")
    for hedtsk_id, found in report.items():
        print(f"  {hedtsk_id}")
        for reason in found:
            print(f"    - {reason}")

    if args.dry_run:
        print("\n--dry-run given; nothing written.")
        return
    out = args.out or args.source
    out.write_text(json.dumps(tasks, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")
    print(f"\nWrote {out}.")


if __name__ == "__main__":
    main()
