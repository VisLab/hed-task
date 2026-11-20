(hedtsk_multiple_object_tracking)=
# Multiple Object Tracking Task

**HED task ID:** `hedtsk_multiple_object_tracking`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md)

**Also known as:** MOT, Pylyshyn Tracking, Multiple Object Tracking

Participants track a subset of identical moving objects among distractors for several seconds; tracking accuracy indexes sustained multifocal attention.

## Description

In the Multiple Object Tracking task, participants view a set of identical objects (typically 8-16 circles), a subset of which are briefly designated as targets (by flashing or color). All objects then move independently and randomly for several seconds, and participants must track the targets among distractors. After movement stops, participants identify which objects were the original targets. Performance is measured as tracking accuracy as a function of target load (typically 1-5 targets). The task provides a direct index of how many individual objects can be simultaneously tracked - a measure of visual attention capacity, estimated at approximately 4 objects.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **How long is it held?** <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-forced-choice">forced choice</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-distractors">number of distractors</a>, <a href="vocabulary.html#setting-number-of-targets">number of targets</a>, <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>
- **Material:** 8-16 identical circles, a few briefly flashed or colored as targets, that then move independently and randomly.
- **Combined with:** <a href="vocabulary.html#how-throughout">throughout</a>, [Fixate Task](hedtsk_fixate.md) (Gaze is held on the fixation target while the main game is played)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A set of identical objects (dots) move randomly.
    2. a subset is designated as targets.
    3. After the targets are highlighted, all dots move for several seconds, then participants identify which dots were targets.
* - **Manipulations**
  - - Number of targets
    - Number of distractors
    - Speed of motion
    - Tracking duration
    - Added identity report for tracked objects
    - Occlusion during tracking (barriers or vanishing)
    - Grouping of tracked objects (clusters vs. independent)
* - **Measurements**
  - - Tracking accuracy (proportion correct)
    - Capacity estimate (Pylyshyn's 4+/-1)
    - Effects of load on accuracy
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
* - Identity-MOT (MIT)

    `hedvar_multiple_object_tracking__identity_mot_mit`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; studied material: <a href="vocabulary.html#rule-study-then-test-studied-material-items-with-context">items with context</a>; test form: <a href="vocabulary.html#rule-study-then-test-test-form-cued-recall">cued recall</a>
  - -
  - Each object carries a hidden identity (letter, picture, or color) and at the end the participant reports which identity is at each target position, so identities bound to tracked positions are studied and recalled to a position cue.
* - 3D MOT (NeuroTracker)

    `hedvar_multiple_object_tracking__3d_mot_neurotracker`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>, <a href="vocabulary.html#facet-task-io-device-stereoscopic-display">stereoscopic display</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - -
  - The spheres move in a simulated three-dimensional volume seen through a stereoscopic display and a staircase adjusts speed to find the fastest trackable rate.
* - Probe-Based MOT

    `hedvar_multiple_object_tracking__probe_based_mot`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>; test form: <a href="vocabulary.html#rule-study-then-test-test-form-old-new">old new</a>
  - -
  - One object is highlighted during or after movement and the participant answers yes or no to whether it is a target, a single old/new judgment instead of selecting all targets.
* - Auditory MOT Analogs

    `hedvar_multiple_object_tracking__auditory_mot_analogs`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - The moving items are sounds that move around the listener in virtual auditory space and the target sounds are tracked by ear.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory)
- [Object-based attention](../processes/selective_and_sustained_attention.md#hed-object-based-attention)

## Key references

- Pylyshyn, Z. W., & Storm, R. W. (1988). Tracking multiple independent targets: Evidence for a parallel tracking mechanism. *Spatial Vision*, 3(3), 179-197. ([DOI](https://doi.org/10.1163/156856888x00122), [PubMed](https://pubmed.ncbi.nlm.nih.gov/3153671/))
- Cavanagh, P., & Alvarez, G. A. (2005). Tracking multiple targets with multifocal attention. *Trends in Cognitive Sciences*, 9(7), 349-354. ([DOI](https://doi.org/10.1016/j.tics.2005.05.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15953754/))

## Further references

- Meyerhoff, H. S., Papenmeier, F., & Huff, M. (2017). Studying visual attention using the multiple object tracking paradigm: A tutorial review. *Attention, Perception, & Psychophysics*, 79(5), 1255-1274. ([DOI](https://doi.org/10.3758/s13414-017-1338-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28584953/))
- Oksama, L., & Hyönä, J. (2016). Position tracking and identity tracking are separate systems: Evidence from eye movements. *Cognition*, 146, 393-409. ([DOI](https://doi.org/10.1016/j.cognition.2015.10.016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26529194/))
- Alvarez, G. A., & Franconeri, S. L. (2007). How many objects can you track? Evidence for a resource-limited attentive tracking mechanism. *Journal of Vision*, 7(13), 14. ([DOI](https://doi.org/10.1167/7.13.14), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17997642/))
- Drew, T., & Vogel, E. K. (2008). Neural measures of individual differences in selecting and tracking multiple moving objects. *Journal of Neuroscience*, 28(16), 4183-4191. ([DOI](https://doi.org/10.1523/jneurosci.0556-08.2008), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18417697/))

## External links

- CogPO: [Visual Pursuit/Tracking Paradigm](http://www.wiki.cogpo.org/index.php?title=Visual_Pursuit_or_Tracking_Paradigm) (close match)

