(hedtsk_mirror_tracing)=
# Mirror Tracing Task

**HED task ID:** `hedtsk_mirror_tracing`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** MTT, Mirror Drawing, Mirror Tracing

Tracing of a figure viewed only in a mirror; error and completion time across trials index visuomotor adaptation and procedural learning.

## Description

The Mirror Tracing Task measures procedural motor learning and sensorimotor adaptation. Participants trace a shape (typically a star outline) while viewing their hand only through a mirror, which reverses the visual feedback left-right. This creates a conflict between visual and proprioceptive information that must be resolved through practice. Performance improves across trials as participants learn to adapt their motor commands to the reversed visual input. Measures include tracing time, number of errors (deviations from the path), and the rate of improvement across trials. The task is a classic demonstration that procedural/implicit memory is preserved in amnesia (H.M. could learn this task despite profound declarative memory loss).

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-produce-movement">Make a movement</a> (`produce_movement`)
- **Game rules:** none are defined for this game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-writing-device">writing device</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-trials">number of trials</a>
- **Material:** A path to trace, such as a star outline or a maze, with the hand seen only in a mirror.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants trace a path (star, maze) while viewing their hand only through a mirror, which reverses visual-motor mapping.
    2. They must stay within path boundaries.
    3. Optional: Tracing is practiced in one session and retested hours or days later with no practice between.
* - **Manipulations**
  - - Path complexity
    - Practice blocks
    - Dominant vs. non-dominant hand
    - Visuomotor mapping (left-right mirror, up-down or two-axis mirror, rotation)
    - Visual field shift (prism goggles; reach to targets)
* - **Measurements**
  - - Tracing time
    - Number of boundary errors
    - Improvement across trials (learning curve)
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
* - Computerized Mirror Tracing

    `hedvar_mirror_tracing__computerized_mirror_tracing`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>, <a href="vocabulary.html#facet-task-io-device-stylus">stylus</a>
  - -
  - The reversal is done in software with a mouse or stylus, with no physical mirror and no felt contact with the track edge.
* - Rotation (Non-Mirror) Variants

    `hedvar_mirror_tracing__rotation_non_mirror_variants`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>, <a href="vocabulary.html#facet-task-io-device-stylus">stylus</a>
  - -
  - The cursor moves in a direction rotated by a fixed angle from the hand's movement instead of mirrored. This is the visuomotor rotation paradigm, which could stand as a task of its own.
* - Prism Adaptation Analog

    `hedvar_mirror_tracing__prism_adaptation_analog`
  - task I/O device: none
  - [Reaching](../processes/motor_preparation_timing_and_execution.md#hed-reaching)
  - The participant wears prism goggles that shift the scene sideways and reaches to targets instead of tracing a shape. This is prism adaptation, which could stand as a task of its own.
* - Dual-Hand Mirror Tracing

    `hedvar_mirror_tracing__dual_hand_mirror_tracing`
  - named form
  - -
  - Both hands trace at once, each with mirror-reversed feedback.
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

