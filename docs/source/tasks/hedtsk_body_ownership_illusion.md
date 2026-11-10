(hedtsk_body_ownership_illusion)=
# Body Ownership Illusion Task

**HED task ID:** `hedtsk_body_ownership_illusion`

**Family:** [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md)

**Also known as:** Rubber Hand Illusion, RHI, Full Body Illusion, Body Transfer Illusion, Virtual Hand Illusion, Enfacement Illusion, Multisensory Body Illusion

Synchronous multisensory stimulation of a participant's hidden body part and a visible fake or virtual counterpart induces illusory ownership of the artificial body part; proprioceptive drift, subjective ratings, and threat responses index the strength of the illusion.

## Description

Body ownership illusion tasks exploit multisensory integration to induce the experience that an artificial body part (or whole body) belongs to the participant. In the classic Rubber Hand Illusion (Botvinick & Cohen, 1998), a participant's real hand is hidden behind a screen while a realistic rubber hand is placed in an anatomically plausible position. Synchronous stroking of both hands with paintbrushes for 1-2 minutes typically produces a vivid sense of ownership over the rubber hand, accompanied by a proprioceptive shift (pointing error toward the rubber hand) and autonomic responses to threats directed at the rubber hand (elevated skin conductance). Asynchronous stroking serves as the critical control condition. The paradigm demonstrates that body ownership is a dynamic, multisensory construction rather than a fixed perceptual given. The illusion depends on spatial, temporal, and anatomical congruence of visual, tactile, and proprioceptive signals, and is modulated by top-down factors (body schema, visual realism, postural plausibility). Computational accounts frame the illusion as Bayesian causal inference over multisensory signals (Samad, Chung, & Shams, 2015). The paradigm has been extended to the whole body (Petkova & Ehrsson, 2008), to faces (enfacement illusion; Tsakiris, 2008), and to virtual reality environments (Slater et al., 2008). Clinical applications include phantom limb pain treatment, eating disorder body image interventions, and assessment of body representation disturbances in schizophrenia and depersonalization.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A participant's real body part is hidden while a visible artificial (rubber, virtual, or video-displayed) counterpart is placed in a plausible position.
    2. Synchronous multisensory stimulation (typically visuotactile stroking) is applied to both the real and artificial body parts, with asynchronous stimulation as a control.
* - **Manipulations**
  - - Synchrony (synchronous vs. asynchronous stroking)
    - Modality of stimulation (visuotactile, visuomotor, visuoproprioceptive)
    - Body part (hand, arm, face, full body)
    - Realism of the artificial body part (rubber, wooden, virtual, incongruent object)
    - Spatial congruence (anatomically plausible vs. rotated position)
    - Temporal delay between seen and felt touch
* - **Measurements**
  - - Proprioceptive drift (pointing error toward the artificial body part, pre- vs. post-stimulation)
    - Subjective ownership questionnaire ratings
    - Skin conductance response to threat directed at the artificial body part
    - Skin temperature change of the real hand
    - Onset latency of the illusion
    - Grip force or other motor measures
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
* - Classic Rubber Hand Illusion

    `hedvar_body_ownership_illusion__classic_rubber_hand_illusion`
  - The participant's real hand is hidden behind a screen and a rubber hand is placed in view where the real hand would be. The experimenter strokes both hands with brushes at the same time for a minute or two. Most people begin to feel the rubber hand is their own. When the strokes are out of time with each other, the feeling does not arise. Afterwards the participant points to where they feel their hand is and answers questions about the experience.
  - Synchronous brush strokes on rubber hand and hidden real hand; canonical embodiment paradigm
* - Full Body Illusion (Body Swap)

    `hedvar_body_ownership_illusion__full_body_illusion_body_swap`
  - The participant wears a head-mounted display showing the view from cameras on a mannequin's head, so they see the mannequin's body where their own should be. The experimenter touches the participant's body and the mannequin's body at the same time, and the participant comes to feel the mannequin's body is theirs.
  - Full-body camera-to-HMD setup creates whole-body ownership; different from hand-only paradigm
