(hedtsk_finger_tapping)=
# Finger Tapping Task

**HED task ID:** `hedtsk_finger_tapping`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** FTT, Tapping Task, Finger Tapping

Repetitive single-finger or sequence tapping at fastest or paced rates; taps-per-interval and tap-timing variability index motor speed and rhythm control.

## Description

Participants tap their fingers (typically index finger) in a repetitive manner at a self-paced or externally paced rate. Self-paced tapping is typically at 2-3 Hz; externally paced versions use an auditory or visual metronome. The task consists of tapping blocks (20-40 seconds) alternating with rest periods. Performance metrics include tapping frequency, inter-tap interval variability, and accuracy. It is the most commonly used simple motor paradigm for motor cortex mapping, clinical motor assessment, and studying motor control. Contralateral primary motor cortex and supplementary motor area are consistently activated.

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
* - **Measurements**
  - - Tapping rate (taps/sec)
    - Inter-tap interval variability
    - Synchronization error and drift in paced conditions
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
* - Self-Paced Tapping

    `hedvar_finger_tapping__self_paced_tapping`
  - The participant taps a key or pad repeatedly with one finger at a steady rate of their own choosing, with no external timing signal. The chosen tempo and its regularity are measured.
  - Participant taps at preferred rate; measures preferred motor tempo
* - Auditorily-Paced Tapping

    `hedvar_finger_tapping__auditorily_paced_tapping`
  - A metronome click is played at a fixed rate, and the participant taps in time with it. The offset between each tap and the click, and the variability of that offset, are measured.
  - Synchronize to auditory metronome; different sensorimotor integration
* - Visually-Paced Tapping

    `hedvar_finger_tapping__visually_paced_tapping`
  - The pacing signal is a flashing shape on a screen rather than a sound, and the participant taps in time with the flashes.
  - Synchronize to visual metronome; different sensory modality for pacing
* - Unimanual vs. Bimanual

    `hedvar_finger_tapping__unimanual_vs_bimanual`
  - Tapping with both hands at once, either in unison or alternating, is compared with tapping with one hand. Coordinating the two hands adds its own difficulty.
  - One vs. two hands; bimanual coordination introduces interlimb constraints
* - Sequential Multi-Finger

    `hedvar_finger_tapping__sequential_multi_finger`
  - Rather than one finger repeating, the participant taps a fixed order of fingers (for example index, middle, ring, little) over and over, as fast or as regularly as possible.
  - Specific finger sequence rather than single finger; different motor programming
* - Complex Rhythmic Patterns

    `hedvar_finger_tapping__complex_rhythmic_patterns`
  - The participant reproduces a rhythm with uneven gaps between taps, such as long-short-short, rather than tapping at an even beat.
  - Non-isochronous rhythm; changes temporal structure of tapping
* - Continuation Paradigm

    `hedvar_finger_tapping__continuation_paradigm`
  - The participant first taps along with a metronome, then the metronome stops and they must keep tapping at the same rate without it. Drift and variability after the metronome stops show how well the rate is kept internally.
  - External pacing withdrawn mid-task; isolates internal vs. externally guided timing
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

