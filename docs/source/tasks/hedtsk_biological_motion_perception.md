(hedtsk_biological_motion_perception)=
# Biological Motion Perception Task

**HED task ID:** `hedtsk_biological_motion_perception`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** Point-Light Displays, Point-Light Walker Task, PLW

Judgment of human action or identity from sparse point-light displays attached to major joints; indexes recognition of biological motion from kinematic cues alone.

## Description

Participants view point-light display stimuli, animations created by placing markers on the joints of a person performing actions and capturing only the light points. The resulting stimuli (12-15 dots representing joints) convey complex human actions (walking, running, dancing) from minimal motion cues. Participants may recognize actions, judge coherence (upright vs. inverted), or discriminate biological from scrambled motion. The task measures perception of complex human movement and activates the posterior superior temporal sulcus, a region specialized for biological motion processing.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants view point-light displays (dots at major joints) and identify actions, discriminate facing direction, or detect biological motion embedded in noise dots.
* - **Manipulations**
  - - Display type (intact vs. scrambled vs. inverted)
    - Noise dot density
    - Action category
    - Viewpoint angle
* - **Measurements**
  - - Accuracy and RT for action identification, direction discrimination, or detection
    - Noise-dot threshold for biological motion detection
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
* - Intact Biological Motion

    `hedvar_biological_motion_perception__intact_biological_motion`
  - The participant watches a display of about a dozen moving dots placed at the joints of a walking person. The dots alone are enough to see a walker, and the participant reports what is seen, for example whether a person is present or which way they are walking.
  - Standard point-light walker; canonical biological motion stimulus
* - Scrambled Displays

    `hedvar_biological_motion_perception__scrambled_displays`
  - Each dot keeps its own movement pattern but is shifted to a random starting position, so the dots no longer line up as a body. The participant sees the same local motions without the overall figure, which serves as a control.
  - Spatially scrambled dots preserve local motion but destroy global form; control condition with different percept
* - Inverted Displays

    `hedvar_biological_motion_perception__inverted_displays`
  - The point-light walker is shown upside down. Recognition becomes much harder, which shows that the visual system expects figures in their usual orientation.
  - Walker inverted; disrupts configural processing while preserving motion signals
* - Reversed (Backward) Motion

    `hedvar_biological_motion_perception__reversed_backward_motion`
  - The walking animation is played in reverse, so the body shape is intact but the movements unfold in an unnatural order. The participant judges the display as usual.
  - Temporal reversal disrupts action identity while preserving form
* - Action Recognition

    `hedvar_biological_motion_perception__action_recognition`
  - The point-light figure performs one of several actions, such as walking, running, jumping, throwing or kicking, and the participant names or chooses which action it was.
  - Participant identifies specific action (running, kicking); classification task beyond detection
* - Detection in Noise

    `hedvar_biological_motion_perception__detection_in_noise`
  - The walker's dots are hidden among extra randomly moving dots, and the participant reports whether a walker is present or where it is. The number of noise dots sets the difficulty.
  - Walker embedded in noise dots; detection task with varying signal-to-noise
* - Gender/Identity Discrimination

    `hedvar_biological_motion_perception__gender_identity_discrimination`

    Cognitive Atlas: [gender discrimination task](https://www.cognitiveatlas.org/task/id/trm_4f241c8d4a75c) (close match)
  - The participant judges whether the point-light walker is male or female, or which of several known people it is, using only the way the dots move.
  - Discrimination of walker gender or identity; different judgment dimension
* - Emotion from Body Motion

    `hedvar_biological_motion_perception__emotion_from_body_motion`
  - The point-light figure moves in a way that expresses an emotion, such as angry, sad or happy walking, and the participant names the emotion from the movement alone.
  - Emotional state judged from body kinematics; different recognition task
* - Partial/Occluded Displays

    `hedvar_biological_motion_perception__partial_occluded_displays`
  - Only some of the joint dots are shown, or parts of the figure pass behind an invisible occluder, and the participant must still judge the figure from the incomplete display.
  - Subset of dots visible; tests perceptual completion of biological motion
* - Comparison with Mechanical Motion

    `hedvar_biological_motion_perception__comparison_with_mechanical_motion`
  - Point-light displays of a person are mixed with displays of rigid or mechanical motion, such as a rotating object or a machine, and the participant decides which kind of motion each display shows.
  - Mechanical motion control alongside biological; category discrimination task
* - Facing Direction Discrimination

    `hedvar_biological_motion_perception__facing_direction_discrimination`
  - The walker walks in place, and the participant reports whether it is facing left or right. Judging facing direction depends on recovering the body's shape from the moving dots.
  - Ambiguous facing direction judgment; different perceptual task
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

