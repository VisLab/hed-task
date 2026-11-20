(hedtsk_facial_emotion_recognition)=
# Facial Emotion Recognition Task

**HED task ID:** `hedtsk_facial_emotion_recognition`

**Family:** [Emotion elicitation and regulation tasks](families/emotion.md)

**Also known as:** Ekman Faces Task, Facial Emotion Recognition

Identification of an emotion category from a face image; accuracy and RT per emotion index emotion decoding ability.

## Description

Participants view photographs of facial expressions (typically from the Ekman and Friesen Pictures of Facial Affect or similar validated sets) and identify the emotion portrayed. The standard set includes six basic emotions (anger, disgust, fear, happiness, sadness, surprise) plus neutral. Accuracy and RT are measured across emotion categories. The task engages a network including the amygdala (particularly for fear), fusiform face area, superior temporal sulcus, and prefrontal cortex. It is widely used in clinical research on schizophrenia, autism, and mood disorders.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>
- **Emotional aspect:** <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>, <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
- **Social aspect:** <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>, <a href="vocabulary.html#setting-stimulus-intensity">stimulus intensity</a>
- **Material:** Photographs of faces of varying race and gender showing one of six basic emotions or a neutral expression, from validated sets such as Ekman and Friesen's.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants view face photographs displaying basic emotions and identify the expressed emotion from a fixed set (happy, sad, angry, fearful, disgusted, surprised, neutral).
* - **Manipulations**
  - - Emotion category
    - Expression intensity (morphed continua)
    - Presentation duration
    - Face race/gender
    - Stimulus format (dynamic video vs. still photograph)
    - Context cue (congruent or conflicting body posture or scene)
* - **Measurements**
  - - Accuracy per emotion
    - Confusion matrices
    - Unbiased hit rate
    - RT
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
* - Dynamic Expressions

    `hedvar_facial_emotion_recognition__dynamic_expressions`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>
  - -
  - The face is a short video unfolding from neutral to full expression instead of a still photograph.
* - Emotion-in-Context

    `hedvar_facial_emotion_recognition__emotion_in_context`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
  - [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
  - A body posture or scene that agrees or conflicts with the expression accompanies the face, so there is now a neighbouring item to disregard while labelling the face.
* - Expression Matching

    `hedvar_facial_emotion_recognition__expression_matching`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-compare">compare</a>
  - -
  - The participant decides whether two faces show the same expression, or picks the match to a target face, instead of naming a category.
* - Dimensional Ratings

    `hedvar_facial_emotion_recognition__dimensional_ratings`
  - named form
  - -
  - The participant places each face on continuous scales (pleasantness, arousal) instead of choosing an emotion category.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)

## Key references

- Ekman, P., & Friesen, W. V. (1976). *Pictures of Facial Affect*. Palo Alto, CA: Consulting Psychologists Press.
- Adolphs, R., Tranel, D., Damasio, H., & Damasio, A. (1994). Impaired recognition of emotion in facial expressions following bilateral damage to the human amygdala. *Nature*, 372(6507), 669-672. ([DOI](https://doi.org/10.1038/372669a0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7990957/))

## Further references

- Calvo, M. G., & Nummenmaa, L. (2016). Perceptual and affective mechanisms in facial expression recognition: An integrative review. *Cognition and Emotion*, 30(6), 1081-1106. ([DOI](https://doi.org/10.1016/b978-0-12-800951-2.00016-9))
- Kret, M. E., & De Gelder, B. (2012). A review on sex differences in processing emotional signals. *Neuropsychologia*, 50(7), 1211-1221. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2011.12.022), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22245006/))
- Dobs, K., Isik, L., Pantazis, D., & Kanwisher, N. (2019). How face perception unfolds over time. *Nature Communications*, 10(1), 1258. ([DOI](https://doi.org/10.1038/s41467-019-09239-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30890707/))
- Palermo, R., & Rhodes, G. (2007). Are you always on my mind? A review of how face perception and attention interact. *Neuropsychologia*, 45(1), 75-92. [Updated: Barrett, L. F., Adolphs, R., Marsella, S., Martinez, A. M., & Pollak, S. D. (2019). Emotional expressions reconsidered: Challenges to inferring emotion from human facial movements. *Psychological Science in the Public Interest*, 20(1), 1-68.] ([DOI](https://doi.org/10.1016/j.neuropsychologia.2006.04.025), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16797607/))

## External links

- Cognitive Atlas: [Emotion Recognition Task](https://www.cognitiveatlas.org/task/id/trm_50f734f86b11a) (close match)

- CogPO: [Face Monitor or Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Face_Monitor_or_Discrimination_Paradigm) (close match)

