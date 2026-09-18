"""Generate the two overview pages: docs/introduction.md and docs/how_to_use.md.

`introduction.md` explains what the catalog is made of and how it came to be.
`how_to_use.md` explains how to read a task page and a process page, how to decide
whether an experiment is an instance of a task, and how to propose a change. Both are
prose written here in the generator, with every count computed from the data.
"""

from __future__ import annotations

from pathlib import Path

from generators.utils import write_page

ISSUES_URL = "https://github.com/hed-standard/hed-task/issues"
CONTRIBUTING_URL = "https://github.com/hed-standard/hed-task/blob/main/CONTRIBUTING.md"
REPO_URL = "https://github.com/hed-standard/hed-task"
ATLAS_URL = "https://www.cognitiveatlas.org/"


def _example_task(tasks: list[dict], hedtsk_id: str) -> dict:
    return next(t for t in tasks if t["hedtsk_id"] == hedtsk_id)


def _introduction(
    tasks: list[dict],
    processes: list[dict],
    categories: list[dict],
    families: list[dict],
    family_of: dict[str, str],
) -> str:
    n_tasks, n_processes = len(tasks), len(processes)
    n_categories, n_families = len(categories), len(families)
    n_variations = sum(len(t.get("variations", [])) for t in tasks)
    stroop = _example_task(tasks, "hedtsk_stroop_color_word")
    stroop_family = family_of[stroop["hedtsk_id"]]
    example_variation = stroop["variations"][3]  # Counting Stroop
    example_var_id = example_variation["variation_id"]

    return f"""\
# Introduction

This page explains the pieces the catalog is made of and how they fit together. It is
the place to start if you have not used the catalog before.

## What the catalog is for

Experiments in cognitive and behavioral neuroscience are built from a fairly small
repertoire of standard tasks, but the datasets they produce rarely say which one was
used in a way a machine can act on. This catalog provides a controlled vocabulary for
that: a list of tasks, a list of the cognitive processes those tasks engage, and the
links between them. Tagging a dataset with identifiers from the catalog makes it
findable by task name, by alias, or by process, and makes datasets that share a task or
a process comparable.

The catalog is developed as part of HED (Hierarchical Event Descriptors), the standard
for annotating what happened during an experiment. HED describes events; the task
catalog describes the paradigm the events belong to. How task and process identifiers
will be carried in HED annotations and in dataset metadata is not yet decided, and the
identifiers here are not HED schema terms.

## Tasks

A **task** in this catalog is a structured experimental paradigm that produces a
sequence of discrete, time-stamped events, has a specific reproducible procedure, is
widely used, and engages identifiable cognitive processes. Questionnaires, clinical
screening instruments, generic labels such as "memory task", and one-off designs are
excluded. The full rules are in the [task selection criteria](methods/task_criteria.md).

The catalog currently has {n_tasks} tasks. Each task page carries:

- a **canonical name** and its **aliases**, so that a search for "CWIT" or "Stroop" lands
  on the Stroop Color-Word Task;
- a **short definition** and a longer **description**;
- an **inclusion test** in three parts: the *procedure* the participant follows, the
  *manipulation* the experimenter varies, and the *measurement* recorded. An experiment
  is an instance of the task when its procedure matches, it manipulates at least one of
  the listed variables, and it records at least one of the listed measures. The
  procedure is decisive: two experiments with the same procedure are the same task even
  if they target different constructs;
- a list of **variations**, each with a description and a justification. A variation
  is a named version that changes what the participant experiences or does, so that the
  event structure of the recorded data differs. Changing the recording equipment, the
  analysis, the population or the stimulus set does not make a variation; changing the
  response modality, the stimulus-response mapping or the required actions does. There
  are {n_variations} variations across the catalog;
- the **cognitive processes** the task engages, linked to their definitions;
- **key references** that established the paradigm and **recent references** that give a
  modern entry point;
- where one exists, the corresponding **Cognitive Atlas** entry.

### Paradigm families

Tasks are filed under {n_families} **paradigm families** by what the participant does:
conflict and interference tasks, response inhibition tasks, recall and recognition
tests, economic games, and so on. The Stroop Color-Word Task is in the family
*{stroop_family}*. A family is a browsing aid, not a claim about mechanism; the
processes a task engages are the place to look for that. Every task is in exactly one
family, and the assignment is a curation decision that is expected to change. The
[task index](tasks/index.md) lists the families with their scope.

## Cognitive processes

A **cognitive process** is a mental operation hypothesized to occur during a trial:
something with an identifiable onset, an eliciting condition and an in-principle
measurable signature. A candidate qualifies when it is plausible to say when in a trial
it happens, what elicits it, and how it is measured. States and traits, specific
emotions, stimulus categories, individual-difference constructs, task parameters,
analysis methods and umbrella terms such as "attention" or "memory" are excluded; the
umbrella role is carried by the categories instead. The full rules are in the
[process selection criteria](methods/process_criteria.md).

The catalog has {n_processes} processes in {n_categories} **categories**. A category
groups processes by research tradition for browsing and carries a scope statement and a
note of what is out of scope. Each process page entry has a definition, aliases where
the literature uses more than one name, fundamental and recent references, and the list
of tasks that engage it. Some processes are engaged by no task in the current catalog;
they are kept because they are real and the catalog may grow a task for them.

## Links between tasks and processes

A task is linked to a process when the task's inclusion test engages that process: the
paradigm-defining papers say so, a standard condition contrast isolates it, or a
standard measure indexes it. A link is not an ontology assertion and not a claim that
the task engages nothing else; it records what the task is designed to probe. The
[task-process links](crossref.md) page lists every link in both directions.

## Identifiers

Every entity has a typed identifier, so an identifier met anywhere can be classified
at sight:

| Kind | Form | Example |
| --- | --- | --- |
| Task | `hedtsk_<slug>` | `{stroop["hedtsk_id"]}` |
| Task variation | `hedvar_<task slug>__<variation slug>` | `{example_var_id}` |
| Process | `hed_<slug>` | `hed_response_inhibition` |
| Process category | `<slug>` | `inhibitory_control_and_conflict_monitoring` |
| Paradigm family | `<slug>` | `{[f["family_id"] for f in families if f["name"] == stroop_family][0]}` |

The `hed_` prefix on process identifiers is the catalog's working prefix and is not a
claim of HED schema membership. Identifiers are provisional while the catalog is being
curated; when they stabilise, renames will become aliases.

## Where the catalog came from

The starting corpus was the [Cognitive Atlas]({ATLAS_URL}), a community-built ontology
of cognitive concepts and the paradigms that measure them. Its task list was narrowed to
paradigms that produce event-structured data, its concepts were reshaped into processes
that pass the selection test above, and a gap analysis added paradigms the Atlas never
registered. Every task and process here is mapped back to the Atlas entry by entry; the
[Cognitive Atlas](atlas/cognitive_atlas.md) pages describe the Atlas on its own terms,
the [relationship](atlas/relationship.md) page says how the two resources differ, and
the [mapping method](methods/atlas_mapping.md) page says how each correspondence was
decided.

## Status

The catalog is a work in progress. Its lists are not definitive, its identifiers are
provisional, and its curation is a continuing process. Suggestions, corrections and
ideas should be posted as issues at <{ISSUES_URL}>; the repository's
[contributing guide]({CONTRIBUTING_URL}) describes the process, and
[how to use the catalog](how_to_use.md) says what a useful proposal contains.
"""


