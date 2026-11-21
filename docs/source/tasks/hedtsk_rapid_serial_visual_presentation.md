(hedtsk_rapid_serial_visual_presentation)=
# Rapid Serial Visual Presentation Task

**HED task ID:** `hedtsk_rapid_serial_visual_presentation`

**Family:** [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md) (also [Visual search and tracking tasks](families/visual_search_and_tracking.md))

**Also known as:** RSVP Task, Attentional Blink Task, AB Task, RSVP Attentional Blink, RSVP Target Detection, RSVP Stream Task, Dual-Target RSVP

A rapid stream of visual items is presented at a single location (typically 6-20 items/second); participants detect one or more targets among distractors. Target detection accuracy, especially for a second target shortly after a first (attentional blink), indexes temporal attention allocation.

## Description

Rapid Serial Visual Presentation (RSVP) is a paradigm for studying the temporal dynamics of visual attention. A stream of visual items (letters, digits, words, images, or complex scenes) is presented sequentially at a single spatial location at rates of 6-20 items per second. Participants must detect, identify, or categorize one or more targets embedded among distractors. The signature finding is the attentional blink (Raymond, Shapiro, & Arnell, 1992): when two targets appear in the stream, detection of the second target (T2) is severely impaired when it follows the first target (T1) by approximately 200-500 ms (lag 2-5), recovering at longer lags. Lag-1 sparing (intact T2 detection when T2 immediately follows T1) is a robust exception. The attentional blink reveals fundamental bottlenecks in temporal attention and has generated competing theoretical accounts: the two-stage model (Chun & Potter, 1995), the episodic simultaneous type/serial token model (Bowman & Wyble, 2007), and the boost-and-bounce model (Olivers & Meeter, 2008). Beyond the attentional blink, RSVP is used to study categorical perception (rapid scene gist extraction), emotion-attention interactions (emotion-induced blindness), and rapid image triage. Applications include brain-computer interfaces (RSVP-based P300 spellers and image triage systems, including satellite imagery analysis), clinical assessment of temporal attention in ADHD and dyslexia, and speed-reading technologies.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-identify">identify</a>
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
  - *How often is there a target?* <a href="vocabulary.html#rule-respond-to-rule-target-rate-rare-target">rare target</a>
  - *How do the stimuli arrive?* <a href="vocabulary.html#rule-respond-to-rule-stream-rapid-stream">rapid stream</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-targets">number of targets</a>, <a href="vocabulary.html#setting-presentation-rate">presentation rate</a>, <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>, <a href="vocabulary.html#setting-stimulus-similarity">stimulus similarity</a>
- **Material:** A stream of letters, digits, words or images at one location at 6-20 items per second, with one or two targets among distractors.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A rapid serial stream of visual items is presented at a single location.
    2. Participants detect, identify, or categorize one or more targets embedded among distractors.
    3. Presentation rate is typically 6-20 items per second.
* - **Manipulations**
  - - Number of targets (single, dual, three)
    - T1-T2 lag (temporal separation between targets)
    - Target-distractor similarity
    - Stream rate (items per second)
    - Target category (letter among digits, face among objects, scene category)
    - Distractor set composition
    - Emotional content of targets or distractors
    - Overt response (none, EEG-flagged targets vs. button press)
    - Number of streams (one, two, three)
* - **Measurements**
  - - Target detection accuracy (T1 and T2)
    - Attentional blink magnitude (T2 accuracy deficit at short lags, conditional on correct T1 detection)
    - lag-1 sparing
    - T1-T2 intrusion errors (order reversals)
    - P300 ERP amplitude for detected targets
    - d-prime for target discrimination
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
* - Emotion-Induced Blindness

    `hedvar_rapid_serial_visual_presentation__emotion_induced_blindness`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
  - The stream is pictures and an emotionally arousing picture appears shortly before the target as a distractor.
* - Rapid Scene Categorization

    `hedvar_rapid_serial_visual_presentation__rapid_scene_categorization`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
  - -
  - Natural scenes are shown at very high rates and the participant reports only whether a picture from a target category appeared, a presence judgment rather than a report of which item.
