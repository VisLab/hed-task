(hedtsk_sternberg_item_recognition)=
# Sternberg Item Recognition Task

**HED task ID:** `hedtsk_sternberg_item_recognition`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** Sternberg Memory Scanning, Memory Search Task

Short memory set followed by a probe; yes/no judgment of set membership. RT typically scales linearly with set size.

## Description

The Sternberg task measures the speed of short-term memory scanning. On each trial, participants encode a brief study list of 1-6 items, then after a retention interval, judge whether a test probe was in the studied list. The critical finding is that RT increases linearly with memory set size for both positive and negative probes, suggesting serial exhaustive scanning. The slope of the RT-by-set-size function indexes memory scanning speed, while the intercept indexes stimulus encoding and response execution time.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **How long is it held?** <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-old-new">old new</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-set-size">set size</a>, <a href="vocabulary.html#setting-stimulus-intensity">stimulus intensity</a>
- **Material:** A memory set of 1-6 digits or letters followed by a single probe item.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants memorize a small set of items (1-6 digits or letters), then a probe appears and they indicate whether it was in the memory set.
* - **Manipulations**
  - - Set size (1-6)
    - Probe type (positive/present vs. negative/absent)
    - Degraded probes
    - Varied vs. fixed set across trials
* - **Measurements**
  - - RT as a function of set size (slope = scanning rate, ~38 ms/item)
    - Intercept
    - Accuracy
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
* - Auditory Sternberg

    `hedvar_sternberg_item_recognition__auditory_sternberg`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The set and the probe are spoken through headphones instead of displayed.
* - Cross-Modal Sternberg

    `hedvar_sternberg_item_recognition__cross_modal_sternberg`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The set is presented in one modality and the probe in the other, so the match is made on identity rather than on the item's look or sound.
* - Sternberg with Irrelevant Items

    `hedvar_sternberg_item_recognition__sternberg_with_irrelevant_items`
  - study instruction: <a href="vocabulary.html#rule-study-then-test-study-instruction-remember-or-forget-by-cue">remember or forget by cue</a>; interval filler: <a href="vocabulary.html#rule-study-then-test-interval-filler-interference-list">interference list</a>
  - [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
  - Some set items are cued as not to be remembered, or extra items are shown during the delay, and some probes match these, so one or both of the study instruction and the interval filler change.
* - Recent-Probes Sternberg

    `hedvar_sternberg_item_recognition__recent_probes_sternberg`

    Cognitive Atlas: [Sternberg Recent Probes](https://www.cognitiveatlas.org/task/id/trm_56674987c8f0c)
  - named form
  - [Proactive interference](../processes/long_term_memory.md#hed-proactive-interference)
  - Some negative probes were members of the previous trial's set, so rejecting them is slower; a negative-probe subtype rather than a change in structure.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
- [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Sternberg, S. (1966). High-speed scanning in human memory. *Science*, 153(3736), 652-654. ([DOI](https://doi.org/10.1126/science.153.3736.652), [PubMed](https://pubmed.ncbi.nlm.nih.gov/5939936/))
- Sternberg, S. (1969). Memory-scanning: Mental processes revealed by reaction-time experiments. *American Scientist*, 57(4), 421-457.

## Further references

- Donkin, C., & Nosofsky, R. M. (2012). A power-law model of psychological memory strength in short-term and long-term recognition. *Psychological Science*, 23(6), 625-634. ([DOI](https://doi.org/10.1177/0956797611430961), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22527527/))
- Van Vugt, M. K., Schulze-Bonhage, A., Litt, B., Brandt, A., & Kahana, M. J. (2010). Hippocampal gamma oscillations increase with memory load. *Journal of Neuroscience*, 30(7), 2694-2699. ([DOI](https://doi.org/10.1523/jneurosci.0567-09.2010), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20164353/))
- Oberauer, K., Lewandowsky, S., Awh, E., Brown, G. D., Conway, A., et al. (2018). Benchmarks for models of short-term and working memory. *Psychological Bulletin*, 144(9), 885-958. ([DOI](https://doi.org/10.1037/bul0000153), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30148379/))

## External links

- Cognitive Atlas: [Sternberg Item Recognition Task](https://www.cognitiveatlas.org/task/id/trm_551f0a8b5ba2c)

- CogPO: [Sternberg Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Sternberg_Task_Paradigm)

