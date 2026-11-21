"""CLI entry point: validate the catalog in data/ and generate the catalog pages.

Inputs, all under data/ and all edited in this repository by pull request:

    task_details.json        the tasks (top level is a bare array)
    process_details.json     the processes and their categories
    mappings/*.tsv           the curated correspondence with the Cognitive Atlas
    task_family_defs.tsv     the task families (membership is on each task record)
    task_facet_defs.json     the facet vocabulary
    task_game_defs.json      game types, rules, motivators, phases, settings, combinations
    vocabulary_candidates.json  the register of candidate vocabulary
    schemas/*.schema.json    JSON Schemas for the catalog and vocabulary files

Two kinds of page live under docs/source/. This script writes only the catalog pages,
which are tabular views of the data:

    tasks/**                     task index, family pages, alphabetical list, task pages,
                                 the vocabulary page and the by-game-type and by-facet
                                 listings
    processes/**                 process index, category pages
    task_process_links.md        task-process links
    _generated/*.md              table fragments that narrative pages include, among
                                 them the full Atlas mapping tables

Those paths are deleted and rewritten on every run, so a page dropped from the
generators cannot linger. Every other file under docs/source/ - the landing page, the
overview pages, the Atlas essays, the Methods documents, conf.py, _static/, _templates/ -
is hand-maintained and is never touched here.

Nothing is written until the whole catalog validates: schema shape, unique identifiers,
every cross-reference resolving, derived fields agreeing with their sources, reference
roles from the allowed vocabulary, and every task filed under a family. A failure names
the record, so a pull request that edits the data gets a precise message from CI.

Usage (from repo root, with venv active):
    python src/generate_docs.py [--docs-dir DIR]

`--docs-dir` writes into another Sphinx source directory (a copy of docs/source) instead
of the repository's, for trying a change without touching the committed pages.
"""

from __future__ import annotations

import argparse
import collections
import shutil
import sys
from pathlib import Path

# Ensure the src/ directory is on the Python path so `generators` can be imported.
_HERE = Path(__file__).parent
if str(_HERE) not in sys.path:
    sys.path.insert(0, str(_HERE))

from generators import (  # noqa: E402
    crossref_atlas_pages,
    crossref_cogpo_pages,
    crossref_page,
    fragments,
    process_pages,
    task_pages,
    vocabulary_pages,
)
from generators.utils import load_json, primary_category, primary_family, read_tsv  # noqa: E402

# Everything the generator owns, relative to docs/source/. Nothing outside this list is
# ever deleted or written.
GENERATED_PATHS = [
    "tasks",
    "processes",
    "task_process_links.md",
    "_generated",
]

_VALID_CONFIDENCE = {"high", "review"}


# ---------------------------------------------------------------------------
# Validation
# ---------------------------------------------------------------------------


def _schema_check(instance, schema_path: Path, label: str, problems: list[str]) -> dict:
    """Validate `instance` against a JSON Schema; return the loaded schema."""
    try:
        import jsonschema
    except ImportError:
        sys.exit('jsonschema is not installed; run: pip install -e ".[docs]"')
    schema = load_json(schema_path)
    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(instance), key=lambda e: list(e.path)):
        where = "/".join(str(p) for p in err.path) or "(root)"
        problems.append(f"{label} at {where}: {err.message[:200]}")
    return schema


def _reference_roles(schema: dict) -> set[str]:
    """The allowed `roles` values, read from the schema so they are defined once."""
    role_def = schema.get("definitions", {}).get("reference_role", {})
    return set(role_def.get("enum", []))


