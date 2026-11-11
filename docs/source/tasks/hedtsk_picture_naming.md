(hedtsk_picture_naming)=
# Picture Naming Task

**HED task ID:** `hedtsk_picture_naming`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Object Naming, Confrontation Naming

Naming of pictured objects; RT and errors index lexical retrieval and are sensitive to name agreement, frequency, and age of acquisition.

## Description

Participants view photographs or line drawings of common objects, animals, or scenes and name each item aloud as quickly and accurately as possible. Naming latency (RT from stimulus onset to vocal response onset) is the primary measure. The task engages multiple stages of language production: conceptual identification, lemma retrieval, phonological encoding, and articulation. fMRI reveals activation in left inferior frontal regions (Broca's area) and temporal cortex. The task is widely used in aphasia research and studies of language production.

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
    - Phonological or semantic context (blocked naming, picture-word interference)
* - **Measurements**
  - - Naming latency
    - Error type (semantic, phonological)
    - Frequency and agreement effects
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
* - Standard Single-Object Naming

    `hedvar_picture_naming__standard_single_object_naming`
  - Line drawings or photographs of objects appear one at a time and the participant says the name of each as quickly as possible. A microphone records the time from picture onset to the start of speech.
  - Canonical overt naming to pictured objects
* - Blocked-Cyclic Naming

    `hedvar_picture_naming__blocked_cyclic_naming`
  - A small set of pictures is named repeatedly in cycles. In some blocks all pictures in the set are from one category (all animals); in others they are mixed. Naming slows over cycles in the same-category blocks because related words compete.
  - Same items repeat in blocked cycles; cumulative interference paradigm
* - Continuous Naming

    `hedvar_picture_naming__continuous_naming`
  - A long list of pictures is named once each, with pictures from the same category scattered through the list. Each additional picture from a category is named a little more slowly than the one before, showing interference building up.
  - Rapid successive naming; tests sustained lexical access
* - Picture-Word Interference (PWI)

    `hedvar_picture_naming__picture_word_interference_pwi`
  - A written or spoken word is presented with each picture, and the participant names the picture while ignoring the word. A word related in meaning (cat for a picture of a dog) slows naming; a word that sounds similar (doll) speeds it.
  - Distractor word accompanies picture; lexical competition paradigm
* - Delayed Naming

    `hedvar_picture_naming__delayed_naming`
  - The picture is shown but the participant must wait for a signal, typically one to two seconds later, before saying the name. Because the name is ready before the signal, response time reflects only speech production.
  - Delay between picture onset and response signal; isolates planning from execution
* - Object + Action Naming

    `hedvar_picture_naming__object_action_naming`
  - Pictures show actions as well as objects, and the participant names the action with a verb ('running') or the object with a noun, in separate or mixed blocks.
  - Name actions as well as objects; different grammatical category
* - Bilingual Picture Naming

    `hedvar_picture_naming__bilingual_picture_naming`
  - A cue on each trial (such as a flag or color) tells a bilingual participant which language to name the picture in. Naming is slower just after a switch of language.
  - Language cue specifies response language; language control demand
* - Tip-of-the-Tongue (TOT) Paradigm

    `hedvar_picture_naming__tip_of_the_tongue_tot_paradigm`
  - Pictures of rarely named things or people (famous faces, unusual objects) are used to provoke states in which the participant knows the name but cannot produce it. The participant reports whether they know it, are in that state, or do not know, and may report partial information such as the first letter.
  - Naming under word-finding difficulty conditions; different metacognitive state
* - Naming with Phonological/Semantic Cues

    `hedvar_picture_naming__naming_with_phonological_semantic_cues`
  - When the participant cannot name a picture, a hint is given, such as the first sound of the name or a description of its meaning, and whether the hint produces the name is recorded.
  - Partial cues provided after TOT; different cueing structure
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

