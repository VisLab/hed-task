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
  - 1. A prime word is followed by a target word.
    2. Participants make a lexical decision or naming response to the target.
    3. Prime-target pairs are semantically related or unrelated.
* - **Manipulations**
  - - Prime-target relatedness (associated, categorical, unrelated)
    - SOA (short for automatic priming, long for strategic)
    - Prime type (word, sentence context)
* - **Measurements**
  - - Priming effect (RT difference: unrelated − related)
    - Accuracy
    - N400 ERP amplitude reduction for related pairs
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
  - The prime word is followed by the target word within a quarter of a second, too soon for the participant to form an expectation about what the target will be. Faster responses to related targets reflect automatic activation of related meanings.
  - Brief prime-target interval; automatic spreading activation
* - Long SOA (> 500 ms)

    `hedvar_semantic_priming__long_soa_500_ms`
  - Half a second or more passes between prime and target, giving the participant time to anticipate likely targets. Priming can then include deliberate expectation as well as automatic activation.
  - Long interval; strategic processing contributes
* - Masked Priming

    `hedvar_semantic_priming__masked_priming`
  - The prime is shown for about 50 ms between masking patterns so it is not consciously seen, and the target follows immediately. Priming that survives masking is taken to be automatic.
  - Prime below awareness; unconscious semantic activation
* - Relatedness Proportion Manipulation

    `hedvar_semantic_priming__relatedness_proportion_manipulation`
  - The share of trials on which prime and target are related is set high (such as 75 percent) in one condition and low (25 percent) in another. When related pairs are common, participants use the prime to predict the target and priming is larger.
  - Varies proportion of related pairs; changes strategic context
* - Semantic Relation Types

    `hedvar_semantic_priming__semantic_relation_types`
  - The prime and target are related in different ways on different trials: by association (bread - butter), by category (cat - dog), by situation (broom - floor) or by function (hammer - nail). Priming is compared across relation types.
  - Taxonomic vs. thematic vs. associative relations; different prime-target relationships
* - Mediated Priming

    `hedvar_semantic_priming__mediated_priming`
  - The prime and target are not directly related but share a common link, for example 'lion' and 'stripes' through 'tiger'. Priming between them shows that activation spreads beyond immediate associates.
  - Prime activates mediator that activates target; tests spread of activation
* - Cross-Modal Priming

    `hedvar_semantic_priming__cross_modal_priming`
  - The prime is spoken through headphones and the target is written on the screen, or vice versa, so that priming must cross from one sense to the other.
  - Auditory prime + visual target; cross-modal semantic activation
* - Sentence Context Priming

    `hedvar_semantic_priming__sentence_context_priming`
  - The prime is a sentence frame rather than a single word, and the target word either fits the sentence or does not. Measures how a whole context prepares the reader for a word.
  - Sentence prime instead of single word; higher-level context
* - Picture-Word Priming

    `hedvar_semantic_priming__picture_word_priming`
  - The prime is a picture and the target a word (or the reverse), so that the relationship is in meaning rather than in the words themselves.
  - Picture prime for word target; conceptual rather than lexical priming
* - Morphological Priming

    `hedvar_semantic_priming__morphological_priming`
  - The prime and target share a word stem, such as 'teach' and 'teacher', or a prefix. Priming from shared structure is compared with priming from shared meaning or shared spelling to see whether words are broken into parts during reading.
  - Morphologically related prime; tests morphological representation
* - Phonological Priming

    `hedvar_semantic_priming__phonological_priming`
  - The prime and target sound alike, for example they rhyme (cat - hat) or share a first sound (cat - cup), without being related in meaning. Measures the role of sound in recognizing words.
  - Phonologically similar prime; tests phonological overlap effects
* - Orthographic Priming

    `hedvar_semantic_priming__orthographic_priming`
  - The prime and target share letters but nothing else, for example 'corner' and 'corn'. Usually a control condition for morphological priming, showing how much priming comes from spelling overlap alone.
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

