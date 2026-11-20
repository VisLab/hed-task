(hedtsk_sustained_attention_to_response)=
# Sustained Attention to Response Task

**HED task ID:** `hedtsk_sustained_attention_to_response`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md) (also [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md), [Spontaneous thought tasks](families/spontaneous_thought.md))

**Also known as:** SART, Sustained Attention to Response

Speeded responses to frequent non-targets with withholding on rare targets; commission errors and RT variability index sustained attention lapses.

## Description

The Sustained Attention to Response Task is a Go/No-Go variant specifically designed to measure sustained attention failures and mind-wandering. Participants respond (button press) to every digit presented (1-9) except for one designated target digit (typically "3"), to which they must withhold their response. Digits are presented at a fixed rate (e.g., every 1150 ms), and the high frequency of Go responses (89%) creates a monotonous, routinized response pattern that promotes attentional lapses. Errors of commission (responding to the No-Go target) serve as the primary index of attention failure. The SART has become the standard behavioral measure for studying mind-wandering, task-unrelated thought, and attentional lapses.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **Must the player ever hold back?** <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
- **How often is there a target?** <a href="vocabulary.html#rule-respond-to-rule-target-rate-rare-target">rare target</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-interstimulus-interval">interstimulus interval</a>, <a href="vocabulary.html#setting-number-of-targets">number of targets</a>, <a href="vocabulary.html#setting-session-duration">session duration</a>
- **Material:** Single digits 1-9 shown one at a time at a fixed rate, one of them (typically 3) the no-go target.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Single digits (1-9) are presented one at a time.
    2. Participants respond to every digit except a designated target (typically 3).
    3. The high go-probability induces a prepotent response tendency.
* - **Manipulations**
  - - Target digit identity
    - Fixed vs. random digit sequences
    - ISI
    - Session duration
    - Added thought probes during the task
    - Stimulus type (shapes, colors or oriented lines vs. digits)
    - Response rule (switching during the run vs. fixed)
    - Number of withhold items (multiple targets vs. one)
* - **Measurements**
  - - Commission errors (responses to the no-go target)
    - Omission errors
    - RT variability
    - Thought-probe responses (mind wandering frequency)
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
* - SART with Thought Probes

    `hedvar_sustained_attention_to_response__sart_with_thought_probes`
  - combined with: <a href="vocabulary.html#how-inserted">inserted</a>, <a href="vocabulary.html#game-report-on-self">report on self</a> (A thought probe interrupts the stream)
  - -
  - At unpredictable points the stream pauses and the participant reports what they were just thinking, inserting a self-report into the ongoing task.
* - Perceptual SART

    `hedvar_sustained_attention_to_response__perceptual_sart`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - -
  - Shapes, colors or oriented lines replace the digits, with one of them as the withhold item.
* - Sustained Attention Task with Response Switching

    `hedvar_sustained_attention_to_response__sustained_attention_task_with_response_switching`
  - rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>
  - [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
  - The key-press rule changes periodically during the run, so the participant tracks the current rule while still withholding on the rare item.
* - Sustained Attention with Clock Task

    `hedvar_sustained_attention_to_response__sustained_attention_with_clock`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>; response demand: <a href="vocabulary.html#rule-respond-to-rule-response-demand-always-respond">always respond</a>; stream: <a href="vocabulary.html#rule-respond-to-rule-stream-continuous">continuous</a>
  - -
  - A clock hand advances in regular jumps and the participant presses only when it double-jumps, a continuous detection task with a rare target rather than a go/no-go stream (this is the Mackworth Clock, arguably a different task listed as a variation).
* - Child-Adapted SART

    `hedvar_sustained_attention_to_response__child_adapted_sart`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; population: <a href="vocabulary.html#facet-population-children">children</a>
  - -
  - Pictures of animals or objects replace the digits and the pace is slowed for children.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Spontaneous thought](../processes/awareness_agency_and_metacognition.md#hed-mind-wandering)
- [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring)
- [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)

## Key references

- Robertson, I. H., Manly, T., Andrade, J., Baddeley, B. T., & Yiend, J. (1997). 'Oops!': Performance correlates of everyday attentional failures in traumatic brain injured and normal subjects. *Neuropsychologia*, 35(6), 747-758. ([DOI](https://doi.org/10.1016/s0028-3932(97)00015-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9204482/))
- Smallwood, J., Davies, J. B., Heim, D., Finnigan, F., Sudberry, M., O'Connor, R., & Obonsawin, M. (2004). Subjective experience and the attentional lapse: Task engagement and disengagement during sustained attention. *Consciousness and Cognition*, 13(4), 657-690. ([DOI](https://doi.org/10.1016/j.concog.2004.06.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15522626/))
- Manly, T., Robertson, I. H., Galloway, M., & Hawkins, K. (1999). The absent mind: Further investigations of sustained attention to response. *Neuropsychologia*, 37(6), 661-670. ([DOI](https://doi.org/10.1016/s0028-3932(98)00127-4), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10390027/))
- Smallwood, J., & Schooler, J. W. (2006). The restless mind. *Psychological Bulletin*, 132(6), 946-958. ([DOI](https://doi.org/10.1037/0033-2909.132.6.946), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17073528/))

## Further references

- Seli, P., Cheyne, J. A., & Smilek, D. (2013). Wandering minds and wavering rhythms: Linking mind wandering and behavioral variability. *Journal of Experimental Psychology: Human Perception and Performance*, 39(1), 1-5. ([DOI](https://doi.org/10.1037/a0030954), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23244046/))
- Head, J., & Helton, W. S. (2014). Sustained attention failures are primarily due to sustained cognitive load not task monotony. *Acta Psychologica*, 153, 87-94. ([DOI](https://doi.org/10.1016/j.actpsy.2014.09.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25310454/))
- Dockree, P. M., Kelly, S. P., Foxe, J. J., Reilly, R. B., & Robertson, I. H. (2007). Optimal sustained attention is linked to the spectral content of background EEG activity: Greater ongoing tonic alpha (~10 Hz) power supports successful phasic goal activation. *European Journal of Neuroscience*, 25(3), 900-907. ([DOI](https://doi.org/10.1111/j.1460-9568.2007.05324.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17328783/))
- McVay, J. C., & Kane, M. J. (2009). Conducting the train of thought: Working memory capacity, goal neglect, and mind wandering in an executive-control task. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 35(1), 196-204. ([DOI](https://doi.org/10.1037/a0014104), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19210090/))
- Seli, P., Risko, E. F., Smilek, D., & Schacter, D. L. (2016). Mind-wandering with and without intention. *Trends in Cognitive Sciences*, 20(8), 605-617. ([DOI](https://doi.org/10.1016/j.tics.2016.05.010), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27318437/))
- Fortenbaugh, F. C., DeGutis, J., & Esterman, M. (2017). Recent theoretical, neural, and clinical advances in sustained attention research. *Annals of the New York Academy of Sciences*, 1396(1), 70-91. ([DOI](https://doi.org/10.1111/nyas.13318), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28260249/))

## External links

- Cognitive Atlas: [sustained attention to response task](https://www.cognitiveatlas.org/task/id/trm_4da86cfe8cf1b)

- CogPO: [Go/No-Go Paradigm](http://www.wiki.cogpo.org/index.php?title=Go%2FNo-Go_Paradigm) (close match)

