(hedtsk_motor_sequence_learning)=
# Motor Sequence Learning Task

**HED task ID:** `hedtsk_motor_sequence_learning`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** Sequence Learning, Finger Sequence Task

Repeated execution of a fixed finger sequence; within- and across-session speed and accuracy changes index motor skill learning.

## Description

Participants are trained to execute finger sequences (e.g., pressing buttons in a specific order: 4-1-3-2-4) either continuously or in discrete blocks. Learning is indexed by decreasing RT, reduced movement duration, and decreased errors. Neuroimaging shows early learning engages cerebellum and prefrontal cortex, while consolidated sequences show greater striatal and reduced cerebellar engagement, reflecting a shift from explicit, attention-demanding processes to implicit, automatic execution. Sleep promotes offline consolidation of motor sequences.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants repeatedly perform a fixed sequence of finger movements (e.g., 4-1-3-2-4) in response to spatial cues. Over practice, performance speeds up and becomes more automatic.
* - **Manipulation**
  - Sequence length and complexity; explicit vs. implicit instruction; amount of practice; sleep consolidation intervals.
* - **Measurement**
  - Sequence execution time; error rate; offline gains (improvement after sleep); transfer to new sequences.
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
* - Discrete Sequence Production (DSP)

    `hedvar_motor_sequence_learning__discrete_sequence_production_dsp`
  - Execute learned sequences from memory as fast as possible.
  - Canonical pre-learned sequence executed rapidly; measures chunking
* - Serial Reaction Time Task variant

    `hedvar_motor_sequence_learning__serial_reaction_time_task_variant`
  - Implicit sequence learning via stimulus-response mapping.
  - Implicit learning via RT advantages for repeating sequences
* - Finger Opposition Task

    `hedvar_motor_sequence_learning__finger_opposition`
  - Sequential thumb-to-finger tapping in fixed patterns.
  - Thumb-to-finger opposition sequences; different finger movement type
* - Bimanual Coordination

    `hedvar_motor_sequence_learning__bimanual_coordination`
  - Both hands performing complementary or conflicting sequences.
  - Both hands performing sequences; interlimb coordination demands
* - Explicit vs. Implicit Sequence Learning

    `hedvar_motor_sequence_learning__explicit_vs_implicit_sequence_learning`
  - Participants aware vs. unaware of sequence structure.
  - Aware vs. unaware of sequence structure; different instruction and learning mechanism
* - Sequence Complexity Manipulation

    `hedvar_motor_sequence_learning__sequence_complexity_manipulation`
  - Simple (4-element) to complex (12-element) sequences.
  - Varies sequence length and structure; tests learning as function of complexity
* - Transfer Tests

    `hedvar_motor_sequence_learning__transfer_tests`
  - Testing learned sequences with different effectors or in mirror configuration.
  - Probe what was learned by testing with modified sequence; different test phase structure
* - Continuous Tracking + Sequence

    `hedvar_motor_sequence_learning__continuous_tracking_sequence`
  - Pursuit-tracking task with embedded repeating segments.
  - Sequence embedded in continuous tracking; tests incidental learning during ongoing task
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

- King, B. R., Hoedlmoser, K., Hirschauer, F., Dolfen, N., & Albouy, G. (2017). Sleeping on the motor engram: The multifaceted nature of sleep-related motor memory consolidation. *Neuroscience & Biobehavioral Reviews*, 80, 1–22. ([DOI](https://doi.org/10.1016/j.neubiorev.2017.04.026), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28465166/))
- Hikosaka, O., Nakamura, K., Sakai, K., & Nakahara, H. (2002). Central mechanisms of motor skill learning. *Current Opinion in Neurobiology*, 12(2), 217–222. [Updated: Diedrichsen, J., & Kornysheva, K. (2015). Motor skill learning between selection and execution. *Trends in Cognitive Sciences*, 19(4), 227–233.] ([DOI](https://doi.org/10.1016/s0959-4388(02)00307-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12015240/))
- Verwey, W. B., Shea, C. H., & Wright, D. L. (2015). A cognitive framework for explaining serial processing and sequence execution strategies. *Psychonomic Bulletin & Review*, 22(1), 54–77. ([DOI](https://doi.org/10.3758/s13423-014-0773-4))

## External links

- Cognitive Atlas: [sequence recall/learning](https://www.cognitiveatlas.org/task/id/trm_4c8a83cac75f5) (close match)

