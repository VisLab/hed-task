(hedtsk_operation_span)=
# Operation Span Task

**HED task ID:** `hedtsk_operation_span`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** OSPAN, Complex Span, Operation Span

Alternating arithmetic verification and word/letter memory items; complex-span score indexes working memory capacity under processing load.

## Description

The Operation Span Task is a complex span measure of working memory capacity. Participants alternate between a processing task (verifying simple math equations, e.g., "Is (2 × 3) + 1 = 8?") and a memory task (remembering letters or words presented after each equation). After a set of 3–7 equation-letter pairs, participants recall the letters in order. The OSPAN score reflects the ability to maintain memory representations while engaging in concurrent processing—a hallmark of working memory capacity (WMC). OSPAN scores are strong predictors of fluid intelligence, reading comprehension, and general executive function.

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
  - - Set size (2–7)
    - Processing task difficulty
    - Type of memoranda
    - Partial-credit vs. absolute scoring
* - **Measurements**
  - - Operation span score (items recalled in correct position)
    - Processing accuracy (to verify engagement with distractor task)
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
* - Automated OSPAN (AOSPAN)

    `hedvar_operation_span__automated_ospan_aospan`
  - Computerized version with automated scoring and timing; most widely used form.
  - Canonical computerized OSPAN with math distractor
* - Reading Span (RSPAN)

    `hedvar_operation_span__reading_span_rspan`
  - Sentence verification replaces math; read and judge sentences, remember target words.
  - Sentence comprehension distractor; different processing demand
* - Symmetry Span (SYMSPAN)

    `hedvar_operation_span__symmetry_span_symspan`
  - Symmetry judgments paired with spatial memory (red-square locations in a matrix).
  - Spatial symmetry judgment distractor; visuospatial storage component
* - Counting Span

    `hedvar_operation_span__counting_span`
  - Count target shapes in displays while remembering the counts.
  - Counting shapes distractor; different processing requirement
* - Shortened OSPAN

    `hedvar_operation_span__shortened_ospan`
  - Fewer sets for quicker administration; validated for equivalent reliability.
  - Abbreviated protocol; recognized efficient version for time-limited settings
* - Adaptive OSPAN

    `hedvar_operation_span__adaptive_ospan`
  - Set sizes adjusted based on performance; efficient estimation.
  - Adaptive set sizes based on performance; different difficulty trajectory
```

## Cognitive processes

This task is designed to engage the following processes:

- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory)
- [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)

## Key references

- Turner, M. L., & Engle, R. W. (1989). Is working memory capacity task dependent? *Journal of Memory and Language*, 28(2), 127–154. ([DOI](https://doi.org/10.1016/0749-596x(89)90040-5))
- Unsworth, N., Heitz, R. P., Schrock, J. C., & Engle, R. W. (2005). An automated version of the operation span task. *Behavior Research Methods*, 37(3), 498–505. ([DOI](https://doi.org/10.3758/bf03192720), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16405146/))
- Conway, A. R. A., Kane, M. J., Bunting, M. F., Hambrick, D. Z., Wilhelm, O., & Engle, R. W. (2005). Working memory span tasks: A methodological review and user's guide. *Psychonomic Bulletin & Review*, 12(5), 769–786. ([DOI](https://doi.org/10.3758/bf03196772), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16523997/))

## Further references

- Foster, J. L., Shipstead, Z., Harrison, T. L., Hicks, K. L., Redick, T. S., & Engle, R. W. (2015). Shortened complex span tasks can reliably measure working memory capacity. *Memory & Cognition*, 43(2), 226–236. ([DOI](https://doi.org/10.1037/t67769-000))
- Draheim, C., Mashburn, C. A., Martin, J. D., & Engle, R. W. (2019). Reaction time in differential and developmental research: A review and commentary on the problems and alternatives. *Psychological Bulletin*, 145(5), 508–535. ([DOI](https://doi.org/10.1037/bul0000192), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30896187/))
- Oberauer, K., Lewandowsky, S., Awh, E., Brown, G. D. A., Conway, A., Cowan, N., ... & Ward, G. (2018). Benchmarks for models of short-term and working memory. *Psychological Bulletin*, 144(9), 885–958. ([DOI](https://doi.org/10.1037/bul0000153), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30148379/))

## External links

- Cognitive Atlas: [operation span task](https://www.cognitiveatlas.org/task/id/trm_4c40d10cd776e)

