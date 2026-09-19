(hedtsk_multi_armed_bandit)=
# Multi-Armed Bandit Task

**HED task ID:** `hedtsk_multi_armed_bandit`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** MAB, Bandit Task, K-Armed Bandit, Multi-Armed Bandit

Repeated choice among options with unknown or changing reward distributions; choice sequences dissociate exploration from exploitation.

## Description

Participants choose among multiple options (the "arms" of a slot machine), each yielding rewards with unknown and often changing probabilities. The central challenge is the explore-exploit dilemma: whether to exploit the currently best-known option or explore alternatives that might yield higher returns. Reward probabilities may be stationary or volatile (drifting over time), with the volatile version (restless bandit) requiring continuous updating of value estimates. This paradigm is the dominant tool in computational psychiatry for studying reinforcement learning, and its computational tractability — fitting with Bayesian, Kalman-filter, or upper-confidence-bound models — has made it central to understanding decision-making deficits in addiction, schizophrenia, depression, and anxiety.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants choose repeatedly among multiple options (arms) that deliver stochastic rewards drawn from different distributions. They must balance exploring unknown options with exploiting known good ones.
* - **Manipulation**
  - Number of arms; reward distributions (stationary vs. drifting); horizon length; information asymmetry.
* - **Measurement**
  - Total reward earned; exploration-exploitation ratio; fit to reinforcement learning models (learning rate, inverse temperature); regret.
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
  - Simplest version; two options with fixed reward probabilities.
  - Canonical two-option stationary reward structure; stable payoff distributions
* - Restless (Volatile) Bandit

    `hedvar_multi_armed_bandit__restless_volatile_bandit`
  - Reward probabilities drift over time via Gaussian random walk; requires continuous updating.
  - Reward probabilities drift over time; tests tracking of non-stationary environments
* - Contextual Bandit

    `hedvar_multi_armed_bandit__contextual_bandit`
  - Reward probabilities depend on observable context features; tests generalization across contexts.
  - Context features predict optimal choice; adds feature-based learning
* - Horizon Task (Wilson et al.)

    `hedvar_multi_armed_bandit__horizon_task_wilson_et_al`
  - Short vs. long decision horizons to separately measure directed and random exploration.
  - Fixed horizon with exploration vs. exploitation trade-off manipulation
* - Four-Armed Bandit with Reversal

    `hedvar_multi_armed_bandit__four_armed_bandit_with_reversal`
  - Multiple arms with occasional reward-probability reversals; combines bandit with reversal-learning demands.
  - Four arms with explicit reversal phase; tests reversal learning in bandit
* - Informative vs. Non-Informative Exploration

    `hedvar_multi_armed_bandit__informative_vs_non_informative_exploration`
  - Designs that separate information-seeking exploration from random exploration (e.g., observed vs. chosen options).
  - Exploration choices yield differential information; changes exploration value
* - Social Bandit

    `hedvar_multi_armed_bandit__social_bandit`
  - Observing another agent's choices and outcomes before making own decisions; adds social learning dimension.
  - Observe another's choices; social learning component
* - Bandit with Effort Cost

    `hedvar_multi_armed_bandit__bandit_with_effort_cost`
  - Incorporating physical or cognitive effort cost into exploration decisions.
  - Effort cost added to choices; combines effort discounting with learning
* - Bandit with Partial Observability

    `hedvar_multi_armed_bandit__bandit_with_partial_observability`
  - Only the chosen arm's outcome is observed (standard) vs. all arms' outcomes are observed; separates learning from exploration.
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

- Daw, N. D., O'Doherty, J. P., Dayan, P., Seymour, B., & Dolan, R. J. (2006). Cortical substrates for exploratory decisions in humans. *Nature*, 441, 876–879. ([DOI](https://doi.org/10.1038/nature04766), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16778890/))

## Further references

- Gershman, S. J. (2018). Deconstructing the human algorithms for exploration. *Cognition*, 173, 34–42. ([DOI](https://doi.org/10.1016/j.cognition.2017.12.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29289795/))
- Schulz, E., & Gershman, S. J. (2019). The algorithmic architecture of exploration in the human brain. *Current Opinion in Neurobiology*, 55, 7–14. ([DOI](https://doi.org/10.1016/j.conb.2018.11.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30529148/))
- Cogliati Dezza, I., Yu, A. J., Cleeremans, A., & Alexander, W. (2017). Learning the value of information and reward over time when solving exploration–exploitation problems. *Scientific Reports*, 7, 16919. ([DOI](https://doi.org/10.1038/s41598-017-17237-w), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29209058/))
- Chakroun, K., Mathar, D., Wiehler, A., Ganzer, F., & Peters, J. (2020). Dopaminergic modulation of the exploration/exploitation trade-off in human decision-making. *eLife*, 9, e51260. ([DOI](https://doi.org/10.7554/elife.51260), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32484779/))

## External links

- Cognitive Atlas: [Volatile Bandit](https://www.cognitiveatlas.org/task/id/trm_5696b180169bd) (close match)

