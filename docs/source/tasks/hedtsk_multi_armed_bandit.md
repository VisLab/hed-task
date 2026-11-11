(hedtsk_multi_armed_bandit)=
# Multi-Armed Bandit Task

**HED task ID:** `hedtsk_multi_armed_bandit`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** MAB, Bandit Task, K-Armed Bandit, Multi-Armed Bandit

Repeated choice among options with unknown or changing reward distributions; choice sequences dissociate exploration from exploitation.

## Description

Participants choose among multiple options (the "arms" of a slot machine), each yielding rewards with unknown and often changing probabilities. The central challenge is the explore-exploit dilemma: whether to exploit the currently best-known option or explore alternatives that might yield higher returns. Reward probabilities may be stationary or volatile (drifting over time), with the volatile version (restless bandit) requiring continuous updating of value estimates. This paradigm is the dominant tool in computational psychiatry for studying reinforcement learning, and its computational tractability - fitting with Bayesian, Kalman-filter, or upper-confidence-bound models - has made it central to understanding decision-making deficits in addiction, schizophrenia, depression, and anxiety.

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
* - **Measurements**
  - - Total reward earned
    - Exploration-exploitation ratio
    - Fit to reinforcement learning models (learning rate, inverse temperature)
    - Regret
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
* - Two-Armed Stationary Bandit

    `hedvar_multi_armed_bandit__two_armed_stationary_bandit`
  - On each trial the participant chooses one of two options (often shown as slot machines or colored boxes) and receives a reward with a fixed probability for that option. The probabilities do not change, so the participant can learn the better option and stick with it.
  - Canonical two-option stationary reward structure; stable payoff distributions
* - Restless (Volatile) Bandit

    `hedvar_multi_armed_bandit__restless_volatile_bandit`
  - The reward probability or amount for each option drifts slowly and randomly over the session, so the best option changes. The participant must keep sampling options that seem worse to notice when they improve.
  - Reward probabilities drift over time; tests tracking of non-stationary environments
* - Contextual Bandit

    `hedvar_multi_armed_bandit__contextual_bandit`
  - A cue shown on each trial, such as a background color or a feature of the options, predicts which option is better. The participant must learn the rule linking the cue to the right choice.
  - Context features predict optimal choice; adds feature-based learning
* - Horizon Task (Wilson et al.)

    `hedvar_multi_armed_bandit__horizon_task_wilson_et_al`
  - The participant is told how many choices remain in the current game, either one or several. After some forced choices that show outcomes, the free choices reveal how much more people explore when there are many choices left to benefit from the information.
  - Fixed horizon with exploration vs. exploitation trade-off manipulation
* - Four-Armed Bandit with Reversal

    `hedvar_multi_armed_bandit__four_armed_bandit_with_reversal`
  - Four options are available and, at unannounced points, their reward probabilities swap so the previously best option becomes worse. The participant must notice and switch.
  - Four arms with explicit reversal phase; tests reversal learning in bandit
* - Informative vs. Non-Informative Exploration

    `hedvar_multi_armed_bandit__informative_vs_non_informative_exploration`
  - The design controls whether choosing an untried option actually teaches the participant something, for example by sometimes showing the outcomes of unchosen options, so that choices made for information can be separated from choices made at random.
  - Exploration choices yield differential information; changes exploration value
* - Social Bandit

    `hedvar_multi_armed_bandit__social_bandit`
  - Before or alongside their own choices, the participant sees the choices or outcomes of another player, and can use that player's experience to guide their own picks.
  - Observe another's choices; social learning component
* - Bandit with Effort Cost

    `hedvar_multi_armed_bandit__bandit_with_effort_cost`
  - Choosing or sampling an option costs physical or mental effort, for example several key presses or a difficult task, so the participant must weigh the cost of exploring against the value of what might be learned.
  - Effort cost added to choices; combines effort discounting with learning
* - Bandit with Partial Observability

    `hedvar_multi_armed_bandit__bandit_with_partial_observability`
  - In the usual task only the chosen option's outcome is shown. Here, in some conditions, the outcomes of all options are shown after each choice, so the participant can learn about options without choosing them and exploration is no longer needed for information.
  - Outcomes sometimes hidden; different information structure
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

