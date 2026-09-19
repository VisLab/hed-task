"""Give every task variation in data/task_details.json a stable slug id.

Variations previously had no identifier at all, only a name, so anything referring to
one had to key on the name and would break silently if the name were edited. This adds
a `variation_id` to each variation, derived deterministically from the parent task id
and the variation name.

Format::

    hedvar_<parent slug without the hedtsk_ prefix>__<variation slug>
    hedvar_stroop_color_word__counting_stroop

The `hedvar_` prefix follows the identifier convention in the task criteria
(docs/source/methods/task_criteria/02_naming_conventions.md) that an
identifier's prefix types it: `hedtsk_` is a task, `hed_` is a process, `hedvar_` is a
task variation. A double underscore separates the parent slug from the variation slug,
so the parent is always recoverable and the two parts never run together.

The slug is derived the same way task slugs are: strip a trailing "Task" or "Test",
lowercase, drop apostrophes, replace separators with underscores, collapse runs.

The script is idempotent and additive. It only ever inserts `variation_id`; it never
edits a name, description, or justification, and re-running it changes nothing.

    python src/add_variation_ids.py --check   # verify without writing
    python src/add_variation_ids.py           # add ids in place
"""

from __future__ import annotations

import argparse
import collections
import json
import re
from pathlib import Path

DEFAULT_TASKS = Path(__file__).parent.parent / "data" / "task_details.json"


def slugify(text: str) -> str:
    """Derive a slug using the same rules as the hedtsk_ task slugs."""
    value = (text or "").strip()
    value = re.sub(r"\s+(Task|Test)$", "", value, flags=re.IGNORECASE)
    value = value.lower()
    # Both apostrophe forms are deleted rather than turned into a separator, so
    # "Raven's" slugs to "ravens" and not "raven_s". The curly form is written as an
    # escape to keep the source ASCII-only.
    value = value.replace("'", "").replace("\u2019", "")
    value = re.sub(r"[^a-z0-9]+", "_", value)
    value = re.sub(r"_+", "_", value)
    return value.strip("_")


def variation_id(hedtsk_id: str, variation_name: str) -> str:
    parent = hedtsk_id[len("hedtsk_") :] if hedtsk_id.startswith("hedtsk_") else hedtsk_id
    return f"hedvar_{parent}__{slugify(variation_name)}"


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tasks", type=Path, default=DEFAULT_TASKS)
    parser.add_argument("--check", action="store_true", help="validate without writing")
    args = parser.parse_args()

    tasks = json.loads(args.tasks.read_text(encoding="utf-8"))

    seen: dict[str, list[str]] = collections.defaultdict(list)
    added = existing = 0

    for task in tasks:
        for variation in task.get("variations") or []:
            name = variation.get("name", "")
            new_id = variation_id(task["hedtsk_id"], name)
            if not slugify(name):
                raise SystemExit(f"{task['hedtsk_id']}: variation name yields an empty slug: {name!r}")
            seen[new_id.lower()].append(f"{task['hedtsk_id']} / {name}")
            if variation.get("variation_id") == new_id:
                existing += 1
                continue
            if "variation_id" in variation and variation["variation_id"] != new_id:
                raise SystemExit(
                    f"{task['hedtsk_id']}: variation {name!r} already has id "
                    f"{variation['variation_id']!r}, which is not the derived {new_id!r}"
                )
            # Insert the id first so it reads as the key of the record.
            variation_items = list(variation.items())
            variation.clear()
            variation["variation_id"] = new_id
            variation.update(variation_items)
            added += 1

    clashes = {k: v for k, v in seen.items() if len(v) > 1}
    if clashes:
        raise SystemExit(f"variation ids are not unique: {clashes}")

    total = sum(len(t.get("variations") or []) for t in tasks)
    print(f"{total} variations across {len(tasks)} tasks")
    print(f"  ids added   : {added}")
    print(f"  already set : {existing}")
    print(f"  all unique  : {len(seen) == total}")

    if args.check:
        print("\n--check given; nothing written.")
        return
    if added:
        args.tasks.write_text(
            json.dumps(tasks, indent=2, ensure_ascii=False) + "\n",
            encoding="utf-8",
            newline="\n",
        )
        print(f"\nWrote {args.tasks}")
    else:
        print("\nNo change needed.")


if __name__ == "__main__":
    main()
