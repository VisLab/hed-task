(hedtsk_self_referential_encoding)=
# Self-Referential Encoding Task

**HED task ID:** `hedtsk_self_referential_encoding`

**Family:** [Memory control and prospective memory tasks](families/memory_control.md) (also [Self-report tasks](families/self_report.md))

**Also known as:** SRET, Self-Reference Effect Paradigm, Self-Referential Processing Task, Trait Adjective Endorsement Task

Participants judge whether trait adjectives describe themselves vs. another person or a semantic property; the self-reference effect (superior recall for self-encoded items) and endorsement patterns index self-concept and self-referential processing.

## Description

The Self-Referential Encoding Task exploits the robust finding that information encoded in relation to the self is remembered better than information encoded in other ways (the self-reference effect; Rogers, Kuiper, & Kirker, 1977). In the standard paradigm, participants view trait adjectives and make judgments under different encoding conditions: 'Does this word describe you?' (self-reference), 'Does this word describe [other person]?' (other-reference), 'Is this a positive word?' (semantic), or 'Is this word in uppercase?' (structural). A surprise recall or recognition test follows. The self-reference effect is the recall advantage for self-encoded items over semantic or other-reference conditions. Beyond the memory effect, the pattern of adjective endorsement (which traits are endorsed as self-descriptive) provides a direct window into self-concept content. This has made the task central to depression research: depressed individuals endorse more negative and fewer positive adjectives as self-descriptive, and show reduced or reversed self-reference memory effects for positive material. The paradigm engages cortical midline structures (medial prefrontal cortex, posterior cingulate) associated with self-referential processing, making it a standard fMRI probe of the default mode network.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">Study, then be tested</a> (`study_then_test`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *How long is it held?* <a href="vocabulary.html#rule-study-then-test-retention-interval-surprise">surprise</a>
  - *What form does the test take?* <a href="vocabulary.html#rule-study-then-test-test-form-free-recall">free recall</a>
  - *What does the player do while studying?* <a href="vocabulary.html#rule-study-then-test-study-job-self-reference-judgment">self reference judgment</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-explicit-social-task">explicit social task</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Trait adjectives (positive, negative or neutral) with a question asking whether each describes oneself or another person, is positive, or is in uppercase.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants judge trait adjectives under self-reference and comparison encoding conditions (other-reference, semantic, structural).
    2. a subsequent memory test assesses the self-reference effect on recall or recognition.
    3. Optional: Only the judgment phase is run and the yes/no endorsement pattern is the measure; there is no memory test.
    4. Optional: At test the participant says not only whether a word was studied but which question it was studied under.
* - **Manipulations**
  - - Encoding condition (self, other, semantic, structural)
    - Valence of adjectives (positive, negative, neutral)
    - Other-reference target (close other vs. distant other vs. celebrity)
    - Self-relevance (high vs. low)
    - Presentation modality
    - Encoding instruction (incidental vs. intentional)
* - **Measurements**
  - - Self-reference effect (recall/recognition advantage for self-encoded items)
    - Endorsement rate by valence and condition
    - Endorsement latency
    - Recall bias (proportion positive vs. negative recalled)
    - Cortical midline activation (medial prefrontal cortex, posterior cingulate)
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
* - Positive/Negative Valence Split

    `hedvar_self_referential_encoding__positive_negative_valence_split`
  - emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - -
  - The adjective set is balanced between positive and negative traits and endorsement and recall are analysed by valence.
* - Incidental vs. Intentional Encoding

    `hedvar_self_referential_encoding__incidental_vs_intentional_encoding`
  - retention interval: <a href="vocabulary.html#rule-study-then-test-retention-interval-minutes">minutes</a>
  - -
  - The participant is told a memory test will follow and to try to remember the words, so the test is announced rather than a surprise.
* - Source Memory for Self-Encoded Items

    `hedvar_self_referential_encoding__source_memory_for_self_encoded_items`
  - test form: <a href="vocabulary.html#rule-study-then-test-test-form-source-attribution">source attribution</a>
  - [Source memory](../processes/long_term_memory.md#hed-source-memory)
  - At test the participant says not only whether a word was studied but which question it was studied under.
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
- Northoff, G., Heinzel, A., de Greck, M., Bermpohl, F., Dobrowolny, H., & Panksepp, J. (2006). Self-referential processing in our brain - A meta-analysis of imaging studies on the self. *NeuroImage*, 31(1), 440-457. ([DOI](https://doi.org/10.1016/j.neuroimage.2005.12.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16466680/))
- Herbert, C., Pauli, P., & Herbert, B. M. (2011). Self-reference modulates the processing of emotional stimuli in the absence of explicit self-referential appraisal instructions. *Social Cognitive and Affective Neuroscience*, 6(5), 653-661. ([DOI](https://doi.org/10.1093/scan/nsq082))
- Fossati, P. (2012). Neural correlates of self-referential processing in depression. *World Journal of Biological Psychiatry*, 13(5), 329-339. ([DOI](https://doi.org/10.1016/j.biopsycho.2013.08.003))