def _check_memberships(records: list[dict], field: str, id_key: str, known: set[str], ident: str, problems: list[str]) -> None:
    """Check a record's family or category memberships (issue 28).

    Exactly one primary, no repeated ids, every id known, confidence in the vocabulary, a
    rationale on every secondary and on every review entry. The JSON Schema checks the
    shape of one membership; these rules span the list, so they live here.

    Parameters:
        records: Task or process records.
        field: "families" or "categories".
        id_key: "family_id" or "category_id".
        known: The vocabulary of ids.
        ident: The record's identifier field, for messages.
        problems: The list to append messages to.
    """
    for r in records:
        members = r.get(field, [])
        label = f"{r[ident]}: {field}"
        primaries = [m for m in members if m.get("role") == "primary"]
        if len(primaries) != 1:
            problems.append(f"{label} has {len(primaries)} primary memberships; exactly one is required")
        ids = [m.get(id_key) for m in members]
        for value, n in collections.Counter(ids).items():
            if n > 1:
                problems.append(f"{label} lists {value!r} {n} times")
        for m in members:
            if m.get(id_key) not in known:
                problems.append(f"{label} names unknown {id_key} {m.get(id_key)!r}")
            if m.get("confidence", "high") not in _VALID_CONFIDENCE:
                problems.append(f"{label} {m.get(id_key)}: confidence {m.get('confidence')!r}, expected high or review")
            needs_rationale = m.get("role") == "secondary" or m.get("confidence") == "review"
            if needs_rationale and not m.get("rationale"):
                problems.append(f"{label} {m.get(id_key)}: a secondary or review membership needs a rationale")


# Reference fields that hold author names and published titles. A letter outside ASCII
# (Jolicoeur written with its ligature, a German umlaut) is genuine data there and stays;
# everywhere else, and for every symbol, the data is ASCII only.
_REFERENCE_TEXT_FIELDS = {"authors", "title", "journal", "venue", "pages", "citation_string"}


def _check_ascii(label: str, value, problems: list[str], path: str = "", in_reference: bool = False) -> None:
    """Report every non-ASCII character in a JSON value, except letters in reference text.

    Parameters:
        label: The file name, for messages.
        value: A JSON value (dict, list, string or scalar).
        problems: The list to append messages to.
        path: Where `value` sits in the file, for messages.
        in_reference: True inside a reference record.
    """
    if isinstance(value, dict):
        for key, item in value.items():
            allowed = in_reference and key in _REFERENCE_TEXT_FIELDS
            _check_ascii(label, item, problems, f"{path}/{key}", allowed or (key == "references"))
    elif isinstance(value, list):
        for i, item in enumerate(value):
            _check_ascii(label, item, problems, f"{path}/{i}", in_reference)
    elif isinstance(value, str):
        bad = sorted({c for c in value if ord(c) > 127 and not (in_reference and c.isalpha())})
        if bad:
            chars = ", ".join(f"U+{ord(c):04X}" for c in bad)
            problems.append(f"{label} at {path}: non-ASCII {chars} in {value[:80]!r}")


# ---------------------------------------------------------------------------
# Vocabulary: facets, games, and the candidate register
# ---------------------------------------------------------------------------

_VOCABULARY_FILES = ("task_facet_defs", "task_game_defs", "vocabulary_candidates")


def load_vocabularies(data_dir: Path, problems: list[str]) -> dict:
    """Load the three vocabulary files, each validated against its schema.

    Parameters:
        data_dir: The data/ directory.
        problems: The list to append messages to.

    Returns:
        A dict of lookup tables: `facets` (facet -> set of values), `game_types` (game type
        -> {rule -> (default, set of values)}), `motivators` (question -> set of values),
        `required_motivators` (questions a task must answer), `phases`, `settings`, `how`
        and `candidates` (sets of names).
    """
    raw = {}
    for name in _VOCABULARY_FILES:
        raw[name] = load_json(data_dir / f"{name}.json")
        _schema_check(raw[name], data_dir / "schemas" / f"{name}.schema.json", f"{name}.json", problems)
        _check_ascii(f"{name}.json", raw[name], problems)

    facets = {f["facet"]: {v["value"] for v in f["values"]} for f in raw["task_facet_defs"]["facets"]}
    games = raw["task_game_defs"]
    game_types: dict[str, dict[str, tuple[str, set[str]]]] = {}
    for g in games["game_types"]:
        rules = {}
        for r in g.get("rules", []):
            values = {v["value"] for v in r["values"]}
            if r["default"] not in values:
                problems.append(
                    f"task_game_defs.json: rule {g['game_type']}.{r['rule']} default {r['default']!r} is not one of its values"
                )
            rules[r["rule"]] = (r["default"], values)
        game_types[g["game_type"]] = rules
    vocab = {
        "facets": facets,
        "game_types": game_types,
        "motivators": {m["key"]: {v["value"] for v in m["values"]} for m in games["motivators"]},
        "required_motivators": {m["key"] for m in games["motivators"] if m.get("required")},
        "phases": {p["phase"] for p in games["phases"]},
        "settings": {s["setting"] for s in games["settings"]},
        "how": {c["how"] for c in games["combinations"]},
        "candidates": {c["candidate_id"] for c in raw["vocabulary_candidates"]["candidates"]},
    }
    for label, items, key in (
        ("facet", raw["task_facet_defs"]["facets"], "facet"),
        ("game type", games["game_types"], "game_type"),
        ("candidate", raw["vocabulary_candidates"]["candidates"], "candidate_id"),
    ):
        for value, n in collections.Counter(i[key] for i in items).items():
            if n > 1:
                problems.append(f"vocabulary: {label} {value!r} appears {n} times")
    return vocab


