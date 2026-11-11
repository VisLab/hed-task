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
* - **Manipulations**
  - - Reinforcement schedule (fixed ratio, variable ratio, fixed interval, variable interval)
    - Outcome valence
    - Contingency degradation
    - Pavlovian-instrumental transfer
* - **Measurements**
  - - Response rate
    - Choice probability
    - Sensitivity to contingency and outcome devaluation
    - Transfer effects between Pavlovian cues and instrumental actions
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
  - A reward (points, money or food) is delivered after every fixed number of responses, for example every tenth press. The participant learns how many presses each reward costs.
  - Reward after fixed number of responses; canonical ratio schedule
* - Variable Ratio (VR)

    `hedvar_instrumental_conditioning__variable_ratio_vr`
  - A reward is delivered after an unpredictable number of responses that average a set value, like a slot machine. Produces high steady rates of responding.
  - Reward after variable number of responses; different reinforcement statistics
* - Fixed Interval (FI)

    `hedvar_instrumental_conditioning__fixed_interval_fi`
  - A reward is available only after a fixed time has passed since the last reward, and the first response after that time earns it. Responses before the interval ends do nothing.
  - First response after fixed time rewarded; different temporal reinforcement structure
* - Variable Interval (VI)

    `hedvar_instrumental_conditioning__variable_interval_vi`
  - Like the fixed interval schedule, but the waiting time before a reward becomes available varies unpredictably around an average.
  - Variable time intervals; different temporal unpredictability
* - Progressive Ratio

    `hedvar_instrumental_conditioning__progressive_ratio`
  - The number of responses needed for each successive reward increases, for example 5, then 10, then 20. The point at which the participant stops responding (the breakpoint) measures how hard they are willing to work for the reward.
  - Ratio requirement escalates; measures motivational breakpoint
* - Concurrent Choice

    `hedvar_instrumental_conditioning__concurrent_choice`
  - Two or more response options are available at the same time, each paying off on its own schedule. How the participant divides responses between them is compared with the relative rates of reward.
  - Two simultaneously available schedules; choice behavior reveals preference
* - Two-Stage Decision Task (Daw)

    `hedvar_instrumental_conditioning__two_stage_decision_task_daw`
  - A choice between two options leads, with set probabilities, to one of two second-stage states, where another choice yields a reward with slowly changing probability. Whether a participant's choices reflect knowledge of the transition structure separates planning from habit. Cataloged in its own right as the Two-Stage Decision Task.
  - Two-step Markov decision; measures model-based vs. model-free learning
* - Devaluation Paradigm

    `hedvar_instrumental_conditioning__devaluation_paradigm`
  - After learning that a response earns a particular reward, the reward is made less desirable, for example by feeding the participant that food to satiety or by telling them it is no longer worth points. A test follows without rewards. Responding that drops shows goal-directed control; responding that persists shows habit.
  - Outcome devaluation tests goal-directed vs. habitual control; different post-training procedure
* - Contingency Degradation

    `hedvar_instrumental_conditioning__contingency_degradation`
  - After learning, the reward begins to appear whether or not the participant responds, so the response no longer makes a difference. A drop in responding shows that the participant is tracking what their actions cause.
  - Action-outcome contingency degraded; tests action sensitivity
* - Outcome-Specific Pavlovian-Instrumental Transfer (PIT)

    `hedvar_instrumental_conditioning__outcome_specific_pavlovian_instrumental_transfer_pit`
  - In separate phases the participant learns that certain cues predict certain rewards and that certain responses earn those same rewards. In a final test the cues are presented while the participant can respond freely, and a cue increases responding for the reward it predicts.
  - Pavlovian CS influences instrumental responding; different multi-phase design
* - Avoidance Learning

    `hedvar_instrumental_conditioning__avoidance_learning`
  - Instead of earning a reward, a response prevents an unpleasant outcome such as a shock, loud noise or loss of money. The participant learns which response, or which response to which warning signal, keeps the outcome away.
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

- Balleine, B. W., & O'Doherty, J. P. (2010). Human and rodent homologies in action control: Corticostriatal determinants of goal-directed and habitual action. *Neuropsychopharmacology*, 35(1), 48-69. ([DOI](https://doi.org/10.1038/npp.2009.131), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19776734/))
- Dolan, R. J., & Dayan, P. (2013). Goals and habits in the brain. *Neuron*, 80(2), 312-325. ([DOI](https://doi.org/10.1016/j.neuron.2013.09.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24139036/))
- Lee, S. W., Shimojo, S., & O'Doherty, J. P. (2014). Neural computations underlying arbitration between model-based and model-free learning. *Neuron*, 81(3), 687-699. ([DOI](https://doi.org/10.1016/j.neuron.2013.11.028), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24507199/))
- Gillan, C. M., Kosinski, M., Whelan, R., Phelps, E. A., & Daw, N. D. (2016). Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. *eLife*, 5, e11305. ([DOI](https://doi.org/10.7554/elife.11305), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26928075/))

## External links

- Cognitive Atlas: [instrumental learning task](https://www.cognitiveatlas.org/task/id/trm_4f2414059baa8)

