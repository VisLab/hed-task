(hedtsk_probabilistic_classification_learning)=
# Probabilistic Classification Learning Task

**HED task ID:** `hedtsk_probabilistic_classification_learning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Weather Prediction, Probabilistic Classification Learning, Weather Prediction Task, WPT

Multi-cue probabilistic prediction of a binary outcome with trial-by-trial feedback; learning curves index gradual procedural category learning.

## Description

The Weather Prediction Task presents 1-3 cues from a set of 4 possible cards; participants predict a binary outcome (rain/sunshine). Each cue is probabilistically associated with outcomes (e.g., 75%/25%), requiring participants to learn from statistical patterns. Feedback is provided after each prediction. Critically, amnesic patients with medial temporal lobe damage show intact learning despite impaired conscious awareness of the task structure, implicating basal ganglia and striatal systems in implicit probabilistic learning.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *Where does the rule come from?* <a href="vocabulary.html#rule-respond-to-rule-rule-source-learned-from-feedback">learned from feedback</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-feedback-reliability">feedback reliability</a>, <a href="vocabulary.html#setting-set-size">set size</a>
- **Material:** Four cue cards, one to three shown per trial, each linked with a fixed probability to rain or sunshine.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants predict an outcome (e.g., rain/sun) based on combinations of cues (cards), where each cue is probabilistically (not deterministically) related to outcomes.
    2. Learning is incremental across hundreds of trials.
    3. Optional: After learning a test phase uses novel card combinations or reversed outcome links.
* - **Manipulations**
  - - Cue-outcome probability structure
    - Number of cues per trial
    - Feedback type (corrective, observational)
    - Concurrent vs. single task
    - Category structure (rule-based vs. information-integration)
* - **Measurements**
  - - Accuracy learning curve
    - Optimal response rate
    - Strategy analysis (multi-cue vs. single-cue)
    - Comparison to Parkinson patients (basal ganglia involvement)
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
* - Information-Integration Category Learning

    `hedvar_probabilistic_classification_learning__information_integration_category_learning`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - -
  - The stimuli become shapes varying continuously on two or more dimensions and the category depends on combining the dimensions in a way that cannot be stated as a rule.
* - Rule-Based Category Learning (comparison)

    `hedvar_probabilistic_classification_learning__rule_based_category_learning_comparison`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - [Hypothesis testing](../processes/reasoning_and_problem_solving.md#hed-hypothesis-testing)
  - The stimuli become shapes varying on several continuous dimensions, with the category fixed by one dimension alone so the rule can be found by hypothesis testing.
* - Feedback vs. Observation Learning

    `hedvar_probabilistic_classification_learning__feedback_vs_observation_learning`
  - feedback: none
  - -
  - In the observation version each card set is shown with its outcome and the participant only watches; both versions are then tested without feedback.
* - Transfer Test Variants

    `hedvar_probabilistic_classification_learning__transfer_test_variants`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-transfer">transfer</a>
  - -
  - After learning, a test phase uses card combinations never seen in training, or the trained cards with their outcome links reversed.
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

- Knowlton, B. J., & Patterson, T. K. (2018). Habit formation and the striatum. *Current Topics in Behavioral Neurosciences*, 37, 275-295. ([DOI](https://doi.org/10.1007/7854_2016_451))
- Meeter, M., Myers, C. E., Shohamy, D., Hopkins, R. O., & Gluck, M. A. (2006). Strategies in probabilistic categorization: Results from a new way of analyzing performance. *Learning & Memory*, 13(2), 230-239. ([DOI](https://doi.org/10.1101/lm.43006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16547162/))
- Price, A. L. (2009). Distinguishing the contributions of implicit and explicit processes to performance of the weather prediction task. *Memory & Cognition*, 37(2), 210-222. ([DOI](https://doi.org/10.3758/mc.37.2.210), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19223570/))
- Foerde, K., Knowlton, B. J., & Poldrack, R. A. (2006). Modulation of competing memory systems by distraction. *Proceedings of the National Academy of Sciences*, 103(31), 11778-11783. ([DOI](https://doi.org/10.1073/pnas.0602659103), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16868087/))

## External links

- Cognitive Atlas: [Probabilistic classification task](https://www.cognitiveatlas.org/task/id/trm_4cacf22a22d80)

