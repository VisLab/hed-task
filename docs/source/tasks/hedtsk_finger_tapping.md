(hedtsk_finger_tapping)=
# Finger Tapping Task

**HED task ID:** `hedtsk_finger_tapping`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** FTT, Tapping Task, Finger Tapping

Repetitive single-finger or sequence tapping at fastest or paced rates; taps-per-interval and tap-timing variability index motor speed and rhythm control.

## Description

Participants tap their fingers (typically index finger) in a repetitive manner at a self-paced or externally paced rate. Self-paced tapping is typically at 2-3 Hz; externally paced versions use an auditory or visual metronome. The task consists of tapping blocks (20-40 seconds) alternating with rest periods. Performance metrics include tapping frequency, inter-tap interval variability, and accuracy. It is the most commonly used simple motor paradigm for motor cortex mapping, clinical motor assessment, and studying motor control. Contralateral primary motor cortex and supplementary motor area are consistently activated.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-produce-movement">Make a movement</a> (`produce_movement`)
- **Game rules:** none are defined for this game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructed-emphasis">instructed emphasis</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-block-duration">block duration</a>, <a href="vocabulary.html#setting-presentation-rate">presentation rate</a>
- **Material:** A metronome beat (a tone or a light) to tap in time with, in the paced form; the self-paced form presents nothing.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants tap a key or button with a single finger as rapidly as possible (maximum rate) or in synchrony with a metronome (paced tapping).
* - **Manipulations**
  - - Hand (dominant vs. non-dominant)
    - Pacing rate
    - Tapping duration
    - Sequence complexity (single finger vs. sequence)
    - Tapping pattern (unequal rhythm vs. even beat)
* - **Measurements**
  - - Tapping rate (taps/sec)
    - Inter-tap interval variability
    - Synchronization error and drift in paced conditions
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
* - Auditorily-Paced Tapping

    `hedvar_finger_tapping__auditorily_paced_tapping`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-clicks">clicks</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - The participant taps in time with a metronome click, so pacing is external.
* - Visually-Paced Tapping

    `hedvar_finger_tapping__visually_paced_tapping`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>
  - [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - The pacing signal is a flashing shape on a screen instead of a sound.
* - Unimanual vs. Bimanual

    `hedvar_finger_tapping__unimanual_vs_bimanual`
  - named form
  - -
  - Both hands tap at once, in unison or alternating, instead of one hand.
* - Sequential Multi-Finger

    `hedvar_finger_tapping__sequential_multi_finger`
  - named form
  - [Motor sequence learning](../processes/motor_preparation_timing_and_execution.md#hed-motor-sequence-learning)
  - A fixed order of fingers is tapped over and over instead of one finger repeating.
* - Complex Rhythmic Patterns

    `hedvar_finger_tapping__complex_rhythmic_patterns`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-clicks">clicks</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - One finger reproduces a rhythm with unequal intervals (long-short-short) rather than tapping an even beat.
* - Continuation Paradigm

    `hedvar_finger_tapping__continuation_paradigm`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-clicks">clicks</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - The participant taps along with a metronome, then keeps the same rate unaided after it stops.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Fine motor control](../processes/motor_preparation_timing_and_execution.md#hed-fine-motor-control)
- [Motor timing](../processes/motor_preparation_timing_and_execution.md#hed-motor-timing)
- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)
- [Motor preparation](../processes/motor_preparation_timing_and_execution.md#hed-motor-preparation)

## Key references

- Witt, S. T., Laird, A. R., & Meyerand, M. E. (2008). Functional neuroimaging correlates of finger-tapping task variations: An ALE meta-analysis. *NeuroImage*, 42(1), 343-356. ([DOI](https://doi.org/10.1016/j.neuroimage.2008.04.025), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18511305/))
- Rao, S. M., Harrington, D. L., Haaland, K. Y., et al. (1997). Distributed neural systems underlying the timing of movements. *Journal of Neuroscience*, 17(14), 5528-5535. ([DOI](https://doi.org/10.1523/jneurosci.17-14-05528.1997), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9204934/))
- Jancke, L., Loose, R., Lutz, K., Specht, K., & Shah, N. J. (2000). Cortical activations during paced finger-tapping applying visual and auditory pacing stimuli. *Cognitive Brain Research*, 10(1-2), 51-66. ([DOI](https://doi.org/10.1016/s0926-6410(00)00022-7), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10978692/))

## Further references

- Haaland, K. Y., Elsinger, C. L., Mayer, A. R., Durgerian, S., & Rao, S. M. (2004). Motor sequence complexity and performing hand produce differential patterns of hemispheric lateralization. *Journal of Cognitive Neuroscience*, 16(4), 621-636. ([DOI](https://doi.org/10.1162/089892904323057344), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15165352/))

## External links

- Cognitive Atlas: [finger tapping task](https://www.cognitiveatlas.org/task/id/trm_4c898f079d05e)

- CogPO: [Finger Tapping Paradigm](http://www.wiki.cogpo.org/index.php?title=Finger_Tapping_Paradigm)

