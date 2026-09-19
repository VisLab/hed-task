(hedtsk_wason_selection)=
# Wason Selection Task

**HED task ID:** `hedtsk_wason_selection`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** Wason, Card Selection Task

Four cards with letters and numbers under a conditional rule; participants choose cards to turn over to test the rule. Indexes conditional reasoning and content effects.

## Description

The Wason Selection Task is the classic test of conditional reasoning. Participants see four cards, each showing information on both sides. A conditional rule is stated (e.g., "If a card has an A on one side, then it has a 2 on the other"). Cards show one side each (e.g., A, B, 2, 7), and participants must select which cards need to be turned over to test the rule. The correct answer is the card showing A (potentially confirming) and the card showing 7 (potentially falsifying), but most participants incorrectly select A and 2 (confirmation bias). When the rule is reframed in terms of social contracts (e.g., "If you drink alcohol, you must be over 21"), performance dramatically improves, supporting evolutionary theories of cheater-detection modules.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants see four cards showing one side each and a conditional rule (if P then Q). They select which cards must be turned over to test the rule.
* - **Manipulation**
  - Rule content (abstract vs. deontic/social contract); rule polarity; number of rules; thematic context.
* - **Measurement**
  - Proportion selecting logically correct cards (P and not-Q); error patterns; facilitation from social-contract framing.
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
* - Abstract Wason Task (Standard)

    `hedvar_wason_selection__abstract_wason_task_standard`
  - Letters and numbers; tests pure conditional reasoning.
  - Canonical abstract conditional reasoning; select cards to test rule
* - Thematic/Concrete Versions

    `hedvar_wason_selection__thematic_concrete_versions`
  - Meaningful content (e.g., "drinking age" rule); facilitates correct selection.
  - Concrete familiar content; tests facilitation of abstract reasoning
* - Social Contract Versions

    `hedvar_wason_selection__social_contract_versions`
  - Rules framed as social exchanges with costs and benefits; tests cheater detection.
  - Cheater-detection framing; different evolutionary content domain
* - Precaution Rules

    `hedvar_wason_selection__precaution_rules`
  - "If X is hazardous, take precaution Y"; tests hazard management reasoning.
  - Safety precaution framing; different pragmatic rule type
* - Deontic vs. Indicative Rules

    `hedvar_wason_selection__deontic_vs_indicative_rules`
  - Permission/obligation rules vs. factual conditional statements.
  - Permission/obligation vs. descriptive conditional; different rule semantics
* - Negated Rules

    `hedvar_wason_selection__negated_rules`
  - Rules with negation ("If not A, then B"); increases difficulty dramatically.
  - Negation in conditional changes logical structure
* - Probabilistic Selection Task

    `hedvar_wason_selection__probabilistic_selection`
  - Probabilistic rather than deterministic rule testing.
  - Probabilistic card selection instead of binary; different decision format
* - Wason 2-4-6 Task (Related)

    `hedvar_wason_selection__wason_2_4_6_task_related`
  - Discover the rule generating number triples; tests hypothesis formation and confirmation bias.
  - Hypothesis-testing number sequence task; related reasoning paradigm
```

## Cognitive processes

This task is designed to engage the following processes:

- [Deductive reasoning](../processes/reasoning_and_problem_solving.md#hed-deductive-reasoning)
- [Hypothesis testing](../processes/reasoning_and_problem_solving.md#hed-hypothesis-testing)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)

## Key references

- Wason, P. C. (1966). Reasoning. In B. M. Foss (Ed.), *New Horizons in Psychology* (pp. 135–151). Penguin.
- Cosmides, L. (1989). The logic of social exchange: Has natural selection shaped how humans reason? Studies with the Wason selection task. *Cognition*, 31(3), 187–276. ([DOI](https://doi.org/10.1016/0010-0277(89)90023-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/2743748/))
- Griggs, R. A., & Cox, J. R. (1982). The elusive thematic-materials effect in Wason's selection task. *British Journal of Psychology*, 73(3), 407–420. ([DOI](https://doi.org/10.1111/j.2044-8295.1982.tb01823.x))

## Further references

- Sperber, D., Cara, F., & Girotto, V. (1995). Relevance theory explains the selection task. *Cognition*, 57(1), 31–95. ([DOI](https://doi.org/10.1016/0010-0277(95)00666-m), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7587018/))
- Ragni, M., & Johnson-Laird, P. N. (2020). Reasoning about epistemic possibilities. *Acta Psychologica*, 208, 103081. ([DOI](https://doi.org/10.1016/j.actpsy.2020.103081), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32497740/))
- Oaksford, M., & Chater, N. (1994). A rational analysis of the selection task as optimal data selection. *Psychological Review*, 101(4), 608–631. ([DOI](https://doi.org/10.1037/0033-295x.101.4.608))

## External links

- Cognitive Atlas: [Wason card selection task](https://www.cognitiveatlas.org/task/id/trm_4f2449bdcb0b1)

