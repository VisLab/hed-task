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
* - **Manipulation**
  - Display type (intact vs. scrambled vs. inverted); noise dot density; action category; viewpoint angle.
* - **Measurement**
  - Accuracy and RT for action identification, direction discrimination, or detection; noise-dot threshold for biological motion detection.
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
  - Standard point-light walkers with coherent body structure.
  - Standard point-light walker; canonical biological motion stimulus
* - Scrambled Displays

    `hedvar_biological_motion_perception__scrambled_displays`
  - Dot positions randomized; preserves local motion, disrupts configural structure.
  - Spatially scrambled dots preserve local motion but destroy global form; control condition with different percept
* - Inverted Displays

    `hedvar_biological_motion_perception__inverted_displays`
  - Upside-down presentation; impairs perception, revealing orientation specificity.
  - Walker inverted; disrupts configural processing while preserving motion signals
* - Reversed (Backward) Motion

    `hedvar_biological_motion_perception__reversed_backward_motion`
  - Normal actions played in reverse.
  - Temporal reversal disrupts action identity while preserving form
* - Action Recognition

    `hedvar_biological_motion_perception__action_recognition`
  - Classify depicted actions (walk, run, jump, throw, kick).
  - Participant identifies specific action (running, kicking); classification task beyond detection
* - Detection in Noise

    `hedvar_biological_motion_perception__detection_in_noise`
  - Biological motion figures embedded in scrambled dot noise masks.
  - Walker embedded in noise dots; detection task with varying signal-to-noise
* - Gender/Identity Discrimination

    `hedvar_biological_motion_perception__gender_identity_discrimination`
  - Judge walker's gender or identity from motion cues alone.
  - Discrimination of walker gender or identity; different judgment dimension
* - Emotion from Body Motion

    `hedvar_biological_motion_perception__emotion_from_body_motion`
  - Recognize emotional states from body/gait dynamics.
  - Emotional state judged from body kinematics; different recognition task
* - Partial/Occluded Displays

    `hedvar_biological_motion_perception__partial_occluded_displays`
  - Subsets of body points visible.
  - Subset of dots visible; tests perceptual completion of biological motion
* - Comparison with Mechanical Motion

    `hedvar_biological_motion_perception__comparison_with_mechanical_motion`
  - Biological vs. rigid/mechanical motion; tests specificity.
  - Mechanical motion control alongside biological; category discrimination task
* - Facing Direction Discrimination

    `hedvar_biological_motion_perception__facing_direction_discrimination`
  - Determine whether the walker faces left or right; sensitive to viewpoint processing.
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

- Johansson, G. (1973). Visual perception of biological motion and a model for its analysis. *Perception & Psychophysics*, 14(2), 201-211.
- Grossman, E. D., & Blake, R. (2002). Brain areas active during visual perception of biological motion. *Neuron*, 35(6), 1167-1175.
- Blake, R., & Shiffrar, M. (2007). Perception of human motion. *Annual Review of Psychology*, 58, 47-73.

## Recent references

- Pavlova, M. A. (2012). Biological motion processing as a hallmark of social cognition. *Cerebral Cortex*, 22(5), 981–995.
- Thompson, J. C., & Baccus, W. (2012). Form and motion make independent contributions to the response to biological motion in occipitotemporal cortex. *NeuroImage*, 59(1), 625–634.
- Federici, A., et al. (2020). Biological motion perception in autism: A meta-analysis. *Research in Autism Spectrum Disorders*, 77, 101610.
- Gilaie-Dotan, S., Kanai, R., Bahrami, B., Rees, G., & Saygin, A. P. (2013). Neuroanatomical correlates of biological motion detection. *Neuropsychologia*, 51(3), 457–463.
- Thurman, S. M., & Lu, H. (2016). Revisiting the importance of common body dynamics in human action perception. *Attention, Perception, & Psychophysics*, 78, 2187–2199.
- van Boxtel, J. J. A., & Lu, H. (2013). A biological motion toolbox for reading, displaying, and manipulating motion capture data in research settings. *Journal of Vision*, 13(12), 7.
- Miller, L. E., & Saygin, A. P. (2013). Individual differences in the perception of biological motion: Links to social cognition and motor imagery. *Cognition*, 128(2), 140–148.

## External links

- Cognitive Atlas: [biological motion task](https://www.cognitiveatlas.org/task/id/trm_4f245326e2eaf)

