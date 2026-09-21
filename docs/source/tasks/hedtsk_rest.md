(hedtsk_rest)=
# Rest Task

**HED task ID:** `hedtsk_rest`

**Family:** [Pseudo tasks: rest, fixation and self-report blocks](families/pseudo_tasks.md)

:::{note}
**Pseudo task.** A block that establishes or holds a state, or collects a self-report,
rather than eliciting a cognitive process through a trial structure. It is in the Catalog
so that such blocks can be labelled with the same vocabulary as the tasks around them.
See [Pseudo tasks](../methods/task_criteria/01_task_selection_criteria.md#task-criteria-1-3) in the task criteria.
:::

**Also known as:** Resting State, Resting-State Recording, Rest Block, Baseline Rest

Participant stays awake, still and unoccupied for a block of several minutes while spontaneous activity is recorded; the block is a baseline for task blocks or a resting-state recording in its own right.

## Description

The participant is asked to remain awake and relaxed, to keep still, and to do nothing in particular while the recording runs, typically for three to ten minutes. No stimulus is presented for processing and no response is required. Rest blocks appear at the start or end of a session as a baseline, between task blocks as a recovery period, or as the whole recording in resting-state studies of spontaneous brain activity and functional connectivity. Eye state is the standard manipulation: eyes closed removes visual input and raises occipital alpha; eyes open is often paired with a fixation cross to limit eye movement. When a cross is merely provided and the instruction is to rest, the block is a Rest Task; when the instruction is to hold gaze on the target and gaze is monitored or required, it is a Fixate Task. Rest is a pseudo task: it establishes a state rather than eliciting a process, so it carries no process links.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participant remains awake, still and relaxed with no stimulus to process and no response to make, for a block typically lasting 3 to 10 minutes.
* - **Manipulation**
  - Eye state (open or closed); block duration; position relative to task blocks (before, between, after); instruction to let the mind wander versus to stay alert.
* - **Measurement**
  - Spontaneous EEG or MEG spectra and microstates; resting-state fMRI connectivity; heart rate and respiration; self-reported drowsiness or thought content after the block. No behavioral performance measure.
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
* - Eyes-Open Rest

    `hedvar_rest__eyes_open_rest`
  - Rest with eyes open, usually with a fixation cross or a blank screen.
  - Eye state changes visual input and the EEG alpha rhythm; a different postural state for the whole block
* - Eyes-Closed Rest

    `hedvar_rest__eyes_closed_rest`
  - Rest with eyes closed.
  - Eye state changes visual input and the EEG alpha rhythm; removes eye-movement artifact and raises the risk of drowsiness
```

## Cognitive processes

None by design. A pseudo task sets up or holds a state rather than probing a process;
the processes engaged during the block are whatever the participant brings to it.

## Key references

- Biswal, B., Yetkin, F. Z., Haughton, V. M., & Hyde, J. S. (1995). Functional connectivity in the motor cortex of resting human brain using echo-planar MRI. *Magnetic Resonance in Medicine*, 34(4), 537-541. ([DOI](https://doi.org/10.1002/mrm.1910340409))
- Raichle, M. E., MacLeod, A. M., Snyder, A. Z., Powers, W. J., Gusnard, D. A., & Shulman, G. L. (2001). A default mode of brain function. *Proceedings of the National Academy of Sciences*, 98(2), 676-682. ([DOI](https://doi.org/10.1073/pnas.98.2.676))

## Further references

- Barry, R. J., Clarke, A. R., Johnstone, S. J., Magee, C. A., & Rushby, J. A. (2007). EEG differences between eyes-closed and eyes-open resting conditions. *Clinical Neurophysiology*, 118(12), 2765-2773. ([DOI](https://doi.org/10.1016/j.clinph.2007.07.028))

