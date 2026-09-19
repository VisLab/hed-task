(hedtsk_reversal_learning)=
# Reversal Learning Task

**HED task ID:** `hedtsk_reversal_learning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** PRL, Probabilistic Reversal Learning

After initial stimulus-reward learning, the contingencies switch; perseveration and reversal speed index behavioral flexibility.

## Description

Participants learn a stimulus-outcome association (e.g., stimulus A is rewarded, B is not), then contingencies are reversed. Participants must flexibly adapt their behavior to the new associations. Performance measures include trials to criterion and perseverative errors (continued selection of the previously rewarded stimulus). The task can use deterministic or probabilistic contingencies. Neuroimaging consistently implicates the orbitofrontal cortex and ventrolateral prefrontal cortex in reversal learning, particularly for updating stimulus-outcome associations based on feedback.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants learn to choose the rewarded stimulus over an unrewarded one. After reaching criterion, contingencies reverse — the previously correct stimulus becomes incorrect and vice versa.
* - **Manipulation**
  - Number of reversals; deterministic vs. probabilistic feedback; stimulus discriminability; serial vs. spatial reversals.
* - **Measurement**
  - Errors to criterion on initial discrimination and on reversals; perseverative errors (continuing to choose previously correct stimulus); reversal cost.
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
* - Deterministic Reversal

    `hedvar_reversal_learning__deterministic_reversal`
  - 100% contingencies; clear-cut reward/punishment signals.
  - Contingency fully reverses; canonical reversal learning
* - Probabilistic Reversal

    `hedvar_reversal_learning__probabilistic_reversal`
  - 80/20 or 70/30 contingencies; requires integration over multiple trials.
  - Stochastic contingency reversal; different uncertainty structure
* - Serial Reversal

    `hedvar_reversal_learning__serial_reversal`
  - Multiple reversals within session; learning-to-learn effects.
  - Multiple reversals in sequence; tests reversal learning rate
* - Stimulus-Outcome vs. Action-Outcome Reversal

    `hedvar_reversal_learning__stimulus_outcome_vs_action_outcome_reversal`
  - Reversal of what (stimulus) vs. where (response location).
  - Reversal of stimulus or action contingency; different associative structure
* - Multi-Dimensional Reversal

    `hedvar_reversal_learning__multi_dimensional_reversal`
  - Stimuli vary on multiple dimensions; only one dimension relevant for reversal.
  - Reversal involves change in relevant stimulus dimension; more complex
* - Reward vs. Punishment Reversal

    `hedvar_reversal_learning__reward_vs_punishment_reversal`
  - Asymmetric effects of positive vs. negative feedback on reversal.
  - Valence manipulation changes learning signal
```

## Cognitive processes

This task is designed to engage the following processes:

- [Reversal learning](../processes/associative_learning_and_reinforcement.md#hed-reversal-learning)
- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)

## Key references

- Dias, R., Robbins, T. W., & Roberts, A. C. (1996). Dissociation in prefrontal cortex of affective and attentional shifts. *Nature*, 380(6569), 69-72. ([DOI](https://doi.org/10.1038/380069a0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8598908/))
- Cools, R., Clark, L., Owen, A. M., & Robbins, T. W. (2002). Defining the neural mechanisms of probabilistic reversal learning using event-related functional magnetic resonance imaging. *Journal of Neuroscience*, 22(11), 4563-4567. ([DOI](https://doi.org/10.1523/jneurosci.22-11-04563.2002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12040063/))

## Further references

- Izquierdo, A., Brigman, J. L., Bhatt, D. K., et al. (2017). The neural basis of reversal learning: An updated perspective. *Neuroscience*, 345, 12–26. ([DOI](https://doi.org/10.1016/j.neuroscience.2016.03.021), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26979052/))
- den Ouden, H. E. M., Daw, N. D., Fernandez, G., et al. (2013). Dissociable effects of dopamine and serotonin on reversal learning. *Neuron*, 80(4), 1090–1100. ([DOI](https://doi.org/10.1016/j.neuron.2013.08.030), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24267657/))
- Schlagenhauf, F., Huys, Q. J. M., Deserno, L., Rapp, M. A., Beck, A., Heinze, H. J., Dolan, R., & Heinz, A. (2014). Striatal dysfunction during reversal learning in unmedicated schizophrenia patients. *NeuroImage*, 89, 171–180. ([DOI](https://doi.org/10.1016/j.neuroimage.2013.11.034), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24291614/))
- Costa, V. D., Tran, V. L., Turchi, J., & Averbeck, B. B. (2015). Reversal learning and dopamine: A Bayesian perspective. *Journal of Neuroscience*, 35(6), 2407–2416. ([DOI](https://doi.org/10.1523/jneurosci.1989-14.2015), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25673835/))

## External links

- Cognitive Atlas: [reversal learning task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949d4e)

