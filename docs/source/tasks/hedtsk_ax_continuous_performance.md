(hedtsk_ax_continuous_performance)=
# AX Continuous Performance Task

**HED task ID:** `hedtsk_ax_continuous_performance`

**Family:** [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md)

**Also known as:** AX-CPT, AX-CPT (Context Processing)

Letters come in cue-probe pairs and the target is an X only when it follows an A; errors on the pairs that break the rule index use of the held cue.

## Description

Letters appear in pairs. The participant presses the target key only when an X follows an A; an X after any other letter, or any other letter after an A, gets the non-target key. The participant has to remember the previous letter to respond correctly, and A-then-X pairs are made frequent so that the A creates a strong expectation.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
  - *Is something held in mind to compare against?* <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-target-probability">target probability</a>
- **Material:** Letters in cue-probe pairs, an A or another letter followed by an X or another letter, with A-then-X pairs frequent.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Letters are presented in cue-probe pairs.
    2. Participants press the target key when an X follows an A and the non-target key for every other cue-probe pair.
* - **Manipulations**
  - - Trial type (AX, AY, BX, BY)
    - Proportion of AX pairs
* - **Measurements**
  - - Error rate by trial type
    - RT by trial type
```

## Cognitive processes

This task is designed to engage the following processes:

- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Alerting](../processes/selective_and_sustained_attention.md#hed-alerting)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Spontaneous thought](../processes/awareness_agency_and_metacognition.md#hed-mind-wandering)
- [Goal maintenance](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-goal-maintenance)
- [Proactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-proactive-control)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)

## Key references

- Carter, C. S., Braver, T. S., Barch, D. M., Botvinick, M. M., Noll, D., & Cohen, J. D. (1998). Anterior cingulate cortex, error detection, and the online monitoring of performance. *Science*, 280(5364), 747-749. ([DOI](https://doi.org/10.1126/science.280.5364.747), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9563953/))

## External links

- Cognitive Atlas: [AX-CPT task](https://www.cognitiveatlas.org/task/id/trm_4c40d2a93ea15)

