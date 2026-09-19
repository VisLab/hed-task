(hedtsk_corsi_block_tapping)=
# Corsi Block-Tapping Task

**HED task ID:** `hedtsk_corsi_block_tapping`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** Corsi, Block Tapping, Corsi Span

Experimenter taps a sequence on spatially arranged blocks; participant reproduces the sequence forward or backward. Indexes visuospatial short-term and working memory span.

## Description

The Corsi Block-Tapping Task measures visuospatial short-term and working memory. Nine blocks are arranged irregularly on a board (or screen). The examiner taps a sequence of blocks, and the participant reproduces the sequence. Sequence length increases from 2 blocks upward until the participant fails two consecutive sequences at a given length. The maximum reliably reproduced length defines the Corsi span, typically around 5–6 for healthy adults. The backward version requires reproducing sequences in reverse order, adding executive demands. The task is the spatial counterpart of Digit Span and is critical for understanding the visuospatial sketchpad component of working memory.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - The experimenter (or computer) taps a sequence of blocks on a board; the participant reproduces the sequence in the same (or reverse) order. Sequence length increases until recall fails.
* - **Manipulation**
  - Sequence length; forward vs. backward reproduction; block spatial arrangement.
* - **Measurement**
  - Span (longest sequence correctly recalled); total score across trials.
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
* - Forward Corsi Span

    `hedvar_corsi_block_tapping__forward_corsi_span`
  - Reproduce sequences in the same order as presented.
  - Reproduce tapped sequence in same order; canonical visuospatial span
* - Backward Corsi Span

    `hedvar_corsi_block_tapping__backward_corsi_span`
  - Reproduce sequences in reverse order; adds executive manipulation.
  - Reproduce sequence in reverse order; requires mental transformation
* - Computerized (eCorsi)

    `hedvar_corsi_block_tapping__computerized_ecorsi`
  - Tablet or screen-based with precise timing and spatial metrics.
  - Screen-based tapping vs. physical blocks; per §5.6 changes spatial/motor demands
* - Supra-Span Corsi

    `hedvar_corsi_block_tapping__supra_span_corsi`
  - Sequences exceeding span; number of trials to learn measures spatial learning.
  - Sequences exceed span; repeated learning-to-criterion procedure
* - Walking Corsi (large-scale)

    `hedvar_corsi_block_tapping__walking_corsi_large_scale`
  - Life-size version where participants walk between floor locations; ecological spatial memory.
  - Full-body locomotion to large floor locations; different motor modality from finger tapping
* - Sequential vs. Simultaneous Presentation

    `hedvar_corsi_block_tapping__sequential_vs_simultaneous_presentation`
  - Blocks highlighted one at a time vs. subset highlighted together.
  - All blocks illuminated at once vs. sequentially; changes encoding demands
* - Crossed/Uncrossed Paths

    `hedvar_corsi_block_tapping__crossed_uncrossed_paths`
  - Sequences with vs. without path crossings to study spatial complexity.
  - Spatial crossing of sequence paths tests motor programming constraints
```

## Cognitive processes

This task is designed to engage the following processes:

- [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory)
- [Manipulation](../processes/short_term_and_working_memory.md#hed-manipulation)

## Key references

- Corsi, P. M. (1972). *Human memory and the medial temporal region of the brain*. Unpublished doctoral dissertation, McGill University.
- Milner, B. (1971). Interhemispheric differences in the localization of psychological processes in man. *British Medical Bulletin*, 27(3), 272–277. ([DOI](https://doi.org/10.1093/oxfordjournals.bmb.a070866), [PubMed](https://pubmed.ncbi.nlm.nih.gov/4937273/))

## Further references

- Pagulayan, K. F., Busch, R. M., Medina, K. L., Bartok, J. A., & Krikorian, R. (2006). Developmental normative data for the Corsi Block-Tapping Task. *Journal of Clinical and Experimental Neuropsychology*, 28(6), 1043–1052. ([DOI](https://doi.org/10.1080/13803390500350977), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16822742/))
- Brunetti, R., Del Gatto, C., & Delogu, F. (2014). eCorsi: Implementation and testing of the Corsi Block-Tapping Task for digital tablets. *Frontiers in Psychology*, 5, 939. ([DOI](https://doi.org/10.3389/fpsyg.2014.00939), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25228888/))

## External links

- Cognitive Atlas: [Corsi Blocks](https://www.cognitiveatlas.org/task/id/trm_4da881dace79c)

