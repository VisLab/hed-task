(hedtsk_digit_symbol_substitution)=
# Digit Symbol Substitution Task

**HED task ID:** `hedtsk_digit_symbol_substitution`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** Digit Symbol Substitution Test, DSST, SDMT, Symbol Digit Modalities, Coding Test, Digit Symbol Substitution

Timed paper-and-pencil or computerized task: substitute digits for symbols (or vice versa) using a visible key; items completed in a fixed interval index processing speed.

## Description

The Digit Symbol Substitution Test (also known as Symbol Digit Modalities Test, SDMT, in its symbol-to-digit variant) is one of the most sensitive neuropsychological measures of processing speed and cognitive efficiency. Participants view a key pairing digits 1-9 with unique abstract symbols. They then fill in the corresponding symbol for each digit in a series (DSST) or write the digit for each symbol (SDMT), working as quickly and accurately as possible for 90-120 seconds. The number of correct substitutions is the primary score. The DSST/SDMT is included in the WAIS and is among the most sensitive tests for detecting cognitive impairment from neurological conditions, medication side effects, and normal aging.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-generate">generate</a>
  - *How do the stimuli arrive?* <a href="vocabulary.html#rule-respond-to-rule-stream-continuous">continuous</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructed-emphasis">instructed emphasis</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-writing-device">writing device</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-block-duration">block duration</a>
- **Material:** A key pairing the digits 1-9 with abstract symbols, and a long series of digits (or symbols) to fill in.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A key pairs digits 1-9 with unique symbols.
    2. Participants fill in the correct symbol below each digit in a long sequence, working as quickly as possible for 90-120 seconds.
* - **Manipulations**
  - - Time limit
    - Paired vs. free recall variants
    - Incidental learning (recall symbols after test)
* - **Measurements**
  - - Number of correct substitutions in the time limit
    - Errors
    - Incidental recall of pairs
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
* - SDMT (Symbol-to-Digit; Smith)

    `hedvar_digit_symbol_substitution__sdmt_symbol_to_digit_smith`
  - named form
  - -
  - A named instrument that reverses the lookup direction, so the rows show symbols and the participant writes the paired digit.
* - Oral SDMT

    `hedvar_digit_symbol_substitution__oral_sdmt`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)
  - The participant says each digit aloud and the examiner writes it down.
* - Computerized DSST/SDMT

    `hedvar_digit_symbol_substitution__computerized_dsst_sdmt`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-touchscreen">touchscreen</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>; stream: <a href="vocabulary.html#rule-respond-to-rule-stream-discrete-trials">discrete trials</a>
  - -
  - Items appear one at a time on a screen and each key press or tap brings the next, so the continuous page becomes a series of self-paced discrete trials timed individually.
* - Paired-Associate Variant

    `hedvar_digit_symbol_substitution__paired_associate_variant`
  - named form
  - [Recall](../processes/long_term_memory.md#hed-recall)
  - After the timed substitution the key is removed and the participant is asked without warning which symbol went with each digit, adding a surprise cued-recall test of the pairs.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)

## Further references

- Hinton-Bayre, A. D., & Geffen, G. M. (2005). Comparability, reliability, and practice effects on alternate forms of the Digit Symbol Substitution and Symbol Digit Modalities Tests. *Psychological Assessment*, 17(2), 237-241. ([DOI](https://doi.org/10.1037/1040-3590.17.2.237), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16029111/))
- Baudouin, A., Clarys, D., Vanneste, S., & de Saint Hilaire, Z. (2009). Age-related changes in coding speed: Test-retest reliability and factor structure. *Aging, Neuropsychology, and Cognition*, 16(5), 553-567.
- Patel, V. P., Walker, L. A. S., & Feinstein, A. (2017). Revisiting cognitive reserve and cognition in multiple sclerosis: A closer look at the SDMT. *Multiple Sclerosis Journal*, 23(10), 1390-1399. ([DOI](https://doi.org/10.1177/1352458517692887), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28273771/))
- Hoyer, W. J., Stawski, R. S., Wasylyshyn, C., & Verhaeghen, P. (2004). Adult age and digit symbol substitution performance: A meta-analysis. *Psychology and Aging*, 19(1), 211-214. ([DOI](https://doi.org/10.1037/0882-7974.19.1.211), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15065945/))

## External links

- Cognitive Atlas: [symbol-digit substitution](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949e44)

