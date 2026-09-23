(hedtsk_mental_rotation)=
# Mental Rotation Task

**HED task ID:** `hedtsk_mental_rotation`

**Family:** [Spatial cognition and navigation tasks](families/spatial_navigation.md) (also [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md))

**Also known as:** MRT, Shepard-Metzler Task, Mental Rotation

Judgment of whether two rotated objects are identical or mirror images; RT scales linearly with angular disparity, indexing mental rotation.

## Description

Participants view pairs of 3D objects (block figures, letters, or geometric forms) and determine whether they are identical (one is a rotated version of the other) or mirror images. Objects are rotated at angles ranging from 0 to 180 degrees relative to each other. The well-established finding is that RT increases linearly with angular disparity, suggesting an analog mental rotation process. The task measures spatial visualization ability, mental imagery, and visuospatial working memory. Sex differences in mental rotation are among the most reliable cognitive sex differences.

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
  - - Angular disparity between the two figures (0°–180°)
    - Stimulus complexity
    - Dimensionality (2D vs. 3D)
* - **Measurements**
  - - RT as a function of angular disparity (linear slope = rotation rate)
    - Accuracy
    - The RT-angle linear function
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
* - Shepard-Metzler 3D Block Figures

    `hedvar_mental_rotation__shepard_metzler_3d_block_figures`
  - Classic 3D object pairs; same vs. mirror-image judgments.
  - Canonical 3D block figure rotation; depth and perspective rotation
* - 2D Shape Rotation

    `hedvar_mental_rotation__2d_shape_rotation`
  - Letters, polygons, or abstract 2D shapes.
  - Flat 2D figures; different stimulus complexity and dimensionality
* - Body Part Rotation (Hand Laterality)

    `hedvar_mental_rotation__body_part_rotation_hand_laterality`
  - Judge left/right hand in rotated orientations.
  - Hands judged as left/right; embodied rotation via motor imagery
* - Mirror vs. Identical Discrimination

    `hedvar_mental_rotation__mirror_vs_identical_discrimination`
  - Discriminating rotated identical from mirror-reflected objects.
  - Distinguish mirrored from same-orientation figure; different judgment type
* - Embodied/Motor-Assisted Rotation

    `hedvar_mental_rotation__embodied_motor_assisted_rotation`
  - Physical rotation gestures during mental rotation.
  - Physical hand rotation accompanies mental rotation; different embodiment condition
* - Virtual Reality Mental Rotation

    `hedvar_mental_rotation__virtual_reality_mental_rotation`
  - Immersive 3D rotation with stereoscopic displays.
  - Immersive VR environment; full-body spatial context changes processing
* - Egocentric vs. Allocentric Rotation

    `hedvar_mental_rotation__egocentric_vs_allocentric_rotation`
  - Rotating self-perspective vs. rotating objects.
  - Participant perspective vs. object-centered rotation; different reference frame
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