def _check_game_layer(
    label: str, rec: dict, game_type: str | None, vocab: dict, ctx: dict, problems: list[str], standard: dict | None = None
) -> None:
    """Check the game-model keys that a task and a variant share.

    Parameters:
        label: The record's name in messages (task id, or task id and variant id).
        rec: The task or variant record.
        game_type: The task's game type; None when it is missing or unknown, in which case
            the rules are not checked.
        vocab: The tables from `load_vocabularies`.
        ctx: `task_ids` and `process_ids`, the known identifiers.
        problems: The list to append messages to.
        standard: For a variant, the standard form (the task record). A task may not state a
            rule with its default; a variant may (to undo a standard-form answer), but may
            not repeat the standard form's answer. A variant may not repeat the standard
            form's list for a facet or its answer to a motivator question, and may give an
            empty facet list only for a facet the standard form carries (the facet does not
            apply to this form).
    """
    std_facets = (standard or {}).get("task_facets") or {}
    std_motivators = (standard or {}).get("motivators") or {}
    for facet, values in (rec.get("task_facets") or {}).items():
        if facet not in vocab["facets"]:
            problems.append(f"{label}: task_facets names unknown facet {facet!r}")
            continue
        for v in values:
            if v not in vocab["facets"][facet]:
                problems.append(f"{label}: task_facets {facet} has unknown value {v!r}")
        if standard is not None:
            if not values and facet not in std_facets:
                problems.append(
                    f"{label}: task_facets {facet} is empty, but the standard form does not carry the facet; leave it out"
                )
            elif values and facet in std_facets and set(values) == set(std_facets[facet]):
                problems.append(f"{label}: task_facets {facet} repeats the standard form's list {values}; leave it out")

    std_rules = (standard or {}).get("rules") or {}
    rules = rec.get("rules") or {}
    if rules and game_type is not None:
        known_rules = vocab["game_types"][game_type]
        if not known_rules:
            problems.append(f"{label}: game type {game_type!r} has no rules, but the record states {sorted(rules)}")
        else:
            for rule, value in rules.items():
                if rule not in known_rules:
                    problems.append(f"{label}: rule {rule!r} does not belong to game type {game_type!r}")
                    continue
                default, values = known_rules[rule]
                if value not in values:
                    problems.append(f"{label}: rule {rule} has unknown value {value!r}")
                elif standard is None and value == default:
                    problems.append(f"{label}: rule {rule} is stated with its default {value!r}; leave it out")
                elif standard is not None and value == std_rules.get(rule, default):
                    problems.append(f"{label}: rule {rule} repeats the standard form's answer {value!r}; leave it out")

    for question, answer in (rec.get("motivators") or {}).items():
        if question not in vocab["motivators"]:
            problems.append(f"{label}: motivators names unknown question {question!r}")
            continue
        for v in answer if isinstance(answer, list) else [answer]:
            if v not in vocab["motivators"][question]:
                problems.append(f"{label}: motivators {question} has unknown value {v!r}")
        if question in std_motivators and set(answer if isinstance(answer, list) else [answer]) == set(
            std_motivators[question] if isinstance(std_motivators[question], list) else [std_motivators[question]]
        ):
            problems.append(f"{label}: motivators {question} repeats the standard form's answer {answer!r}; leave it out")

    for phase in rec.get("phases") or []:
        if phase not in vocab["phases"]:
            problems.append(f"{label}: unknown phase {phase!r}")
    for setting in rec.get("settings") or []:
        if setting not in vocab["settings"]:
            problems.append(f"{label}: unknown setting {setting!r}")
    for i, c in enumerate(rec.get("combined_with") or []):
        if c.get("how") not in vocab["how"]:
            problems.append(f"{label}: combined_with {i} has unknown how {c.get('how')!r}")
        if "game_type" in c and c["game_type"] not in vocab["game_types"]:
            problems.append(f"{label}: combined_with {i} names unknown game type {c['game_type']!r}")
        if "task" in c and c["task"] not in ctx["task_ids"]:
            problems.append(f"{label}: combined_with {i} names unknown task {c['task']!r}")
    for cand in rec.get("candidates") or []:
        if cand not in vocab["candidates"]:
            problems.append(f"{label}: candidate {cand!r} is not in vocabulary_candidates.json")


