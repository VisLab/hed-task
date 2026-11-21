(hedtsk_affective_priming)=
# Affective Priming Task

**HED task ID:** `hedtsk_affective_priming`

**Family:** [Emotion elicitation and regulation tasks](families/emotion.md) (also [Conflict and interference tasks](families/conflict_and_interference.md))

**Also known as:** Evaluative Priming

Target evaluation (good/bad) preceded by a briefly presented affective prime; response facilitation on congruent trials indexes automatic evaluation.

## Description

Participants categorize target stimuli (e.g., judge words as "good" or "bad") that are immediately preceded by briefly presented prime stimuli (words, faces, or images) of matching or mismatching emotional valence. The affective priming effect (faster RT for congruent vs. incongruent prime-target pairs) reflects automatic activation of evaluative representations. Subliminal variants (very brief prime exposure) provide evidence for unconscious emotional processing.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-preceding-prime">preceding prime</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>, <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** A briefly shown prime (a word, face or image of positive or negative valence) followed by a target word to be judged good or bad.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A briefly presented prime (word, face, or image with positive or negative valence) is followed by a target that participants evaluate as good/bad or classify.
* - **Manipulations**
  - - Congruence between prime valence and target valence
    - Prime duration and SOA
    - Prime and target type (words, emotional pictures, emotional faces)
* - **Measurements**
  - - RT and accuracy for target evaluation
    - Congruency effect (faster on congruent trials) indexes automatic affective evaluation
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
* - Pronunciation/Naming

    `hedvar_affective_priming__pronunciation_naming`
  - emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-identify">identify</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)
  - The participant reads the target word aloud instead of judging its valence, so the response names the word itself rather than its category.
* - Picture-Word Priming

    `hedvar_affective_priming__picture_word_priming`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - -
  - The prime is an emotional photograph instead of a word; the target word is still judged good or bad.
* - Face-Face Priming

    `hedvar_affective_priming__face_face_priming`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
  - Both prime and target are emotional faces and the target's expression is classified (happy or angry) instead of a word being judged good or bad.
* - Cross-Modal Affective Priming

    `hedvar_affective_priming__cross_modal_affective_priming`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>, <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The prime is heard through headphones while the target is a written word; the judgment is unchanged.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Affective priming](../processes/emotion_perception_and_regulation.md#hed-affective-priming)
- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)
- [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict)

## Key references

- Fazio, R. H., Sanbonmatsu, D. M., Powell, M. C., & Kardes, F. R. (1986). On the automatic activation of attitudes. *Journal of Personality and Social Psychology*, 50(2), 229-238. ([DOI](https://doi.org/10.1037/0022-3514.50.2.229))
- Hermans, D., De Houwer, J., & Eelen, P. (2001). A time course analysis of the affective priming effect. *Cognition and Emotion*, 15(2), 143-165. ([DOI](https://doi.org/10.1080/02699930125768))
- Murphy, S. T., & Zajonc, R. B. (1993). Affect, cognition, and awareness: Affective priming with optimal and suboptimal stimulus exposures. *Journal of Personality and Social Psychology*, 64(5), 723-739. ([DOI](https://doi.org/10.1037/0022-3514.64.5.723), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8505704/))

## Further references

- Herring, D. R., White, K. R., Jabeen, L. N., Hinojos, M., Terrazas, G., Reyes, S. M., Taylor, J. H., & Crites, S. L. (2013). On the automatic activation of attitudes: A quarter century of evaluative priming research. *Psychological Bulletin*, 139(5), 1062-1089. ([DOI](https://doi.org/10.1037/a0031309), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23339522/))
- De Houwer, J., Teige-Mocigemba, S., Spruyt, A., & Moors, A. (2009). Implicit measures: A normative analysis and review. *Psychological Bulletin*, 135(3), 347-368. ([DOI](https://doi.org/10.1037/a0014211), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19379018/))
- Fazio, R. H. (2001). On the automatic activation of associated evaluations: An overview. *Cognition and Emotion*, 15(2), 115-141. ([DOI](https://doi.org/10.1080/02699930125908))

