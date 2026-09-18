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
  - Participants judge trait adjectives under self-reference and comparison encoding conditions (other-reference, semantic, structural); a subsequent memory test assesses the self-reference effect on recall or recognition.
* - **Manipulation**
  - Encoding condition (self, other, semantic, structural); valence of adjectives (positive, negative, neutral); other-reference target (close other vs. distant other vs. celebrity); self-relevance (high vs. low); presentation modality.
* - **Measurement**
  - Self-reference effect (recall/recognition advantage for self-encoded items); endorsement rate by valence and condition; endorsement latency; recall bias (proportion positive vs. negative recalled); cortical midline activation (medial prefrontal cortex, posterior cingulate).
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
  - Self/other/semantic/structural encoding of trait adjectives followed by surprise recall. The Rogers et al. (1977) design. The foundational paradigm.
  - Canonical: judge whether adjective describes self; incidental encoding
* - Positive/Negative Valence Split

    `hedvar_self_referential_encoding__positive_negative_valence_split`
  - Separate analysis by adjective valence. Depression studies focus on the positive endorsement deficit and negative recall bias.
  - Valence-matched sets tested separately; tests self-relevance by valence
* - Close vs. Distant Other-Reference

    `hedvar_self_referential_encoding__close_vs_distant_other_reference`
  - Compare self-encoding with encoding relative to mother, best friend, celebrity, or stranger. Tests whether self-reference advantage is graded by social closeness.
  - Encoding with reference to close vs. distant others; tests reference specificity
* - Incidental vs. Intentional Encoding

    `hedvar_self_referential_encoding__incidental_vs_intentional_encoding`
  - Standard version uses incidental encoding (surprise memory test). Intentional encoding versions test whether self-reference benefit persists under deliberate memorization.
  - Explicit memory instruction vs. incidental; changes encoding goal
* - Endorsement-Only (No Memory Test)

    `hedvar_self_referential_encoding__endorsement_only_no_memory_test`
  - Clinical use: just the self-endorsement phase. Patterns of positive and negative endorsement index self-concept content in depression.
  - Task without memory test phase; tests self-referential processing in isolation
* - Source Memory for Self-Encoded Items

    `hedvar_self_referential_encoding__source_memory_for_self_encoded_items`
  - Combines self-referential encoding with source memory judgments. Tests whether self-reference enhances contextual recollection or just item familiarity.
  - Retrieval includes source judgment for self vs. other items; adds source component
```

## Cognitive processes

This task is designed to engage the following processes:

- [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Recollection](../processes/long_term_memory.md#hed-recollection)

## Key references

- Rogers, T. B., Kuiper, N. A., & Kirker, W. S. (1977). Self-reference and the encoding of personal information. *Journal of Personality and Social Psychology*, 35(9), 677-688.
- Symons, C. S., & Johnson, B. T. (1997). The self-reference effect in memory: A meta-analysis. *Psychological Bulletin*, 121(3), 371-394.
- Kelley, W. M., Macrae, C. N., Wyland, C. L., Caglar, S., Inati, S., & Heatherton, T. F. (2002). Finding the self? An event-related fMRI study. *Journal of Cognitive Neuroscience*, 14(5), 785-794.

## Recent references

- Derry, P. A., & Kuiper, N. A. (1981). Schematic processing and self-reference in clinical depression. *Journal of Abnormal Psychology*, 90(4), 286-297.
- Northoff, G., Heinzel, A., de Greck, M., Bermpohl, F., Dobrowolny, H., & Panksepp, J. (2006). Self-referential processing in our brain — A meta-analysis of imaging studies on the self. *NeuroImage*, 31(1), 440-457.
- Herbert, C., Pauli, P., & Herbert, B. M. (2011). Self-reference modulates the processing of emotional stimuli in the absence of explicit self-referential appraisal instructions. *Social Cognitive and Affective Neuroscience*, 6(5), 653-661.
- Fossati, P. (2012). Neural correlates of self-referential processing in depression. *World Journal of Biological Psychiatry*, 13(5), 329-339.

