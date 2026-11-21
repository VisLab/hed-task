(hedtsk_verb_generation)=
# Verb Generation Task

**HED task ID:** `hedtsk_verb_generation`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Verb Gen, Verb Generation

Produce a verb associated with each presented noun; indexes lexical-semantic retrieval and inhibition of prepotent responses, with well-known left-prefrontal activation.

## Description

The Verb Generation Task is a semantic retrieval and language production paradigm. Participants see or hear a concrete noun (e.g., "hammer") and must generate an associated verb (e.g., "hit" or "pound"). The task requires accessing semantic knowledge, selecting among competing responses, and executing a language production response. It robustly activates left inferior frontal gyrus (Broca's area) and anterior cingulate cortex, and is one of the most frequently used language tasks in neuroimaging. Performance is measured by response latency, accuracy, and the specificity/typicality of verb selections.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-generate">generate</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Concrete nouns (such as hammer), seen or heard, varying in imageability, frequency and number of competing verb associates.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A concrete noun is presented (e.g., HAMMER).
    2. Participants generate an associated verb (e.g., 'hit' or 'pound') as quickly as possible.
    3. Optional: The same noun list is repeated across blocks until responses become automatic, then a new list is introduced.
* - **Manipulations**
  - - Noun imageability and frequency
    - Number of competing verb associates
    - Repetition (novel vs. repeated nouns)
    - Overt vs. covert generation
    - Task direction (generate a noun for a verb vs. a verb for a noun)
* - **Measurements**
  - - Response latency
    - Competition effect (slower for nouns with many associates)
    - Repetition suppression
    - fMRI left IFG (Broca's area) activation
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
* - Covert Verb Generation

    `hedvar_verb_generation__covert_verb_generation`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - -
  - The verb is thought but not spoken and a key press marks when it has come to mind, to avoid speech movement in the scanner.
* - Written Verb Generation

    `hedvar_verb_generation__written_verb_generation`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - -
  - The verb is typed or written instead of spoken.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Language production](../processes/language_comprehension_and_production.md#hed-language-production)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)
- [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)

## Key references

- Petersen, S. E., Fox, P. T., Posner, M. I., Mintun, M., & Raichle, M. E. (1988). Positron emission tomographic studies of the cortical anatomy of single-word processing. *Nature*, 331(6157), 585-589. ([DOI](https://doi.org/10.1038/331585a0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/3277066/))
- Thompson-Schill, S. L., D'Esposito, M., Aguirre, G. K., & Farah, M. J. (1997). Role of left inferior prefrontal cortex in retrieval of semantic knowledge: A reevaluation. *Proceedings of the National Academy of Sciences*, 94(26), 14792-14797. ([DOI](https://doi.org/10.1073/pnas.94.26.14792), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9405692/))
- Raichle, M. E., Fiez, J. A., Videen, T. O., MacLeod, A. M. K., Pardo, J. V., Fox, P. T., & Petersen, S. E. (1994). Practice-related changes in human brain functional anatomy during nonmotor learning. *Cerebral Cortex*, 4(1), 8-26. ([DOI](https://doi.org/10.1093/cercor/4.1.8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8180494/))

## Further references

- Snyder, H. R., Feigenson, K., & Thompson-Schill, S. L. (2007). Prefrontal cortical response to conflict during semantic and phonological tasks. *Journal of Cognitive Neuroscience*, 19(5), 761-775. ([DOI](https://doi.org/10.1162/jocn.2007.19.5.761), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17488203/))
- Martin, R. C., & Cheng, Y. (2006). Selection demands versus association strength in the verb generation task. *Psychonomic Bulletin & Review*, 13(3), 396-401. ([DOI](https://doi.org/10.3758/bf03193859), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17048721/))
- Perret, C., & Laganaro, M. (2012). Comparison of electrophysiological correlates of writing and speaking: A topographic ERP analysis. *Brain Topography*, 25(1), 64-72. ([DOI](https://doi.org/10.1007/s10548-011-0200-3))
- Crescentini, C., Shallice, T., & Macaluso, E. (2010). Item retrieval and competition in noun and verb generation: An FMRI study. *Journal of Cognitive Neuroscience*, 22(6), 1140-1157. ([DOI](https://doi.org/10.1162/jocn.2009.21255), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19413479/))

## External links

- Cognitive Atlas: [verb generation task](https://www.cognitiveatlas.org/task/id/trm_4f24183fe80c6)

- CogPO: [Word Generation (Overt) Paradigm](http://www.wiki.cogpo.org/index.php?title=Word_Generation_%28Overt%29_Paradigm) (close match)

