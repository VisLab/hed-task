(hedtsk_face_processing)=
# Face Processing Task

**HED task ID:** `hedtsk_face_processing`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** FFA Localizer, Face Localizer

Blocked or event-related presentation of faces vs. objects (or scrambled faces) to localize face-selective cortical regions (FFA, OFA, pSTS).

## Description

The FFA Localizer presents alternating blocks of faces and non-face objects (houses, cars, scrambled images) while participants perform passive viewing or a simple task (one-back matching, gender judgment). The contrast of faces > objects identifies face-selective regions, particularly the fusiform face area (FFA) in ventral temporal cortex. The task provides an individually-defined localizer for face-selective cortex and has been fundamental to understanding the neural basis of face perception and the question of domain-specific processing modules.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Blocks of faces alternate with blocks of non-face objects (houses, scrambled images) while participants perform a simple repetition-detection task. The contrast localizes face-selective cortex.
* - **Manipulation**
  - Stimulus category (faces vs. objects vs. scrambled vs. scenes); block duration; task (1-back, passive viewing).
* - **Measurement**
  - fMRI contrast (faces > objects) identifying FFA, OFA, STS; extent and magnitude of face-selective activation; lateralization index.
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
* - Faces vs. Objects Block Design

    `hedvar_face_processing__faces_vs_objects_block_design`
  - Alternating blocks; canonical localizer contrast.
  - Localizer with objects as contrast; category-selective activation paradigm
* - Faces vs. Scrambled Faces

    `hedvar_face_processing__faces_vs_scrambled_faces`
  - Controls for low-level visual features.
  - Scrambled faces as control; tests configural vs. feature processing
* - Faces vs. Houses

    `hedvar_face_processing__faces_vs_houses`
  - Reliable contrast producing focused FFA activation.
  - Houses as non-face object category; standard FFA localizer contrast
* - Dynamic Face Localizer

    `hedvar_face_processing__dynamic_face_localizer`
  - Video clips of faces; higher sensitivity.
  - Moving/dynamic faces; different temporal and motion processing demands
* - Upright vs. Inverted Faces

    `hedvar_face_processing__upright_vs_inverted_faces`
  - Probes holistic/configural processing.
  - Face inversion disrupts configural processing; different perceptual experience
* - Identity Adaptation

    `hedvar_face_processing__identity_adaptation`
  - Repeated same-identity presentations to measure identity-specific responses.
  - Adaptation paradigm with identity pairs; different temporal structure
* - Face Parts (Eyes, Mouth)

    `hedvar_face_processing__face_parts_eyes_mouth`
  - Isolated features vs. whole face.
  - Isolated face regions; participant views different spatial configuration
* - Familiar vs. Unfamiliar Faces

    `hedvar_face_processing__familiar_vs_unfamiliar_faces`
  - Personal familiarity effects on face-selective regions.
  - Familiarity manipulation changes recognition demand
```

## Cognitive processes

This task is designed to engage the following processes:

- [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
- [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)

## Key references

- Kanwisher, N., McDermott, J., & Chun, M. M. (1997). The fusiform face area: A module in human extrastriate cortex specialized for face perception. *Journal of Neuroscience*, 17(11), 4302-4311.
- Grill-Spector, K., Knouf, N., & Kanwisher, N. (2004). The fusiform face area subserves face perception, not generic within-category identification. *Nature Neuroscience*, 7(5), 555-562.
- Haxby, J. V., Hoffman, E. A., & Gobbini, M. I. (2000). The distributed human neural system for face perception. *Trends in Cognitive Sciences*, 4(6), 223-233.

## Recent references

- Weiner, K. S., & Grill-Spector, K. (2012). The improbable simplicity of the fusiform face area. *Trends in Cognitive Sciences*, 16(5), 251–254.
- Pitcher, D., Walsh, V., & Duchaine, B. (2011). The role of the occipital face area in the cortical face perception network. *Experimental Brain Research*, 209(4), 481–493.
- Grill-Spector, K., Weiner, K. S., Kay, K., & Gomez, J. (2017). The functional neuroanatomy of human face perception. *Annual Review of Vision Science*, 3, 167–196.

