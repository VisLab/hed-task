(hedtsk_digit_span)=
# Digit Span Task

**HED task ID:** `hedtsk_digit_span`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** DS, Forward/Backward Span, Digit Span

Auditory or visual digit sequences reproduced in forward or backward order; longest correctly reproduced length indexes verbal short-term and working memory span.

## Description

The Digit Span task measures verbal short-term and working memory capacity. In the Forward condition, participants listen to sequences of digits presented at a rate of one per second and immediately repeat them in the same order; sequence length increases until recall fails. In the Backward condition, participants repeat digits in reverse order, adding a manipulation component. The Sequencing condition (from WAIS-IV) requires reordering digits numerically. Digit Span is one of the oldest and most widely administered neuropsychological measures, embedded in the Wechsler intelligence and memory scales. Forward span primarily indexes the phonological loop, while backward span engages central executive processes.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Sequences of digits are presented at a rate of one per second; participants reproduce the sequence in forward, backward, or sequencing order. Length increases until two consecutive failures.
* - **Manipulation**
  - Direction (forward, backward, sequencing); sequence length; presentation modality (auditory vs. visual).
* - **Measurement**
  - Span (longest correct sequence); total score; forward-backward difference as index of executive load.
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
* - Forward Digit Span

    `hedvar_digit_span__forward_digit_span`
  - Repeat digits in presentation order; primarily measures phonological loop capacity.
  - Reproduce digits in order; canonical phonological span measure
* - Backward Digit Span

    `hedvar_digit_span__backward_digit_span`
  - Repeat digits in reverse; adds manipulation and executive demand.
  - Reproduce in reverse; requires mental transformation
* - Digit Span Sequencing (WAIS-IV)

    `hedvar_digit_span__digit_span_sequencing_wais_iv`
  - Reorder digits from lowest to highest; requires sequencing operations.
  - Reorder digits from smallest to largest; different transformation requirement
* - Letter-Number Sequencing

    `hedvar_digit_span__letter_number_sequencing`
  - Mixed sequences of letters and digits; reorder numbers first, then letters alphabetically.
  - Alternating letters and numbers reordered separately; dual sequencing demand
* - Auditory vs. Visual Presentation

    `hedvar_digit_span__auditory_vs_visual_presentation`
  - Digits spoken aloud vs. presented visually on screen; modality effects on span.
  - Visual digit presentation vs. auditory; different input modality
* - Adaptive Staircase Versions

    `hedvar_digit_span__adaptive_staircase_versions`
  - Computerized versions adjusting sequence length based on accuracy; more precise span estimates.
  - Adaptive difficulty tracking; different trial-generation procedure
* - Spatial Digit Span

    `hedvar_digit_span__spatial_digit_span`
  - Digits presented at spatial locations; combines verbal and spatial demands.
  - Digits at spatial locations; adds spatial component
* - Running Digit Span

    `hedvar_digit_span__running_digit_span`
  - Unpredictable sequence lengths; recall the last N items; measures updating.
  - Recall last N digits of unknown-length list; different task structure
* - Grouped/Chunked Presentation

    `hedvar_digit_span__grouped_chunked_presentation`
  - Digits presented in rhythmic groups; examines effects of chunking.
  - Digits presented in groups; tests chunking facilitation
* - Matrix Span

    `hedvar_digit_span__matrix_span`
  - Memory for spatial locations within a matrix; visuospatial analog.
  - Spatial matrix locations instead of digits; different stimulus type
* - Supra-Span Lists

    `hedvar_digit_span__supra_span_lists`
  - Lists exceeding span; number of trials to criterion measures learning rate.
  - Lists exceed span; tests learning over trials
```

## Cognitive processes

This task is designed to engage the following processes:

- [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory)
- [Rehearsal](../processes/short_term_and_working_memory.md#hed-rehearsal)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Manipulation](../processes/short_term_and_working_memory.md#hed-manipulation)
- [Chunking](../processes/short_term_and_working_memory.md#hed-chunking)

## Key references

- Baddeley, A. D. (1986). *Working Memory*. Oxford University Press. ([DOI](https://doi.org/10.1016/s0166-4115(08)61202-9))
- Miller, G. A. (1956). The magical number seven, plus or minus two: Some limits on our capacity for processing information. *Psychological Review*, 63(2), 81–97. ([DOI](https://doi.org/10.1037/h0043158), [PubMed](https://pubmed.ncbi.nlm.nih.gov/13310704/))

## Further references

- Woods, D. L., Kishiyama, M. M., Yund, E. W., Herron, T. J., Edwards, B., Poliva, O., ... & Reed, B. (2011). Improving digit span assessment of short-term verbal memory. *Journal of Clinical and Experimental Neuropsychology*, 33(1), 101–111. ([DOI](https://doi.org/10.1080/13803395.2010.550602), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21957866/))

## External links

- Cognitive Atlas: [digit span task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949a0d)

