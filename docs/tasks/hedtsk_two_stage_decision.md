(hedtsk_two_stage_decision)=

# Two-Stage Decision Task

**HED Task ID:** `hedtsk_two_stage_decision`

**Also known as:** Two-Step Task, Daw Task, MB/MF Task

Sequential two-choice task with probabilistic transitions to second-stage states and drifting rewards; choice patterns dissociate model-based from model-free control.

## Description

Participants make two sequential choices per trial. The first-stage choice leads (with fixed transition probabilities — 70% common, 30% rare) to one of two second-stage states, each containing its own pair of options. Second-stage options yield rewards with slowly drifting probabilities. Daw et al. (2011) designed this task to dissociate model-based reinforcement learning (using knowledge of the transition structure to plan) from model-free reinforcement learning (repeating previously rewarded actions regardless of transition type). The diagnostic signature is the interaction between reward and transition type on subsequent first-stage choices: model-based agents show opposite stay/switch patterns after common vs. rare transitions, while model-free agents show the same pattern regardless of transition type.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - First stage: choose between two options that lead probabilistically (70/30) to one of two second-stage choice sets. Second stage: choose between two options with drifting reward probabilities. This separates model-based from model-free learning.
* - **Manipulation**
  - Transition structure (common vs. rare); reward probability drift rate; reward magnitude.
* - **Measurement**
  - Stay probability as a function of previous trial outcome × transition type; model-based index; computational model fits (hybrid MB/MF learning rates, mixing weight).
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
* - Standard Daw et al. (2011) Version
  - Two first-stage options, two second-stage states, each with two options; 70/30 transition probabilities.
  - Canonical two-step Markov decision task; measures model-based vs. model-free
* - Shortened/Simplified Versions
  - Fewer trials or simplified transition structure for clinical or developmental populations.
  - Fewer trials or simplified state structure; recognized efficient version
* - Enhanced Model-Based Version
  - More complex transition structures (three or more stages) to increase model-based demands.
  - Design features that enhance model-based learning; different incentive structure
* - Devaluation Manipulation
  - Changing reward magnitudes mid-task to test sensitivity to outcome value (model-based predicts rapid adjustment).
  - Reward devalued after training; tests habitual vs. goal-directed control
* - Two-Stage with Instructed Knowledge
  - Explicitly teaching the transition structure before the task; tests whether model-based behavior increases with explicit knowledge.
  - Transition structure explicitly taught; tests instructed vs. learned model
```

## Cognitive processes

This task engages the following cognitive processes:

- [Model-based learning](../processes/associative_learning_and_reinforcement.md#hed-model-based-learning)
- [Model-free learning](../processes/associative_learning_and_reinforcement.md#hed-model-free-learning)
- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)

## Key references

- {'authors': 'Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P., & Dolan, R. J.', 'year': 2011, 'title': "Model-Based Influences on Humans' Choices and Striatal Prediction Errors", 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '69', 'issue': '6', 'pages': '1204-1215', 'doi': '10.1016/j.neuron.2011.02.027', 'openalex_id': None, 'pmid': None, 'citation_string': "Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P., & Dolan, R. J. (2011). Model-based influences on humans' choices and striatal prediction errors. *Neuron*, 69(6), 1204–1215.", 'url': 'https://doi.org/10.1016/j.neuron.2011.02.027', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Dolan, R. J., & Dayan, P.', 'year': 2013, 'title': 'Goals and Habits in the Brain', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '80', 'issue': '2', 'pages': '312-325', 'doi': '10.1016/j.neuron.2013.09.007', 'openalex_id': None, 'pmid': None, 'citation_string': 'Dolan, R. J., & Dayan, P. (2013). Goals and habits in the brain. *Neuron*, 80(2), 312–325.', 'url': 'https://doi.org/10.1016/j.neuron.2013.09.007', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': "Gläscher, J., Daw, N., Dayan, P., & O'Doherty, J. P.", 'year': 2010, 'title': 'States versus Rewards: Dissociable Neural Prediction Error Signals Underlying Model-Based and Model-Free Reinforcement Learning', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '66', 'issue': '4', 'pages': '585-595', 'doi': '10.1016/j.neuron.2010.04.016', 'openalex_id': None, 'pmid': None, 'citation_string': "Glascher, J., Daw, N., Dayan, P., & O'Doherty, J. P. (2010). States versus rewards: Dissociable neural prediction error signals underlying model-based and model-free reinforcement learning. *Neuron*, 66(4), 585–595.", 'url': 'https://doi.org/10.1016/j.neuron.2010.04.016', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'Kool, W., Cushman, F. A., & Gershman, S. J.', 'year': 2016, 'title': 'When Does Model-Based Control Pay Off?', 'venue': 'PLOS Computational Biology', 'venue_type': 'journal', 'journal': 'PLOS Computational Biology', 'volume': '12', 'issue': '8', 'pages': 'e1005090', 'doi': '10.1371/journal.pcbi.1005090', 'openalex_id': None, 'pmid': None, 'citation_string': 'Kool, W., Cushman, F. A., & Gershman, S. J. (2016). When does model-based control pay off? *PLoS Computational Biology*, 12(8), e1005090.', 'url': 'https://doi.org/10.1371/journal.pcbi.1005090', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Gillan, C. M., Kosinski, M., Whelan, R., Phelps, E. A., & Daw, N. D.', 'year': 2016, 'title': 'Characterizing a psychiatric symptom dimension related to deficits in goal-directed control', 'venue': 'eLife', 'venue_type': 'journal', 'journal': 'eLife', 'volume': '5', 'issue': None, 'pages': None, 'doi': '10.7554/elife.11305', 'openalex_id': None, 'pmid': None, 'citation_string': 'Gillan, C. M., Kosinski, M., Whelan, R., Phelps, E. A., & Daw, N. D. (2016). Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. *eLife*, 5, e11305.', 'url': 'https://doi.org/10.7554/elife.11305', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Feher da Silva, C., & Hare, T. A.', 'year': 2020, 'title': 'Humans primarily use model-based inference in the two-stage task', 'venue': 'Nature Human Behaviour', 'venue_type': 'journal', 'journal': 'Nature Human Behaviour', 'volume': '4', 'issue': '10', 'pages': '1053-1066', 'doi': '10.1038/s41562-020-0905-y', 'openalex_id': None, 'pmid': None, 'citation_string': 'da Silva, C. F., & Hare, T. A. (2020). Humans primarily use model-based inference in the two-stage task. *Nature Human Behaviour*, 4, 1053–1066.', 'url': 'https://doi.org/10.1038/s41562-020-0905-y', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Feher da Silva, C., & Hare, T. A.', 'year': 2018, 'title': 'A note on the analysis of two-stage task results: How changes in task structure affect what model-free and model-based strategies predict about the effects of reward and transition on the stay probability', 'venue': 'PLOS ONE', 'venue_type': 'journal', 'journal': 'PLOS ONE', 'volume': '13', 'issue': '4', 'pages': 'e0195328', 'doi': '10.1371/journal.pone.0195328', 'openalex_id': None, 'pmid': None, 'citation_string': 'Feher da Silva, C., & Hare, T. A. (2018). A note on the analysis of two-stage task results: How changes in task structure affect what model-free and model-based strategies predict about the effects of reward and transition on the stay probability. *PLoS ONE*, 13(4), e0195328.', 'url': 'https://doi.org/10.1371/journal.pone.0195328', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [2-stage decision task](https://www.cognitiveatlas.org/task/id/trm_5667451917a34)
