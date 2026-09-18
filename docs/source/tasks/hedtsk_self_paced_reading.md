(hedtsk_self_paced_reading)=
# Self-Paced Reading Task

**HED task ID:** `hedtsk_self_paced_reading`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Moving-Window Reading Task, Word-by-Word Reading Task, Non-Cumulative Self-Paced Reading, Cumulative Self-Paced Reading, Phrase-by-Phrase Reading Task

Participants press a key to reveal each word or phrase of a sentence/passage; reading time per region indexes online processing difficulty and is sensitive to syntactic, semantic, and discourse-level manipulations.

## Description

Self-Paced Reading is the primary behavioral paradigm for studying online language comprehension at the sentence and discourse level. Participants read text presented one word or phrase at a time by pressing a button to advance; the time between button presses at each region is the dependent measure. In the non-cumulative (moving-window) variant, each new word replaces the previous one; in the cumulative variant, words accumulate on screen. Reading time elevations at critical regions reveal processing difficulty caused by syntactic ambiguity (garden-path effects), semantic anomaly, coherence breaks, anaphor resolution, predictability violations, and discourse-level inference demands. The paradigm was developed as an accessible alternative to eye-tracking that preserves the temporal dynamics of incremental comprehension while requiring minimal equipment. Spillover effects (elevated reading times on words following the critical region) are routinely analyzed. Comprehension questions after each trial ensure participants are reading for meaning. Self-paced reading has been central to testing models of sentence processing (surprisal theory, expectation-based parsing), discourse representation theory (situation models), and cross-linguistic processing differences.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants read sentences or passages presented one word or phrase at a time, advancing by button press; reading time at each region is recorded. Comprehension questions follow each trial.
* - **Manipulation**
  - Linguistic manipulation at the critical region: syntactic ambiguity (reduced relative clause, garden-path), semantic plausibility (plausible vs. implausible continuation), discourse coherence (coherent vs. incoherent continuation), anaphor type (pronoun, repeated name, definite NP), word predictability (high vs. low cloze probability), syntactic complexity (embedded clause, long-distance dependency).
* - **Measurement**
  - Reading time at the critical region (ms); spillover reading time (region + 1, + 2); wrap-up effects (sentence-final reading time); comprehension question accuracy; reading time differences between conditions at the critical region.
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
* - Non-Cumulative (Moving Window)

    `hedvar_self_paced_reading__non_cumulative_moving_window`
  - Each word replaces the previous one; only the current word is visible. Dashes mark unrevealed positions. The standard variant; prevents regressions.
  - Canonical word-by-word presentation without previous words visible
* - Cumulative Self-Paced Reading

    `hedvar_self_paced_reading__cumulative_self_paced_reading`
  - Each new word is added to the display; all previously read words remain visible. Allows re-reading of prior context; more natural but harder to control.
  - Words accumulate on screen; different visual context during reading
* - Phrase-by-Phrase Presentation

    `hedvar_self_paced_reading__phrase_by_phrase_presentation`
  - Text revealed in multi-word chunks (syntactic constituents). Reduces noise from word-level variability; captures phrase-level processing.
  - Phrases instead of words; different chunking of presentation
* - Maze Task

    `hedvar_self_paced_reading__maze`
  - At each position, participants choose between two words (the correct continuation and a distractor). Forced choice at each step; eliminates spillover artifacts. Boyce et al. (2020).
  - Word-by-word forced choice between correct and anomalous continuation; different response structure
* - Cross-Modal Self-Paced Listening

    `hedvar_self_paced_reading__cross_modal_self_paced_listening`
  - Auditory version: participants control the pace of listening to segments of spoken sentences. Less common than visual; used in speech processing research.
  - Auditory presentation instead of visual; different sensory modality
* - Passage-Level Self-Paced Reading

    `hedvar_self_paced_reading__passage_level_self_paced_reading`
  - Multi-sentence passages rather than isolated sentences. Enables study of discourse coherence, bridging inferences, and situation model construction.
  - Full passages instead of sentences; different text-level processing
```

## Cognitive processes

This task is designed to engage the following processes:

- [Discourse processing](../processes/language_comprehension_and_production.md#hed-discourse-processing)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Word recognition](../processes/language_comprehension_and_production.md#hed-word-recognition)

## Key references

- Just, M. A., Carpenter, P. A., & Woolley, J. D. (1982). Paradigms and processes in reading comprehension. Journal of Experimental Psychology: General, 111(2), 228-238.
- Ferreira, F., & Clifton, C. (1986). The independence of syntactic processing. Journal of Memory and Language, 25(3), 348-368.

## Recent references

- Jegerski, J. (2014). Self-paced reading. In J. Jegerski & B. VanPatten (Eds.), Research Methods in Second Language Psycholinguistics (pp. 20-49). Routledge.
- Vasishth, S., & Nicenboim, B. (2016). Statistical methods for linguistic research: Foundational ideas -- Part I. Language and Linguistics Compass, 10(8), 349-369.
- Smith, N. J., & Levy, R. (2013). The effect of word predictability on reading time is logarithmic. Cognition, 128(3), 302-319.
- Boyce, V., Futrell, R., & Levy, R. P. (2020). Maze made easy: Better and easier measurement of incremental processing difficulty. Journal of Memory and Language, 111, 104082.

