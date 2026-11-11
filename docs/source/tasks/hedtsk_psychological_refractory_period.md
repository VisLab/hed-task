(hedtsk_psychological_refractory_period)=
# Psychological Refractory Period Task

**HED task ID:** `hedtsk_psychological_refractory_period`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** PRP, Psychological Refractory Period

Two tasks presented with a short SOA; RT for the second task lengthens as SOA shortens, indexing a central response-selection bottleneck.

## Description

Two stimuli are presented in rapid succession (S1 then S2, separated by a variable stimulus onset asynchrony or SOA), each requiring its own speeded response (R1 and R2). The robust finding is that R2 is slowed as the SOA decreases - the psychological refractory period effect - because central response-selection processes for S2 must wait until response selection for S1 is complete. Pashler (1994) provided the definitive review establishing the central bottleneck model: perceptual processing and motor execution can overlap between tasks, but response selection (choosing which response to make) represents a serial bottleneck. The PRP paradigm remains the primary tool for mapping the architecture of cognitive processing stages and understanding the limits of multitasking.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Two stimuli requiring separate speeded responses are presented in rapid succession with a variable stimulus-onset asynchrony (SOA).
    2. Both responses are required.
* - **Manipulations**
  - - SOA between S1 and S2 (50-1000 ms)
    - Task difficulty of each task
    - Response modality overlap
* - **Measurements**
  - - RT2 as a function of SOA (PRP effect: RT2 slowing at short SOAs)
    - RT1 (usually unaffected)
    - Locus of interference per bottleneck models
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
* - Standard Auditory-Visual PRP

    `hedvar_psychological_refractory_period__standard_auditory_visual_prp`
  - On each trial a tone sounds and, a short and variable time later, a letter or digit appears. The participant responds to the tone (for example high or low pitch, with one hand) and then to the visual item (with the other hand). The shorter the gap between them, the slower the second response.
  - Canonical PRP: auditory then visual stimulus with variable SOA
* - Visual-Visual PRP

    `hedvar_psychological_refractory_period__visual_visual_prp`
  - Both stimuli are visual, shown at different positions so they can be told apart, for example a colored patch followed by a letter. Tests whether the slowing of the second response depends on using two senses.
  - Both stimuli visual; tests modality effects on bottleneck
* - Variable SOA Design

    `hedvar_psychological_refractory_period__variable_soa_design`
  - The gap between the first and second stimulus is varied across a wide range, from about 50 ms up to a second, so that the second response time can be plotted against the gap.
  - Multiple SOAs parametrically varied; standard PRP SOA manipulation
* - PRP with Practice

    `hedvar_psychological_refractory_period__prp_with_practice`
  - Participants perform thousands of trials across several sessions, to see whether the slowing of the second response shrinks or disappears with extensive practice.
  - Extended practice changes PRP magnitude; tests dual-task automatization
* - PRP with Ideomotor-Compatible Tasks

    `hedvar_psychological_refractory_period__prp_with_ideomotor_compatible_tasks`
  - The tasks are chosen so the response naturally matches the stimulus, such as saying 'A' when hearing 'A' or pressing a key under a finger that is touched. Such tasks produce little or no slowing of the second response.
  - Ideomotor-compatible S-R mappings eliminate bottleneck; tests structural bottleneck theory
* - Triple-Task PRP

    `hedvar_psychological_refractory_period__triple_task_prp`
  - Three stimuli are presented in quick succession, each needing its own response, to test how the slowing builds up when more than two tasks overlap.
  - Three concurrent tasks; extends bottleneck theory to three tasks
```

## Cognitive processes

This task is designed to engage the following processes:

- [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)
- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)
- [Motor preparation](../processes/motor_preparation_timing_and_execution.md#hed-motor-preparation)

## Key references

- Pashler, H. (1994). Dual-task interference in simple tasks: Data and theory. *Psychological Bulletin*, 116(2), 220-244. ([DOI](https://doi.org/10.1037/0033-2909.116.2.220), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7972591/))
- Pashler, H., & Johnston, J. C. (1998). Attentional limitations in dual-task performance. In H. Pashler (Ed.), *Attention* (pp. 155-189). Psychology Press.

## Further references

- Tombu, M., & Jolicoeur, P. (2003). A central capacity sharing model of dual-task performance. *Journal of Experimental Psychology: Human Perception and Performance*, 29(1), 3-18. ([DOI](https://doi.org/10.1037/0096-1523.29.1.3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12669744/))
- Sigman, M., & Dehaene, S. (2008). Brain mechanisms of serial and parallel processing during dual-task performance. *Journal of Neuroscience*, 28(30), 7585-7598. ([DOI](https://doi.org/10.1523/jneurosci.0948-08.2008), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18650336/))
- Strobach, T., Schubert, T., Pashler, H., & Rickard, T. (2014). The specificity of stimulus-response and response-response compatibility effects in dual tasks. *Journal of Experimental Psychology: Human Perception and Performance*, 40(5), 1966-1984.
- Zickerick, B., Thönes, S., Kobald, S. O., Wascher, E., Schneider, D., & Küper, K. (2021). Differential effects of the psychological refractory period on early perceptual processing. *Psychophysiology*, 58(5), e13791.

## External links

- Cognitive Atlas: [psychological refractory period (PRP) paradigm](https://www.cognitiveatlas.org/task/id/trm_51c453f64d2a6)

