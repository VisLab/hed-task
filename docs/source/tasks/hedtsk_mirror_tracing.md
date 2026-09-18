(hedtsk_mirror_tracing)=
# Mirror Tracing Task

**HED task ID:** `hedtsk_mirror_tracing`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** MTT, Mirror Drawing

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
  - Participants trace a path (star, maze) while viewing their hand only through a mirror, which reverses visual-motor mapping. They must stay within path boundaries.
* - **Manipulation**
  - Path complexity; practice blocks; dominant vs. non-dominant hand.
* - **Measurement**
  - Tracing time; number of boundary errors; improvement across trials (learning curve).
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
  - Trace a six-pointed star outline viewed in a mirror.
  - Canonical mirror tracing of star with visuomotor reversal
* - Circle/Diamond/Complex Shapes

    `hedvar_mirror_tracing__circle_diamond_complex_shapes`
  - Different contour shapes varying in difficulty.
  - Different shape complexity and curvature demands
* - Computerized Mirror Tracing

    `hedvar_mirror_tracing__computerized_mirror_tracing`
  - Mouse or stylus on tablet with software-reversed cursor; precise error and kinematic recording.
  - Screen/stylus instead of physical mirror/pencil; per §5.6, loses haptic edge feedback
* - Left-Right vs. Up-Down Reversal

    `hedvar_mirror_tracing__left_right_vs_up_down_reversal`
  - Reversing only one axis vs. both to study adaptation components.
  - Different mirror axis changes visuomotor mapping
* - Rotation (Non-Mirror) Variants

    `hedvar_mirror_tracing__rotation_non_mirror_variants`
  - Cursor rotated by varying degrees rather than reflected; parametric visuomotor adaptation.
  - Rotation rather than mirror reversal; different visuomotor transformation
* - Prism Adaptation Analog

    `hedvar_mirror_tracing__prism_adaptation_analog`
  - Wearing prism goggles that shift visual field; aftereffects measure adaptation.
  - Prismatic displacement of visual field; different mechanism from mirror reversal
* - Dual-Hand Mirror Tracing

    `hedvar_mirror_tracing__dual_hand_mirror_tracing`
  - Both hands tracing simultaneously with mirrored feedback.
  - Both hands trace simultaneously with mirrored feedback; bimanual coordination variant
* - Mirror Tracing with Delay

    `hedvar_mirror_tracing__mirror_tracing_with_delay`
  - Delayed visual feedback adds temporal decoupling challenge.
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

- Gabrieli, J. D. E., Corkin, S., Mickel, S. F., & Growdon, J. H. (1993). Intact acquisition and long-term retention of mirror-tracing skill in Alzheimer's disease and in global amnesia. *Behavioral Neuroscience*, 107(6), 899–910.
- Sanes, J. N. (2003). Neocortical mechanisms in motor learning. *Current Opinion in Neurobiology*, 13(2), 225–231.

## Recent references

- Halsband, U., & Lange, R. K. (2006). Motor learning in man: A review of functional and clinical studies. *Journal of Physiology-Paris*, 99(4-6), 414–424.
- Treutwein, B., & Strasburger, H. (1999). Fitting the psychometric function. *Perception & Psychophysics*, 61(1), 87–106. [Methodological context for motor learning curves]
- Hardwick, R. M., Rottschy, C., Miall, R. C., & Eickhoff, S. B. (2013). A quantitative meta-analysis and review of motor learning in the human brain. *NeuroImage*, 67, 283–297.
- Boyd, L. A., & Winstein, C. J. (2004). Cerebellar stroke impairs temporal but not spatial accuracy during implicit motor learning. *Neurorehabilitation and Neural Repair*, 18(3), 134–143.

## External links

- Cognitive Atlas: [mirror tracing task](https://www.cognitiveatlas.org/task/id/trm_4f244a67d5b17)

