(hedtsk_instrumental_conditioning)=
# Instrumental Conditioning Task

**HED task ID:** `hedtsk_instrumental_conditioning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Operant Conditioning, Instrumental Learning, PIT, Pavlovian-Instrumental Transfer

Actions are reinforced by contingent outcomes under defined schedules; response rate and choice probability across schedules index instrumental learning. Specific human instantiations include lever/button-press reward paradigms and free-operant tasks.

## Description

In instrumental conditioning, voluntary actions are associated with rewarding or punishing consequences through repeated experience. Laboratory implementations present discrete choice options where specific responses are followed by desirable outcomes (food, money, points) or undesirable outcomes (loss, punishment). Common schedules include fixed-ratio, variable-ratio, fixed-interval, and variable-interval. Performance measures include response rates, choice patterns, and reaction times. The ventral striatum, dopamine system, and orbitofrontal cortex are critical for representing value predictions and learning from outcomes.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants perform actions (button presses, lever responses) that produce contingent outcomes (rewards or punishments) according to defined reinforcement schedules.
* - **Manipulation**
  - Reinforcement schedule (fixed ratio, variable ratio, fixed interval, variable interval); outcome valence; contingency degradation; Pavlovian-instrumental transfer.
* - **Measurement**
  - Response rate; choice probability; sensitivity to contingency and outcome devaluation; transfer effects between Pavlovian cues and instrumental actions.
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
* - Fixed Ratio (FR)

    `hedvar_instrumental_conditioning__fixed_ratio_fr`
  - Reinforcement after fixed number of responses.
  - Reward after fixed number of responses; canonical ratio schedule
* - Variable Ratio (VR)

    `hedvar_instrumental_conditioning__variable_ratio_vr`
  - Reinforcement after variable number of responses (average specified).
  - Reward after variable number of responses; different reinforcement statistics
* - Fixed Interval (FI)

    `hedvar_instrumental_conditioning__fixed_interval_fi`
  - Reinforcement for first response after fixed time period.
  - First response after fixed time rewarded; different temporal reinforcement structure
* - Variable Interval (VI)

    `hedvar_instrumental_conditioning__variable_interval_vi`
  - Reinforcement for first response after variable time period.
  - Variable time intervals; different temporal unpredictability
* - Progressive Ratio

    `hedvar_instrumental_conditioning__progressive_ratio`
  - Ratio requirement increases progressively; breakpoint indexes motivation.
  - Ratio requirement escalates; measures motivational breakpoint
* - Concurrent Choice

    `hedvar_instrumental_conditioning__concurrent_choice`
  - Multiple response options with different reinforcement schedules; matching law studies.
  - Two simultaneously available schedules; choice behavior reveals preference
* - Two-Stage Decision Task (Daw)

    `hedvar_instrumental_conditioning__two_stage_decision_task_daw`
  - Sequential choice task dissociating model-based (goal-directed) from model-free (habitual) learning.
  - Two-step Markov decision; measures model-based vs. model-free learning
* - Devaluation Paradigm

    `hedvar_instrumental_conditioning__devaluation_paradigm`
  - Reward value changed after learning; goal-directed behavior adjusts, habitual does not.
  - Outcome devaluation tests goal-directed vs. habitual control; different post-training procedure
* - Contingency Degradation

    `hedvar_instrumental_conditioning__contingency_degradation`
  - Weakening action-outcome relationship; tests sensitivity to causal structure.
  - Action-outcome contingency degraded; tests action sensitivity
* - Outcome-Specific Pavlovian-Instrumental Transfer (PIT)

    `hedvar_instrumental_conditioning__outcome_specific_pavlovian_instrumental_transfer_pit`
  - Pavlovian cues bias instrumental responding.
  - Pavlovian CS influences instrumental responding; different multi-phase design
* - Avoidance Learning

    `hedvar_instrumental_conditioning__avoidance_learning`
  - Responses prevent aversive outcomes; safety signal learning.
  - Response prevents aversive outcome; different valence and contingency structure
```

## Cognitive processes

This task is designed to engage the following processes:

- [Instrumental conditioning](../processes/associative_learning_and_reinforcement.md#hed-instrumental-conditioning)
- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Goal-directed behavior](../processes/associative_learning_and_reinforcement.md#hed-goal-directed-behavior)
- [Habit](../processes/associative_learning_and_reinforcement.md#hed-habit)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)

## Key references

- Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593-1599. ([DOI](https://doi.org/10.1126/science.275.5306.1593), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9054347/))
- Haber, S. N., & Knutson, B. (2010). The reward circuit: Linking primate anatomy and human imaging. *Neuropsychopharmacology*, 35(1), 4-26. ([DOI](https://doi.org/10.1038/npp.2010.129), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20736993/))

## Further references

- Balleine, B. W., & O'Doherty, J. P. (2010). Human and rodent homologies in action control: Corticostriatal determinants of goal-directed and habitual action. *Neuropsychopharmacology*, 35(1), 48–69. ([DOI](https://doi.org/10.1038/npp.2009.131), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19776734/))
- Dolan, R. J., & Dayan, P. (2013). Goals and habits in the brain. *Neuron*, 80(2), 312–325. ([DOI](https://doi.org/10.1016/j.neuron.2013.09.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24139036/))
- Lee, S. W., Shimojo, S., & O'Doherty, J. P. (2014). Neural computations underlying arbitration between model-based and model-free learning. *Neuron*, 81(3), 687–699. ([DOI](https://doi.org/10.1016/j.neuron.2013.11.028), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24507199/))
- Gillan, C. M., Kosinski, M., Whelan, R., Phelps, E. A., & Daw, N. D. (2016). Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. *eLife*, 5, e11305. ([DOI](https://doi.org/10.7554/elife.11305), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26928075/))

## External links

- Cognitive Atlas: [instrumental learning task](https://www.cognitiveatlas.org/task/id/trm_4f2414059baa8)

