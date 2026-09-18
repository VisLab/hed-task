# HED task catalog

A curated vocabulary of the standard tasks used in cognitive and behavioral neuroscience
experiments, and of the cognitive processes those tasks engage. It exists so that
datasets can be tagged with what their participants were asked to do, in terms that are
the same across laboratories.

## What is the HED task catalog?

The catalog is two linked lists.

**Tasks** are experimental paradigms with a specific, reproducible procedure: the Stroop
Color-Word Task, the N-Back Task, the Iowa Gambling Task. Each task has a canonical name
and its aliases, a description, an *inclusion test* stating the procedure, the
manipulation and the measurement that make an experiment an instance of that task, a list
of named variations with the reason each one counts as a variation, and verified
references. Tasks are filed under 18 paradigm families according to what the
participant does.

**Cognitive processes** are the mental operations a task is designed to engage: response
inhibition, working memory updating, reward anticipation. Each process has a definition,
references, and a place in one of 19 categories.

Every task states which processes it engages, and every process lists the tasks that
engage it. The catalog is part of the HED (Hierarchical Event Descriptors) effort to
make the events in neuroimaging and behavioral data machine-readable; see the
[HED resources](https://www.hedtags.org/hed-resources) site for HED itself.

## Why a task and process taxonomy?

A data repository knows what files a dataset contains but usually not what its
participants did beyond a free-text label such as `task-flanker` or `task-rest`. The
same paradigm goes by different names across laboratories, and related paradigms that
engage the same process are not connected at all. This catalog is meant to supply the
missing layer:

- **Tags for datasets.** A dataset tagged with a task identifier from this catalog, and
  with the process identifiers that task engages, can be found by a repository search for
  the task, for any of its aliases, or for a process, whatever the dataset called it
  locally.
- **Commonalities across datasets.** Two datasets tagged with the same task can be
  compared directly. Two datasets tagged with different tasks that share a process can be
  grouped for a question about that process.
- **Context for event annotation.** A task tag tells a reader of a HED-annotated events
  file what the trial structure was designed to do, which the event-level annotations
  alone do not.

How these tags will be expressed in HED annotations and in dataset metadata is still being
worked out; the identifiers here are the catalog's own and are not yet HED schema terms.

## What the catalog contains

| What | Count | Where |
|---|---|---|
| Tasks | 103 | [Tasks](tasks/index.md) |
| Paradigm families the tasks are filed under | 18 | [Tasks](tasks/index.md) |
| Named task variations | 772 | on each task page |
| Cognitive processes | 172 | [Cognitive processes](processes/index.md) |
| Process categories | 19 | [Cognitive processes](processes/index.md) |
| Task-to-process links | 486 | [Task-process links](crossref.md) |
| Processes engaged by at least one task | 152 | [Task-process links](crossref.md) |

## Where to begin

::::{grid} 2
:gutter: 3

:::{grid-item-card} Browse the tasks
:link: tasks/index
:link-type: doc

103 tasks in 18 paradigm families, each with its inclusion test,
variations, processes and references.
:::

:::{grid-item-card} Browse the cognitive processes
:link: processes/index
:link-type: doc

172 processes in 19 categories, each with a definition, references
and the tasks that engage it.
:::

:::{grid-item-card} Read how tasks and processes were chosen
:link: methods/task_criteria
:link-type: doc

The selection criteria, naming rules, inclusion test and the rules that decide what
counts as a variation.
:::

:::{grid-item-card} Compare with the Cognitive Atlas
:link: atlas/relationship
:link-type: doc

What the Atlas contains, how this catalog maps onto it entry by entry, and what each
adds to the other.
:::

::::

New to the catalog? Start with the [introduction](introduction.md). Planning to tag a
dataset or to read a task page closely? See [how to use the catalog](how_to_use.md).

## Status and how to contribute

This catalog is a work in progress and its curation is a continuing process, not a
finished product. The task and process lists began from the
[Cognitive Atlas](https://www.cognitiveatlas.org/), were narrowed to paradigms that produce event-structured
data, and have been added to, merged and redefined since. Tasks, processes, categories
and paradigm families will keep changing as the catalog is used.

Suggestions, corrections and ideas are welcome: please open an issue at
<https://github.com/hed-standard/hed-task/issues>. The repository's [contributing guide](https://github.com/hed-standard/hed-task/blob/main/CONTRIBUTING.md) describes the
process. A proposal for a new task is most useful when it comes with a procedure,
a manipulation and a measurement in the form the inclusion tests use; a proposal for a
new process is most useful when it says when in a trial the process happens, what
elicits it and how it is measured.

```{toctree}
:hidden:
:caption: Overview

introduction
how_to_use
```

```{toctree}
:hidden:
:caption: Catalog

tasks/index
processes/index
Task-process links <crossref>
```

```{toctree}
:hidden:
:caption: Methods

methods/task_criteria
methods/process_criteria
methods/atlas_mapping
```

```{toctree}
:hidden:
:caption: Cognitive Atlas

atlas/cognitive_atlas
atlas/relationship
atlas/task_mapping
atlas/process_mapping
```
