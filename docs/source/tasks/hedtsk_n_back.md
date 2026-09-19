(hedtsk_n_back)=
# N-Back Task

**HED task ID:** `hedtsk_n_back`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** N-Back, Dual N-Back

Continuous stream in which each item must be compared to the one n items back; accuracy and RT index working memory updating and monitoring.

## Description

The N-Back task is a continuous performance paradigm in which participants view a sequence of stimuli (letters, numbers, or spatial locations) and judge whether each current stimulus matches the one presented n trials earlier. Difficulty scales parametrically with n (1-back, 2-back, 3-back). The task engages working memory maintenance, updating, and comparison processes. Performance typically shows decreased accuracy and increased RT with higher n values. The N-back is the most widely used working memory paradigm in neuroimaging, consistently activating dorsolateral prefrontal cortex and parietal regions.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A continuous stream of stimuli is presented; participants indicate when the current item matches the one presented N items back.
* - **Manipulation**
  - Load level (N = 0, 1, 2, 3); stimulus type (letters, locations, faces); lure trials (N±1 matches); dual N-back (two simultaneous streams).
* - **Measurement**
  - Hit rate, false alarm rate, d-prime; RT; load-dependent accuracy decline.
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
* - Verbal N-Back

    `hedvar_n_back__verbal_n_back`
  - Letters, digits, or words as stimuli; engages phonological loop.
  - Letters or words; phonological working memory
* - Spatial N-Back

    `hedvar_n_back__spatial_n_back`
  - Stimulus position changes across locations; engages visuospatial sketchpad.
  - Locations instead of letters; visuospatial working memory
* - Emotional N-Back

    `hedvar_n_back__emotional_n_back`
  - Emotional faces or affective words; probes emotion-cognition interaction in WM.
  - Emotional stimuli; retained per §5.1 (EMOT retired)
* - Dual N-Back

    `hedvar_n_back__dual_n_back`
  - Two independent streams (e.g., auditory + spatial) simultaneously; used in WM training.
  - Simultaneous visual and auditory streams; recognized named paradigm (Jaeggi et al., 2008)
* - Fractal/Object N-Back

    `hedvar_n_back__fractal_object_n_back`
  - Complex non-verbal stimuli (fractals, abstract patterns); reduces verbal coding strategies.
  - Complex visual objects; different stimulus type
* - Adaptive N-Back

    `hedvar_n_back__adaptive_n_back`
  - Difficulty adjusts to performance; maintains ~80% accuracy across ability levels.
  - N-level adjusts with performance; changes task difficulty trajectory
* - N-Back with Lures

    `hedvar_n_back__n_back_with_lures`
  - Include items matching at n±1 positions (lures) to increase interference and diagnostic sensitivity.
  - Near-miss stimuli create high interference; changes task demand
* - Auditory N-Back

    `hedvar_n_back__auditory_n_back`
  - Tones, phonemes, or spoken words; auditory working memory.
  - Auditory tones or words; different sensory modality
```

## Cognitive processes

This task is designed to engage the following processes:

- [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Jonides, J., Schumacher, E. H., Smith, E. E., Koeppe, R. A., Awh, E., Minoshima, S., & Mintun, M. A. (1997). The role of parietal cortex in verbal working memory. *Journal of Neuroscience*, 17(13), 5282-5288. ([DOI](https://doi.org/10.1162/jocn.1997.9.4.462), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23968211/))
- Owen, A. M., McMillan, K. M., Laird, A. R., & Bullmore, E. (2005). N-back working memory paradigm: A meta-analysis of normative functional neuroimaging studies. *Human Brain Mapping*, 25(1), 46-59. ([DOI](https://doi.org/10.1002/hbm.20131), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15846822/))

## Further references

- Redick, T. S., & Lindsey, D. R. B. (2013). Complex span and n-back measures of working memory: A meta-analysis. *Psychonomic Bulletin & Review*, 20(6), 1102–1113. ([DOI](https://doi.org/10.3758/s13423-013-0453-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23733330/))
- Jaeggi, S. M., Buschkuehl, M., Perrig, W. J., & Meier, B. (2010). The concurrent validity of the N-back task as a working memory measure. *Memory*, 18(4), 394–412. ([DOI](https://doi.org/10.1080/09658211003702171), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20408039/))
- Chatham, C. H., Herd, S. A., Brant, A. M., Hazy, T. E., Miyake, A., O'Reilly, R., & Friedman, N. P. (2011). From an executive network to executive control: A computational model of the n-back task. *Journal of Cognitive Neuroscience*, 23(11), 3598–3619. ([DOI](https://doi.org/10.1162/jocn_a_00047), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21563882/))
- Soveri, A., Antfolk, J., Karlsson, L., Salo, B., & Laine, M. (2017). Working memory training revisited: A multi-level meta-analysis of n-back training studies. *Psychonomic Bulletin & Review*, 24(4), 1077–1096. ([DOI](https://doi.org/10.3758/s13423-016-1217-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28116702/))
- Exploring the n-back task: insights, applications, and future directions. (2025). *Frontiers in Human Neuroscience*, 19, 1721330. doi:10.3389/fnhum.2025.1721330 ([DOI](https://doi.org/10.3389/fnhum.2025.1721330), [PubMed](https://pubmed.ncbi.nlm.nih.gov/41426299/))

## External links

- Cognitive Atlas: [n-back task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949bcd)

