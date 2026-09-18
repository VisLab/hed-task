(hedtsk_stop_signal)=
# Stop-Signal Task

**HED Task ID:** `hedtsk_stop_signal`

**Also known as:** SST, Stop Task

Choice RT task in which an occasional stop signal requires response cancellation; stop-signal reaction time (SSRT) estimates inhibitory latency.

## Description

The Stop-Signal Task measures the ability to inhibit a prepotent motor response after it has been initiated. Participants perform a primary go task (button press to go signals) but on a subset of trials, a stop signal (auditory tone or visual cue) appears after a variable delay (stop-signal delay, SSD), instructing them to cancel their response. SSD is adjusted dynamically using a staircase procedure converging on 50% inhibition probability. The key measure is stop-signal reaction time (SSRT), estimated using the race model framework, which indexes the latency of the internal inhibitory process.

## Inclusion test

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - On most trials, participants make a speeded response to a go stimulus. On a minority of trials, a stop signal (tone or visual cue) appears after the go stimulus, instructing them to withhold their response.
* - **Manipulation**
  - Stop-signal delay (SSD, adjusted by staircase); proportion of stop trials (typically 25%); go stimulus type.
* - **Measurement**
  - Stop-signal reaction time (SSRT, estimated via race model); go RT; probability of stopping at each SSD.
```

## Variations

```{list-table}
:widths: 25 40 35
:header-rows: 1

* - Variation
  - Description
  - Justification
* - Standard SST with Staircase SSD
  - Dynamic SSD adjustment converging on 50% inhibition probability; yields SSRT via race model.
  - Canonical adaptive stop-signal delay tracking
* - Fixed SSD Procedure
  - Predetermined SSDs; simpler but less efficient for SSRT estimation.
  - Non-adaptive fixed delays; different trial structure
* - Stop-Change Task
  - Stop signal requires switching to alternative response rather than pure inhibition.
  - Stop signal replaced by change signal; different inhibition-and-substitute
* - Selective Stop-Signal
  - Stop signal applies to only one of multiple possible responses; probes response-specific inhibition.
  - Stop signal applies to one response type only; selective inhibition
* - Proactive vs. Reactive Inhibition Manipulation
  - Varying stop-signal probability across blocks to separate anticipatory from stimulus-triggered control.
  - Pre-signal preparatory inhibition vs. post-signal reactive; different inhibition timing
* - Stop-Signal in Reaching/Saccade Tasks
  - Non-button-press responses; extends to oculomotor and reaching domains.
  - Arm reaching or eye movement response; different motor effector
* - Context-Dependent Stop-Signal
  - Environmental context predicts stop-signal probability.
  - Stop signal context varies; tests context-sensitive inhibition
* - Conditional Stop-Signal
  - Stop signal presented but inhibition required only under certain conditions (e.g., specific signal color).
  - Inhibit only under specific conditions; conditional stopping logic
```

## Cognitive processes

This task engages the following cognitive processes:

- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)
- [Motor preparation](../processes/motor_preparation_timing_and_execution.md#hed-motor-preparation)
- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)
- [Reactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-reactive-control)

## Key references

- Logan, G. D., & Cowan, W. B. (1984). On the ability to inhibit thought and action: A theory of an act of control. *Psychological Review*, 91(3), 295-327.
- Aron, A. R., & Poldrack, R. A. (2006). Cortical and subcortical contributions to Stop signal response inhibition: Role of the subthalamic nucleus. *Journal of Neuroscience*, 26(9), 2424-2433.
- Verbruggen, F., & Logan, G. D. (2008). Response inhibition in the stop-signal paradigm. *Trends in Cognitive Sciences*, 12(11), 418-424.

## Recent references

- Verbruggen, F., Aron, A. R., Band, G. P., Beste, C., et al. (2019). A consensus guide to capturing the ability to inhibit actions and impulsive behaviors in the stop-signal task. *eLife*, 8, e46323.
- Matzke, D., Curley, S., Gong, Q., & Heathcote, A. (2019). Bayesian modeling of stop-signal reaction time distributions. *Psychological Review*, 126(5), 663–722.
- Skippen, P., Matzke, D., Heathcote, A., Fulham, W. R., Michie, P., & Karayanidis, F. (2019). Reliability of triggering inhibitory process is a better predictor of impulsivity than SSRT. *Acta Psychologica*, 192, 104–117.
- Bissett, P. G., Hagen, M. P., Jones, H. M., & Poldrack, R. A. (2021). Design issues and solutions for stop-signal data from the Adolescent Brain Cognitive Development (ABCD) study. *eLife*, 10, e60185.

## External links

- Cognitive Atlas: [stop signal task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949e1a)

