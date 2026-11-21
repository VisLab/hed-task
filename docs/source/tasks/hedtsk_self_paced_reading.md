(hedtsk_self_paced_reading)=
# Self-Paced Reading Task

**HED task ID:** `hedtsk_self_paced_reading`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Moving-Window Reading Task, Word-by-Word Reading Task, Non-Cumulative Self-Paced Reading, Cumulative Self-Paced Reading, Phrase-by-Phrase Reading Task

Participants press a key to reveal each word or phrase of a sentence/passage; reading time per region indexes online processing difficulty and is sensitive to syntactic, semantic, and discourse-level manipulations.

## Description

Self-Paced Reading is the primary behavioral paradigm for studying online language comprehension at the sentence and discourse level. Participants read text presented one word or phrase at a time by pressing a button to advance; the time between button presses at each region is the dependent measure. In the non-cumulative (moving-window) variant, each new word replaces the previous one; in the cumulative variant, words accumulate on screen. Reading time elevations at critical regions reveal processing difficulty caused by syntactic ambiguity (garden-path effects), semantic anomaly, coherence breaks, anaphor resolution, predictability violations, and discourse-level inference demands. The paradigm was developed as an accessible alternative to eye-tracking that preserves the temporal dynamics of incremental comprehension while requiring minimal equipment. Spillover effects (elevated reading times on words following the critical region) are routinely analyzed. Comprehension questions after each trial ensure participants are reading for meaning. Self-paced reading has been central to testing models of sentence processing (surprisal theory, expectation-based parsing), discourse representation theory (situation models), and cross-linguistic processing differences.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-experience-passively">Experience passively</a> (`experience_passively`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *Is anything asked afterwards?* <a href="vocabulary.html#rule-experience-passively-report-after-comprehension-question">comprehension question</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-text">text</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Sentences or passages revealed one word or phrase at a time, with a comprehension question after each.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants read sentences or passages presented one word or phrase at a time, advancing by button press.
    2. Reading time at each region is recorded.
    3. Comprehension questions follow each trial.
* - **Manipulations**
  - - Syntactic ambiguity at the critical region (reduced relative clause, garden-path)
    - Semantic plausibility (plausible vs. implausible continuation)
    - Discourse coherence (coherent vs. incoherent continuation)
    - Anaphor type (pronoun, repeated name, definite NP)
    - Word predictability (high vs. low cloze probability)
    - Syntactic complexity (embedded clause, long-distance dependency)
    - Reading unit (phrase or clause vs. single word)
    - Text length (single sentence vs. multi-sentence passage)
* - **Measurements**
  - - Reading time at the critical region (ms)
    - Spillover reading time (region + 1, + 2)
    - Wrap-up effects (sentence-final reading time)
    - Comprehension question accuracy
    - Reading time differences between conditions at the critical region
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
* - Cumulative Self-Paced Reading

    `hedvar_self_paced_reading__cumulative_self_paced_reading`
  - named form
  - -
  - Earlier words stay on screen after each press so the reader can look back.
* - Maze Task

    `hedvar_self_paced_reading__maze`
  - combined with: <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (A two-alternative continuation choice at every word)
  - -
  - At every position two words are shown and the participant chooses the one that continues the sentence correctly, so choice time replaces reading time.
* - Cross-Modal Self-Paced Listening

    `hedvar_self_paced_reading__cross_modal_self_paced_listening`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The sentence is spoken in segments and each press plays the next segment.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Discourse processing](../processes/language_comprehension_and_production.md#hed-discourse-processing)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Word recognition](../processes/language_comprehension_and_production.md#hed-word-recognition)

## Key references

- Just, M. A., Carpenter, P. A., & Woolley, J. D. (1982). Paradigms and processes in reading comprehension. Journal of Experimental Psychology: General, 111(2), 228-238. ([DOI](https://doi.org/10.1037/0096-3445.111.2.228), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6213735/))
- Ferreira, F., & Clifton, C. (1986). The independence of syntactic processing. Journal of Memory and Language, 25(3), 348-368. ([DOI](https://doi.org/10.1016/0749-596x(86)90006-9))

## Further references

- Jegerski, J. (2014). Self-paced reading. In J. Jegerski & B. VanPatten (Eds.), Research Methods in Second Language Psycholinguistics (pp. 20-49). Routledge. ([DOI](https://doi.org/10.4324/9780203123430))
- Vasishth, S., & Nicenboim, B. (2016). Statistical methods for linguistic research: Foundational ideas -- Part I. Language and Linguistics Compass, 10(8), 349-369. ([DOI](https://doi.org/10.1111/lnc3.12201))
- Smith, N. J., & Levy, R. (2013). The effect of word predictability on reading time is logarithmic. Cognition, 128(3), 302-319. ([DOI](https://doi.org/10.1016/j.cognition.2013.02.013), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23747651/))
- Boyce, V., Futrell, R., & Levy, R. P. (2020). Maze made easy: Better and easier measurement of incremental processing difficulty. Journal of Memory and Language, 111, 104082. ([DOI](https://doi.org/10.1016/j.jml.2019.104082))

## External links

- CogPO: [Reading (Covert) Paradigm](http://www.wiki.cogpo.org/index.php?title=Reading_%28Covert%29_Paradigm) (close match)

