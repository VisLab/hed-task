(hedtsk_eriksen_flanker)=
# Eriksen Flanker Task

**HED task ID:** `hedtsk_eriksen_flanker`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Flanker, Flanker Task

A central target flanked by congruent or incongruent distractors; RT and error differences index selective attention and conflict resolution.

## Description

The Eriksen Flanker Task measures selective attention and the ability to inhibit responses to irrelevant flanking stimuli. Participants view a brief display of five items arranged horizontally, with a central target flanked by two non-target items on each side. The central target requires a specific response, while flanking items may be congruent (same response), incongruent (opposite response), or neutral. Participants respond via speeded button press while ignoring flankers. The flanker compatibility effect (slowed RT and increased errors on incongruent trials) indexes the degree of response competition and the efficiency of attentional filtering.

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
* - **Measurements**
  - - RT and accuracy
    - Congruency effect (incongruent - congruent RT)
    - Delta plots (interference across RT distribution)
    - Conflict adaptation (Gratton effect)
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
* - Arrow Flanker (Standard)

    `hedvar_eriksen_flanker__arrow_flanker_standard`
  - Five arrows appear in a row. The participant presses a left or right key for the direction of the middle arrow. The outer arrows point the same way (congruent) or the opposite way (incongruent), and responses are slower and less accurate when they conflict.
  - Canonical flanker: central arrow surrounded by congruent/incongruent arrows
* - Letter Flanker

    `hedvar_eriksen_flanker__letter_flanker`
  - The row consists of letters, and the participant presses one key for a central H and another for a central S (for example). The flanking letters belong to the same response as the center or to the other one. This is the original 1974 form of the task.
  - Letter stimuli instead of arrows; different S-R mapping and stimulus class
* - Color Flanker

    `hedvar_eriksen_flanker__color_flanker`
  - The participant responds to the color of a central patch or item while the flanking items are the same or a different color linked to the other response.
  - Color response with flanking distractors; different response dimension
* - Emotional Flanker

    `hedvar_eriksen_flanker__emotional_flanker`
  - The central item and the flankers are faces or pictures with emotional expressions. The participant classifies the central item's emotion while the flanking items show the same or a different emotion.
  - Emotional face flankers; retained per section 5.1 (EMOT retired)
* - Numerical Flanker

    `hedvar_eriksen_flanker__numerical_flanker`
  - The items are digits, and the participant judges the central digit, for example whether it is larger or smaller than 5, while flanking digits fall on the same or the other side of 5.
  - Number stimuli with magnitude response; different S-R domain
* - Proportion-Congruent Flanker

    `hedvar_eriksen_flanker__proportion_congruent_flanker`
  - The share of conflicting trials is changed between blocks, for example 80 percent congruent in one block and 20 percent in another. Conflict effects shrink when conflict is common, because the participant learns to focus more narrowly.
  - Varies ratio of congruent to incongruent trials; changes conflict adaptation context per section 5.2
* - Combined Flanker + Go/No-Go

    `hedvar_eriksen_flanker__combined_flanker_go_no_go`
  - On most trials the participant responds to the central item as usual, but on some trials a feature of the display (for example a particular color) signals that no response should be made. The task measures withholding a response under flanker conflict.
  - Integrated flanker-GNG design; targets response inhibition under conflict
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

