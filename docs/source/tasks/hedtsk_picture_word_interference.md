(hedtsk_picture_word_interference)=
# Picture-Word Interference Task

**HED task ID:** `hedtsk_picture_word_interference`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** PWI, Picture-Word Interference (PWI)

Naming of pictures while ignoring a written or spoken distractor word; a word related in meaning slows naming and one similar in sound speeds it.

## Description

A written or spoken word is presented with each picture, and the participant names the picture while ignoring the word. A word related in meaning (cat for a picture of a dog) slows naming; a word that sounds similar (doll) speeds it.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-identify">identify</a>
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Pictures of objects, each with a written or spoken distractor word related in meaning, similar in sound, or unrelated.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A picture of an object is presented together with a written or spoken distractor word.
    2. Participants name the picture aloud as quickly as possible while ignoring the word.
* - **Manipulations**
  - - Distractor relation to the picture name (related in meaning, similar in sound, unrelated)
    - Distractor modality (written vs. spoken)
* - **Measurements**
  - - Naming latency
    - Naming errors
```

## Cognitive processes

This task is designed to engage the following processes:

- [Naming](../processes/language_comprehension_and_production.md#hed-naming)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Language production](../processes/language_comprehension_and_production.md#hed-language-production)
- [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)

## Key references

- Schriefers, H., Meyer, A. S., & Levelt, W. J. M. (1990). Exploring the time course of lexical access in language production: Picture-word interference studies. *Journal of Memory and Language*, 29(1), 86-102. ([DOI](https://doi.org/10.1016/0749-596x(90)90011-n))

## External links

- Cognitive Atlas: [picture-word Stroop test](https://www.cognitiveatlas.org/task/id/trm_4dadbfd771a54) (close match)

