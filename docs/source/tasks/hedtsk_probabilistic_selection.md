(hedtsk_probabilistic_selection)=
# Probabilistic Selection Task

**HED task ID:** `hedtsk_probabilistic_selection`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** PST, Probabilistic Stimulus Selection Task, PSS, Frank Task, Probabilistic Selection

Learn to choose between stimulus pairs through probabilistic feedback, then select among novel recombinations; choose-A vs. avoid-B accuracy dissociates positive and negative reinforcement learning.

## Description

The Probabilistic Selection Task, developed by Frank and colleagues, assesses the separable contributions of positive and negative reinforcement learning, linked to striatal Go and NoGo pathway function respectively. During training, participants learn to choose between pairs of stimuli (AB, CD, EF) where each stimulus has a fixed probability of reward (e.g., A=80%, B=20%). At test, stimuli are recombined into novel pairs (e.g., A vs. C, B vs. D). Choosing A in novel contexts indexes Go learning (approach from positive feedback), while avoiding B indexes NoGo learning (avoidance from negative feedback). The task was specifically designed to probe basal ganglia dopaminergic mechanisms and is sensitive to dopaminergic medication effects in Parkinson's disease.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants learn to choose between stimulus pairs through probabilistic feedback (80/20 or 70/30 contingencies), then are tested on novel recombinations without feedback to dissociate Go learning (choose A) from NoGo learning (avoid B).
* - **Manipulation**
  - Feedback probability; number of training pairs; transfer test composition; dopaminergic manipulation (medication status in Parkinson's).
* - **Measurement**
  - Training accuracy; transfer test accuracy (choose-A vs. avoid-B dissociation); fit to actor-critic or opponent-actor learning models.
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
* - Standard PST (3 Stimulus Pairs)

    `hedvar_probabilistic_selection__standard_pst_3_stimulus_pairs`
  - AB (80/20), CD (70/30), EF (60/40); training then transfer test.
  - Canonical Frank et al. learn-then-test with choose/avoid pairs
* - Extended Training Versions

    `hedvar_probabilistic_selection__extended_training_versions`
  - More training trials to ensure asymptotic learning before test.
  - More training trials; tests asymptotic learning
* - 4-Pair Version

    `hedvar_probabilistic_selection__4_pair_version`
  - Additional stimulus pairs for more reliable individual-difference estimates.
  - Additional stimulus pairs; larger choice set
* - Gain-Only and Loss-Only Variants

    `hedvar_probabilistic_selection__gain_only_and_loss_only_variants`
  - Separating reward and punishment learning into distinct phases.
  - Separate gain vs. loss feedback conditions; isolates approach vs. avoidance learning
* - PST with Volatility

    `hedvar_probabilistic_selection__pst_with_volatility`
  - Changing reward contingencies to measure adaptation.
  - Contingencies shift over time; tests learning in non-stationary environment
```

## Cognitive processes

This task is designed to engage the following processes:

- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation)
- [Value learning](../processes/associative_learning_and_reinforcement.md#hed-value-learning)

## Key references

- Frank, M. J., Seeberger, L. C., & O'Reilly, R. C. (2004). By carrot or by stick: Cognitive reinforcement learning in parkinsonism. *Science*, 306(5703), 1940–1943. ([DOI](https://doi.org/10.1126/science.1102941), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15528409/))
- Frank, M. J., Moustafa, A. A., Haughey, H. M., Curran, T., & Hutchison, K. E. (2007). Genetic triple dissociation reveals multiple roles for dopamine in reinforcement learning. *Proceedings of the National Academy of Sciences*, 104(41), 16311–16316. ([DOI](https://doi.org/10.1073/pnas.0706111104), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17913879/))
- Frank, M. J. (2005). Dynamic dopamine modulation in the basal ganglia: A neurocomputational account of cognitive deficits in medicated and nonmedicated parkinsonism. *Journal of Cognitive Neuroscience*, 17(1), 51–72. ([DOI](https://doi.org/10.1162/0898929052880093), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15701239/))

## Further references

- Waltz, J. A., Frank, M. J., Robinson, B. M., & Gold, J. M. (2007). Selective reinforcement learning deficits in schizophrenia support predictions from computational models of striatal-cortical dysfunction. *Biological Psychiatry*, 62(7), 756–764. ([DOI](https://doi.org/10.1016/j.biopsych.2006.09.042), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17300757/))
- Cavanagh, J. F., Frank, M. J., Klein, T. J., & Allen, J. J. B. (2010). Frontal theta links prediction errors to behavioral adaptation in reinforcement learning. *NeuroImage*, 49(4), 3198–3209. ([DOI](https://doi.org/10.1016/j.neuroimage.2009.11.080), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19969093/))
- Doll, B. B., Jacobs, W. J., Sanfey, A. G., & Frank, M. J. (2009). Instructional control of reinforcement learning: A behavioral and neurocomputational investigation. *Brain Research*, 1299, 74–94. ([DOI](https://doi.org/10.1016/j.brainres.2009.07.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19595993/))
- Bodi, N., Keri, S., Nagy, H., Moustafa, A., Myers, C. E., Daw, N., ... & Gluck, M. A. (2009). Reward-learning and the novelty-seeking personality: A between- and within-subjects study of the effects of dopamine agonists on young Parkinson's patients. *Brain*, 132(9), 2385–2395. ([DOI](https://doi.org/10.1093/brain/awp094), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19416950/))

## External links

- Cognitive Atlas: [Probabilistic Selection Task](https://www.cognitiveatlas.org/task/id/trm_5667483dcc371)

