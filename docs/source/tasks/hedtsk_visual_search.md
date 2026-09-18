(hedtsk_visual_search)=
# Visual Search Task

**HED task ID:** `hedtsk_visual_search`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md)

**Also known as:** Feature Search, Conjunction Search

Detection of a target in a display of distractors; search slopes across set size dissociate feature (parallel) from conjunction (serial) search.

## Description

Visual Search Tasks present participants with a display containing multiple items among which they must locate a target. In feature search, the target is defined by a single distinctive feature (e.g., a red item among blue) and "pops out" preattentively, with search time independent of set size. In conjunction search, the target is defined by a combination of features (e.g., a red square among red triangles and green squares) requiring serial, attention-dependent search with RT increasing linearly with set size. The task measures search efficiency, reaction time slopes, and accuracy, providing insights into parallel versus serial attentional processing.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - An array of items is displayed; participants search for a target defined by a feature or feature conjunction among distractors and indicate its presence/absence or identity.
* - **Manipulation**
  - Set size; target-distractor similarity; feature vs. conjunction target; target prevalence; display duration.
* - **Measurement**
  - RT × set size slope (search efficiency); intercept; accuracy; miss rate at low target prevalence.
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
* - Feature Search (Pop-Out)

    `hedvar_visual_search__feature_search_pop_out`
  - Target defined by single unique feature; flat set-size functions; parallel processing.
  - Canonical preattentive pop-out; target defined by single feature
* - Conjunction Search

    `hedvar_visual_search__conjunction_search`
  - Target defined by feature combination; linear set-size functions; serial/guided search.
  - Target defined by conjunction of features; requires serial search
* - Spatial Configuration Search

    `hedvar_visual_search__spatial_configuration_search`
  - Target defined by spatial arrangement of elements (e.g., rotated T among L's).
  - Learned spatial configuration guides search; contextual cueing component
* - Absent Trials and Target-Present/Absent Ratio

    `hedvar_visual_search__absent_trials_and_target_present_absent_ratio`
  - Manipulating target prevalence; low prevalence produces miss errors (prevalence effect).
  - Systematically varies target presence probability; changes decision criteria
* - Multiple-Target Search (Foraging)

    `hedvar_visual_search__multiple_target_search_foraging`
  - Finding multiple targets in a display; reveals satisfaction-of-search effects.
  - Multiple targets per display; foraging paradigm with different decision structure
* - Real-World/Naturalistic Search

    `hedvar_visual_search__real_world_naturalistic_search`
  - Searching photographs or 3D environments for objects in cluttered natural scenes.
  - Natural scenes as search arrays; different stimulus class and recognition demands
* - Guided Search Variants

    `hedvar_visual_search__guided_search_variants`
  - Manipulating top-down guidance via instruction or preview; tests guided search model predictions.
  - Top-down feature guidance provides target template; changes attentional control
* - Additional-Singleton Paradigm

    `hedvar_visual_search__additional_singleton_paradigm`
  - Salient but irrelevant distractor captures attention; measures bottom-up capture vs. top-down control.
  - Color singleton distractor captures attention; distinct capture paradigm
* - Preview Search

    `hedvar_visual_search__preview_search`
  - Half of items presented early (preview); search operates over new items only (visual marking).
  - Subset of items previewed before search display; different temporal structure
* - Adaptive Choice Visual Search

    `hedvar_visual_search__adaptive_choice_visual_search`
  - Participants choose which display region to search; models foraging decisions.
  - Participant chooses between search types; tests cost-benefit of different strategies
* - Hybrid Search (Visual + Memory)

    `hedvar_visual_search__hybrid_search_visual_memory`
  - Searching displays for any of multiple targets held in memory; combines visual search and memory search.
  - Memory set held while visual search proceeds; combined memory-search paradigm
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Feature-based attention](../processes/selective_and_sustained_attention.md#hed-feature-based-attention)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Object-based attention](../processes/selective_and_sustained_attention.md#hed-object-based-attention)

## Key references

- Treisman, A., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97-136.
- Behrmann, M., Geng, J. J., & Shomstein, S. (2004). Parietal cortex and attention. *Current Opinion in Neurobiology*, 14(2), 212-217.

## Recent references

- Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review*, 28, 1060–1092.
- Eckstein, M. P. (2011). Visual search: A retrospective. *Journal of Vision*, 11(5), 14.
- Luck, S. J., & Ford, M. A. (1998). On the role of selective attention in visual perception. *Proceedings of the National Academy of Sciences*, 95(3), 825–830. [Updated by: Liesefeld, H. R., & Müller, H. J. (2019). Distractor handling via dimension weighting. *Current Opinion in Psychology*, 29, 160–167.]
- Wolfe, J. M., & Horowitz, T. S. (2017). Five factors that guide attention in visual search. *Nature Human Behaviour*, 1, 0058.

## External links

- Cognitive Atlas: [visual search task](https://www.cognitiveatlas.org/task/id/trm_4f2447fe67fb9)

