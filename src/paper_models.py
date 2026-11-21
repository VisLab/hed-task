"""Start and check the task models of papers kept in data/paper_models/.

A paper is modeled by filling in one JSON file: the paper, who coded it, and one entry
for each task the paper runs. An entry describes the task as a game in the terms of
data/task_game_defs.json and data/task_facet_defs.json, with every answer written out
and its basis (`stated` in the paper, `inferred` from it, or `assumed`), and says how
the game relates to a task of the catalog. docs/source/modeling_process.md describes the
steps; data/paper_models/README.md says how to fill the file in.

Two commands:

    python src/paper_models.py new [GAME_TYPE] [--from HEDTSK_ID] [--out FILE]
    python src/paper_models.py check PATH [PATH ...]

`new` prints a blank file with one task entry. With GAME_TYPE the entry lists every rule
question of that game type, answered with its default. With `--from` the answers are
those of the standard form of that catalog task (GAME_TYPE may then be left out). Every
answer written by `new` has the basis `assumed`: nobody has checked it against the paper
yet. A list of objects starts with one blank row that shows its keys; `check` skips a row
left blank. Without either argument the result is data/paper_models/template.json.

`check` validates each file (a directory means its *.json files, template.json
excepted) against data/schemas/paper_task_model.schema.json and against the vocabulary,
and reports how each task differs from the form of the catalog task or variant it
names. Exit status is 1 if any file has a problem, otherwise 0.

Usage is from the repository root, with the venv active.
"""

from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from generators.utils import load_json  # noqa: E402

DATA_DIR = _HERE.parent / "data"
TEMPLATE_VERSION = "0.1"
BASES = ("stated", "inferred", "assumed")
RELATIONS = ("standard_form", "variant", "new_variant", "new_task", "unclear")
PROCESS_SOURCES = ("authors", "catalog", "coder")
# Motivator questions whose answer is a single value; the others take a list.
SINGLE_MOTIVATORS = ("sign", "earned_by")


class Vocabulary:
    """The game vocabulary and the catalog, loaded once.

    Parameters:
        data_dir: The data/ directory.
    """

    def __init__(self, data_dir: Path) -> None:
        games = load_json(data_dir / "task_game_defs.json")
        self.game_types = {g["game_type"]: g for g in games["game_types"]}
        self.rules = {
            g["game_type"]: {r["rule"]: (r["default"], {v["value"] for v in r["values"]}) for r in g["rules"]}
            for g in games["game_types"]
        }
        self.motivators = {m["key"]: {v["value"] for v in m["values"]} for m in games["motivators"]}
        self.phases = {p["phase"] for p in games["phases"]}
        self.settings = {s["setting"] for s in games["settings"]}
        self.how = {c["how"] for c in games["combinations"]}
        facets = load_json(data_dir / "task_facet_defs.json")["facets"]
        self.facets = {f["facet"]: {v["value"] for v in f["values"]} for f in facets}
        self.tasks = {t["hedtsk_id"]: t for t in load_json(data_dir / "task_details.json")}
        self.processes = {p["process_id"] for p in load_json(data_dir / "process_details.json")["processes"]}

    def catalog_form(self, hedtsk_id: str, hedvar_id: str = "") -> dict:
        """Return the full game model of a catalog task, or of one of its variants.

        Rules the record does not state are filled with their defaults, and a variant's
        answers replace those of the standard form, so the result can be compared with
        a paper's model answer by answer.

        Parameters:
            hedtsk_id: The catalog task.
            hedvar_id: One of its variants, or "" for the standard form.
        """
        task = self.tasks[hedtsk_id]
        variant = next((v for v in task.get("variants", []) if v["variant_id"] == hedvar_id), {})
        game_type = task["game_type"]
        rules = {rule: default for rule, (default, _) in self.rules[game_type].items()}
        rules.update(task.get("rules") or {})
        rules.update(variant.get("rules") or {})
        motivators = dict(task.get("motivators") or {})
        motivators.update(variant.get("motivators") or {})
        facets = dict(task.get("task_facets") or {})
        facets.update(variant.get("task_facets") or {})
        return {
            "game_type": game_type,
            "rules": rules,
            "motivators": motivators,
            "phases": variant.get("phases") or task.get("phases") or [],
            "task_facets": {f: v for f, v in facets.items() if v},
            "settings": task.get("settings") or [],
            "material": task.get("material") or "",
            "combined_with": variant.get("combined_with") or task.get("combined_with") or [],
        }


