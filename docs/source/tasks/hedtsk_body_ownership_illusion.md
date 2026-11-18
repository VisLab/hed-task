(hedtsk_body_ownership_illusion)=
# Body Ownership Illusion Task

**HED task ID:** `hedtsk_body_ownership_illusion`

**Family:** [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md)

**Also known as:** Rubber Hand Illusion, RHI, Full Body Illusion, Body Transfer Illusion, Virtual Hand Illusion, Enfacement Illusion, Multisensory Body Illusion

Synchronous multisensory stimulation of a participant's hidden body part and a visible fake or virtual counterpart induces illusory ownership of the artificial body part; proprioceptive drift, subjective ratings, and threat responses index the strength of the illusion.

## Description

Body ownership illusion tasks exploit multisensory integration to induce the experience that an artificial body part (or whole body) belongs to the participant. In the classic Rubber Hand Illusion (Botvinick & Cohen, 1998), a participant's real hand is hidden behind a screen while a realistic rubber hand is placed in an anatomically plausible position. Synchronous stroking of both hands with paintbrushes for 1-2 minutes typically produces a vivid sense of ownership over the rubber hand, accompanied by a proprioceptive shift (pointing error toward the rubber hand) and autonomic responses to threats directed at the rubber hand (elevated skin conductance). Asynchronous stroking serves as the critical control condition. The paradigm demonstrates that body ownership is a dynamic, multisensory construction rather than a fixed perceptual given. The illusion depends on spatial, temporal, and anatomical congruence of visual, tactile, and proprioceptive signals, and is modulated by top-down factors (body schema, visual realism, postural plausibility). Computational accounts frame the illusion as Bayesian causal inference over multisensory signals (Samad, Chung, & Shams, 2015). The paradigm has been extended to the whole body (Petkova & Ehrsson, 2008), to faces (enfacement illusion; Tsakiris, 2008), and to virtual reality environments (Slater et al., 2008). Clinical applications include phantom limb pain treatment, eating disorder body image interventions, and assessment of body representation disturbances in schizophrenia and depersonalization.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-undergo-stream">undergo stream</a>
- **What is the player told to do while it runs?** <a href="vocabulary.html#rule-undergo-stream-instruction-none">none</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-tactile">tactile</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-pressure">pressure</a>, <a href="vocabulary.html#facet-stimulus-type-real-objects">real objects</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-writing-device">writing device</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** An artificial hand (rubber, wooden or virtual) in view while the participant's hidden hand is stroked with a paintbrush in or out of time with it.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A participant's real body part is hidden while a visible artificial (rubber, virtual, or video-displayed) counterpart is placed in a plausible position.
    2. Synchronous multisensory stimulation (typically visuotactile stroking) is applied to both the real and artificial body parts, with asynchronous stimulation as a control.
    3. Optional: After the illusion is induced the experimenter threatens the rubber hand and the response to the threat is recorded.
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
* - Full Body Illusion (Body Swap)

    `hedvar_body_ownership_illusion__full_body_illusion_body_swap`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-head-mounted-display">head mounted display</a>, <a href="vocabulary.html#facet-task-io-device-writing-device">writing device</a>
  - -
  - The whole body replaces the hand, seen through a head-mounted display fed by cameras on a mannequin.
* - Virtual Hand / Virtual Body Illusion

    `hedvar_body_ownership_illusion__virtual_hand_virtual_body_illusion`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-head-mounted-display">head mounted display</a>, <a href="vocabulary.html#facet-task-io-device-writing-device">writing device</a>; experimental environment: <a href="vocabulary.html#facet-experimental-environment-virtual-world">virtual world</a>
  - -
  - A virtual hand or body in virtual reality moves with the participant or is touched in time with the real body.
* - Enfacement Illusion

    `hedvar_body_ownership_illusion__enfacement_illusion`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>, <a href="vocabulary.html#facet-stimulus-type-pressure">pressure</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>; report after: <a href="vocabulary.html#rule-undergo-stream-report-after-judgment">judgment</a>
  - [Face perception](../processes/face_and_object_perception.md#hed-face-perception), [Self-other distinction](../processes/social_cognition_and_strategic_social_choice.md#hed-self-other-distinction)
  - The participant's face is stroked in time with a video of another person's face being stroked, and afterwards they judge morphed faces as self or other, a judgment replacing the questionnaire rating.
* - Somatosensory Rubber Hand Illusion

    `hedvar_body_ownership_illusion__somatosensory_rubber_hand_illusion`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-tactile">tactile</a>
  - [Somatosensory perception](../processes/face_and_object_perception.md#hed-somatosensory-perception)
  - The participant is blindfolded and one of their hands is guided to stroke the rubber hand while the hidden hand is stroked the same way, so the illusion is induced without vision.
* - Kinesthetic Mirror Illusion

    `hedvar_body_ownership_illusion__kinesthetic_mirror_illusion`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-somatic">somatic</a>
  - [Proprioception](../processes/motor_preparation_timing_and_execution.md#hed-proprioception), [Somatosensory perception](../processes/face_and_object_perception.md#hed-somatosensory-perception)
  - A mirror between the hands puts the reflection of the moving hand where the still hand is, and the participant feels the hidden hand move; there is no stroking and no artificial hand.
* - Threat Response Paradigm

    `hedvar_body_ownership_illusion__threat_response_paradigm`
  - emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotion-induction">emotion induction</a>
  - -
  - After the illusion is induced the experimenter threatens the rubber hand, and the skin conductance or brain response to the threat is the measure.
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

