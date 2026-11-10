(hedtsk_prospective_memory)=
# Prospective Memory Task

**HED task ID:** `hedtsk_prospective_memory`

**Family:** [Memory control and prospective memory tasks](families/memory_control.md)

**Also known as:** Event-Based Prospective Memory, Time-Based Prospective Memory, PM Task, Einstein-McDaniel Paradigm, PMTASK

Participants perform an ongoing task while remembering to execute a deferred intention when a target event occurs (event-based) or after a time interval (time-based); PM hit rate indexes the ability to remember to remember.

## Description

Prospective memory (PM) is the ability to remember to carry out an intended action in the future. In the standard Einstein-McDaniel paradigm, participants perform a continuous ongoing task (e.g., pleasantness rating, lexical decision) while simultaneously holding the intention to execute a secondary action when a specific cue appears (event-based PM: e.g., press a key when an animal word appears) or after a fixed time interval (time-based PM: e.g., press a key every 2 minutes). The critical measure is whether the participant detects the PM cue and executes the intended action. PM is theoretically distinct from retrospective memory: the challenge is not remembering the content of the intention but spontaneously retrieving it at the right moment without an external prompt. The multiprocess framework (McDaniel & Einstein, 2000) proposes that PM retrieval can be supported by automatic, reflexive-associative processes or by resource-demanding strategic monitoring, depending on cue focality, ongoing-task absorption, and individual differences. PM failures are a leading cause of real-world memory complaints and are sensitive to aging, traumatic brain injury, ADHD, and schizophrenia.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participant performs a continuous ongoing task while holding a delayed intention.
    2. On designated trials (event cue) or at designated times (time cue), the participant must interrupt the ongoing task to execute the prospective action.
* - **Manipulations**
  - - PM cue type (event-based vs. time-based)
    - Cue focality (focal cue processed as part of ongoing task vs. non-focal cue requiring monitoring)
    - Ongoing-task demand (low vs. high load)
    - PM target frequency
    - Delay between intention formation and PM window
    - Number of PM targets
* - **Measurements**
  - - PM hit rate (proportion of cues correctly detected and acted upon)
    - Ongoing-task cost (RT and accuracy difference between PM blocks and baseline blocks)
    - Time-monitoring behavior (clock-checking frequency in time-based PM)
    - False alarms to lure items
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
* - Event-Based PM (Focal Cue)

    `hedvar_prospective_memory__event_based_pm_focal_cue`
  - The participant performs an ongoing task, such as deciding whether letter strings are words, and is also asked to press a special key whenever a particular word (such as 'tiger') appears. Because the ongoing task already requires reading each word, the cue is noticed with little extra effort.
  - PM cue is focal target of ongoing task; different resource demand from non-focal
* - Event-Based PM (Non-Focal Cue)

    `hedvar_prospective_memory__event_based_pm_non_focal_cue`
  - The special key must be pressed when a word has some feature the ongoing task does not require looking at, for example when a word contains the syllable 'tor' while the participant is rating words for pleasantness. The participant must keep checking for the feature, which slows the ongoing task.
  - PM cue is non-focal; requires additional monitoring attention
* - Time-Based PM

    `hedvar_prospective_memory__time_based_pm`
  - The special response must be made at set times, for example every two minutes, with no external reminder. A clock is available but must be checked deliberately, and how often the participant checks it is recorded.
  - Time check required at specified interval; different PM cue type
* - Activity-Based PM

    `hedvar_prospective_memory__activity_based_pm`
  - The special response must be made when a particular activity ends, such as at the end of a block of trials or when a questionnaire is finished, rather than at a set time or on seeing a particular item.
  - PM intention linked to completing an activity; different cue type
* - Multiple-Intention PM

    `hedvar_prospective_memory__multiple_intention_pm`
  - The participant holds several delayed intentions at once, each triggered by a different cue and requiring a different response, so that the limits on keeping several intentions in mind can be tested.
  - Several PM intentions simultaneously maintained; different load
* - Naturalistic PM

    `hedvar_prospective_memory__naturalistic_pm`
  - The intended actions are everyday ones outside the laboratory, such as mailing a postcard on a given day, phoning at a set time, or completing errands in a virtual town, and whether they are done is recorded.
  - Real-world task context instead of lab; different ecological setting
```

## Cognitive processes

This task is designed to engage the following processes:

- [Prospective memory](../processes/long_term_memory.md#hed-prospective-memory)
- [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)

## Key references

- Einstein, G. O., & McDaniel, M. A. (1990). Normal aging and prospective memory. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 16(4), 717-726. ([DOI](https://doi.org/10.1037/0278-7393.16.4.717))
- McDaniel, M. A., & Einstein, G. O. (2000). Strategic and automatic processes in prospective memory retrieval: A multiprocess framework. *Applied Cognitive Psychology*, 14(7), S127-S144. ([DOI](https://doi.org/10.1002/acp.775))
- Smith, R. E. (2003). The cost of remembering to remember in event-based prospective memory: Investigating the capacity demands of delayed intention performance. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 29(3), 347-361. ([DOI](https://doi.org/10.1037/0278-7393.29.3.347), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12776746/))

## Further references

- Scullin, M. K., McDaniel, M. A., & Shelton, J. T. (2013). The Dynamic Multiprocess Framework: Evidence from prospective memory with contextual variability. *Cognitive Psychology*, 67(1-2), 55-71. ([DOI](https://doi.org/10.1016/j.cogpsych.2013.07.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23916951/))
- Cona, G., Scarpazza, C., Sartori, G., Moscovitch, M., & Bhisset, P. (2015). Neural bases of prospective memory: A meta-analysis and the 'Attention to Delayed Intention' (AtoDI) model. *Neuroscience & Biobehavioral Reviews*, 52, 21-37. ([DOI](https://doi.org/10.1016/j.neubiorev.2015.02.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25704073/))
- Anderson, F. T., & McDaniel, M. A. (2019). Hey buddy, why don't we take it outside: An experience sampling study of prospective memory. *Memory & Cognition*, 47(1), 47-62. ([DOI](https://doi.org/10.4324/9781351000154))

## External links

- Cognitive Atlas: [prospective memory task](https://www.cognitiveatlas.org/task/id/trm_4f244860c702c)

