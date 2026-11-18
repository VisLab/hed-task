(hedtsk_heartbeat_detection)=
# Heartbeat Detection Task

**HED task ID:** `hedtsk_heartbeat_detection`

**Family:** [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md)

**Also known as:** Heartbeat Counting Task, Heartbeat Perception Task, Heartbeat Tracking Task, Schandry Task, Cardiac Interoceptive Accuracy Task, Whitehead Heartbeat Discrimination Task

Participants count or discriminate their own heartbeats without external feedback; the correspondence between perceived and actual heartbeat counts (or discrimination accuracy) indexes interoceptive sensitivity.

## Description

The Heartbeat Detection Task is the standard paradigm for measuring interoceptive accuracy - the ability to perceive internal physiological signals. In the Schandry (1981) heartbeat counting variant, participants silently count their heartbeats during timed intervals (e.g., 25, 35, 45 seconds) without taking their pulse; an interoceptive accuracy score is computed from the discrepancy between counted and actual heartbeats (recorded via ECG or pulse oximetry). In the Whitehead heartbeat discrimination variant, participants judge whether an external stimulus (tone or light) is presented synchronously or asynchronously with their heartbeat; d-prime indexes perceptual sensitivity. Interoceptive accuracy is central to theories of emotion (the somatic marker hypothesis; Damasio, 1994), anxiety (interoceptive hypersensitivity models), and embodied cognition (predictive interoception). Individual differences in heartbeat detection correlate with emotional intensity, anxiety sensitivity, and decision-making quality. The paradigm has generated substantial methodological debate: the counting variant may partially reflect beliefs about heart rate rather than true perception, motivating the discrimination variant and newer alternatives.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-report-on-self">report on self</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-somatic">somatic</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-block-duration">block duration</a>, <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** The participant's own heartbeat and, in the discrimination form, a tone or light presented in or out of time with it.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants perceive their own heartbeats - either counting them during timed intervals (counting variant) or judging synchrony between external stimuli and cardiac events (discrimination variant) - while actual heartbeats are recorded physiologically.
* - **Manipulations**
  - - Task variant (counting vs. discrimination)
    - Interval duration
    - Stimulus timing relative to R-wave (synchronous vs. delayed)
    - Attention condition (interoceptive focus vs. exteroceptive distraction)
    - Pharmacological manipulation (beta-blockers, isoproterenol)
    - Interoceptive signal (breathing resistance vs. heartbeat)
* - **Measurements**
  - - Interoceptive accuracy score (1 - |counted - actual| / actual)
    - Heartbeat discrimination d-prime
    - Confidence ratings (interoceptive sensibility)
    - Heart rate variability as a covariate
    - Heartbeat-evoked potential (HEP) amplitude as a neural index
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
* - Heartbeat Discrimination (Whitehead)

    `hedvar_heartbeat_detection__heartbeat_discrimination_whitehead`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-somatic">somatic</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - A train of tones locked to each heartbeat, either immediate or delayed, is played and the participant judges whether it was in time with their heart, instead of counting heartbeats.
* - Confidence-Accuracy Paradigm

    `hedvar_heartbeat_detection__confidence_accuracy_paradigm`
  - named form
  - -
  - After each trial the participant also rates confidence in the answer.
* - Interoceptive Attention Manipulation

    `hedvar_heartbeat_detection__interoceptive_attention_manipulation`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-somatic">somatic</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>, <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception), [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - In alternating blocks the participant attends to the heartbeat or to an external tone or display while heart and brain responses are recorded, the listed attention-condition manipulation delivered with added stimuli and blocked trials.
* - Respiratory Interoception Variant

    `hedvar_heartbeat_detection__respiratory_interoception_variant`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - -
  - The participant breathes through a mouthpiece and reports on each breath whether an added resistance made it harder, the smallest detectable load being the measure.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Interoceptive awareness](../processes/awareness_agency_and_metacognition.md#hed-interoceptive-awareness)
- [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring)
- [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)

## Key references

- Schandry, R. (1981). Heart beat perception and emotional experience. *Psychophysiology*, 18(4), 483-488. ([DOI](https://doi.org/10.1111/j.1469-8986.1981.tb02486.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/7267933/))
- Whitehead, W. E., Drescher, V. M., Heiman, P., & Blackwell, B. (1977). Relation of heart rate control to heartbeat perception. *Biofeedback and Self-Regulation*, 2(4), 371-392. ([DOI](https://doi.org/10.1007/bf00998623), [PubMed](https://pubmed.ncbi.nlm.nih.gov/612350/))
- Garfinkel, S. N., Seth, A. K., Barrett, A. B., Suzuki, K., & Critchley, H. D. (2015). Knowing your own heart: Distinguishing interoceptive accuracy from interoceptive sensibility. *Biological Psychology*, 104, 65-74. ([DOI](https://doi.org/10.1016/j.biopsycho.2014.11.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25451381/))

## Further references

- Murphy, J., Brewer, R., Catmur, C., & Bird, G. (2017). Interoception and psychopathology: A developmental neuroscience perspective. *Developmental Cognitive Neuroscience*, 23, 45-56. ([DOI](https://doi.org/10.1016/j.dcn.2016.12.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28081519/))
- Zamariola, G., Maurage, P., Luminet, O., & Corneille, O. (2018). Interoceptive accuracy scores from the heartbeat counting task are problematic: Evidence from simple bivariate correlations. *Biological Psychology*, 137, 12-17. ([DOI](https://doi.org/10.1016/j.biopsycho.2018.06.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29944964/))
- Desmedt, O., Luminet, O., & Corneille, O. (2018). The heartbeat counting task largely measures non-interoceptive processes: Better alternatives exist. *Biological Psychology*, 137, 80-84. ([DOI](https://doi.org/10.1016/j.biopsycho.2018.09.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30218689/))

