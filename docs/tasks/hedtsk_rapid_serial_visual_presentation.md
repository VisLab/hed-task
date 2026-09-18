(hedtsk_rapid_serial_visual_presentation)=
# Rapid Serial Visual Presentation Task

**HED Task ID:** `hedtsk_rapid_serial_visual_presentation`

**Also known as:** RSVP Task, Attentional Blink Task, AB Task, RSVP Attentional Blink, RSVP Target Detection, RSVP Stream Task, Dual-Target RSVP

A rapid stream of visual items is presented at a single location (typically 6-20 items/second); participants detect one or more targets among distractors. Target detection accuracy, especially for a second target shortly after a first (attentional blink), indexes temporal attention allocation.

## Description

Rapid Serial Visual Presentation (RSVP) is a paradigm for studying the temporal dynamics of visual attention. A stream of visual items (letters, digits, words, images, or complex scenes) is presented sequentially at a single spatial location at rates of 6-20 items per second. Participants must detect, identify, or categorize one or more targets embedded among distractors. The signature finding is the attentional blink (Raymond, Shapiro, & Arnell, 1992): when two targets appear in the stream, detection of the second target (T2) is severely impaired when it follows the first target (T1) by approximately 200-500 ms (lag 2-5), recovering at longer lags. Lag-1 sparing (intact T2 detection when T2 immediately follows T1) is a robust exception. The attentional blink reveals fundamental bottlenecks in temporal attention and has generated competing theoretical accounts: the two-stage model (Chun & Potter, 1995), the episodic simultaneous type/serial token model (Bowman & Wyble, 2007), and the boost-and-bounce model (Olivers & Meeter, 2008). Beyond the attentional blink, RSVP is used to study categorical perception (rapid scene gist extraction), emotion-attention interactions (emotion-induced blindness), and rapid image triage. Applications include brain-computer interfaces (RSVP-based P300 spellers and image triage systems, including satellite imagery analysis), clinical assessment of temporal attention in ADHD and dyslexia, and speed-reading technologies.

## Inclusion test

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - A rapid serial stream of visual items is presented at a single location; participants detect, identify, or categorize one or more targets embedded among distractors. Presentation rate is typically 6-20 items per second.
* - **Manipulation**
  - Number of targets (single vs. dual); T1-T2 lag (temporal separation between targets); target-distractor similarity; stream rate (items per second); target category (letter among digits, face among objects, scene category); distractor set composition; emotional content of targets or distractors.
* - **Measurement**
  - Target detection accuracy (T1 and T2); attentional blink magnitude (T2 accuracy deficit at short lags, conditional on correct T1 detection); lag-1 sparing; T1-T2 intrusion errors (order reversals); P300 ERP amplitude for detected targets; d-prime for target discrimination.
```

## Variations

```{list-table}
:widths: 25 40 35
:header-rows: 1

* - Variation
  - Description
  - Justification
* - Dual-Target Attentional Blink
  - Two targets in a single stream; T2 accuracy at varying lags from T1. The canonical paradigm for studying the attentional blink. Raymond et al. (1992).
  - Canonical AB: T2 missed when presented shortly after T1
* - Single-Target RSVP
  - One target in the stream; measures basic temporal attention and target detection at rapid rates. Baseline for attentional blink studies.
  - Detect or identify one target in stream; no AB protocol
* - Emotion-Induced Blindness
  - Emotionally arousing distractor (e.g., threat image) impairs detection of a subsequent neutral target. Emotional analogue of the attentional blink. Most et al. (2005).
  - Emotional T1 causes blindness to T2; retained per §5.1 (EMOT retired)
* - Rapid Scene Categorization
  - Natural scene images presented at high rates (20 ms per image); participants detect a target category (animal, vehicle). Demonstrates rapid perceptual gist extraction. Potter (1976).
  - Categorize natural scenes at rapid presentation rates; different stimulus class