def check_game_records(tasks: list[dict], vocab: dict, process_ids: set[str], problems: list[str]) -> dict[str, list[str]]:
    """Check the game-model keys of every task and of its variants.

    Every task must state `game_type`, `motivators` (with every required question) and
    `task_facets`. The JSON Schema requires the three keys too; the checks here give a
    message per task.

    Parameters:
        tasks: The task records.
        vocab: The tables from `load_vocabularies`.
        process_ids: The known process ids.
        problems: The list to append messages to.

    Returns:
        Candidate id -> the tasks (standard form or a variant) that cite it, for every
        candidate cited by two or more tasks. This is a report, not a failure.
    """
    ctx = {"task_ids": {t["hedtsk_id"] for t in tasks}, "process_ids": process_ids}
    seen_variant_ids: set[str] = set()
    cited_by: dict[str, set[str]] = collections.defaultdict(set)
    for t in tasks:
        tid = t["hedtsk_id"]
        game_type = t.get("game_type")
        if game_type is None:
            problems.append(f"{tid}: game_type is missing")
        elif game_type not in vocab["game_types"]:
            problems.append(f"{tid}: unknown game type {game_type!r}")
            game_type = None
        motivators = t.get("motivators")
        if motivators is None:
            problems.append(f"{tid}: motivators is missing")
        else:
            for question in sorted(vocab["required_motivators"] - set(motivators)):
                problems.append(f"{tid}: motivators {question} is missing")
        if "task_facets" not in t:
            problems.append(f"{tid}: task_facets is missing")
        _check_game_layer(tid, t, game_type, vocab, ctx, problems)
        for cand in t.get("candidates") or []:
            cited_by[cand].add(tid)

        slug_prefix = "hedvar_" + tid.removeprefix("hedtsk_") + "__"
        for v in t.get("variants") or []:
            vid = v.get("variant_id", "")
            label = f"{tid}: variant {vid or v.get('name')!r}"
            rest = vid.removeprefix(slug_prefix)
            if not vid.startswith(slug_prefix) or not rest or not all(c.islower() or c.isdigit() or c == "_" for c in rest):
                problems.append(f"{label}: variant_id must be {slug_prefix}<slug> (lowercase letters, digits, underscores)")
            if vid in seen_variant_ids:
                problems.append(f"{label}: duplicate variant_id")
            seen_variant_ids.add(vid)
            _check_game_layer(label, v, game_type, vocab, ctx, problems, standard=t)
            for pid in v.get("hed_process_ids") or []:
                if pid not in process_ids:
                    problems.append(f"{label}: hed_process_ids names unknown process {pid!r}")
                elif pid in (t.get("hed_process_ids") or []):
                    problems.append(f"{label}: hed_process_ids repeats {pid!r}, already on the task; leave it out")
            for cand in v.get("candidates") or []:
                cited_by[cand].add(tid)
    return {c: sorted(ts) for c, ts in sorted(cited_by.items()) if len(ts) > 1}


