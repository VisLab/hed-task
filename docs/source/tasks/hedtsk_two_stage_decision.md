(hedtsk_two_stage_decision)=
# Two-Stage Decision Task

**HED task ID:** `hedtsk_two_stage_decision`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Two-Step Task, Daw Task, MB/MF Task

Sequential two-choice task with probabilistic transitions to second-stage states and drifting rewards; choice patterns dissociate model-based from model-free control.

## Description

Participants make two sequential choices per trial. The first-stage choice leads (with fixed transition probabilities — 70% common, 30% rare) to one of two second-stage states, each containing its own pair of options. Second-stage options yield rewards with slowly drifting probabilities. Daw et al. (2011) designed this task to dissociate model-based reinforcement learning (using knowledge of the transition structure to plan) from model-free reinforcement learning (repeating previously rewarded actions regardless of transition type). The diagnostic signature is the interaction between reward and transition type on subsequent first-stage choices: model-based agents show opposite stay/switch patterns after common vs. rare transitions, while model-free agents show the same pattern regardless of transition type.

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
* - **Manipulations**
  - - Transition structure (common vs. rare)
    - Reward probability drift rate
    - Reward magnitude
* - **Measurements**
  - - Stay probability as a function of previous trial outcome × transition type
    - Model-based index
    - Computational model fits (hybrid MB/MF learning rates, mixing weight)
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
* - Standard Daw et al. (2011) Version

    `hedvar_two_stage_decision__standard_daw_et_al_2011_version`
  - Two first-stage options, two second-stage states, each with two options; 70/30 transition probabilities.
  - Canonical two-step Markov decision task; measures model-based vs. model-free
* - Shortened/Simplified Versions

    `hedvar_two_stage_decision__shortened_simplified_versions`
  - Fewer trials or simplified transition structure for clinical or developmental populations.
  - Fewer trials or simplified state structure; recognized efficient version
* - Enhanced Model-Based Version

    `hedvar_two_stage_decision__enhanced_model_based_version`
  - More complex transition structures (three or more stages) to increase model-based demands.
  - Design features that enhance model-based learning; different incentive structure
* - Devaluation Manipulation

    `hedvar_two_stage_decision__devaluation_manipulation`
  - Changing reward magnitudes mid-task to test sensitivity to outcome value (model-based predicts rapid adjustment).
  - Reward devalued after training; tests habitual vs. goal-directed control
* - Two-Stage with Instructed Knowledge

    `hedvar_two_stage_decision__two_stage_with_instructed_knowledge`
  - Explicitly teaching the transition structure before the task; tests whether model-based behavior increases with explicit knowledge.
  - Transition structure explicitly taught; tests instructed vs. learned model
```

## Cognitive processes

This task is designed to engage the following processes:

- [Model-based learning](../processes/associative_learning_and_reinforcement.md#hed-model-based-learning)
- [Model-free learning](../processes/associative_learning_and_reinforcement.md#hed-model-free-learning)
- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)

## Key references

- Daw, N. D., Gershman, S. J., Seymour, B., Dayan, P., & Dolan, R. J. (2011). Model-based influences on humans' choices and striatal prediction errors. *Neuron*, 69(6), 1204–1215. ([DOI](https://doi.org/10.1016/j.neuron.2011.02.027), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21435563/))
- Dolan, R. J., & Dayan, P. (2013). Goals and habits in the brain. *Neuron*, 80(2), 312–325. ([DOI](https://doi.org/10.1016/j.neuron.2013.09.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24139036/))
- Glascher, J., Daw, N., Dayan, P., & O'Doherty, J. P. (2010). States versus rewards: Dissociable neural prediction error signals underlying model-based and model-free reinforcement learning. *Neuron*, 66(4), 585–595. ([DOI](https://doi.org/10.1016/j.neuron.2010.04.016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20510862/))

## Further references

- Kool, W., Cushman, F. A., & Gershman, S. J. (2016). When does model-based control pay off? *PLoS Computational Biology*, 12(8), e1005090. ([DOI](https://doi.org/10.1371/journal.pcbi.1005090), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27564094/))
- Gillan, C. M., Kosinski, M., Whelan, R., Phelps, E. A., & Daw, N. D. (2016). Characterizing a psychiatric symptom dimension related to deficits in goal-directed control. *eLife*, 5, e11305. ([DOI](https://doi.org/10.7554/elife.11305), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26928075/))
- da Silva, C. F., & Hare, T. A. (2020). Humans primarily use model-based inference in the two-stage task. *Nature Human Behaviour*, 4, 1053–1066. ([DOI](https://doi.org/10.1038/s41562-020-0905-y), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32632333/))
- Feher da Silva, C., & Hare, T. A. (2018). A note on the analysis of two-stage task results: How changes in task structure affect what model-free and model-based strategies predict about the effects of reward and transition on the stay probability. *PLoS ONE*, 13(4), e0195328. ([DOI](https://doi.org/10.1371/journal.pone.0195328), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29614130/))

## External links

- Cognitive Atlas: [2-stage decision task](https://www.cognitiveatlas.org/task/id/trm_5667451917a34)

