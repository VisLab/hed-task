(hedtsk_mental_rotation)=
# Mental Rotation Task

**HED task ID:** `hedtsk_mental_rotation`

**Family:** [Spatial cognition and navigation tasks](families/spatial_navigation.md) (also [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md))

**Also known as:** MRT, Shepard-Metzler Task, Mental Rotation

Judgment of whether two rotated objects are identical or mirror images; RT scales linearly with angular disparity, indexing mental rotation.

## Description

Participants view pairs of 3D objects (block figures, letters, or geometric forms) and determine whether they are identical (one is a rotated version of the other) or mirror images. Objects are rotated at angles ranging from 0 to 180 degrees relative to each other. The well-established finding is that RT increases linearly with angular disparity, suggesting an analog mental rotation process. The task measures spatial visualization ability, mental imagery, and visuospatial working memory. Sex differences in mental rotation are among the most reliable cognitive sex differences.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-compare">compare</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-viewpoint-angle">viewpoint angle</a>
- **Material:** Pairs of 2D or 3D figures (block figures, letters or hands) rotated relative to each other, identical or mirror-reversed.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Two figures (3-D block shapes, letters, or hands) are presented at different orientations.
    2. Participants judge whether they are the same or mirror-reversed.
* - **Manipulations**
  - - Angular disparity between the two figures (0-180 degrees)
    - Stimulus complexity
    - Dimensionality (2D vs. 3D)
    - Task rule (hand laterality judgment vs. same-or-mirror comparison)
    - Concurrent movement (hand rotation congruent or incongruent with the imagined rotation)
    - Rotation frame (self-rotation vs. object rotation)
* - **Measurements**
  - - RT as a function of angular disparity (linear slope = rotation rate)
    - Accuracy
    - The RT-angle linear function
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
* - 2D Shape Rotation

    `hedvar_mental_rotation__2d_shape_rotation`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; reference: <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
  - -
  - Flat letters, digits or polygons are rotated in the picture plane and a single rotated item is judged normal or mirror-reversed against its remembered canonical form, instead of being compared with a partner on screen.
* - Body Part Rotation (Hand Laterality)

    `hedvar_mental_rotation__body_part_rotation_hand_laterality`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-classify">classify</a>
  - -
  - A single picture of a hand in some orientation is classified as left or right, instead of two pictures being compared as same or mirrored.
* - Mirror vs. Identical Discrimination

    `hedvar_mental_rotation__mirror_vs_identical_discrimination`
  - reference: <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
  - -
  - One rotated figure is shown per trial and judged as the standard or its mirror image, so the comparison is against a figure held in memory.
* - Embodied/Motor-Assisted Rotation

    `hedvar_mental_rotation__embodied_motor_assisted_rotation`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-joystick">joystick</a>; combined with: <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-produce-movement">produce movement</a> (A hand movement is made while the rotation judgment is formed)
  - -
  - While judging, the participant turns a handle or rotates the hand in the same or the opposite direction as the imagined rotation; whether the two directions agree is the factor of interest.
* - Virtual Reality Mental Rotation

    `hedvar_mental_rotation__virtual_reality_mental_rotation`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-head-mounted-display">head mounted display</a>, <a href="vocabulary.html#facet-task-io-device-handheld-controller">handheld controller</a>; experimental environment: <a href="vocabulary.html#facet-experimental-environment-virtual-world">virtual world</a>
  - -
  - The objects are rendered in stereoscopic 3D through a head-mounted display and may be walked around or handled; the same-or-mirror judgment is unchanged.
* - Egocentric vs. Allocentric Rotation

    `hedvar_mental_rotation__egocentric_vs_allocentric_rotation`
  - named form
  - [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking)
  - In one condition the participant imagines turning themselves to a new viewpoint and reports what they would see; in the other they imagine the object turning while staying still.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Mental rotation](../processes/spatial_cognition_and_navigation.md#hed-mental-rotation)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Shepard, R. N., & Metzler, J. (1971). Mental rotation of three-dimensional objects. *Science*, 171(3972), 701-703. ([DOI](https://doi.org/10.1126/science.171.3972.701), [PubMed](https://pubmed.ncbi.nlm.nih.gov/5540314/))
- Zacks, J. M. (2008). Neuroimaging studies of mental rotation: A meta-analysis and review. *Journal of Cognitive Neuroscience*, 20(1), 1-19. ([DOI](https://doi.org/10.1162/jocn.2008.20.1.1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17919082/))

## Further references

- Milivojevic, B., et al. (2023). Imaging the spin: Disentangling the core processes underlying mental rotation by meta-analysis. *Neuroscience & Biobehavioral Reviews*, 147, 105131. ([DOI](https://doi.org/10.1016/j.neubiorev.2023.105187))

## External links

- Cognitive Atlas: [mental rotation task](https://www.cognitiveatlas.org/task/id/trm_4c8990810541d)

- CogPO: [Mental Rotation Paradigm](http://www.wiki.cogpo.org/index.php?title=Mental_Rotation_Paradigm)

