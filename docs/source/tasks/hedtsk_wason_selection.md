(hedtsk_wason_selection)=
# Wason Selection Task

**HED task ID:** `hedtsk_wason_selection`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** Wason, Card Selection Task

Four cards with letters and numbers under a conditional rule; participants choose cards to turn over to test the rule. Indexes conditional reasoning and content effects.

## Description

The Wason Selection Task is the classic test of conditional reasoning. Participants see four cards, each showing information on both sides. A conditional rule is stated (e.g., "If a card has an A on one side, then it has a 2 on the other"). Cards show one side each (e.g., A, B, 2, 7), and participants must select which cards need to be turned over to test the rule. The correct answer is the card showing A (potentially confirming) and the card showing 7 (potentially falsifying), but most participants incorrectly select A and 2 (confirmation bias). When the rule is reframed in terms of social contracts (e.g., "If you drink alcohol, you must be over 21"), performance dramatically improves, supporting evolutionary theories of cheater-detection modules.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-solve-problem">Solve a puzzle</a> (`solve_problem`)
- **Game rules:** none are defined for this game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>, <a href="vocabulary.html#facet-stimulus-type-text">text</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-writing-device">writing device</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-rules">number of rules</a>
- **Material:** Four cards showing one side each (such as A, B, 2, 7) and a conditional rule, abstract or framed as a social contract.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants see four cards showing one side each and a conditional rule (if P then Q).
    2. They select which cards must be turned over to test the rule.
* - **Manipulations**
  - - Rule content (abstract vs. deontic/social contract)
    - Rule polarity
    - Number of rules
    - Thematic context
    - Task type (rule discovery by proposing triples)
* - **Measurements**
  - - Proportion selecting logically correct cards (P and not-Q)
    - Error patterns
    - Facilitation from social-contract framing
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
* - Social Contract Versions

    `hedvar_wason_selection__social_contract_versions`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - -
  - The rule is a benefit-for-requirement exchange and the participant looks for cheaters.
* - Wason 2-4-6 Task (Related)

    `hedvar_wason_selection__wason_2_4_6_task_related`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>; feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - [Inductive reasoning](../processes/reasoning_and_problem_solving.md#hed-inductive-reasoning)
  - A different rule-discovery task: the participant proposes number triples, is told whether each fits a hidden rule, and finally states the rule.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Deductive reasoning](../processes/reasoning_and_problem_solving.md#hed-deductive-reasoning)
- [Hypothesis testing](../processes/reasoning_and_problem_solving.md#hed-hypothesis-testing)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)

## Key references

- Wason, P. C. (1966). Reasoning. In B. M. Foss (Ed.), *New Horizons in Psychology* (pp. 135-151). Penguin.
- Cosmides, L. (1989). The logic of social exchange: Has natural selection shaped how humans reason? Studies with the Wason selection task. *Cognition*, 31(3), 187-276. ([DOI](https://doi.org/10.1016/0010-0277(89)90023-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/2743748/))
- Griggs, R. A., & Cox, J. R. (1982). The elusive thematic-materials effect in Wason's selection task. *British Journal of Psychology*, 73(3), 407-420. ([DOI](https://doi.org/10.1111/j.2044-8295.1982.tb01823.x))

## Further references

- Sperber, D., Cara, F., & Girotto, V. (1995). Relevance theory explains the selection task. *Cognition*, 57(1), 31-95. ([DOI](https://doi.org/10.1016/0010-0277(95)00666-m), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7587018/))
- Ragni, M., & Johnson-Laird, P. N. (2020). Reasoning about epistemic possibilities. *Acta Psychologica*, 208, 103081. ([DOI](https://doi.org/10.1016/j.actpsy.2020.103081), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32497740/))
- Oaksford, M., & Chater, N. (1994). A rational analysis of the selection task as optimal data selection. *Psychological Review*, 101(4), 608-631. ([DOI](https://doi.org/10.1037/0033-295x.101.4.608))

## External links

- Cognitive Atlas: [Wason card selection task](https://www.cognitiveatlas.org/task/id/trm_4f2449bdcb0b1)

- CogPO: [Deductive Reasoning Paradigm](http://www.wiki.cogpo.org/index.php?title=Deductive_Reasoning_Paradigm) (close match)

