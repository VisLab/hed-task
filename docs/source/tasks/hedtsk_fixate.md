(hedtsk_fixate)=
# Fixate Task

**HED task ID:** `hedtsk_fixate`

**Family:** [Pseudo tasks: rest, fixation, self-report and feedback blocks](families/pseudo_tasks.md)

:::{note}
**Pseudo task.** A block that establishes or holds a state, collects a self-report or
delivers feedback, rather than eliciting a cognitive process through a trial structure. It is in the Catalog
so that such blocks can be labelled with the same vocabulary as the tasks around them.
See [Pseudo tasks](../methods/task_criteria/01_task_selection_criteria.md#task-criteria-1-3) in the task criteria.
:::

**Also known as:** Fixation Block, Fixation Baseline, Central Fixation

Participant holds gaze on a fixation target for a block with nothing else to process or do; used as a baseline or control block and to limit eye movement.

## Description

A fixation target, usually a cross or dot at the centre of the screen, is shown and the participant is instructed to keep looking at it for the duration of the block. Nothing else is presented and no response is made. Fixation blocks serve as the implicit baseline in block-design fMRI, as the inter-block interval in many EEG designs, and as the control condition for localizers. Gaze may be monitored with an eye tracker, but that is a matter of measurement and does not make a different task. The distinction from an eyes-open Rest Task is the instruction: here fixation is the required activity, not a convenience. Fixate is a pseudo task: it holds a state rather than eliciting a process, so it carries no process links.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participant maintains gaze on a fixation target for the block, with no other stimulus to process and no response to make.
* - **Manipulations**
  - - Block duration
    - Target form and size
    - Background (blank, static scene)
    - Whether gaze is monitored and fed back
* - **Measurements**
  - - Baseline neural activity for contrast with task blocks
    - Fixation stability (gaze dispersion, saccade and blink counts) when eye-tracked
```

## Cognitive processes

No process links have been recorded for this pseudo task. That is a gap in the Catalog, not a
claim that the block engages no process: a pseudo task is not run to probe a process, and the
processes it does engage have not yet been linked.

## Further references

- Stark, C. E. L., & Squire, L. R. (2001). When zero is not zero: The problem of ambiguous baseline conditions in fMRI. *Proceedings of the National Academy of Sciences*, 98(22), 12760-12766. ([DOI](https://doi.org/10.1073/pnas.221462998))

## External links

- CogPO: [Fixation Paradigm](http://www.wiki.cogpo.org/index.php?title=Fixation_Paradigm)

