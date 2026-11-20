(hedtsk_eriksen_flanker)=
# Eriksen Flanker Task

**HED task ID:** `hedtsk_eriksen_flanker`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Flanker, Flanker Task

A central target flanked by congruent or incongruent distractors; RT and error differences index selective attention and conflict resolution.

## Description

The Eriksen Flanker Task measures selective attention and the ability to inhibit responses to irrelevant flanking stimuli. Participants view a brief display of five items arranged horizontally, with a central target flanked by two non-target items on each side. The central target requires a specific response, while flanking items may be congruent (same response), incongruent (opposite response), or neutral. Participants respond via speeded button press while ignoring flankers. The flanker compatibility effect (slowed RT and increased errors on incongruent trials) indexes the degree of response competition and the efficiency of attentional filtering.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What competes with the correct response?** <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-proportion-congruent">proportion congruent</a>, <a href="vocabulary.html#setting-response-deadline">response deadline</a>, <a href="vocabulary.html#setting-spatial-separation">spatial separation</a>
- **Material:** A row of five items, a central arrow or letter between flankers that call for the same response, the opposite response or neither.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants identify a central target (arrow or letter) flanked by congruent, incongruent, or neutral distractors.
* - **Manipulations**
  - - Flanker congruency
    - Flanker-target distance
    - Proportion congruent
    - Response deadline
    - Stimulus type (arrows, letters, color patches, digits, emotional faces or pictures)
    - Added no-go signal on a minority of trials
* - **Measurements**
  - - RT and accuracy
    - Congruency effect (incongruent - congruent RT)
    - Delta plots (interference across RT distribution)
    - Conflict adaptation (Gratton effect)
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
* - Letter Flanker

    `hedvar_eriksen_flanker__letter_flanker`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - -
  - Letters replace arrows with an arbitrary letter-to-key mapping; the original 1974 form.
* - Color Flanker

    `hedvar_eriksen_flanker__color_flanker`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - -
  - The response is to the color of a central patch while flanking patches share the color or carry the other response's color.
* - Emotional Flanker

    `hedvar_eriksen_flanker__emotional_flanker`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>, <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
  - The central item and flankers are expressive faces or pictures and the participant classifies the central emotion.
* - Numerical Flanker

    `hedvar_eriksen_flanker__numerical_flanker`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>
  - -
  - Digits replace arrows and the participant classifies the central digit against a boundary (larger or smaller than 5) while flanking digits fall on the same or the other side.
* - Combined Flanker + Go/No-Go

    `hedvar_eriksen_flanker__combined_flanker_go_no_go`
  - response demand: <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
  - [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
  - On a minority of trials a display feature signals that no response should be made, so responding is withheld under flanker conflict.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)
- [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Eriksen, B. A., & Eriksen, C. W. (1974). Effects of noise letters upon the identification of a target letter in a nonsearch task. *Perception & Psychophysics*, 16(2), 143-149. ([DOI](https://doi.org/10.3758/bf03203267))
- Botvinick, M. M., Braver, T. S., Barch, D. M., Carter, C. S., & Cohen, J. D. (2001). Conflict monitoring and cognitive control. *Psychological Review*, 108(3), 624-652. ([DOI](https://doi.org/10.1037/0033-295x.108.3.624), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11488380/))
- Egner, T., & Hirsch, J. (2005). Cognitive control mechanisms resolve conflict through cortical amplification of task-relevant information. *Nature Neuroscience*, 8(12), 1784-1790. ([DOI](https://doi.org/10.1038/nn1594), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16286928/))

## Further references

- White, C. N., Servant, M., & Logan, G. D. (2018). Testing the validity of conflict drift-diffusion models for use in estimating cognitive processes: A parameter-recovery study. *Psychonomic Bulletin & Review*, 25(1), 323-330. ([DOI](https://doi.org/10.3758/s13423-017-1271-2))
- Ulrich, R., Schröter, H., Leuthold, H., & Birngruber, D. (2015). Automatic and controlled stimulus processing in conflict tasks: Superimposed diffusion processes and delta functions. *Cognitive Psychology*, 78, 148-174. ([DOI](https://doi.org/10.1016/j.cogpsych.2015.02.005), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25909766/))
- Servant, M., & Logan, G. D. (2019). Dynamics of attentional focusing in the Eriksen flanker task. *Attention, Perception, & Psychophysics*, 81, 2710-2721. ([DOI](https://doi.org/10.3758/s13414-019-01796-3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31250363/))
- Donner, T. H., Siegel, M., Fries, P., & Engel, A. K. (2009). Buildup of choice-predictive activity in human motor cortex during perceptual decision making. *Current Biology*, 19(18), 1581-1585. ([DOI](https://doi.org/10.1016/j.cub.2009.07.066), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19747828/))

## External links

- Cognitive Atlas: [Eriksen flanker task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949a4f)

- CogPO: [Flanker Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Flanker_Task_Paradigm)

