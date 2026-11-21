(hedtsk_operation_span)=
# Operation Span Task

**HED task ID:** `hedtsk_operation_span`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** OSPAN, Complex Span, Operation Span

Alternating arithmetic verification and word/letter memory items; complex-span score indexes working memory capacity under processing load.

## Description

The Operation Span Task is a complex span measure of working memory capacity. Participants alternate between a processing task (verifying simple math equations, e.g., "Is (2 x 3) + 1 = 8?") and a memory task (remembering letters or words presented after each equation). After a set of 3-7 equation-letter pairs, participants recall the letters in order. The OSPAN score reflects the ability to maintain memory representations while engaging in concurrent processing - a hallmark of working memory capacity (WMC). OSPAN scores are strong predictors of fluid intelligence, reading comprehension, and general executive function.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">Study, then be tested</a> (`study_then_test`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is studied?* <a href="vocabulary.html#rule-study-then-test-studied-material-sequence-order">sequence order</a>
  - *How long is it held?* <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
  - *What fills the interval?* <a href="vocabulary.html#rule-study-then-test-interval-filler-distraction">distraction</a>
  - *What form does the test take?* <a href="vocabulary.html#rule-study-then-test-test-form-serial-recall">serial recall</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-set-size">set size</a>
- **Material:** Simple math equations to verify (such as (2 x 3) + 1 = 8), each followed by a letter or word to remember.
- **Combined with:** <a href="vocabulary.html#how-interleaved">interleaved</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (An equation is verified between each item to be remembered)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants alternate between processing a distractor task (verifying math equations) and remembering items (letters or words).
    2. At the end of each set, they recall items in order.
* - **Manipulations**
  - - Set size (2-7)
    - Processing task difficulty
    - Type of memoranda
    - Partial-credit vs. absolute scoring
* - **Measurements**
  - - Operation span score (items recalled in correct position)
    - Processing accuracy (to verify engagement with distractor task)
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
* - Reading Span (RSPAN)

    `hedvar_operation_span__reading_span_rspan`

    Cognitive Atlas: [reading span task](https://www.cognitiveatlas.org/task/id/trm_4c40d168898db)
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-text">text</a>
  - [Sentence comprehension](../processes/language_comprehension_and_production.md#hed-sentence-comprehension)
  - The interleaved processing task is judging whether a sentence makes sense instead of verifying an equation, with a word or letter to remember after each sentence.
* - Symmetry Span (SYMSPAN)

    `hedvar_operation_span__symmetry_span_symspan`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-abstract-patterns">abstract patterns</a>, <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory)
  - The processing task is a symmetry judgment and the memoranda are grid positions recalled in order, a spatial version of the same structure.
* - Counting Span

    `hedvar_operation_span__counting_span`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - -
  - The participant counts target shapes in each display and says the total, then recalls the totals in order, so the memoranda are the answers produced by the processing task rather than items presented separately.
* - Shortened OSPAN

    `hedvar_operation_span__shortened_ospan`
  - named form
  - -
  - A named shorter protocol with fewer sets and smaller maximum set sizes that gives similar scores in about half the time.
* - Adaptive OSPAN

    `hedvar_operation_span__adaptive_ospan`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - -
  - Set size rises after correct recall and falls after errors so that most trials fall near the participant's limit instead of running a fixed series.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory)
- [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)

## Key references

- Turner, M. L., & Engle, R. W. (1989). Is working memory capacity task dependent? *Journal of Memory and Language*, 28(2), 127-154. ([DOI](https://doi.org/10.1016/0749-596x(89)90040-5))
- Unsworth, N., Heitz, R. P., Schrock, J. C., & Engle, R. W. (2005). An automated version of the operation span task. *Behavior Research Methods*, 37(3), 498-505. ([DOI](https://doi.org/10.3758/bf03192720), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16405146/))
- Conway, A. R. A., Kane, M. J., Bunting, M. F., Hambrick, D. Z., Wilhelm, O., & Engle, R. W. (2005). Working memory span tasks: A methodological review and user's guide. *Psychonomic Bulletin & Review*, 12(5), 769-786. ([DOI](https://doi.org/10.3758/bf03196772), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16523997/))

## Further references

- Foster, J. L., Shipstead, Z., Harrison, T. L., Hicks, K. L., Redick, T. S., & Engle, R. W. (2015). Shortened complex span tasks can reliably measure working memory capacity. *Memory & Cognition*, 43(2), 226-236. ([DOI](https://doi.org/10.1037/t67769-000))
- Draheim, C., Mashburn, C. A., Martin, J. D., & Engle, R. W. (2019). Reaction time in differential and developmental research: A review and commentary on the problems and alternatives. *Psychological Bulletin*, 145(5), 508-535. ([DOI](https://doi.org/10.1037/bul0000192), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30896187/))
- Oberauer, K., Lewandowsky, S., Awh, E., Brown, G. D. A., Conway, A., Cowan, N., ... & Ward, G. (2018). Benchmarks for models of short-term and working memory. *Psychological Bulletin*, 144(9), 885-958. ([DOI](https://doi.org/10.1037/bul0000153), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30148379/))

## External links

- Cognitive Atlas: [operation span task](https://www.cognitiveatlas.org/task/id/trm_4c40d10cd776e)

