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
  - 1. Blocks of faces alternate with blocks of non-face objects (houses, scrambled images) while participants perform a simple repetition-detection task.
    2. The contrast localizes face-selective cortex.
* - **Manipulations**
  - - Stimulus category (faces vs. objects vs. scrambled vs. scenes)
    - Block duration
    - Task (1-back, passive viewing)
* - **Measurements**
  - - fMRI contrast (faces > objects) identifying FFA, OFA, STS
    - Extent and magnitude of face-selective activation
    - Lateralization index
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
  - Pictures of faces and pictures of everyday objects are shown in alternating blocks of about 15 to 20 seconds each while brain activity is recorded. The participant usually just watches, or presses a key when a picture repeats to stay alert. Comparing face blocks with object blocks locates face-selective brain areas.
  - Localizer with objects as contrast; category-selective activation paradigm
* - Faces vs. Scrambled Faces

    `hedvar_face_processing__faces_vs_scrambled_faces`
  - The comparison pictures are the same face images cut into pieces and rearranged so they no longer look like faces. This keeps the colors and contrast identical, so any difference is due to seeing a face rather than to low-level image properties.
  - Scrambled faces as control; tests configural vs. feature processing
* - Faces vs. Houses

    `hedvar_face_processing__faces_vs_houses`
  - The comparison blocks show pictures of houses or buildings, another category with its own specialized brain response, giving a clean contrast for locating face areas.
  - Houses as non-face object category; standard FFA localizer contrast
* - Dynamic Face Localizer

    `hedvar_face_processing__dynamic_face_localizer`
  - Short video clips of moving faces (talking, changing expression) are used instead of still photographs, with moving objects as the comparison. Video gives stronger and more reliable responses in face areas.
  - Moving/dynamic faces; different temporal and motion processing demands
* - Upright vs. Inverted Faces

    `hedvar_face_processing__upright_vs_inverted_faces`
  - Faces are shown upright in some blocks and upside down in others. Inverted faces are harder to process as a whole, and the difference between the two isolates whole-face processing.
  - Face inversion disrupts configural processing; different perceptual experience
* - Identity Adaptation

    `hedvar_face_processing__identity_adaptation`
  - Faces are shown in pairs or short runs. Sometimes the same person's face repeats, sometimes a different person follows. The brain response is weaker to a repeated identity, so the drop measures sensitivity to who the face belongs to.
  - Adaptation paradigm with identity pairs; different temporal structure
* - Face Parts (Eyes, Mouth)

    `hedvar_face_processing__face_parts_eyes_mouth`
  - Only parts of faces are shown, such as the eyes alone or the mouth alone, in separate blocks from whole faces, to see whether face areas respond to features or need the whole face.
  - Isolated face regions; participant views different spatial configuration
* - Familiar vs. Unfamiliar Faces

    `hedvar_face_processing__familiar_vs_unfamiliar_faces`
  - Some faces are of people the participant knows personally or famous people, and others are strangers. The participant views them (or judges familiarity), and responses to known and unknown faces are compared.
  - Familiarity manipulation changes recognition demand
```

## Cognitive processes

This task is designed to engage the following processes:

- [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
- [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)

## Key references

- Kanwisher, N., McDermott, J., & Chun, M. M. (1997). The fusiform face area: A module in human extrastriate cortex specialized for face perception. *Journal of Neuroscience*, 17(11), 4302-4311. ([DOI](https://doi.org/10.1523/jneurosci.17-11-04302.1997), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9151747/))
- Grill-Spector, K., Knouf, N., & Kanwisher, N. (2004). The fusiform face area subserves face perception, not generic within-category identification. *Nature Neuroscience*, 7(5), 555-562. ([DOI](https://doi.org/10.1038/nn1224), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15077112/))
- Haxby, J. V., Hoffman, E. A., & Gobbini, M. I. (2000). The distributed human neural system for face perception. *Trends in Cognitive Sciences*, 4(6), 223-233. ([DOI](https://doi.org/10.1016/s1364-6613(00)01482-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10827445/))

## Further references

- Weiner, K. S., & Grill-Spector, K. (2012). The improbable simplicity of the fusiform face area. *Trends in Cognitive Sciences*, 16(5), 251-254. ([DOI](https://doi.org/10.1016/j.tics.2012.03.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22481071/))
- Pitcher, D., Walsh, V., & Duchaine, B. (2011). The role of the occipital face area in the cortical face perception network. *Experimental Brain Research*, 209(4), 481-493. ([DOI](https://doi.org/10.1007/s00221-011-2579-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21318346/))
- Grill-Spector, K., Weiner, K. S., Kay, K., & Gomez, J. (2017). The functional neuroanatomy of human face perception. *Annual Review of Vision Science*, 3, 167-196. ([DOI](https://doi.org/10.1146/annurev-vision-102016-061214), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28715955/))

## External links

- CogPO: [Face Monitor or Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Face_Monitor_or_Discrimination_Paradigm) (close match)

