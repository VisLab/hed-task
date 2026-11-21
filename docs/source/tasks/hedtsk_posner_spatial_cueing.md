(hedtsk_posner_spatial_cueing)=
# Posner Spatial Cueing Task

**HED task ID:** `hedtsk_posner_spatial_cueing`

**Family:** [Attentional cueing and orienting tasks](families/attentional_cueing.md)

**Also known as:** Posner Task, Spatial Cueing Task

A central or peripheral cue indicates the likely target location; RT differences between valid, neutral, and invalid cues index covert spatial orienting.

## Description

The Posner Spatial Cueing Task measures covert orienting of visual attention. Participants fixate on a central point with two peripheral locations marked. A cue stimulus appears (exogenous: at the target location; or endogenous: a central arrow) followed by a target stimulus at one of the peripheral locations. Cues can be valid (same location as target) or invalid (opposite location). The cueing effect (faster RT to validly cued targets vs. invalidly cued) reflects the cost and benefit of attentional orienting. The task dissociates different components of attention: engaging, disengaging, and shifting.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
  - *Does a cue come before the target?* <a href="vocabulary.html#rule-respond-to-rule-cue-location-cue">location cue</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-proportion-congruent">proportion congruent</a>, <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** A central fixation point with two marked peripheral locations, a cue (a peripheral flash or a central arrow), and a target at the cued or the other location.
- **Combined with:** <a href="vocabulary.html#how-throughout">throughout</a>, [Fixate Task](hedtsk_fixate.md) (Gaze is held on the fixation target while the main game is played)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A cue (peripheral flash or central arrow) indicates a likely target location.
    2. The target then appears at the cued or uncued location and participants detect or discriminate it.
* - **Manipulations**
  - - Cue type (exogenous/peripheral, endogenous/central, double/alerting)
    - Cue validity (proportion valid trials)
    - SOA
    - Target task (detection vs. discrimination)
    - Fixation offset (gap vs. overlap)
    - Cue dimension (target feature vs. location)
    - Cue placement (within vs. between objects)
* - **Measurements**
  - - RT difference between valid and invalid trials (attention effect)
    - Costs (invalid - neutral) and benefits (neutral - valid)
    - IOR at long SOAs
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
* - Double-Cue Paradigm

    `hedvar_posner_spatial_cueing__double_cue_paradigm`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-alerting-cue">alerting cue</a>
  - -
  - Both boxes flash at once, so the cue warns that a target is coming without saying where; the cue becomes an alerting cue.
* - Feature-Based Cueing

    `hedvar_posner_spatial_cueing__feature_based_cueing`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-feature-cue">feature cue</a>
  - [Feature-based attention](../processes/selective_and_sustained_attention.md#hed-feature-based-attention)
  - The cue indicates a feature of the target (color, orientation) rather than its location.
* - Object-Based Cueing

    `hedvar_posner_spatial_cueing__object_based_cueing`
  - named form
  - [Object-based attention](../processes/selective_and_sustained_attention.md#hed-object-based-attention)
  - Two elongated objects replace the boxes and the cue sits at one end of one object, so the comparison is within versus between objects; the cue and response are unchanged.
* - Cross-Modal Cueing

    `hedvar_posner_spatial_cueing__cross_modal_cueing`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>, <a href="vocabulary.html#facet-stimulus-modality-tactile">tactile</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>, <a href="vocabulary.html#facet-stimulus-type-pressure">pressure</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-loudspeaker">loudspeaker</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception), [Somatosensory perception](../processes/face_and_object_perception.md#hed-somatosensory-perception)
  - The cue is a sound from one side or a touch on one hand while the target stays visual; only the cue's modality and device change.
* - Detection vs. Discrimination Targets

    `hedvar_posner_spatial_cueing__detection_vs_discrimination_targets`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-classify">classify</a>
  - -
  - The target job is either a single press for any target, as in the standard form, or a report of which of two target forms appeared.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Orienting](../processes/selective_and_sustained_attention.md#hed-orienting)
- [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
- [Attention shifting](../processes/selective_and_sustained_attention.md#hed-attention-shifting)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)

## Key references

- Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, 32(1), 3-25. ([DOI](https://doi.org/10.1080/00335558008248231), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7367577/))
- Corbetta, M., & Shulman, G. L. (2002). Control of goal-directed and stimulus-driven attention in the brain. *Nature Reviews Neuroscience*, 3(3), 201-215. ([DOI](https://doi.org/10.1038/nrn755), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11994752/))
- Corbetta, M., Kincade, J. M., Lewis, C., Snyder, A. Z., & Sapir, A. (2005). Neural basis and recovery of spatial attention deficits in spatial neglect. *Nature Neuroscience*, 8(11), 1603-1610. ([DOI](https://doi.org/10.1038/nn1574), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16234807/))

## Further references

- Chica, A. B., Martín-Arévalo, E., Botta, F., & Lupiáñez, J. (2014). The Spatial Orienting paradigm: How to design and interpret spatial attention experiments. *Neuroscience & Biobehavioral Reviews*, 40, 35-51. ([DOI](https://doi.org/10.1016/j.neubiorev.2014.01.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24462751/))
- Theeuwes, J. (2019). Goal-driven, stimulus-driven, and history-driven selection. *Current Opinion in Psychology*, 29, 97-101. ([DOI](https://doi.org/10.1016/j.copsyc.2018.12.024), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30711911/))
- Petersen, S. E., & Posner, M. I. (2012). The attention system of the human brain: 20 years after. *Annual Review of Neuroscience*, 35, 73-89. ([DOI](https://doi.org/10.1146/annurev-neuro-062111-150525), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22524787/))
- Dugué, L., Merriam, E. P., Heeger, D. J., & Carrasco, M. (2020). Differential impact of endogenous and exogenous attention on activity in human visual cortex. *Scientific Reports*, 10, 21274. ([DOI](https://doi.org/10.1038/s41598-020-78172-x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/33277552/))

## External links

- Cognitive Atlas: [Posner cueing task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949d17)

- CogPO: [Posner Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Posner_Task_Paradigm)

