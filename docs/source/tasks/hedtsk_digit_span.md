(hedtsk_digit_span)=
# Digit Span Task

**HED task ID:** `hedtsk_digit_span`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** DS, Forward/Backward Span, Digit Span

Auditory or visual digit sequences reproduced in forward or backward order; longest correctly reproduced length indexes verbal short-term and working memory span.

## Description

The Digit Span task measures verbal short-term and working memory capacity. In the Forward condition, participants listen to sequences of digits presented at a rate of one per second and immediately repeat them in the same order; sequence length increases until recall fails. In the Backward condition, participants repeat digits in reverse order, adding a manipulation component. The Sequencing condition (from WAIS-IV) requires reordering digits numerically. Digit Span is one of the oldest and most widely administered neuropsychological measures, embedded in the Wechsler intelligence and memory scales. Forward span primarily indexes the phonological loop, while backward span engages central executive processes.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **What is studied?** <a href="vocabulary.html#rule-study-then-test-studied-material-sequence-order">sequence order</a>
- **How long is it held?** <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-serial-recall">serial recall</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-examiner">examiner</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-list-length">list length</a>
- **Material:** Spoken sequences of digits, one per second, growing longer until recall fails.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Sequences of digits are presented at a rate of one per second.
    2. Participants reproduce the sequence in forward, backward, or sequencing order.
    3. Length increases until two consecutive failures.
* - **Manipulations**
  - - Direction (forward, backward, sequencing)
    - Sequence length
    - Presentation modality (auditory vs. visual)
    - Task instruction (keep only the most recent items vs. report all)
    - List presentation (grouped by pauses vs. even pace)
    - Stimulus type (spatial grid sequence vs. digits)
* - **Measurements**
  - - Span (longest correct sequence)
    - Total score
    - Forward-backward difference as index of executive load
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
* - Letter-Number Sequencing

    `hedvar_digit_span__letter_number_sequencing`

    Cognitive Atlas: [letter number sequencing](https://www.cognitiveatlas.org/task/id/trm_4c3e0a9576c3b)
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - -
  - The list mixes letters and digits and the participant reports the digits in ascending order then the letters in alphabetical order, the sequencing direction applied twice to one list.
* - Auditory vs. Visual Presentation

    `hedvar_digit_span__auditory_vs_visual_presentation`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - The digits are shown one at a time on a screen instead of being spoken, and are said or typed back.
* - Adaptive Staircase Versions

    `hedvar_digit_span__adaptive_staircase_versions`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - -
  - A computer sets each list length from recent accuracy instead of running the fixed ascending series, and span is read from where performance settles.
* - Spatial Digit Span

    `hedvar_digit_span__spatial_digit_span`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>; studied material: <a href="vocabulary.html#rule-study-then-test-studied-material-items-with-context">items with context</a>
  - [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory), [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - Each digit appears at a different screen position and the participant reproduces the digits in order, sometimes also reporting where each one appeared, which binds a location to each item.
* - Running Digit Span

    `hedvar_digit_span__running_digit_span`
  - named form
  - [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating)
  - Lists stop at an unpredictable point and only the last few digits are reported, so the participant keeps only the most recent items and drops older ones as new ones arrive.
* - Matrix Span

    `hedvar_digit_span__matrix_span`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>
  - [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory), [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - A sequence of cells lights up in a grid and the participant indicates the cells in the order shown, a spatial counterpart of digit span.
* - Supra-Span Lists

    `hedvar_digit_span__supra_span_lists`

    Cognitive Atlas: [span/supra-span test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949de3) (close match)
  - cycles: <a href="vocabulary.html#rule-study-then-test-cycles-learn-to-criterion">learn to criterion</a>
  - -
  - One list longer than span is repeated until recalled perfectly, so the study-test cycle repeats to a criterion and the number of repetitions is the score.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory)
- [Rehearsal](../processes/short_term_and_working_memory.md#hed-rehearsal)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Manipulation](../processes/short_term_and_working_memory.md#hed-manipulation)
- [Chunking](../processes/short_term_and_working_memory.md#hed-chunking)

## Key references

- Baddeley, A. D. (1986). *Working Memory*. Oxford University Press. ([DOI](https://doi.org/10.1016/s0166-4115(08)61202-9))
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81-97. ([DOI](https://doi.org/10.1037/h0043158), [PubMed](https://pubmed.ncbi.nlm.nih.gov/13310704/))

## Further references

- Woods, D. L., Kishiyama, M. M., Yund, E. W., Herron, T. J., Edwards, B., Poliva, O., ... & Reed, B. (2011). Improving digit span assessment of short-term verbal memory. *Journal of Clinical and Experimental Neuropsychology*, 33(1), 101-111. ([DOI](https://doi.org/10.1080/13803395.2010.493149))

## External links

- Cognitive Atlas: [digit span task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949a0d)