def validate_catalog(data_dir: Path, tasks: list[dict], proc_data: dict) -> None:
    """Check the two catalog files against their schemas and against each other.

    Exits with every problem found, so that a contributor sees the whole list at once
    rather than one failure per run.
    """
    problems: list[str] = []
    task_schema = _schema_check(tasks, data_dir / "schemas" / "task_details.schema.json", "task_details.json", problems)
    proc_schema = _schema_check(
        proc_data, data_dir / "schemas" / "process_details.schema.json", "process_details.json", problems
    )
    roles = _reference_roles(task_schema) | _reference_roles(proc_schema)

    processes = proc_data["processes"]
    categories = proc_data["categories"]

    # Unique identifiers and names.
    for field, records, label in (
        ("hedtsk_id", tasks, "task"),
        ("canonical_name", tasks, "task"),
        ("process_id", processes, "process"),
        ("process_name", processes, "process"),
        ("category_id", categories, "category"),
    ):
        for value, n in collections.Counter(r[field] for r in records).items():
            if n > 1:
                problems.append(f"{label} {field} {value!r} appears {n} times")

    # Cross-references.
    process_ids = {p["process_id"] for p in processes}
    category_ids = {c["category_id"] for c in categories}
    task_ids = {t["hedtsk_id"] for t in tasks}
    for t in tasks:
        for pid in t.get("hed_process_ids", []):
            if pid not in process_ids:
                problems.append(f"{t['hedtsk_id']}: hed_process_ids names unknown process {pid!r}")
        # The inclusion test is three lists (data/README.md, "Editing a task or process"):
        # procedure steps are sentences, the other two are fragments. The schema checks
        # the shape; the text rules are here.
        test = t.get("inclusion_test") or {}
        for step in test.get("procedure") or []:
            if step != step.strip() or not step.endswith((".", "!", "?")):
                problems.append(f"{t['hedtsk_id']}: procedure step must be a trimmed sentence ending in a period: {step!r}")
        for field in ("manipulations", "measurements"):
            for item in test.get(field) or []:
                # No capital-letter rule: an item may begin with an initialism (fMRI) or
                # a conventionally lowercase term (d-prime).
                if item != item.strip() or not item or item.endswith((";", ".")) or not (item[0].isalnum() or item[0] == "("):
                    problems.append(
                        f"{t['hedtsk_id']}: {field} item must be trimmed, begin with a letter, digit or parenthesis "
                        f"and carry no final period or semicolon: {item!r}"
                    )
        # Every task engages at least one process.
        if not t.get("hed_process_ids"):
            problems.append(f"{t['hedtsk_id']}: hed_process_ids is empty; every task is linked to at least one process")
    _check_memberships(processes, "categories", "category_id", category_ids, "process_id", problems)
    primary_cats = {primary_category(p) for p in processes if any(m.get("role") == "primary" for m in p.get("categories", []))}
    for cid in sorted(category_ids - primary_cats):
        problems.append(f"category {cid}: no process is filed under it")

    # Derived fields must agree with their sources: a process's tasks[] with the tasks
    # that name it, task_count with tasks[], and the category and header counts.
    derived: dict[str, list[str]] = collections.defaultdict(list)
    for t in tasks:
        for pid in t.get("hed_process_ids", []):
            derived[pid].append(t["hedtsk_id"])
    for p in processes:
        listed = [x["hedtsk_id"] for x in p.get("tasks", [])]
        expected = sorted(derived.get(p["process_id"], []))
        if sorted(listed) != expected:
            problems.append(
                f"{p['process_id']}: tasks[] lists {sorted(listed)} but the task records name it from {expected}; "
                "update tasks[] and task_count on the process"
            )
        if p.get("task_count", len(listed)) != len(listed):
            problems.append(f"{p['process_id']}: task_count {p.get('task_count')} but tasks[] has {len(listed)}")
        for x in p.get("tasks", []):
            if x["hedtsk_id"] not in task_ids:
                problems.append(f"{p['process_id']}: tasks[] names unknown task {x['hedtsk_id']!r}")
    per_category = collections.Counter(
        primary_category(p) for p in processes if any(m.get("role") == "primary" for m in p.get("categories", []))
    )
    for c in categories:
        if c.get("process_count") != per_category[c["category_id"]]:
            problems.append(
                f"category {c['category_id']}: process_count {c.get('process_count')} but "
                f"{per_category[c['category_id']]} processes are filed under it"
            )
    for key, actual in (
        ("total_processes", len(processes)),
        ("total_categories", len(categories)),
        ("total_tasks", len(tasks)),
        ("total_processes_used_by_tasks", sum(1 for p in processes if derived.get(p["process_id"]))),
    ):
        if key in proc_data and proc_data[key] != actual:
            problems.append(f"process_details.json header {key} is {proc_data[key]} but the data has {actual}")

    # Reference roles from the vocabulary; no new reference should be left `unknown`.
    for records, idf in ((tasks, "hedtsk_id"), (processes, "process_id")):
        for r in records:
            for i, ref in enumerate(r.get("references", [])):
                bad = [role for role in ref.get("roles", []) if role not in roles]
                if bad:
                    problems.append(f"{r[idf]}: reference {i} has roles {bad} not in {sorted(roles)}")

    # The game model: game type, rules, motivators, facets, phases, settings, combined
    # games, candidates and variants, against the three vocabulary files. Variant ids are
    # stored; check_game_records checks their form and that they are unique.
    vocab = load_vocabularies(data_dir, problems)
    shared = check_game_records(tasks, vocab, process_ids, problems)
    for cand, task_list in shared.items():
        print(f"  note: candidate {cand} is cited by {len(task_list)} tasks ({', '.join(task_list)}); consider promoting it")

    # ASCII only, apart from letters in author names and published titles. The TSV
    # tables have no such fields, so they are ASCII throughout; the Atlas tables are
    # cleaned when src/build_atlas_maps.py writes them.
    _check_ascii("task_details.json", tasks, problems)
    _check_ascii("process_details.json", proc_data, problems)
    for tsv in sorted(data_dir.rglob("*.tsv")):
        for n, line in enumerate(tsv.read_text(encoding="utf-8").splitlines(), 1):
            bad = sorted({c for c in line if ord(c) > 127})
            if bad:
                chars = ", ".join(f"U+{ord(c):04X}" for c in bad)
                problems.append(f"{tsv.relative_to(data_dir).as_posix()}:{n}: non-ASCII {chars}")

    if problems:
        sys.exit(f"Catalog data is inconsistent ({len(problems)} problems); nothing written.\n  " + "\n  ".join(problems))


