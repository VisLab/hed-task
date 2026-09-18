(hedtsk_contextual_cueing)=
# Contextual Cueing Task

**HED task ID:** `hedtsk_contextual_cueing`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md)

**Also known as:** CC Task

Visual search in which some distractor configurations repeat across blocks; faster search on repeated configurations indexes implicit spatial context learning.

## Description

Participants perform visual search for a T-shaped target among L-shaped distractors. Critically, half the search displays repeat across blocks (with the target always in the same location within a given repeated display), while the other half are newly generated on each block. Search becomes faster for repeated displays over blocks, even though participants cannot consciously recognize which displays have been repeated. Chun and Jiang (1998) demonstrated that this contextual cueing effect reflects implicit learning and memory for spatial configurations that guide spatial attention to the likely target location. The paradigm has become a standard tool for studying the interface between attention, implicit learning, and long-term memory.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Visual search through letter arrays; some spatial configurations repeat across blocks while others are novel. Participants find and respond to a target embedded in the display.
* - **Manipulation**
  - Repeated vs. novel display configurations; number of repetitions across blocks; explicit awareness of repetition.
* - **Measurement**
  - RT advantage for repeated over novel configurations (contextual cueing effect); learning curve across blocks; recognition test for repeated displays.
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
* - Standard Visual Search CC

    `hedvar_contextual_cueing__standard_visual_search_cc`
  - T among L's with repeated vs. novel configurations; the Chun & Jiang (1998) version.
  - Canonical: repeated spatial configurations implicitly facilitate target detection
* - Configuration-Based vs. Association-Based CC

    `hedvar_contextual_cueing__configuration_based_vs_association_based_cc`
  - Manipulating whether the entire configuration or just target-distractor associations drive the effect.
  - Separates global configuration from local target-distractor association; different learning conditions
* - Semantic Contextual Cueing

    `hedvar_contextual_cueing__semantic_contextual_cueing`
  - Meaningful scenes rather than letter arrays; contextual regularities in naturalistic visual environments.
  - Semantic scene content instead of arbitrary array; different memory system engaged
* - Cross-Modal Contextual Cueing

    `hedvar_contextual_cueing__cross_modal_contextual_cueing`
  - Auditory or tactile context associated with visual target locations.
  - Auditory context cues visual search; cross-modal learning paradigm
* - Dynamic Contextual Cueing

    `hedvar_contextual_cueing__dynamic_contextual_cueing`
  - Displays with moving elements; tests whether temporal-spatial regularities can be learned.
  - Moving-element arrays instead of static; different perceptual and memory demands
* - Transfer of Contextual Cueing

    `hedvar_contextual_cueing__transfer_of_contextual_cueing`
  - Changing distractor identities or adding/removing distractors to test what aspects of context are learned.
  - Tests whether learned context transfers to new target locations; different probe phase
```

## Cognitive processes

This task is designed to engage the following processes:

- [Implicit memory](../processes/implicit_and_statistical_learning.md#hed-implicit-memory)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)

## Key references

- Chun, M. M., & Jiang, Y. (1998). Contextual cueing: Implicit learning and memory of visual context guides spatial attention. *Cognitive Psychology*, 36(1), 28–71.
- Chun, M. M., & Jiang, Y. (2003). Implicit, long-term spatial contextual memory. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 29(2), 224–234.
- Goujon, A., Didierjean, A., & Thorpe, S. (2015). Investigating implicit statistical learning mechanisms through contextual cueing. *Trends in Cognitive Sciences*, 19(9), 524–533.

## Recent references

- Vadillo, M. A., Konstantinidis, E., & Shanks, D. R. (2022). Underpowered samples, false negatives, and unconscious learning. *Psychonomic Bulletin & Review*, 29, 307–337.
- Zinchenko, A., Conci, M., Müller, H. J., & Geyer, T. (2018). Predictive visual search: Role of environmental regularities in the learning of context cues. *Attention, Perception, & Psychophysics*, 80, 1096–1109.
- Sisk, C. A., Remington, R. W., & Jiang, Y. V. (2019). Mechanisms of contextual cueing: A tutorial review. *Attention, Perception, & Psychophysics*, 81, 2571–2589.
- Annac, E., Conci, M., Müller, H. J., & Geyer, T. (2017). Local item density modulates adaptation of learned contextual cues. *Visual Cognition*, 25(1–3), 262–277.

## External links

- Cognitive Atlas: [contextual cueing task](https://www.cognitiveatlas.org/task/id/trm_4f24492504ca0)

