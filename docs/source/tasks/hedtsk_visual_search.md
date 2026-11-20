(hedtsk_visual_search)=
# Visual Search Task

**HED task ID:** `hedtsk_visual_search`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md)

**Also known as:** Feature Search, Conjunction Search

Detection of a target in a display of distractors; search slopes across set size dissociate feature (parallel) from conjunction (serial) search.

## Description

Visual Search Tasks present participants with a display containing multiple items among which they must locate a target. In feature search, the target is defined by a single distinctive feature (e.g., a red item among blue) and "pops out" preattentively, with search time independent of set size. In conjunction search, the target is defined by a combination of features (e.g., a red square among red triangles and green squares) requiring serial, attention-dependent search with RT increasing linearly with set size. The task measures search efficiency, reaction time slopes, and accuracy, providing insights into parallel versus serial attentional processing.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What does the rule ask about each stimulus?** <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
- **What competes with the correct response?** <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-targets">number of targets</a>, <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>, <a href="vocabulary.html#setting-set-size">set size</a>, <a href="vocabulary.html#setting-stimulus-similarity">stimulus similarity</a>, <a href="vocabulary.html#setting-target-probability">target probability</a>
- **Material:** An array of items with a target defined by one feature or by a conjunction of features among distractors (such as a red square among red triangles and green squares).

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. An array of items is displayed.
    2. Participants search for a target defined by a feature or feature conjunction among distractors and indicate its presence/absence or identity.
* - **Manipulations**
  - - Set size
    - Target-distractor similarity
    - Feature vs. conjunction target
    - Target prevalence
    - Display duration
    - Number of targets per display (multiple targets, with patch leaving)
    - Display type (real-world scene vs. simple array)
    - Target information before the display (feature cue or preview)
    - Irrelevant singleton distractor (color singleton vs. none)
    - Display onset (preview of half the distractors vs. simultaneous)
    - Memory set size (hybrid search through a memorized set)
* - **Measurements**
  - - RT x set size slope (search efficiency)
    - Intercept
    - Accuracy
    - Miss rate at low target prevalence
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
* - Absent Trials and Target-Present/Absent Ratio

    `hedvar_visual_search__absent_trials_and_target_present_absent_ratio`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - Target prevalence is set per block, from 50 percent down to 2 percent.
* - Multiple-Target Search (Foraging)

    `hedvar_visual_search__multiple_target_search_foraging`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-localize">localize</a>; combined with: <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-choose-for-outcomes">choose for outcomes</a> (The player decides when to leave the display)
  - [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)
  - Each display holds several targets that the participant collects by clicking, deciding when to quit the display for a new one, so the job becomes localizing targets with a patch-leaving choice layered on top.
* - Real-World/Naturalistic Search

    `hedvar_visual_search__real_world_naturalistic_search`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>
  - [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition)
  - The participant searches a photograph of a real scene (or a 3D environment) for a named object instead of an array of simple items.
* - Guided Search Variants

    `hedvar_visual_search__guided_search_variants`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-feature-cue">feature cue</a>
  - -
  - Before the display the participant is told or shown what the target looks like, or sees part of the display in advance, so a feature cue precedes the search.
* - Additional-Singleton Paradigm

    `hedvar_visual_search__additional_singleton_paradigm`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-irrelevant-dimension">irrelevant dimension</a>
  - [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
  - On some trials one distractor is unique on an irrelevant dimension (color) while the target is defined by shape, so the competitor is a salient irrelevant dimension carried by a neighbouring item.
* - Adaptive Choice Visual Search

    `hedvar_visual_search__adaptive_choice_visual_search`
  - named form
  - -
  - Two targets are always present, one per color, and the participant chooses which to look for while the color proportions drift; whether they switch to the easier target is the measure.
* - Hybrid Search (Visual + Memory)

    `hedvar_visual_search__hybrid_search_visual_memory`
  - reference: <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
  - [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory), [Recognition](../processes/long_term_memory.md#hed-recognition)
  - The participant first memorizes a set of possible targets (from a few to a hundred) and then searches each display for any of them.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Feature-based attention](../processes/selective_and_sustained_attention.md#hed-feature-based-attention)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Object-based attention](../processes/selective_and_sustained_attention.md#hed-object-based-attention)

## Key references

- Treisman, A., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97-136. ([DOI](https://doi.org/10.1016/0010-0285(80)90005-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7351125/))
- Behrmann, M., Geng, J. J., & Shomstein, S. (2004). Parietal cortex and attention. *Current Opinion in Neurobiology*, 14(2), 212-217. ([DOI](https://doi.org/10.1016/j.conb.2004.03.012), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15082327/))

## Further references

- Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review*, 28, 1060-1092. ([DOI](https://doi.org/10.3758/s13423-020-01859-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/33547630/))
- Eckstein, M. P. (2011). Visual search: A retrospective. *Journal of Vision*, 11(5), 14. ([DOI](https://doi.org/10.1167/11.5.14), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22209816/))
- Luck, S. J., & Ford, M. A. (1998). On the role of selective attention in visual perception. *Proceedings of the National Academy of Sciences*, 95(3), 825-830. [Updated by: Liesefeld, H. R., & Müller, H. J. (2019). Distractor handling via dimension weighting. *Current Opinion in Psychology*, 29, 160-167.] ([DOI](https://doi.org/10.1073/pnas.95.3.825), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9448247/))
- Wolfe, J. M., & Horowitz, T. S. (2017). Five factors that guide attention in visual search. *Nature Human Behaviour*, 1, 0058. ([DOI](https://doi.org/10.1038/s41562-017-0058), [PubMed](https://pubmed.ncbi.nlm.nih.gov/36711068/))

## External links

- Cognitive Atlas: [visual search task](https://www.cognitiveatlas.org/task/id/trm_4f2447fe67fb9)

- CogPO: [Visual Distractor/Visual Attention Paradigm](http://www.wiki.cogpo.org/index.php?title=Visual_Distractor_or_Visual_Attention_Paradigm) (close match)

