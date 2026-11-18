(hedtsk_lexical_decision)=
# Lexical Decision Task

**HED task ID:** `hedtsk_lexical_decision`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** LDT, Lexical Decision

Speeded word/nonword judgment; RT and accuracy index lexical access and are sensitive to frequency, priming, and context.

## Description

Participants view letter strings and must rapidly determine whether each string is a valid word or a nonword by pressing designated response buttons. Stimuli include high- and low-frequency words and pronounceable nonwords. RT and accuracy to words versus nonwords indexes lexical access efficiency. The task is often combined with priming manipulations to examine semantic, phonological, or morphological processing. It is one of the most fundamental paradigms in psycholinguistics.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-pseudowords">pseudowords</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Letter strings that are real words, varying in frequency, length and orthographic neighborhood, or nonwords that are pronounceable or random.

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
    - Language mix (words from two languages in one list)
    - Number of words per participant (megastudy)
    - Response format (go/no-go vs. two-key decision)
* - **Measurements**
  - - RT and accuracy
    - Frequency effect
    - Priming effect (primed - unprimed RT)
    - d-prime
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
* - Auditory LDT

    `hedvar_lexical_decision__auditory_ldt`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The items are spoken through headphones instead of printed; the word/nonword decision is unchanged.
* - Masked Priming LDT

    `hedvar_lexical_decision__masked_priming_ldt`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-preceding-prime">preceding prime</a>
  - -
  - A prime word is flashed for about 50 ms between masks before each target, adding a preceding prime whose relatedness to the target is varied.
* - Cross-Modal LDT

    `hedvar_lexical_decision__cross_modal_ldt`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-pseudowords">pseudowords</a>, <a href="vocabulary.html#facet-stimulus-type-text">text</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>; competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-preceding-prime">preceding prime</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - A spoken prime (word or sentence) is played before or during a printed target, or the reverse, adding a prime in a second modality.
* - LDT with Different Nonword Types

    `hedvar_lexical_decision__ldt_with_different_nonword_types`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-pseudowords">pseudowords</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - -
  - The nonwords are made more or less word-like (pseudohomophones, transposed-letter strings, consonant strings); the decision is unchanged and nonword type is the difficulty factor.
* - Bilingual LDT

    `hedvar_lexical_decision__bilingual_ldt`
  - population: <a href="vocabulary.html#facet-population-bilinguals">bilinguals</a>
  - -
  - Words from two of the participant's languages are mixed in one list and the decision is "a word in either language" or "a word in the named language"; the classification structure is unchanged.
* - Go/No-Go LDT

    `hedvar_lexical_decision__go_no_go_ldt`
  - response demand: <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
  - [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
  - The participant presses for one class (words) and withholds for the other, instead of having a key for each.
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

