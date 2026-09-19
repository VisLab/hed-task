(hedtsk_useful_field_of_view)=
# Useful Field of View Task

**HED task ID:** `hedtsk_useful_field_of_view`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md)

**Also known as:** Useful Field of View, UFOV

Brief central identification combined with peripheral localization under increasing distractor and divided-attention load; thresholds index processing speed and divided attention.

## Description

The Useful Field of View test measures the visual field area over which information can be rapidly extracted without eye or head movements. It consists of three subtests of increasing complexity: (1) central target identification (processing speed), (2) central identification with simultaneous peripheral target localization (divided attention), and (3) the same dual-task with embedded distractors (selective attention). Each subtest uses a staircase procedure to determine the shortest display duration achieving 75% accuracy. The UFOV was originally developed for assessing driving fitness in older adults and has become the standard measure of functional visual attention, with strong predictive validity for crash risk, instrumental activities of daily living, and cognitive decline.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Three subtests of increasing demand: central target identification, divided attention (central + peripheral targets simultaneously), and selective attention (peripheral target among distractors).
* - **Manipulation**
  - Display duration (thresholded per subtest); distractor density; eccentricity of peripheral target.
* - **Measurement**
  - Display duration threshold for 75% accuracy per subtest; UFOV composite score; correlation with driving safety measures.
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
* - Subtest 1: Central Processing Speed

    `hedvar_useful_field_of_view__subtest_1_central_processing_speed`
  - Identify a central target (car or truck) at varying display durations.
  - Central target discrimination; measures processing speed component
* - Subtest 2: Divided Attention

    `hedvar_useful_field_of_view__subtest_2_divided_attention`
  - Central identification plus localization of a peripheral target.
  - Central + peripheral target; divided attention component
* - Subtest 3: Selective Attention

    `hedvar_useful_field_of_view__subtest_3_selective_attention`
  - Subtest 2 with distracting triangles surrounding the peripheral target.
  - Peripheral target with distractors; selective attention component
* - UFOV with Varying Eccentricities

    `hedvar_useful_field_of_view__ufov_with_varying_eccentricities`
  - Peripheral targets at different distances from center.
  - Peripheral target at different distances; tests eccentricity function
```

## Cognitive processes

This task is designed to engage the following processes:

- [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)

## Key references

- Ball, K., Owsley, C., Sloane, M. E., Roenker, D. L., & Bruni, J. R. (1993). Visual attention problems as a predictor of vehicle crashes in older drivers. *Investigative Ophthalmology & Visual Science*, 34(11), 3110–3123. ([DOI](https://doi.org/10.1177/154193129303700212))
- Edwards, J. D., Vance, D. E., Wadley, V. G., Cissell, G. M., Roenker, D. L., & Ball, K. K. (2005). Reliability and validity of useful field of view test scores as administered by personal computer. *Journal of Clinical and Experimental Neuropsychology*, 27(5), 529–543. ([DOI](https://doi.org/10.1080/13803390490515432), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16019630/))

## Further references

- Edwards, J. D., Lunsman, M., Perkins, M., Rebok, G. W., & Roth, D. L. (2009). Driving cessation and health trajectories in older adults. *Journals of Gerontology Series A*, 64(12), 1290–1295. ([DOI](https://doi.org/10.1093/gerona/glp114), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19675177/))
- Ball, K., Edwards, J. D., & Ross, L. A. (2007). The impact of speed of processing training on cognitive and everyday functions. *Journals of Gerontology Series B*, 62(Special Issue 1), 19–31. ([DOI](https://doi.org/10.1093/geronb/62.special_issue_1.19), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17565162/))
- Wolfe, B., Dobres, J., Rosenholtz, R., & Reimer, B. (2017). More than the Useful Field: Considering peripheral vision in driving. *Applied Ergonomics*, 65, 316–325. ([DOI](https://doi.org/10.1016/j.apergo.2017.07.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28802451/))

