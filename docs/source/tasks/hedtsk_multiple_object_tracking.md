(hedtsk_multiple_object_tracking)=
# Multiple Object Tracking Task

**HED task ID:** `hedtsk_multiple_object_tracking`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md)

**Also known as:** MOT, Pylyshyn Tracking, Multiple Object Tracking

Participants track a subset of identical moving objects among distractors for several seconds; tracking accuracy indexes sustained multifocal attention.

## Description

In the Multiple Object Tracking task, participants view a set of identical objects (typically 8–16 circles), a subset of which are briefly designated as targets (by flashing or color). All objects then move independently and randomly for several seconds, and participants must track the targets among distractors. After movement stops, participants identify which objects were the original targets. Performance is measured as tracking accuracy as a function of target load (typically 1–5 targets). The task provides a direct index of how many individual objects can be simultaneously tracked—a measure of visual attention capacity, estimated at approximately 4 objects.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A set of identical objects (dots) move randomly; a subset is designated as targets. After the targets are highlighted, all dots move for several seconds, then participants identify which dots were targets.
* - **Manipulation**
  - Number of targets; number of distractors; speed of motion; tracking duration.
* - **Measurement**
  - Tracking accuracy (proportion correct); capacity estimate (Pylyshyn's 4±1); effects of load on accuracy.
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
* - Standard MOT

    `hedvar_multiple_object_tracking__standard_mot`
  - Track 1–5 targets among 8–16 total objects; measure accuracy by load.
  - Canonical: track subset of identical moving dots
* - Identity-MOT (MIT)

    `hedvar_multiple_object_tracking__identity_mot_mit`
  - Each object has a unique identity; report which identity is at each location after tracking.
  - Track identity features of moving objects; adds identity memory demand
* - 3D MOT (NeuroTracker)

    `hedvar_multiple_object_tracking__3d_mot_neurotracker`
  - Objects moving in simulated 3D space; used in sports training and clinical assessment.
  - Three-dimensional display with depth; different spatial processing
* - MOT with Occlusion

    `hedvar_multiple_object_tracking__mot_with_occlusion`
  - Objects briefly disappear behind occluders; tests object persistence during tracking.
  - Objects temporarily hidden; requires inference of hidden trajectories
* - Probe-Based MOT

    `hedvar_multiple_object_tracking__probe_based_mot`
  - Probe appears on one object during tracking; participant judges target vs. distractor.
  - Probe object after tracking to test spatial knowledge; different response method
* - Hierarchical MOT

    `hedvar_multiple_object_tracking__hierarchical_mot`
  - Targets embedded within groups; examines grouping effects on tracking.
  - Nested groups of objects tracked at multiple levels; different attentional structure
* - Auditory MOT Analogs

    `hedvar_multiple_object_tracking__auditory_mot_analogs`
  - Track sound sources moving in auditory space.
  - Tracking moving sounds; different sensory modality
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory)
- [Object-based attention](../processes/selective_and_sustained_attention.md#hed-object-based-attention)

## Key references

- Pylyshyn, Z. W., & Storm, R. W. (1988). Tracking multiple independent targets: Evidence for a parallel tracking mechanism. *Spatial Vision*, 3(3), 179–197. ([DOI](https://doi.org/10.1163/156856888x00122), [PubMed](https://pubmed.ncbi.nlm.nih.gov/3153671/))
- Cavanagh, P., & Alvarez, G. A. (2005). Tracking multiple targets with multifocal attention. *Trends in Cognitive Sciences*, 9(7), 349–354. ([DOI](https://doi.org/10.1016/j.tics.2005.05.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15953754/))

## Further references

- Meyerhoff, H. S., Papenmeier, F., & Huff, M. (2017). Studying visual attention using the multiple object tracking paradigm: A tutorial review. *Attention, Perception, & Psychophysics*, 79(5), 1255–1274. ([DOI](https://doi.org/10.3758/s13414-017-1338-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28584953/))
- Oksama, L., & Hyönä, J. (2016). Position tracking and identity tracking are separate systems: Evidence from eye movements. *Cognition*, 146, 393–409. ([DOI](https://doi.org/10.1016/j.cognition.2015.10.016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26529194/))
- Alvarez, G. A., & Franconeri, S. L. (2007). How many objects can you track? Evidence for a resource-limited attentive tracking mechanism. *Journal of Vision*, 7(13), 14. ([DOI](https://doi.org/10.1167/7.13.14), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17997642/))
- Drew, T., & Vogel, E. K. (2008). Neural measures of individual differences in selecting and tracking multiple moving objects. *Journal of Neuroscience*, 28(16), 4183–4191. ([DOI](https://doi.org/10.1523/jneurosci.0556-08.2008), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18417697/))

