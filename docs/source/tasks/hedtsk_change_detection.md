(hedtsk_change_detection)=
# Change Detection Task

**HED task ID:** `hedtsk_change_detection`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** Luck-Vogel Task, VWM Capacity Task

Brief sample array followed after a blank delay by a probe array; participant reports whether any item changed. Yields visual working memory capacity (K).

## Description

The Change Detection Task, developed by Luck and Vogel (1997), is the standard paradigm for measuring visual working memory capacity. Participants briefly view a memory array of colored squares (typically 100–500 ms), followed by a blank retention interval (~900 ms), then a test array. On half the trials, one item changes color; participants report whether a change occurred. Performance is converted to a capacity estimate (K) using Cowan's formula: K = set size × (hit rate − false alarm rate). The task established that visual WM capacity is approximately 3–4 items in healthy adults and has been instrumental in research linking WM capacity to attention, intelligence, and neural oscillations.

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
* - **Measurements**
  - - Accuracy converted to capacity estimate K (Cowan's K or Pashler's K)
    - RT
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
* - Standard Color Change Detection

    `hedvar_change_detection__standard_color_change_detection`
  - A few colored squares appear briefly, the screen goes blank for about a second, and the squares reappear. On half the trials one square has changed color. The participant reports whether anything changed. Accuracy at different numbers of squares gives an estimate of how many items can be held in mind.
  - Canonical flicker paradigm: colored squares change across blank; whole/partial report
* - Single-Probe Change Detection

    `hedvar_change_detection__single_probe_change_detection`
  - After the blank interval only one square reappears, at one of the original locations, and the participant reports whether that one square is the same or different. This removes the need to compare the whole display.
  - Post-array probe tests one item; different response structure from whole-display report
* - Orientation Change Detection

    `hedvar_change_detection__orientation_change_detection`
  - The items are tilted bars rather than colored squares, and a change is a bar rotating to a new angle. Everything else is as in the color version.
  - Orientation feature instead of color; different perceptual dimension
* - Conjunction Change Detection

    `hedvar_change_detection__conjunction_change_detection`
  - Each item has two features, such as a color and an orientation, and a change can swap features between items or alter one feature. The participant must remember which color went with which orientation, not just which features were present.
  - Conjunctions of features can change; higher-order binding demand
* - Change Detection with Filtering

    `hedvar_change_detection__change_detection_with_filtering`
  - The display includes items the participant is told to ignore (for example, remember only the red bars, not the blue ones). Memory for the relevant items is then compared with a display that had no distractors, measuring how well the irrelevant items were kept out.
  - Some items task-relevant, others to be ignored; adds selective attention demand
* - Continuous Report / Precision Task

    `hedvar_change_detection__continuous_report_precision`
  - Instead of a same-or-different answer, one location is probed and the participant reproduces the remembered feature exactly, for example by clicking the remembered color on a color wheel. The spread of errors measures how precise each memory is.
  - Participant reports exact remembered value on continuous wheel; different response format
* - Sequential Presentation

    `hedvar_change_detection__sequential_presentation`
  - The items are shown one after another rather than all at the same time, and the test display follows the last item. Memory must be built up serially instead of from a single glance.
  - Items presented serially before test; different encoding structure
```

## Cognitive processes

This task is designed to engage the following processes:

- [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Encoding](../processes/long_term_memory.md#hed-encoding)

## Key references

- Luck, S. J., & Vogel, E. K. (1997). The capacity of visual working memory for features and conjunctions. *Nature*, 390(6657), 279–281. ([DOI](https://doi.org/10.1038/36846), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9384378/))
- Cowan, N. (2001). The magical number 4 in short-term memory: A reconsideration of mental storage capacity. *Behavioral and Brain Sciences*, 24(1), 87–114. ([DOI](https://doi.org/10.1017/s0140525x01003922), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11515286/))
- Vogel, E. K., & Machizawa, M. G. (2004). Neural activity predicts individual differences in visual working memory capacity. *Nature*, 428(6984), 748–751. ([DOI](https://doi.org/10.1038/nature02447), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15085132/))

## Further references

- Luck, S. J., & Vogel, E. K. (2013). Visual working memory capacity: From psychophysics and neurobiology to individual differences. *Trends in Cognitive Sciences*, 17(8), 391–400. ([DOI](https://doi.org/10.1016/j.tics.2013.06.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23850263/))
- Adam, K. C. S., Mance, I., Fukuda, K., & Vogel, E. K. (2015). The contribution of attentional lapses to individual differences in visual working memory capacity. *Journal of Cognitive Neuroscience*, 27(8), 1601–1616. ([DOI](https://doi.org/10.1162/jocn_a_00811), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25811710/))
- Luria, R., Balaban, H., Awh, E., & Vogel, E. K. (2016). The contralateral delay activity as a neural measure of visual working memory. *Neuroscience & Biobehavioral Reviews*, 62, 100–108. ([DOI](https://doi.org/10.1016/j.neubiorev.2016.01.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26802451/))
- Ma, W. J., Husain, M., & Bays, P. M. (2014). Changing concepts of working memory. *Nature Neuroscience*, 17(3), 347–356. ([DOI](https://doi.org/10.1038/nn.3655), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24569831/))

## External links

- Cognitive Atlas: [Change Detection Task](https://www.cognitiveatlas.org/task/id/trm_5154906cbead5)

