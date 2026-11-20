(hedtsk_change_detection)=
# Change Detection Task

**HED task ID:** `hedtsk_change_detection`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** Luck-Vogel Task, VWM Capacity Task

Brief sample array followed after a blank delay by a probe array; participant reports whether any item changed. Yields visual working memory capacity (K).

## Description

The Change Detection Task, developed by Luck and Vogel (1997), is the standard paradigm for measuring visual working memory capacity. Participants briefly view a memory array of colored squares (typically 100-500 ms), followed by a blank retention interval (~900 ms), then a test array. On half the trials, one item changes color; participants report whether a change occurred. Performance is converted to a capacity estimate (K) using Cowan's formula: K = set size x (hit rate - false alarm rate). The task established that visual WM capacity is approximately 3-4 items in healthy adults and has been instrumental in research linking WM capacity to attention, intelligence, and neural oscillations.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **How long is it held?** <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-same-changed">same changed</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-retention-interval">retention interval</a>, <a href="vocabulary.html#setting-set-size">set size</a>
- **Material:** Arrays of colored squares (or oriented bars) in which one item may change color between the memory array and the test array.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A brief memory array of colored squares (or oriented bars) is followed by a retention interval and a test array.
    2. Participants indicate whether a change occurred.
* - **Manipulations**
  - - Set size (number of items)
    - Retention interval
    - Number of changes
    - Feature complexity
    - Presentation format (sequential vs. simultaneous)
* - **Measurements**
  - - Accuracy converted to capacity estimate K (Cowan's K or Pashler's K)
    - RT
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
* - Single-Probe Change Detection

    `hedvar_change_detection__single_probe_change_detection`
  - named form
  - -
  - Only one square reappears at one of the original locations and the same/different judgment is about that item alone rather than the whole array.
* - Change Detection with Filtering

    `hedvar_change_detection__change_detection_with_filtering`
  - study instruction: <a href="vocabulary.html#rule-study-then-test-study-instruction-remember-or-forget-by-cue">remember or forget by cue</a>
  - -
  - The array includes items the participant is told by a feature cue to ignore (remember the red bars, not the blue), so the study instruction selects a cued subset of the array.
* - Continuous Report / Precision Task

    `hedvar_change_detection__continuous_report_precision`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>
  - -
  - One location is probed and the participant reproduces the remembered feature on a continuous scale such as a color wheel, instead of judging whether it changed; the spread of the errors measures memory precision.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Encoding](../processes/long_term_memory.md#hed-encoding)

## Key references

- Luck, S. J., & Vogel, E. K. (1997). The capacity of visual working memory for features and conjunctions. *Nature*, 390(6657), 279-281. ([DOI](https://doi.org/10.1038/36846), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9384378/))
- Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87-114. ([DOI](https://doi.org/10.1017/s0140525x01003922), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11515286/))
- Vogel, E. K., & Machizawa, M. G. (2004). Neural activity predicts individual differences in visual working memory capacity. *Nature*, 428(6984), 748-751. ([DOI](https://doi.org/10.1038/nature02447), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15085132/))

## Further references

- Luck, S. J., & Vogel, E. K. (2013). Visual working memory capacity: From psychophysics and neurobiology to individual differences. *Trends in Cognitive Sciences*, 17(8), 391-400. ([DOI](https://doi.org/10.1016/j.tics.2013.06.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23850263/))
- Adam, K. C. S., Mance, I., Fukuda, K., & Vogel, E. K. (2015). The contribution of attentional lapses to individual differences in visual working memory capacity. *Journal of Cognitive Neuroscience*, 27(8), 1601-1616. ([DOI](https://doi.org/10.1162/jocn_a_00811), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25811710/))
- Luria, R., Balaban, H., Awh, E., & Vogel, E. K. (2016). The contralateral delay activity as a neural measure of visual working memory. *Neuroscience & Biobehavioral Reviews*, 62, 100-108. ([DOI](https://doi.org/10.1016/j.neubiorev.2016.01.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26802451/))
- Ma, W. J., Husain, M., & Bays, P. M. (2014). Changing concepts of working memory. *Nature Neuroscience*, 17(3), 347-356. ([DOI](https://doi.org/10.1038/nn.3655), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24569831/))

## External links

- Cognitive Atlas: [Change Detection Task](https://www.cognitiveatlas.org/task/id/trm_5154906cbead5)

