(hedtsk_useful_field_of_view)=
# Useful Field of View Task

**HED task ID:** `hedtsk_useful_field_of_view`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md)

**Also known as:** Useful Field of View, UFOV

Brief central identification combined with peripheral localization under increasing distractor and divided-attention load; thresholds index processing speed and divided attention.

## Description

The Useful Field of View test measures the visual field area over which information can be rapidly extracted without eye or head movements. It consists of three subtests of increasing complexity: (1) central target identification (processing speed), (2) central identification with simultaneous peripheral target localization (divided attention), and (3) the same dual-task with embedded distractors (selective attention). Each subtest uses a staircase procedure to determine the shortest display duration achieving 75% accuracy. The UFOV was originally developed for assessing driving fitness in older adults and has become the standard measure of functional visual attention, with strong predictive validity for crash risk, instrumental activities of daily living, and cognitive decline.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-noise-or-mask">noise or mask</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - Population: <a href="vocabulary.html#facet-population-older-adults">older adults</a>, <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-eccentricity">eccentricity</a>, <a href="vocabulary.html#setting-number-of-distractors">number of distractors</a>, <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>
- **Material:** Brief displays with a central target, a peripheral target at varying eccentricity, and in the third subtest surrounding distractors.
- **Combined with:** <a href="vocabulary.html#how-throughout">throughout</a>, [Fixate Task](hedtsk_fixate.md) (Gaze is held on the fixation target while the main game is played)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Three subtests of increasing demand: central target identification, divided attention (central + peripheral targets simultaneously), and selective attention (peripheral target among distractors).
* - **Manipulations**
  - - Display duration (thresholded per subtest)
    - Distractor density
    - Eccentricity of peripheral target
    - Added simultaneous peripheral target to localize
* - **Measurements**
  - - Display duration threshold for 75% accuracy per subtest
    - UFOV composite score
    - Correlation with driving safety measures
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
* - Subtest 2: Divided Attention

    `hedvar_useful_field_of_view__subtest_2_divided_attention`
  - combined with: <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (A peripheral target is localized while the central item is identified)
  - -
  - A peripheral car appears at the same time and must also be located while the central item is identified, so two jobs are done at once.
* - Subtest 3: Selective Attention

    `hedvar_useful_field_of_view__subtest_3_selective_attention`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>; combined with: <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (A peripheral target is localized among distractors while the central item is identified)
  - -
  - As subtest 2 but the display is filled with distracting triangles, so the peripheral target must be found among clutter as well as behind the mask.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)

## Key references

- Ball, K., Owsley, C., Sloane, M. E., Roenker, D. L., & Bruni, J. R. (1993). Visual attention problems as a predictor of vehicle crashes in older drivers. *Investigative Ophthalmology & Visual Science*, 34(11), 3110-3123.
- Edwards, J. D., Vance, D. E., Wadley, V. G., Cissell, G. M., Roenker, D. L., & Ball, K. K. (2005). Reliability and validity of useful field of view test scores as administered by personal computer. *Journal of Clinical and Experimental Neuropsychology*, 27(5), 529-543. ([DOI](https://doi.org/10.1080/13803390490515432), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16019630/))

## Further references

- Edwards, J. D., Lunsman, M., Perkins, M., Rebok, G. W., & Roth, D. L. (2009). Driving cessation and health trajectories in older adults. *Journals of Gerontology Series A*, 64(12), 1290-1295. ([DOI](https://doi.org/10.1093/gerona/glp114), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19675177/))
- Ball, K., Edwards, J. D., & Ross, L. A. (2007). The impact of speed of processing training on cognitive and everyday functions. *Journals of Gerontology Series B*, 62(Special Issue 1), 19-31. ([DOI](https://doi.org/10.1093/geronb/62.special_issue_1.19), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17565162/))
- Wolfe, B., Dobres, J., Rosenholtz, R., & Reimer, B. (2017). More than the Useful Field: Considering peripheral vision in driving. *Applied Ergonomics*, 65, 316-325. ([DOI](https://doi.org/10.1016/j.apergo.2017.07.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28802451/))

