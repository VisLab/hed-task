(hedtsk_task_switching)=
# Task Switching Task

**HED task ID:** `hedtsk_task_switching`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** Set Shifting, Alternating Runs

Alternation between two or more simple tasks on cue; switch-cost RT and errors index task-set reconfiguration.

## Description

Task Switching paradigms measure cognitive flexibility by requiring participants to alternate between two or more classification tasks. Participants view stimuli (e.g., bivalent alphanumeric characters like "G3") and perform different classifications depending on a task cue (letter: vowel/consonant; digit: odd/even). Tasks alternate in predictable sequences (e.g., AABB) or are cued on each trial. The primary measures are switch costs (increased RT and errors when switching tasks vs. repeating the same task) and mixing costs (increased RT in mixed-task blocks vs. single-task blocks). Switch costs reflect the time for task-set reconfiguration.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-previous-rule">previous rule</a>
  - *Does a cue come before the target?* <a href="vocabulary.html#rule-respond-to-rule-cue-rule-cue">rule cue</a>
  - *Does the rule change during play?* <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** Bivalent characters such as a letter-digit pair (G3), classified by the letter (vowel or consonant) or the digit (odd or even) as the cue directs.

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
    - Task sequence (random cued, predictable alternating runs, voluntary choice)
    - Block type (pure vs. mixed)
    - Response-stimulus interval
    - Stimulus type (univalent vs. bivalent)
    - Added conflict from an irrelevant stimulus dimension
* - **Measurements**
  - - Switch cost (switch - repeat RT and accuracy)
    - Mixing cost (mixed block - pure block)
    - Preparation effect (switch cost reduction with longer CSI)
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
* - Alternating Runs (AABB)

    `hedvar_task_switching__alternating_runs_aabb`

    Cognitive Atlas: [alternating runs paradigm](https://www.cognitiveatlas.org/task/id/trm_4da88b8b60ffb)
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-none">none</a>
  - -
  - No cue is given; the task changes on a fixed, known schedule (two trials of each), often marked by the stimulus stepping around a grid, and the participant must keep track.
* - Voluntary Task Switching

    `hedvar_task_switching__voluntary_task_switching`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-none">none</a>
  - -
  - The participant chooses which task to do on each trial, with no cue, and is asked to use both about equally often and in a random order.
* - Mixing Cost Paradigm

    `hedvar_task_switching__mixing_cost_paradigm`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>; rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-fixed">fixed</a>
  - -
  - Pure blocks in which the rule never changes are added and compared with the mixed blocks of the standard form.
* - Univalent vs. Bivalent Stimuli

    `hedvar_task_switching__univalent_vs_bivalent_stimuli`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-none">none</a>
  - -
  - Stimuli that afford only one of the rules (letters only, digits only) are compared with the standard bivalent stimuli that afford both, which removes the previous rule as a competitor in the univalent condition.
* - Predictable vs. Random Task Sequences

    `hedvar_task_switching__predictable_vs_random_task_sequences`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-none">none</a>
  - -
  - A fixed, known order of tasks with no cue is compared with the standard random, cued order.
* - Task Switching with Conflict

    `hedvar_task_switching__task_switching_with_conflict`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-irrelevant-dimension">irrelevant dimension</a>
  - [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
  - The stimuli are built as Stroop or flanker items, so an irrelevant dimension competes with the response as well as the previous task's rule.
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

