(hedtsk_delayed_match_to_sample)=
# Delayed Match-to-Sample Task

**HED task ID:** `hedtsk_delayed_match_to_sample`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** DMTS, DMS, Delayed Match-to-Sample

Sample stimulus followed by a delay and then a probe or choice array; response indicates whether the probe matches the sample. Indexes short-term memory maintenance.

## Description

The Delayed Match-to-Sample (DMTS) task consists of three phases: sample, delay, and choice. During the sample phase, a stimulus is presented. Following a delay period (0-30 seconds), the participant must identify which of several test stimuli matches the original sample. Memory demands are manipulated by varying delay duration or the number of choice alternatives. The task has been fundamental in primate neuroscience for identifying the neural substrates of working memory, particularly delay-period persistent activity in prefrontal cortex.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **How long is it held?** <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-forced-choice">forced choice</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-abstract-patterns">abstract patterns</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-alternatives">number of alternatives</a>, <a href="vocabulary.html#setting-retention-interval">retention interval</a>
- **Material:** A sample stimulus followed after a delay by test stimuli, one of which matches it.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A sample stimulus is presented, followed by a retention interval (delay), then a test stimulus.
    2. Participants indicate whether the test matches the sample.
* - **Manipulations**
  - - Delay duration
    - Sample complexity
    - Number of test alternatives
    - Interference during delay
    - Remembered attribute (location vs. identity)
    - Test rule (choose the non-match vs. the match)
* - **Measurements**
  - - Accuracy (proportion correct)
    - RT
    - Decay function across delay intervals
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
* - DMTS with Distraction During Delay

    `hedvar_delayed_match_to_sample__dmts_with_distraction_during_delay`
  - interval filler: <a href="vocabulary.html#rule-study-then-test-interval-filler-distraction">distraction</a>
  - -
  - Other pictures, sounds, or a brief secondary task fill the retention interval to test how well the memory withstands interference.
* - Spatial DMTS

    `hedvar_delayed_match_to_sample__spatial_dmts`
  - named form
  - [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory)
  - The sample's location rather than its identity is remembered, and after the delay the participant indicates where it was or chooses between locations.
* - DMTS with Object Complexity Manipulation

    `hedvar_delayed_match_to_sample__dmts_with_object_complexity_manipulation`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-abstract-patterns">abstract patterns</a>
  - -
  - Samples range from simple colored shapes to detailed hard-to-name patterns and accuracy is compared across complexity levels.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory)

## Key references

- Fuster, J. M., & Alexander, G. E. (1971). Neuron activity related to short-term memory. *Science*, 173(3997), 652-654. ([DOI](https://doi.org/10.1126/science.173.3997.652), [PubMed](https://pubmed.ncbi.nlm.nih.gov/4998337/))
- Miller, E. K., Erickson, C. A., & Desimone, R. (1996). Neural mechanisms of visual working memory in prefrontal cortex of the macaque. *Journal of Neuroscience*, 16(16), 5154-5167. ([DOI](https://doi.org/10.1523/jneurosci.16-16-05154.1996), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8756444/))
- Pessoa, L., Gutierrez, E., Bandettini, P. A., & Ungerleider, L. G. (2002). Neural correlates of visual working memory: fMRI amplitude predicts task performance. *Neuron*, 35(5), 975-987. ([DOI](https://doi.org/10.1016/s0896-6273(02)00817-6), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12372290/))

## Further references

- Lara, A. H., & Wallis, J. D. (2015). The role of prefrontal cortex in working memory: A mini review. *Frontiers in Systems Neuroscience*, 9, 173. ([DOI](https://doi.org/10.3389/fnsys.2015.00173), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26733825/))
- Constantinidis, C., Funahashi, S., Lee, D., Murray, J. D., Qi, X. L., Wang, M., & Arnsten, A. F. T. (2018). Persistent spiking activity underlies working memory. *Journal of Neuroscience*, 38(32), 7020-7028. ([DOI](https://doi.org/10.1523/jneurosci.2486-17.2018), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30089641/))
- Lundqvist, M., Herman, P., & Miller, E. K. (2018). Working memory: Delay activity, yes! Persistent activity? Maybe not. *Journal of Neuroscience*, 38(32), 7013-7019. ([DOI](https://doi.org/10.1523/jneurosci.2485-17.2018), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30089640/))
- Stokes, M. G. (2015). 'Activity-silent' working memory in prefrontal cortex: A dynamic coding framework. *Trends in Cognitive Sciences*, 19(7), 394-405. ([DOI](https://doi.org/10.1016/j.tics.2015.05.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26051384/))

## External links

- Cognitive Atlas: [delayed match to sample task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb9499e3)

- CogPO: [Delayed Match To Sample Paradigm](http://www.wiki.cogpo.org/index.php?title=Delayed_Match_To_Sample_Paradigm)

