(hedtsk_directed_forgetting)=
# Directed Forgetting Task

**HED task ID:** `hedtsk_directed_forgetting`

**Family:** [Memory control and prospective memory tasks](families/memory_control.md)

**Also known as:** DF Task, Item-Method DF, List-Method DF

Study-phase cues instruct participants to remember or forget specific items or lists; later memory tests index intentional forgetting.

## Description

Participants study items (typically words) under instructions that each item should either be remembered or forgotten. In the item method, a remember or forget cue follows each individual item. In the list method, a single cue midway through the study phase instructs participants to forget everything studied so far. On a subsequent memory test, recall and recognition of forget-cued items is impaired relative to remember-cued items. The paradigm provides the primary laboratory tool for studying intentional forgetting and memory control, with theoretical implications for understanding inhibitory control over memory, context change, and selective rehearsal.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Items are presented one at a time or in lists; after each item (item method) or after a full list (list method), a cue instructs the participant to remember or forget it. A final test probes all items.
* - **Manipulation**
  - Remember vs. forget cues; item vs. list method; retention interval; item type (words, pictures, emotional content).
* - **Measurement**
  - Recall/recognition accuracy for remember-cued vs. forget-cued items; directed forgetting effect (remember advantage); intrusion of forget items.
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
* - Item-Method Directed Forgetting

    `hedvar_directed_forgetting__item_method_directed_forgetting`
  - Remember/forget cue after each individual item; primarily affects encoding.
  - Forget cue follows each item; individual item suppression
* - List-Method Directed Forgetting

    `hedvar_directed_forgetting__list_method_directed_forgetting`
  - Single forget cue after the first list; affects both retrieval and encoding of second list.
  - Forget cue follows entire first list; list-level suppression
* - Recognition vs. Recall Test

    `hedvar_directed_forgetting__recognition_vs_recall`
  - Directed forgetting effects are typically larger in recall than recognition.
  - Different retrieval test changes what type of access is measured
* - Directed Forgetting with Source Memory

    `hedvar_directed_forgetting__directed_forgetting_with_source_memory`
  - Testing whether source information is forgotten alongside item information.
  - Retrieval includes source judgment; adds contextual memory component
* - Emotional Directed Forgetting

    `hedvar_directed_forgetting__emotional_directed_forgetting`
  - Emotional vs. neutral items; emotional items may resist directed forgetting.
  - Emotional to-be-forgotten material; retained per §5.1 (EMOT retired)
* - Directed Forgetting of Actions (SPT)

    `hedvar_directed_forgetting__directed_forgetting_of_actions_spt`
  - Forgetting subject-performed tasks; tests embodied memory control.
  - Subject-performed tasks as to-be-forgotten items; different encoding modality
* - Cumulative Directed Forgetting

    `hedvar_directed_forgetting__cumulative_directed_forgetting`
  - Multiple lists with forget cues; tests whether inhibition accumulates across lists.
  - Multiple forget cues accumulate across list; different suppression structure
```

## Cognitive processes

This task is designed to engage the following processes:

- [Directed forgetting](../processes/long_term_memory.md#hed-directed-forgetting)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Metacognitive control](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-control)

## Key references

- Bjork, R. A. (1970). Positive forgetting: The noninterference of items intentionally forgotten. *Journal of Verbal Learning and Verbal Behavior*, 9(3), 255–268.

## Recent references

- Anderson, M. C., & Hanslmayr, S. (2014). Neural mechanisms of motivated forgetting. *Trends in Cognitive Sciences*, 18(6), 279–292.
- Pastötter, B., & Bäuml, K.-H. T. (2014). Distinct slow and fast cortical theta dynamics in episodic memory retrieval. *NeuroImage*, 94, 155–161.
- Sahakyan, L., Delaney, P. F., Foster, N. L., & Abushanab, B. (2013). List-method directed forgetting in cognitive and clinical research: A theoretical and methodological review. *Psychology of Learning and Motivation*, 59, 131–189.
- Fellner, M.-C., Waldhauser, G. T., & Axmacher, N. (2020). Tracking selective rehearsal and active inhibition of memory traces in directed forgetting. *Current Biology*, 30(13), 2638–2644.

## External links

- Cognitive Atlas: [directed forgetting task](https://www.cognitiveatlas.org/task/id/trm_4da87f383435b)

