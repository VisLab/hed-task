(hedtsk_take_questionnaire)=
# Take Questionnaire Task

**HED task ID:** `hedtsk_take_questionnaire`

**Family:** [Self-report tasks](families/self_report.md)

**Also known as:** Questionnaire Block, Questionnaire Administration, Self-Report Block, Survey

Participant reads or hears a series of questionnaire items and records a response to each; the instrument administered is a parameter of the block, not a variation.

## Description

A self-report instrument is administered as a block of the session, before, between or after task blocks. Items are presented on paper, on screen or read aloud, and the participant answers each in the instrument's response format. There is no time pressure and no stimulus other than the items themselves. The Catalog does not list instruments as tasks; answering one is this task, and which instrument was used is a parameter of it. Each item is a stimulus and each answer a response, but no answer is correct. To answer, the participant reads and understands the item, recalls what is relevant from their own experience, judges how it applies to them, and picks the response option that fits. A computerized administration records when each item was shown and answered.

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
  - Each item appears on a screen and the participant answers by key press, mouse click or touch. The time at which each item was shown and answered is recorded.
  - Different response modality and one recorded event per item
* - Interviewer-Administered Questionnaire

    `hedvar_take_questionnaire__interviewer_administered_questionnaire`
  - An interviewer reads each item aloud and the participant answers in speech, with the interviewer recording the answers.
  - Different sensory and response modality
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

