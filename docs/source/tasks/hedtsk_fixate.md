(hedtsk_fixate)=
# Fixate Task

**HED task ID:** `hedtsk_fixate`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md) (also [Attentional cueing and orienting tasks](families/attentional_cueing.md), [Visual search and tracking tasks](families/visual_search_and_tracking.md))

**Also known as:** Fixation Block, Fixation Baseline, Central Fixation

Participant holds gaze on a fixation target. It is used in two ways: as a block of its own with nothing else to do, as a baseline or control, and as a job held throughout another task so that the eyes stay still while that task is performed.

## Description

A fixation target, usually a cross or dot at the centre of the screen, is shown and the participant is instructed to keep looking at it for the duration of the block. Nothing else is presented and no response is made. Fixation blocks serve as the implicit baseline in block-design fMRI, as the inter-block interval in many EEG designs, and as the control condition for localizers. Gaze may be monitored with an eye tracker, but that is a matter of measurement and does not make a different task. The distinction from an eyes-open Rest Task is the instruction: here fixation is the required activity, not a convenience. Fixation is also held throughout other tasks, as in spatial cueing, where attention moves to the cued location while the eyes stay on the cross; there it is a second job done alongside the main one. In both uses the participant keeps attention on the target and holds back the urge to look away.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participant maintains gaze on a fixation target for the block, with no other stimulus to process and no response to make.
    2. Or, participant holds gaze on the target throughout the trials of another task while performing that task.
* - **Manipulations**
  - - Block duration
    - Target form and size
    - Background (blank, static scene)
    - Whether gaze is monitored and fed back
* - **Measurements**
  - - Baseline neural activity for contrast with task blocks
    - Fixation stability (gaze dispersion, saccade and blink counts) when eye-tracked
    - Fixation breaks during the other task's trials
```

## Cognitive processes

This task is designed to engage the following processes:

- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Goal maintenance](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-goal-maintenance)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)

## Further references

- Stark, C. E. L., & Squire, L. R. (2001). When zero is not zero: The problem of ambiguous baseline conditions in fMRI. *Proceedings of the National Academy of Sciences*, 98(22), 12760-12766. ([DOI](https://doi.org/10.1073/pnas.221462998))

## External links

- Cognitive Atlas: [fixation task](https://www.cognitiveatlas.org/task/id/trm_4c898f72228f3)

- CogPO: [Fixation Paradigm](http://www.wiki.cogpo.org/index.php?title=Fixation_Paradigm)

