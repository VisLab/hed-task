(hedtsk_contextual_cueing)=
# Contextual Cueing Task

**HED task ID:** `hedtsk_contextual_cueing`

**Family:** [Visual search and tracking tasks](families/visual_search_and_tracking.md) (also [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md))

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
  - 1. Visual search through letter arrays.
    2. Some spatial configurations repeat across blocks while others are novel.
    3. Participants find and respond to a target embedded in the display.
* - **Manipulations**
  - - Repeated vs. novel display configurations
    - Number of repetitions across blocks
    - Explicit awareness of repetition
* - **Measurements**
  - - RT advantage for repeated over novel configurations (contextual cueing effect)
    - Learning curve across blocks
    - Recognition test for repeated displays
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
  - The participant searches for a rotated T among rotated Ls and reports which way the T points. Unknown to the participant, half the displays repeat the same arrangement of items across blocks. Search gets faster on the repeated displays even though participants cannot tell them from new ones.
  - Canonical: repeated spatial configurations implicitly facilitate target detection
* - Configuration-Based vs. Association-Based CC

    `hedvar_contextual_cueing__configuration_based_vs_association_based_cc`
  - Repeated displays are built so that either the whole layout repeats, or only the pairing between the target's position and the positions of a few distractors repeats while the rest changes. Comparing the two shows what part of the context is being learned.
  - Separates global configuration from local target-distractor association; different learning conditions
* - Semantic Contextual Cueing

    `hedvar_contextual_cueing__semantic_contextual_cueing`
  - The search displays are photographs of real scenes with a target object placed somewhere in each. Scenes repeat across blocks, and the participant learns where the target is likely to be in a given scene.
  - Semantic scene content instead of arbitrary array; different memory system engaged
* - Cross-Modal Contextual Cueing

    `hedvar_contextual_cueing__cross_modal_contextual_cueing`
  - The repeated context is a sound or a touch pattern rather than a visual layout. A particular sound is paired with a particular target location, and search becomes faster when that sound plays.
  - Auditory context cues visual search; cross-modal learning paradigm
* - Dynamic Contextual Cueing

    `hedvar_contextual_cueing__dynamic_contextual_cueing`
  - The items in the search display move. What repeats is the pattern of motion and the target's eventual position rather than a fixed static layout, and the participant learns to find the target from the repeated motion pattern.
  - Moving-element arrays instead of static; different perceptual and memory demands
* - Transfer of Contextual Cueing

    `hedvar_contextual_cueing__transfer_of_contextual_cueing`
  - After the usual learning blocks, the repeated displays are altered in a test phase: distractor identities are changed, distractors are added or removed, or the target is moved to a new place in a familiar layout. Whether the speed-up survives shows what was learned.
  - Tests whether learned context transfers to new target locations; different probe phase
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

