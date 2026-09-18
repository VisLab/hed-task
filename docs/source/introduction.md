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

The catalog currently has 103 tasks. Each task page carries:

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
  are 772 variations across the catalog;
- the **cognitive processes** the task engages, linked to their definitions;
- **key references** that established the paradigm and **recent references** that give a
  modern entry point;
- where one exists, the corresponding **Cognitive Atlas** entry.

### Paradigm families

Tasks are filed under 18 **paradigm families** by what the participant does:
conflict and interference tasks, response inhibition tasks, recall and recognition
tests, economic games, and so on. The Stroop Color-Word Task is in the family
*Conflict and interference tasks*. A family is a browsing aid, not a claim about mechanism; the
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

The catalog has 172 processes in 19 **categories**. A category
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
| Task | `hedtsk_<slug>` | `hedtsk_stroop_color_word` |
| Task variation | `hedvar_<task slug>__<variation slug>` | `hedvar_stroop_color_word__counting_stroop` |
| Process | `hed_<slug>` | `hed_response_inhibition` |
| Process category | `<slug>` | `inhibitory_control_and_conflict_monitoring` |
| Paradigm family | `<slug>` | `conflict_and_interference` |

The `hed_` prefix on process identifiers is the catalog's working prefix and is not a
claim of HED schema membership. Identifiers are provisional while the catalog is being
curated; when they stabilise, renames will become aliases.

## Where the catalog came from

The starting corpus was the [Cognitive Atlas](https://www.cognitiveatlas.org/), a community-built ontology
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
ideas should be posted as issues at <https://github.com/hed-standard/hed-task/issues>; the repository's
[contributing guide](https://github.com/hed-standard/hed-task/blob/main/CONTRIBUTING.md) describes the process, and
[how to use the catalog](how_to_use.md) says what a useful proposal contains.
