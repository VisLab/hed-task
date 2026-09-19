(hedtsk_sustained_attention_to_response)=
# Sustained Attention to Response Task

**HED task ID:** `hedtsk_sustained_attention_to_response`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md)

**Also known as:** SART, Sustained Attention to Response

Speeded responses to frequent non-targets with withholding on rare targets; commission errors and RT variability index sustained attention lapses.

## Description

The Sustained Attention to Response Task is a Go/No-Go variant specifically designed to measure sustained attention failures and mind-wandering. Participants respond (button press) to every digit presented (1–9) except for one designated target digit (typically "3"), to which they must withhold their response. Digits are presented at a fixed rate (e.g., every 1150 ms), and the high frequency of Go responses (89%) creates a monotonous, routinized response pattern that promotes attentional lapses. Errors of commission (responding to the No-Go target) serve as the primary index of attention failure. The SART has become the standard behavioral measure for studying mind-wandering, task-unrelated thought, and attentional lapses.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Single digits (1–9) are presented one at a time; participants respond to every digit except a designated target (typically 3). The high go-probability induces a prepotent response tendency.
* - **Manipulation**
  - Target digit identity; fixed vs. random digit sequences; ISI; session duration.
* - **Measurement**
  - Commission errors (responses to the no-go target); omission errors; RT variability; thought-probe responses (mind wandering frequency).
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
* - Standard SART (Fixed Sequence)

    `hedvar_sustained_attention_to_response__standard_sart_fixed_sequence`
  - Digits 1-9 repeated in a fixed order; No-Go to "3."
  - Canonical: respond to digits except 3; fixed pseudo-random sequence
* - Random SART

    `hedvar_sustained_attention_to_response__random_sart`
  - Digits presented in random order; eliminates predictability.
  - Random digit order; removes sequential predictability
* - SART with Thought Probes

    `hedvar_sustained_attention_to_response__sart_with_thought_probes`
  - Intermittent probes asking "Were you on-task or mind-wandering?"
  - Mind-wandering probes inserted; adds metacognitive reporting
* - Perceptual SART

    `hedvar_sustained_attention_to_response__perceptual_sart`
  - Non-digit stimuli (shapes, colors) for populations where digit recognition varies.
  - Perceptual variants (lines, shapes); different stimulus type
* - Sustained Attention Task with Response Switching

    `hedvar_sustained_attention_to_response__sustained_attention_task_with_response_switching`
  - Alternating response keys to add task-switching demands.
  - Response switches during task; adds rule-change demand
* - SART with Multiple Targets

    `hedvar_sustained_attention_to_response__sart_with_multiple_targets`
  - Two or more target digits to vary no-go probability.
  - Multiple no-go digits instead of one; different inhibition load
* - Sustained Attention with Clock Task

    `hedvar_sustained_attention_to_response__sustained_attention_with_clock`
  - Mackworth Clock Test variant; watching a clock hand for occasional double jumps over extended periods.
  - Clock face rather than digit sequence; different stimulus format
* - Child-Adapted SART

    `hedvar_sustained_attention_to_response__child_adapted_sart`
  - Pictorial stimuli (animals, objects) replacing digits for developmental populations.
  - Modified timing and stimuli for children; adapted per §5.3
```

## Cognitive processes

This task is designed to engage the following processes:

- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Mind wandering](../processes/awareness_agency_and_metacognition.md#hed-mind-wandering)
- [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring)
- [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)

## Key references

- Robertson, I. H., Manly, T., Andrade, J., Baddeley, B. T., & Yiend, J. (1997). 'Oops!': Performance correlates of everyday attentional failures in traumatic brain injured and normal subjects. *Neuropsychologia*, 35(6), 747–758. ([DOI](https://doi.org/10.1016/s0028-3932(97)00015-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9204482/))
- Smallwood, J., Davies, J. B., Heim, D., Finnigan, F., Sudberry, M., O'Connor, R., & Obonsawin, M. (2004). Subjective experience and the attentional lapse: Task engagement and disengagement during sustained attention. *Consciousness and Cognition*, 13(4), 657–690. ([DOI](https://doi.org/10.1016/j.concog.2004.06.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15522626/))
- Manly, T., Robertson, I. H., Galloway, M., & Hawkins, K. (1999). The absent mind: Further investigations of sustained attention to response. *Neuropsychologia*, 37(6), 661–670. ([DOI](https://doi.org/10.1016/s0028-3932(98)00127-4), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10390027/))
- Smallwood, J., & Schooler, J. W. (2006). The restless mind. *Psychological Bulletin*, 132(6), 946–958. ([DOI](https://doi.org/10.1037/0033-2909.132.6.946), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17073528/))

## Further references

- Seli, P., Cheyne, J. A., & Smilek, D. (2013). Wandering minds and wavering rhythms: Linking mind wandering and behavioral variability. *Journal of Experimental Psychology: Human Perception and Performance*, 39(1), 1–5. ([DOI](https://doi.org/10.1037/a0030954), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23244046/))
- Head, J., & Helton, W. S. (2014). Sustained attention failures are primarily due to sustained cognitive load not task monotony. *Acta Psychologica*, 153, 87–94. ([DOI](https://doi.org/10.1016/j.actpsy.2014.09.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25310454/))
- Dockree, P. M., Kelly, S. P., Foxe, J. J., Reilly, R. B., & Robertson, I. H. (2007). Optimal sustained attention is linked to the spectral content of background EEG activity: Greater ongoing tonic alpha (~10 Hz) power supports successful phasic goal activation. *European Journal of Neuroscience*, 25(3), 900–907. ([DOI](https://doi.org/10.1111/j.1460-9568.2007.05324.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17328783/))
- McVay, J. C., & Kane, M. J. (2009). Conducting the train of thought: Working memory capacity, goal neglect, and mind wandering in an executive-control task. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 35(1), 196–204. ([DOI](https://doi.org/10.1037/a0014104), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19210090/))
- Seli, P., Risko, E. F., Smilek, D., & Schacter, D. L. (2016). Mind-wandering with and without intention. *Trends in Cognitive Sciences*, 20(8), 605–617. ([DOI](https://doi.org/10.1016/j.tics.2016.05.010), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27318437/))
- Fortenbaugh, F. C., DeGutis, J., & Esterman, M. (2017). Recent theoretical, neural, and clinical advances in sustained attention research. *Annals of the New York Academy of Sciences*, 1396(1), 70–91. ([DOI](https://doi.org/10.1111/nyas.13318), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28260249/))

## External links

- Cognitive Atlas: [sustained attention to response task](https://www.cognitiveatlas.org/task/id/trm_4da86cfe8cf1b)

