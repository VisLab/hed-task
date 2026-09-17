(hedtsk_probabilistic_selection)=

# Probabilistic Selection Task

**HED Task ID:** `hedtsk_probabilistic_selection`

**Also known as:** PST, Probabilistic Stimulus Selection Task, PSS, Frank Task, Probabilistic Selection

Learn to choose between stimulus pairs through probabilistic feedback, then select among novel recombinations; choose-A vs. avoid-B accuracy dissociates positive and negative reinforcement learning.

## Description

The Probabilistic Selection Task, developed by Frank and colleagues, assesses the separable contributions of positive and negative reinforcement learning, linked to striatal Go and NoGo pathway function respectively. During training, participants learn to choose between pairs of stimuli (AB, CD, EF) where each stimulus has a fixed probability of reward (e.g., A=80%, B=20%). At test, stimuli are recombined into novel pairs (e.g., A vs. C, B vs. D). Choosing A in novel contexts indexes Go learning (approach from positive feedback), while avoiding B indexes NoGo learning (avoidance from negative feedback). The task was specifically designed to probe basal ganglia dopaminergic mechanisms and is sensitive to dopaminergic medication effects in Parkinson's disease.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - Participants learn to choose between stimulus pairs through probabilistic feedback (80/20 or 70/30 contingencies), then are tested on novel recombinations without feedback to dissociate Go learning (choose A) from NoGo learning (avoid B).
* - **Manipulation**
  - Feedback probability; number of training pairs; transfer test composition; dopaminergic manipulation (medication status in Parkinson's).
* - **Measurement**
  - Training accuracy; transfer test accuracy (choose-A vs. avoid-B dissociation); fit to actor-critic or opponent-actor learning models.
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
* - Standard PST (3 Stimulus Pairs)
  - AB (80/20), CD (70/30), EF (60/40); training then transfer test.
  - Canonical Frank et al. learn-then-test with choose/avoid pairs
* - Extended Training Versions
  - More training trials to ensure asymptotic learning before test.
  - More training trials; tests asymptotic learning
* - 4-Pair Version
  - Additional stimulus pairs for more reliable individual-difference estimates.
  - Additional stimulus pairs; larger choice set
* - Gain-Only and Loss-Only Variants
  - Separating reward and punishment learning into distinct phases.
  - Separate gain vs. loss feedback conditions; isolates approach vs. avoidance learning
* - PST with Volatility
  - Changing reward contingencies to measure adaptation.
  - Contingencies shift over time; tests learning in non-stationary environment
```

## Cognitive processes

This task engages the following cognitive processes:

- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation)
- [Value learning](../processes/associative_learning_and_reinforcement.md#hed-value-learning)

## Key references

- {'authors': "Frank, M. J., Seeberger, L. C., & O'Reilly, R. C.", 'year': 2004, 'title': 'By Carrot or by Stick: Cognitive Reinforcement Learning in Parkinsonism', 'venue': 'Science', 'venue_type': 'journal', 'journal': 'Science', 'volume': '306', 'issue': '5703', 'pages': '1940-1943', 'doi': '10.1126/science.1102941', 'openalex_id': None, 'pmid': None, 'citation_string': "Frank, M. J., Seeberger, L. C., & O'Reilly, R. C. (2004). By carrot or by stick: Cognitive reinforcement learning in parkinsonism. *Science*, 306(5703), 1940–1943.", 'url': 'https://doi.org/10.1126/science.1102941', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Frank, M. J., Moustafa, A. A., Haughey, H. M., Curran, T., & Hutchison, K. E.', 'year': 2007, 'title': 'Genetic triple dissociation reveals multiple roles for dopamine in reinforcement learning', 'venue': 'Proceedings of the National Academy of Sciences', 'venue_type': 'journal', 'journal': 'Proceedings of the National Academy of Sciences', 'volume': '104', 'issue': '41', 'pages': '16311-16316', 'doi': '10.1073/pnas.0706111104', 'openalex_id': None, 'pmid': None, 'citation_string': 'Frank, M. J., Moustafa, A. A., Haughey, H. M., Curran, T., & Hutchison, K. E. (2007). Genetic triple dissociation reveals multiple roles for dopamine in reinforcement learning. *Proceedings of the National Academy of Sciences*, 104(41), 16311–16316.', 'url': 'https://doi.org/10.1073/pnas.0706111104', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Frank, M. J.', 'year': 2005, 'title': 'Dynamic Dopamine Modulation in the Basal Ganglia: A Neurocomputational Account of Cognitive Deficits in Medicated and Nonmedicated Parkinsonism', 'venue': 'Journal of Cognitive Neuroscience', 'venue_type': 'journal', 'journal': 'Journal of Cognitive Neuroscience', 'volume': '17', 'issue': '1', 'pages': '51-72', 'doi': '10.1162/0898929052880093', 'openalex_id': None, 'pmid': None, 'citation_string': 'Frank, M. J. (2005). Dynamic dopamine modulation in the basal ganglia: A neurocomputational account of cognitive deficits in medicated and nonmedicated parkinsonism. *Journal of Cognitive Neuroscience*, 17(1), 51–72.', 'url': 'https://doi.org/10.1162/0898929052880093', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'Waltz, J. A., Frank, M. J., Robinson, B. M., & Gold, J. M.', 'year': 2007, 'title': 'Selective Reinforcement Learning Deficits in Schizophrenia Support Predictions from Computational Models of Striatal-Cortical Dysfunction', 'venue': 'Biological Psychiatry', 'venue_type': 'journal', 'journal': 'Biological Psychiatry', 'volume': '62', 'issue': '7', 'pages': '756-764', 'doi': '10.1016/j.biopsych.2006.09.042', 'openalex_id': None, 'pmid': None, 'citation_string': 'Waltz, J. A., Frank, M. J., Robinson, B. M., & Gold, J. M. (2007). Selective reinforcement learning deficits in schizophrenia support predictions from computational models of striatal-cortical dysfunction. *Biological Psychiatry*, 62(7), 756–764.', 'url': 'https://doi.org/10.1016/j.biopsych.2006.09.042', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Cavanagh, J. F., Frank, M. J., Klein, T. J., & Allen, J. J.', 'year': 2010, 'title': 'Frontal theta links prediction errors to behavioral adaptation in reinforcement learning', 'venue': 'NeuroImage', 'venue_type': 'journal', 'journal': 'NeuroImage', 'volume': '49', 'issue': '4', 'pages': '3198-3209', 'doi': '10.1016/j.neuroimage.2009.11.080', 'openalex_id': None, 'pmid': None, 'citation_string': 'Cavanagh, J. F., Frank, M. J., Klein, T. J., & Allen, J. J. B. (2010). Frontal theta links prediction errors to behavioral adaptation in reinforcement learning. *NeuroImage*, 49(4), 3198–3209.', 'url': 'https://doi.org/10.1016/j.neuroimage.2009.11.080', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Doll, B. B., Jacobs, W. J., Sanfey, A. G., & Frank, M. J.', 'year': 2009, 'title': 'Instructional control of reinforcement learning: A behavioral and neurocomputational investigation', 'venue': 'Brain Research', 'venue_type': 'journal', 'journal': 'Brain Research', 'volume': '1299', 'issue': None, 'pages': '74-94', 'doi': '10.1016/j.brainres.2009.07.007', 'openalex_id': None, 'pmid': None, 'citation_string': 'Doll, B. B., Jacobs, W. J., Sanfey, A. G., & Frank, M. J. (2009). Instructional control of reinforcement learning: A behavioral and neurocomputational investigation. *Brain Research*, 1299, 74–94.', 'url': 'https://doi.org/10.1016/j.brainres.2009.07.007', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Bodi, N., Keri, S., Nagy, H., Moustafa, A., Myers, C. E., Daw, N., Dibo, G., Takats, A., Bereczki, D., & Gluck, M. A.', 'year': 2009, 'title': "Reward-learning and the novelty-seeking personality: a between- and within-subjects study of the effects of dopamine agonists on young Parkinson's patients", 'venue': 'Brain', 'venue_type': 'journal', 'journal': 'Brain', 'volume': '132', 'issue': '9', 'pages': '2385-2395', 'doi': '10.1093/brain/awp094', 'openalex_id': None, 'pmid': None, 'citation_string': "Bodi, N., Keri, S., Nagy, H., Moustafa, A., Myers, C. E., Daw, N., ... & Gluck, M. A. (2009). Reward-learning and the novelty-seeking personality: A between- and within-subjects study of the effects of dopamine agonists on young Parkinson's patients. *Brain*, 132(9), 2385–2395.", 'url': 'https://doi.org/10.1093/brain/awp094', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [Probabilistic Selection Task](https://www.cognitiveatlas.org/task/id/trm_5667483dcc371)
