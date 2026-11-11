(hedtsk_task_switching)=
# Task Switching Task

**HED task ID:** `hedtsk_task_switching`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** Set Shifting, Alternating Runs

Alternation between two or more simple tasks on cue; switch-cost RT and errors index task-set reconfiguration.

## Description

Task Switching paradigms measure cognitive flexibility by requiring participants to alternate between two or more classification tasks. Participants view stimuli (e.g., bivalent alphanumeric characters like "G3") and perform different classifications depending on a task cue (letter: vowel/consonant; digit: odd/even). Tasks alternate in predictable sequences (e.g., AABB) or are cued on each trial. The primary measures are switch costs (increased RT and errors when switching tasks vs. repeating the same task) and mixing costs (increased RT in mixed-task blocks vs. single-task blocks). Switch costs reflect the time for task-set reconfiguration.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants alternate between two (or more) simple tasks on the same stimuli, cued by an explicit cue or a predictable alternation schedule.
* - **Manipulations**
  - - Switch vs. repeat trials
    - Cue-stimulus interval (preparation time)
    - Task difficulty
    - Number of tasks
    - Cue transparency
* - **Measurements**
  - - Switch cost (switch - repeat RT and accuracy)
    - Mixing cost (mixed block - pure block)
    - Preparation effect (switch cost reduction with longer CSI)
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
* - Cued Task-Switching

    `hedvar_task_switching__cued_task_switching`
  - Each trial starts with a cue, such as a word or a colored frame, telling the participant which of two tasks to do on the coming stimulus (for example, judge a digit as odd or even, or as bigger or smaller than 5). Responses are slower when the task differs from the previous trial.
  - Canonical cue specifies task each trial
* - Alternating Runs (AABB)

    `hedvar_task_switching__alternating_runs_aabb`

    Cognitive Atlas: [alternating runs paradigm](https://www.cognitiveatlas.org/task/id/trm_4da88b8b60ffb)
  - No cue is given; instead the tasks alternate in a fixed pattern, usually two trials of one then two of the other, often with the stimulus moving around a grid to mark position in the pattern. The participant must keep track of where they are.
  - Predictable alternation without explicit cue; different task structure
* - Voluntary Task Switching

    `hedvar_task_switching__voluntary_task_switching`
  - The participant decides on each trial which task to perform, with the instruction to do both about equally often in a random order. The choice is read from which response keys are used. How often people choose to switch is measured as well as the cost.
  - Participant chooses task; measures voluntary switching rates
* - Mixing Cost Paradigm

    `hedvar_task_switching__mixing_cost_paradigm`
  - Blocks in which only one task is done are compared with blocks in which the two tasks are mixed. Even trials in the mixed blocks that repeat the task are slower than single-task trials, a cost of keeping both tasks ready.
  - Compares mixed-block to pure-block performance; different block structure
* - Cue-Stimulus Interval (CSI) Manipulation

    `hedvar_task_switching__cue_stimulus_interval_csi_manipulation`
  - The time between the cue and the stimulus is varied, from almost none to a second or more. Longer preparation time reduces the switch cost but does not remove it.
  - Varies preparation time; tests proactive preparation
* - Response-Stimulus Interval (RSI) Manipulation

    `hedvar_task_switching__response_stimulus_interval_rsi_manipulation`
  - The time between one trial's response and the next trial's stimulus is varied, without changing the preparation time, to see how the previous task's influence fades on its own.
  - Varies post-response interval; tests backward inhibition decay
* - Task Switching with N>2 Tasks

    `hedvar_task_switching__task_switching_with_n_2_tasks`
  - Three or more tasks are cued. Returning to a task that was done two trials ago (A-B-A) is slower than coming to a task not done recently (C-B-A), which shows that a task is inhibited when it is abandoned.
  - Three or more tasks; different reconfiguration demands
* - Univalent vs. Bivalent Stimuli

    `hedvar_task_switching__univalent_vs_bivalent_stimuli`
  - Stimuli either allow only one of the tasks (for example letters for a letter task, digits for a digit task) or allow both (a letter and a digit together). Switch costs are larger when the stimulus could be used for either task.
  - Stimuli compatible with one vs. both tasks; different interference structure
* - Predictable vs. Random Task Sequences

    `hedvar_task_switching__predictable_vs_random_task_sequences`
  - The order of tasks is either known in advance (a fixed alternation) or random with a cue, to see how much knowing what comes next helps preparation.
  - Known vs. unknown switch sequence; tests preparation strategies
* - Task Switching with Conflict

    `hedvar_task_switching__task_switching_with_conflict`
  - The stimuli are also designed to create response conflict, for example a Stroop or flanker item, so that the cost of switching tasks and the cost of resolving conflict can be studied together.
  - Bivalent stimuli with competing responses; combined switching and conflict
```

## Cognitive processes

This task is designed to engage the following processes:

- [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
- [Goal maintenance](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-goal-maintenance)
- [Proactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-proactive-control)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Rogers, R. D., & Monsell, S. (1995). Costs of a predictable switch between simple cognitive tasks. *Journal of Experimental Psychology: General*, 124(2), 207-231. ([DOI](https://doi.org/10.1037/0096-3445.124.2.207))
- Monsell, S. (2003). Task switching. *Trends in Cognitive Sciences*, 7(3), 134-140. ([DOI](https://doi.org/10.1016/s1364-6613(03)00028-7), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12639695/))
- Braver, T. S., Reynolds, J. R., & Donaldson, D. I. (2003). Neural mechanisms of transient and sustained cognitive control during task switching. *Neuron*, 39(4), 713-726. ([DOI](https://doi.org/10.1016/s0896-6273(03)00466-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12925284/))

## Further references

- Kiesel, A., Steinhauser, M., Wendt, M., Falkenstein, M., Jost, K., Philipp, A. M., & Koch, I. (2010). Control and interference in task switching - A review. *Psychological Bulletin*, 136(5), 849-874. ([DOI](https://doi.org/10.1037/a0019842), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20804238/))
- Vandierendonck, A., Liefooghe, B., & Verbruggen, F. (2010). Task switching: Interplay of reconfiguration and interference control. *Psychological Bulletin*, 136(4), 601-626. ([DOI](https://doi.org/10.1037/a0019791), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20565170/))
- Grange, J. A., & Houghton, G. (2014). Models of cognitive control in task switching. In *Task Switching and Cognitive Control* (pp. 160-199). Oxford University Press. ([DOI](https://doi.org/10.1093/acprof:osobl/9780199921959.003.0008))
- Braem, S., & Egner, T. (2018). Getting a grip on cognitive flexibility. *Current Directions in Psychological Science*, 27(6), 470-476. ([DOI](https://doi.org/10.1177/0963721418787475), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30555214/))

## External links

- Cognitive Atlas: [task-switching ](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949e8a)

- CogPO: [Task Switching Paradigm](http://www.wiki.cogpo.org/index.php?title=Task_Switching_Paradigm)

