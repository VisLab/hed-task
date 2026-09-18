(hedtsk_delayed_match_to_sample)=
# Delayed Match-to-Sample Task

**HED Task ID:** `hedtsk_delayed_match_to_sample`

**Also known as:** DMTS, DMS

Sample stimulus followed by a delay and then a probe or choice array; response indicates whether the probe matches the sample. Indexes short-term memory maintenance.

## Description

The Delayed Match-to-Sample (DMTS) task consists of three phases: sample, delay, and choice. During the sample phase, a stimulus is presented. Following a delay period (0-30 seconds), the participant must identify which of several test stimuli matches the original sample. Memory demands are manipulated by varying delay duration or the number of choice alternatives. The task has been fundamental in primate neuroscience for identifying the neural substrates of working memory, particularly delay-period persistent activity in prefrontal cortex.

## Inclusion test

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A sample stimulus is presented, followed by a retention interval (delay), then a test stimulus; participants indicate whether the test matches the sample.
* - **Manipulation**
  - Delay duration; sample complexity; number of test alternatives; interference during delay.
* - **Measurement**
  - Accuracy (proportion correct); RT; decay function across delay intervals.
```

## Variations

```{list-table}
:widths: 25 40 35
:header-rows: 1

* - Variation
  - Description
  - Justification
* - Standard DMTS
  - Single sample → delay → two-choice test (match vs. non-match).
  - Canonical: sample presented, delay, then match from array
* - Variable Delay DMTS
  - Delay ranging from 0 to 30 seconds; maps forgetting function.
  - Systematically varies delay length; tests forgetting function
* - Multi-Choice DMTS
  - More than two choice alternatives; increases memory precision demands.
  - More than two choices at test; increases decision complexity
* - DMTS with Distraction During Delay
  - Irrelevant stimuli during retention; measures interference resistance.
  - Interfering stimuli during retention interval; changes delay period structure
* - Spatial DMTS
  - Location-based matching rather than object-based.
  - Location rather than identity must be matched; different memory dimension
* - DMTS with Object Complexity Manipulation
  - Simple colors vs. complex patterns; manipulates encoding demands.
  - Varies object complexity; tests encoding difficulty directly
* - Delayed Non-Match-to-Sample (DNMS)
  - Select the novel stimulus; used extensively in primate lesion studies.
  - Respond to non-matching item; opposite stimulus-response mapping
```

## Cognitive processes

This task engages the following cognitive processes:

- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory)

## Key references

- Fuster, J. M., & Alexander, G. E. (1971). Neuron activity related to short-term memory. *Science*, 173(3997), 652-654.
- Miller, E. K., Erickson, C. A., & Desimone, R. (1996). Neural mechanisms of visual working memory in prefrontal cortex of the macaque. *Journal of Neuroscience*, 16(16), 5154-5167.
- Pessoa, L., Gutierrez, E., Bandettini, P. A., & Ungerleider, L. G. (2002). Neural correlates of visual working memory: fMRI amplitude predicts task performance. *Neuron*, 35(5), 975-987.

## Recent references

- Lara, A. H., & Wallis, J. D. (2015). The role of prefrontal cortex in working memory: A mini review. *Frontiers in Systems Neuroscience*, 9, 173.
- Constantinidis, C., Funahashi, S., Lee, D., Murray, J. D., Qi, X. L., Wang, M., & Arnsten, A. F. T. (2018). Persistent spiking activity underlies working memory. *Journal of Neuroscience*, 38(32), 7020–7028.
- Lundqvist, M., Herman, P., & Miller, E. K. (2018). Working memory: Delay activity, yes! Persistent activity? Maybe not. *Journal of Neuroscience*, 38(32), 7013–7019.
- Stokes, M. G. (2015). 'Activity-silent' working memory in prefrontal cortex: A dynamic coding framework. *Trends in Cognitive Sciences*, 19(7), 394–405.

## External links

- Cognitive Atlas: [delayed match to sample task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb9499e3)

