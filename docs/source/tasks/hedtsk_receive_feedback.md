(hedtsk_receive_feedback)=
# Receive Feedback Task

**HED task ID:** `hedtsk_receive_feedback`

**Family:** [Pseudo tasks: rest, fixation, self-report and feedback blocks](families/pseudo_tasks.md)

:::{note}
**Pseudo task.** A block that establishes or holds a state, collects a self-report or
delivers feedback, rather than eliciting a cognitive process through a trial structure. It is in the Catalog
so that such blocks can be labelled with the same vocabulary as the tasks around them.
See [Pseudo tasks](../methods/task_criteria/01_task_selection_criteria.md#task-criteria-1-3) in the task criteria.
:::

**Also known as:** Feedback Block, Performance Feedback, Trial Feedback, Score Screen

Participant is told whether a response was right or wrong, how fast it was, or what was earned, after a response, a block or a session; feedback is a pseudo task when it accompanies a task incidentally, and part of the task itself when the task is built on it.

## Description

Feedback is information given to the participant about their own performance or its outcome: correct or incorrect, a reaction time, a score, points or money earned, a rank, or a qualitative message. It appears in nearly every experiment, delivered on screen, by sound or by the experimenter, and it does several things at once. It carries information, letting the participant detect errors and adjust strategy; it carries valence, engaging reward processing and motivation; it supports metacognition, letting participants calibrate their confidence against their actual accuracy; and negative or corrective feedback recruits performance monitoring and cognitive control. When feedback is delivered matters as much as what it says. Trial-by-trial feedback, given immediately after each response, speeds error correction and acquisition but can leave the participant dependent on the external signal, so that performance drops when it is withdrawn; summary feedback, aggregated over a block and given at its end, shows systematic bias rather than trial noise and demands self-assessment in the meantime, which favours retention and transfer. Which schedule is better depends on task difficulty: immediate feedback helps most early in a complex task, summary feedback in a simple one. Receive Feedback is a pseudo task because feedback usually accompanies a task rather than constituting one. The line the Catalog draws is whether the feedback is essential to the task. Where the task is built on it, as in reinforcement learning, reversal learning, gambling and conditioning paradigms, where the outcome of each choice is the signal the participant learns from, the feedback is part of that task's procedure and is described there. Where feedback merely accompanies the task, telling the participant how they are doing in a paradigm that would be the same task without it, it is labelled with this pseudo task, whatever its schedule; the schedule, content and valence are parameters of the feedback, recorded as manipulations. The processes feedback engages, among them reward prediction error, error detection and metacognitive monitoring, are in the Catalog; pseudo tasks have not yet been given process links.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participant receives information about the correctness, speed or outcome of their own performance, after a response, a block or a session, in a task that would be the same task without it.
    2. No task response to the feedback is required beyond acknowledging it.
* - **Manipulations**
  - - Schedule (after each response, after a block, at the end of a session; immediate or delayed)
    - Content (correct/incorrect, reaction time, score, points, money, rank, message)
    - Valence (positive, negative, neutral)
    - Modality (visual, auditory, spoken by the experimenter)
    - Whether the feedback is accurate or manipulated
* - **Measurements**
  - - Feedback-locked physiological responses (feedback-related potentials, skin conductance, heart rate)
    - Changes in accuracy, speed or strategy on the trials that follow
    - Self-reported motivation, affect or confidence. Where these are the study's object, the feedback is essential and the experiment is an instance of the task built on it, not of this pseudo task
```

## Cognitive processes

No process links have been recorded for this pseudo task. That is a gap in the Catalog, not a
claim that the block engages no process: a pseudo task is not run to probe a process, and the
processes it does engage have not yet been linked.

