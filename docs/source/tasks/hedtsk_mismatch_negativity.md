(hedtsk_mismatch_negativity)=
# Mismatch Negativity Task

**HED task ID:** `hedtsk_mismatch_negativity`

**Family:** [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md)

**Also known as:** MMN, Mismatch Negativity Paradigm, Mismatch Negativity

Passive auditory oddball in which rare deviant sounds elicit a negative ERP around 150–250 ms, indexing pre-attentive auditory change detection.

## Description

Participants are passively exposed to repetitive acoustic stimuli (standard tones, 80%) occasionally interrupted by deviant tones (20%) differing in pitch, duration, or location. The MMN can be elicited without active attention. Recorded via EEG, the MMN appears as a negative deflection peaking at 100-250 ms after deviance onset at frontocentral sites. It reflects automatic, pre-attentive comparison between incoming input and a neural representation of the standard stimulus stored in sensory (echoic) memory. MMN is used as a biomarker of auditory processing capacity and has clinical applications in schizophrenia, coma prognosis, and language development research.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A repetitive standard tone is occasionally replaced by a deviant tone differing in frequency, duration, or intensity. Participants typically ignore the sounds while reading or watching a silent video.
* - **Manipulation**
  - Deviant type (frequency, duration, intensity, phoneme); deviant probability; magnitude of deviance; ISI.
* - **Measurement**
  - MMN amplitude and latency (deviant-minus-standard difference wave, peaking 100–250 ms); scalp topography.
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
* - Frequency MMN

    `hedvar_mismatch_negativity__frequency_mmn`
  - Deviant tone frequency differs from standard.
  - Frequency deviant in auditory stream; canonical MMN stimulus type
* - Duration MMN

    `hedvar_mismatch_negativity__duration_mmn`
  - Deviant tone duration differs from standard.
  - Duration deviant; different acoustic dimension
* - Intensity MMN

    `hedvar_mismatch_negativity__intensity_mmn`
  - Deviant tone intensity differs from standard.
  - Intensity deviant; tests loudness change detection
* - Location/Spatial MMN

    `hedvar_mismatch_negativity__location_spatial_mmn`
  - Deviant sound location differs from standard.
  - Spatial location change; different perceptual dimension
* - Complex Pattern MMN

    `hedvar_mismatch_negativity__complex_pattern_mmn`
  - Rule-violation deviants in patterned sequences.
  - Pattern-level violation; higher-order regularity processing
* - Multi-Feature MMN (Optimum)

    `hedvar_mismatch_negativity__multi_feature_mmn_optimum`
  - Multiple deviant types within single paradigm; efficient clinical protocol.
  - Multiple deviants in single paradigm; different stimulus sequence
* - Phoneme/Speech MMN

    `hedvar_mismatch_negativity__phoneme_speech_mmn`
  - Vowel, consonant, or syllable deviants; language-specific processing.
  - Phonemic contrast as deviant; linguistic processing
* - Visual MMN (vMMN)

    `hedvar_mismatch_negativity__visual_mmn_vmmn`
  - Deviant visual stimuli in sequences; tests predictive coding in vision.
  - Visual change detection; different sensory modality
* - Roving Standard MMN

    `hedvar_mismatch_negativity__roving_standard_mmn`
  - Standard identity changes after train of repetitions; connects to repetition suppression.
  - Standard changes after each sequence; different stimulus history structure
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

- Näätänen, R., Kujala, T., & Winkler, I. (2011). Auditory processing that leads to conscious perception: A unique window to central auditory processing opened by the mismatch negativity and related responses. *Psychophysiology*, 48(1), 4–22. ([DOI](https://doi.org/10.1111/j.1469-8986.2011.01239.x))
- Erickson, M. A., Ruffle, A., & Gold, J. M. (2016). A meta-analysis of mismatch negativity in schizophrenia: From clinical risk to disease specificity and progression. *Biological Psychiatry*, 79(12), 980–987. ([DOI](https://doi.org/10.1016/j.biopsych.2015.08.025), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26444073/))
- Wacongne, C., Labyt, E., van Wassenhove, V., Bekinschtein, T., Naccache, L., & Dehaene, S. (2011). Evidence for a hierarchy of predictions and prediction errors in the human cortex. *Proceedings of the National Academy of Sciences*, 108(51), 20754–20759. ([DOI](https://doi.org/10.1073/pnas.1117807108), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22147913/))

