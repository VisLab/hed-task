(hedtsk_psychological_refractory_period)=
# Psychological Refractory Period Task

**HED task ID:** `hedtsk_psychological_refractory_period`

**Family:** [Motor performance and speeded response tasks](families/motor_performance.md)

**Also known as:** PRP, Psychological Refractory Period

Two tasks presented with a short SOA; RT for the second task lengthens as SOA shortens, indexing a central response-selection bottleneck.

## Description

Two stimuli are presented in rapid succession (S1 then S2, separated by a variable stimulus onset asynchrony or SOA), each requiring its own speeded response (R1 and R2). The robust finding is that R2 is slowed as the SOA decreases - the psychological refractory period effect - because central response-selection processes for S2 must wait until response selection for S1 is complete. Pashler (1994) provided the definitive review establishing the central bottleneck model: perceptual processing and motor execution can overlap between tasks, but response selection (choosing which response to make) represents a serial bottleneck. The PRP paradigm remains the primary tool for mapping the architecture of cognitive processing stages and understanding the limits of multitasking.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** Two stimuli in rapid succession at a variable onset asynchrony, each calling for its own speeded response.
- **Combined with:** <a href="vocabulary.html#how-in-quick-succession">in quick succession</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (A second speeded classification whose stimulus follows the first at a varied short interval)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Two stimuli requiring separate speeded responses are presented in rapid succession with a variable stimulus-onset asynchrony (SOA).
    2. Both responses are required.
    3. Optional: Thousands of trials are run across several sessions to see whether the second-response slowing shrinks with practice.
* - **Manipulations**
  - - SOA between S1 and S2 (50-1000 ms)
    - Task difficulty of each task
    - Response modality overlap
    - Task compatibility (ideomotor-compatible vs. standard stimulus-response mapping)
    - Number of tasks (three overlapping tasks vs. two)
* - **Measurements**
  - - RT2 as a function of SOA (PRP effect: RT2 slowing at short SOAs)
    - RT1 (usually unaffected)
    - Locus of interference per bottleneck models
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
* - Visual-Visual PRP

    `hedvar_psychological_refractory_period__visual_visual_prp`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - -
  - Both stimuli are visual, shown at different positions, for example a colored patch then a letter.
* - PRP with Ideomotor-Compatible Tasks

    `hedvar_psychological_refractory_period__prp_with_ideomotor_compatible_tasks`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>, <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-tactile">tactile</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-pressure">pressure</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - [Somatosensory perception](../processes/face_and_object_perception.md#hed-somatosensory-perception)
  - The two tasks are chosen so that the response naturally matches the stimulus, for example saying "A" on hearing "A" or pressing the key under a touched finger.
* - Triple-Task PRP

    `hedvar_psychological_refractory_period__triple_task_prp`
  - combined with: <a href="vocabulary.html#how-in-quick-succession">in quick succession</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (Second speeded classification); combined with: <a href="vocabulary.html#how-in-quick-succession">in quick succession</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (Third speeded classification)
  - -
  - Three stimuli arrive in quick succession within one trial, and each needs its own response, so three responses overlap instead of two.
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

