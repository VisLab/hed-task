(hedtsk_corsi_block_tapping)=
# Corsi Block-Tapping Task

**HED task ID:** `hedtsk_corsi_block_tapping`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** Corsi, Block Tapping, Corsi Span

Experimenter taps a sequence on spatially arranged blocks; participant reproduces the sequence forward or backward. Indexes visuospatial short-term and working memory span.

## Description

The Corsi Block-Tapping Task measures visuospatial short-term and working memory. Nine blocks are arranged irregularly on a board (or screen). The examiner taps a sequence of blocks, and the participant reproduces the sequence. Sequence length increases from 2 blocks upward until the participant fails two consecutive sequences at a given length. The maximum reliably reproduced length defines the Corsi span, typically around 5-6 for healthy adults. The backward version requires reproducing sequences in reverse order, adding executive demands. The task is the spatial counterpart of Digit Span and is critical for understanding the visuospatial sketchpad component of working memory.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **What is studied?** <a href="vocabulary.html#rule-study-then-test-studied-material-sequence-order">sequence order</a>
- **How long is it held?** <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-serial-recall">serial recall</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-examiner">examiner</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-list-length">list length</a>
- **Material:** Nine blocks arranged irregularly on a board or screen, tapped in sequences of increasing length.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. The experimenter (or computer) taps a sequence of blocks on a board.
    2. The participant reproduces the sequence in the same (or reverse) order.
    3. Sequence length increases until recall fails.
* - **Manipulations**
  - - Sequence length
    - Forward vs. backward reproduction
    - Block spatial arrangement
* - **Measurements**
  - - Span (longest sequence correctly recalled)
    - Total score across trials
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
* - Computerized (eCorsi)

    `hedvar_corsi_block_tapping__computerized_ecorsi`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-touchscreen">touchscreen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>
  - -
  - Squares on a screen light up in sequence and are touched or clicked in order, with each touch timed.
* - Supra-Span Corsi

    `hedvar_corsi_block_tapping__supra_span_corsi`
  - cycles: <a href="vocabulary.html#rule-study-then-test-cycles-learn-to-criterion">learn to criterion</a>
  - -
  - One sequence longer than span is presented repeatedly until it is reproduced correctly, and the number of attempts is the score.
* - Walking Corsi (large-scale)

    `hedvar_corsi_block_tapping__walking_corsi_large_scale`
  - named form
  - -
  - The blocks become tiles on the floor of a room, the examiner walks a route over them and the participant walks the same route.
* - Sequential vs. Simultaneous Presentation

    `hedvar_corsi_block_tapping__sequential_vs_simultaneous_presentation`
  - named form
  - -
  - In the simultaneous condition all blocks of a set are highlighted at once with numbers or arrows giving the order, instead of being tapped one after another, and the participant still reproduces them in order.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory)
- [Manipulation](../processes/short_term_and_working_memory.md#hed-manipulation)

## Key references

- Corsi, P. M. (1972). *Human memory and the medial temporal region of the brain*. Unpublished doctoral dissertation, McGill University.
- Milner, B. (1971). Interhemispheric differences in the localization of psychological processes in man. *British Medical Bulletin*, 27(3), 272-277. ([DOI](https://doi.org/10.1093/oxfordjournals.bmb.a070866), [PubMed](https://pubmed.ncbi.nlm.nih.gov/4937273/))

## Further references

- Pagulayan, K. F., Busch, R. M., Medina, K. L., Bartok, J. A., & Krikorian, R. (2006). Developmental normative data for the Corsi Block-Tapping Task. *Journal of Clinical and Experimental Neuropsychology*, 28(6), 1043-1052. ([DOI](https://doi.org/10.1080/13803390500350977), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16822742/))
- Brunetti, R., Del Gatto, C., & Delogu, F. (2014). eCorsi: Implementation and testing of the Corsi Block-Tapping Task for digital tablets. *Frontiers in Psychology*, 5, 939. ([DOI](https://doi.org/10.3389/fpsyg.2014.00939), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25228888/))

## External links

- Cognitive Atlas: [Corsi Blocks](https://www.cognitiveatlas.org/task/id/trm_4da881dace79c)