def _answer(value, basis: str = "") -> dict:
    """Return one answer of a paper model: a value, its basis and its evidence."""
    return {"value": value, "basis": basis, "evidence": ""}


def new_model(vocab: Vocabulary, game_type: str = "", hedtsk_id: str = "") -> dict:
    """Return a blank paper model with one task entry.

    Parameters:
        vocab: The vocabulary and catalog.
        game_type: The game type of the entry, or "" for the generic template.
        hedtsk_id: A catalog task whose standard form fills in the answers, or "".
    """
    form = vocab.catalog_form(hedtsk_id) if hedtsk_id else None
    if form:
        game_type = form["game_type"]
    basis = "assumed" if game_type else ""
    rules = form["rules"] if form else {r: d for r, (d, _) in vocab.rules.get(game_type, {}).items()}
    motivators = form["motivators"] if form else {}
    facets = form["task_facets"] if form else {}
    entry = {
        "task_label": "",
        "experiment": "",
        "summary": "",
        "game_type": _answer(game_type, basis),
        "rules": {rule: _answer(value, "assumed") for rule, value in rules.items()},
        "motivators": {
            key: _answer(
                motivators.get(key, "" if key in SINGLE_MOTIVATORS else []),
                "assumed" if key in motivators else "",
            )
            for key in vocab.motivators
        },
        "phases": _answer(list(form["phases"]) if form else [], "assumed" if form else ""),
        "task_facets": {f: _answer(list(facets.get(f, [])), "assumed" if f in facets else "") for f in vocab.facets},
        "settings": [{"setting": s, "value": "", "unit": "", "evidence": ""} for s in (form["settings"] if form else [])]
        or [{"setting": "", "value": "", "unit": "", "evidence": ""}],
        "material": "",
        "combined_with": [dict(c) for c in (form["combined_with"] if form else [])]
        or [{"game_type": "", "task": "", "how": "", "note": ""}],
        "procedure": [],
        "manipulations": [],
        "measurements": [],
        "catalog_match": {"relation": "", "hedtsk_id": hedtsk_id, "hedvar_id": "", "note": ""},
        "processes": [{"process_id": "", "source": "", "evidence": ""}],
        "participants": {"n": None, "description": ""},
        "recording": [],
        "not_in_vocabulary": [{"part": "", "proposed": "", "description": "", "evidence": ""}],
        "notes": "",
    }
    return {
        "template_version": TEMPLATE_VERSION,
        "paper": {"citation": "", "doi": "", "pmid": "", "url": "", "datasets": [{"repository": "", "id": "", "url": ""}]},
        "coding": {"coded_by": "", "coded_on": "", "sources_read": [], "status": "draft"},
        "tasks": [entry],
    }


def _as_set(value) -> set[str]:
    """Return an answer's value as a set, whether it is one value, a list or empty."""
    if isinstance(value, list):
        return set(value)
    return {value} if value else set()


def _check_answer(label: str, answer: dict, allowed: set[str], problems: list[str], notes: list[str]) -> None:
    """Check one answer's values against the vocabulary, and its basis and evidence."""
    for v in sorted(_as_set(answer["value"]) - allowed):
        problems.append(f"{label}: {v!r} is not in the vocabulary")
    if _as_set(answer["value"]) and not answer["basis"]:
        problems.append(f"{label}: an answer is given without a basis")
    if answer["basis"] == "stated" and not answer["evidence"].strip():
        notes.append(f"{label}: basis is `stated` but no evidence is given")


