(hedtsk_affective_picture_viewing)=
# Affective Picture Viewing Task

**HED task ID:** `hedtsk_affective_picture_viewing`

**Family:** [Emotion elicitation and regulation tasks](families/emotion.md)

**Also known as:** IAPS Viewing, Passive Viewing Task

Passive or instructed viewing of emotionally valenced images (IAPS, GAPED, NAPS, OASIS) while physiological, neural, or rating responses to valence and arousal are recorded.

## Description

Participants passively view color photographs from the International Affective Picture System (IAPS), a validated database of 1,182 images varying in emotional valence (pleasant, unpleasant, neutral) and arousal (calm to exciting). Images are presented for 3-5 seconds each without requiring an overt response. Post-viewing, participants rate valence and arousal on 9-point scales. The task serves as a standardized emotion elicitation tool in neuroimaging, consistently activating amygdala (for high-arousal images), visual cortex (enhanced processing of emotional stimuli), and prefrontal regions.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants view emotionally valenced images (e.g., IAPS) presented for several seconds each; may rate valence/arousal or simply view while physiological signals are recorded.
* - **Manipulation**
  - Emotional valence (positive, negative, neutral) and arousal level of the images; viewing instructions (passive, reappraise, suppress).
* - **Measurement**
  - Subjective valence and arousal ratings (SAM); skin conductance, startle reflex magnitude, corrugator/zygomatic EMG; ERP components (LPP); fMRI amygdala/PFC activation.
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
* - Category-Specific Selection

    `hedvar_affective_picture_viewing__category_specific_selection`
  - Images selected for discrete emotions (fear, disgust, sadness).
  - Restricts stimuli to specific emotional categories (e.g., fear, disgust), creating category-structured event blocks distinct from mixed viewing
```

## Cognitive processes

This task is designed to engage the following processes:

- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation)

## Key references

- Sabatinelli, D., Bradley, M. M., Fitzsimmons, J. R., & Lang, P. J. (2005). Parallel amygdala and inferotemporal activation reflect emotional intensity and fear relevance. *NeuroImage*, 24(4), 1265-1270.
- Phan, K. L., Wager, T., Taylor, S. F., & Liberzon, I. (2002). Functional neuroanatomy of emotion: A meta-analysis of emotion activation studies in PET and fMRI. *NeuroImage*, 16(2), 331-348.

## Recent references

- Lindquist, K. A., Wager, T. D., Kober, H., Bliss-Moreau, E., & Barrett, L. F. (2012). The brain basis of emotion: A meta-analytic review. *Behavioral and Brain Sciences*, 35(3), 121–143.
- Wager, T. D., Kang, J., Johnson, T. D., Nichols, T. E., Satpute, A. B., & Barrett, L. F. (2015). A Bayesian model of category-specific emotional brain responses. *PLoS Computational Biology*, 11(4), e1004066.

## External links

- Cognitive Atlas: [International Affective Picture System](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949aca) (close match)

