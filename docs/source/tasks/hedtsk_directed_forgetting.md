(hedtsk_directed_forgetting)=
# Directed Forgetting Task

**HED task ID:** `hedtsk_directed_forgetting`

**Family:** [Memory control and prospective memory tasks](families/memory_control.md)

**Also known as:** DF Task, Item-Method DF, List-Method DF

Study-phase cues instruct participants to remember or forget specific items or lists; later memory tests index intentional forgetting.

## Description

Participants study items (typically words) under instructions that each item should either be remembered or forgotten. In the item method, a remember or forget cue follows each individual item. In the list method, a single cue midway through the study phase instructs participants to forget everything studied so far. On a subsequent memory test, recall and recognition of forget-cued items is impaired relative to remember-cued items. The paradigm provides the primary laboratory tool for studying intentional forgetting and memory control, with theoretical implications for understanding inhibitory control over memory, context change, and selective rehearsal.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">Study, then be tested</a> (`study_then_test`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is the player told to remember?* <a href="vocabulary.html#rule-study-then-test-study-instruction-remember-or-forget-by-cue">remember or forget by cue</a>
  - *What form does the test take?* <a href="vocabulary.html#rule-study-then-test-test-form-free-recall">free recall</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-retention-interval">retention interval</a>
- **Material:** Lists of words, each word (or the list) followed by a cue to remember or to forget it.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Items are presented one at a time or in lists.
    2. After each item (item method) or after a full list (list method), a cue instructs the participant to remember or forget it.
    3. A final test probes all items.
    4. Optional: The final test is old/new recognition among new words rather than free recall.
    5. Optional: At test the participant also says which cue each recognized word received or which list it came from.
* - **Manipulations**
  - - Remember vs. forget cues
    - Item vs. list method
    - Retention interval
    - Item type (words, pictures, emotional content)
    - Study task (performing the action vs. reading the phrase)
* - **Measurements**
  - - Recall/recognition accuracy for remember-cued vs. forget-cued items
    - Directed forgetting effect (remember advantage)
    - Intrusion of forget items
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
* - List-Method Directed Forgetting

    `hedvar_directed_forgetting__list_method_directed_forgetting`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - The cue comes once after a whole first list instead of after each item, a second list is studied, and the final test covers both lists.
* - Recognition vs. Recall Test

    `hedvar_directed_forgetting__recognition_vs_recall`
  - test form: <a href="vocabulary.html#rule-study-then-test-test-form-old-new">old new</a>
  - [Recognition](../processes/long_term_memory.md#hed-recognition)
  - The final test is old/new recognition among new words rather than free recall.
* - Directed Forgetting with Source Memory

    `hedvar_directed_forgetting__directed_forgetting_with_source_memory`
  - test form: <a href="vocabulary.html#rule-study-then-test-test-form-source-attribution">source attribution</a>
  - [Source memory](../processes/long_term_memory.md#hed-source-memory)
  - At test the participant also says which cue each recognized word received or which list it came from, so the test is a source judgment rather than plain recall.
* - Emotional Directed Forgetting

    `hedvar_directed_forgetting__emotional_directed_forgetting`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - -
  - Emotional words or pictures are studied alongside neutral ones and the forgetting effect is compared across valence.
* - Directed Forgetting of Actions (SPT)

    `hedvar_directed_forgetting__directed_forgetting_of_actions_spt`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-text">text</a>, <a href="vocabulary.html#facet-stimulus-type-real-objects">real objects</a>
  - -
  - The items are action phrases that the participant performs with real objects at study, before each is cued to be remembered or forgotten, instead of only reading them.
* - Cumulative Directed Forgetting

    `hedvar_directed_forgetting__cumulative_directed_forgetting`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - Several lists are studied in a row, each followed by its own remember or forget cue, before one final test.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Directed forgetting](../processes/long_term_memory.md#hed-directed-forgetting)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Metacognitive control](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-control)

## Key references

- Bjork, R. A. (1970). Positive forgetting: The noninterference of items intentionally forgotten. *Journal of Verbal Learning and Verbal Behavior*, 9(3), 255-268. ([DOI](https://doi.org/10.1016/s0022-5371(70)80059-7))

## Further references

- Anderson, M. C., & Hanslmayr, S. (2014). Neural mechanisms of motivated forgetting. *Trends in Cognitive Sciences*, 18(6), 279-292. ([DOI](https://doi.org/10.1016/j.tics.2014.03.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24747000/))
- Pastötter, B., & Bäuml, K.-H. T. (2014). Distinct slow and fast cortical theta dynamics in episodic memory retrieval. *NeuroImage*, 94, 155-161. ([DOI](https://doi.org/10.1016/j.neuroimage.2014.03.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24632089/))
- Sahakyan, L., Delaney, P. F., Foster, N. L., & Abushanab, B. (2013). List-method directed forgetting in cognitive and clinical research: A theoretical and methodological review. *Psychology of Learning and Motivation*, 59, 131-189. ([DOI](https://doi.org/10.1016/b978-0-12-407187-2.00004-6))
- Fellner, M.-C., Waldhauser, G. T., & Axmacher, N. (2020). Tracking selective rehearsal and active inhibition of memory traces in directed forgetting. *Current Biology*, 30(13), 2638-2644. ([DOI](https://doi.org/10.1016/j.cub.2020.04.091), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32442462/))

## External links

- Cognitive Atlas: [directed forgetting task](https://www.cognitiveatlas.org/task/id/trm_4da87f383435b)

