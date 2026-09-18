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
  - A participant's real body part is hidden while a visible artificial (rubber, virtual, or video-displayed) counterpart is placed in a plausible position; synchronous multisensory stimulation (typically visuotactile stroking) is applied to both the real and artificial body parts, with asynchronous stimulation as a control.
* - **Manipulation**
  - Synchrony (synchronous vs. asynchronous stroking); modality of stimulation (visuotactile, visuomotor, visuoproprioceptive); body part (hand, arm, face, full body); realism of the artificial body part (rubber, wooden, virtual, incongruent object); spatial congruence (anatomically plausible vs. rotated position); temporal delay between seen and felt touch.
* - **Measurement**
  - Proprioceptive drift (pointing error toward the artificial body part, pre- vs. post-stimulation); subjective ownership questionnaire ratings; skin conductance response to threat directed at the artificial body part; skin temperature change of the real hand; onset latency of the illusion; grip force or other motor measures.
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
  - Botvinick & Cohen (1998): synchronous vs. asynchronous visuotactile stroking of hidden real hand and visible rubber hand. The foundational paradigm. Measures proprioceptive drift and subjective ownership.
  - Synchronous brush strokes on rubber hand and hidden real hand; canonical embodiment paradigm
* - Full Body Illusion (Body Swap)

    `hedvar_body_ownership_illusion__full_body_illusion_body_swap`
  - Petkova & Ehrsson (2008): head-mounted display shows a mannequin's first-person perspective while synchronous stroking is applied. Induces illusory ownership of an entire artificial body.
  - Full-body camera-to-HMD setup creates whole-body ownership; different from hand-only paradigm
* - Virtual Hand / Virtual Body Illusion

    `hedvar_body_ownership_illusion__virtual_hand_virtual_body_illusion`
  - Virtual reality implementation with a virtual hand or body that moves synchronously with the participant's real movements (visuomotor correlation). Allows parametric manipulation of appearance, delay, and spatial offset.
  - Virtual avatar hand in VR; different sensory integration conditions
* - Enfacement Illusion

    `hedvar_body_ownership_illusion__enfacement_illusion`
  - Tsakiris (2008): synchronous touching of participant's face and a viewed face (live video or another person). Shifts self-face recognition toward the other face. Tests facial body ownership.
  - Synchronous touch to face and rubber face; different body part and social dimension
* - Somatosensory Rubber Hand Illusion

    `hedvar_body_ownership_illusion__somatosensory_rubber_hand_illusion`
  - Participant touches the rubber hand with their hidden finger while their real hand is simultaneously stroked. Self-touch variant strengthens the ownership illusion through active tactile involvement.
  - Tactile stimulation without visual component; isolates tactile-proprioceptive integration
* - Kinesthetic Mirror Illusion

    `hedvar_body_ownership_illusion__kinesthetic_mirror_illusion`
  - Mirror placed at the body midline makes the reflection of one hand appear as the other. Active movement of the visible hand creates illusory movement of the hidden hand. Related to mirror therapy for phantom limb pain.
  - Proprioceptive/kinesthetic basis without visual rubber hand; different sensory modality
* - Threat Response Paradigm

    `hedvar_body_ownership_illusion__threat_response_paradigm`
  - After inducing the illusion, a threatening stimulus (needle, knife, hammer) is directed at the rubber hand. Skin conductance response magnitude indexes the strength of embodiment.
  - Threatening stimulus applied to rubber hand; measures embodiment via threat response
* - Incongruent Object Control

    `hedvar_body_ownership_illusion__incongruent_object_control`
  - Replace the rubber hand with a non-hand object (wooden block, rubber ball). Tests whether anatomical plausibility is necessary for the illusion. Typically produces no ownership.
  - Non-hand object used instead of rubber hand; tests specificity of body-form requirement
```

## Cognitive processes

This task is designed to engage the following processes:

- [Body ownership](../processes/awareness_agency_and_metacognition.md#hed-body-ownership)
- [Interoceptive awareness](../processes/awareness_agency_and_metacognition.md#hed-interoceptive-awareness)
- [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing)

## Key references

- Botvinick, M., & Cohen, J. (1998). Rubber hands 'feel' touch that eyes see. *Nature*, 391(6669), 756.
- Tsakiris, M. (2010). My body in the brain: A neurocognitive model of body-ownership. *Neuropsychologia*, 48(3), 703-712.

## Recent references

- Kilteni, K., Maselli, A., Kording, K. P., & Slater, M. (2015). Over my fake body: Body ownership illusions for studying the multisensory basis of own-body perception. *Frontiers in Human Neuroscience*, 9, 141.
- Samad, M., Chung, A. J., & Shams, L. (2015). Perception of body ownership is driven by Bayesian sensory inference. *PLoS ONE*, 10(2), e0117178.
- Petkova, V. I., & Ehrsson, H. H. (2008). If I were you: Perceptual illusion of body swapping. *PLoS ONE*, 3(12), e3832.
- Moseley, G. L., Olthof, N., Venema, A., Don, S., Wijers, M., Gallace, A., & Spence, C. (2008). Psychologically induced cooling of a specific body part caused by the illusory ownership of an artificial counterpart. *Proceedings of the National Academy of Sciences*, 105(35), 13169-13173.

## External links

- Cognitive Atlas: [rubber hand illusion](https://www.cognitiveatlas.org/task/id/trm_4e5bb14d814a8) (close match)

