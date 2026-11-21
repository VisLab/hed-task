(hedtsk_verbal_fluency)=
# Verbal Fluency Task

**HED task ID:** `hedtsk_verbal_fluency`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** FAS Test, Controlled Oral Word Association Test, COWAT, Letter Fluency, Phonemic Fluency, Category Fluency, Semantic Fluency

Generate as many words as possible within a time limit matching a phonemic (letter) or semantic (category) constraint; production count and clustering/switching patterns index executive-lexical retrieval.

## Description

Participants produce as many unique words as possible in a fixed interval (typically 60 seconds) that satisfy a constraint: a starting letter (phonemic/letter fluency, e.g., F, A, S) or a semantic category (e.g., animals, fruits). Phonemic fluency loads heavily on left frontal executive systems involved in strategic search and self-monitoring, while semantic fluency additionally engages temporal-lobe semantic stores. Beyond raw word count, temporal analyses of clustering (runs of semantically or phonemically similar words) and switching (transitions between clusters) dissociate automatic retrieval from effortful executive search. Verbal fluency is one of the most widely administered neuropsychological tasks, sensitive to frontal-lobe lesions, neurodegenerative disease (especially Alzheimer's vs. frontotemporal dementia), schizophrenia, and normal aging. Its brevity, minimal equipment needs, and robust normative data make it a cornerstone of clinical assessment batteries.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-solve-problem">Solve a puzzle</a> (`solve_problem`)
- **Game rules:** none are defined for this game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructed-emphasis">instructed emphasis</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-examiner">examiner</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-block-duration">block duration</a>
- **Material:** A starting letter (such as F, A or S) or a semantic category (such as animals) given by the examiner.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participant generates words aloud matching a letter or category constraint within a timed interval.
    2. An examiner records all responses.
* - **Manipulations**
  - - Constraint type (phonemic letter vs. semantic category)
    - Letter difficulty (e.g., F vs. Q)
    - Category breadth (animals vs. tools)
    - Time interval (30 s, 60 s, 90 s)
    - Switching vs. free-generation instructions
    - Response type (drawing designs vs. saying words)
* - **Measurements**
  - - Total correct words
    - Number of perseverations and rule violations
    - Cluster size (mean words per semantic/phonemic cluster)
    - Number of switches between clusters
    - Temporal production curve (words per 15-s quartile)
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
* - Semantic / Category Fluency

    `hedvar_verbal_fluency__semantic_category_fluency`

    Cognitive Atlas: [category fluency test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949923), [semantic fluency task](https://www.cognitiveatlas.org/task/id/trm_4f241bd52b509) (close match)
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - -
  - The constraint is a semantic category such as animals instead of a starting letter.
* - Action / Verb Fluency

    `hedvar_verbal_fluency__action_verb_fluency`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - -
  - The constraint is a grammatical class, verbs for things people can do, a third constraint type beside letter and category.
* - Switching Fluency

    `hedvar_verbal_fluency__switching_fluency`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
  - The participant alternates between two categories word by word for one minute.
* - Design Fluency

    `hedvar_verbal_fluency__design_fluency`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-writing-device">writing device</a>
  - [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - The participant draws as many different designs as possible on a grid of dots, joining dots with a fixed number of lines, instead of saying words.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Verbal fluency](../processes/language_comprehension_and_production.md#hed-verbal-fluency)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Semantic knowledge](../processes/language_comprehension_and_production.md#hed-semantic-knowledge)
- [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring)

## Key references

- Benton, A. L., Hamsher, K., & Sivan, A. B. (1983). *Multilingual Aphasia Examination* (3rd ed.). Iowa City: AJA Associates.
- Troyer, A. K., Moscovitch, M., & Winocur, G. (1997). Clustering and switching as two components of verbal fluency: Evidence from younger and older healthy adults. *Neuropsychology*, 11(1), 138-146. ([DOI](https://doi.org/10.1037/0894-4105.11.1.138), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9055277/))
- Henry, J. D., & Crawford, J. R. (2004). A meta-analytic review of verbal fluency performance following focal cortical lesions. *Neuropsychology*, 18(2), 284-295. ([DOI](https://doi.org/10.1037/0894-4105.18.2.284), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15099151/))

## Further references

- Shao, Z., Janse, E., Visser, K., & Meyer, A. S. (2014). What do verbal fluency tasks measure? Predictors of verbal fluency performance in older adults. *Frontiers in Psychology*, 5, 772. ([DOI](https://doi.org/10.3389/fpsyg.2014.00772), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25101034/))
- Aita, S. L., Beach, J. D., Taylor, S. E., et al. (2019). Executive, language, or both? An examination of the construct validity of verbal fluency measures. *Applied Neuropsychology: Adult*, 26(5), 441-451. ([DOI](https://doi.org/10.1080/23279095.2018.1439830))
- Tallberg, I. M., Ivachova, E., Jones Tinghag, K., & Ostberg, P. (2008). Swedish norms for word fluency tests: FAS, animals and verbs. *Scandinavian Journal of Psychology*, 49(5), 479-485. ([DOI](https://doi.org/10.1111/j.1467-9450.2008.00653.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18452499/))

## External links

- Cognitive Atlas: [verbal fluency task](https://www.cognitiveatlas.org/task/id/trm_4f240f1c740da)

- CogPO: [Word Generation (Overt) Paradigm](http://www.wiki.cogpo.org/index.php?title=Word_Generation_%28Overt%29_Paradigm) (close match)

