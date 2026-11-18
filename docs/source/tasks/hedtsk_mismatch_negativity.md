(hedtsk_mismatch_negativity)=
# Mismatch Negativity Task

**HED task ID:** `hedtsk_mismatch_negativity`

**Family:** [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md)

**Also known as:** MMN, Mismatch Negativity Paradigm, Mismatch Negativity

Passive auditory oddball in which rare deviant sounds elicit a negative ERP around 150-250 ms, indexing pre-attentive auditory change detection.

## Description

Participants are passively exposed to repetitive acoustic stimuli (standard tones, 80%) occasionally interrupted by deviant tones (20%) differing in pitch, duration, or location. The MMN can be elicited without active attention. Recorded via EEG, the MMN appears as a negative deflection peaking at 100-250 ms after deviance onset at frontocentral sites. It reflects automatic, pre-attentive comparison between incoming input and a neural representation of the standard stimulus stored in sensory (echoic) memory. MMN is used as a biomarker of auditory processing capacity and has clinical applications in schizophrenia, coma prognosis, and language development research.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-undergo-stream">undergo stream</a>
- **What is the player told to do while it runs?** <a href="vocabulary.html#rule-undergo-stream-instruction-none">none</a>
- **Is anything asked afterwards?** <a href="vocabulary.html#rule-undergo-stream-report-after-none">none</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-interstimulus-interval">interstimulus interval</a>, <a href="vocabulary.html#setting-stimulus-similarity">stimulus similarity</a>, <a href="vocabulary.html#setting-target-probability">target probability</a>
- **Material:** A repeated standard tone occasionally replaced by a deviant tone differing in pitch, duration, intensity or location.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A repetitive standard tone is occasionally replaced by a deviant tone differing in frequency, duration, or intensity.
    2. Participants typically ignore the sounds while reading or watching a silent video.
* - **Manipulations**
  - - Deviant type (frequency, duration, intensity, phoneme, location; one or several per stream)
    - Deviant probability
    - Magnitude of deviance
    - ISI
    - Standard tone sequence (roving vs. fixed standard)
* - **Measurements**
  - - MMN amplitude and latency (deviant-minus-standard difference wave, peaking 100-250 ms)
    - Scalp topography
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
* - Location/Spatial MMN

    `hedvar_mismatch_negativity__location_spatial_mmn`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-loudspeaker">loudspeaker</a>
  - -
  - The deviant comes from a different direction, which may mean loudspeakers instead of headphones.
* - Complex Pattern MMN

    `hedvar_mismatch_negativity__complex_pattern_mmn`
  - named form
  - -
  - The regularity is a multi-tone pattern (alternation, rising pair) and the deviant breaks the pattern although every individual tone is familiar.
* - Multi-Feature MMN (Optimum)

    `hedvar_mismatch_negativity__multi_feature_mmn_optimum`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - -
  - Several deviant types alternate with the standard in one sequence so that all are collected in one short run.
* - Phoneme/Speech MMN

    `hedvar_mismatch_negativity__phoneme_speech_mmn`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-syllables">syllables</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The standard and deviant are speech syllables rather than tones.
* - Visual MMN (vMMN)

    `hedvar_mismatch_negativity__visual_mmn_vmmn`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - The ignored stream is visual, shown at the edge of the screen while an unrelated central task occupies the participant.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
- [Auditory tone discrimination](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-tone-discrimination)
- [Pitch perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-pitch-perception)
- [Acoustic processing](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-acoustic-processing)

## Key references

- Naatanen, R., Gaillard, A. W. K., & Mantysalo, S. (1978). Early selective-attention effect on evoked potential reinterpreted. *Acta Psychologica*, 42(4), 313-329. ([DOI](https://doi.org/10.1016/0001-6918(78)90006-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/685709/))
- Naatanen, R., Paavilainen, P., Rinne, T., & Alho, K. (2007). The mismatch negativity (MMN) in basic research of central auditory processing: A review. *Clinical Neurophysiology*, 118(12), 2544-2590. ([DOI](https://doi.org/10.1016/j.clinph.2007.04.026), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17931964/))
- Garrido, M. I., Kilner, J. M., Stephan, K. E., & Friston, K. J. (2009). The mismatch negativity: A review of underlying mechanisms. *Clinical Neurophysiology*, 120(3), 453-463. ([DOI](https://doi.org/10.1016/j.clinph.2008.11.029), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19181570/))

## Further references

- Näätänen, R., Kujala, T., & Winkler, I. (2011). Auditory processing that leads to conscious perception: A unique window to central auditory processing opened by the mismatch negativity and related responses. *Psychophysiology*, 48(1), 4-22. ([DOI](https://doi.org/10.1111/j.1469-8986.2010.01114.x))
- Erickson, M. A., Ruffle, A., & Gold, J. M. (2016). A meta-analysis of mismatch negativity in schizophrenia: From clinical risk to disease specificity and progression. *Biological Psychiatry*, 79(12), 980-987. ([DOI](https://doi.org/10.1016/j.biopsych.2015.08.025), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26444073/))
- Wacongne, C., Labyt, E., van Wassenhove, V., Bekinschtein, T., Naccache, L., & Dehaene, S. (2011). Evidence for a hierarchy of predictions and prediction errors in the human cortex. *Proceedings of the National Academy of Sciences*, 108(51), 20754-20759. ([DOI](https://doi.org/10.1073/pnas.1117807108), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22147913/))

## External links

- CogPO: Auditory Oddball Paradigm (close match)

