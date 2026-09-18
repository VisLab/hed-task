(hedtsk_facial_emotion_recognition)=
# Facial Emotion Recognition Task

**HED task ID:** `hedtsk_facial_emotion_recognition`

**Family:** [Emotion elicitation and regulation tasks](families/emotion.md)

**Also known as:** Ekman Faces Task, FER

Identification of an emotion category from a face image; accuracy and RT per emotion index emotion decoding ability.

## Description

Participants view photographs of facial expressions (typically from the Ekman and Friesen Pictures of Facial Affect or similar validated sets) and identify the emotion portrayed. The standard set includes six basic emotions (anger, disgust, fear, happiness, sadness, surprise) plus neutral. Accuracy and RT are measured across emotion categories. The task engages a network including the amygdala (particularly for fear), fusiform face area, superior temporal sulcus, and prefrontal cortex. It is widely used in clinical research on schizophrenia, autism, and mood disorders.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants view face photographs displaying basic emotions and identify the expressed emotion from a fixed set (happy, sad, angry, fearful, disgusted, surprised, neutral).
* - **Manipulation**
  - Emotion category; expression intensity (morphed continua); presentation duration; face race/gender.
* - **Measurement**
  - Accuracy per emotion; confusion matrices; unbiased hit rate; RT.
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
* - Static Ekman Faces (6 basic emotions)

    `hedvar_facial_emotion_recognition__static_ekman_faces_6_basic_emotions`
  - Standard categorization of anger, disgust, fear, happiness, sadness, surprise.
  - Canonical categorical recognition with posed expressions
* - Morphed Intensity

    `hedvar_facial_emotion_recognition__morphed_intensity`
  - Expressions blended at different intensities (20%, 40%, 60%, 80%, 100%).
  - Continuous emotion intensity gradient; participant categorizes or rates on morph scale
* - Dynamic Expressions

    `hedvar_facial_emotion_recognition__dynamic_expressions`
  - Video clips transitioning from neutral to full expression.
  - Temporally unfolding expressions; different stimulus type with motion information
* - Microexpression Detection

    `hedvar_facial_emotion_recognition__microexpression_detection`
  - Brief (40–200 ms) expression flashes; tests rapid perception.
  - Very brief (~40 ms) expressions; different detection difficulty and timing
* - Emotion-in-Context

    `hedvar_facial_emotion_recognition__emotion_in_context`
  - Faces presented with body posture and scene context.
  - Body or scene context accompanies face; changes integration demands
* - Expression Matching

    `hedvar_facial_emotion_recognition__expression_matching`
  - Match expression to labeled emotion or to another face.
  - Match-to-sample format; different response structure from labeling
* - Compound Expressions

    `hedvar_facial_emotion_recognition__compound_expressions`
  - Faces showing mixed emotions (happy-surprise, angry-disgust).
  - Blended or simultaneous multi-emotion displays; different stimulus category
* - Dimensional Ratings

    `hedvar_facial_emotion_recognition__dimensional_ratings`
  - Rating faces on continuous valence and arousal rather than category.
  - Continuous valence/arousal ratings instead of categorical labels; different response type and scale
```

## Cognitive processes

This task is designed to engage the following processes:

- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)

## Key references

- Ekman, P., & Friesen, W. V. (1976). *Pictures of Facial Affect*. Palo Alto, CA: Consulting Psychologists Press.
- Adolphs, R., Tranel, D., Damasio, H., & Damasio, A. (1994). Impaired recognition of emotion in facial expressions following bilateral damage to the human amygdala. *Nature*, 372(6507), 669-672.

## Recent references

- Calvo, M. G., & Nummenmaa, L. (2016). Perceptual and affective mechanisms in facial expression recognition: An integrative review. *Cognition and Emotion*, 30(6), 1081–1106.
- Kret, M. E., & De Gelder, B. (2012). A review on sex differences in processing emotional signals. *Neuropsychologia*, 50(7), 1211–1221.
- Dobs, K., Isik, L., Pantazis, D., & Kanwisher, N. (2019). How face perception unfolds over time. *Nature Communications*, 10(1), 1258.
- Palermo, R., & Rhodes, G. (2007). Are you always on my mind? A review of how face perception and attention interact. *Neuropsychologia*, 45(1), 75–92. [Updated: Barrett, L. F., Adolphs, R., Marsella, S., Martinez, A. M., & Pollak, S. D. (2019). Emotional expressions reconsidered: Challenges to inferring emotion from human facial movements. *Psychological Science in the Public Interest*, 20(1), 1–68.]

## External links

- Cognitive Atlas: [Emotion Recognition Task](https://www.cognitiveatlas.org/task/id/trm_50f734f86b11a) (close match)

