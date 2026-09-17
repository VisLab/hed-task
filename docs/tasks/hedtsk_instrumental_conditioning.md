(hedtsk_instrumental_conditioning)=

# Instrumental Conditioning Task

**HED Task ID:** `hedtsk_instrumental_conditioning`

**Also known as:** Operant Conditioning, Instrumental Learning, PIT

Actions are reinforced by contingent outcomes under defined schedules; response rate and choice probability across schedules index instrumental learning. Specific human instantiations include lever/button-press reward paradigms and free-operant tasks.

## Description

In instrumental conditioning, voluntary actions are associated with rewarding or punishing consequences through repeated experience. Laboratory implementations present discrete choice options where specific responses are followed by desirable outcomes (food, money, points) or undesirable outcomes (loss, punishment). Common schedules include fixed-ratio, variable-ratio, fixed-interval, and variable-interval. Performance measures include response rates, choice patterns, and reaction times. The ventral striatum, dopamine system, and orbitofrontal cortex are critical for representing value predictions and learning from outcomes.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - Participants perform actions (button presses, lever responses) that produce contingent outcomes (rewards or punishments) according to defined reinforcement schedules.
* - **Manipulation**
  - Reinforcement schedule (fixed ratio, variable ratio, fixed interval, variable interval); outcome valence; contingency degradation; Pavlovian-instrumental transfer.
* - **Measurement**
  - Response rate; choice probability; sensitivity to contingency and outcome devaluation; transfer effects between Pavlovian cues and instrumental actions.
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
* - Fixed Ratio (FR)
  - Reinforcement after fixed number of responses.
  - Reward after fixed number of responses; canonical ratio schedule
* - Variable Ratio (VR)
  - Reinforcement after variable number of responses (average specified).
  - Reward after variable number of responses; different reinforcement statistics
* - Fixed Interval (FI)
  - Reinforcement for first response after fixed time period.
  - First response after fixed time rewarded; different temporal reinforcement structure
* - Variable Interval (VI)
  - Reinforcement for first response after variable time period.
  - Variable time intervals; different temporal unpredictability
* - Progressive Ratio
  - Ratio requirement increases progressively; breakpoint indexes motivation.
  - Ratio requirement escalates; measures motivational breakpoint
* - Concurrent Choice
  - Multiple response options with different reinforcement schedules; matching law studies.
  - Two simultaneously available schedules; choice behavior reveals preference
* - Two-Stage Decision Task (Daw)
  - Sequential choice task dissociating model-based (goal-directed) from model-free (habitual) learning.
  - Two-step Markov decision; measures model-based vs. model-free learning
* - Devaluation Paradigm
  - Reward value changed after learning; goal-directed behavior adjusts, habitual does not.
  - Outcome devaluation tests goal-directed vs. habitual control; different post-training procedure
* - Contingency Degradation
  - Weakening action-outcome relationship; tests sensitivity to causal structure.
  - Action-outcome contingency degraded; tests action sensitivity
* - Outcome-Specific Pavlovian-Instrumental Transfer (PIT)
  - Pavlovian cues bias instrumental responding.
  - Pavlovian CS influences instrumental responding; different multi-phase design
* - Avoidance Learning
  - Responses prevent aversive outcomes; safety signal learning.
  - Response prevents aversive outcome; different valence and contingency structure
