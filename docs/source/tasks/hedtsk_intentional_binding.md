(hedtsk_intentional_binding)=
# Intentional Binding Task

**HED task ID:** `hedtsk_intentional_binding`

**Family:** [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md)

**Also known as:** Temporal Binding Task, Action-Effect Binding Task, Libet Clock Binding Task, Interval Estimation Agency Task

Participants judge the perceived time of a voluntary action and/or its sensory effect using a Libet clock; the temporal compression between action and effect (intentional binding) indexes the implicit sense of agency.

## Description

The Intentional Binding Task (Haggard, Clark, & Kalogeras, 2002) measures the implicit sense of agency through perceived temporal shifts between voluntary actions and their sensory consequences. Participants watch a rotating clock hand (Libet clock) and make voluntary key presses that produce a tone after a fixed delay (typically 250 ms). In separate blocks, they report either the perceived time of their action (action binding: judged time shifts toward the tone) or the perceived time of the tone (effect binding: judged time shifts toward the action). The net temporal compression between action and effect - intentional binding - is taken as an implicit, pre-reflective marker of the sense of agency. Involuntary actions (e.g., TMS-induced movements) or externally triggered tones produce temporal repulsion rather than binding, establishing the specificity of the effect to voluntary agency. The paradigm has become the standard implicit measure of sense of agency, complementing explicit agency judgments. It is sensitive to disorders of agency including schizophrenia (reduced binding, especially in patients with passivity experiences), functional neurological disorder, and anarchic hand syndrome. Computational accounts link binding to motor prediction: the forward model predicts sensory consequences of voluntary actions, and the match between prediction and outcome generates the binding effect.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-report-on-self">report on self</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-delay-to-outcome">delay to outcome</a>, <a href="vocabulary.html#setting-reward-probability">reward probability</a>
- **Material:** A rotating clock hand (Libet clock) and a tone that follows the key press after a fixed delay.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants make voluntary actions (key presses) that produce delayed sensory effects (tones) while monitoring a Libet clock.
    2. They report the perceived time of either the action or the effect in separate blocks.
* - **Manipulations**
  - - Action type (voluntary vs. involuntary/TMS-induced vs. passive observation)
    - Action-effect interval (150, 250, 450, 650 ms)
    - Effect probability (certain vs. uncertain)
    - Causal belief (participant told action causes vs. does not cause effect)
    - Outcome valence (positive vs. negative vs. neutral tone)
    - Social agency (self-caused vs. other-caused)
* - **Measurements**
  - - Action binding (shift of perceived action time toward the effect)
    - Effect binding (shift of perceived effect time toward the action)
    - Overall intentional binding (action binding + effect binding)
    - Interval estimation (judged action-effect interval vs. actual)
    - Binding magnitude as individual-difference variable
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
* - Interval Estimation Method

    `hedvar_intentional_binding__interval_estimation_method`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - -
  - No clock is shown; after each key press and tone the participant estimates or reproduces the interval between them, instead of reporting a time point.
* - Involuntary Action Control (TMS)

    `hedvar_intentional_binding__involuntary_action_control_tms`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-brain-stimulator">brain stimulator</a>
  - -
  - The finger movement is produced by a magnetic pulse to motor cortex rather than by the participant's decision, the action-type manipulation at its involuntary level, delivered with a brain stimulator.
* - Social Intentional Binding

    `hedvar_intentional_binding__social_intentional_binding`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>
  - [Self-other distinction](../processes/social_cognition_and_strategic_social_choice.md#hed-self-other-distinction)
  - Another person presses the key and the participant judges the timing of that person's action and its tone, or two people act together, so the reported event is someone else's action rather than one's own.
* - Outcome Valence Manipulation

    `hedvar_intentional_binding__outcome_valence_manipulation`
  - emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-nonvocal-sounds">nonvocal sounds</a>, <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>; drive: <a href="vocabulary.html#motivation-drive-unearned-outcome">unearned outcome</a>; sign: <a href="vocabulary.html#motivation-sign-both">both</a>; earned by: <a href="vocabulary.html#motivation-earned-by-nothing">nothing</a>; what: <a href="vocabulary.html#motivation-what-money">money</a>
  - -
  - The press produces a pleasant, unpleasant or neutral sound, or wins or loses money, and binding is compared across outcomes.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Sense of agency](../processes/awareness_agency_and_metacognition.md#hed-sense-of-agency)
- [Motor planning](../processes/motor_preparation_timing_and_execution.md#hed-motor-planning)
- [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)

## Key references

- Haggard, P., Clark, S., & Kalogeras, J. (2002). Voluntary action and conscious awareness. Nature Neuroscience, 5(4), 382-385. ([DOI](https://doi.org/10.1038/nn827), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11896397/))
- Moore, J. W., & Obhi, S. S. (2012). Intentional binding and the sense of agency: A review. Consciousness and Cognition, 21(1), 546-561. ([DOI](https://doi.org/10.1016/j.concog.2011.12.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22240158/))
- Wolpe, N., Haggard, P., Siebner, H. R., & Rowe, J. B. (2013). Cue integration and the perception of action in intentional binding. Experimental Brain Research, 229(3), 467-474. ([DOI](https://doi.org/10.1007/s00221-013-3419-2), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23371752/))

## Further references

- Voss, M., Moore, J., Hauser, M., Gallinat, J., Heinz, A., & Haggard, P. (2010). Altered awareness of action in schizophrenia: A specific deficit in predicting action consequences. Brain, 133(10), 3104-3112. ([DOI](https://doi.org/10.1093/brain/awq152), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20685805/))
- Borhani, K., Beck, B., & Haggard, P. (2017). Choosing, doing, and controlling: Implicit sense of agency over somatosensory events. Psychological Science, 28(7), 882-893. ([DOI](https://doi.org/10.1177/0956797617697693), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28488908/))
- Suzuki, K., Lush, P., Seth, A. K., & Roseboom, W. (2019). Intentional binding without intentional action. Psychological Science, 30(6), 842-853. ([DOI](https://doi.org/10.1177/0956797619842191), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31023161/))

## External links

- Cognitive Atlas: [Interval Estimation Task](https://www.cognitiveatlas.org/task/id/tsk_YShVp2KOuWrSS) (related match)