* - RSVP Image Triage (BCI)
  - Participants view rapid streams of images (e.g., satellite imagery, surveillance footage) while EEG detects P300 responses to target-category images. Used in brain-computer interface applications for rapid image screening.
  - Brain-computer interface using RSVP for rapid image tagging; different application and response structure
* - Triple-RSVP (Multiple Streams)
  - Three concurrent RSVP streams; target can appear in any stream. Increases target detection rate for BCI applications; adds spatial competition to temporal attention demands.
  - Three simultaneous streams; different attentional load structure
* - Whole-Report RSVP
  - Report all items from a short RSVP stream (4-8 items). Measures visual short-term memory capacity under rapid presentation conditions.
  - Report all items seen; different response requirement
* - RSVP with Task Switch
  - T1 and T2 require different judgments (e.g., identify T1 letter, detect T2 presence). Task switch between targets amplifies the attentional blink.
  - Task changes within or between streams; adds switching demand
* - Detection vs. Identification
  - T2 requiring simple presence detection vs. full identity report; manipulates the depth of processing needed to reveal the blink.
  - Detect presence vs. identify identity; different judgment type
* - Three-Target Variant
  - Third target added to probe extended temporal limits of attention beyond the standard T1-T2 paradigm.
  - Three targets in stream; extends AB to three-target scenario
* - Cross-Modal Attentional Blink
  - Targets in different modalities (e.g., auditory T1, visual T2); tests whether the attentional bottleneck is supramodal.
  - T1 and T2 in different modalities; tests cross-modal attentional resources
* - Emotional Attentional Blink
  - Emotional stimuli (faces, words) as T1 or T2; emotional targets modulate blink magnitude. Distinct from emotion-induced blindness (which uses emotional distractors).
  - Emotional T2; retained per §5.1 (EMOT retired)
* - Spatial Two-Stream RSVP
  - Two concurrent RSVP streams at different locations; targets may appear in either stream, separating spatial and temporal attention limits.
  - Two streams at different spatial locations; tests spatial attention in RSVP
```

## Cognitive processes

This task engages the following cognitive processes:

- [Temporal attention](../processes/selective_and_sustained_attention.md#hed-temporal-attention)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)
- [Attentional awareness](../processes/awareness_agency_and_metacognition.md#hed-attentional-awareness)
- [Perceptual awareness](../processes/awareness_agency_and_metacognition.md#hed-perceptual-awareness)
- [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating)

## Key references

- Raymond, J. E., Shapiro, K. L., & Arnell, K. M. (1992). Temporary suppression of visual processing in an RSVP task: An attentional blink? Journal of Experimental Psychology: Human Perception and Performance, 18(3), 849-860.
- Chun, M. M., & Potter, M. C. (1995). A two-stage model for multiple target detection in rapid serial visual presentation. Journal of Experimental Psychology: Human Perception and Performance, 21(1), 109-127.
- Potter, M. C. (1976). Short-term conceptual memory for pictures. Journal of Experimental Psychology: Human Learning and Memory, 2(5), 509-522.

## Recent references

- Dux, P. E., & Marois, R. (2009). The attentional blink: A review of data and theory. Attention, Perception, & Psychophysics, 71(8), 1683-1700.
- Olivers, C. N. L., & Meeter, M. (2008). A boost and bounce theory of temporal attention. Psychological Review, 115(4), 836-863.
- Most, S. B., Chun, M. M., Widders, D. M., & Zald, D. H. (2005). Attentional rubbernecking: Cognitive control and personality in emotion-induced blindness. Psychonomic Bulletin & Review, 12(4), 654-661.
- Marois, R., & Ivanoff, J. (2005). Capacity limits of information processing in the brain. Trends in Cognitive Sciences, 9(6), 296-305.
- Asplund, C. L., Fougnie, D., Zughni, S., Martin, J. W., & Marois, R. (2014). The attentional blink reveals the probabilistic nature of discrete conscious perception. Psychological Science, 25(3), 824-831.

## External links

- Cognitive Atlas: [rapid serial visual presentation task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949879)

