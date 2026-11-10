(hedtsk_navon)=
# Navon Task

**HED task ID:** `hedtsk_navon`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md) (also [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md))

**Also known as:** Global-Local Task, Navon Letters

Hierarchical letters in which large letters are composed of small ones; RT differences between global and local identification index attentional scope.

## Description

The Navon Task investigates hierarchical processing in vision using compound stimuli—large (global) letters composed of smaller (local) letters (e.g., a large "H" made of small "S" letters). Participants identify either the global or local letter depending on instruction. The robust finding of global precedence shows faster identification of global than local forms, with global-to-local interference exceeding local-to-global interference. The task dissociates dorsal/ventral visual stream contributions and is sensitive to hemispheric specialization (left hemisphere for local, right for global processing).

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
  - - Target level (global vs. local)
    - Congruency (same vs. different letter at two levels)
    - Exposure duration
    - Visual field
* - **Measurements**
  - - RT and accuracy
    - Global precedence effect (faster global)
    - Asymmetric interference (global disrupts local more than reverse)
    - Congruency effect
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
* - Standard Navon (Blocked)

    `hedvar_navon__standard_navon_blocked`
  - A large letter made up of small letters is shown, for example a big H built from small Ss. In some blocks the participant identifies the big letter, in others the small letters. People are usually faster with the big letter and are slowed when the two levels disagree.
  - Canonical blocked global/local judgment of hierarchical figures
* - Mixed/Cued Navon

    `hedvar_navon__mixed_cued_navon`
  - Whether to report the big or the small letter is signaled by a cue on each trial rather than fixed for a block, so the participant must switch between levels from trial to trial.
  - Trial-by-trial cue indicates level; task-switching demand added
* - Divided Attention Navon

    `hedvar_navon__divided_attention_navon`
  - The participant looks for a target letter that may appear at either level, or must report both the big and the small letter, so attention cannot be set to one level in advance.
  - Respond to both levels simultaneously; different attentional demand
* - Consistent vs. Inconsistent Stimuli

    `hedvar_navon__consistent_vs_inconsistent_stimuli`
  - Trials in which the big and small letters are the same (a big H made of small Hs) are compared with trials where they differ (a big H made of small Ss). The slowdown on different-letter trials measures interference between levels.
  - Local and global levels same vs. different; conflict manipulation
* - Sparse vs. Dense Local Elements

    `hedvar_navon__sparse_vs_dense_local_elements`
  - The number and spacing of the small letters making up the big letter is varied. With fewer, more widely spaced elements the big letter is harder to see and the usual advantage for the big letter shrinks.
  - Number of local elements varies; tests density effect on global processing
* - Emotional Navon

    `hedvar_navon__emotional_navon`
  - The compound figure is built from faces or emotional pictures, for example a large happy face made of small sad faces, and the participant reports the emotion at the cued level.
  - Emotional faces at global/local level; retained per §5.1 (EMOT retired)
* - Auditory Navon Analogs

    `hedvar_navon__auditory_navon_analogs`
  - The hierarchy is in sound: a short melody (the global level) is made up of smaller note patterns (the local level), and the participant judges either the overall contour or the local pattern.
  - Hierarchical auditory stimuli; different sensory modality
* - Navon with Priming

    `hedvar_navon__navon_with_priming`
  - A task that requires attending to the big or the small level is performed first, and its effect on a following task is measured. Attending to one level carries over and biases later processing toward that level.
  - Preceding prime influences level processing; temporal context manipulation
* - Lateralized Presentation

    `hedvar_navon__lateralized_presentation`
  - The compound letter is flashed briefly to the left or right of fixation, so that it reaches one hemisphere of the brain first. The right hemisphere tends to favor the big letter and the left the small letters.
  - Stimuli presented to one visual field; tests hemispheric contributions
* - Navon Figures with Shapes

    `hedvar_navon__navon_figures_with_shapes`
  - The compound figures are geometric shapes, such as a large square made of small triangles, rather than letters, so that reading is not involved.
  - Non-letter shapes at global/local level; different stimulus class
* - Temporal Precedence (Brief Exposure)

    `hedvar_navon__temporal_precedence_brief_exposure`
  - The compound figure is flashed for only 50 to 100 ms and sometimes masked. At such short exposures the big letter is usually identified more often than the small ones, which shows which level is available first.
  - Brief exposure tests which level is processed first
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict)

## Key references

- Navon, D. (1977). Forest before trees: The precedence of global features in visual perception. *Cognitive Psychology*, 9(3), 353–383. ([DOI](https://doi.org/10.1016/0010-0285(77)90012-3))
- Kimchi, R. (1992). Primacy of wholistic processing and global/local paradigm: A critical review. *Psychological Bulletin*, 112(1), 24–38. ([DOI](https://doi.org/10.1037/0033-2909.112.1.24))
- Fink, G. R., Halligan, P. W., Marshall, J. C., Frith, C. D., Frackowiak, R. S. J., & Dolan, R. J. (1996). Where in the brain does visual attention select the forest and the trees? *Nature*, 382, 626–628. ([DOI](https://doi.org/10.1038/382626a0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8757132/))

## Further references

- Poirel, N., Pineau, A., & Mellet, E. (2008). What does the nature of the stimuli tell us about the global precedence effect? *Acta Psychologica*, 127(1), 1–11. ([DOI](https://doi.org/10.1016/j.actpsy.2006.12.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17240344/))
- Beaucousin, V., Cassotti, M., Simon, G., Pineau, A., Kostova, M., Houdé, O., & Poirel, N. (2011). ERP evidence of a meaningfulness impact on visual global/local processing: When meaning captures attention. *Neuropsychologia*, 49(5), 1258–1266. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2011.01.039), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21281654/))
- Gerlach, C., & Poirel, N. (2018). Navon's classical paradigm concerning local and global processing relates systematically to visual object classification performance. *Scientific Reports*, 8, 324. ([DOI](https://doi.org/10.1038/s41598-017-18664-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29321634/))
- Förster, J., & Dannenberg, L. (2010). GLOMOsys: A systems account of global versus local processing. *Psychological Inquiry*, 21(3), 175–197. ([DOI](https://doi.org/10.1080/1047840x.2010.487849))
- Kaur, J., & Paul, S. (2022). Global precedence changes by environment: A systematic review and meta-analysis on effect of perceptual field variables on global-local visual processing. *Attention, Perception, & Psychophysics*, 84, 1833–1877.
- Song, Y., Hakoda, Y., & Sang, B. (2015). Lack of global precedence and global-to-local interference without local processing deficit in children with ADHD. *Journal of Attention Disorders*, 20(8), 671–682. ([DOI](https://doi.org/10.1037/neu0000213), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26146856/))

## External links

- Cognitive Atlas: [global-local task](https://www.cognitiveatlas.org/task/id/trm_4f241d7adf14e)

