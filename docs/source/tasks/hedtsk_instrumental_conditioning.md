(hedtsk_instrumental_conditioning)=
# Instrumental Conditioning Task

**HED task ID:** `hedtsk_instrumental_conditioning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Operant Conditioning, Instrumental Learning, PIT, Pavlovian-Instrumental Transfer

Actions are reinforced by contingent outcomes under defined schedules; response rate and choice probability across schedules index instrumental learning. Specific human instantiations include lever/button-press reward paradigms and free-operant tasks.

## Description

In instrumental conditioning, voluntary actions are associated with rewarding or punishing consequences through repeated experience. Laboratory implementations present discrete choice options where specific responses are followed by desirable outcomes (food, money, points) or undesirable outcomes (loss, punishment). Common schedules include fixed-ratio, variable-ratio, fixed-interval, and variable-interval. Performance measures include response rates, choice patterns, and reaction times. The ventral striatum, dopamine system, and orbitofrontal cortex are critical for representing value predictions and learning from outcomes.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-payoff">Choose for a payoff</a> (`choose_for_payoff`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is traded against what?* <a href="vocabulary.html#rule-choose-for-payoff-tradeoff-amount-vs-effort">amount vs effort</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-goal">reward goal</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-gain">gain</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-choice">choice</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-food">food</a>, <a href="vocabulary.html#motivator-what-money">money</a>, <a href="vocabulary.html#motivator-what-points">points</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>, <a href="vocabulary.html#facet-stimulus-type-food">food</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Choice options whose responses are followed, on a reinforcement schedule, by rewards (food, money, points) or losses.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants perform actions (button presses, lever responses) that produce contingent outcomes (rewards or punishments) according to defined reinforcement schedules.
    2. Optional: After training, the earned outcome is made less desirable and responding is tested without reward.
* - **Manipulations**
  - - Reinforcement schedule (fixed ratio, variable ratio, fixed interval, variable interval, progressive ratio)
    - Outcome valence
    - Contingency degradation
    - Pavlovian-instrumental transfer
    - Number of concurrent options (concurrent schedules)
* - **Measurements**
  - - Response rate
    - Choice probability
    - Sensitivity to contingency and outcome devaluation
    - Transfer effects between Pavlovian cues and instrumental actions
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
* - Progressive Ratio

    `hedvar_instrumental_conditioning__progressive_ratio`
  - option set: <a href="vocabulary.html#rule-choose-for-payoff-option-set-one-option-with-stop">one option with stop</a>
  - [Effort allocation](../processes/reward_anticipation_and_motivation.md#hed-effort-allocation)
  - The response requirement rises after each reward and the participant may quit at any time, so the schedule becomes a single escalating option with a stop decision; progressive ratio is not among the listed schedule levels.
* - Concurrent Choice

    `hedvar_instrumental_conditioning__concurrent_choice`
  - named form
  - [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)
  - Two or more response options are available at once, each on its own schedule, so the participant allocates responses among options with hidden payoff rates.
* - Devaluation Paradigm

    `hedvar_instrumental_conditioning__devaluation_paradigm`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-devaluation">devaluation</a>, <a href="vocabulary.html#phase-test">test</a>
  - -
  - After training, the earned outcome is made less desirable and responding is tested without reward.
* - Contingency Degradation

    `hedvar_instrumental_conditioning__contingency_degradation`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>
  - -
  - After training, the reward is delivered whether or not the participant responds.
* - Outcome-Specific Pavlovian-Instrumental Transfer (PIT)

    `hedvar_instrumental_conditioning__outcome_specific_pavlovian_instrumental_transfer_pit`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-transfer">transfer</a>
  - [Pavlovian conditioning](../processes/associative_learning_and_reinforcement.md#hed-pavlovian-conditioning)
  - A separate Pavlovian phase of cue-outcome pairings is added, and a final transfer test presents the cues during free responding.
* - Avoidance Learning

    `hedvar_instrumental_conditioning__avoidance_learning`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>, <a href="vocabulary.html#facet-stimulus-modality-somatic">somatic</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>, <a href="vocabulary.html#facet-stimulus-type-noise">noise</a>, <a href="vocabulary.html#facet-stimulus-type-electrical">electrical</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>; sign: <a href="vocabulary.html#motivator-sign-loss">loss</a>; what: <a href="vocabulary.html#motivator-what-aversive">aversive</a>
  - [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation), [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception), [Somatosensory perception](../processes/face_and_object_perception.md#hed-somatosensory-perception)
  - The response prevents an unpleasant outcome (shock, noise, loss of money) instead of earning a reward.
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