* - Virtual Hand / Virtual Body Illusion

    `hedvar_body_ownership_illusion__virtual_hand_virtual_body_illusion`
  - A virtual hand or body is shown in virtual reality and moves when the participant moves, or is touched in time with touches to the real body. The appearance, delay and position of the virtual body can be changed at will.
  - Virtual avatar hand in VR; different sensory integration conditions
* - Enfacement Illusion

    `hedvar_body_ownership_illusion__enfacement_illusion`
  - The participant watches a video of another person's face being stroked with a brush while their own face is stroked in the same place at the same time. Afterwards they are more likely to judge faces morphed between their own and the other person's as their own.
  - Synchronous touch to face and rubber face; different body part and social dimension
* - Somatosensory Rubber Hand Illusion

    `hedvar_body_ownership_illusion__somatosensory_rubber_hand_illusion`
  - The participant is blindfolded. The experimenter guides the participant's one hand to stroke the rubber hand while stroking the participant's other, hidden hand in the same way. The illusion arises from touch and position sense alone, without vision.
  - Tactile stimulation without visual component; isolates tactile-proprioceptive integration
* - Kinesthetic Mirror Illusion

    `hedvar_body_ownership_illusion__kinesthetic_mirror_illusion`
  - A mirror is placed between the participant's hands so that the reflection of one hand appears where the other hand is. When the visible hand moves, the participant feels the hidden hand moving too, even if it is still.
  - Proprioceptive/kinesthetic basis without visual rubber hand; different sensory modality
* - Threat Response Paradigm

    `hedvar_body_ownership_illusion__threat_response_paradigm`
  - After the illusion has been induced, the experimenter suddenly stabs toward or bends back the rubber hand. The participant's skin conductance rise or brain response to the threat measures how much the rubber hand has been taken as their own.
  - Threatening stimulus applied to rubber hand; measures embodiment via threat response
* - Incongruent Object Control

    `hedvar_body_ownership_illusion__incongruent_object_control`
  - A wooden block, a rubber ball or a rubber hand in an impossible position is used in place of the properly placed rubber hand, with the same synchronous stroking. The illusion normally fails, showing that the object must look like a hand in a plausible place.
  - Non-hand object used instead of rubber hand; tests specificity of body-form requirement
```

## Cognitive processes

This task is designed to engage the following processes:

- [Body ownership](../processes/awareness_agency_and_metacognition.md#hed-body-ownership)
- [Interoceptive awareness](../processes/awareness_agency_and_metacognition.md#hed-interoceptive-awareness)
- [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing)

## Key references

- Botvinick, M., & Cohen, J. (1998). Rubber hands 'feel' touch that eyes see. *Nature*, 391(6669), 756. ([DOI](https://doi.org/10.1038/35784), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9486643/))
- Tsakiris, M. (2010). My body in the brain: A neurocognitive model of body-ownership. *Neuropsychologia*, 48(3), 703-712. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2009.09.034), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19819247/))

## Further references

- Kilteni, K., Maselli, A., Kording, K. P., & Slater, M. (2015). Over my fake body: Body ownership illusions for studying the multisensory basis of own-body perception. *Frontiers in Human Neuroscience*, 9, 141. ([DOI](https://doi.org/10.3389/fnhum.2015.00141), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25852524/))
- Samad, M., Chung, A. J., & Shams, L. (2015). Perception of body ownership is driven by Bayesian sensory inference. *PLoS ONE*, 10(2), e0117178. ([DOI](https://doi.org/10.1371/journal.pone.0117178), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25658822/))
- Petkova, V. I., & Ehrsson, H. H. (2008). If I were you: Perceptual illusion of body swapping. *PLoS ONE*, 3(12), e3832. ([DOI](https://doi.org/10.1371/journal.pone.0003832), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19050755/))
- Moseley, G. L., Olthof, N., Venema, A., Don, S., Wijers, M., Gallace, A., & Spence, C. (2008). Psychologically induced cooling of a specific body part caused by the illusory ownership of an artificial counterpart. *Proceedings of the National Academy of Sciences*, 105(35), 13169-13173. ([DOI](https://doi.org/10.1073/pnas.0803768105), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18725630/))

## External links

- Cognitive Atlas: [rubber hand illusion](https://www.cognitiveatlas.org/task/id/trm_4e5bb14d814a8) (close match)