def load_families(data_dir: Path, tasks: list[dict]) -> list[dict]:
    """Read data/task_family_defs.tsv and validate every task's `families` against it.

    Raises SystemExit with a list of every problem found, so that a partial site is never
    published from an inconsistent assignment. Returns the family definitions sorted by
    display order.
    """
    defs = read_tsv(data_dir / "task_family_defs.tsv")
    problems: list[str] = []

    if not defs:
        problems.append("data/task_family_defs.tsv is missing or empty")

    family_ids = [d["family_id"] for d in defs]
    if len(family_ids) != len(set(family_ids)):
        problems.append("duplicate family_id in task_family_defs.tsv")
    known = set(family_ids)

    _check_memberships(tasks, "families", "family_id", known, "hedtsk_id", problems)
    with_primary = [t for t in tasks if any(m.get("role") == "primary" for m in t.get("families", []))]
    used = {primary_family(t) for t in with_primary}
    for fid in sorted(known - used):
        problems.append(f"task_family_defs.tsv: no task is filed under family {fid}")

    if problems:
        sys.exit("Family data is inconsistent; nothing written.\n  " + "\n  ".join(problems))

    defs.sort(key=lambda d: int(d["order"]))
    return defs


# ---------------------------------------------------------------------------
# Generation
# ---------------------------------------------------------------------------


def clear_generated(docs_dir: Path) -> int:
    """Delete the generated paths under docs/source/. Returns the number of files removed."""
    removed = 0
    for rel in GENERATED_PATHS:
        path = docs_dir / rel
        if path.is_dir():
            removed += sum(1 for p in path.rglob("*") if p.is_file())
            shutil.rmtree(path)
        elif path.exists():
            path.unlink()
            removed += 1
    return removed


