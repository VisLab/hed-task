(hedtsk_contextual_cueing)=
# Contextual Cueing Task

**HED task ID:** `hedtsk_contextual_cueing`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md) (also [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md))

**Also known as:** CC Task

Visual search in which some distractor configurations repeat across blocks; faster search on repeated configurations indexes implicit spatial context learning.

## Description

Participants perform visual search for a T-shaped target among L-shaped distractors. Critically, half the search displays repeat across blocks (with the target always in the same location within a given repeated display), while the other half are newly generated on each block. Search becomes faster for repeated displays over blocks, even though participants cannot consciously recognize which displays have been repeated. Chun and Jiang (1998) demonstrated that this contextual cueing effect reflects implicit learning and memory for spatial configurations that guide spatial attention to the likely target location. The paradigm has become a standard tool for studying the interface between attention, implicit learning, and long-term memory.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
  - *Where does the rule come from?* <a href="vocabulary.html#rule-respond-to-rule-rule-source-hidden-regularity">hidden regularity</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-repetitions">number of repetitions</a>
- **Material:** A T-shaped target among L-shaped distractors, in spatial configurations that either repeat across blocks or are new.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Visual search through letter arrays.
    2. Some spatial configurations repeat across blocks while others are novel.
    3. Participants find and respond to a target embedded in the display.
    4. Optional: After the learning blocks a test phase alters the repeated displays to see whether the speed-up survives.
* - **Manipulations**
  - - Repeated vs. novel display configurations
    - Number of repetitions across blocks
    - Explicit awareness of repetition
    - Display type (real-world scenes vs. letter arrays)
* - **Measurements**
  - - RT advantage for repeated over novel configurations (contextual cueing effect)
    - Learning curve across blocks
    - Recognition test for repeated displays
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
* - Configuration-Based vs. Association-Based CC

    `hedvar_contextual_cueing__configuration_based_vs_association_based_cc`
  - named form
  - -
  - Either the whole layout repeats or only the pairing of target position with a few distractor positions, to see which is learned.
* - Semantic Contextual Cueing

    `hedvar_contextual_cueing__semantic_contextual_cueing`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>
  - -
  - The displays are photographs of real scenes with a target object placed in each, and the scenes repeat across blocks.
* - Cross-Modal Contextual Cueing

    `hedvar_contextual_cueing__cross_modal_contextual_cueing`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>, <a href="vocabulary.html#facet-stimulus-modality-tactile">tactile</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>, <a href="vocabulary.html#facet-stimulus-type-vibration">vibration</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>; cue: <a href="vocabulary.html#rule-respond-to-rule-cue-location-cue">location cue</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception), [Somatosensory perception](../processes/face_and_object_perception.md#hed-somatosensory-perception)
  - A sound or touch pattern, rather than the visual layout, is paired with the target location and search speeds up when it plays; the learned sound works as a location cue whose validity is discovered rather than instructed.
* - Dynamic Contextual Cueing

    `hedvar_contextual_cueing__dynamic_contextual_cueing`
  - named form
  - -
  - The search items move and what repeats is the motion pattern and the target's final position rather than a static layout.
* - Transfer of Contextual Cueing

    `hedvar_contextual_cueing__transfer_of_contextual_cueing`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-transfer">transfer</a>
  - -
  - After the learning blocks a test phase alters the repeated displays (the distractor identities, their number, or the target position) to see whether the speed-up survives.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Implicit memory](../processes/implicit_and_statistical_learning.md#hed-implicit-memory)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)

## Key references

- Chun, M. M., & Jiang, Y. (1998). Contextual cueing: Implicit learning and memory of visual context guides spatial attention. *Cognitive Psychology*, 36(1), 28-71. ([DOI](https://doi.org/10.1006/cogp.1998.0681), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9679076/))
- Chun, M. M., & Jiang, Y. (2003). Implicit, long-term spatial contextual memory. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 29(2), 224-234. ([DOI](https://doi.org/10.1037/0278-7393.29.2.224), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12696811/))
- Goujon, A., Didierjean, A., & Thorpe, S. (2015). Investigating implicit statistical learning mechanisms through contextual cueing. *Trends in Cognitive Sciences*, 19(9), 524-533. ([DOI](https://doi.org/10.1016/j.tics.2015.07.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26255970/))

## Further references

- Vadillo, M. A., Konstantinidis, E., & Shanks, D. R. (2022). Underpowered samples, false negatives, and unconscious learning. *Psychonomic Bulletin & Review*, 29, 307-337.
- Zinchenko, A., Conci, M., Müller, H. J., & Geyer, T. (2018). Predictive visual search: Role of environmental regularities in the learning of context cues. *Attention, Perception, & Psychophysics*, 80, 1096-1109. ([DOI](https://doi.org/10.3758/s13414-018-1500-4), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29600489/))
- Sisk, C. A., Remington, R. W., & Jiang, Y. V. (2019). Mechanisms of contextual cueing: A tutorial review. *Attention, Perception, & Psychophysics*, 81, 2571-2589. ([DOI](https://doi.org/10.3758/s13414-019-01832-2), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31410759/))
- Annac, E., Conci, M., Müller, H. J., & Geyer, T. (2017). Local item density modulates adaptation of learned contextual cues. *Visual Cognition*, 25(1-3), 262-277. ([DOI](https://doi.org/10.1080/13506285.2017.1339158))

## External links

- Cognitive Atlas: [contextual cueing task](https://www.cognitiveatlas.org/task/id/trm_4f24492504ca0)

