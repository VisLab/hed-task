"""Generate docs/atlas/ -- pages about the Cognitive Atlas.

`cognitive_atlas.md` describes the Atlas as a resource, on its own terms, from the
statistics in `.working/atlas_summary.json`. It makes no comparison to this catalog;
that belongs on a separate page.

Tables are built into local variables before the page text is assembled, so that no
f-string has to nest a quoted subscript (which is a syntax error before Python 3.12).
"""

from __future__ import annotations

from pathlib import Path

from generators.utils import write_page

ATLAS_URL = "https://www.cognitiveatlas.org/"
ATLAS_API = "http://cognitiveatlas.org/api/v-alpha"
ATLAS_PAPER = (
    "Poldrack, R. A., Kittur, A., Kalar, D., Miller, E., Seppa, C., Gil, Y., "
    "Parker, D. S., Sabb, F. W., & Bilder, R. M. (2011). The Cognitive Atlas: "
    "Toward a knowledge foundation for cognitive neuroscience. "
    "*Frontiers in Neuroinformatics*, 5, 17."
)


def _table(headers: list[str], rows: list[list]) -> str:
    """Render a GitHub-style Markdown table."""
    out = ["| " + " | ".join(headers) + " |"]
    out.append("|" + "|".join("---" for _ in headers) + "|")
    for row in rows:
        out.append("| " + " | ".join(str(cell) for cell in row) + " |")
    return "\n".join(out)


def _pct(value: float) -> str:
    return f"{value}%"


def _share(part: int, whole: int) -> str:
    return f"{round(100 * part / whole, 1)}%"


def _code_list(names: list[str]) -> str:
    return ", ".join("`" + name + "`" for name in names)


def _row(rows: list[dict], label: str) -> dict:
    return next(r for r in rows if r["label"] == label)


def _index_page() -> str:
    return f"""\
# The Cognitive Atlas

The [Cognitive Atlas]({ATLAS_URL}) is a community-built ontology of cognitive processes
and the experimental paradigms used to measure them. It is the largest openly licensed
resource of its kind and was the starting corpus for this catalog.

These pages describe the Atlas as it stands and how this catalog relates to it.

```{{toctree}}
:maxdepth: 2

cognitive_atlas
relationship
task_crossref
process_crossref
```
"""