def _differences(entry: dict, form: dict) -> list[str]:
    """Return the parts on which a paper's task differs from a catalog form.

    Parameters:
        entry: One task entry of a paper model.
        form: The catalog form from `Vocabulary.catalog_form`.
    """
    out = []
    if entry["game_type"]["value"] != form["game_type"]:
        return [f"game_type: {entry['game_type']['value']!r}, catalog {form['game_type']!r}"]
    for rule, answer in entry["rules"].items():
        if rule in form["rules"] and answer["value"] != form["rules"][rule]:
            out.append(f"rule {rule}: {answer['value']!r}, catalog {form['rules'][rule]!r}")
    for key, answer in entry["motivators"].items():
        ours, theirs = _as_set(answer["value"]), _as_set(form["motivators"].get(key))
        if ours != theirs:
            out.append(f"motivator {key}: {sorted(ours)}, catalog {sorted(theirs)}")
    if entry["phases"]["value"] != list(form["phases"]):
        out.append(f"phases: {entry['phases']['value']}, catalog {list(form['phases'])}")
    for facet, answer in entry["task_facets"].items():
        ours, theirs = _as_set(answer["value"]), _as_set(form["task_facets"].get(facet))
        if ours != theirs:
            out.append(f"facet {facet}: {sorted(ours)}, catalog {sorted(theirs)}")
    ours = {(c.get("task") or c.get("game_type"), c.get("how")) for c in entry["combined_with"] if any(c.values())}
    theirs = {(c.get("task") or c.get("game_type"), c.get("how")) for c in form["combined_with"]}
    if ours != theirs:
        out.append(f"combined_with: {sorted(ours)}, catalog {sorted(theirs)}")
    return out


def check_entry(vocab: Vocabulary, entry: dict, label: str) -> tuple[list[str], list[str]]:
    """Check one task entry of a paper model.

    Parameters:
        vocab: The vocabulary and catalog.
        entry: The task entry.
        label: What to call the entry in messages.

    Returns:
        (problems, notes). A problem makes the file invalid; a note is for the coder.
    """
    problems: list[str] = []
    notes: list[str] = []
    game_type = entry["game_type"]["value"]
    if game_type not in vocab.game_types:
        return [f"{label}: game_type {game_type!r} is not in the vocabulary"], notes
    _check_answer(f"{label}: game_type", entry["game_type"], set(vocab.game_types), problems, notes)

    rules = vocab.rules[game_type]
    for rule in sorted(set(rules) - set(entry["rules"])):
        problems.append(f"{label}: rule {rule} of {game_type} is not answered")
    for rule, answer in entry["rules"].items():
        if rule not in rules:
            problems.append(f"{label}: {rule!r} is not a rule of {game_type}")
            continue
        if not answer["value"]:
            problems.append(f"{label}: rule {rule} has no answer")
        _check_answer(f"{label}: rule {rule}", answer, rules[rule][1], problems, notes)

    for key, answer in entry["motivators"].items():
        if key not in vocab.motivators:
            problems.append(f"{label}: {key!r} is not a motivator question")
            continue
        _check_answer(f"{label}: motivator {key}", answer, vocab.motivators[key], problems, notes)
    if not _as_set(entry["motivators"].get("drive", {}).get("value")):
        problems.append(f"{label}: motivator drive is not answered")

    _check_answer(f"{label}: phases", entry["phases"], vocab.phases, problems, notes)
    for facet, answer in entry["task_facets"].items():
        if facet not in vocab.facets:
            problems.append(f"{label}: {facet!r} is not a facet")
            continue
        _check_answer(f"{label}: facet {facet}", answer, vocab.facets[facet], problems, notes)

    for s in entry["settings"]:
        if s["setting"] and s["setting"] not in vocab.settings:
            notes.append(f"{label}: setting {s['setting']!r} is not in the vocabulary; list it under not_in_vocabulary")
    for c in entry["combined_with"]:
        if not any(c.values()):
            continue  # a blank row left from the template
        if c["how"] not in vocab.how:
            problems.append(f"{label}: combined_with how {c['how']!r} is not in the vocabulary")
        if c.get("task") and c["task"] not in vocab.tasks:
            problems.append(f"{label}: combined_with task {c['task']!r} is not in the catalog")
        if c.get("game_type") and c["game_type"] not in vocab.game_types:
            problems.append(f"{label}: combined_with game_type {c['game_type']!r} is not in the vocabulary")
    for p in entry["processes"]:
        if p["process_id"] and p["process_id"] not in vocab.processes:
            problems.append(f"{label}: process {p['process_id']!r} is not in the catalog")

    answers = [entry["game_type"], entry["phases"], *entry["rules"].values()]
    answers += [*entry["motivators"].values(), *entry["task_facets"].values()]
    assumed = sum(1 for a in answers if a["basis"] == "assumed")
    if assumed:
        notes.append(f"{label}: {assumed} answers are still `assumed`")

    match = entry["catalog_match"]
    if not match["relation"]:
        notes.append(f"{label}: catalog_match relation is not filled in")
    if match["hedtsk_id"]:
        task = vocab.tasks.get(match["hedtsk_id"])
        if task is None:
            problems.append(f"{label}: catalog task {match['hedtsk_id']!r} is not in the catalog")
        elif match["hedvar_id"] and match["hedvar_id"] not in {v["variant_id"] for v in task.get("variants", [])}:
            problems.append(f"{label}: {match['hedvar_id']!r} is not a variant of {match['hedtsk_id']}")
        else:
            diffs = _differences(entry, vocab.catalog_form(match["hedtsk_id"], match["hedvar_id"]))
            against = match["hedvar_id"] or f"the standard form of {match['hedtsk_id']}"
            notes.append(f"{label}: {len(diffs)} differences from {against}")
            notes.extend(f"{label}:   {d}" for d in diffs)
            if diffs and match["relation"] in ("standard_form", "variant"):
                notes.append(f"{label}: relation is {match['relation']!r} but the model differs; see the lines above")
    elif match["relation"] in ("standard_form", "variant", "new_variant"):
        problems.append(f"{label}: relation {match['relation']!r} needs a hedtsk_id")
    return problems, notes


