(hedtsk_stop_signal)=
# Stop-Signal Task

**HED task ID:** `hedtsk_stop_signal`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md)

**Also known as:** SST, Stop Task, Stop-Signal, Stop Signal

Choice RT task in which an occasional stop signal requires response cancellation; stop-signal reaction time (SSRT) estimates inhibitory latency.

## Description

The Stop-Signal Task measures the ability to inhibit a prepotent motor response after it has been initiated. Participants perform a primary go task (button press to go signals) but on a subset of trials, a stop signal (auditory tone or visual cue) appears after a variable delay (stop-signal delay, SSD), instructing them to cancel their response. SSD is adjusted dynamically using a staircase procedure converging on 50% inhibition probability. The key measure is stop-signal reaction time (SSRT), estimated using the race model framework, which indexes the latency of the internal inhibitory process.

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
* - **Measurements**
  - - Stop-signal reaction time (SSRT, estimated via race model)
    - Go RT
    - Probability of stopping at each SSD
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
* - Standard SST with Staircase SSD

    `hedvar_stop_signal__standard_sst_with_staircase_ssd`
  - The participant makes a quick left-or-right choice to each stimulus. On about a quarter of trials a beep or visual signal follows the stimulus and the participant must try not to respond. The delay before the signal is increased after successful stops and decreased after failures so that stopping succeeds about half the time, which allows the stopping speed to be estimated.
  - Canonical adaptive stop-signal delay tracking
* - Fixed SSD Procedure

    `hedvar_stop_signal__fixed_ssd_procedure`
  - The stop signal comes at a few preset delays after the stimulus (for example 100, 200, 300 and 400 ms) rather than being adjusted to the participant. Stopping success is plotted against delay.
  - Non-adaptive fixed delays; different trial structure
* - Stop-Change Task

    `hedvar_stop_signal__stop_change`

    Cognitive Atlas: [stop-change task](https://www.cognitiveatlas.org/task/id/trm_4f2447dfa5947)
  - Instead of simply withholding, the participant must cancel the planned response and make a different one, for example pressing a third key, when the signal occurs.
  - Stop signal replaced by change signal; different inhibition-and-substitute
* - Selective Stop-Signal

    `hedvar_stop_signal__selective_stop_signal`
  - Only one of the signals, or one of the responses, requires stopping. For example, a high tone means stop but a low tone means carry on, or stopping is needed only for left-hand responses. The participant must identify the signal before deciding whether to stop.
  - Stop signal applies to one response type only; selective inhibition
* - Proactive vs. Reactive Inhibition Manipulation

    `hedvar_stop_signal__proactive_vs_reactive_inhibition_manipulation`
  - A cue or block instruction tells the participant how likely a stop signal is on coming trials (for example none, some, or many). Responses slow when stopping is likely, which shows the participant preparing to stop before any signal appears.
  - Pre-signal preparatory inhibition vs. post-signal reactive; different inhibition timing
* - Stop-Signal in Reaching/Saccade Tasks

    `hedvar_stop_signal__stop_signal_in_reaching_saccade_tasks`
  - The response to be stopped is an arm reach to a target or an eye movement to a target rather than a key press, and movement or eye position is recorded to see whether the action was cancelled.
  - Arm reaching or eye movement response; different motor effector
* - Context-Dependent Stop-Signal

    `hedvar_stop_signal__context_dependent_stop_signal`
  - Features of the display or environment, such as a background color, are associated with different stop-signal probabilities, and the participant learns to adjust their readiness to stop from these features.
  - Stop signal context varies; tests context-sensitive inhibition
* - Conditional Stop-Signal

    `hedvar_stop_signal__conditional_stop_signal`
  - A stop signal always appears, but stopping is required only when it has a particular property, such as a specific color, and otherwise the response should go ahead.
  - Inhibit only under specific conditions; conditional stopping logic
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

