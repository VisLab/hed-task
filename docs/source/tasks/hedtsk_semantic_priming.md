(hedtsk_semantic_priming)=
# Semantic Priming Task

**HED task ID:** `hedtsk_semantic_priming`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Priming, Associative Priming, Morphological Priming, Phonological Priming, Orthographic Priming

Lexical or semantic decision on targets preceded by semantically related or unrelated primes; RT facilitation indexes automatic semantic activation.

## Description

Word pairs are presented in sequence: a prime word followed by a target. Prime-target relationships are manipulated (semantically related, unrelated, or neutral). Participants typically make lexical decisions on the target. Semantic priming is measured as faster RT to related versus unrelated pairs, reflecting automatic spreading activation through semantic memory networks. SOA manipulation distinguishes automatic (short SOA) from strategic (long SOA) priming.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-preceding-prime">preceding prime</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-pseudowords">pseudowords</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-proportion-congruent">proportion congruent</a>, <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** A prime word followed by a target word or nonword, the pair related by association or category or unrelated.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A prime word is followed by a target word.
    2. Participants make a lexical decision or naming response to the target.
    3. Prime-target pairs are semantically related or unrelated.
* - **Manipulations**
  - - Prime-target relatedness (associated, categorical, unrelated)
    - SOA (short for automatic priming, long for strategic)
    - Prime type (word, sentence context)
    - Proportion of related trials (75% vs. 25%)
    - Prime and target type (picture vs. word)
* - **Measurements**
  - - Priming effect (RT difference: unrelated - related)
    - Accuracy
    - N400 ERP amplitude reduction for related pairs
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
* - Cross-Modal Priming

    `hedvar_semantic_priming__cross_modal_priming`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The prime is spoken and the target printed, or the reverse; the decision is unchanged.
* - Sentence Context Priming

    `hedvar_semantic_priming__sentence_context_priming`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-pseudowords">pseudowords</a>, <a href="vocabulary.html#facet-stimulus-type-text">text</a>
  - -
  - The prime is a sentence frame rather than a word and the target either fits it or not; a level of the prime-type manipulation.
* - Picture-Word Priming

    `hedvar_semantic_priming__picture_word_priming`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-pseudowords">pseudowords</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
  - [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition)
  - The prime is a picture and the target a word, or the reverse, so the relation is conceptual rather than lexical.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Semantic knowledge](../processes/language_comprehension_and_production.md#hed-semantic-knowledge)
- [Word recognition](../processes/language_comprehension_and_production.md#hed-word-recognition)

## Key references

- Meyer, D. E., & Schvaneveldt, R. W. (1971). Facilitation in recognizing pairs of words. *Journal of Experimental Psychology*, 90(2), 227-234. ([DOI](https://doi.org/10.1037/h0031564), [PubMed](https://pubmed.ncbi.nlm.nih.gov/5134329/))
- Collins, A. M., & Loftus, E. F. (1975). A spreading-activation theory of semantic processing. *Psychological Review*, 82(6), 407-428. ([DOI](https://doi.org/10.1037/0033-295x.82.6.407))
- Rissman, J., Eliassen, J. C., & Blumstein, S. E. (2003). An event-related fMRI investigation of implicit semantic priming. *Journal of Cognitive Neuroscience*, 15(8), 1160-1169. ([DOI](https://doi.org/10.1162/089892903322598120), [PubMed](https://pubmed.ncbi.nlm.nih.gov/14709234/))

## Further references

- Hutchison, K. A., Balota, D. A., Neely, J. H., et al. (2013). The semantic priming project. *Behavior Research Methods*, 45(4), 1099-1114. ([DOI](https://doi.org/10.3758/s13428-012-0304-z), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23344737/))
- Buchanan, E. M., et al. (2025). Measuring the semantic priming effect across many languages. *Nature Human Behaviour*, 9, 133-142.
- Jones, L. L., & Golonka, S. (2012). Different results from different procedures: The impact of SOA and masked/unmasked priming on semantic priming effects. *Attention, Perception, & Psychophysics*, 74(5), 854-864.
- Lau, E. F., Phillips, C., & Poeppel, D. (2008). A cortical network for semantics: (De)constructing the N400. *Nature Reviews Neuroscience*, 9(12), 920-933. ([DOI](https://doi.org/10.1038/nrn2532), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19020511/))
- Rastle, K., & Davis, M. H. (2008). Morphological decomposition based on the analysis of orthography. *Language and Cognitive Processes*, 23(7-8), 942-971. ([DOI](https://doi.org/10.1080/01690960802069730))

## External links

- Cognitive Atlas: [contextual semantic priming task](https://www.cognitiveatlas.org/task/id/trm_553e73e29cf7d) (close match)

