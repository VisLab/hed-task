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
  - The target sound and the masking sound play at the same time. The participant reports whether the target was present, and its level is adjusted to find the quietest level still detectable in the masker. Used to measure how finely the ear separates frequencies.
  - Masker and target overlap in time; fundamental temporal configuration of masking
* - Forward masking

    `hedvar_auditory_masking__forward_masking`
  - The masker plays first and stops, and the target sound follows after a short silent gap (a few to a few hundred milliseconds). The participant reports whether the target was heard. The closer the target follows the masker, the harder it is to hear.
  - Masker precedes target; different temporal relationship produces distinct masking mechanism
* - Backward masking

    `hedvar_auditory_masking__backward_masking`
  - The brief target sound plays first and the masker follows it. Even though the target comes first, a masker arriving soon enough afterwards makes it harder to detect.
  - Masker follows target; different temporal order from forward masking
* - Energetic masking (peripheral)

    `hedvar_auditory_masking__energetic_masking_peripheral`
  - The masker is a noise or tone that overlaps the target in frequency, so the two sounds physically compete in the same region of the inner ear. Detection thresholds can be predicted from the acoustics alone.
  - Peripheral auditory overlap; mechanistically distinct from informational masking
* - Informational masking (central)

    `hedvar_auditory_masking__informational_masking_central`
  - The masker does not overlap the target in frequency, but it is similar or unpredictable enough (for example random tone complexes or other speech) that the listener has trouble telling target from masker. The difficulty comes from confusion and attention rather than from the ear itself.
  - Central/cognitive masking mechanism; different stimulus and processing demands
* - Comodulation masking release (CMR)

    `hedvar_auditory_masking__comodulation_masking_release_cmr`
  - The target tone is masked by a narrow band of noise, and additional noise bands are added at other frequencies. When those bands rise and fall in loudness together with the masker, the target becomes easier to hear; when they fluctuate independently, it does not.
  - Comodulated flanking bands release target from masking; unique stimulus configuration
* - Speech-in-noise

    `hedvar_auditory_masking__speech_in_noise`
  - The target is spoken words or sentences, and the masker is other talkers, babble or steady noise. The participant repeats or identifies what was said, and the signal-to-noise ratio at which half the words are correct is the measure.
  - Speech target in noise background; distinct task with different linguistic processing demands
* - Tone-in-noise detection

    `hedvar_auditory_masking__tone_in_noise_detection`
  - The target is a pure tone and the masker is broadband or narrowband noise. The participant reports whether the tone was present in each noise burst, often choosing which of two intervals contained it. The basic version of the task.
  - Pure tone detection in wideband noise; different target type from speech or complex stimuli
* - Modulation masking

    `hedvar_auditory_masking__modulation_masking`
  - Rather than detecting a sound, the participant detects whether a sound's loudness is fluttering (amplitude modulated). A masker with its own loudness fluctuations at a nearby rate makes the target flutter harder to notice.
  - Masking of temporal amplitude modulation; different perceptual dimension
* - Spatial release from masking

    `hedvar_auditory_masking__spatial_release_from_masking`
  - The target and masker are played from different directions, either from separate loudspeakers or with headphone cues that place them apart. The participant's detection threshold is compared with the same sounds played from the same location.
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

