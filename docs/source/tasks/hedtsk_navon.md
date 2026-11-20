(hedtsk_navon)=
# Navon Task

**HED task ID:** `hedtsk_navon`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md) (also [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md))

**Also known as:** Global-Local Task, Navon Letters

Hierarchical letters in which large letters are composed of small ones; RT differences between global and local identification index attentional scope.

## Description

The Navon Task investigates hierarchical processing in vision using compound stimuli - large (global) letters composed of smaller (local) letters (e.g., a large "H" made of small "S" letters). Participants identify either the global or local letter depending on instruction. The robust finding of global precedence shows faster identification of global than local forms, with global-to-local interference exceeding local-to-global interference. The task dissociates dorsal/ventral visual stream contributions and is sensitive to hemispheric specialization (left hemisphere for local, right for global processing).

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What competes with the correct response?** <a href="vocabulary.html#rule-respond-to-rule-competitor-irrelevant-dimension">irrelevant dimension</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>
- **Material:** Large letters made of small letters (such as an H made of S's), the same or a different letter at the two levels.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A large letter (global) composed of small letters (local) is presented.
    2. Participants identify the letter at the designated level (global or local).
* - **Manipulations**
  - - Target level (global, local, divided across both)
    - Congruency (same vs. different letter at two levels)
    - Exposure duration
    - Visual field
    - Level cue (cued per trial vs. fixed per block)
    - Stimulus type (letters, geometric shapes, emotional faces)
    - Preceding Navon task and its carry-over to a following task
* - **Measurements**
  - - RT and accuracy
    - Global precedence effect (faster global)
    - Asymmetric interference (global disrupts local more than reverse)
    - Congruency effect
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
* - Mixed/Cued Navon

    `hedvar_navon__mixed_cued_navon`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>; cue: <a href="vocabulary.html#rule-respond-to-rule-cue-rule-cue">rule cue</a>; rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>
  - [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
  - A cue on each trial says which level to report, so the level switches trial by trial instead of being fixed per block.
* - Divided Attention Navon

    `hedvar_navon__divided_attention_navon`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>; combined with: <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (The target may be at the global or the local level, and both are monitored)
  - [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
  - The target may appear at either level, or both levels must be reported, so attention is divided across both levels instead of set to one.
* - Sparse vs. Dense Local Elements

    `hedvar_navon__sparse_vs_dense_local_elements`
  - named form
  - -
  - The number and spacing of the small letters is varied, which weakens the global advantage when elements are sparse.
* - Emotional Navon

    `hedvar_navon__emotional_navon`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>, <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
  - The compound figure is a large expressive face built from small expressive faces and the participant reports the emotion at the cued level.
* - Auditory Navon Analogs

    `hedvar_navon__auditory_navon_analogs`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-music">music</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - The hierarchy is a melody built from short note patterns and the participant judges either the contour or the local pattern.
* - Navon Figures with Shapes

    `hedvar_navon__navon_figures_with_shapes`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - -
  - Geometric shapes replace letters at both levels so reading plays no part.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict)

## Key references

- Navon, D. (1977). Forest before trees: The precedence of global features in visual perception. *Cognitive Psychology*, 9(3), 353-383. ([DOI](https://doi.org/10.1016/0010-0285(77)90012-3))
- Kimchi, R. (1992). Primacy of wholistic processing and global/local paradigm: A critical review. *Psychological Bulletin*, 112(1), 24-38. ([DOI](https://doi.org/10.1037/0033-2909.112.1.24))
- Fink, G. R., Halligan, P. W., Marshall, J. C., Frith, C. D., Frackowiak, R. S. J., & Dolan, R. J. (1996). Where in the brain does visual attention select the forest and the trees? *Nature*, 382, 626-628. ([DOI](https://doi.org/10.1038/382626a0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8757132/))

## Further references

- Poirel, N., Pineau, A., & Mellet, E. (2008). What does the nature of the stimuli tell us about the global precedence effect? *Acta Psychologica*, 127(1), 1-11. ([DOI](https://doi.org/10.1016/j.actpsy.2006.12.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17240344/))
- Beaucousin, V., Cassotti, M., Simon, G., Pineau, A., Kostova, M., Houdé, O., & Poirel, N. (2011). ERP evidence of a meaningfulness impact on visual global/local processing: When meaning captures attention. *Neuropsychologia*, 49(5), 1258-1266. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2011.01.039), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21281654/))
- Gerlach, C., & Poirel, N. (2018). Navon's classical paradigm concerning local and global processing relates systematically to visual object classification performance. *Scientific Reports*, 8, 324. ([DOI](https://doi.org/10.1038/s41598-017-18664-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29321634/))
- Förster, J., & Dannenberg, L. (2010). GLOMOsys: A systems account of global versus local processing. *Psychological Inquiry*, 21(3), 175-197. ([DOI](https://doi.org/10.1080/1047840x.2010.487849))
- Kaur, J., & Paul, S. (2022). Global precedence changes by environment: A systematic review and meta-analysis on effect of perceptual field variables on global-local visual processing. *Attention, Perception, & Psychophysics*, 84, 1833-1877.
- Song, Y., Hakoda, Y., & Sang, B. (2015). Lack of global precedence and global-to-local interference without local processing deficit in children with ADHD. *Journal of Attention Disorders*, 20(8), 671-682. ([DOI](https://doi.org/10.1037/neu0000213), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26146856/))

## External links

- Cognitive Atlas: [global-local task](https://www.cognitiveatlas.org/task/id/trm_4f241d7adf14e)

