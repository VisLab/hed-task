(hedtsk_posner_spatial_cueing)=
# Posner Spatial Cueing Task

**HED task ID:** `hedtsk_posner_spatial_cueing`

**Family:** [Attentional cueing and orienting tasks](families/attentional_cueing.md)

**Also known as:** Posner Task, Spatial Cueing Task

A central or peripheral cue indicates the likely target location; RT differences between valid, neutral, and invalid cues index covert spatial orienting.

## Description

The Posner Spatial Cueing Task measures covert orienting of visual attention. Participants fixate on a central point with two peripheral locations marked. A cue stimulus appears (exogenous: at the target location; or endogenous: a central arrow) followed by a target stimulus at one of the peripheral locations. Cues can be valid (same location as target) or invalid (opposite location). The cueing effect (faster RT to validly cued targets vs. invalidly cued) reflects the cost and benefit of attentional orienting. The task dissociates different components of attention: engaging, disengaging, and shifting.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A cue (peripheral flash or central arrow) indicates a likely target location; the target then appears at the cued or uncued location and participants detect or discriminate it.
* - **Manipulation**
  - Cue type (exogenous/peripheral vs. endogenous/central); cue validity (proportion valid trials); SOA; target task (detection vs. discrimination).
* - **Measurement**
  - RT difference between valid and invalid trials (attention effect); costs (invalid − neutral) and benefits (neutral − valid); IOR at long SOAs.
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
* - Exogenous (Peripheral) Cueing

    `hedvar_posner_spatial_cueing__exogenous_peripheral_cueing`
  - Abrupt-onset cue at potential target location; captures attention reflexively.
  - Peripheral onset cue drives automatic orienting; canonical exogenous attention
* - Endogenous (Central) Cueing

    `hedvar_posner_spatial_cueing__endogenous_central_cueing`
  - Central symbolic cue (arrow, letter) indicating likely target location; requires volitional orienting.
  - Central arrow cue drives voluntary orienting; different mechanism
* - Valid, Invalid, and Neutral Cue Conditions

    `hedvar_posner_spatial_cueing__valid_invalid_and_neutral_cue_conditions`
  - Standard design decomposing attention effects into costs (invalid minus neutral) and benefits (neutral minus valid).
  - Three cue validity conditions test benefit and cost of orienting
* - Inhibition of Return (IOR) Paradigm

    `hedvar_posner_spatial_cueing__inhibition_of_return_ior_paradigm`
  - Long cue-target SOAs (>300 ms) with peripheral cues revealing inhibitory tagging of previously attended locations.
  - Long SOA reverses validity benefit; distinct temporal structure
* - Gap vs. Overlap Conditions

    `hedvar_posner_spatial_cueing__gap_vs_overlap_conditions`
  - Fixation point disappears (gap) or remains (overlap) at cue onset; modulates saccade latency and disengagement.
  - Fixation offset before/during cue changes alerting
* - Double-Cue Paradigm

    `hedvar_posner_spatial_cueing__double_cue_paradigm`
  - Two successive cues to examine dynamic reorienting.
  - Both locations cued simultaneously; tests alerting without orienting
* - Predictive vs. Non-Predictive Cues

    `hedvar_posner_spatial_cueing__predictive_vs_non_predictive_cues`
  - Cues with varying validity ratios (50%, 75%, 100%) to separate voluntary from reflexive orienting.
  - Cue validity changes attentional weight given to cue
* - Feature-Based Cueing

    `hedvar_posner_spatial_cueing__feature_based_cueing`
  - Cueing attention to a feature dimension (color, orientation) rather than a spatial location.
  - Feature rather than location cued; tests feature-based attention
* - Object-Based Cueing

    `hedvar_posner_spatial_cueing__object_based_cueing`
  - Cueing within vs. between objects to study object-based attention.
  - Object defines cued location; tests object-based attention
* - Cross-Modal Cueing

    `hedvar_posner_spatial_cueing__cross_modal_cueing`
  - Auditory or tactile cues directing visual spatial attention.
  - Auditory or tactile cue precedes visual target; cross-modal orienting
* - Detection vs. Discrimination Targets

    `hedvar_posner_spatial_cueing__detection_vs_discrimination_targets`
  - Simple detection tasks vs. discrimination (identity, orientation) at cued locations.
  - Simple detection vs. identity discrimination; different response task
```

## Cognitive processes

This task is designed to engage the following processes:

- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Orienting](../processes/selective_and_sustained_attention.md#hed-orienting)
- [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
- [Attention shifting](../processes/selective_and_sustained_attention.md#hed-attention-shifting)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)

## Key references

- Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, 32(1), 3-25.
- Corbetta, M., & Shulman, G. L. (2002). Control of goal-directed and stimulus-driven attention in the brain. *Nature Reviews Neuroscience*, 3(3), 201-215.
- Corbetta, M., Kincade, J. M., Lewis, C., Snyder, A. Z., & Sapir, A. (2005). Neural basis and recovery of spatial attention deficits in spatial neglect. *Nature Neuroscience*, 8(11), 1603-1610.

## Recent references

- Chica, A. B., Martín-Arévalo, E., Botta, F., & Lupiáñez, J. (2014). The Spatial Orienting paradigm: How to design and interpret spatial attention experiments. *Neuroscience & Biobehavioral Reviews*, 40, 35–51.
- Theeuwes, J. (2019). Goal-driven, stimulus-driven, and history-driven selection. *Current Opinion in Psychology*, 29, 97–101.
- Petersen, S. E., & Posner, M. I. (2012). The attention system of the human brain: 20 years after. *Annual Review of Neuroscience*, 35, 73–89.
- Dugué, L., Merriam, E. P., Heeger, D. J., & Carrasco, M. (2020). Differential impact of endogenous and exogenous attention on activity in human visual cortex. *Scientific Reports*, 10, 21274.

## External links

- Cognitive Atlas: [Posner cueing task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949d17)

