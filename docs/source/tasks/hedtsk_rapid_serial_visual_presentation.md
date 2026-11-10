(hedtsk_rapid_serial_visual_presentation)=
# Rapid Serial Visual Presentation Task

**HED task ID:** `hedtsk_rapid_serial_visual_presentation`

**Family:** [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md) (also [Visual search and tracking tasks](families/visual_search_and_tracking.md))

**Also known as:** RSVP Task, Attentional Blink Task, AB Task, RSVP Attentional Blink, RSVP Target Detection, RSVP Stream Task, Dual-Target RSVP

A rapid stream of visual items is presented at a single location (typically 6-20 items/second); participants detect one or more targets among distractors. Target detection accuracy, especially for a second target shortly after a first (attentional blink), indexes temporal attention allocation.

## Description

Rapid Serial Visual Presentation (RSVP) is a paradigm for studying the temporal dynamics of visual attention. A stream of visual items (letters, digits, words, images, or complex scenes) is presented sequentially at a single spatial location at rates of 6-20 items per second. Participants must detect, identify, or categorize one or more targets embedded among distractors. The signature finding is the attentional blink (Raymond, Shapiro, & Arnell, 1992): when two targets appear in the stream, detection of the second target (T2) is severely impaired when it follows the first target (T1) by approximately 200-500 ms (lag 2-5), recovering at longer lags. Lag-1 sparing (intact T2 detection when T2 immediately follows T1) is a robust exception. The attentional blink reveals fundamental bottlenecks in temporal attention and has generated competing theoretical accounts: the two-stage model (Chun & Potter, 1995), the episodic simultaneous type/serial token model (Bowman & Wyble, 2007), and the boost-and-bounce model (Olivers & Meeter, 2008). Beyond the attentional blink, RSVP is used to study categorical perception (rapid scene gist extraction), emotion-attention interactions (emotion-induced blindness), and rapid image triage. Applications include brain-computer interfaces (RSVP-based P300 spellers and image triage systems, including satellite imagery analysis), clinical assessment of temporal attention in ADHD and dyslexia, and speed-reading technologies.

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
  - - Number of targets (single vs. dual)
    - T1-T2 lag (temporal separation between targets)
    - Target-distractor similarity
    - Stream rate (items per second)
    - Target category (letter among digits, face among objects, scene category)
    - Distractor set composition
    - Emotional content of targets or distractors
* - **Measurements**
  - - Target detection accuracy (T1 and T2)
    - Attentional blink magnitude (T2 accuracy deficit at short lags, conditional on correct T1 detection)
    - lag-1 sparing
    - T1-T2 intrusion errors (order reversals)
    - P300 ERP amplitude for detected targets
    - d-prime for target discrimination
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
* - Dual-Target Attentional Blink

    `hedvar_rapid_serial_visual_presentation__dual_target_attentional_blink`
  - Letters or pictures flash at one spot about ten per second. Two of them are targets, for example two letters among digits or a white letter among black ones. At the end the participant reports both targets. The second target is often missed when it comes 200 to 500 ms after the first.
  - Canonical AB: T2 missed when presented shortly after T1
* - Single-Target RSVP

    `hedvar_rapid_serial_visual_presentation__single_target_rsvp`
  - Only one target is placed in the stream, and the participant reports it at the end. Measures how well a single item can be picked out at high presentation rates and serves as a baseline.
  - Detect or identify one target in stream; no AB protocol
* - Emotion-Induced Blindness

    `hedvar_rapid_serial_visual_presentation__emotion_induced_blindness`
  - The stream is made of pictures, and an emotionally arousing picture (such as a violent or erotic scene) appears shortly before the target picture that must be reported. The emotional distractor makes the following target harder to see.
  - Emotional T1 causes blindness to T2; retained per §5.1 (EMOT retired)
* - Rapid Scene Categorization

    `hedvar_rapid_serial_visual_presentation__rapid_scene_categorization`
  - Photographs of natural scenes are shown at very high rates (down to about 20 ms per picture), and the participant reports whether a picture from a target category, such as an animal, appeared. Shows how quickly the gist of a scene is extracted.
  - Categorize natural scenes at rapid presentation rates; different stimulus class
* - RSVP Image Triage (BCI)

    `hedvar_rapid_serial_visual_presentation__rsvp_image_triage_bci`
  - Images such as satellite photographs are shown in a rapid stream while electroencephalography is recorded, and the brain response to target images is used to flag them, without the participant pressing anything. Used in brain-computer interface research for screening large image sets.
  - Brain-computer interface using RSVP for rapid image tagging; different application and response structure
* - Triple-RSVP (Multiple Streams)

    `hedvar_rapid_serial_visual_presentation__triple_rsvp_multiple_streams`
  - Three streams run at once at different positions on the screen, and a target may appear in any of them. The participant must monitor all three, which adds spatial demands to the rapid timing.
  - Three simultaneous streams; different attentional load structure
* - Whole-Report RSVP

    `hedvar_rapid_serial_visual_presentation__whole_report_rsvp`
  - A short stream of four to eight items is shown and the participant reports all of them, not just designated targets. Measures how many rapidly shown items can be captured and held.
  - Report all items seen; different response requirement
* - RSVP with Task Switch

    `hedvar_rapid_serial_visual_presentation__rsvp_with_task_switch`
  - The two targets require different judgments, such as naming the first and reporting whether the second was present, so the participant must change what they are doing between the targets.
  - Task changes within or between streams; adds switching demand
* - Detection vs. Identification

    `hedvar_rapid_serial_visual_presentation__detection_vs_identification`
  - For the second target the participant either just reports whether it was there or has to say which item it was. The blink is measured with each kind of report.
  - Detect presence vs. identify identity; different judgment type
* - Three-Target Variant

    `hedvar_rapid_serial_visual_presentation__three_target_variant`
  - Three targets are placed in the stream rather than two, and the participant reports all three, to probe how attention recovers across a longer sequence of targets.
  - Three targets in stream; extends AB to three-target scenario
* - Cross-Modal Attentional Blink

    `hedvar_rapid_serial_visual_presentation__cross_modal_attentional_blink`
  - The first target is in one sense and the second in another, for example a spoken target followed by a visual one, to test whether the blink occurs when the two targets use different senses.
  - T1 and T2 in different modalities; tests cross-modal attentional resources
* - Emotional Attentional Blink

    `hedvar_rapid_serial_visual_presentation__emotional_attentional_blink`
  - The targets themselves are emotional, such as emotional words or faces that must be reported, rather than emotional distractors. Emotional second targets are missed less often than neutral ones.
  - Emotional T2; retained per §5.1 (EMOT retired)
* - Spatial Two-Stream RSVP

    `hedvar_rapid_serial_visual_presentation__spatial_two_stream_rsvp`
  - Two streams run at once at different positions, and the two targets may appear in the same stream or in different ones. Separates the costs of shifting attention in time from the costs of shifting it in space.
  - Two streams at different spatial locations; tests spatial attention in RSVP
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

