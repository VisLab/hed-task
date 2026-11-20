(hedtsk_stop_signal)=
# Stop-Signal Task

**HED task ID:** `hedtsk_stop_signal`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md)

**Also known as:** SST, Stop Task, Stop-Signal, Stop Signal

Choice RT task in which an occasional stop signal requires response cancellation; stop-signal reaction time (SSRT) estimates inhibitory latency.

## Description

The Stop-Signal Task measures the ability to inhibit a prepotent motor response after it has been initiated. Participants perform a primary go task (button press to go signals) but on a subset of trials, a stop signal (auditory tone or visual cue) appears after a variable delay (stop-signal delay, SSD), instructing them to cancel their response. SSD is adjusted dynamically using a staircase procedure converging on 50% inhibition probability. The key measure is stop-signal reaction time (SSRT), estimated using the race model framework, which indexes the latency of the internal inhibitory process.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **Must the player ever hold back?** <a href="vocabulary.html#rule-respond-to-rule-response-demand-cancel-on-signal">cancel on signal</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>, <a href="vocabulary.html#setting-target-probability">target probability</a>
- **Material:** A go stimulus on every trial and, on a minority of trials, a stop signal (a tone or a visual cue) after a variable delay.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. On most trials, participants make a speeded response to a go stimulus.
    2. On a minority of trials, a stop signal (tone or visual cue) appears after the go stimulus, instructing them to withhold their response.
* - **Manipulations**
  - - Stop-signal delay (SSD, adjusted by staircase)
    - Proportion of stop trials (typically 25%)
    - Go stimulus type
    - Response on signal trials (change to a different response vs. cancel)
    - Stop-signal relevance (every signal vs. only signals or responses of one kind)
    - Context cue paired with stop probability (background color)
* - **Measurements**
  - - Stop-signal reaction time (SSRT, estimated via race model)
    - Go RT
    - Probability of stopping at each SSD
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
* - Fixed SSD Procedure

    `hedvar_stop_signal__fixed_ssd_procedure`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - -
  - The stop signal comes at a few preset delays instead of a delay adjusted to the participant's performance.
* - Stop-Change Task

    `hedvar_stop_signal__stop_change`

    Cognitive Atlas: [stop-change task](https://www.cognitiveatlas.org/task/id/trm_4f2447dfa5947)
  - named form
  - [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)
  - On signal trials the planned response is cancelled and a different one made instead, a response demand the vocabulary lacks (cancel and replace rather than cancel).
* - Proactive vs. Reactive Inhibition Manipulation

    `hedvar_stop_signal__proactive_vs_reactive_inhibition_manipulation`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-demand-probability-cue">demand probability cue</a>
  - [Proactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-proactive-control)
  - A cue or block instruction announces how likely a stop signal is on coming trials, the same demand-probability cue proposed for Cued Go/No-Go.
* - Stop-Signal in Reaching/Saccade Tasks

    `hedvar_stop_signal__stop_signal_in_reaching_saccade_tasks`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-eye-tracker">eye tracker</a>
  - -
  - The response to be cancelled is an arm reach or a saccade rather than a key press; only effector and recording change.
* - Context-Dependent Stop-Signal

    `hedvar_stop_signal__context_dependent_stop_signal`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-demand-probability-cue">demand probability cue</a>
  - [Proactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-proactive-control), [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
  - A display feature such as background color is paired with a stop probability, and the participant learns the pairing rather than being told it.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)
- [Motor preparation](../processes/motor_preparation_timing_and_execution.md#hed-motor-preparation)
- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)
- [Reactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-reactive-control)

## Key references

- Logan, G. D., & Cowan, W. B. (1984). On the ability to inhibit thought and action: A theory of an act of control. *Psychological Review*, 91(3), 295-327. ([DOI](https://doi.org/10.1037/0033-295x.91.3.295))
- Aron, A. R., & Poldrack, R. A. (2006). Cortical and subcortical contributions to Stop signal response inhibition: Role of the subthalamic nucleus. *Journal of Neuroscience*, 26(9), 2424-2433. ([DOI](https://doi.org/10.1523/jneurosci.4682-05.2006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16510720/))
- Verbruggen, F., & Logan, G. D. (2008). Response inhibition in the stop-signal paradigm. *Trends in Cognitive Sciences*, 12(11), 418-424. ([DOI](https://doi.org/10.1016/j.tics.2008.07.005), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18799345/))

## Further references

- Verbruggen, F., Aron, A. R., Band, G. P., Beste, C., et al. (2019). A consensus guide to capturing the ability to inhibit actions and impulsive behaviors in the stop-signal task. *eLife*, 8, e46323. ([DOI](https://doi.org/10.7554/elife.46323), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31033438/))
- Matzke, D., Curley, S., Gong, Q., & Heathcote, A. (2019). Bayesian modeling of stop-signal reaction time distributions. *Psychological Review*, 126(5), 663-722.
- Skippen, P., Matzke, D., Heathcote, A., Fulham, W. R., Michie, P., & Karayanidis, F. (2019). Reliability of triggering inhibitory process is a better predictor of impulsivity than SSRT. *Acta Psychologica*, 192, 104-117. ([DOI](https://doi.org/10.1016/j.actpsy.2018.10.016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30469044/))
- Bissett, P. G., Hagen, M. P., Jones, H. M., & Poldrack, R. A. (2021). Design issues and solutions for stop-signal data from the Adolescent Brain Cognitive Development (ABCD) study. *eLife*, 10, e60185. ([DOI](https://doi.org/10.7554/elife.60185), [PubMed](https://pubmed.ncbi.nlm.nih.gov/33661097/))

## External links

- Cognitive Atlas: [stop signal task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949e1a)

- CogPO: [Go/No-Go Paradigm](http://www.wiki.cogpo.org/index.php?title=Go%2FNo-Go_Paradigm) (close match)

