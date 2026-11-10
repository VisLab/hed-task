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
  - 1. A cue (peripheral flash or central arrow) indicates a likely target location.
    2. The target then appears at the cued or uncued location and participants detect or discriminate it.
* - **Manipulations**
  - - Cue type (exogenous/peripheral vs. endogenous/central)
    - Cue validity (proportion valid trials)
    - SOA
    - Target task (detection vs. discrimination)
* - **Measurements**
  - - RT difference between valid and invalid trials (attention effect)
    - Costs (invalid − neutral) and benefits (neutral − valid)
    - IOR at long SOAs
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
  - The participant fixates the center while two boxes sit to the left and right. One box briefly brightens, and shortly afterwards a target appears in one of the boxes. The participant responds to the target as fast as possible. The flash pulls attention to that side automatically, so targets there are detected faster.
  - Peripheral onset cue drives automatic orienting; canonical exogenous attention
* - Endogenous (Central) Cueing

    `hedvar_posner_spatial_cueing__endogenous_central_cueing`
  - The cue is an arrow or other symbol at fixation pointing to the side where the target is likely to appear. The participant must interpret the cue and shift attention deliberately, which takes longer than a flash.
  - Central arrow cue drives voluntary orienting; different mechanism
* - Valid, Invalid, and Neutral Cue Conditions

    `hedvar_posner_spatial_cueing__valid_invalid_and_neutral_cue_conditions`
  - Three kinds of trial are mixed: the cue correctly indicates the target side (valid), indicates the wrong side (invalid), or gives no side information (neutral). The benefit of a valid cue and the cost of an invalid one are measured against the neutral trials.
  - Three cue validity conditions test benefit and cost of orienting
* - Inhibition of Return (IOR) Paradigm

    `hedvar_posner_spatial_cueing__inhibition_of_return_ior_paradigm`
  - A flash cue is used and the delay before the target is lengthened beyond about 300 ms. At these delays targets at the flashed location are detected more slowly, not faster, as attention has moved on and is reluctant to return.
  - Long SOA reverses validity benefit; distinct temporal structure
* - Gap vs. Overlap Conditions

    `hedvar_posner_spatial_cueing__gap_vs_overlap_conditions`
  - The fixation point either disappears shortly before the cue (gap) or stays on (overlap). Removing fixation makes it easier to disengage attention and speeds responses.
  - Fixation offset before/during cue changes alerting
* - Double-Cue Paradigm

    `hedvar_posner_spatial_cueing__double_cue_paradigm`
  - Both boxes flash at the same time, so the participant is alerted that a target is coming but gets no information about which side. Comparing with single flashes separates the alerting effect from the orienting effect.
  - Both locations cued simultaneously; tests alerting without orienting
* - Predictive vs. Non-Predictive Cues

    `hedvar_posner_spatial_cueing__predictive_vs_non_predictive_cues`
  - The proportion of trials on which the cue correctly indicates the target side is varied, for example 50 percent (uninformative), 75 percent or 100 percent. Only informative cues encourage the participant to shift attention deliberately.
  - Cue validity changes attentional weight given to cue
* - Feature-Based Cueing

    `hedvar_posner_spatial_cueing__feature_based_cueing`
  - The cue indicates a feature of the target, such as its color or orientation, rather than its location. Tests whether attention can be directed to a feature across the whole display.
  - Feature rather than location cued; tests feature-based attention
* - Object-Based Cueing

    `hedvar_posner_spatial_cueing__object_based_cueing`
  - Two elongated objects are shown and the cue appears at one end of one object. Targets at the uncued end of the same object are detected faster than targets at an equally distant location on the other object.
  - Object defines cued location; tests object-based attention
* - Cross-Modal Cueing

    `hedvar_posner_spatial_cueing__cross_modal_cueing`
  - The cue is a sound from the left or right, or a touch on one hand, and the target is visual. Tests whether attention directed by one sense benefits another.
  - Auditory or tactile cue precedes visual target; cross-modal orienting
* - Detection vs. Discrimination Targets

    `hedvar_posner_spatial_cueing__detection_vs_discrimination_targets`
  - In the detection version the participant presses one key as soon as any target appears. In the discrimination version the target has one of two forms and the participant reports which, for example its orientation or identity.
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

- Posner, M. I. (1980). Orienting of attention. *Quarterly Journal of Experimental Psychology*, 32(1), 3-25. ([DOI](https://doi.org/10.1080/00335558008248231), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7367577/))
- Corbetta, M., & Shulman, G. L. (2002). Control of goal-directed and stimulus-driven attention in the brain. *Nature Reviews Neuroscience*, 3(3), 201-215. ([DOI](https://doi.org/10.1038/nrn755), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11994752/))
- Corbetta, M., Kincade, J. M., Lewis, C., Snyder, A. Z., & Sapir, A. (2005). Neural basis and recovery of spatial attention deficits in spatial neglect. *Nature Neuroscience*, 8(11), 1603-1610. ([DOI](https://doi.org/10.1038/nn1574), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16234807/))

## Further references

- Chica, A. B., Martín-Arévalo, E., Botta, F., & Lupiáñez, J. (2014). The Spatial Orienting paradigm: How to design and interpret spatial attention experiments. *Neuroscience & Biobehavioral Reviews*, 40, 35–51. ([DOI](https://doi.org/10.1016/j.neubiorev.2014.01.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24462751/))
- Theeuwes, J. (2019). Goal-driven, stimulus-driven, and history-driven selection. *Current Opinion in Psychology*, 29, 97–101. ([DOI](https://doi.org/10.1016/j.copsyc.2018.12.024), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30711911/))
- Petersen, S. E., & Posner, M. I. (2012). The attention system of the human brain: 20 years after. *Annual Review of Neuroscience*, 35, 73–89. ([DOI](https://doi.org/10.1146/annurev-neuro-062111-150525), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22524787/))
- Dugué, L., Merriam, E. P., Heeger, D. J., & Carrasco, M. (2020). Differential impact of endogenous and exogenous attention on activity in human visual cortex. *Scientific Reports*, 10, 21274. ([DOI](https://doi.org/10.1038/s41598-020-78172-x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/33277552/))

## External links

- Cognitive Atlas: [Posner cueing task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949d17)

- CogPO: [Posner Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Posner_Task_Paradigm)

