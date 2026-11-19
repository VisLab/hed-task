"""Normalize NEMAR task labels and match them to the Catalog (automatic first pass).

Usage: python src/match_nemar_tasks.py [inventory.tsv] [output.tsv]

Reads the inventory written by ``build_nemar_inventory.py`` and
``data/task_details.json``. Writes ``data/mappings/nemar_task_to_hed.tsv`` with every
automatic hit at confidence ``review`` and everything else ``unresolved``. The hand
passes (``differs``, ``proposal``, final match types) are not done here.
"""

import csv
import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

NOISE = {
    "run", "stim", "task", "unnamed", "visual", "control", "loc", "localizer", "block",
    "trial", "session", "ses", "t1", "t2", "test", "train", "day", "sub", "recording",
}  # fmt: skip
KEEP_DIGITS = re.compile(r"^[pnc]\d{2,3}$")
COLUMNS = [
    "dataset_id", "task_label", "match_type", "hedtsk_id", "hed_task_name",
    "hed_variant_id", "hed_variant_name", "differs", "proposal", "confidence",
    "evidence", "notes",
]  # fmt: skip
MAX_ROWS_PER_TERM = 60  # a term matching more rows than this by substring is generic


def words(text):
    """Split text into lowercase words, breaking camel case and digit runs.

    Parameters:
        text (str): A label, title or keyword.

    Returns:
        list[str]: Lowercase words.
    """
    text = re.sub(r"([a-z])([A-Z])", r"\1 \2", text)
    text = re.sub(r"([A-Z]+)([A-Z][a-z])", r"\1 \2", text)
    return re.findall(r"[a-z]+|\d+", text.lower())


def normalize_label(label):
    """Normalize a BIDS task label.

    Run, session and stimulus numbers are dropped (``interictal1234`` becomes
    ``interictal``); ``p300``-style names keep their digits.

    Parameters:
        label (str): The label as it appears in file names.

    Returns:
        str: A lowercase, space-joined label, or empty when the label is a known
        noise label, only digits, or empty.
    """
    parts = words(label or "")
    if not parts or all(p.isdigit() for p in parts):
        return ""
    if KEEP_DIGITS.match("".join(parts)):
        return "".join(parts)
    else:
        parts = [p for p in parts if not p.isdigit()] or parts
    joined = " ".join(parts)
    return "" if joined in NOISE else joined


def compact(text):
    """Return only the lowercase letters and digits of text.

    Parameters:
        text (str): Any string.

    Returns:
        str: The compact form used for label comparison.
    """
    return re.sub(r"[^a-z0-9]", "", text.lower())


def load_terms(catalog):
    """Collect matching terms from the Catalog.

    Parameters:
        catalog (list[dict]): Parsed task_details.json.

    Returns:
        tuple: (task_terms, variant_terms), each a list of dicts with keys term,
        kind, hedtsk_id, task_name, variant_id, variant_name.
    """
    task_terms, variant_terms = [], []
    for task in catalog:
        names = [(task["canonical_name"], "canonical_name")]
        names += [(a, "alias") for a in task.get("aliases", [])]
        for name, kind in list(names):
            stripped = re.sub(r"\s+tasks?$", "", name, flags=re.I)
            if stripped != name:
                names.append((stripped, kind))
        for name, kind in names:
            task_terms.append(
                {"term": name, "kind": kind, "hedtsk_id": task["hedtsk_id"],
                 "task_name": task["canonical_name"], "variant_id": "", "variant_name": ""}
            )  # fmt: skip
        for var in task.get("variants", []):
            variant_terms.append(
                {"term": var["name"], "kind": "variant", "hedtsk_id": task["hedtsk_id"],
                 "task_name": task["canonical_name"], "variant_id": var["variant_id"],
                 "variant_name": var["name"]}
            )  # fmt: skip
    return task_terms, variant_terms


def label_hit(label_compact, term):
    """Test a compact label against a term.

    Parameters:
        label_compact (str): Compact normalized label.
        term (dict): A term record from load_terms.

    Returns:
        str: "exact", "substring" or empty. Terms of three characters or fewer
        match only as the whole label.
    """
    tc = compact(term["term"])
    if not tc or not label_compact:
        return ""
    if label_compact == tc:
        return "exact"
    if len(tc) > 3 and tc in label_compact:
        return "substring"
    return ""


def text_hit(text_words, term):
    """Test a word string (title or one keyword) for a term as whole words.

    Parameters:
        text_words (str): Space-joined lowercase words.
        term (dict): A term record from load_terms.

    Returns:
        bool: True when the term's words occur contiguously. Terms of three
        characters or fewer must equal the whole text.
    """
    tw = " ".join(words(term["term"]))
    if len(compact(tw)) <= 3:
        return text_words == tw
    return f" {tw} " in f" {text_words} "


def find_generic(terms, labels):
    """Find terms that match too many rows as a substring of the label.

    Parameters:
        terms (list[dict]): Term records.
        labels (list[str]): Compact normalized label of every row.

    Returns:
        dict: term string -> number of rows it matches, for generic terms only.
    """
    generic = {}
    for term in terms:
        n = sum(1 for lab in labels if label_hit(lab, term) == "substring")
        if n > MAX_ROWS_PER_TERM:
            generic[term["term"]] = n
    return generic


