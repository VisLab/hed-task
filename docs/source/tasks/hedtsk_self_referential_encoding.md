(hedtsk_self_referential_encoding)=
# Self-Referential Encoding Task

**HED task ID:** `hedtsk_self_referential_encoding`

**Family:** [Memory control and prospective memory tasks](families/memory_control.md)

**Also known as:** SRET, Self-Reference Effect Paradigm, Self-Referential Processing Task, Trait Adjective Endorsement Task

Participants judge whether trait adjectives describe themselves vs. another person or a semantic property; the self-reference effect (superior recall for self-encoded items) and endorsement patterns index self-concept and self-referential processing.

## Description

The Self-Referential Encoding Task exploits the robust finding that information encoded in relation to the self is remembered better than information encoded in other ways (the self-reference effect; Rogers, Kuiper, & Kirker, 1977). In the standard paradigm, participants view trait adjectives and make judgments under different encoding conditions: 'Does this word describe you?' (self-reference), 'Does this word describe [other person]?' (other-reference), 'Is this a positive word?' (semantic), or 'Is this word in uppercase?' (structural). A surprise recall or recognition test follows. The self-reference effect is the recall advantage for self-encoded items over semantic or other-reference conditions. Beyond the memory effect, the pattern of adjective endorsement (which traits are endorsed as self-descriptive) provides a direct window into self-concept content. This has made the task central to depression research: depressed individuals endorse more negative and fewer positive adjectives as self-descriptive, and show reduced or reversed self-reference memory effects for positive material. The paradigm engages cortical midline structures (medial prefrontal cortex, posterior cingulate) associated with self-referential processing, making it a standard fMRI probe of the default mode network.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants judge trait adjectives under self-reference and comparison encoding conditions (other-reference, semantic, structural).
    2. a subsequent memory test assesses the self-reference effect on recall or recognition.
* - **Manipulations**
  - - Encoding condition (self, other, semantic, structural)
    - Valence of adjectives (positive, negative, neutral)
    - Other-reference target (close other vs. distant other vs. celebrity)
    - Self-relevance (high vs. low)
    - Presentation modality
* - **Measurements**
  - - Self-reference effect (recall/recognition advantage for self-encoded items)
    - Endorsement rate by valence and condition
    - Endorsement latency
    - Recall bias (proportion positive vs. negative recalled)
    - Cortical midline activation (medial prefrontal cortex, posterior cingulate)
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
* - Standard Trait Adjective Encoding

    `hedvar_self_referential_encoding__standard_trait_adjective_encoding`
  - Trait words such as 'honest' or 'lazy' are shown, each with a question: does this describe you (self), does it describe another person such as a public figure (other), does it mean the same as a given word (meaning), or is it printed in capitals (appearance). After all words, a surprise recall test follows. Words judged about the self are recalled best.
  - Canonical: judge whether adjective describes self; incidental encoding
* - Positive/Negative Valence Split

    `hedvar_self_referential_encoding__positive_negative_valence_split`
  - The trait words are balanced between positive (kind) and negative (selfish), and endorsement and recall are analyzed separately for each. Depressed participants endorse and recall more negative words about themselves.
  - Valence-matched sets tested separately; tests self-relevance by valence
* - Close vs. Distant Other-Reference

    `hedvar_self_referential_encoding__close_vs_distant_other_reference`
  - The 'other' person in the question is varied from someone very close (mother, best friend) to a celebrity or a stranger, to see whether the memory advantage for self-judged words shrinks as the other becomes closer.
  - Encoding with reference to close vs. distant others; tests reference specificity
* - Incidental vs. Intentional Encoding

    `hedvar_self_referential_encoding__incidental_vs_intentional_encoding`
  - In the usual version the participant does not know a memory test is coming. In the intentional version they are told to remember the words as well as answering the questions, to see whether the self-reference advantage holds when people are trying to learn.
  - Explicit memory instruction vs. incidental; changes encoding goal
* - Endorsement-Only (No Memory Test)

    `hedvar_self_referential_encoding__endorsement_only_no_memory_test`
  - Only the self-judgment phase is run: the participant says yes or no to whether each trait word describes them, and the pattern of positive and negative endorsements is the measure. No recall test is given.
  - Task without memory test phase; tests self-referential processing in isolation
* - Source Memory for Self-Encoded Items

    `hedvar_self_referential_encoding__source_memory_for_self_encoded_items`
  - At test the participant must say not only whether a word was studied but which question it was studied with (self, other, meaning), to check whether self-reference improves memory for the context as well as for the word.
  - Retrieval includes source judgment for self vs. other items; adds source component
```

## Cognitive processes

This task is designed to engage the following processes:

- [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Recollection](../processes/long_term_memory.md#hed-recollection)

## Key references

- Rogers, T. B., Kuiper, N. A., & Kirker, W. S. (1977). Self-reference and the encoding of personal information. *Journal of Personality and Social Psychology*, 35(9), 677-688. ([DOI](https://doi.org/10.1037/0022-3514.35.9.677))
- Symons, C. S., & Johnson, B. T. (1997). The self-reference effect in memory: A meta-analysis. *Psychological Bulletin*, 121(3), 371-394. ([DOI](https://doi.org/10.1037/0033-2909.121.3.371), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9136641/))
- Kelley, W. M., Macrae, C. N., Wyland, C. L., Caglar, S., Inati, S., & Heatherton, T. F. (2002). Finding the self? An event-related fMRI study. *Journal of Cognitive Neuroscience*, 14(5), 785-794. ([DOI](https://doi.org/10.1162/08989290260138672), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12167262/))

## Further references

- Derry, P. A., & Kuiper, N. A. (1981). Schematic processing and self-reference in clinical depression. *Journal of Abnormal Psychology*, 90(4), 286-297. ([DOI](https://doi.org/10.1037/0021-843x.90.4.286))
- Northoff, G., Heinzel, A., de Greck, M., Bermpohl, F., Dobrowolny, H., & Panksepp, J. (2006). Self-referential processing in our brain — A meta-analysis of imaging studies on the self. *NeuroImage*, 31(1), 440-457. ([DOI](https://doi.org/10.1016/j.neuroimage.2005.12.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16466680/))
- Herbert, C., Pauli, P., & Herbert, B. M. (2011). Self-reference modulates the processing of emotional stimuli in the absence of explicit self-referential appraisal instructions. *Social Cognitive and Affective Neuroscience*, 6(5), 653-661. ([DOI](https://doi.org/10.1093/scan/nsq082))
- Fossati, P. (2012). Neural correlates of self-referential processing in depression. *World Journal of Biological Psychiatry*, 13(5), 329-339. ([DOI](https://doi.org/10.1016/j.biopsycho.2013.08.003))

