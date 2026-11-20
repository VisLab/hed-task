"""Build the NEMAR task-label inventory (one row per dataset and task label).

Usage: python src/build_nemar_inventory.py <mirror-root> [output.tsv]

The mirror root is the folder holding ``dataset_repos/`` and
``dataset_summaries/repo_contents.json``. It is passed as an argument and never
stored in the repository. The default output is
``.status/scratch/nemar_inventory.tsv``.
"""

import csv
import json
import re
import sys
from pathlib import Path

LABEL_RX = re.compile(r"task-([A-Za-z0-9]+)_")
SENTENCE_RX = re.compile(r"(?<=[.!?])\s+|\n+")
COLUMNS = [
    "dataset_id",
    "task_label",
    "title",
    "modalities",
    "keywords",
    "description",
    "text_sentence",
    "events_levels",
]


def clean(text):
    """Collapse whitespace so a value fits in one TSV cell.

    Parameters:
        text (str): Any string.

    Returns:
        str: The string on one line with single spaces.
    """
    return re.sub(r"\s+", " ", text or "").strip()


def find_labels(entry):
    """Return the sorted task labels found in a repo_contents entry.

    Parameters:
        entry (dict): One value of repo_contents.json.

    Returns:
        list[str]: Distinct labels from the top-level and event file paths.
    """
    found = set()
    for item in entry.get("top_level_files", []) + entry.get("event_files", []):
        found.update(LABEL_RX.findall(item["path"]))
    return sorted(found)


def read_json(path):
    """Read a JSON file, returning an empty dict when it is missing or bad.

    Parameters:
        path (Path): File to read.

    Returns:
        dict: The parsed content, or an empty dict.
    """
    try:
        return json.loads(path.read_text(encoding="utf8"))
    except (OSError, ValueError):
        return {}


def pick_sentence(texts, label):
    """Pick the first sentence that names the label, else one that says task.

    Parameters:
        texts (list[str]): Source texts, in priority order.
        label (str): The task label, or empty.

    Returns:
        str: Up to 300 characters of one sentence, or empty.
    """
    sentences = [s for t in texts for s in SENTENCE_RX.split(t or "")]
    if label:
        low = label.lower()
        for s in sentences:
            if low in s.lower():
                return clean(s)[:300]
    for s in sentences:
        if re.search(r"\btasks?\b", s, re.I):
            return clean(s)[:300]
    return ""


def events_levels(repo_dir, label):
    """Collect the Levels keys of a top-level events sidecar.

    Parameters:
        repo_dir (Path): The dataset repo folder.
        label (str): The task label.

    Returns:
        str: Level names joined by a pipe, at most 400 characters.
    """
    if not label:
        return ""
    sidecar = read_json(repo_dir / f"task-{label}_events.json")
    names = []
    if not isinstance(sidecar, dict):
        return ""
    for field in sidecar.values():
        if isinstance(field, dict) and isinstance(field.get("Levels"), dict):
            names.extend(field["Levels"])
    return "|".join(names)[:400]


def build_rows(root):
    """Build the inventory rows for every dataset in the mirror.

    Parameters:
        root (Path): Mirror root.

    Returns:
        list[dict]: One row per (dataset, label); one row with an empty label
        for a dataset that has none.
    """
    index = root / "dataset_summaries" / "repo_contents.json"
    try:
        contents = json.loads(index.read_text(encoding="utf8"))
    except (OSError, ValueError) as err:
        sys.exit(f"Cannot read the mirror index {index}: {err}")
    if not isinstance(contents, dict) or not contents:
        sys.exit(f"The mirror index {index} is not a non-empty object keyed by dataset id; nothing written.")
    rows = []
    for dataset_id in sorted(contents):
        repo_dir = root / "dataset_repos" / dataset_id
        meta = read_json(repo_dir / ".nemar" / "metadata.json")
        readme = ""
        try:
            readme = (repo_dir / "README.md").read_text(encoding="utf8", errors="replace")
        except OSError:
            pass
        keywords = "|".join(
            clean(k.get("term", "")) if isinstance(k, dict) else clean(str(k)) for k in meta.get("keywords", [])
        )
        for label in find_labels(contents[dataset_id]) or [""]:
            rows.append(
                {
                    "dataset_id": dataset_id,
                    "task_label": label,
                    "title": clean(meta.get("title", "")),
                    "modalities": "|".join(meta.get("modalities", [])),
                    "keywords": keywords,
                    "description": clean(meta.get("description", ""))[:300],
                    "text_sentence": pick_sentence([meta.get("methods_description", ""), readme], label),
                    "events_levels": events_levels(repo_dir, label),
                }
            )
    return rows


def main(argv):
    """Write the inventory TSV and print row and coverage counts.

    Parameters:
        argv (list[str]): Command-line arguments after the program name.
    """
    if not argv:
        sys.exit(__doc__)
    root = Path(argv[0])
    out = Path(argv[1]) if len(argv) > 1 else Path(".status/scratch/nemar_inventory.tsv")
    rows = build_rows(root)
    out.parent.mkdir(parents=True, exist_ok=True)
    with out.open("w", encoding="utf8", newline="") as handle:
        writer = csv.DictWriter(handle, COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(rows)
    print(f"rows {len(rows)}; datasets {len({r['dataset_id'] for r in rows})}")
    print(f"distinct labels {len({r['task_label'] for r in rows if r['task_label']})}")
    for col in COLUMNS[2:]:
        print(f"{col}: {sum(1 for r in rows if r[col])} filled")


if __name__ == "__main__":
    main(sys.argv[1:])
