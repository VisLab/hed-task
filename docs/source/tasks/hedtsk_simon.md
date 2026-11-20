(hedtsk_simon)=
# Simon Task

**HED task ID:** `hedtsk_simon`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Simon Effect Task, Spatial Compatibility

Non-spatial feature (e.g. color) dictates a left/right response while task-irrelevant stimulus location varies; RT cost on incongruent trials indexes spatial response conflict.

## Description

The Simon Task measures the effect of spatial stimulus-response correspondence on performance. Participants respond to a non-spatial stimulus attribute (e.g., color: press left for red, right for blue) while the stimulus appears on either the left or right side of the screen. When stimulus location corresponds with the assigned response side (congruent), responses are faster and more accurate than when they do not correspond (incongruent). The Simon effect reflects automatic activation of a spatially corresponding response that must be overridden when incongruent. The task is a foundational paradigm for studying stimulus-response compatibility and dimensional overlap.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What competes with the correct response?** <a href="vocabulary.html#rule-respond-to-rule-competitor-irrelevant-dimension">irrelevant dimension</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-eccentricity">eccentricity</a>, <a href="vocabulary.html#setting-proportion-congruent">proportion congruent</a>
- **Material:** Stimuli that differ in color or shape and appear on the left or the right of the screen.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Stimuli varying on a non-spatial attribute (color, shape) appear on the left or right.
    2. Participants respond with spatially mapped keys.
    3. On incongruent trials, stimulus location conflicts with response location.
* - **Manipulations**
  - - Spatial congruency (stimulus side matches or conflicts with response side)
    - Stimulus eccentricity
    - Proportion congruent
    - Stimulus and response axis (vertical vs. horizontal)
    - Accessory tone (same side, opposite side, center)
    - Prior stimulus-response mapping (reversed training or instruction)
    - Number of participants (joint vs. individual)
    - Added flankers around the lateral stimulus
    - Stimulus type (emotional faces or words)
* - **Measurements**
  - - Simon effect (RT difference: incongruent - congruent)
    - Accuracy
    - Delta-plot analysis of time-course of interference
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
* - Auditory Simon Task

    `hedvar_simon__auditory_simon`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - A tone in the left or right ear is classified by pitch, so the irrelevant location is the ear of presentation.
* - Simon Task with Accessory Stimuli

    `hedvar_simon__simon_task_with_accessory_stimuli`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>; cue: <a href="vocabulary.html#rule-respond-to-rule-cue-alerting-cue">alerting cue</a>
  - [Alerting](../processes/selective_and_sustained_attention.md#hed-alerting), [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - An irrelevant tone sounds together with the visual stimulus from the same side, the opposite side or the center, acting as an alerting event (simultaneous, not in advance).
* - Joint Simon Task

    `hedvar_simon__joint_simon`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>; response demand: <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
  - [Self-other distinction](../processes/social_cognition_and_strategic_social_choice.md#hed-self-other-distinction), [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
  - Two people sit side by side, each owning one key and one color, so each performs a go/no-go task while the position conflict reappears.
* - Hybrid Simon-Flanker Task

    `hedvar_simon__hybrid_simon_flanker`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
  - -
  - The lateral stimulus is also surrounded by flankers, so its irrelevant location and the neighbouring items both compete with the response on the same trial.
* - Emotional Simon Task

    `hedvar_simon__emotional_simon`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>, <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
  - Emotional faces or words appear left or right and the response is based on their emotion, or the keys carry positive and negative meanings so emotional content conflicts with the response.
* - Mouse-Tracking Simon

    `hedvar_simon__mouse_tracking_simon`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>
  - -
  - The response is a mouse movement to an upper-left or upper-right target and the cursor path is the measure; the trial design is unchanged.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Simon, J. R., & Rudell, A. P. (1967). Auditory S-R compatibility: The effect of an irrelevant cue on information processing. *Journal of Applied Psychology*, 51(3), 300-304. ([DOI](https://doi.org/10.1037/h0020586), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6045637/))
- Kornblum, S., Hasbroucq, T., & Osman, A. (1990). Dimensional overlap: Cognitive basis for stimulus-response compatibility - A model and taxonomy. *Psychological Review*, 97(2), 253-270. ([DOI](https://doi.org/10.1037/0033-295x.97.2.253), [PubMed](https://pubmed.ncbi.nlm.nih.gov/2186425/))
- De Jong, R., Liang, C.-C., & Lauber, E. (1994). Conditional and unconditional automaticity: A dual-process model of effects of spatial stimulus-response correspondence. *Journal of Experimental Psychology: Human Perception and Performance*, 20(4), 731-750. ([DOI](https://doi.org/10.1037/0096-1523.20.4.731), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8083631/))

## Further references

- Hommel, B. (2011). The Simon effect as tool and heuristic. *Acta Psychologica*, 136(2), 189-202. ([DOI](https://doi.org/10.1016/j.actpsy.2010.04.011), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20507830/))
- Wiegand, K., & Wascher, E. (2005). Dynamic aspects of stimulus-response correspondence: Evidence for two mechanisms involved in the Simon effect. *Journal of Experimental Psychology: Human Perception and Performance*, 31(3), 453-464. ([DOI](https://doi.org/10.1037/0096-1523.31.3.453), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15982125/))
- Proctor, R. W., Miles, J. D., & Baroni, G. (2011). Reaction time distribution analysis of spatial correspondence effects. *Psychonomic Bulletin & Review*, 18(2), 242-266. ([DOI](https://doi.org/10.3758/s13423-011-0053-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21327376/))
- Salzer, Y., de Hollander, G., & Forstmann, B. U. (2017). Sensory neural pathways revisited to unravel the temporal dynamics of the Simon effect: A model-based cognitive neuroscience approach. *Neuroscience & Biobehavioral Reviews*, 77, 48-57. ([DOI](https://doi.org/10.1016/j.neubiorev.2017.02.023), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28238943/))

## External links

- Cognitive Atlas: [Simon task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949dbb)

- CogPO: [Simon Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Simon_Task_Paradigm)

