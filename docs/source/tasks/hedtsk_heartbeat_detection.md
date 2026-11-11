(hedtsk_heartbeat_detection)=
# Heartbeat Detection Task

**HED task ID:** `hedtsk_heartbeat_detection`

**Family:** [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md)

**Also known as:** Heartbeat Counting Task, Heartbeat Perception Task, Heartbeat Tracking Task, Schandry Task, Cardiac Interoceptive Accuracy Task, Whitehead Heartbeat Discrimination Task

Participants count or discriminate their own heartbeats without external feedback; the correspondence between perceived and actual heartbeat counts (or discrimination accuracy) indexes interoceptive sensitivity.

## Description

The Heartbeat Detection Task is the standard paradigm for measuring interoceptive accuracy - the ability to perceive internal physiological signals. In the Schandry (1981) heartbeat counting variant, participants silently count their heartbeats during timed intervals (e.g., 25, 35, 45 seconds) without taking their pulse; an interoceptive accuracy score is computed from the discrepancy between counted and actual heartbeats (recorded via ECG or pulse oximetry). In the Whitehead heartbeat discrimination variant, participants judge whether an external stimulus (tone or light) is presented synchronously or asynchronously with their heartbeat; d-prime indexes perceptual sensitivity. Interoceptive accuracy is central to theories of emotion (the somatic marker hypothesis; Damasio, 1994), anxiety (interoceptive hypersensitivity models), and embodied cognition (predictive interoception). Individual differences in heartbeat detection correlate with emotional intensity, anxiety sensitivity, and decision-making quality. The paradigm has generated substantial methodological debate: the counting variant may partially reflect beliefs about heart rate rather than true perception, motivating the discrimination variant and newer alternatives.

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
* - **Measurements**
  - - Interoceptive accuracy score (1 - |counted - actual| / actual)
    - Heartbeat discrimination d-prime
    - Confidence ratings (interoceptive sensibility)
    - Heart rate variability as a covariate
    - Heartbeat-evoked potential (HEP) amplitude as a neural index
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
* - Heartbeat Counting (Schandry)

    `hedvar_heartbeat_detection__heartbeat_counting_schandry`
  - The participant sits quietly and, between a start and stop signal, silently counts their own heartbeats without feeling for a pulse. The count is compared with the number of beats recorded by an electrocardiogram over intervals of about 25 to 60 seconds.
  - Count heartbeats over interval; canonical interoception measure
* - Heartbeat Discrimination (Whitehead)

    `hedvar_heartbeat_detection__heartbeat_discrimination_whitehead`
  - A series of tones is played, each triggered by a heartbeat either immediately or after a delay, so the tones are in time with the heart or slightly out of step. The participant judges whether the tones were synchronous with their heartbeat.
  - Judge whether tone is synchronous with heartbeat; different detection task
* - Confidence-Accuracy Paradigm

    `hedvar_heartbeat_detection__confidence_accuracy_paradigm`
  - After each counting or discrimination trial the participant also rates how confident they are in their answer, and separately fills in a questionnaire about how aware of bodily sensations they generally are. The match between confidence and accuracy is a third measure alongside the two.
  - Sole confidence-rating exception per section 5.5; Garfinkel et al. (2015) interoception model
* - Interoceptive Attention Manipulation

    `hedvar_heartbeat_detection__interoceptive_attention_manipulation`
  - In some blocks the participant is told to attend to their heartbeat, and in others to attend to an external stimulus such as a tone or a visual display, while heartbeats and brain responses to them are recorded. Compares cardiac processing with and without attention on it.
  - Instructions to attend to vs. distract from heartbeat; changes attentional focus
* - Respiratory Interoception Variant

    `hedvar_heartbeat_detection__respiratory_interoception_variant`
  - The participant breathes through a mouthpiece and on some breaths a small resistance is added. They report whether each breath was harder than normal, and the smallest resistance they can detect is the measure. Tests sensitivity to breathing rather than to the heart.
  - Respiratory signals instead of cardiac; different physiological channel
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

