(hedtsk_mnemonic_similarity)=
# Mnemonic Similarity Task

**HED task ID:** `hedtsk_mnemonic_similarity`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** MST, Mnemonic Discrimination Task, Pattern Separation Task, Mnemonic Similarity

Incidental encoding of images followed by a test with old, new, and lure items; discrimination of lures from repetitions indexes pattern separation.

## Description

The Mnemonic Similarity Task measures hippocampal pattern separation - the ability to distinguish similar but not identical memory representations. During encoding, participants view a series of everyday object images. At test, they classify each image as "old" (previously seen), "similar" (a different exemplar of a studied object with slight visual changes), or "new" (novel). The critical measure is the ability to correctly identify "similar" lures as similar rather than incorrectly endorsing them as old. This discrimination (lure discrimination index) is thought to rely on dentate gyrus/CA3 pattern separation processes and is impaired in early-stage Alzheimer's disease and normal aging.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **What does the player do while studying?** <a href="vocabulary.html#rule-study-then-test-study-job-incidental-judgment">incidental judgment</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-list-length">list length</a>, <a href="vocabulary.html#setting-retention-interval">retention interval</a>, <a href="vocabulary.html#setting-stimulus-similarity">stimulus similarity</a>
- **Material:** Pictures of everyday objects, and at test the same objects, new objects and similar lures that differ slightly.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants study a set of images, then view old items, new items, and similar lures (items resembling studied items).
    2. They classify each as old, new, or similar.
* - **Manipulations**
  - - Lure similarity (mnemonic similarity parameter)
    - Encoding depth
    - Retention interval
    - Number of items
    - Stimulus type (objects, scenes, faces)
    - Study and test structure (continuous vs. separate phases)
    - Judged attribute (item location vs. item identity)
* - **Measurements**
  - - Lure discrimination index (LDI: p('similar'|lure) - p('similar'|foil))
    - Recognition d-prime
    - Pattern separation score
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
* - Scene MST

    `hedvar_mnemonic_similarity__scene_mst`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>
  - -
  - Indoor and outdoor scenes replace single objects, with lures being slightly altered versions of studied scenes.
* - Continuous MST

    `hedvar_mnemonic_similarity__continuous_mst`
  - study and test: <a href="vocabulary.html#rule-study-then-test-study-and-test-merged">merged</a>; retention interval: <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
  - -
  - Study and test are merged into one stream in which each picture is judged old, similar or new as it appears.
* - MST for Faces

    `hedvar_mnemonic_similarity__mst_for_faces`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
  - Faces replace objects, with lures being similar faces or the same face with one feature changed.
* - Spatial MST

    `hedvar_mnemonic_similarity__spatial_mst`
  - studied material: <a href="vocabulary.html#rule-study-then-test-studied-material-items-with-context">items with context</a>
  - [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory)
  - Objects are studied at screen locations and the test asks whether the location is the same, slightly shifted or new, so what is studied and judged is the item-location pairing rather than the item.
* - Short-Delay vs. Long-Delay MST

    `hedvar_mnemonic_similarity__short_delay_vs_long_delay_mst`
  - retention interval: <a href="vocabulary.html#rule-study-then-test-retention-interval-hours-or-days">hours or days</a>
  - -
  - The test is given immediately in one condition and after hours or a day in another.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Pattern separation](../processes/long_term_memory.md#hed-pattern-separation)
- [Pattern completion](../processes/long_term_memory.md#hed-pattern-completion)
- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)
- [Familiarity](../processes/long_term_memory.md#hed-familiarity)

## Key references

- Kirwan, C. B., & Stark, C. E. L. (2007). Overcoming interference: An fMRI investigation of pattern separation in the medial temporal lobe. *Learning & Memory*, 14(9), 625-633. ([DOI](https://doi.org/10.1101/lm.663507), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17848502/))
- Stark, S. M., Yassa, M. A., Lacy, J. W., & Stark, C. E. L. (2013). A task to assess behavioral pattern separation (BPS) in humans: Data from healthy aging and mild cognitive impairment. *Neuropsychologia*, 51(12), 2442-2449. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2012.12.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23313292/))
- Yassa, M. A., & Stark, C. E. L. (2011). Pattern separation in the hippocampus. *Trends in Neurosciences*, 34(10), 515-525. ([DOI](https://doi.org/10.1016/j.tins.2011.06.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21788086/))

## Further references

- Lacy, J. W., Yassa, M. A., Stark, S. M., Muftuler, L. T., & Stark, C. E. L. (2011). Distinct pattern separation related transfer functions in human CA3/dentate and CA1 revealed using high-resolution fMRI and variable mnemonic similarity. *Learning & Memory*, 18(1), 15-18. ([DOI](https://doi.org/10.1101/lm.1971111))
- Bakker, A., Kirwan, C. B., Miller, M., & Stark, C. E. L. (2008). Pattern separation in the human hippocampal CA3 and dentate gyrus. *Science*, 319(5870), 1640-1642. ([DOI](https://doi.org/10.1126/science.1152882), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18356518/))
- Stark, S. M., & Stark, C. E. L. (2017). Age-related deficits in the mnemonic similarity task for objects and scenes. *Behavioural Brain Research*, 333, 109-117. ([DOI](https://doi.org/10.1016/j.bbr.2017.06.049), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28673769/))
- Reagh, Z. M., & Yassa, M. A. (2014). Object and spatial mnemonic interference differentially engage lateral and medial entorhinal cortex in humans. *Proceedings of the National Academy of Sciences*, 111(40), E4264-E4273. ([DOI](https://doi.org/10.1073/pnas.1411250111), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25246569/))

## External links

- Cognitive Atlas: [Mnemonic similarity task](https://www.cognitiveatlas.org/task/id/tsk_RXmB56vrYW66T)

