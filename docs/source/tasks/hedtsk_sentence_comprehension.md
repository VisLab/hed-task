(hedtsk_sentence_comprehension)=
# Sentence Comprehension Task

**HED task ID:** `hedtsk_sentence_comprehension`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Garden-Path Reading, Syntactic Ambiguity Task

Reading or listening to locally ambiguous sentences; reading-time disruptions and offline comprehension indexes syntactic reanalysis.

## Description

Participants read sentences containing temporary syntactic ambiguities (garden-path sentences) that initially lead to an incorrect parse before disambiguating information forces reanalysis. Classic example: "The horse raced past the barn fell." Sentences may be presented word-by-word (self-paced reading) or while eye movements are tracked. Comprehension is assessed via subsequent questions. Neuroimaging reveals left inferior frontal and temporal activation during syntactic reanalysis. The task probes how the parser uses syntactic, semantic, and probabilistic cues in real-time language processing.

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
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Written sentences with a temporary syntactic ambiguity (garden-path sentences such as The horse raced past the barn fell), varying in ambiguity type, disambiguation point, plausibility and preceding context.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants read sentences word-by-word or in regions.
    2. Some sentences contain temporary syntactic ambiguities that lead the reader down a wrong parse (garden path) before disambiguation.
* - **Manipulations**
  - - Ambiguity type (main verb/reduced relative, NP/S, etc.)
    - Disambiguation point
    - Plausibility
    - Context sentences
    - Response signal lag after the sentence
* - **Measurements**
  - - Reading time at disambiguating region (self-paced reading, eye tracking)
    - Regression probability
    - ERP (P600, N400)
    - Comprehension question accuracy
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
* - Eye-Tracking Reading

    `hedvar_sentence_comprehension__eye_tracking_reading`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-eye-tracker">eye tracker</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - -
  - The whole sentence is shown at once and gaze is recorded instead of key-press reading times.
* - Speed-Accuracy Tradeoff (SAT) Studies

    `hedvar_sentence_comprehension__speed_accuracy_tradeoff_sat_studies`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>; report after: <a href="vocabulary.html#rule-experience-passively-report-after-judgment">judgment</a>
  - -
  - The participant judges each sentence's acceptability at a response signal that comes at one of several delays after the sentence ends.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Syntactic parsing](../processes/language_comprehension_and_production.md#hed-syntactic-parsing)
- [Sentence comprehension](../processes/language_comprehension_and_production.md#hed-sentence-comprehension)
- [Language comprehension](../processes/language_comprehension_and_production.md#hed-language-comprehension)
- [Reading](../processes/language_comprehension_and_production.md#hed-reading)
- [Error detection](../processes/inhibitory_control_and_conflict_monitoring.md#hed-error-detection)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)

## Key references

- Frazier, L., & Rayner, K. (1982). Making and correcting errors during sentence comprehension: Eye movements in the analysis of structurally ambiguous sentences. *Cognitive Psychology*, 14(2), 178-210. ([DOI](https://doi.org/10.1016/0010-0285(82)90008-1))
- Friederici, A. D. (2002). Towards a neural basis of auditory sentence processing. *Trends in Cognitive Sciences*, 6(2), 78-84. ([DOI](https://doi.org/10.1016/s1364-6613(00)01839-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15866191/))
- Novick, J. M., Trueswell, J. C., & Thompson-Schill, S. L. (2005). Cognitive control and parsing: Reexamining the role of Broca's area in sentence comprehension. *Cognitive, Affective, & Behavioral Neuroscience*, 5(3), 263-281. ([DOI](https://doi.org/10.3758/cabn.5.3.263), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16396089/))

## Further references

- Levy, R. (2008). Expectation-based syntactic comprehension. *Cognition*, 106(3), 1126-1177. ([DOI](https://doi.org/10.1016/j.cognition.2007.05.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17662975/))
- Fedorenko, E., & Thompson-Schill, S. L. (2014). Reworking the language network. *Trends in Cognitive Sciences*, 18(3), 120-126. ([DOI](https://doi.org/10.1016/j.tics.2013.12.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24440115/))
- Staub, A. (2015). The effect of lexical predictability on eye movements in reading: Critical review and theoretical interpretation. *Language and Linguistics Compass*, 9(8), 311-327. ([DOI](https://doi.org/10.1111/lnc3.12151))

## External links

- CogPO: [Syntactic Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Syntactic_Discrimination_Paradigm) (close match)

