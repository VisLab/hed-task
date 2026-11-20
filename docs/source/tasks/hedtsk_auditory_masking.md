(hedtsk_auditory_masking)=
# Auditory Masking Task

**HED task ID:** `hedtsk_auditory_masking`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** Tone-in-Noise Detection, Speech-in-Noise, Energetic Masking

Detect, discriminate, or identify a target sound in the presence of a masking sound; threshold shifts between masked and unmasked conditions index frequency selectivity, temporal resolution, and auditory scene analysis.

## Description

A target sound (tone, speech token, or noise burst) is presented alongside, before, or after a masking sound, and participants detect, discriminate, or identify the target. By varying the temporal and spectral relationship between target and masker, the paradigm dissociates peripheral (energetic) masking - where masker and target excite overlapping auditory filters - from central (informational) masking - where the masker is spectrally remote but introduces perceptual uncertainty. Threshold shifts, psychometric functions, and comodulation masking release are the core dependent measures. The paradigm is foundational to auditory psychophysics and clinical audiology, and maps onto distinct subcortical and cortical processing stages.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What does the rule ask about each stimulus?** <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
- **What competes with the correct response?** <a href="vocabulary.html#rule-respond-to-rule-competitor-noise-or-mask">noise or mask</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-noise">noise</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-spatial-separation">spatial separation</a>, <a href="vocabulary.html#setting-stimulus-similarity">stimulus similarity</a>
- **Material:** A target sound (a tone, a speech token or a noise burst) presented with, before or after a masker of noise, tones, speech or modulated sound.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A target sound is presented alongside, before, or after a masker.
    2. Participants detect, discriminate, or identify the target.
* - **Manipulations**
  - - Temporal relation (simultaneous, forward, backward)
    - Spectral overlap between target and masker
    - Masker type (noise, tones, speech, modulated)
    - Spatial separation
* - **Measurements**
  - - Detection threshold (masked vs. unmasked)
    - Threshold shift
    - Psychometric function slope
    - Speech reception threshold in noise
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
* - Speech-in-noise

    `hedvar_auditory_masking__speech_in_noise`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-text">text</a>, <a href="vocabulary.html#facet-stimulus-type-noise">noise</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-identify">identify</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The target is spoken words or sentences and the participant repeats or identifies what was said rather than reporting presence.
* - Spatial release from masking

    `hedvar_auditory_masking__spatial_release_from_masking`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-loudspeaker">loudspeaker</a>
  - -
  - Target and masker are played from different directions and the threshold is compared with the co-located case.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
- [Masking](../processes/awareness_agency_and_metacognition.md#hed-masking)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Perceptual decision making](../processes/perceptual_decision_making_evidence_accumulation.md#hed-perceptual-decision-making)

## Key references

- Moore, B. C. J. (2012). An Introduction to the Psychology of Hearing (6th ed.). Brill. ([DOI](https://doi.org/10.1007/978-0-230-36409-7_1))

## Further references

- Shinn-Cunningham, B. G. (2008). Object-based auditory and visual attention. Trends in Cognitive Sciences, 12(5), 182-186. ([DOI](https://doi.org/10.1016/j.tics.2008.02.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18396091/))

## External links

- Cognitive Atlas: [auditory masking task](https://www.cognitiveatlas.org/task/id/trm_551b1b6f6a262)

