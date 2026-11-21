(hedtsk_reversal_learning)=
# Reversal Learning Task

**HED task ID:** `hedtsk_reversal_learning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** PRL, Probabilistic Reversal Learning

After initial stimulus-reward learning, the contingencies switch; perseveration and reversal speed index behavioral flexibility.

## Description

Participants learn a stimulus-outcome association (e.g., stimulus A is rewarded, B is not), then contingencies are reversed. Participants must flexibly adapt their behavior to the new associations. Performance measures include trials to criterion and perseverative errors (continued selection of the previously rewarded stimulus). The task can use deterministic or probabilistic contingencies. Neuroimaging consistently implicates the orbitofrontal cortex and ventrolateral prefrontal cortex in reversal learning, particularly for updating stimulus-outcome associations based on feedback. Some forms take points away for a wrong choice rather than merely withholding a win.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-payoff">Choose for a payoff</a> (`choose_for_payoff`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What are the options?* <a href="vocabulary.html#rule-choose-for-payoff-option-set-stimulus-pairs">stimulus pairs</a>
  - *What is traded against what?* <a href="vocabulary.html#rule-choose-for-payoff-tradeoff-probability-learning">probability learning</a>
  - *Does what pays change?* <a href="vocabulary.html#rule-choose-for-payoff-contingency-stability-reversal">reversal</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-goal">reward goal</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-gain">gain</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-choice">choice</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-points">points</a>, <a href="vocabulary.html#motivator-what-money">money</a>, <a href="vocabulary.html#motivator-what-signal-only">signal only</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-feedback-reliability">feedback reliability</a>, <a href="vocabulary.html#setting-stimulus-similarity">stimulus similarity</a>
- **Material:** Two stimuli, one rewarded and one not, whose assignment reverses once the participant reaches criterion.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants learn to choose the rewarded stimulus over an unrewarded one.
    2. After reaching criterion, contingencies reverse - the previously correct stimulus becomes incorrect and vice versa.
* - **Manipulations**
  - - Number of reversals
    - Deterministic vs. probabilistic feedback
    - Stimulus discriminability
    - Serial vs. spatial reversals
    - Feedback type (reward vs. punishment reversal)
* - **Measurements**
  - - Errors to criterion on initial discrimination and on reversals
    - Perseverative errors (continuing to choose previously correct stimulus)
    - Reversal cost
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
* - Multi-Dimensional Reversal

    `hedvar_reversal_learning__multi_dimensional_reversal`
  - named form
  - -
  - Stimuli differ on several features of which only one predicts reward, and a reversal can switch the rewarded value within that feature or move to a different feature altogether.
* - Reward vs. Punishment Reversal

    `hedvar_reversal_learning__reward_vs_punishment_reversal`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>; sign: <a href="vocabulary.html#motivator-sign-both">both</a>
  - -
  - Feedback is win-versus-no-win in some blocks and lose-versus-no-lose in others.
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

- Izquierdo, A., Brigman, J. L., Bhatt, D. K., et al. (2017). The neural basis of reversal learning: An updated perspective. *Neuroscience*, 345, 12-26. ([DOI](https://doi.org/10.1016/j.neuroscience.2016.03.021), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26979052/))
- den Ouden, H. E. M., Daw, N. D., Fernandez, G., et al. (2013). Dissociable effects of dopamine and serotonin on reversal learning. *Neuron*, 80(4), 1090-1100. ([DOI](https://doi.org/10.1016/j.neuron.2013.08.030), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24267657/))
- Schlagenhauf, F., Huys, Q. J. M., Deserno, L., Rapp, M. A., Beck, A., Heinze, H. J., Dolan, R., & Heinz, A. (2014). Striatal dysfunction during reversal learning in unmedicated schizophrenia patients. *NeuroImage*, 89, 171-180. ([DOI](https://doi.org/10.1016/j.neuroimage.2013.11.034), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24291614/))
- Costa, V. D., Tran, V. L., Turchi, J., & Averbeck, B. B. (2015). Reversal learning and dopamine: A Bayesian perspective. *Journal of Neuroscience*, 35(6), 2407-2416. ([DOI](https://doi.org/10.1523/jneurosci.1989-14.2015), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25673835/))

## External links

- Cognitive Atlas: [reversal learning task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949d4e)

