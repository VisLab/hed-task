(hedtsk_lexical_decision)=
# Lexical Decision Task

**HED task ID:** `hedtsk_lexical_decision`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** LDT, Lexical Decision

Speeded word/nonword judgment; RT and accuracy index lexical access and are sensitive to frequency, priming, and context.

## Description

Participants view letter strings and must rapidly determine whether each string is a valid word or a nonword by pressing designated response buttons. Stimuli include high- and low-frequency words and pronounceable nonwords. RT and accuracy to words versus nonwords indexes lexical access efficiency. The task is often combined with priming manipulations to examine semantic, phonological, or morphological processing. It is one of the most fundamental paradigms in psycholinguistics.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Letter strings are presented one at a time.
    2. Participants classify each as a real word or a nonword as quickly and accurately as possible.
* - **Manipulations**
  - - Word frequency
    - Word length
    - Orthographic neighborhood
    - Nonword type (pseudoword vs. random)
    - Priming (semantic, associative, morphological)
* - **Measurements**
  - - RT and accuracy
    - Frequency effect
    - Priming effect (primed - unprimed RT)
    - d-prime
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
* - Standard Visual LDT

    `hedvar_lexical_decision__standard_visual_ldt`
  - Strings of letters appear one at a time on a screen. The participant presses one key if the string is a real word (such as TABLE) and another if it is not (such as TOBLE), as quickly as possible.
  - Canonical: word/nonword judgment to visually presented strings
* - Auditory LDT

    `hedvar_lexical_decision__auditory_ldt`
  - The items are spoken through headphones rather than shown, and the participant decides whether what they heard was a real word.
  - Auditory presentation; different sensory modality
* - Masked Priming LDT

    `hedvar_lexical_decision__masked_priming_ldt`
  - Immediately before each target, a prime word is flashed for about 50 ms between masking patterns so the participant does not consciously see it. The word decision on the target is faster when the hidden prime is related to it.
  - Brief masked prime before target; changes prime awareness
* - Cross-Modal LDT

    `hedvar_lexical_decision__cross_modal_ldt`
  - A prime is heard and the target is seen (or the reverse). The participant decides whether the visible target is a word while a spoken word or sentence is played just before or during it.
  - Prime in one modality, target in another; cross-modal priming structure
* - LDT with Different Nonword Types

    `hedvar_lexical_decision__ldt_with_different_nonword_types`
  - The non-words are chosen to be more or less word-like: strings that sound like real words when read aloud (BRANE), strings with two letters swapped (JUGDE), or unpronounceable consonant strings (TBLK). More word-like non-words make the decision harder.
  - Pseudowords, random letter strings, pseudohomophones; nonword type changes task difficulty
* - Bilingual LDT

    `hedvar_lexical_decision__bilingual_ldt`
  - Words from two languages the participant speaks are mixed in the same list, sometimes with words that exist in both languages, and the participant decides whether each is a word in either language or in a specified one.
  - Targets in two languages; different language switching demand
* - LDT Megastudies

    `hedvar_lexical_decision__ldt_megastudies`
  - Each participant responds to thousands of words over many sessions, as in the English Lexicon Project, so that response times are available for every word rather than for small chosen sets.
  - Large-scale normed stimulus sets enabling item-level analyses; different methodological scope
* - Go/No-Go LDT

    `hedvar_lexical_decision__go_no_go_ldt`
  - The participant presses a key only for words and makes no response to non-words (or the reverse), instead of having a separate key for each.
  - Respond to one word class, withhold to another; different response structure
```

## Cognitive processes

This task is designed to engage the following processes:

- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)
- [Word recognition](../processes/language_comprehension_and_production.md#hed-word-recognition)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Reading](../processes/language_comprehension_and_production.md#hed-reading)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)

## Key references

- Meyer, D. E., & Schvaneveldt, R. W. (1971). Facilitation in recognizing pairs of words: Evidence of a dependence between retrieval operations. *Journal of Experimental Psychology*, 90(2), 227-234. ([DOI](https://doi.org/10.1037/h0031564), [PubMed](https://pubmed.ncbi.nlm.nih.gov/5134329/))
- Neely, J. H. (1977). Semantic priming and retrieval from lexical memory: Roles of inhibitionless spreading activation and limited-capacity attention. *Journal of Experimental Psychology: General*, 106(3), 226-254. ([DOI](https://doi.org/10.1037/0096-3445.106.3.226))
- Fiebach, C. J., Friederici, A. D., Muller, K., & von Cramon, D. Y. (2002). fMRI evidence for dual routes to the mental lexicon in visual word recognition. *Journal of Cognitive Neuroscience*, 14(1), 11-23. ([DOI](https://doi.org/10.1162/089892902317205285), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11798383/))

## Further references

- Keuleers, E., & Brysbaert, M. (2010). Wuggy: A multilingual pseudoword generator. *Behavior Research Methods*, 42(3), 627-633. [Updated: Keuleers, E., Lacey, P., Rastle, K., & Brysbaert, M. (2012). The British Lexicon Project. *Quarterly Journal of Experimental Psychology*, 65(8), 1441-1469.] ([DOI](https://doi.org/10.3758/brm.42.3.627), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20805584/))
- Taylor, J. S. H., Rastle, K., & Davis, M. H. (2013). Can cognitive models explain brain activation during word and pseudoword reading? A meta-analysis of 36 neuroimaging studies. *Psychological Bulletin*, 139(4), 766-791. ([DOI](https://doi.org/10.1037/a0030266), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23046391/))
- Balota, D. A., Yap, M. J., Hutchison, K. A., et al. (2007). The English Lexicon Project. *Behavior Research Methods*, 39(3), 445-459. [Megastudy approach] ([DOI](https://doi.org/10.3758/bf03193014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17958156/))
- Ratcliff, R., Gomez, P., & McKoon, G. (2004). A diffusion model account of the lexical decision task. *Psychological Review*, 111(1), 159-182. ([DOI](https://doi.org/10.1037/0033-295x.111.1.159), [PubMed](https://pubmed.ncbi.nlm.nih.gov/14756592/))
- Ball, L. V., Brusini, P., & Bannard, C. (2025). Revisiting novel word semantic priming: The role of strategic priming mechanisms. *Quarterly Journal of Experimental Psychology*, 78. doi:10.1177/17470218241306747

## External links

- Cognitive Atlas: [lexical decision task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949b38)

- CogPO: [Semantic Monitor/Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Semantic_Monitor_or_Discrimination_Paradigm) (close match)