def _how_to_use(tasks: list[dict], processes: list[dict]) -> str:
    stroop = _example_task(tasks, "hedtsk_stroop_color_word")
    inclusion = stroop["inclusion_test"]
    n_tasks = len(tasks)

    return f"""\
# How to use the catalog

This page is for a reader who wants to do something with the catalog: identify the task
in an experiment, tag a dataset, look up a process, or propose a change.

## Finding a task

Three routes lead to a task page.

- **By name or alias.** The search box in the sidebar indexes canonical names, aliases,
  definitions and variation names, so "CWIT", "Stroop" and "color-word interference"
  all reach the Stroop Color-Word Task.
- **By what the participant does.** The [task index](tasks/index.md) groups the
  {n_tasks} tasks into paradigm families such as conflict and interference tasks, span
  tasks and economic games. Each family has a scope sentence and a table of its tasks.
- **By process.** Each entry on a [process category page](processes/index.md) lists the
  tasks that engage the process, and the [task-process links](crossref.md) page gives
  the whole matrix.

The [alphabetical list](tasks/all_tasks.md) is the fallback when you know the name but
not the family.

## Reading a task page

Take the [Stroop Color-Word Task](tasks/hedtsk_stroop_color_word.md) as the example.

**Identifier and aliases.** The identifier `{stroop["hedtsk_id"]}` is the value to
record when tagging. The aliases are the other names the literature uses for the same
procedure.

**Inclusion test.** The three rows decide whether a particular experiment is an
instance of this task:

- *Procedure*: {inclusion["procedure"]}
- *Manipulation*: {inclusion["manipulation"]}
- *Measurement*: {inclusion["measurement"]}

An experiment is an instance when its procedure matches, it manipulates at least one of
the listed variables, and it records at least one of the listed measures. If the
procedure does not match, it is a different task even if the construct is the same. If
the procedure matches but the experiment differs in a way listed under *Variations*, it
is an instance of that variation.

**Variations.** Each row names a version that changes what the participant experiences
or does, describes it, and says why it counts. Variations have identifiers of the form
`hedvar_<task>__<variation>`, so a dataset can be tagged with a variation when the
distinction matters. Things that are deliberately *not* variations, such as adding a
recording modality or testing a different population, are listed in the
[task criteria](methods/task_criteria.md).

**Cognitive processes.** The processes the task is designed to engage, each linked to
its definition. These are the process tags a dataset using this task would carry.

**References.** *Key references* established the paradigm; *recent references* are
reviews or influential recent papers. Citations are reproduced as the source supplies
them.

**External links.** The corresponding Cognitive Atlas entry, with a qualifier when the
match is close rather than exact.

## Reading a process page

Processes are presented one category to a page. The category page opens with the
category's scope, what is out of scope, any open issue about its boundaries, and a
summary table of its processes. Each process entry then gives the identifier, aliases
with a note on the terminological distinction, the definition, the tasks that engage it,
and references. A process with no linked tasks says so; it is kept because the catalog
may grow a task for it.

## Tagging a dataset

The catalog's identifiers are stable enough to record now, even though how they will be
expressed in HED annotations and dataset metadata is still being decided. For a dataset:

1. Identify the task with the inclusion test, and the variation if one applies.
2. Record the task identifier (`hedtsk_...`) and, if applicable, the variation
   identifier (`hedvar_...`).
3. Record the process identifiers (`hed_...`) listed on the task page. Add processes
   the task page does not list only if the experiment's own design targets them; the
   task page lists what the paradigm is designed to probe, not everything it touches.
4. If the experiment is a task the catalog does not have, or a variation a task page
   does not list, propose it (next section) rather than forcing a fit.

## Proposing a change

The catalog is curated continuously and depends on its users to grow. The repository's
[contributing guide]({CONTRIBUTING_URL}) describes the process; in short, post an issue at
<{ISSUES_URL}> for any of the following.

- **A new task.** Give the canonical name and aliases, a procedure, a manipulation and
  a measurement in the form the inclusion tests use, the processes it engages, and one
  or two references. Say why it is not a variation of an existing task.
- **A new variation.** Name the parent task, describe what changes in what the
  participant experiences or does, and say why that is not one of the excluded kinds of
  change (measurement modality, analysis, population, stimulus swap, and so on).
- **A new process.** Say when in a trial it happens, what elicits it, how it is
  measured, and which category it belongs in. Say why it is not an alias of an existing
  process.
- **A correction.** Anything wrong on a page: a definition, a reference, a link, a
  family assignment, an Atlas mapping. Quote the page and the text.
- **A disagreement with a rule.** The criteria pages state the rules as they stand;
  arguments for changing one are welcome.

The source for the site is at <{REPO_URL}>. The pages are generated from the catalog
data, so corrections are applied to the data, not to the pages.
"""


def generate(
    docs_dir: Path,
    tasks: list[dict],
    processes: list[dict],
    categories: list[dict],
    families: list[dict],
    family_of: dict[str, str],
) -> int:
    """Write docs/introduction.md and docs/how_to_use.md. Returns the file count."""
    write_page(docs_dir / "introduction.md", _introduction(tasks, processes, categories, families, family_of))
    write_page(docs_dir / "how_to_use.md", _how_to_use(tasks, processes))
    return 2
