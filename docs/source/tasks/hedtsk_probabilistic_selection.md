(hedtsk_probabilistic_selection)=
# Probabilistic Selection Task

**HED task ID:** `hedtsk_probabilistic_selection`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** PST, Probabilistic Stimulus Selection Task, PSS, Frank Task, Probabilistic Selection

Learn to choose between stimulus pairs through probabilistic feedback, then select among novel recombinations; choose-A vs. avoid-B accuracy dissociates positive and negative reinforcement learning.

## Description

The Probabilistic Selection Task, developed by Frank and colleagues, assesses the separable contributions of positive and negative reinforcement learning, linked to striatal Go and NoGo pathway function respectively. During training, participants learn to choose between pairs of stimuli (AB, CD, EF) where each stimulus has a fixed probability of reward (e.g., A=80%, B=20%). At test, stimuli are recombined into novel pairs (e.g., A vs. C, B vs. D). Choosing A in novel contexts indexes Go learning (approach from positive feedback), while avoiding B indexes NoGo learning (avoidance from negative feedback). The task was specifically designed to probe basal ganglia dopaminergic mechanisms and is sensitive to dopaminergic medication effects in Parkinson's disease.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-outcomes">choose for outcomes</a>
- **What are the options?** <a href="vocabulary.html#rule-choose-for-outcomes-option-set-stimulus-pairs">stimulus pairs</a>
- **What is traded against what?** <a href="vocabulary.html#rule-choose-for-outcomes-tradeoff-probability-learning">probability learning</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-reward-goal">reward goal</a>
- **Can the player gain, lose, or both?** <a href="vocabulary.html#motivation-sign-both">both</a>
- **What earns the outcome?** <a href="vocabulary.html#motivation-earned-by-choice">choice</a>
- **What is the outcome?** <a href="vocabulary.html#motivation-what-signal-only">signal only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Feedback:** <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-feedback-reliability">feedback reliability</a>, <a href="vocabulary.html#setting-number-of-trials">number of trials</a>, <a href="vocabulary.html#setting-set-size">set size</a>
- **Material:** Pairs of stimuli (AB, CD, EF), each stimulus rewarded with a fixed probability such as 80 or 20 percent.
- **Phases:** <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-transfer">transfer</a>

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants learn to choose between stimulus pairs through probabilistic feedback (80/20 or 70/30 contingencies), then are tested on novel recombinations without feedback to dissociate Go learning (choose A) from NoGo learning (avoid B).
* - **Manipulations**
  - - Feedback probability
    - Number of training pairs
    - Transfer test composition
    - Dopaminergic manipulation (medication status in Parkinson's)
    - Amount of training (extended or to criterion)
    - Feedback type (win-only vs. loss-only vs. correct/incorrect)
    - Probability stability (volatile vs. stable)
* - **Measurements**
  - - Training accuracy
    - Transfer test accuracy (choose-A vs. avoid-B dissociation)
    - Fit to actor-critic or opponent-actor learning models
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
* - Gain-Only and Loss-Only Variants

    `hedvar_probabilistic_selection__gain_only_and_loss_only_variants`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>, <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>; what: <a href="vocabulary.html#motivation-what-money">money</a>; real: <a href="vocabulary.html#motivation-real-paid">paid</a>
  - -
  - Feedback is win-or-nothing in some blocks and lose-or-nothing in others instead of "correct" and "incorrect".
* - PST with Volatility

    `hedvar_probabilistic_selection__pst_with_volatility`
  - contingency stability: <a href="vocabulary.html#rule-choose-for-outcomes-contingency-stability-reversal">reversal</a>
  - [Reversal learning](../processes/associative_learning_and_reinforcement.md#hed-reversal-learning)
  - The probabilities attached to the symbols change partway through training.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation)
- [Value learning](../processes/associative_learning_and_reinforcement.md#hed-value-learning)

## Key references

- Frank, M. J., Seeberger, L. C., & O'Reilly, R. C. (2004). By carrot or by stick: Cognitive reinforcement learning in parkinsonism. *Science*, 306(5703), 1940-1943. ([DOI](https://doi.org/10.1126/science.1102941), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15528409/))
- Frank, M. J., Moustafa, A. A., Haughey, H. M., Curran, T., & Hutchison, K. E. (2007). Genetic triple dissociation reveals multiple roles for dopamine in reinforcement learning. *Proceedings of the National Academy of Sciences*, 104(41), 16311-16316. ([DOI](https://doi.org/10.1073/pnas.0706111104), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17913879/))
- Frank, M. J. (2005). Dynamic dopamine modulation in the basal ganglia: A neurocomputational account of cognitive deficits in medicated and nonmedicated parkinsonism. *Journal of Cognitive Neuroscience*, 17(1), 51-72. ([DOI](https://doi.org/10.1162/0898929052880093), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15701239/))

## Further references

- Waltz, J. A., Frank, M. J., Robinson, B. M., & Gold, J. M. (2007). Selective reinforcement learning deficits in schizophrenia support predictions from computational models of striatal-cortical dysfunction. *Biological Psychiatry*, 62(7), 756-764. ([DOI](https://doi.org/10.1016/j.biopsych.2006.09.042), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17300757/))
- Cavanagh, J. F., Frank, M. J., Klein, T. J., & Allen, J. J. B. (2010). Frontal theta links prediction errors to behavioral adaptation in reinforcement learning. *NeuroImage*, 49(4), 3198-3209. ([DOI](https://doi.org/10.1016/j.neuroimage.2009.11.080), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19969093/))
- Doll, B. B., Jacobs, W. J., Sanfey, A. G., & Frank, M. J. (2009). Instructional control of reinforcement learning: A behavioral and neurocomputational investigation. *Brain Research*, 1299, 74-94. ([DOI](https://doi.org/10.1016/j.brainres.2009.07.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19595993/))
- Bodi, N., Keri, S., Nagy, H., Moustafa, A., Myers, C. E., Daw, N., ... & Gluck, M. A. (2009). Reward-learning and the novelty-seeking personality: A between- and within-subjects study of the effects of dopamine agonists on young Parkinson's patients. *Brain*, 132(9), 2385-2395. ([DOI](https://doi.org/10.1093/brain/awp094), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19416950/))

## External links

- Cognitive Atlas: [Probabilistic Selection Task](https://www.cognitiveatlas.org/task/id/trm_5667483dcc371)

