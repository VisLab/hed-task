(hedtsk_multi_armed_bandit)=

# Multi-Armed Bandit Task

**HED Task ID:** `hedtsk_multi_armed_bandit`

**Also known as:** MAB, Bandit Task, K-Armed Bandit

Repeated choice among options with unknown or changing reward distributions; choice sequences dissociate exploration from exploitation.

## Description

Participants choose among multiple options (the "arms" of a slot machine), each yielding rewards with unknown and often changing probabilities. The central challenge is the explore-exploit dilemma: whether to exploit the currently best-known option or explore alternatives that might yield higher returns. Reward probabilities may be stationary or volatile (drifting over time), with the volatile version (restless bandit) requiring continuous updating of value estimates. This paradigm is the dominant tool in computational psychiatry for studying reinforcement learning, and its computational tractability — fitting with Bayesian, Kalman-filter, or upper-confidence-bound models — has made it central to understanding decision-making deficits in addiction, schizophrenia, depression, and anxiety.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - Participants choose repeatedly among multiple options (arms) that deliver stochastic rewards drawn from different distributions. They must balance exploring unknown options with exploiting known good ones.
* - **Manipulation**
  - Number of arms; reward distributions (stationary vs. drifting); horizon length; information asymmetry.
* - **Measurement**
  - Total reward earned; exploration-exploitation ratio; fit to reinforcement learning models (learning rate, inverse temperature); regret.
```

## Variations

```{list-table}
---
widths: 25 40 35
header-rows: 1
---
* - Variation
  - Description
  - Justification
* - Two-Armed Stationary Bandit
  - Simplest version; two options with fixed reward probabilities.
  - Canonical two-option stationary reward structure; stable payoff distributions
* - Restless (Volatile) Bandit
  - Reward probabilities drift over time via Gaussian random walk; requires continuous updating.
  - Reward probabilities drift over time; tests tracking of non-stationary environments
* - Contextual Bandit
  - Reward probabilities depend on observable context features; tests generalization across contexts.
  - Context features predict optimal choice; adds feature-based learning
* - Horizon Task (Wilson et al.)
  - Short vs. long decision horizons to separately measure directed and random exploration.
  - Fixed horizon with exploration vs. exploitation trade-off manipulation
* - Four-Armed Bandit with Reversal
  - Multiple arms with occasional reward-probability reversals; combines bandit with reversal-learning demands.
  - Four arms with explicit reversal phase; tests reversal learning in bandit
* - Informative vs. Non-Informative Exploration
  - Designs that separate information-seeking exploration from random exploration (e.g., observed vs. chosen options).
  - Exploration choices yield differential information; changes exploration value
* - Social Bandit
  - Observing another agent's choices and outcomes before making own decisions; adds social learning dimension.
  - Observe another's choices; social learning component
* - Bandit with Effort Cost
  - Incorporating physical or cognitive effort cost into exploration decisions.
  - Effort cost added to choices; combines effort discounting with learning
* - Bandit with Partial Observability
  - Only the chosen arm's outcome is observed (standard) vs. all arms' outcomes are observed; separates learning from exploration.
  - Outcomes sometimes hidden; different information structure
```

## Cognitive processes

This task engages the following cognitive processes:

- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Value learning](../processes/associative_learning_and_reinforcement.md#hed-value-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)
- [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use)

## Key references

- {'authors': "Daw, N. D., O'Doherty, J. P., Dayan, P., Seymour, B., & Dolan, R. J.", 'year': 2006, 'title': 'Cortical substrates for exploratory decisions in humans', 'venue': 'Nature', 'venue_type': 'journal', 'journal': 'Nature', 'volume': '441', 'issue': '7095', 'pages': '876-879', 'doi': '10.1038/nature04766', 'openalex_id': None, 'pmid': None, 'citation_string': "Daw, N. D., O'Doherty, J. P., Dayan, P., Seymour, B., & Dolan, R. J. (2006). Cortical substrates for exploratory decisions in humans. *Nature*, 441, 876–879.", 'url': 'https://doi.org/10.1038/nature04766', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'Gershman, S. J.', 'year': 2018, 'title': 'Deconstructing the human algorithms for exploration', 'venue': 'Cognition', 'venue_type': 'journal', 'journal': 'Cognition', 'volume': '173', 'issue': None, 'pages': '34-42', 'doi': '10.1016/j.cognition.2017.12.014', 'openalex_id': None, 'pmid': None, 'citation_string': 'Gershman, S. J. (2018). Deconstructing the human algorithms for exploration. *Cognition*, 173, 34–42.', 'url': 'https://doi.org/10.1016/j.cognition.2017.12.014', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Schulz, E., & Gershman, S. J.', 'year': 2019, 'title': 'The algorithmic architecture of exploration in the human brain', 'venue': 'Current Opinion in Neurobiology', 'venue_type': 'journal', 'journal': 'Current Opinion in Neurobiology', 'volume': '55', 'issue': None, 'pages': '7-14', 'doi': '10.1016/j.conb.2018.11.003', 'openalex_id': None, 'pmid': None, 'citation_string': 'Schulz, E., & Gershman, S. J. (2019). The algorithmic architecture of exploration in the human brain. *Current Opinion in Neurobiology*, 55, 7–14.', 'url': 'https://doi.org/10.1016/j.conb.2018.11.003', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Cogliati Dezza, I., Yu, A. J., Cleeremans, A., & Alexander, W.', 'year': 2017, 'title': 'Learning the value of information and reward over time when solving exploration-exploitation problems', 'venue': 'Scientific Reports', 'venue_type': 'journal', 'journal': 'Scientific Reports', 'volume': '7', 'issue': '1', 'pages': None, 'doi': '10.1038/s41598-017-17237-w', 'openalex_id': None, 'pmid': None, 'citation_string': 'Cogliati Dezza, I., Yu, A. J., Cleeremans, A., & Alexander, W. (2017). Learning the value of information and reward over time when solving exploration–exploitation problems. *Scientific Reports*, 7, 16919.', 'url': 'https://doi.org/10.1038/s41598-017-17237-w', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Chakroun, K., Mathar, D., Wiehler, A., Ganzer, F., & Peters, J.', 'year': 2020, 'title': 'Dopaminergic modulation of the exploration/exploitation trade-off in human decision-making', 'venue': 'eLife', 'venue_type': 'journal', 'journal': 'eLife', 'volume': '9', 'issue': None, 'pages': None, 'doi': '10.7554/elife.51260', 'openalex_id': None, 'pmid': None, 'citation_string': 'Chakroun, K., Mathar, D., Wiehler, A., Ganzer, F., & Peters, J. (2020). Dopaminergic modulation of the exploration/exploitation trade-off in human decision-making. *eLife*, 9, e51260.', 'url': 'https://doi.org/10.7554/elife.51260', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [Volatile Bandit](https://www.cognitiveatlas.org/task/id/trm_5696b180169bd) (close match)
