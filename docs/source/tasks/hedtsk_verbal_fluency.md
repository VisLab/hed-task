(hedtsk_verbal_fluency)=
# Verbal Fluency Task

**HED task ID:** `hedtsk_verbal_fluency`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** FAS Test, Controlled Oral Word Association Test, COWAT, Letter Fluency, Phonemic Fluency, Category Fluency, Semantic Fluency

Generate as many words as possible within a time limit matching a phonemic (letter) or semantic (category) constraint; production count and clustering/switching patterns index executive-lexical retrieval.

## Description

Participants produce as many unique words as possible in a fixed interval (typically 60 seconds) that satisfy a constraint: a starting letter (phonemic/letter fluency, e.g., F, A, S) or a semantic category (e.g., animals, fruits). Phonemic fluency loads heavily on left frontal executive systems involved in strategic search and self-monitoring, while semantic fluency additionally engages temporal-lobe semantic stores. Beyond raw word count, temporal analyses of clustering (runs of semantically or phonemically similar words) and switching (transitions between clusters) dissociate automatic retrieval from effortful executive search. Verbal fluency is one of the most widely administered neuropsychological tasks, sensitive to frontal-lobe lesions, neurodegenerative disease (especially Alzheimer's vs. frontotemporal dementia), schizophrenia, and normal aging. Its brevity, minimal equipment needs, and robust normative data make it a cornerstone of clinical assessment batteries.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participant generates words aloud matching a letter or category constraint within a timed interval; an examiner records all responses.
* - **Manipulation**
  - Constraint type (phonemic letter vs. semantic category); letter difficulty (e.g., F vs. Q); category breadth (animals vs. tools); time interval (30 s, 60 s, 90 s); switching vs. free-generation instructions.
* - **Measurement**
  - Total correct words; number of perseverations and rule violations; cluster size (mean words per semantic/phonemic cluster); number of switches between clusters; temporal production curve (words per 15-s quartile).
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
* - Phonemic / Letter Fluency (FAS)

    `hedvar_verbal_fluency__phonemic_letter_fluency_fas`
  - Generate words beginning with a specified letter (typically F, A, S). Loads heavily on left inferior frontal (executive search) systems. The standard clinical measure.
  - Generate words by initial letter; canonical phonemic fluency
* - Semantic / Category Fluency

    `hedvar_verbal_fluency__semantic_category_fluency`
  - Generate exemplars of a semantic category (e.g., animals, fruits, supermarket items). Engages temporal-lobe semantic stores in addition to frontal search. Differentially impaired in Alzheimer's disease vs. frontal lesions.
  - Generate words from category; different retrieval strategy and structure
* - Action / Verb Fluency

    `hedvar_verbal_fluency__action_verb_fluency`
  - Generate verbs (things people can do). More sensitive to frontal-subcortical pathology than noun-based category fluency; emerging as a clinical complement.
  - Generate verbs/actions; different grammatical category
* - Switching Fluency

    `hedvar_verbal_fluency__switching_fluency`
  - Alternate between two categories (e.g., fruit, furniture, fruit, ...) on each successive word. Adds an explicit set-shifting demand beyond simple generation.
  - Alternate between two categories; adds cognitive flexibility demand
* - Design Fluency

    `hedvar_verbal_fluency__design_fluency`
  - Non-verbal analogue: generate novel designs by connecting dots in a grid. Tests figural/spatial fluency and right-hemisphere executive function.
  - Draw novel designs instead of words; different modality
* - Excluded-Letter Fluency

    `hedvar_verbal_fluency__excluded_letter_fluency`
  - Generate words that do NOT contain a specified letter. Adds an inhibitory constraint to the standard phonemic task.
  - Generate words avoiding a letter; adds constraint that changes retrieval strategy
```

## Cognitive processes

This task is designed to engage the following processes:

- [Verbal fluency](../processes/language_comprehension_and_production.md#hed-verbal-fluency)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Semantic knowledge](../processes/language_comprehension_and_production.md#hed-semantic-knowledge)
- [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring)

## Key references

- Benton, A. L., Hamsher, K., & Sivan, A. B. (1983). *Multilingual Aphasia Examination* (3rd ed.). Iowa City: AJA Associates. ([DOI](https://doi.org/10.1037/t10132-000))
- Troyer, A. K., Moscovitch, M., & Winocur, G. (1997). Clustering and switching as two components of verbal fluency: Evidence from younger and older healthy adults. *Neuropsychology*, 11(1), 138-146. ([DOI](https://doi.org/10.1037/0894-4105.11.1.138), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9055277/))
- Henry, J. D., & Crawford, J. R. (2004). A meta-analytic review of verbal fluency performance following focal cortical lesions. *Neuropsychology*, 18(2), 284-295. ([DOI](https://doi.org/10.1037/0894-4105.18.2.284), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15099151/))

## Further references

- Shao, Z., Janse, E., Visser, K., & Meyer, A. S. (2014). What do verbal fluency tasks measure? Predictors of verbal fluency performance in older adults. *Frontiers in Psychology*, 5, 772. ([DOI](https://doi.org/10.3389/fpsyg.2014.00772), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25101034/))
- Aita, S. L., Beach, J. D., Taylor, S. E., et al. (2019). Executive, language, or both? An examination of the construct validity of verbal fluency measures. *Applied Neuropsychology: Adult*, 26(5), 441-451. ([DOI](https://doi.org/10.1093/arclin/acz034.29))
- Tallberg, I. M., Ivachova, E., Jones Tinghag, K., & Ostberg, P. (2008). Swedish norms for word fluency tests: FAS, animals and verbs. *Scandinavian Journal of Psychology*, 49(5), 479-485. ([DOI](https://doi.org/10.1111/j.1467-9450.2008.00653.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18452499/))

## External links

- Cognitive Atlas: [verbal fluency task](https://www.cognitiveatlas.org/task/id/trm_4f240f1c740da)