* - RSVP Image Triage (BCI)

    `hedvar_rapid_serial_visual_presentation__rsvp_image_triage_bci`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
  - -
  - The participant looks for target images but never presses anything; their EEG response marks which images were targets.
* - Whole-Report RSVP

    `hedvar_rapid_serial_visual_presentation__whole_report_rsvp`
  - named form
  - -
  - A short stream of four to eight items is shown and the participant reports all of them, so there are no designated targets.
* - RSVP with Task Switch

    `hedvar_rapid_serial_visual_presentation__rsvp_with_task_switch`
  - rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>
  - [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
  - The two targets call for different judgments (name the first, say whether the second was present), so the rule changes between targets within the stream.
* - Detection vs. Identification

    `hedvar_rapid_serial_visual_presentation__detection_vs_identification`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
  - -
  - For the second target the participant either reports only whether it was there or must say which item it was.
* - Cross-Modal Attentional Blink

    `hedvar_rapid_serial_visual_presentation__cross_modal_attentional_blink`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The first target is in one sense and the second in another, for example spoken then visual.
* - Emotional Attentional Blink

    `hedvar_rapid_serial_visual_presentation__emotional_attentional_blink`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - -
  - The targets themselves are emotional words or faces to be reported.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Temporal attention](../processes/selective_and_sustained_attention.md#hed-temporal-attention)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)
- [Attentional awareness](../processes/awareness_agency_and_metacognition.md#hed-attentional-awareness)
- [Perceptual awareness](../processes/awareness_agency_and_metacognition.md#hed-perceptual-awareness)
- [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating)

## Key references

- Raymond, J. E., Shapiro, K. L., & Arnell, K. M. (1992). Temporary suppression of visual processing in an RSVP task: An attentional blink? Journal of Experimental Psychology: Human Perception and Performance, 18(3), 849-860. ([DOI](https://doi.org/10.1037/0096-1523.18.3.849), [PubMed](https://pubmed.ncbi.nlm.nih.gov/1500880/))
- Chun, M. M., & Potter, M. C. (1995). A two-stage model for multiple target detection in rapid serial visual presentation. Journal of Experimental Psychology: Human Perception and Performance, 21(1), 109-127. ([DOI](https://doi.org/10.1037/0096-1523.21.1.109), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7707027/))
- Potter, M. C. (1976). Short-term conceptual memory for pictures. Journal of Experimental Psychology: Human Learning and Memory, 2(5), 509-522. ([DOI](https://doi.org/10.1037/0278-7393.2.5.509), [PubMed](https://pubmed.ncbi.nlm.nih.gov/1003124/))

## Further references

- Dux, P. E., & Marois, R. (2009). The attentional blink: A review of data and theory. Attention, Perception, & Psychophysics, 71(8), 1683-1700. ([DOI](https://doi.org/10.3758/app.71.8.1683), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19933555/))
- Olivers, C. N. L., & Meeter, M. (2008). A boost and bounce theory of temporal attention. Psychological Review, 115(4), 836-863. ([DOI](https://doi.org/10.1037/a0013395), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18954206/))
- Most, S. B., Chun, M. M., Widders, D. M., & Zald, D. H. (2005). Attentional rubbernecking: Cognitive control and personality in emotion-induced blindness. Psychonomic Bulletin & Review, 12(4), 654-661. ([DOI](https://doi.org/10.3758/bf03196754), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16447378/))
- Marois, R., & Ivanoff, J. (2005). Capacity limits of information processing in the brain. Trends in Cognitive Sciences, 9(6), 296-305. ([DOI](https://doi.org/10.1016/j.tics.2005.04.010), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15925809/))
- Asplund, C. L., Fougnie, D., Zughni, S., Martin, J. W., & Marois, R. (2014). The attentional blink reveals the probabilistic nature of discrete conscious perception. Psychological Science, 25(3), 824-831. ([DOI](https://doi.org/10.1177/0956797613513810), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24434237/))

## External links

- Cognitive Atlas: [rapid serial visual presentation task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949879)

