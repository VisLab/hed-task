(hedtsk_take_questionnaire)=
# Take Questionnaire Task

**HED task ID:** `hedtsk_take_questionnaire`

**Family:** [Self-report tasks](families/self_report.md)

**Also known as:** Questionnaire Block, Questionnaire Administration, Self-Report Block, Survey

Participant reads or hears a series of questionnaire items and records a response to each; the instrument administered is a parameter of the block, not a variant.

## Description

A self-report instrument is administered as a block of the session, before, between or after task blocks. Items are presented on paper, on screen or read aloud, and the participant answers each in the instrument's response format. There is no time pressure and no stimulus other than the items themselves. The Catalog does not list instruments as tasks; answering one is this task, and which instrument was used is a parameter of it. Each item is a stimulus and each answer a response, but no answer is correct. To answer, the participant reads and understands the item, recalls what is relevant from their own experience, judges how it applies to them, and picks the response option that fits. A computerized administration records when each item was shown and answered.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-report-on-self">Report on yourself</a> (`report_on_self`)
- **Game rules:** none are defined for this game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-text">text</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** The items of a self-report instrument, on paper, on screen or read aloud, with the instrument's response options.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participant reads or hears each item of a questionnaire and records a response to it, in the instrument's format, with no time pressure.
* - **Manipulations**
  - - The instrument administered (a parameter, not a variant)
    - Administration mode (paper, computerized, interviewer-read)
    - Response format (Likert, forced choice, free text)
    - Position relative to task blocks
* - **Measurements**
  - - Item responses and derived scale scores
    - Per-item response times when computerized
    - Physiological recording during completion is incidental
```

## Variants

Attested forms of the task. Each states only what differs from the standard form
above and inherits the rest; a named form differs in name only. The identifier of a
variant is `hedvar_<task>__<variant>`.

```{list-table}
:widths: 22 33 15 30
:header-rows: 1

* - Variant
  - What differs
  - Processes added
  - Note
* - Interviewer-Administered Questionnaire

    `hedvar_take_questionnaire__interviewer_administered_questionnaire`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-examiner">examiner</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - An interviewer reads each item aloud and the participant answers in speech, the interviewer recording the answers.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Sentence comprehension](../processes/language_comprehension_and_production.md#hed-sentence-comprehension)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Autobiographical memory](../processes/long_term_memory.md#hed-autobiographical-memory)
- [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Further references

- Bowling, A. (2005). Mode of questionnaire administration can have serious effects on data quality. *Journal of Public Health*, 27(3), 281-291. ([DOI](https://doi.org/10.1093/pubmed/fdi031))
- Tourangeau, R., Rips, L. J., & Rasinski, K. (2000). *The psychology of survey response*. Cambridge University Press. ([DOI](https://doi.org/10.1017/CBO9780511819322))

