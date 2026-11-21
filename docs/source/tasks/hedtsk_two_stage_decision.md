(hedtsk_two_stage_decision)=
# Two-Stage Decision Task

**HED task ID:** `hedtsk_two_stage_decision`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Two-Step Task, Daw Task, MB/MF Task

Sequential two-choice task with probabilistic transitions to second-stage states and drifting rewards; choice patterns dissociate model-based from model-free control.

## Description

Participants make two sequential choices per trial. The first-stage choice leads (with fixed transition probabilities - 70% common, 30% rare) to one of two second-stage states, each containing its own pair of options. Second-stage options yield rewards with slowly drifting probabilities. Daw et al. (2011) designed this task to dissociate model-based reinforcement learning (using knowledge of the transition structure to plan) from model-free reinforcement learning (repeating previously rewarded actions regardless of transition type). The diagnostic signature is the interaction between reward and transition type on subsequent first-stage choices: model-based agents show opposite stay/switch patterns after common vs. rare transitions, while model-free agents show the same pattern regardless of transition type.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-outcomes">Choose for a payoff</a> (`choose_for_outcomes`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is traded against what?* <a href="vocabulary.html#rule-choose-for-outcomes-tradeoff-explore-vs-exploit">explore vs exploit</a>
  - *Does what pays change?* <a href="vocabulary.html#rule-choose-for-outcomes-contingency-stability-drifting">drifting</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-goal">reward goal</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-gain">gain</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-choice">choice</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-money">money</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>
- **Material:** A pair of first-stage options leading by common (70%) or rare (30%) transitions to one of two second-stage pairs whose reward probabilities drift slowly.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. First stage: choose between two options that lead probabilistically (70/30) to one of two second-stage choice sets.
    2. Second stage: choose between two options with drifting reward probabilities.
    3. This separates model-based from model-free learning.
    4. Optional: After learning, the reward in one second-stage state is declared worthless and first-stage choice is retested.
* - **Manipulations**
  - - Transition structure (common vs. rare)
    - Reward probability drift rate
    - Reward magnitude
    - Simplified version (fewer trials or options, cover story)
* - **Measurements**
  - - Stay probability as a function of previous trial outcome x transition type
    - Model-based index
    - Computational model fits (hybrid MB/MF learning rates, mixing weight)
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
* - Shortened/Simplified Versions

    `hedvar_two_stage_decision__shortened_simplified_versions`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>; population: <a href="vocabulary.html#facet-population-children">children</a>, <a href="vocabulary.html#facet-population-patients">patients</a>
  - -
  - Fewer trials, fewer options or a cover story (spaceships and planets) for children or patients; trial count is not a listed manipulation of this task.
* - Devaluation Manipulation

    `hedvar_two_stage_decision__devaluation_manipulation`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-devaluation">devaluation</a>, <a href="vocabulary.html#phase-test">test</a>
  - [Goal-directed behavior](../processes/associative_learning_and_reinforcement.md#hed-goal-directed-behavior)
  - After learning, the reward in one second-stage state is declared worthless and the first-stage choice is tested again.
* - Two-Stage with Instructed Knowledge

    `hedvar_two_stage_decision__two_stage_with_instructed_knowledge`
  - named form
  - -
  - The transition probabilities are taught before the task, while the second-stage reward probabilities are still learned by experience.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Model-based learning](../processes/associative_learning_and_reinforcement.md#hed-model-based-learning)
- [Model-free learning](../processes/associative_learning_and_reinforcement.md#hed-model-free-learning)
- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)

## Key references

- Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P., & Dolan, R. J. (2011). Model-based influences on humans' choices and striatal prediction errors. *Neuron*, 69(6), 1204-1215. ([DOI](https://doi.org/10.1016/j.neuron.2011.02.027), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21435563/))
- Dolan, R. J., & Dayan, P. (2013). Goals and habits in the brain. *Neuron*, 80(2), 312-325. ([DOI](https://doi.org/10.1016/j.neuron.2013.09.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24139036/))
- Glascher, J., Daw, N., Dayan, P., & O'Doherty, J. P. (2010). States versus rewards: Dissociable neural prediction error signals underlying model-based and model-free reinforcement learning. *Neuron*, 66(4), 585-595. ([DOI](https://doi.org/10.1016/j.neuron.2010.04.016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20510862/))

## Further references

- Kool, W., Cushman, F. A., & Gershman, S. J. (2016). When does model-based control pay off? *PLoS Computational Biology*, 12(8), e1005090. ([DOI](https://doi.org/10.1371/journal.pcbi.1005090), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27564094/))
- Gillan, C. M., Kosinski, M., Whelan, R., Phelps, E. A., & Daw, N. D. (2016). Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. *eLife*, 5, e11305. ([DOI](https://doi.org/10.7554/elife.11305), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26928075/))
- da Silva, C. F., & Hare, T. A. (2020). Humans primarily use model-based inference in the two-stage task. *Nature Human Behaviour*, 4, 1053-1066. ([DOI](https://doi.org/10.1038/s41562-020-0905-y), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32632333/))
- Feher da Silva, C., & Hare, T. A. (2018). A note on the analysis of two-stage task results: How changes in task structure affect what model-free and model-based strategies predict about the effects of reward and transition on the stay probability. *PLoS ONE*, 13(4), e0195328. ([DOI](https://doi.org/10.1371/journal.pone.0195328), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29614130/))

## External links

- Cognitive Atlas: [2-stage decision task](https://www.cognitiveatlas.org/task/id/trm_5667451917a34)

