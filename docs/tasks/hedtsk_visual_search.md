(hedtsk_visual_search)=

# Visual Search Task

**HED Task ID:** `hedtsk_visual_search`

**Also known as:** Feature Search, Conjunction Search

Detection of a target in a display of distractors; search slopes across set size dissociate feature (parallel) from conjunction (serial) search.

## Description

Visual Search Tasks present participants with a display containing multiple items among which they must locate a target. In feature search, the target is defined by a single distinctive feature (e.g., a red item among blue) and "pops out" preattentively, with search time independent of set size. In conjunction search, the target is defined by a combination of features (e.g., a red square among red triangles and green squares) requiring serial, attention-dependent search with RT increasing linearly with set size. The task measures search efficiency, reaction time slopes, and accuracy, providing insights into parallel versus serial attentional processing.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - An array of items is displayed; participants search for a target defined by a feature or feature conjunction among distractors and indicate its presence/absence or identity.
* - **Manipulation**
  - Set size; target-distractor similarity; feature vs. conjunction target; target prevalence; display duration.
* - **Measurement**
  - RT × set size slope (search efficiency); intercept; accuracy; miss rate at low target prevalence.
```

## Variations

```{list-table}
---
widths: 25 40 35
header-rows: 1
---
* - Variation
  - Description
  - Justification
* - Feature Search (Pop-Out)
  - Target defined by single unique feature; flat set-size functions; parallel processing.
  - Canonical preattentive pop-out; target defined by single feature
* - Conjunction Search
  - Target defined by feature combination; linear set-size functions; serial/guided search.
  - Target defined by conjunction of features; requires serial search
* - Spatial Configuration Search
  - Target defined by spatial arrangement of elements (e.g., rotated T among L's).
  - Learned spatial configuration guides search; contextual cueing component
* - Absent Trials and Target-Present/Absent Ratio
  - Manipulating target prevalence; low prevalence produces miss errors (prevalence effect).
  - Systematically varies target presence probability; changes decision criteria
* - Multiple-Target Search (Foraging)
  - Finding multiple targets in a display; reveals satisfaction-of-search effects.
  - Multiple targets per display; foraging paradigm with different decision structure
* - Real-World/Naturalistic Search
  - Searching photographs or 3D environments for objects in cluttered natural scenes.
  - Natural scenes as search arrays; different stimulus class and recognition demands
* - Guided Search Variants
  - Manipulating top-down guidance via instruction or preview; tests guided search model predictions.
  - Top-down feature guidance provides target template; changes attentional control
* - Additional-Singleton Paradigm
  - Salient but irrelevant distractor captures attention; measures bottom-up capture vs. top-down control.
  - Color singleton distractor captures attention; distinct capture paradigm
* - Preview Search
  - Half of items presented early (preview); search operates over new items only (visual marking).
  - Subset of items previewed before search display; different temporal structure
* - Adaptive Choice Visual Search
  - Participants choose which display region to search; models foraging decisions.
  - Participant chooses between search types; tests cost-benefit of different strategies
* - Hybrid Search (Visual + Memory)
  - Searching displays for any of multiple targets held in memory; combines visual search and memory search.
  - Memory set held while visual search proceeds; combined memory-search paradigm
```

## Cognitive processes

This task engages the following cognitive processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Feature-based attention](../processes/selective_and_sustained_attention.md#hed-feature-based-attention)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Object-based attention](../processes/selective_and_sustained_attention.md#hed-object-based-attention)

## Key references

- {'authors': 'Treisman, A. M., & Gelade, G.', 'year': 1980, 'title': 'A feature-integration theory of attention', 'venue': 'Cognitive Psychology', 'venue_type': 'journal', 'journal': 'Cognitive Psychology', 'volume': '12', 'issue': '1', 'pages': '97-136', 'doi': '10.1016/0010-0285(80)90005-5', 'openalex_id': None, 'pmid': None, 'citation_string': 'Treisman, A., & Gelade, G. (1980). A feature-integration theory of attention. *Cognitive Psychology*, 12(1), 97-136.', 'url': 'https://doi.org/10.1016/0010-0285(80)90005-5', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Behrmann, M., Geng, J. J., & Shomstein, S.', 'year': 2004, 'title': 'Parietal cortex and attention', 'venue': 'Current Opinion in Neurobiology', 'venue_type': 'journal', 'journal': 'Current Opinion in Neurobiology', 'volume': '14', 'issue': '2', 'pages': '212-217', 'doi': '10.1016/j.conb.2004.03.012', 'openalex_id': None, 'pmid': None, 'citation_string': 'Behrmann, M., Geng, J. J., & Shomstein, S. (2004). Parietal cortex and attention. *Current Opinion in Neurobiology*, 14(2), 212-217.', 'url': 'https://doi.org/10.1016/j.conb.2004.03.012', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'Wolfe, J. M.', 'year': 2021, 'title': 'Guided Search 6.0: An updated model of visual search', 'venue': 'Psychonomic Bulletin & Review', 'venue_type': 'journal', 'journal': 'Psychonomic Bulletin & Review', 'volume': '28', 'issue': '4', 'pages': '1060-1092', 'doi': '10.3758/s13423-020-01859-9', 'openalex_id': None, 'pmid': None, 'citation_string': 'Wolfe, J. M. (2021). Guided Search 6.0: An updated model of visual search. *Psychonomic Bulletin & Review*, 28, 1060–1092.', 'url': 'https://doi.org/10.3758/s13423-020-01859-9', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Eckstein, M. P.', 'year': 2011, 'title': 'Visual search: A retrospective', 'venue': 'Journal of Vision', 'venue_type': 'journal', 'journal': 'Journal of Vision', 'volume': '11', 'issue': '5', 'pages': '14-14', 'doi': '10.1167/11.5.14', 'openalex_id': None, 'pmid': None, 'citation_string': 'Eckstein, M. P. (2011). Visual search: A retrospective. *Journal of Vision*, 11(5), 14.', 'url': 'https://doi.org/10.1167/11.5.14', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Luck, S. J., & Ford, M. A.', 'year': 1998, 'title': 'On the role of selective attention in visual\\u2009perception', 'venue': 'Proceedings of the National Academy of Sciences', 'venue_type': 'journal', 'journal': 'Proceedings of the National Academy of Sciences', 'volume': '95', 'issue': '3', 'pages': '825-830', 'doi': '10.1073/pnas.95.3.825', 'openalex_id': None, 'pmid': None, 'citation_string': 'Luck, S. J., & Ford, M. A. (1998). On the role of selective attention in visual perception. *Proceedings of the National Academy of Sciences*, 95(3), 825–830. \[Updated by: Liesefeld, H. R., & Müller, H. J. (2019). Distractor handling via dimension weighting. *Current Opinion in Psychology*, 29, 160–167.\]', 'url': 'https://doi.org/10.1073/pnas.95.3.825', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Wolfe, J. M., & Horowitz, T. S.', 'year': 2017, 'title': 'Five factors that guide attention in visual search', 'venue': 'Nature Human Behaviour', 'venue_type': 'journal', 'journal': 'Nature Human Behaviour', 'volume': '1', 'issue': '3', 'pages': None, 'doi': '10.1038/s41562-017-0058', 'openalex_id': None, 'pmid': None, 'citation_string': 'Wolfe, J. M., & Horowitz, T. S. (2017). Five factors that guide attention in visual search. *Nature Human Behaviour*, 1, 0058.', 'url': 'https://doi.org/10.1038/s41562-017-0058', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [visual search task](https://www.cognitiveatlas.org/task/id/trm_4f2447fe67fb9)