def match_row(row, n_labels, norm, term_sets, generic):
    """Match one inventory row to a task, then (if no task) to a variant.

    Title and keyword text is used only when the dataset has at most one label
    or the label is noise, because a title describes the whole dataset.

    Parameters:
        row (dict): An inventory row.
        n_labels (int): Number of labels the dataset has.
        norm (str): The normalized label.
        term_sets (list[tuple]): (match_type, terms) in priority order.
        generic (set[str]): Terms excluded as generic.

    Returns:
        dict | None: match_type, term, evidence and notes, or None.
    """
    lab = compact(norm)
    texts = []
    if n_labels <= 1 or not norm:
        texts.append(("title", " ".join(words(row["title"]))))
        for kw in row["keywords"].split("|"):
            texts.append(("keywords", " ".join(words(kw))))
    for match_type, terms in term_sets:
        hits = []
        for term in terms:
            if term["term"] in generic:
                continue
            size = -len(compact(term["term"]))
            kind = label_hit(lab, term)
            if kind:
                hits.append((0 if kind == "exact" else 1, size, term, "label"))
                continue
            for source, text in texts:
                if text and text_hit(text, term):
                    hits.append((2 if source == "title" else 3, size, term, source))
        if hits:
            hits.sort(key=lambda h: (h[0], h[1], h[2]["hedtsk_id"], h[2]["term"]))
            _, _, term, source = hits[0]
            others = sorted({h[2]["hedtsk_id"] for h in hits} - {term["hedtsk_id"]})
            note = f"auto: {source} matched {term['kind']} '{term['term']}'"
            if others:
                note += "; also " + ", ".join(others[:4])
            return {"match_type": match_type, "term": term, "evidence": source, "notes": note}
    return None


def ascii_cell(value, counter):
    """Replace non-ASCII characters in a cell and count the cells changed.

    Parameters:
        value (str): Cell text.
        counter (list[int]): One-element list incremented per changed cell.

    Returns:
        str: ASCII text.
    """
    if value.isascii():
        return value
    counter[0] += 1
    return value.encode("ascii", "ignore").decode()


def main(argv):
    """Run the normalization and automatic pass and write the mapping table.

    Parameters:
        argv (list[str]): Optional inventory path and output path.
    """
    inv_path = Path(argv[0]) if argv else Path(".status/scratch/nemar_inventory.tsv")
    out_path = Path(argv[1]) if len(argv) > 1 else Path("data/mappings/nemar_task_to_hed.tsv")
    catalog = json.loads(Path("data/task_details.json").read_text(encoding="utf8"))
    task_terms, variant_terms = load_terms(catalog)
    with inv_path.open(encoding="utf8", newline="") as handle:
        rows = list(csv.DictReader(handle, delimiter="\t"))
    per_dataset = Counter(r["dataset_id"] for r in rows if r["task_label"])
    labels = [compact(normalize_label(r["task_label"])) for r in rows]
    generic_t = find_generic(task_terms, labels)
    generic_v = find_generic(variant_terms, labels)
    generic = set(generic_t) | set(generic_v)
    term_sets = [("task", task_terms), ("variant", variant_terms)]
    changed = [0]
    out_rows = []
    by_norm = defaultdict(set)
    for row in rows:
        norm = normalize_label(row["task_label"])
        if norm:
            by_norm[norm].add(row["dataset_id"])
        hit = match_row(row, per_dataset[row["dataset_id"]], norm, term_sets, generic)
        base = dict.fromkeys(COLUMNS, "")
        base.update(dataset_id=row["dataset_id"], task_label=row["task_label"])
        if hit:
            t = hit["term"]
            base.update(
                match_type=hit["match_type"], hedtsk_id=t["hedtsk_id"], hed_task_name=t["task_name"],
                hed_variant_id=t["variant_id"], hed_variant_name=t["variant_name"],
                confidence="review", evidence=hit["evidence"], notes=hit["notes"],
            )  # fmt: skip
        else:
            why = "" if norm else "; noise, numeric or empty label"
            base.update(match_type="unresolved", notes="auto: no match" + why)
        out_rows.append({k: ascii_cell(v, changed) for k, v in base.items()})
    out_rows.sort(key=lambda r: (r["dataset_id"], r["task_label"]))
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with out_path.open("w", encoding="utf8", newline="") as handle:
        writer = csv.DictWriter(handle, COLUMNS, delimiter="\t", lineterminator="\n")
        writer.writeheader()
        writer.writerows(out_rows)
    raw = {r["task_label"] for r in rows if r["task_label"]}
    noise = sum(1 for r in rows if r["task_label"] and not normalize_label(r["task_label"]))
    print(f"raw labels {len(raw)} -> normalized {len(by_norm)}; noise rows {noise}")
    print("largest clusters (datasets):", Counter({k: len(v) for k, v in by_norm.items()}).most_common(20))
    print("generic terms excluded (task):", generic_t)
    print("generic terms excluded (variant):", generic_v)
    print("rows by match_type:", Counter(r["match_type"] for r in out_rows))
    print("non-ASCII cells changed:", changed[0])


if __name__ == "__main__":
    main(sys.argv[1:])
