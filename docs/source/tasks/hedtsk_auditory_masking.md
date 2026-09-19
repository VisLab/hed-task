(hedtsk_auditory_masking)=
# Auditory Masking Task

**HED task ID:** `hedtsk_auditory_masking`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** Tone-in-Noise Detection, Speech-in-Noise, Energetic Masking

Detect, discriminate, or identify a target sound in the presence of a masking sound; threshold shifts between masked and unmasked conditions index frequency selectivity, temporal resolution, and auditory scene analysis.

## Description

A target sound (tone, speech token, or noise burst) is presented alongside, before, or after a masking sound, and participants detect, discriminate, or identify the target. By varying the temporal and spectral relationship between target and masker, the paradigm dissociates peripheral (energetic) masking — where masker and target excite overlapping auditory filters — from central (informational) masking — where the masker is spectrally remote but introduces perceptual uncertainty. Threshold shifts, psychometric functions, and comodulation masking release are the core dependent measures. The paradigm is foundational to auditory psychophysics and clinical audiology, and maps onto distinct subcortical and cortical processing stages.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A target sound is presented alongside, before, or after a masker; participants detect, discriminate, or identify the target.
* - **Manipulation**
  - Temporal relation (simultaneous, forward, backward); spectral overlap between target and masker; masker type (noise, tones, speech, modulated); spatial separation.
* - **Measurement**
  - Detection threshold (masked vs. unmasked); threshold shift; psychometric function slope; speech reception threshold in noise.
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
* - Simultaneous masking

    `hedvar_auditory_masking__simultaneous_masking`
  - Target and masker overlap in time; measures frequency selectivity via notched-noise or band-reject paradigms.
  - Masker and target overlap in time; fundamental temporal configuration of masking
* - Forward masking

    `hedvar_auditory_masking__forward_masking`
  - Masker precedes target by a brief interval; probes temporal resolution and adaptation recovery.
  - Masker precedes target; different temporal relationship produces distinct masking mechanism
* - Backward masking

    `hedvar_auditory_masking__backward_masking`
  - Masker follows target; demonstrates retroactive interference in early auditory processing.
  - Masker follows target; different temporal order from forward masking
* - Energetic masking (peripheral)

    `hedvar_auditory_masking__energetic_masking_peripheral`
  - Target and masker excite overlapping auditory filters; threshold shift predicted by excitation-pattern models.
  - Peripheral auditory overlap; mechanistically distinct from informational masking
* - Informational masking (central)

    `hedvar_auditory_masking__informational_masking_central`
  - Masker is spectrally remote but perceptually confusable; threshold shift exceeds energetic predictions.
  - Central/cognitive masking mechanism; different stimulus and processing demands
* - Comodulation masking release (CMR)

    `hedvar_auditory_masking__comodulation_masking_release_cmr`
  - Coherent amplitude modulation across frequency bands releases target from masking; indexes across-channel grouping.
  - Comodulated flanking bands release target from masking; unique stimulus configuration
* - Speech-in-noise

    `hedvar_auditory_masking__speech_in_noise`
  - Speech target masked by competing talkers, babble, or steady-state noise; measures speech reception threshold.
  - Speech target in noise background; distinct task with different linguistic processing demands
* - Tone-in-noise detection

    `hedvar_auditory_masking__tone_in_noise_detection`
  - Pure-tone target in broadband or narrowband noise; foundational psychoacoustic paradigm for measuring auditory filter shape.
  - Pure tone detection in wideband noise; different target type from speech or complex stimuli
* - Modulation masking

    `hedvar_auditory_masking__modulation_masking`
  - Amplitude-modulated masker reduces detection of amplitude modulation on a carrier; probes modulation filter bank.
  - Masking of temporal amplitude modulation; different perceptual dimension
* - Spatial release from masking

    `hedvar_auditory_masking__spatial_release_from_masking`
  - Separating masker and target in space reduces masking; measures binaural and spatial processing.
  - Spatial separation of target and masker; binaural processing distinguishes it from monaural variants
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

- Shinn-Cunningham, B. G. (2008). Object-based auditory and visual attention. Trends in Cognitive Sciences, 12(5), 182–186. ([DOI](https://doi.org/10.1016/j.tics.2008.02.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18396091/))

## External links

- Cognitive Atlas: [auditory masking task](https://www.cognitiveatlas.org/task/id/trm_551b1b6f6a262)

