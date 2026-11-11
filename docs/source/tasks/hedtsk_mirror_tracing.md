(hedtsk_mirror_tracing)=
# Mirror Tracing Task

**HED task ID:** `hedtsk_mirror_tracing`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** MTT, Mirror Drawing, Mirror Tracing

Tracing of a figure viewed only in a mirror; error and completion time across trials index visuomotor adaptation and procedural learning.

## Description

The Mirror Tracing Task measures procedural motor learning and sensorimotor adaptation. Participants trace a shape (typically a star outline) while viewing their hand only through a mirror, which reverses the visual feedback left-right. This creates a conflict between visual and proprioceptive information that must be resolved through practice. Performance improves across trials as participants learn to adapt their motor commands to the reversed visual input. Measures include tracing time, number of errors (deviations from the path), and the rate of improvement across trials. The task is a classic demonstration that procedural/implicit memory is preserved in amnesia (H.M. could learn this task despite profound declarative memory loss).

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants trace a path (star, maze) while viewing their hand only through a mirror, which reverses visual-motor mapping.
    2. They must stay within path boundaries.
* - **Manipulations**
  - - Path complexity
    - Practice blocks
    - Dominant vs. non-dominant hand
* - **Measurements**
  - - Tracing time
    - Number of boundary errors
    - Improvement across trials (learning curve)
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
* - Star Tracing (Standard)

    `hedvar_mirror_tracing__star_tracing_standard`
  - A six-pointed star outline is placed behind a screen so the participant can see it only in a mirror. They trace between the double lines of the star with a pencil, and the number of times the pencil leaves the track and the time to finish are recorded over repeated attempts.
  - Canonical mirror tracing of star with visuomotor reversal
* - Circle/Diamond/Complex Shapes

    `hedvar_mirror_tracing__circle_diamond_complex_shapes`
  - The figure to be traced is a circle, diamond, spiral or other shape instead of a star. Shapes with more corners and direction changes are harder to trace in the mirror.
  - Different shape complexity and curvature demands
* - Computerized Mirror Tracing

    `hedvar_mirror_tracing__computerized_mirror_tracing`
  - The participant moves a mouse or stylus while the cursor on screen moves in the mirror-reversed direction. No physical mirror is used, and the cursor cannot be felt bumping the edge of the track.
  - Screen/stylus instead of physical mirror/pencil; per section 5.6, loses haptic edge feedback
* - Left-Right vs. Up-Down Reversal

    `hedvar_mirror_tracing__left_right_vs_up_down_reversal`
  - The mirror or software reverses only the left-right axis, only the up-down axis, or both. Each reversal is a different remapping between what the hand does and what the eye sees.
  - Different mirror axis changes visuomotor mapping
* - Rotation (Non-Mirror) Variants

    `hedvar_mirror_tracing__rotation_non_mirror_variants`
  - Instead of a mirror reversal, the seen cursor direction is rotated by a chosen angle (such as 30 or 90 degrees) from the hand's actual direction. The size of the rotation sets the difficulty.
  - Rotation rather than mirror reversal; different visuomotor transformation
* - Prism Adaptation Analog

    `hedvar_mirror_tracing__prism_adaptation_analog`
  - The participant wears goggles with prisms that shift the visual scene sideways and reaches or points at targets. Pointing errors shrink with practice and reappear in the opposite direction when the goggles are removed.
  - Prismatic displacement of visual field; different mechanism from mirror reversal
* - Dual-Hand Mirror Tracing

    `hedvar_mirror_tracing__dual_hand_mirror_tracing`
  - Both hands trace at the same time, each with mirror-reversed feedback, either on two figures or on mirror-image halves of one figure.
  - Both hands trace simultaneously with mirrored feedback; bimanual coordination variant
* - Mirror Tracing with Delay

    `hedvar_mirror_tracing__mirror_tracing_with_delay`
  - Tracing is practiced in one session and tested again after a delay of hours or days, with no practice in between, to see how much of the adaptation is kept.
  - Delay between practice and test; tests retention of visuomotor adaptation
```

## Cognitive processes

This task is designed to engage the following processes:

- [Visuomotor adaptation](../processes/motor_preparation_timing_and_execution.md#hed-visuomotor-adaptation)
- [Fine motor control](../processes/motor_preparation_timing_and_execution.md#hed-fine-motor-control)
- [Procedural memory](../processes/implicit_and_statistical_learning.md#hed-procedural-memory)
- [Error detection](../processes/inhibitory_control_and_conflict_monitoring.md#hed-error-detection)
- [Motor planning](../processes/motor_preparation_timing_and_execution.md#hed-motor-planning)

## Key references

- Gabrieli, J. D. E., Corkin, S., Mickel, S. F., & Growdon, J. H. (1993). Intact acquisition and long-term retention of mirror-tracing skill in Alzheimer's disease and in global amnesia. *Behavioral Neuroscience*, 107(6), 899-910. ([DOI](https://doi.org/10.1037/0735-7044.107.6.899), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8136066/))
- Sanes, J. N. (2003). Neocortical mechanisms in motor learning. *Current Opinion in Neurobiology*, 13(2), 225-231. ([DOI](https://doi.org/10.1016/s0959-4388(03)00046-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12744978/))

## Further references

- Halsband, U., & Lange, R. K. (2006). Motor learning in man: A review of functional and clinical studies. *Journal of Physiology-Paris*, 99(4-6), 414-424. ([DOI](https://doi.org/10.1016/j.jphysparis.2006.03.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16730432/))
- Treutwein, B., & Strasburger, H. (1999). Fitting the psychometric function. *Perception & Psychophysics*, 61(1), 87-106. [Methodological context for motor learning curves] ([DOI](https://doi.org/10.3758/bf03211951), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10070202/))
- Hardwick, R. M., Rottschy, C., Miall, R. C., & Eickhoff, S. B. (2013). A quantitative meta-analysis and review of motor learning in the human brain. *NeuroImage*, 67, 283-297. ([DOI](https://doi.org/10.1016/j.neuroimage.2012.11.020), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23194819/))
- Boyd, L. A., & Winstein, C. J. (2004). Cerebellar stroke impairs temporal but not spatial accuracy during implicit motor learning. *Neurorehabilitation and Neural Repair*, 18(3), 134-143. ([DOI](https://doi.org/10.1177/0888439004269072), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15375273/))

## External links

- Cognitive Atlas: [mirror tracing task](https://www.cognitiveatlas.org/task/id/trm_4f244a67d5b17)

