(hedtsk_old_new_recognition_memory)=
# Old/New Recognition Memory Task

**HED task ID:** `hedtsk_old_new_recognition_memory`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** Recognition Memory Test, Yes/No Recognition

Studied items mixed with new lures at test; hit and false-alarm rates yield d' and can be decomposed into recollection and familiarity via ROC or remember/know.

## Description

Participants study a list of stimuli (words, pictures, or faces) during an encoding phase. In the test phase, they view a mixture of studied (old) and unstudied (new) items and make binary old/new recognition judgments. Performance is analyzed using signal detection measures (hits, false alarms, d') and can be further decomposed into familiarity-based (rapid, automatic) and recollection-based (slower, effortful) processes using confidence ratings or remember/know judgments. Neuroimaging consistently implicates the hippocampus, angular gyrus, and default mode network in successful recognition.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-old-new">old new</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-words">words</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-list-length">list length</a>, <a href="vocabulary.html#setting-response-deadline">response deadline</a>, <a href="vocabulary.html#setting-retention-interval">retention interval</a>
- **Material:** A studied list of words (or pictures or faces), and at test the studied items mixed with new ones.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants study a list of items, then view a test list containing studied (old) items and unstudied (new) items and classify each as old or new.
    2. Optional: Items are studied in pairs and the old/new judgment is made on pairs, with rearranged pairs of studied items as lures.
* - **Manipulations**
  - - Study list length
    - Encoding depth (levels of processing)
    - Retention interval
    - Confidence judgment
    - Response deadline
    - Study and test structure (continuous vs. separate lists)
* - **Measurements**
  - - Hit rate
    - False alarm rate
    - d-prime (discriminability)
    - Criterion (response bias)
    - Confidence ratings
    - ROC curves
    - ERP old/new effects (FN400, LPC)
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
* - Associative Recognition

    `hedvar_old_new_recognition_memory__associative_recognition`
  - studied material: <a href="vocabulary.html#rule-study-then-test-studied-material-pairs">pairs</a>
  - -
  - Items are studied in pairs and the old/new judgment is made on pairs, with rearranged pairs of studied items as lures.
* - Forced-Choice Recognition

    `hedvar_old_new_recognition_memory__forced_choice_recognition`
  - test form: <a href="vocabulary.html#rule-study-then-test-test-form-forced-choice">forced choice</a>
  - -
  - Each test trial shows a studied item beside one or more new items and the participant picks the studied one.
* - Continuous Recognition

    `hedvar_old_new_recognition_memory__continuous_recognition`

    Cognitive Atlas: [continuous recognition paradigm](https://www.cognitiveatlas.org/task/id/tsk_4a57abb9499c7)
  - study and test: <a href="vocabulary.html#rule-study-then-test-study-and-test-merged">merged</a>; retention interval: <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
  - -
  - Study and test are merged into one stream in which every item is judged new or repeated, and an item may repeat again later.
* - DRM (Deese-Roediger-McDermott) False Memory Variant

    `hedvar_old_new_recognition_memory__drm_deese_roediger_mcdermott_false_memory_variant`
  - named form
  - -
  - Each study list is built from associates of one unpresented word, and that word is placed among the test items so its false-alarm rate can be measured.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Recollection](../processes/long_term_memory.md#hed-recollection)
- [Familiarity](../processes/long_term_memory.md#hed-familiarity)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)

## Key references

- Mandler, G. (1980). Recognizing: The judgment of previous occurrence. *Psychological Review*, 87(3), 252-271. ([DOI](https://doi.org/10.1037/0033-295x.87.3.252))
- Henson, R. N., Rugg, M. D., Shallice, T., Josephs, O., & Dolan, R. J. (1999). Recollection and familiarity in recognition memory: An event-related functional magnetic resonance imaging study. *Journal of Neuroscience*, 19(10), 3962-3972. ([DOI](https://doi.org/10.1523/jneurosci.19-10-03962.1999), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10234026/))
- Rugg, M. D., & Curran, T. (2007). Event-related potentials and recognition memory. *Trends in Cognitive Sciences*, 11(6), 251-257. ([DOI](https://doi.org/10.1016/j.tics.2007.04.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17481940/))

## Further references

- Wixted, J. T. (2007). Dual-process theory and signal-detection theory of recognition memory. *Psychological Review*, 114(1), 152-176. ([DOI](https://doi.org/10.1037/0033-295x.114.1.152), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17227185/))
- Rugg, M. D., & Vilberg, K. L. (2013). Brain networks underlying episodic memory retrieval. *Current Opinion in Neurobiology*, 23(2), 255-260. ([DOI](https://doi.org/10.1016/j.conb.2012.11.005), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23206590/))
- Wixted, J. T., & Mickes, L. (2014). A signal-detection-based diagnostic-feature-detection model of eyewitness identification. *Psychological Review*, 121(4), 588-607. ([DOI](https://doi.org/10.1037/a0035940), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24730600/))

## External links

- Cognitive Atlas: [recognition memory test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949d40)

- CogPO: [Cued Explicit Recognition Paradigm](http://www.wiki.cogpo.org/index.php?title=Cued_Explicit_Recognition_Paradigm)

