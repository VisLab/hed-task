(hedtsk_imitation_inhibition)=
# Imitation-Inhibition Task

**HED task ID:** `hedtsk_imitation_inhibition`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Automatic Imitation Task, Automatic Imitation, Brass Imitation Task, Stimulus-Response Compatibility Imitation Task, Action Observation Compatibility Task

Execute an instructed finger movement while observing a congruent or incongruent action performed by another person; the congruency effect (faster responses on congruent trials) indexes automatic imitation and the cost of inhibiting observed-action representations.

## Description

The Imitation-Inhibition Task (Brass, Bekkering, Wohlschlager, & Prinz, 2000) measures the involuntary tendency to copy observed actions and the executive cost of suppressing that tendency. Participants are cued to perform a simple action (e.g., lift the index finger when a number '1' appears) while simultaneously viewing a task-irrelevant video of another person's hand performing either the same action (congruent), a different action (incongruent, e.g., lifting the middle finger), or no action (neutral/static hand). The congruency effect -- faster and more accurate responses on congruent than incongruent trials -- indexes automatic imitation, while the interference effect (incongruent minus neutral) specifically indexes the inhibitory cost of suppressing the observed action. The paradigm is grounded in common-coding / ideomotor theory (Prinz, 1997): perceiving an action activates the same motor representations as executing it, creating response conflict when the observed and instructed actions differ. The task has become a standard probe of the human mirror system and self-other distinction. The automatic imitation effect is modulated by animacy (stronger for human than robotic agents), social context (in-group vs. out-group models), empathy, and developmental stage (weaker in young children, inverted-U trajectory). Clinical applications include autism spectrum conditions (mixed findings on reduced automatic imitation) and schizophrenia (impaired self-other distinction).

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** every rule takes the default of the game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** A digit cue (such as 1) naming the finger to lift, shown over a video of another person's hand lifting the same or a different finger or staying still.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants perform an instructed action (e.g., finger lift) in response to a symbolic cue while simultaneously observing a task-irrelevant video or animation of another agent performing a congruent, incongruent, or neutral action.
    2. Optional: A training phase before the test pairs an observed index-finger lift with a middle-finger response and the reverse.
* - **Manipulations**
  - - Congruency (observed action matches vs. mismatches instructed action)
    - Agent type (human hand, robotic hand, non-biological stimulus)
    - Social context (in-group vs. out-group model)
    - Action type (finger lift, hand open/close, whole-arm movement)
    - Spatial compatibility control (orthogonal spatial arrangement to dissociate imitative from spatial compatibility)
    - Goal of the observed action (movement vs. goal dissociated)
    - Task instruction (imitate vs. move regardless, cued per trial)
* - **Measurements**
  - - Congruency effect (RT and error rate difference: incongruent minus congruent)
    - Interference effect (incongruent minus neutral)
    - Facilitation effect (neutral minus congruent)
    - Congruency effect magnitude as individual-difference measure
    - EEG mu-suppression as neural index of motor simulation
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
* - Kinematic Paradigm (Kilner Task)

    `hedvar_imitation_inhibition__kinematic_paradigm_kilner_task`
  - stimulus type: none; task I/O device: <a href="vocabulary.html#facet-task-io-device-motion-capture">motion capture</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>; stream: <a href="vocabulary.html#rule-respond-to-rule-stream-continuous">continuous</a>; combined with: <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-produce-movement">produce movement</a> (Continuous self-paced arm movements replace the cued finger lifts)
  - -
  - The participant makes continuous, repeated arm movements while watching a person or a robot move in the same or a perpendicular direction, and the variability of the participant's movement is the measure.
* - Vocal Stimulus-Response Compatibility

    `hedvar_imitation_inhibition__vocal_stimulus_response_compatibility`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-syllables">syllables</a>; social aspect: none; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The participant hears a syllable while instructed to say the same or a different syllable; the heard syllable is the observed action.
* - Controlled Imitation Task (Reverse)

    `hedvar_imitation_inhibition__controlled_imitation_task_reverse`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-rule-cue">rule cue</a>; rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>
  - [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
  - Trial by trial the participant is told either to imitate the observed movement or to make the instructed movement regardless, so the rule is cued and switches across trials.
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

