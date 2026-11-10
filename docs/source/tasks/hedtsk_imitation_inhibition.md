(hedtsk_imitation_inhibition)=
# Imitation-Inhibition Task

**HED task ID:** `hedtsk_imitation_inhibition`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Automatic Imitation Task, Automatic Imitation, Brass Imitation Task, Stimulus-Response Compatibility Imitation Task, Action Observation Compatibility Task

Execute an instructed finger movement while observing a congruent or incongruent action performed by another person; the congruency effect (faster responses on congruent trials) indexes automatic imitation and the cost of inhibiting observed-action representations.

## Description

The Imitation-Inhibition Task (Brass, Bekkering, Wohlschlager, & Prinz, 2000) measures the involuntary tendency to copy observed actions and the executive cost of suppressing that tendency. Participants are cued to perform a simple action (e.g., lift the index finger when a number '1' appears) while simultaneously viewing a task-irrelevant video of another person's hand performing either the same action (congruent), a different action (incongruent, e.g., lifting the middle finger), or no action (neutral/static hand). The congruency effect -- faster and more accurate responses on congruent than incongruent trials -- indexes automatic imitation, while the interference effect (incongruent minus neutral) specifically indexes the inhibitory cost of suppressing the observed action. The paradigm is grounded in common-coding / ideomotor theory (Prinz, 1997): perceiving an action activates the same motor representations as executing it, creating response conflict when the observed and instructed actions differ. The task has become a standard probe of the human mirror system and self-other distinction. The automatic imitation effect is modulated by animacy (stronger for human than robotic agents), social context (in-group vs. out-group models), empathy, and developmental stage (weaker in young children, inverted-U trajectory). Clinical applications include autism spectrum conditions (mixed findings on reduced automatic imitation) and schizophrenia (impaired self-other distinction).

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants perform an instructed action (e.g., finger lift) in response to a symbolic cue while simultaneously observing a task-irrelevant video or animation of another agent performing a congruent, incongruent, or neutral action.
* - **Manipulations**
  - - Congruency (observed action matches vs. mismatches instructed action)
    - Agent type (human hand, robotic hand, non-biological stimulus)
    - Social context (in-group vs. out-group model)
    - Action type (finger lift, hand open/close, whole-arm movement)
    - Spatial compatibility control (orthogonal spatial arrangement to dissociate imitative from spatial compatibility)
* - **Measurements**
  - - Congruency effect (RT and error rate difference: incongruent minus congruent)
    - Interference effect (incongruent minus neutral)
    - Facilitation effect (neutral minus congruent)
    - Congruency effect magnitude as individual-difference measure
    - EEG mu-suppression as neural index of motor simulation
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
* - Classic Finger-Lift Paradigm (Brass et al.)

    `hedvar_imitation_inhibition__classic_finger_lift_paradigm_brass_et_al`
  - The participant rests their hand on a table and watches a video of another hand. A number appears (1 or 2) telling them to lift the index or middle finger, while the hand on screen lifts either the same finger or the other one. Responses are slower when the observed movement differs from the instructed one.
  - Canonical: respond to number cue, observe incongruent finger lift
* - Kinematic Paradigm (Kilner Task)

    `hedvar_imitation_inhibition__kinematic_paradigm_kilner_task`
  - The participant makes repeated arm movements, for example side to side, while watching another person (or a robot) move their arm either in the same direction or up and down. The participant's movements become more variable when the observed movement conflicts with their own.
  - Perform arm movement while observing congruent/incongruent arm; different motor effector
* - Hand Open/Close Variant

    `hedvar_imitation_inhibition__hand_open_close_variant`
  - The instructed action is to open or close the whole hand, and the observed hand opens or closes at the same time, so that the imitation effect is measured with a larger movement than a finger lift.
  - Open/close hand in response to/despite observed hand action
* - Animacy Manipulation

    `hedvar_imitation_inhibition__animacy_manipulation`
  - The observed movement is performed by a human hand, a robotic hand, or a non-biological object such as a moving bar, to see whether the tendency to copy depends on seeing a living agent.
  - Animate vs. inanimate observed movement; tests social specificity of imitation
* - Goal-Directed Imitation Variant

    `hedvar_imitation_inhibition__goal_directed_imitation_variant`
  - The observed hand grasps an object, and the design separates how the hand moved from what it was trying to do, for example by having the same movement achieve different goals. Shows whether the participant copies the movement or the goal.
  - Imitate goal vs. means; tests level of imitative representation
* - Vocal Stimulus-Response Compatibility

    `hedvar_imitation_inhibition__vocal_stimulus_response_compatibility`
  - The participant hears a syllable such as 'pa' while being instructed to say either 'pa' or 'ba'. Saying a syllable that differs from the one heard is slower, the speech version of the finger task.
  - Vocal response to observed action; different response modality
* - Controlled Imitation Task (Reverse)

    `hedvar_imitation_inhibition__controlled_imitation_task_reverse`
  - On some trials the participant is told to imitate the observed movement and on others to make the instructed movement regardless of what they see. Tests the ability to choose when to copy and when not to.
  - Instructed to imitate or not; tests explicit voluntary control
* - Counter-Imitation Training

    `hedvar_imitation_inhibition__counter_imitation_training`
  - Before the test, the participant practices many trials of responding to an observed index-finger lift with a middle-finger lift and vice versa. After such training the usual tendency to copy is reduced or reversed.
  - Training to suppress imitation; tests plasticity of imitative tendencies
```

## Cognitive processes

This task is designed to engage the following processes:

- [Imitation](../processes/social_cognition_and_strategic_social_choice.md#hed-imitation)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring)

## Key references

- Brass, M., Bekkering, H., Wohlschlager, A., & Prinz, W. (2000). Compatibility between observed and executed finger movements: Comparing symbolic, spatial, and imitative cues. Brain and Cognition, 44(2), 124-143. ([DOI](https://doi.org/10.1006/brcg.2000.1225), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11041986/))
- Heyes, C. (2011). Automatic imitation. Psychological Bulletin, 137(3), 463-483. ([DOI](https://doi.org/10.1037/a0022288), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21280938/))

## Further references

- Cracco, E., Bardi, L., Desmet, C., Genschow, O., Rigoni, D., De Coster, L., Radkova, I., Deschrijver, E., & Brass, M. (2018). Automatic imitation: A meta-analysis. Psychological Bulletin, 144(5), 453-500. ([DOI](https://doi.org/10.1037/bul0000143), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29517262/))
- Genschow, O., van Den Bossche, S., Cracco, E., & Brass, M. (2017). Mimicry and automatic imitation are not correlated. PLoS ONE, 12(9), e0183784. ([DOI](https://doi.org/10.1371/journal.pone.0183784), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28877197/))
- Deschrijver, E., Wiersema, J. R., & Brass, M. (2017). Action-based touch observation in adults with high functioning autism. Social Cognitive and Affective Neuroscience, 12(2), 273-282. ([DOI](https://doi.org/10.1093/scan/nsw126))
- Kilner, J. M., Paulignan, Y., & Blakemore, S. J. (2003). An interference effect of observed biological movement on action. Current Biology, 13(6), 522-525. ([DOI](https://doi.org/10.1016/s0960-9822(03)00165-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12646137/))

## External links

- Cognitive Atlas: [action observation task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949846) (related match)

