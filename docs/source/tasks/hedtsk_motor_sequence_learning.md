(hedtsk_motor_sequence_learning)=
# Motor Sequence Learning Task

**HED task ID:** `hedtsk_motor_sequence_learning`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** Sequence Learning, Finger Sequence Task

Repeated execution of a fixed finger sequence; within- and across-session speed and accuracy changes index motor skill learning.

## Description

Participants are trained to execute finger sequences (e.g., pressing buttons in a specific order: 4-1-3-2-4) either continuously or in discrete blocks. Learning is indexed by decreasing RT, reduced movement duration, and decreased errors. Neuroimaging shows early learning engages cerebellum and prefrontal cortex, while consolidated sequences show greater striatal and reduced cerebellar engagement, reflecting a shift from explicit, attention-demanding processes to implicit, automatic execution. Sleep promotes offline consolidation of motor sequences.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-produce-movement">Make a movement</a> (`produce_movement`)
- **Game rules:** none are defined for this game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-list-length">list length</a>, <a href="vocabulary.html#setting-number-of-repetitions">number of repetitions</a>, <a href="vocabulary.html#setting-retention-interval">retention interval</a>
- **Material:** Spatial cues or a digit sequence (such as 4-1-3-2-4) naming the fingers to press in order.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants repeatedly perform a fixed sequence of finger movements (e.g., 4-1-3-2-4) in response to spatial cues.
    2. Over practice, performance speeds up and becomes more automatic.
    3. Optional: After practice the sequence is performed with the other hand, other fingers or mirror-reversed.
* - **Manipulations**
  - - Sequence length and complexity
    - Explicit vs. implicit instruction
    - Amount of practice
    - Sleep consolidation intervals
    - Number of hands (bimanual vs. unimanual)
    - Movement type (continuous tracking with hidden repeating path)
* - **Measurements**
  - - Sequence execution time
    - Error rate
    - Offline gains (improvement after sleep)
    - Transfer to new sequences
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
* - Finger Opposition Task

    `hedvar_motor_sequence_learning__finger_opposition`
  - task I/O device: none
  - -
  - The thumb touches the other fingers in a fixed order with no keys or screen; the sequence is given by instruction.
* - Transfer Tests

    `hedvar_motor_sequence_learning__transfer_tests`
  - phases: <a href="vocabulary.html#phase-transfer">transfer</a>
  - -
  - After practice the sequence is performed with the other hand, with other fingers, or mirror-reversed.
* - Continuous Tracking + Sequence

    `hedvar_motor_sequence_learning__continuous_tracking_sequence`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-joystick">joystick</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>
  - -
  - The participant follows a moving target with a joystick, and part of the target's path secretly repeats.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Motor sequence learning](../processes/motor_preparation_timing_and_execution.md#hed-motor-sequence-learning)
- [Procedural memory](../processes/implicit_and_statistical_learning.md#hed-procedural-memory)
- [Motor planning](../processes/motor_preparation_timing_and_execution.md#hed-motor-planning)
- [Fine motor control](../processes/motor_preparation_timing_and_execution.md#hed-fine-motor-control)
- [Consolidation](../processes/long_term_memory.md#hed-consolidation)

## Key references

- Karni, A., Meyer, G., Rey-Hipolito, C., et al. (1998). The acquisition of skilled motor performance: Fast and slow experience-driven changes in primary motor cortex. *Proceedings of the National Academy of Sciences*, 95(3), 861-868. ([DOI](https://doi.org/10.1073/pnas.95.3.861), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9448252/))
- Doyon, J., Bellec, P., Amsel, R., et al. (2009). Contributions of the basal ganglia and functionally related brain structures to motor learning. *Behavioural Brain Research*, 199(1), 61-72. ([DOI](https://doi.org/10.1016/j.bbr.2008.11.012), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19061920/))
- Walker, M. P., Brakefield, T., Morgan, A., Hobson, J. A., & Stickgold, R. (2002). Practice with sleep makes perfect: Sleep-dependent motor skill learning. *Neuron*, 35(1), 205-211. ([DOI](https://doi.org/10.1016/s0896-6273(02)00746-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12123620/))

## Further references

- King, B. R., Hoedlmoser, K., Hirschauer, F., Dolfen, N., & Albouy, G. (2017). Sleeping on the motor engram: The multifaceted nature of sleep-related motor memory consolidation. *Neuroscience & Biobehavioral Reviews*, 80, 1-22. ([DOI](https://doi.org/10.1016/j.neubiorev.2017.04.026), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28465166/))
- Hikosaka, O., Nakamura, K., Sakai, K., & Nakahara, H. (2002). Central mechanisms of motor skill learning. *Current Opinion in Neurobiology*, 12(2), 217-222. [Updated: Diedrichsen, J., & Kornysheva, K. (2015). Motor skill learning between selection and execution. *Trends in Cognitive Sciences*, 19(4), 227-233.] ([DOI](https://doi.org/10.1016/s0959-4388(02)00307-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12015240/))
- Verwey, W. B., Shea, C. H., & Wright, D. L. (2015). A cognitive framework for explaining serial processing and sequence execution strategies. *Psychonomic Bulletin & Review*, 22(1), 54-77. ([DOI](https://doi.org/10.3758/s13423-014-0773-4))

## External links

- Cognitive Atlas: [sequence recall/learning](https://www.cognitiveatlas.org/task/id/trm_4c8a83cac75f5) (close match)

- CogPO: [Sequence Recall/Learning Paradigm](http://www.wiki.cogpo.org/index.php?title=Sequence_Recall_or_Learning_Paradigm)

