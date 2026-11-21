(hedtsk_face_processing)=
# Face Processing Task

**HED task ID:** `hedtsk_face_processing`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** FFA Localizer, Face Localizer

Blocked or event-related presentation of faces vs. objects (or scrambled faces) to localize face-selective cortical regions (FFA, OFA, pSTS).

## Description

The FFA Localizer presents alternating blocks of faces and non-face objects (houses, cars, scrambled images) while participants perform passive viewing or a simple task (one-back matching, gender judgment). The contrast of faces > objects identifies face-selective regions, particularly the fusiform face area (FFA) in ventral temporal cortex. The task provides an individually-defined localizer for face-selective cortex and has been fundamental to understanding the neural basis of face perception and the question of domain-specific processing modules.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-experience-passively">Experience passively</a> (`experience_passively`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *Is anything asked afterwards?* <a href="vocabulary.html#rule-experience-passively-report-after-none">none</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-block-duration">block duration</a>
- **Material:** Blocks of face photographs alternating with blocks of non-face objects such as houses, cars or scrambled images.
- **Combined with:** <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (A repetition-detection job is done on the items while they are viewed)

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
  - - Stimulus category (faces, objects, scrambled, scenes, inverted faces, face parts)
    - Block duration
    - Task (1-back, passive viewing)
    - Stimulus format (dynamic video vs. still photograph)
    - Identity repetition between faces (adaptation)
    - Face familiarity (known or famous vs. unknown)
* - **Measurements**
  - - fMRI contrast (faces > objects) identifying FFA, OFA, STS
    - Extent and magnitude of face-selective activation
    - Lateralization index
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
* - Dynamic Face Localizer

    `hedvar_face_processing__dynamic_face_localizer`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>
  - -
  - Short video clips of moving faces and moving objects replace still photographs.
* - Identity Adaptation

    `hedvar_face_processing__identity_adaptation`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - [Face identity recognition](../processes/face_and_object_perception.md#hed-face-identity-recognition)
  - Faces are shown in pairs or short runs in which identity repeats or changes trial by trial, and the response reduction to a repeat is the measure instead of a block contrast.
* - Familiar vs. Unfamiliar Faces

    `hedvar_face_processing__familiar_vs_unfamiliar_faces`
  - named form
  - [Face identity recognition](../processes/face_and_object_perception.md#hed-face-identity-recognition)
  - Some faces belong to people the participant knows or to famous people, and responses to known and unknown faces are compared.
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