def check_file(vocab: Vocabulary, path: Path, schema: dict) -> tuple[list[str], list[str]]:
    """Check one paper model file against the schema and the vocabulary."""
    import jsonschema

    try:
        model = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as err:
        return [f"not valid JSON: {err}"], []
    errors = sorted(jsonschema.Draft7Validator(schema).iter_errors(model), key=lambda e: list(e.path))
    if errors:
        return [f"schema, at {'/'.join(str(p) for p in e.path) or '(root)'}: {e.message[:200]}" for e in errors], []
    problems: list[str] = []
    notes: list[str] = []
    for n, entry in enumerate(model["tasks"], 1):
        p, m = check_entry(vocab, entry, entry["task_label"] or f"task {n}")
        problems += p
        notes += m
    return problems, notes


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = parser.add_subparsers(dest="command", required=True)
    new = sub.add_parser("new", help="print a blank paper model")
    new.add_argument("game_type", nargs="?", default="", help="game type of the task entry")
    new.add_argument("--from", dest="hedtsk_id", default="", help="catalog task whose standard form fills in the answers")
    new.add_argument("--out", type=Path, help="write to this file instead of standard output")
    check = sub.add_parser("check", help="check paper model files")
    check.add_argument("paths", nargs="+", type=Path, help="files, or directories of *.json files")
    args = parser.parse_args()
    vocab = Vocabulary(DATA_DIR)

    if args.command == "new":
        if args.game_type and args.game_type not in vocab.game_types:
            sys.exit(f"unknown game type {args.game_type!r}; one of: {', '.join(vocab.game_types)}")
        if args.hedtsk_id and args.hedtsk_id not in vocab.tasks:
            sys.exit(f"unknown catalog task {args.hedtsk_id!r}")
        text = json.dumps(new_model(vocab, args.game_type, args.hedtsk_id), indent=2) + "\n"
        if args.out:
            args.out.write_text(text, encoding="utf-8", newline="\n")
        else:
            sys.stdout.write(text)
        return

    schema = load_json(DATA_DIR / "schemas" / "paper_task_model.schema.json")
    files = []
    for path in args.paths:
        files += sorted(p for p in path.glob("*.json") if p.name != "template.json") if path.is_dir() else [path]
    failed = 0
    for path in files:
        problems, notes = check_file(vocab, path, schema)
        failed += bool(problems)
        print(f"{path}: {len(problems)} problems, {len(notes)} notes")
        for line in problems:
            print(f"  PROBLEM {line}")
        for line in notes:
            print(f"  note    {line}")
    print(f"{len(files)} files checked, {failed} with problems")
    sys.exit(1 if failed else 0)


if __name__ == "__main__":
    main()
