(hedtsk_serial_reaction_time)=
# Serial Reaction Time Task

**HED task ID:** `hedtsk_serial_reaction_time`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md) (also [Motor performance and speeded response tasks](families/motor_performance.md))

**Also known as:** SRTT, Serial RT, Serial Reaction Time

Sequential key-press responses to cued locations; RT speedup on repeating vs random sequences indexes implicit sequence learning.

## Description

The SRTT measures implicit motor sequence learning. Visual stimuli appear sequentially at different spatial locations, each corresponding to a response button. Participants respond as quickly as possible, unaware that stimuli follow a repeating sequence interspersed with random blocks. Learning is inferred from decreasing RT for the repeating sequence relative to random sequences. The dissociation between improved performance and lack of conscious awareness of the sequence structure is a hallmark of implicit learning and provides evidence for procedural memory systems.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Stimuli appear at one of several spatial locations in a repeating (but covert) sequence; participants respond to each location with a spatially mapped keypress. Sequence awareness is typically not disclosed.
* - **Manipulation**
  - Sequence length and complexity; sequence vs. random blocks; explicit vs. implicit instruction; secondary task (dual-task interference).
* - **Measurement**
  - RT slowing when sequence is replaced by random order (sequence learning effect); explicit sequence knowledge (generation task, recognition); offline consolidation gains.
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
* - Deterministic SRTT

    `hedvar_serial_reaction_time__deterministic_srtt`
  - Fixed repeating sequence (e.g., 10-element) embedded in random blocks.
  - Fixed repeating sequence; canonical implicit sequence learning
* - Probabilistic SRTT

    `hedvar_serial_reaction_time__probabilistic_srtt`
  - Transition probabilities rather than fixed sequences; tests statistical learning.
  - High-probability sequence structure; tests learning under uncertainty
* - Alternating Serial Reaction Time (ASRT)

    `hedvar_serial_reaction_time__alternating_serial_reaction_time_asrt`
  - Pattern and random elements alternate in fixed schedule.
  - Alternating random and patterned elements; tests learning of alternating structure
* - SRTT with Awareness Assessment

    `hedvar_serial_reaction_time__srtt_with_awareness_assessment`
  - Post-task sequence generation, recognition, or verbal report tests.
  - Explicit sequence knowledge probed after implicit learning; adds awareness component
* - Second-Order Conditional (SOC) Sequences

    `hedvar_serial_reaction_time__second_order_conditional_soc_sequences`
  - Sequence structure based on triplet dependencies rather than simple transitions.
  - Each response depends on two preceding; different sequence order
* - Arm-Reaching/Foot-Stepping SRTT

    `hedvar_serial_reaction_time__arm_reaching_foot_stepping_srtt`
  - Non-finger responses to test effector-specific learning.
  - Full-limb movements instead of finger presses; different motor effector
* - Cross-Modal SRTT

    `hedvar_serial_reaction_time__cross_modal_srtt`
  - Stimuli in different modalities (visual positions, auditory tones) to test modality specificity.
  - Auditory sequence instead of visual; different sensory modality
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

- Janacsek, K., & Nemeth, D. (2012). Predicting the future: From implicit learning to consolidation. *International Journal of Psychophysiology*, 83(2), 213–221. ([DOI](https://doi.org/10.1016/j.ijpsycho.2011.11.012), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22154521/))
- Abrahamse, E. L., Jiménez, L., Verwey, W. B., & Clegg, B. A. (2010). Representing serial action and perception. *Psychonomic Bulletin & Review*, 17(5), 603–623. ([DOI](https://doi.org/10.3758/pbr.17.5.603), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21037157/))
- Siegert, R. J., Taylor, K. D., Weatherall, M., & Abernethy, D. A. (2006). Is implicit sequence learning impaired in Parkinson's disease? A meta-analysis. *Neuropsychology*, 20(4), 490–495. [Updated: Clark, G. M., Lum, J. A., & Ullman, M. T. (2014). A meta-analysis and meta-regression of serial reaction time task performance in Parkinson's disease. *Neuropsychology*, 28(6), 945–958.] ([DOI](https://doi.org/10.1037/0894-4105.20.4.490), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16846267/))

## External links

- Cognitive Atlas: [serial reaction time task](https://www.cognitiveatlas.org/task/id/trm_4f241c735e7f6)

