(hedtsk_semantic_priming)=
# Semantic Priming Task

**HED task ID:** `hedtsk_semantic_priming`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Priming, Associative Priming, Morphological Priming, Phonological Priming, Orthographic Priming

Lexical or semantic decision on targets preceded by semantically related or unrelated primes; RT facilitation indexes automatic semantic activation.

## Description

Word pairs are presented in sequence: a prime word followed by a target. Prime-target relationships are manipulated (semantically related, unrelated, or neutral). Participants typically make lexical decisions on the target. Semantic priming is measured as faster RT to related versus unrelated pairs, reflecting automatic spreading activation through semantic memory networks. SOA manipulation distinguishes automatic (short SOA) from strategic (long SOA) priming.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A prime word is followed by a target word; participants make a lexical decision or naming response to the target. Prime-target pairs are semantically related or unrelated.
* - **Manipulation**
  - Prime-target relatedness (associated, categorical, unrelated); SOA (short for automatic priming, long for strategic); prime type (word, sentence context).
* - **Measurement**
  - Priming effect (RT difference: unrelated − related); accuracy; N400 ERP amplitude reduction for related pairs.
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
* - Short SOA (< 250 ms)

    `hedvar_semantic_priming__short_soa_250_ms`
  - Favors automatic spreading activation; minimal strategic processing.
  - Brief prime-target interval; automatic spreading activation
* - Long SOA (> 500 ms)

    `hedvar_semantic_priming__long_soa_500_ms`
  - Allows strategic expectancy generation and semantic matching.
  - Long interval; strategic processing contributes
* - Masked Priming

    `hedvar_semantic_priming__masked_priming`
  - Subliminal prime (50–67 ms) followed by mask; purely automatic priming.
  - Prime below awareness; unconscious semantic activation
* - Relatedness Proportion Manipulation

    `hedvar_semantic_priming__relatedness_proportion_manipulation`
  - High (75%) vs. low (25%) proportion of related pairs; modulates strategic control.
  - Varies proportion of related pairs; changes strategic context
* - Semantic Relation Types

    `hedvar_semantic_priming__semantic_relation_types`
  - Associative (bread-butter), categorical (cat-dog), thematic (broom-floor), functional (hammer-nail).
  - Taxonomic vs. thematic vs. associative relations; different prime-target relationships
* - Mediated Priming

    `hedvar_semantic_priming__mediated_priming`
  - Indirect semantic connection (lion → stripes via tiger); tests spreading activation range.
  - Prime activates mediator that activates target; tests spread of activation
* - Cross-Modal Priming

    `hedvar_semantic_priming__cross_modal_priming`
  - Auditory prime → visual target; tests amodal semantic representations.
  - Auditory prime + visual target; cross-modal semantic activation
* - Sentence Context Priming

    `hedvar_semantic_priming__sentence_context_priming`
  - Words embedded in sentence contexts rather than isolated pairs.
  - Sentence prime instead of single word; higher-level context
* - Picture-Word Priming

    `hedvar_semantic_priming__picture_word_priming`
  - Pictures priming words or vice versa.
  - Picture prime for word target; conceptual rather than lexical priming
* - Morphological Priming

    `hedvar_semantic_priming__morphological_priming`
  - Prime-target pairs share a morpheme (e.g., teach-teacher, un-do/redo). Distinguishes morphological decomposition from semantic and orthographic overlap. Used with masked and overt priming to probe automatic vs. strategic morphological processing.
  - Morphologically related prime; tests morphological representation
* - Phonological Priming

    `hedvar_semantic_priming__phonological_priming`
  - Prime-target pairs share phonological overlap (e.g., rhyme: cat-hat; onset: cat-cup). Distinguishes phonological from semantic and orthographic contributions to lexical access.
  - Phonologically similar prime; tests phonological overlap effects
* - Orthographic Priming

    `hedvar_semantic_priming__orthographic_priming`
  - Prime-target pairs share letter sequences without semantic or morphological relation (e.g., corner-corn). Typically a control condition for morphological priming studies; indexes form-level activation.
  - Orthographically similar prime; tests spelling overlap effects
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

- Hutchison, K. A., Balota, D. A., Neely, J. H., et al. (2013). The semantic priming project. *Behavior Research Methods*, 45(4), 1099–1114. ([DOI](https://doi.org/10.3758/s13428-012-0304-z), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23344737/))
- Buchanan, E. M., et al. (2025). Measuring the semantic priming effect across many languages. *Nature Human Behaviour*, 9, 133–142.
- Jones, L. L., & Golonka, S. (2012). Different results from different procedures: The impact of SOA and masked/unmasked priming on semantic priming effects. *Attention, Perception, & Psychophysics*, 74(5), 854–864.
- Lau, E. F., Phillips, C., & Poeppel, D. (2008). A cortical network for semantics: (De)constructing the N400. *Nature Reviews Neuroscience*, 9(12), 920–933. ([DOI](https://doi.org/10.1038/nrn2532), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19020511/))
- Rastle, K., & Davis, M. H. (2008). Morphological decomposition based on the analysis of orthography. *Language and Cognitive Processes*, 23(7-8), 942-971. ([DOI](https://doi.org/10.1080/01690960802069730))

## External links

- Cognitive Atlas: [contextual semantic priming task](https://www.cognitiveatlas.org/task/id/trm_553e73e29cf7d) (close match)

