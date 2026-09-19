(hedtsk_probabilistic_classification_learning)=
# Probabilistic Classification Learning Task

**HED task ID:** `hedtsk_probabilistic_classification_learning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Weather Prediction, Probabilistic Classification Learning, Weather Prediction Task, WPT

Multi-cue probabilistic prediction of a binary outcome with trial-by-trial feedback; learning curves index gradual procedural category learning.

## Description

The Weather Prediction Task presents 1-3 cues from a set of 4 possible cards; participants predict a binary outcome (rain/sunshine). Each cue is probabilistically associated with outcomes (e.g., 75%/25%), requiring participants to learn from statistical patterns. Feedback is provided after each prediction. Critically, amnesic patients with medial temporal lobe damage show intact learning despite impaired conscious awareness of the task structure, implicating basal ganglia and striatal systems in implicit probabilistic learning.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants predict an outcome (e.g., rain/sun) based on combinations of cues (cards), where each cue is probabilistically (not deterministically) related to outcomes. Learning is incremental across hundreds of trials.
* - **Manipulation**
  - Cue-outcome probability structure; number of cues per trial; feedback type (corrective, observational); concurrent vs. single task.
* - **Measurement**
  - Accuracy learning curve; optimal response rate; strategy analysis (multi-cue vs. single-cue); comparison to Parkinson patients (basal ganglia involvement).
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
* - Standard Weather Prediction (4 cues, binary outcome)

    `hedvar_probabilistic_classification_learning__standard_weather_prediction_4_cues_binary_outcome`
  - Four cards with probabilistic associations to rain/sun.
  - Canonical probabilistic categorization with cue combinations
* - Deterministic Version

    `hedvar_probabilistic_classification_learning__deterministic_version`
  - 100% cue-outcome mappings; becomes explicit rule learning.
  - Cues perfectly predict outcome; removes probabilistic uncertainty
* - Varying Probability Levels

    `hedvar_probabilistic_classification_learning__varying_probability_levels`
  - Different probabilistic strengths (60/40 to 90/10).
  - Cue-outcome reliability systematically manipulated; different learning statistics
* - Information-Integration Category Learning

    `hedvar_probabilistic_classification_learning__information_integration_category_learning`
  - Multi-dimensional continuous stimuli; optimal categorization requires integration across dimensions.
  - Categories defined by integration of dimensions; different decision rule
* - Rule-Based Category Learning (comparison)

    `hedvar_probabilistic_classification_learning__rule_based_category_learning_comparison`
  - Stimuli categorizable by single explicit rule; dissociates from implicit systems.
  - Explicit rule applicable; contrasts implicit vs. explicit learning systems
* - Feedback vs. Observation Learning

    `hedvar_probabilistic_classification_learning__feedback_vs_observation_learning`
  - Learning from trial-by-trial feedback vs. observing cue-outcome pairings.
  - Active feedback vs. observational learning; different learning mechanism
* - Transfer Test Variants

    `hedvar_probabilistic_classification_learning__transfer_test_variants`
  - New cue combinations or reversed contingencies after initial learning.
  - Probe generalization with novel cue combinations; different test phase
```

## Cognitive processes

This task is designed to engage the following processes:

- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)
- [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use)
- [Procedural memory](../processes/implicit_and_statistical_learning.md#hed-procedural-memory)

## Key references

- Knowlton, B. J., Squire, L. R., & Gluck, M. A. (1994). Probabilistic classification learning in amnesia. *Learning & Memory*, 1(2), 106-120. ([DOI](https://doi.org/10.1101/lm.1.2.106), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10467589/))
- Poldrack, R. A., Prabhakaran, V., Seger, C. A., & Gabrieli, J. D. (1999). Striatal activation during acquisition of a cognitive skill. *Neuropsychology*, 13(4), 564-574. ([DOI](https://doi.org/10.1037/0894-4105.13.4.564), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10527065/))
- Seger, C. A. (2008). How do the basal ganglia contribute to categorization? Their roles in generalization, response selection, and learning via feedback. *Neuroscience & Biobehavioral Reviews*, 32(2), 265-278. ([DOI](https://doi.org/10.1016/j.neubiorev.2007.07.010), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17919725/))

## Further references

- Knowlton, B. J., & Patterson, T. K. (2018). Habit formation and the striatum. *Current Topics in Behavioral Neurosciences*, 37, 275–295. ([DOI](https://doi.org/10.1007/7854_2016_451))
- Meeter, M., Myers, C. E., Shohamy, D., Hopkins, R. O., & Gluck, M. A. (2006). Strategies in probabilistic categorization: Results from a new way of analyzing performance. *Learning & Memory*, 13(2), 230–239. ([DOI](https://doi.org/10.1101/lm.43006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16547162/))
- Price, A. L. (2009). Distinguishing the contributions of implicit and explicit processes to performance of the weather prediction task. *Memory & Cognition*, 37(2), 210–222. ([DOI](https://doi.org/10.3758/mc.37.2.210), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19223570/))
- Foerde, K., Knowlton, B. J., & Poldrack, R. A. (2006). Modulation of competing memory systems by distraction. *Proceedings of the National Academy of Sciences*, 103(31), 11778–11783. ([DOI](https://doi.org/10.1073/pnas.0602659103), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16868087/))

## External links

- Cognitive Atlas: [Probabilistic classification task](https://www.cognitiveatlas.org/task/id/trm_4cacf22a22d80)

