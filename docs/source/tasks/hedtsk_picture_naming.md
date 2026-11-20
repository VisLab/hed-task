(hedtsk_picture_naming)=
# Picture Naming Task

**HED task ID:** `hedtsk_picture_naming`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Object Naming, Confrontation Naming

Naming of pictured objects; RT and errors index lexical retrieval and are sensitive to name agreement, frequency, and age of acquisition.

## Description

Participants view photographs or line drawings of common objects, animals, or scenes and name each item aloud as quickly and accurately as possible. Naming latency (RT from stimulus onset to vocal response onset) is the primary measure. The task engages multiple stages of language production: conceptual identification, lemma retrieval, phonological encoding, and articulation. fMRI reveals activation in left inferior frontal regions (Broca's area) and temporal cortex. The task is widely used in aphasia research and studies of language production.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What does the rule ask about each stimulus?** <a href="vocabulary.html#rule-respond-to-rule-rule-asks-identify">identify</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Line drawings or photographs of common objects and animals, varying in object frequency, name agreement and visual complexity.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Line drawings or photographs of objects are presented one at a time.
    2. Participants name each object as quickly as possible.
* - **Manipulations**
  - - Object frequency
    - Name agreement
    - Visual complexity
    - Phonological or semantic context (blocked naming)
    - Response release (delayed go signal vs. immediate naming)
    - Naming language (cued per trial; switch vs. repeat)
    - Retrieval report (know, tip-of-the-tongue, do not know) with partial information
    - Hint after failed naming (first sound or meaning)
* - **Measurements**
  - - Naming latency
    - Error type (semantic, phonological)
    - Frequency and agreement effects
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
* - Blocked-Cyclic Naming

    `hedvar_picture_naming__blocked_cyclic_naming`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - A small picture set is named repeatedly in cycles, in blocks that are all one category or mixed, so that related names compete across trials.
* - Object + Action Naming

    `hedvar_picture_naming__object_action_naming`
  - named form
  - -
  - Pictures of actions are added and the participant names the action with a verb or the object with a noun, in separate or mixed blocks.
* - Bilingual Picture Naming

    `hedvar_picture_naming__bilingual_picture_naming`
  - population: <a href="vocabulary.html#facet-population-bilinguals">bilinguals</a>; cue: <a href="vocabulary.html#rule-respond-to-rule-cue-rule-cue">rule cue</a>; rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>
  - [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
  - A cue on each trial tells a bilingual participant which language to name the picture in, and trials where the language switches are compared with repeats.
* - Tip-of-the-Tongue (TOT) Paradigm

    `hedvar_picture_naming__tip_of_the_tongue_tot_paradigm`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>; combined with: <a href="vocabulary.html#how-inserted">inserted</a>, <a href="vocabulary.html#game-report-on-self">report on self</a> (When naming fails, the player reports their retrieval state and what they partly know)
  - [Feeling of knowing](../processes/awareness_agency_and_metacognition.md#hed-feeling-of-knowing), [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)
  - Rarely named items and famous faces provoke states where the name is known but cannot be produced, and the participant reports know / tip-of-the-tongue / do not know plus any partial information, adding a report on their own retrieval state to the naming job.
* - Naming with Phonological/Semantic Cues

    `hedvar_picture_naming__naming_with_phonological_semantic_cues`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-feature-cue">feature cue</a>
  - -
  - When naming fails a hint is given (the first sound, or a description of the meaning), and whether the hint brings out the name is recorded.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Naming](../processes/language_comprehension_and_production.md#hed-naming)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Language production](../processes/language_comprehension_and_production.md#hed-language-production)
- [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)

## Key references

- Levelt, W. J. M., Roelofs, A., & Meyer, A. S. (1999). A theory of lexical access in speech production. *Behavioral and Brain Sciences*, 22(1), 1-38. ([DOI](https://doi.org/10.1017/s0140525x99001776), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11301520/))
- Indefrey, P., & Levelt, W. J. M. (2004). The spatial and temporal signatures of word production components. *Cognition*, 92(1-2), 101-144. ([DOI](https://doi.org/10.1016/j.cognition.2002.06.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15037128/))
- DeLeon, J., Gottesman, R. F., Kleinman, J. T., et al. (2007). Neural regions essential for distinct cognitive processes underlying picture naming. *Brain*, 130(5), 1408-1422. ([DOI](https://doi.org/10.1093/brain/awm011), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17337482/))

## Further references

- Indefrey, P. (2011). The spatial and temporal signatures of word production components: A critical update. *Frontiers in Psychology*, 2, 255. ([DOI](https://doi.org/10.3389/fpsyg.2011.00255), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22016740/))
- Nozari, N., & Hepner, C. R. (2019). To select or to wait? The importance of criterion setting in debates of competitive lexical selection. *Cognitive Neuropsychology*, 36(5-6), 193-207. ([DOI](https://doi.org/10.1080/02643294.2019.1632280), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31238793/))
- Piai, V., & Eikelboom, J. (2023). Brain areas critical for picture naming: A systematic review and meta-analysis of lesion-symptom mapping studies. *Neurobiology of Language*, 4(2), 280-296. ([DOI](https://doi.org/10.1162/nol_a_00097), [PubMed](https://pubmed.ncbi.nlm.nih.gov/37229507/))

## External links

- Cognitive Atlas: [picture naming task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949cfb)

- CogPO: [Naming (Overt) Paradigm](http://www.wiki.cogpo.org/index.php?title=Naming_%28Overt%29_Paradigm)

