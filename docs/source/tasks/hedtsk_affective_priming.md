(hedtsk_affective_priming)=
# Affective Priming Task

**HED task ID:** `hedtsk_affective_priming`

**Family:** [Emotion elicitation and regulation tasks](families/emotion.md) (also [Conflict and interference tasks](families/conflict_and_interference.md))

**Also known as:** Evaluative Priming

Target evaluation (good/bad) preceded by a briefly presented affective prime; response facilitation on congruent trials indexes automatic evaluation.

## Description

Participants categorize target stimuli (e.g., judge words as "good" or "bad") that are immediately preceded by briefly presented prime stimuli (words, faces, or images) of matching or mismatching emotional valence. The affective priming effect (faster RT for congruent vs. incongruent prime-target pairs) reflects automatic activation of evaluative representations. Subliminal variants (very brief prime exposure) provide evidence for unconscious emotional processing.

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
* - **Measurements**
  - - RT and accuracy for target evaluation
    - Congruency effect (faster on congruent trials) indexes automatic affective evaluation
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
* - Evaluative Decision (Good/Bad)

    `hedvar_affective_priming__evaluative_decision_good_bad`
  - A brief positive or negative prime (a word or picture) is followed by a target word, and the participant presses one key if the target is good or pleasant and another if it is bad or unpleasant. Responses are faster when prime and target share the same valence. This is the most common form of the task.
  - Participant makes explicit valence judgment; changes response task from standard LDT
* - Pronunciation/Naming

    `hedvar_affective_priming__pronunciation_naming`
  - After the prime, the participant reads the target word aloud as quickly as possible instead of judging it. Naming time is shorter when the prime and target have the same valence, so priming is measured without asking the participant to evaluate anything.
  - Vocal naming response instead of evaluative judgment; different output modality and response event
* - Subliminal Priming

    `hedvar_affective_priming__subliminal_priming`
  - The prime is flashed so briefly (typically under 30 ms) and is immediately covered by a mask, so the participant cannot consciously see it. The participant then evaluates the visible target as usual. Any priming effect must arise from processing the participant is not aware of.
  - Prime below conscious threshold; changes stimulus timing structure and awareness conditions
* - Picture-Word Priming

    `hedvar_affective_priming__picture_word_priming`
  - The prime is an emotional photograph rather than a word, and the target is a word to be evaluated. The participant sees a picture briefly, then a word, and judges the word as good or bad.
  - Visual picture prime instead of word; different stimulus type with distinct semantic processing
* - Face-Face Priming

    `hedvar_affective_priming__face_face_priming`
  - Both the prime and the target are faces with emotional expressions. The participant sees a brief face, then a second face, and judges the second face's expression (for example happy or angry).
  - Social/facial stimuli as both prime and target; structurally distinct from word-prime paradigm
* - Cross-Modal Affective Priming

    `hedvar_affective_priming__cross_modal_affective_priming`
  - The prime is heard rather than seen, for example a spoken word or an emotional sound, and the target is a visible word. The participant judges the written target while the prime arrives through headphones.
  - Auditory prime + visual target; cross-modal structure creates distinct event types
* - Masked vs. Unmasked Priming

    `hedvar_affective_priming__masked_vs_unmasked_priming`
  - The same prime-target pairs are run in two conditions: one where the prime is clearly visible and one where it is masked and too brief to be seen. Comparing the two separates fast automatic priming from priming that depends on the participant noticing the prime and using it strategically.
  - Systematic masking manipulation changes prime visibility and conscious access to prime
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

- Herring, D. R., White, K. R., Jabeen, L. N., Hinojos, M., Terrazas, G., Reyes, S. M., Taylor, J. H., & Crites, S. L. (2013). On the automatic activation of attitudes: A quarter century of evaluative priming research. *Psychological Bulletin*, 139(5), 1062–1089. ([DOI](https://doi.org/10.1037/a0031309), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23339522/))
- De Houwer, J., Teige-Mocigemba, S., Spruyt, A., & Moors, A. (2009). Implicit measures: A normative analysis and review. *Psychological Bulletin*, 135(3), 347–368. ([DOI](https://doi.org/10.1037/a0014211), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19379018/))
- Fazio, R. H. (2001). On the automatic activation of associated evaluations: An overview. *Cognition and Emotion*, 15(2), 115–141. ([DOI](https://doi.org/10.1080/02699930125908))

