(hedtsk_biological_motion_perception)=
# Biological Motion Perception Task

**HED task ID:** `hedtsk_biological_motion_perception`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** Point-Light Displays, Point-Light Walker Task, PLW

Judgment of human action or identity from sparse point-light displays attached to major joints; indexes recognition of biological motion from kinematic cues alone.

## Description

Participants view point-light display stimuli, animations created by placing markers on the joints of a person performing actions and capturing only the light points. The resulting stimuli (12-15 dots representing joints) convey complex human actions (walking, running, dancing) from minimal motion cues. Participants may recognize actions, judge coherence (upright vs. inverted), or discriminate biological from scrambled motion. The task measures perception of complex human movement and activates the posterior superior temporal sulcus, a region specialized for biological motion processing.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-points-of-light">points of light</a>
- **Social aspect:** <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-stimulus-intensity">stimulus intensity</a>, <a href="vocabulary.html#setting-viewpoint-angle">viewpoint angle</a>
- **Material:** Point-light animations of 12-15 dots at the joints of a person walking, running or dancing, shown intact, scrambled or inverted.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants view point-light displays (dots at major joints) and identify actions, discriminate facing direction, or detect biological motion embedded in noise dots.
* - **Manipulations**
  - - Display type (intact, scrambled, inverted, reversed playback)
    - Noise dot density
    - Action category
    - Viewpoint angle
    - Comparison motion (mechanical vs. biological point-light motion)
* - **Measurements**
  - - Accuracy and RT for action identification, direction discrimination, or detection
    - Noise-dot threshold for biological motion detection
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
* - Action Recognition

    `hedvar_biological_motion_perception__action_recognition`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-identify">identify</a>
  - -
  - The figure performs one of several actions and the participant names or chooses which.
* - Detection in Noise

    `hedvar_biological_motion_perception__detection_in_noise`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-points-of-light">points of light</a>, <a href="vocabulary.html#facet-stimulus-type-random-dots">random dots</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>; competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-noise-or-mask">noise or mask</a>
  - -
  - The walker's dots are hidden among extra random dots and the participant reports whether or where a walker is present.
* - Gender/Identity Discrimination

    `hedvar_biological_motion_perception__gender_identity_discrimination`

    Cognitive Atlas: [gender discrimination task](https://www.cognitiveatlas.org/task/id/trm_4f241c8d4a75c) (close match)
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>, <a href="vocabulary.html#facet-social-aspect-explicit-social-task">explicit social task</a>
  - -
  - The participant judges from the motion alone either the walker's gender, as in the standard form, or which known person it is.
* - Emotion from Body Motion

    `hedvar_biological_motion_perception__emotion_from_body_motion`
  - emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>, <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>, <a href="vocabulary.html#facet-social-aspect-explicit-social-task">explicit social task</a>
  - [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
  - The figure moves in an emotional style and the participant names the emotion from the movement alone.
* - Partial/Occluded Displays

    `hedvar_biological_motion_perception__partial_occluded_displays`
  - named form
  - -
  - Only some joint dots are shown, or parts of the figure pass behind an invisible occluder, and the participant judges the incomplete display.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Biological motion perception](../processes/face_and_object_perception.md#hed-biological-motion-perception)
- [Motion perception](../processes/face_and_object_perception.md#hed-motion-perception)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Pattern recognition](../processes/face_and_object_perception.md#hed-pattern-recognition)

## Key references

- Johansson, G. (1973). Visual perception of biological motion and a model for its analysis. *Perception & Psychophysics*, 14(2), 201-211. ([DOI](https://doi.org/10.3758/bf03212378))
- Grossman, E. D., & Blake, R. (2002). Brain areas active during visual perception of biological motion. *Neuron*, 35(6), 1167-1175. ([DOI](https://doi.org/10.1016/s0896-6273(02)00897-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12354405/))
- Blake, R., & Shiffrar, M. (2007). Perception of human motion. *Annual Review of Psychology*, 58, 47-73. ([DOI](https://doi.org/10.1146/annurev.psych.57.102904.190152), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16903802/))

## Further references

- Pavlova, M. A. (2012). Biological motion processing as a hallmark of social cognition. *Cerebral Cortex*, 22(5), 981-995. ([DOI](https://doi.org/10.1093/acprof:oso/9780195393705.003.0011))
- Thompson, J. C., & Baccus, W. (2012). Form and motion make independent contributions to the response to biological motion in occipitotemporal cortex. *NeuroImage*, 59(1), 625-634. ([DOI](https://doi.org/10.1016/j.neuroimage.2011.07.051), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21839175/))
- Federici, A., et al. (2020). Biological motion perception in autism: A meta-analysis. *Research in Autism Spectrum Disorders*, 77, 101610. ([DOI](https://doi.org/10.1186/s13229-019-0299-8))
- Gilaie-Dotan, S., Kanai, R., Bahrami, B., Rees, G., & Saygin, A. P. (2013). Neuroanatomical correlates of biological motion detection. *Neuropsychologia*, 51(3), 457-463. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2012.11.027), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23211992/))
- Thurman, S. M., & Lu, H. (2016). Revisiting the importance of common body dynamics in human action perception. *Attention, Perception, & Psychophysics*, 78, 2187-2199.
- van Boxtel, J. J. A., & Lu, H. (2013). A biological motion toolbox for reading, displaying, and manipulating motion capture data in research settings. *Journal of Vision*, 13(12), 7. ([DOI](https://doi.org/10.1167/13.12.7), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24130256/))
- Miller, L. E., & Saygin, A. P. (2013). Individual differences in the perception of biological motion: Links to social cognition and motor imagery. *Cognition*, 128(2), 140-148. ([DOI](https://doi.org/10.1016/j.cognition.2013.03.013), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23680791/))

## External links

- Cognitive Atlas: [biological motion task](https://www.cognitiveatlas.org/task/id/trm_4f245326e2eaf)

