(hedtsk_verb_generation)=
# Verb Generation Task

**HED task ID:** `hedtsk_verb_generation`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Verb Gen, Verb Generation

Produce a verb associated with each presented noun; indexes lexical-semantic retrieval and inhibition of prepotent responses, with well-known left-prefrontal activation.

## Description

The Verb Generation Task is a semantic retrieval and language production paradigm. Participants see or hear a concrete noun (e.g., "hammer") and must generate an associated verb (e.g., "hit" or "pound"). The task requires accessing semantic knowledge, selecting among competing responses, and executing a language production response. It robustly activates left inferior frontal gyrus (Broca's area) and anterior cingulate cortex, and is one of the most frequently used language tasks in neuroimaging. Performance is measured by response latency, accuracy, and the specificity/typicality of verb selections.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A concrete noun is presented (e.g., HAMMER).
    2. Participants generate an associated verb (e.g., 'hit' or 'pound') as quickly as possible.
* - **Manipulations**
  - - Noun imageability and frequency
    - Number of competing verb associates
    - Repetition (novel vs. repeated nouns)
    - Overt vs. covert generation
* - **Measurements**
  - - Response latency
    - Competition effect (slower for nouns with many associates)
    - Repetition suppression
    - FMRI left IFG (Broca's area) activation
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
* - Standard Overt Verb Generation

    `hedvar_verb_generation__standard_overt_verb_generation`
  - See noun, say verb aloud; used in PET and behavioral studies.
  - Canonical Petersen et al.: say verb aloud in response to noun
* - Covert Verb Generation

    `hedvar_verb_generation__covert_verb_generation`
  - Generate verb silently; preferred in fMRI to avoid motion artifacts.
  - Internal silent generation; different response mode
* - High vs. Low Selection Demand

    `hedvar_verb_generation__high_vs_low_selection_demand`
  - Nouns with many competing verbs (high selection: "cat") vs. one dominant verb (low selection: "scissors"); manipulates executive demand.
  - Dominant vs. non-dominant verb associations; tests selection difficulty
* - Verb Generation with Practice

    `hedvar_verb_generation__verb_generation_with_practice`
  - Repeated presentation of same nouns; measuring automatization and practice-related prefrontal deactivation.
  - Repeated generation reduces demand; tests automatization
* - Noun Generation (Reverse)

    `hedvar_verb_generation__noun_generation_reverse`
  - Given a verb, generate a noun; control condition.
  - Generate noun to verb cue; reversed direction
* - Written Verb Generation

    `hedvar_verb_generation__written_verb_generation`
  - Typed or handwritten responses; captures production pathway.
  - Written response instead of vocal; different response modality
```

## Cognitive processes

This task is designed to engage the following processes:

- [Language production](../processes/language_comprehension_and_production.md#hed-language-production)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)
- [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)

## Key references

- Petersen, S. E., Fox, P. T., Posner, M. I., Mintun, M., & Raichle, M. E. (1988). Positron emission tomographic studies of the cortical anatomy of single-word processing. *Nature*, 331(6157), 585–589. ([DOI](https://doi.org/10.1038/331585a0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/3277066/))
- Thompson-Schill, S. L., D'Esposito, M., Aguirre, G. K., & Farah, M. J. (1997). Role of left inferior prefrontal cortex in retrieval of semantic knowledge: A reevaluation. *Proceedings of the National Academy of Sciences*, 94(26), 14792–14797. ([DOI](https://doi.org/10.1073/pnas.94.26.14792), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9405692/))
- Raichle, M. E., Fiez, J. A., Videen, T. O., MacLeod, A. M. K., Pardo, J. V., Fox, P. T., & Petersen, S. E. (1994). Practice-related changes in human brain functional anatomy during nonmotor learning. *Cerebral Cortex*, 4(1), 8–26. ([DOI](https://doi.org/10.1093/cercor/4.1.8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8180494/))

## Further references

- Snyder, H. R., Feigenson, K., & Thompson-Schill, S. L. (2007). Prefrontal cortical response to conflict during semantic and phonological tasks. *Journal of Cognitive Neuroscience*, 19(5), 761–775. ([DOI](https://doi.org/10.1162/jocn.2007.19.5.761), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17488203/))
- Martin, R. C., & Cheng, Y. (2006). Selection demands versus association strength in the verb generation task. *Psychonomic Bulletin & Review*, 13(3), 396–401. ([DOI](https://doi.org/10.3758/bf03193859), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17048721/))
- Perret, C., & Laganaro, M. (2012). Comparison of electrophysiological correlates of writing and speaking: A topographic ERP analysis. *Brain Topography*, 25(1), 64–72. ([DOI](https://doi.org/10.1007/s10548-011-0200-3))
- Crescentini, C., Shallice, T., & Macaluso, E. (2010). Item retrieval and competition in noun and verb generation: An FMRI study. *Journal of Cognitive Neuroscience*, 22(6), 1140–1157. ([DOI](https://doi.org/10.1162/jocn.2009.21255), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19413479/))

## External links

- Cognitive Atlas: [verb generation task](https://www.cognitiveatlas.org/task/id/trm_4f24183fe80c6)

- CogPO: [Word Generation (Overt) Paradigm](http://www.wiki.cogpo.org/index.php?title=Word_Generation_%28Overt%29_Paradigm) (close match)