```

## Cognitive processes

This task engages the following cognitive processes:

- [Instrumental conditioning](../processes/associative_learning_and_reinforcement.md#hed-instrumental-conditioning)
- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Goal-directed behavior](../processes/associative_learning_and_reinforcement.md#hed-goal-directed-behavior)
- [Habit](../processes/associative_learning_and_reinforcement.md#hed-habit)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)

## Key references

- {'authors': 'Schultz, W., Dayan, P., & Montague, P. R.', 'year': 1997, 'title': 'A Neural Substrate of Prediction and Reward', 'venue': 'Science', 'venue_type': 'journal', 'journal': 'Science', 'volume': '275', 'issue': '5306', 'pages': '1593-1599', 'doi': '10.1126/science.275.5306.1593', 'openalex_id': None, 'pmid': None, 'citation_string': 'Schultz, W., Dayan, P., & Montague, P. R. (1997). A neural substrate of prediction and reward. *Science*, 275(5306), 1593-1599.', 'url': 'https://doi.org/10.1126/science.275.5306.1593', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Haber, S. N., & Knutson, B.', 'year': 2010, 'title': 'The reward circuit: Linking primate anatomy and human imaging', 'venue': 'Neuropsychopharmacology', 'venue_type': 'journal', 'journal': 'Neuropsychopharmacology', 'volume': '35', 'issue': '1', 'pages': '4-26', 'doi': None, 'openalex_id': None, 'pmid': None, 'citation_string': 'Haber, S. N., & Knutson, B. (2010). The reward circuit: Linking primate anatomy and human imaging. *Neuropsychopharmacology*, 35(1), 4-26.', 'url': None, 'source': 'unresolved', 'confidence': 'none', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': "Balleine, B. W., & O'Doherty, J. P.", 'year': 2010, 'title': 'Human and rodent homologies in action control: Corticostriatal determinants of goal-directed and habitual action', 'venue': 'Neuropsychopharmacology', 'venue_type': 'journal', 'journal': 'Neuropsychopharmacology', 'volume': '35', 'issue': '1', 'pages': '48–69', 'doi': None, 'openalex_id': None, 'pmid': None, 'citation_string': "Balleine, B. W., & O'Doherty, J. P. (2010). Human and rodent homologies in action control: Corticostriatal determinants of goal-directed and habitual action. *Neuropsychopharmacology*, 35(1), 48–69.", 'url': None, 'source': 'unresolved', 'confidence': 'none', 'verified_on': '2026-04-20'}
- {'authors': 'Dolan, R. J., & Dayan, P.', 'year': 2013, 'title': 'Goals and Habits in the Brain', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '80', 'issue': '2', 'pages': '312-325', 'doi': '10.1016/j.neuron.2013.09.007', 'openalex_id': None, 'pmid': None, 'citation_string': 'Dolan, R. J., & Dayan, P. (2013). Goals and habits in the brain. *Neuron*, 80(2), 312–325.', 'url': 'https://doi.org/10.1016/j.neuron.2013.09.007', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Lee, S. W., Shimojo, S., & O’Doherty, J. P.', 'year': 2014, 'title': 'Neural Computations Underlying Arbitration between Model-Based and Model-free Learning', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '81', 'issue': '3', 'pages': '687-699', 'doi': '10.1016/j.neuron.2013.11.028', 'openalex_id': None, 'pmid': None, 'citation_string': "Lee, S. W., Shimojo, S., & O'Doherty, J. P. (2014). Neural computations underlying arbitration between model-based and model-free learning. *Neuron*, 81(3), 687–699.", 'url': 'https://doi.org/10.1016/j.neuron.2013.11.028', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Gillan, C. M., Kosinski, M., Whelan, R., Phelps, E. A., & Daw, N. D.', 'year': 2016, 'title': 'Characterizing a psychiatric symptom dimension related to deficits in goal-directed control', 'venue': 'eLife', 'venue_type': 'journal', 'journal': 'eLife', 'volume': '5', 'issue': None, 'pages': None, 'doi': '10.7554/elife.11305', 'openalex_id': None, 'pmid': None, 'citation_string': 'Gillan, C. M., Kosinski, M., Whelan, R., Phelps, E. A., & Daw, N. D. (2016). Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. *eLife*, 5, e11305.', 'url': 'https://doi.org/10.7554/elife.11305', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [instrumental learning task](https://www.cognitiveatlas.org/task/id/trm_4f2414059baa8)
