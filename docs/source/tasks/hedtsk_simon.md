(hedtsk_simon)=
# Simon Task

**HED task ID:** `hedtsk_simon`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Simon Effect Task, Spatial Compatibility

Non-spatial feature (e.g. color) dictates a left/right response while task-irrelevant stimulus location varies; RT cost on incongruent trials indexes spatial response conflict.

## Description

The Simon Task measures the effect of spatial stimulus-response correspondence on performance. Participants respond to a non-spatial stimulus attribute (e.g., color: press left for red, right for blue) while the stimulus appears on either the left or right side of the screen. When stimulus location corresponds with the assigned response side (congruent), responses are faster and more accurate than when they do not correspond (incongruent). The Simon effect reflects automatic activation of a spatially corresponding response that must be overridden when incongruent. The task is a foundational paradigm for studying stimulus-response compatibility and dimensional overlap.

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
* - **Measurements**
  - - Simon effect (RT difference: incongruent - congruent)
    - Accuracy
    - Delta-plot analysis of time-course of interference
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
* - Visual Simon Task (Standard)

    `hedvar_simon__visual_simon_task_standard`
  - A colored shape appears to the left or right of center, and the participant presses a left key for one color and a right key for the other. Position is irrelevant, but responses are slower when the stimulus appears on the side opposite the required key.
  - Canonical: respond to color/shape despite irrelevant spatial position
* - Auditory Simon Task

    `hedvar_simon__auditory_simon`
  - A tone is played to the left or right ear and the participant presses a key based on its pitch. Responses are slower when the required key is on the opposite side from the ear that heard the tone.
  - Auditory stimulus location as irrelevant dimension; different sensory modality
* - Vertical Simon Task

    `hedvar_simon__vertical_simon`
  - The stimulus appears above or below center and the response keys are arranged one above the other, so the conflict is between up-down position and up-down response.
  - Vertical rather than horizontal spatial dimension; different axis of conflict
* - Simon Task with Accessory Stimuli

    `hedvar_simon__simon_task_with_accessory_stimuli`
  - An irrelevant tone is played at the same time as the visual stimulus, from the same or opposite side, or centrally, to study how an extra event affects the position conflict.
  - Non-response-relevant accessory stimulus added; tests alerting-compatibility interaction
* - Reversed Simon Task

    `hedvar_simon__reversed_simon`
  - The participant is told to press the key opposite to where the stimulus appears, or practices such a mapping, before the standard task. This can reverse the usual effect.
  - Stimulus-response mapping reversed; opposite compatibility mapping
* - Joint Simon Task

    `hedvar_simon__joint_simon`
  - Two people sit side by side and each is responsible for one response key and one color, so each has a simple go/no-go task. The position conflict reappears for each person as if they were doing the whole task alone.
  - Two participants share one Simon task; tests social simulation of co-actor's response
* - Hybrid Simon-Flanker Task

    `hedvar_simon__hybrid_simon_flanker`
  - The lateral stimulus is also surrounded by flanker items that match or conflict with it, so that position conflict and flanker conflict are present in the same trial.
  - Integrates flanker conflict with Simon conflict; combined interference paradigm
* - Emotional Simon Task

    `hedvar_simon__emotional_simon`
  - The stimuli are emotional faces or words shown to the left or right, with the response based on their emotion, or the response keys are labeled with positive and negative meanings so that the irrelevant emotional content can conflict with the response.
  - Emotional content as irrelevant dimension; retained per section 5.1 (EMOT retired)
* - Mouse-Tracking Simon

    `hedvar_simon__mouse_tracking_simon`
  - The participant responds by moving a mouse to a target in the upper left or right of the screen, and the whole path of the cursor is recorded. Curvature toward the wrong side shows the pull of the stimulus position.
  - Continuous mouse trajectory as response; different response modality
* - Simon with Proportion-Congruent Manipulation

    `hedvar_simon__simon_with_proportion_congruent_manipulation`
  - The share of trials on which position and response agree is varied between blocks, for example mostly agreeing in one block and mostly conflicting in another, to see how the effect changes when conflict is expected.
  - Varies conflict frequency; adaptation context manipulation per section 5.2
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

