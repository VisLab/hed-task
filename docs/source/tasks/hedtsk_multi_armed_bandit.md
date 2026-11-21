(hedtsk_multi_armed_bandit)=
# Multi-Armed Bandit Task

**HED task ID:** `hedtsk_multi_armed_bandit`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** MAB, Bandit Task, K-Armed Bandit, Multi-Armed Bandit

Repeated choice among options with unknown or changing reward distributions; choice sequences dissociate exploration from exploitation.

## Description

Participants choose among multiple options (the "arms" of a slot machine), each yielding rewards with unknown and often changing probabilities. The central challenge is the explore-exploit dilemma: whether to exploit the currently best-known option or explore alternatives that might yield higher returns. Reward probabilities may be stationary or volatile (drifting over time), with the volatile version (restless bandit) requiring continuous updating of value estimates. This paradigm is the dominant tool in computational psychiatry for studying reinforcement learning, and its computational tractability - fitting with Bayesian, Kalman-filter, or upper-confidence-bound models - has made it central to understanding decision-making deficits in addiction, schizophrenia, depression, and anxiety.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-payoff">Choose for a payoff</a> (`choose_for_payoff`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is traded against what?* <a href="vocabulary.html#rule-choose-for-payoff-tradeoff-explore-vs-exploit">explore vs exploit</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-goal">reward goal</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-gain">gain</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-choice">choice</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-points">points</a>, <a href="vocabulary.html#motivator-what-money">money</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>, <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-alternatives">number of alternatives</a>, <a href="vocabulary.html#setting-number-of-trials">number of trials</a>
- **Material:** Several options, the arms of a slot machine, each paying out rewards with unknown probabilities that are stationary or drifting.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants choose repeatedly among multiple options (arms) that deliver stochastic rewards drawn from different distributions.
    2. They must balance exploring unknown options with exploiting known good ones.
* - **Manipulations**
  - - Number of arms
    - Reward distributions (stationary vs. drifting)
    - Horizon length
    - Information asymmetry
    - Cue before each trial (contextual vs. none)
    - Effort cost of sampling an option
* - **Measurements**
  - - Total reward earned
    - Exploration-exploitation ratio
    - Fit to reinforcement learning models (learning rate, inverse temperature)
    - Regret
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
* - Restless (Volatile) Bandit

    `hedvar_multi_armed_bandit__restless_volatile_bandit`
  - contingency stability: <a href="vocabulary.html#rule-choose-for-payoff-contingency-stability-drifting">drifting</a>
  - -
  - Each option's reward probability or amount drifts slowly and randomly over the session, so the best option changes.
* - Contextual Bandit

    `hedvar_multi_armed_bandit__contextual_bandit`

    Cognitive Atlas: [contextual bandit](https://www.cognitiveatlas.org/task/id/tsk_3ICXMd8R3ekcb)
  - contingency cue: <a href="vocabulary.html#rule-choose-for-payoff-contingency-cue-per-trial-cue">per trial cue</a>
  - [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
  - A cue shown on each trial predicts which option is better, so the participant learns which choice goes with which cue.
* - Four-Armed Bandit with Reversal

    `hedvar_multi_armed_bandit__four_armed_bandit_with_reversal`
  - contingency stability: <a href="vocabulary.html#rule-choose-for-payoff-contingency-stability-reversal">reversal</a>
  - [Reversal learning](../processes/associative_learning_and_reinforcement.md#hed-reversal-learning)
  - Four options whose reward probabilities swap at unannounced points.
* - Social Bandit

    `hedvar_multi_armed_bandit__social_bandit`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>
  - [Social decision making](../processes/social_cognition_and_strategic_social_choice.md#hed-social-decision-making)
  - The choices or outcomes of another player are shown before or alongside the participant's own.
* - Bandit with Effort Cost

    `hedvar_multi_armed_bandit__bandit_with_effort_cost`
  - sign: <a href="vocabulary.html#motivator-sign-both">both</a>; what: <a href="vocabulary.html#motivator-what-points">points</a>, <a href="vocabulary.html#motivator-what-money">money</a>, <a href="vocabulary.html#motivator-what-effort-cost">effort cost</a>
  - [Effort allocation](../processes/reward_anticipation_and_motivation.md#hed-effort-allocation)
  - Choosing or sampling an option costs key presses or a hard task, so exploration carries an effort cost on top of the usual tradeoff.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Value learning](../processes/associative_learning_and_reinforcement.md#hed-value-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)
- [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use)

## Key references

- Daw, N. D., O'Doherty, J. P., Dayan, P., Seymour, B., & Dolan, R. J. (2006). Cortical substrates for exploratory decisions in humans. *Nature*, 441, 876-879. ([DOI](https://doi.org/10.1038/nature04766), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16778890/))

## Further references

- Gershman, S. J. (2018). Deconstructing the human algorithms for exploration. *Cognition*, 173, 34-42. ([DOI](https://doi.org/10.1016/j.cognition.2017.12.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29289795/))
- Schulz, E., & Gershman, S. J. (2019). The algorithmic architecture of exploration in the human brain. *Current Opinion in Neurobiology*, 55, 7-14. ([DOI](https://doi.org/10.1016/j.conb.2018.11.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30529148/))
- Cogliati Dezza, I., Yu, A. J., Cleeremans, A., & Alexander, W. (2017). Learning the value of information and reward over time when solving exploration-exploitation problems. *Scientific Reports*, 7, 16919. ([DOI](https://doi.org/10.1038/s41598-017-17237-w), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29209058/))
- Chakroun, K., Mathar, D., Wiehler, A., Ganzer, F., & Peters, J. (2020). Dopaminergic modulation of the exploration/exploitation trade-off in human decision-making. *eLife*, 9, e51260. ([DOI](https://doi.org/10.7554/elife.51260), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32484779/))

## External links

- Cognitive Atlas: [Volatile Bandit](https://www.cognitiveatlas.org/task/id/trm_5696b180169bd) (close match)

