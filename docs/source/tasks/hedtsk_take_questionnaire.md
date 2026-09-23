(hedtsk_take_questionnaire)=
# Take Questionnaire Task

**HED task ID:** `hedtsk_take_questionnaire`

**Family:** [Pseudo tasks: rest, fixation, self-report and feedback blocks](families/pseudo_tasks.md)

:::{note}
**Pseudo task.** A block that establishes or holds a state, collects a self-report or
delivers feedback, rather than eliciting a cognitive process through a trial structure. It is in the Catalog
so that such blocks can be labelled with the same vocabulary as the tasks around them.
See [Pseudo tasks](../methods/task_criteria/01_task_selection_criteria.md#task-criteria-1-3) in the task criteria.
:::

**Also known as:** Questionnaire Block, Questionnaire Administration, Self-Report Block, Survey

Participant reads or hears a series of questionnaire items and records a response to each; the instrument administered is a parameter of the block, not a variation.

## Description

A self-report instrument is administered as a block of the session, before, between or after task blocks. Items are presented on paper, on screen or read aloud, and the participant answers each in the instrument's response format. There is no time pressure and no stimulus other than the items themselves. The Catalog does not list instruments as tasks; it records the administration as a block so that the time spent on it, and any physiology recorded during it, can be labelled, and it records which instrument was used as a parameter of the block. Take Questionnaire is a pseudo task: it collects a self-report rather than eliciting a process, so it carries no process links.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participant reads or hears each item of a questionnaire and records a response to it, in the instrument's format, with no time pressure.
* - **Manipulations**
  - - The instrument administered (a parameter, not a variation)
    - Administration mode (paper, computerized, interviewer-read)
    - Response format (Likert, forced choice, free text)
    - Position relative to task blocks
* - **Measurements**
  - - Item responses and derived scale scores
    - Per-item response times when computerized
    - Physiological recording during completion is incidental
```

## Variations

Named versions that change what the participant experiences or does. The identifier
of a variation is `hedvar_<task>__<variation>`.

```{list-table}
:widths: 25 40 35
:header-rows: 1

* - Variation
  - Description
  - Justification
* - Computerized Questionnaire

    `hedvar_take_questionnaire__computerized_questionnaire`
  - Items on screen, responses by key or mouse, item timing recorded.
  - Different response modality and one recorded event per item
* - Interviewer-Administered Questionnaire

    `hedvar_take_questionnaire__interviewer_administered_questionnaire`
  - Items read aloud by an interviewer and answered verbally.
  - Different sensory and response modality
```

## Cognitive processes

No process links have been recorded for this pseudo task. That is a gap in the Catalog, not a
claim that the block engages no process: a pseudo task is not run to probe a process, and the
processes it does engage have not yet been linked.

## Further references

- Bowling, A. (2005). Mode of questionnaire administration can have serious effects on data quality. *Journal of Public Health*, 27(3), 281-291. ([DOI](https://doi.org/10.1093/pubmed/fdi031))