def _atlas_page(data: dict) -> str:  # noqa: PLR0914 - a report with many named figures
    inv = data["inventory"]
    tasks = data["tasks"]
    concepts = data["concepts"]
    hyg = data["hygiene"]
    orphans = concepts["orphans"]
    linked = concepts["linked"]

    total_tasks = tasks["total"]
    total_concepts = concepts["total"]
    snapshot = data.get("harvested_on", "")[:10]

    zero_concepts = _row(tasks["concept_links"], "0 concepts")
    one_concept = _row(tasks["concept_links"], "1 concept")
    skeletal = _row(data["tiers"], "Skeletal")
    well = _row(data["tiers"], "Well annotated")

    thin_graph = round(zero_concepts["percent"] + one_concept["percent"])
    non_paradigms = sum(r["count"] for r in data["entry_types"][:-1])
    no_relations = concepts["detail_records"] - concepts["with_relations"]
    no_citations = concepts["detail_records"] - concepts["with_citations"]

    # --- tables -------------------------------------------------------
    inventory_table = _table(
        ["Layer", "Entries", "Detail records retrieved"],
        [
            ["Tasks (experimental paradigms)", inv["tasks_listed"], inv["task_records"]],
            ["Concepts (mental processes)", inv["concepts_listed"], inv["concept_records"]],
        ],
    )
    task_def_table = _table(
        ["Definition length", "Tasks", "Share"],
        [[r["label"], r["count"], _pct(r["percent"])] for r in tasks["definitions"]],
    )
    concept_link_table = _table(
        ["Concepts asserted", "Tasks", "Share"],
        [[r["label"], r["count"], _pct(r["percent"])] for r in tasks["concept_links"]],
    )
    citation_table = _table(
        ["Measure", "Count", "Share of tasks"],
        [
            ["Tasks with at least one citation", tasks["cited"], _pct(tasks["cited_percent"])],
            ["Tasks with no citation", tasks["uncited"], _pct(tasks["uncited_percent"])],
        ],
    )
    completeness_table = _table(
        ["Combination", "Tasks", "Share"],
        [
            [
                "Definition and concepts and citation",
                tasks["complete"],
                _share(tasks["complete"], total_tasks),
            ],
            [
                "No citation and no concepts",
                tasks["no_citation_no_concepts"],
                _share(tasks["no_citation_no_concepts"], total_tasks),
            ],
            [
                "No definition and no concepts",
                tasks["no_definition_no_concepts"],
                _share(tasks["no_definition_no_concepts"], total_tasks),
            ],
        ],
    )
    fields_table = _table(
        ["Field", "Tasks with at least one", "Share", "Total entries"],
        [[r["label"], r["tasks"], _pct(r["percent"]), r["entries"]] for r in tasks["fields"]],
    )
    concept_def_table = _table(
        ["Definition length", "Concepts", "Share"],
        [[r["label"], r["count"], _pct(r["percent"])] for r in concepts["definitions"]],
    )
    orphan_table = _table(
        ["Group", "Concepts", "Share", "No definition", "No class", "Median definition"],
        [
            [
                "Asserted by at least one task",
                linked["total"],
                _pct(linked["percent"]),
                _pct(linked["no_definition_percent"]),
                _pct(linked["no_class_percent"]),
                f"{linked['definition_median']} chars",
            ],
            [
                "Asserted by no task",
                orphans["total"],
                _pct(orphans["percent"]),
                _pct(orphans["no_definition_percent"]),
                _pct(orphans["no_class_percent"]),
                f"{orphans['definition_median']} chars",
            ],
        ],
    )
    class_table = _table(
        ["Concept class", "Concepts", "Share"],
        [[r["label"], r["concepts"], _pct(r["percent"])] for r in concepts["classes"]],
    )
    unclassified_table = _table(
        ["Concept", "Tasks asserting it"],
        [[r["name"], r["tasks"]] for r in concepts["top_unclassified"]],
    )
    spread_table = _table(
        ["Tasks per concept", "Concepts", "Share"],
        [[r["label"], r["count"], _pct(r["percent"])] for r in concepts["task_spread"]],
    )
    top_concept_table = _table(
        ["Concept", "Tasks"],
        [[r["name"], r["tasks"]] for r in concepts["top_concepts"]],
    )
    relation_table = _table(
        ["Relation", "Edges"],
        [[r["label"], r["count"]] for r in concepts["relations"]],
    )
    tier_table = _table(
        ["Tier", "Tasks", "Share"],
        [[r["label"], r["count"], _pct(r["percent"])] for r in data["tiers"]],
    )
    entry_type_table = _table(
        ["Entry kind (name-based)", "Entries"],
        [[r["label"], r["count"]] for r in data["entry_types"]],
    )
    fragmentation_table = _table(
        ["Family", "Entries", "With zero concepts", "Best-annotated entry", "Concepts"],
        [
            [
                r["family"],
                r["entries"],
                r["zero_concept_entries"],
                r["best_entry"],
                r["best_concepts"],
            ]
            for r in data["fragmentation"]
        ],
    )
    hygiene_table = _table(
        ["Issue", "Tasks", "Concepts"],
        [
            [
                "Raw HTML entities in the definition",
                hyg["task_entities"],
                hyg["concept_entities"],
            ],
            [
                "Mis-decoded UTF-8 in the definition",
                hyg["task_mojibake"],
                hyg["concept_mojibake"],
            ],
            [
                "Definition is the literal string `None`",
                hyg["null_definition_tasks"],
                hyg["null_definition_concepts"],
            ],
        ],
    )
    year_table = _table(
        ["Year", "Task entries", "Concept entries"],
        [[r["year"], r["tasks"], r["concepts"]] for r in data["years"]],
    )

    # --- inline figures ----------------------------------------------
    placeholder_concepts = _code_list(concepts["placeholder_names"])
    placeholder_count = len(concepts["placeholder_names"])
    duplicate_tasks = _code_list(hyg["duplicate_task_names"])
    duplicate_concepts = _code_list(concepts["duplicate_names"])
    complete_share = _share(tasks["complete"], total_tasks)

    return f"""\
# What is in the Cognitive Atlas

The [Cognitive Atlas]({ATLAS_URL}) is a collaboratively built ontology of cognitive
processes and the experimental paradigms that measure them. It separates *concepts*
(mental processes) from *tasks* (experimental paradigms), gives each a stable
identifier, and records which concepts a task is claimed to assess. It is the only
openly licensed lexicon spanning the breadth of cognitive neuroscience, and it was the
starting corpus for this catalog.

This page describes the Atlas on its own terms: what it contains, how completely its
entries are filled in, and what condition the data is in. It draws no comparison with
the task and process catalog published here.

## In short

The Atlas is best understood as a broad but thinly and unevenly curated corpus rather
than a finished reference. Its breadth is real, and so is its architecture: separating
processes from paradigms is right, the identifiers are stable, and a genuine
{concepts["relation_total"]}-edge relation graph connects concepts to one another.

The curation is partial, in both layers at once. On the task side,
{zero_concepts["count"]} of {total_tasks} tasks ({_pct(zero_concepts["percent"])})
assert no concept at all, which disconnects them from the ontology that gives the
Atlas its value, and only {tasks["complete"]} ({complete_share}) have a definition, a
concept, and a citation together. On the concept side, {orphans["total"]} of
{total_concepts} concepts ({_pct(orphans["percent"])}) are asserted by no task,
{concepts["unclassified"]} ({_pct(concepts["unclassified_percent"])}) carry no class,
and {no_citations} ({_share(no_citations, concepts["detail_records"])}) have no
citation. Curation also stopped: almost nothing in either layer was entered after 2017.

Anything built on the Atlas should treat it as a source of candidate terms and stable
identifiers to be verified, not as a curated authority.

## What was captured

The figures come from a snapshot of the Atlas REST API (`{ATLAS_API}`) taken on
{snapshot}. Both layers were pulled in full: the bulk listing for each, then the
detail record for every entry, which is where concept relations and citations live.

{inventory_table}

Pulling the concept endpoint directly matters. A harvest taken from the task endpoint
alone reaches a concept only when some task asserts it, which hides
{orphans["total"]} of the {total_concepts} concepts and every one of the
concept-to-concept relations.

## Tasks

### Definitions

{task_def_table}

Among the {tasks["definition_real_count"]} tasks that have a real definition, the mean
length is {tasks["definition_mean"]} characters, the median {tasks["definition_median"]},
and the longest {tasks["definition_max"]}. The spread is the point: entries range from a
single clause to a small essay, with no house style.

{hyg["null_definition_tasks"]} of the entries counted as missing hold the literal
four-character string `None` rather than any text. They cover well-known paradigms,
among them `visual search task`, `serial reaction time task`, and `color naming task`.

### Concept linkage

{concept_link_table}

There are {tasks["concept_link_total"]} task-to-concept links in total, a mean of
{tasks["concept_link_mean"]} per task against a maximum of {tasks["concept_link_max"]}.
About a third of tasks ({_pct(zero_concepts["percent"])}) assert no concept whatsoever
and another {_pct(one_concept["percent"])} assert exactly one, so for roughly
{thin_graph}% of entries the knowledge graph is either absent or a single edge. A long
definition is no guarantee of a linked one: several entries carry a substantial
write-up and no concepts at all.

### Citations

{citation_table}

The {tasks["cited"]} cited tasks carry {tasks["citation_total"]} citations between
them, of which {tasks["citation_with_pmid"]} record a PubMed id. The rest are
reachable only through a free-text reference or a bare URL.

### Everything filled in at once

{completeness_table}

Fewer than half of all task entries are complete in this minimal sense.

### Other structured fields

The schema offers more than definitions, concepts, and citations. Most of it is
sparsely used.

{fields_table}

Contrasts are the exception and are populated for most tasks, which makes them the most
reusable structured content in the Atlas after the concept links themselves.

## Concepts

### Definitions

{concept_def_table}

Concept definitions are shorter and more consistently present than task definitions.
{placeholder_count} are unfinished in a way that is visible in the published data,
carrying an editing placeholder such as `ADD DEFINITION HERE`, or a serialized null,
in place of a definition:

{placeholder_concepts}.

These are not obscure corners of the vocabulary. `working memory updating`,
`implicit learning`, `arousal`, `risk aversion`, and `exogenous attention` are all
constructs in active use, published with no definition at all.

### The half no task points at

{orphan_table}

Nearly half the concept layer is asserted by no task at all. The instinct is to assume
those are the leftovers, but they are not: the two groups have the same median
definition length and nearly the same rate of missing definitions. The orphans are
ordinary, adequately defined concepts that simply never got wired to a paradigm. They
are somewhat less likely to carry a class, but the difference is one of degree.

The consequence is that the Atlas's task-to-concept graph rests on about half its own
vocabulary, and a consumer who reaches the Atlas through tasks never sees the rest.

### Concept classes

The Atlas sorts concepts into ten top-level classes. Class assignment is the single
largest gap in the concept layer: {concepts["unclassified"]} of {total_concepts}
concepts ({_pct(concepts["unclassified_percent"])}) carry no class.

{class_table}

This is not confined to rarely used terms. The most heavily used concepts carrying no
class are:

{unclassified_table}

Among the classified concepts the balance is skewed. Learning and Memory, Language, and
Perception dominate, while Motivation, Action, and Social Function are barely
populated. That reflects curator interest rather than the shape of the field.

The class layer also mixes kinds of thing. Alongside cognitive processes it carries
traits, symptoms, and clinical constructs such as `impulsivity`, `hyperactivity`,
`defiance`, `obsession`, `anhedonia`, `perfectionism`, and `restricted behavior`. These
are legitimate research constructs but they are not mental processes, and nothing in
the schema separates them from those that are.

### Relations between concepts

Unlike the flat class assignment, the concept layer carries a real relation graph:
{concepts["relation_total"]} edges over {concepts["with_relations"]} concepts.

{relation_table}

This is the Atlas at its most valuable and is invisible to anyone who reads only the
task endpoint. It is also incomplete: {no_relations} concepts
({_share(no_relations, concepts["detail_records"])}) sit in the graph with no relation
to any other concept, so the hierarchy covers a majority of the vocabulary but far
from all of it.

### Citations

Only {concepts["with_citations"]} concepts
({_pct(concepts["with_citations_percent"])}) carry any citation, together holding
{concepts["citation_total"]} references. The other {no_citations} concepts
({_share(no_citations, concepts["detail_records"])}) have a definition with no source
of record, which is the concept layer's most consequential omission for anyone who
needs to justify a term.

### How widely concepts are used

{spread_table}

A small head does most of the work:

{top_concept_table}

These are the coarsest available labels. `visual perception`, `attention`, and
`cognitive control` are the terms an annotator reaches for when nothing more specific
is at hand. Their dominance suggests annotation stopped at the top of the hierarchy
rather than showing that these processes matter most.

## Overall task annotation quality

Combining definition length with concept count sorts every task entry into a tier. An
entry is *well annotated* with a definition of 300 characters or more and at least four
concepts, and *skeletal* with a definition under 50 characters or no concepts at all.

{tier_table}

Only {well["count"]} entries ({_pct(well["percent"])}) are well annotated, while
{skeletal["count"]} ({_pct(skeletal["percent"])}) are skeletal.

## What kind of thing is an entry?

The Atlas files everything under "task". In practice the corpus mixes experimental
paradigms with instruments that are not paradigms at all. Classifying by name gives a
lower bound, since it only catches entries whose name declares what they are.

{entry_type_table}

At least {non_paradigms} entries are rating scales, questionnaires, standardized
batteries, imaging protocol labels, or physiological procedures. Nothing in the record
distinguishes them from experimental paradigms, so any consumer has to impose that
distinction itself.

## Duplicate and fragmented entries

A paradigm family is often spread across several entries, one per implementation, with
no entry marked canonical and the best-annotated one frequently not the standard
version.

{fragmentation_table}

A reader searching for a paradigm lands on whichever variant matches their wording, and
the quality of what they find is largely accidental.

Names are duplicated outright in both layers: {duplicate_tasks} among tasks, and
{duplicate_concepts} among concepts. One concept is named `test term`, with no
definition, and is published alongside the rest.

## Data hygiene

{hygiene_table}

Definitions were pasted in from mixed sources without normalization, so escaped markup
such as `&#39;` and `&#34;` survives in the published text, along with byte sequences
from a double-encoding error. Any text taken from the Atlas needs cleaning before it is
displayed.

Non-ASCII characters in entry names are worth special care. Several tasks use a curly
apostrophe or an en dash in their name (`Raven's Progressive Matrices Test`,
`Penn's Logical Reasoning Test`, `Angling Risk Task - Always Sunny`), which is a
common source of retrieval failures in client code that assumes ASCII.

## When the curation happened

{year_table}

Entry timestamps cluster in an initial build-out around 2009 and a second push in 2012
and 2015, then stop. The absence of paradigms that became standard afterwards is a
direct consequence, and so is the absence of the computational vocabulary (model-based
and model-free learning, reward prediction error, evidence accumulation) that the field
adopted over the same period.

## Reading the Atlas fairly

The weaknesses above are those of an unfunded community resource that stopped being
actively curated, not of its design. What the Atlas got right still matters: separating
processes from paradigms is the correct architecture, the identifiers are stable and
citable, the relation graph is real, and the breadth of coverage is unmatched by any
open alternative. For the subset of entries that were curated properly, the
task-to-concept graph is exactly the structure a paradigm ontology needs.

The practical conclusion is about how to use it. The Atlas is a well-designed, broadly
scoped, partially populated corpus. It is an excellent source of candidate paradigm
names, concept labels, and stable identifiers. It is not a source that can be consumed
without verification, because a given entry may be complete, a stub, a duplicate
variant, or a questionnaire, and nothing in the record says which.

## Reference

{ATLAS_PAPER}

The Atlas is published at <{ATLAS_URL}>, with a REST API at `{ATLAS_API}` and a Python
client at <https://github.com/CognitiveAtlas/cogat-python>.
"""


def generate(docs_dir: Path, atlas_data: dict) -> int:
    """Write docs/atlas/index.md and docs/atlas/cognitive_atlas.md.

    Returns the number of files written.
    """
    atlas_dir = docs_dir / "atlas"
    write_page(atlas_dir / "index.md", _index_page())
    write_page(atlas_dir / "cognitive_atlas.md", _atlas_page(atlas_data))
    return 2
