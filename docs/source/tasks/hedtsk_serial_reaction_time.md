(hedtsk_serial_reaction_time)=
# Serial Reaction Time Task

**HED task ID:** `hedtsk_serial_reaction_time`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md) (also [Motor performance and speeded response tasks](families/motor_performance.md))

**Also known as:** SRTT, Serial RT, Serial Reaction Time

Sequential key-press responses to cued locations; RT speedup on repeating vs random sequences indexes implicit sequence learning.

## Description

The SRTT measures implicit motor sequence learning. Visual stimuli appear sequentially at different spatial locations, each corresponding to a response button. Participants respond as quickly as possible, unaware that stimuli follow a repeating sequence interspersed with random blocks. Learning is inferred from decreasing RT for the repeating sequence relative to random sequences. The dissociation between improved performance and lack of conscious awareness of the sequence structure is a hallmark of implicit learning and provides evidence for procedural memory systems.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-localize">localize</a>
  - *Where does the rule come from?* <a href="vocabulary.html#rule-respond-to-rule-rule-source-hidden-regularity">hidden regularity</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-list-length">list length</a>
- **Material:** A stimulus at one of several screen locations, each mapped to a key, following a repeating sequence or a random order.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Stimuli appear at one of several spatial locations in a repeating (but covert) sequence.
    2. Participants respond to each location with a spatially mapped keypress.
    3. Sequence awareness is typically not disclosed.
    4. Optional: After the main task the participant is asked whether a sequence was noticed, asked to reproduce it, or shown fragments to recognize.
* - **Manipulations**
  - - Sequence length and complexity
    - Sequence vs. random blocks
    - Explicit vs. implicit instruction
    - Secondary task (dual-task interference)
    - Sequence structure (probabilistic vs. deterministic)
* - **Measurements**
  - - RT slowing when sequence is replaced by random order (sequence learning effect)
    - Explicit sequence knowledge (generation task, recognition)
    - Offline consolidation gains
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
* - Alternating Serial Reaction Time (ASRT)

    `hedvar_serial_reaction_time__alternating_serial_reaction_time_asrt`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - -
  - Fixed-sequence positions alternate item by item with random positions, so the regularity spans every other element.
* - Arm-Reaching/Foot-Stepping SRTT

    `hedvar_serial_reaction_time__arm_reaching_foot_stepping_srtt`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-motion-capture">motion capture</a>, <a href="vocabulary.html#facet-task-io-device-pedal">pedal</a>
  - -
  - The responses are reaches to targets or steps onto floor pads instead of finger presses.
* - Cross-Modal SRTT

    `hedvar_serial_reaction_time__cross_modal_srtt`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - The cues are tones of different pitches mapped to keys instead of visual positions, or the modality switches between learning and test.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Motor sequence learning](../processes/motor_preparation_timing_and_execution.md#hed-motor-sequence-learning)
- [Implicit memory](../processes/implicit_and_statistical_learning.md#hed-implicit-memory)
- [Procedural memory](../processes/implicit_and_statistical_learning.md#hed-procedural-memory)
- [Motor preparation](../processes/motor_preparation_timing_and_execution.md#hed-motor-preparation)
- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)

## Key references

- Nissen, M. J., & Bullemer, P. (1987). Attentional requirements of learning: Evidence from performance measures. *Cognitive Psychology*, 19(1), 1-32. ([DOI](https://doi.org/10.1016/0010-0285(87)90002-8))
- Robertson, E. M. (2007). The serial reaction time task: Implicit motor skill learning? *Journal of Neuroscience*, 27(38), 10073-10075. ([DOI](https://doi.org/10.1523/jneurosci.2747-07.2007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17881512/))
- Grafton, S. T., Hazeltine, E., & Ivry, R. B. (1995). Functional mapping of sequence learning in normal humans. *Journal of Cognitive Neuroscience*, 7(4), 497-510. ([DOI](https://doi.org/10.1162/jocn.1995.7.4.497), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23961907/))

## Further references

- Janacsek, K., & Nemeth, D. (2012). Predicting the future: From implicit learning to consolidation. *International Journal of Psychophysiology*, 83(2), 213-221. ([DOI](https://doi.org/10.1016/j.ijpsycho.2011.11.012), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22154521/))
- Abrahamse, E. L., Jiménez, L., Verwey, W. B., & Clegg, B. A. (2010). Representing serial action and perception. *Psychonomic Bulletin & Review*, 17(5), 603-623. ([DOI](https://doi.org/10.3758/pbr.17.5.603), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21037157/))
- Siegert, R. J., Taylor, K. D., Weatherall, M., & Abernethy, D. A. (2006). Is implicit sequence learning impaired in Parkinson's disease? A meta-analysis. *Neuropsychology*, 20(4), 490-495. [Updated: Clark, G. M., Lum, J. A., & Ullman, M. T. (2014). A meta-analysis and meta-regression of serial reaction time task performance in Parkinson's disease. *Neuropsychology*, 28(6), 945-958.] ([DOI](https://doi.org/10.1037/0894-4105.20.4.490), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16846267/))

## External links

- Cognitive Atlas: [serial reaction time task](https://www.cognitiveatlas.org/task/id/trm_4f241c735e7f6)

- CogPO: [Sequence Recall/Learning Paradigm](http://www.wiki.cogpo.org/index.php?title=Sequence_Recall_or_Learning_Paradigm) (close match)