def main() -> None:
    repo_root = _HERE.parent
    parser = argparse.ArgumentParser(description="Validate the catalog and generate the catalog pages.")
    parser.add_argument(
        "--docs-dir",
        type=Path,
        default=repo_root / "docs" / "source",
        help="The Sphinx source directory to write into (default: docs/source). Use a copy to try a change.",
    )
    args = parser.parse_args()
    data_dir = repo_root / "data"
    docs_dir = args.docs_dir.resolve()

    print("Loading data/task_details.json and data/process_details.json ...")
    tasks: list[dict] = load_json(data_dir / "task_details.json")
    proc_data: dict = load_json(data_dir / "process_details.json")
    categories: list[dict] = proc_data["categories"]
    processes: list[dict] = proc_data["processes"]

    print("Validating the catalog ...")
    validate_catalog(data_dir, tasks, proc_data)
    families = load_families(data_dir, tasks)
    print(
        f"  {len(tasks)} tasks, {len(processes)} processes, {len(categories)} categories, {len(families)} families: consistent"
    )

    # The curated mapping drives the Atlas link on each task page and is the only Atlas
    # cross-reference; task records carry no atlas_id of their own.
    atlas_map = {r["hedtsk_id"]: r for r in read_tsv(data_dir / "mappings" / "hed_task_to_atlas.tsv")}
    # Atlas entries matched to a variant (exact or close) are linked from that variant's
    # row, so that a task with several Atlas entries shows all of them where each belongs.
    atlas_variant_map: dict[str, list[dict]] = collections.defaultdict(list)
    for row in read_tsv(data_dir / "mappings" / "atlas_task_to_hed.tsv"):
        if row["match_level"] == "variant" and row["match_type"] in ("exact", "close"):
            atlas_variant_map[row["hed_variant_id"]].append(row)

    # The CogPO mapping drives the CogPO link on each task page the same way. A class
    # links to its page on the CogPO wiki, whose title the summary records; the two
    # Oddball subclasses have no wiki page and get no link.
    cogpo_summary = load_json(data_dir / "cogpo_summary.json")
    wiki_titles = {p["id"]: p["wiki"]["title"] for p in cogpo_summary["paradigms"] if p.get("wiki")}
    wiki_titles.update({p["title"]: p["title"] for p in cogpo_summary["paradigm_comparison"]["wiki_only"]})
    cogpo_map = {}
    for row in read_tsv(data_dir / "mappings" / "hed_task_to_cogpo.tsv"):
        row["cogpo_wiki_title"] = wiki_titles.get(row["cogpo_id"], "")
        cogpo_map[row["hedtsk_id"]] = row

    tasks_by_id: dict[str, dict] = {t["hedtsk_id"]: t for t in tasks}
    processes_by_id: dict[str, dict] = {p["process_id"]: p for p in processes}

    removed = clear_generated(docs_dir)
    print(f"Removed {removed} previously generated files.")
    total = 0

    print("Generating docs/source/tasks/ ...")
    game_defs = load_json(data_dir / "task_game_defs.json")
    n = task_pages.generate(docs_dir, tasks, processes_by_id, families, atlas_map, cogpo_map, atlas_variant_map, game_defs)
    total += n
    print(
        f"  Wrote {n} task files (index, tasks_by_family, {len(families)} family pages, tasks_alphabetically, {len(tasks)} task pages)."
    )
    n = vocabulary_pages.generate(docs_dir, data_dir, tasks)
    total += n
    print(f"  Wrote {n} vocabulary files (vocabulary, by_game_type, by_facet).")

    print("Generating docs/source/processes/ ...")
    n = process_pages.generate(docs_dir, processes, categories, tasks_by_id)
    total += n
    print(f"  Wrote {n} process files (index, processes_by_category, processes_alphabetically, {n - 3} category pages).")

    print("Generating docs/source/task_process_links.md ...")
    total += crossref_page.generate(docs_dir, tasks, processes, categories)

    print("Generating docs/source/_generated/ fragments ...")
    total += crossref_atlas_pages.generate(docs_dir, data_dir)
    total += crossref_cogpo_pages.generate(docs_dir, data_dir)
    total += fragments.generate(docs_dir, data_dir, tasks, processes, categories, families)

    print(f"\nDone. {total} files written to {docs_dir}. Narrative pages were not touched.")


if __name__ == "__main__":
    main()
