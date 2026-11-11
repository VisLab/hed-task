(hedtsk_anti_saccade)=
# Anti-Saccade Task

**HED task ID:** `hedtsk_anti_saccade`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md)

**Also known as:** AST, Antisaccade, Anti-Saccade

Participants must suppress a prepotent saccade toward a peripheral cue and generate a voluntary saccade to the opposite location; errors and saccade latency index oculomotor inhibition.

## Description

The Anti-Saccade Task measures voluntary control over reflexive eye movements. Participants fixate centrally while a peripheral stimulus suddenly appears in the left or right visual field. Instead of looking toward the stimulus (the reflexive prosaccade), participants must look in the opposite direction (antisaccade). This requires inhibiting the automatic orienting response and generating a volitional saccade. Performance is measured by antisaccade accuracy, latency, and the rate of prosaccadic intrusions (errors). The task indexes voluntary oculomotor control and prefrontal inhibitory function.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A peripheral cue appears.
    2. Participants must suppress the reflexive saccade toward it and instead generate a voluntary saccade to the mirror-opposite location.
* - **Manipulations**
  - - Prosaccade vs. antisaccade blocks or interleaved trials
    - Cue eccentricity
    - Gap vs. overlap conditions
* - **Measurements**
  - - Saccade direction errors (% erroneous prosaccades on antisaccade trials)
    - Saccade latency
    - Corrective saccade latency
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
* - Standard Anti-Saccade

    `hedvar_anti_saccade__standard_anti_saccade`
  - The participant fixates a central point. A cue flashes to the left or right, and the participant must look to the opposite side, at the same distance from center, as quickly as possible. Looking toward the cue by mistake is counted as an error.
  - Canonical paradigm: participant inhibits reflexive saccade and redirects gaze to mirror location
* - Prosaccade (Control Condition)

    `hedvar_anti_saccade__prosaccade_control_condition`
  - The same display, but the participant is told to look toward the flashing cue rather than away from it. This is the reflexive, easy response and serves as a baseline for eye-movement speed and accuracy.
  - Opposite stimulus-response mapping (look toward cue); different response requirement from anti-saccade
* - Interleaved Pro/Anti-Saccade

    `hedvar_anti_saccade__interleaved_pro_anti_saccade`
  - Look-toward and look-away trials are mixed unpredictably within the same block, with a cue on each trial (often fixation color) saying which rule applies. The participant must switch rules from trial to trial.
  - Mixed trial types require on-trial task-set switching; distinct from blocked presentation
* - Blocked Pro/Anti-Saccade

    `hedvar_anti_saccade__blocked_pro_anti_saccade`
  - Look-toward trials and look-away trials are run in separate blocks, so the participant keeps the same rule throughout a block and never has to switch.
  - Separate blocks of pro- and anti-saccade trials; different cognitive context from interleaved
* - Gap vs. Overlap Conditions

    `hedvar_anti_saccade__gap_vs_overlap_conditions`
  - Varies what happens to the central fixation point when the cue appears. In the gap condition it disappears about 200 ms before the cue, which speeds up eye movements and increases errors. In the overlap condition it stays on while the cue is shown.
  - Fixation offset timing changes saccade initiation dynamics and error rates
* - Delayed Anti-Saccade

    `hedvar_anti_saccade__delayed_anti_saccade`
  - The cue appears, but the participant must keep looking at the center and wait for a go signal (often the fixation point going off) before looking away from where the cue was. Holding the eyes still through the delay adds a waiting and memory demand.
  - Memory-guided response after delay period; adds working memory component
* - Emotional Anti-Saccade

    `hedvar_anti_saccade__emotional_anti_saccade`
  - The peripheral cue is a face with an emotional expression (or another emotional picture) instead of a plain dot. The participant still looks away from it; the question is whether emotional cues are harder to look away from.
  - Emotional stimuli as saccade targets; retained per section 5.1 (EMOT retired)
* - Memory-Guided Anti-Saccade

    `hedvar_anti_saccade__memory_guided_anti_saccade`
  - The cue flashes and then disappears, and the participant must remember where it was during a delay before making the look-away eye movement to the opposite location on a later signal.
  - Target location must be retained in memory before response; distinct memory demand
* - Double-Step Anti-Saccade

    `hedvar_anti_saccade__double_step_anti_saccade`
  - Two cues appear in quick succession, or the target jumps to a new place just as the eye movement starts. The participant has to correct an eye movement that is already planned or under way.
  - Two-step target displacement requires online motor reprogramming
```

## Cognitive processes

This task is designed to engage the following processes:

- [Antisaccade](../processes/motor_preparation_timing_and_execution.md#hed-antisaccade)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Saccade](../processes/motor_preparation_timing_and_execution.md#hed-saccade)
- [Executive attention](../processes/inhibitory_control_and_conflict_monitoring.md#hed-executive-attention)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)
- [Motor preparation](../processes/motor_preparation_timing_and_execution.md#hed-motor-preparation)

## Key references

- Hallett, P. E. (1978). Primary and secondary saccades to goals defined by instructions. *Vision Research*, 18(11), 1279-1296. ([DOI](https://doi.org/10.1016/0042-6989(78)90218-3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/726270/))
- Munoz, D. P., & Everling, S. (2004). Look away: The anti-saccade task and the voluntary control of eye movement. *Nature Reviews Neuroscience*, 5(3), 218-228. ([DOI](https://doi.org/10.1038/nrn1345), [PubMed](https://pubmed.ncbi.nlm.nih.gov/14976521/))
- Everling, S., & Fischer, B. (1998). The antisaccade: A review of basic research and clinical findings. *Neuropsychologia*, 36(9), 885-899. ([DOI](https://doi.org/10.1016/s0028-3932(98)00020-7), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9740362/))

## Further references

- Hutton, S. B., & Ettinger, U. (2006). The antisaccade task as a research tool in psychopathology: A critical review. *Psychophysiology*, 43(3), 302-313. [Updated: Amador, S. C., Hood, A. J., Schiess, M. C., Izor, R., & Sereno, A. B. (2006). Dissociating cognitive deficits involved in voluntary eye movement dysfunctions in Parkinson's disease patients. *Neuropsychologia*, 44(8), 1475-1482.] ([DOI](https://doi.org/10.1111/j.1469-8986.2006.00403.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16805870/))
- Antoniades, C. A., Ettinger, U., Gaymard, B., et al. (2013). An internationally standardised antisaccade protocol. *Vision Research*, 84, 1-5. ([DOI](https://doi.org/10.1016/j.visres.2013.02.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23474300/))
- Crawford, T. J., Higham, S., Renvoize, T., Patel, J., Dale, M., Surber, A., & Smeeton, R. (2005). Inhibitory control of saccadic eye movements and cognitive impairment in Alzheimer's disease. *Biological Psychiatry*, 57(9), 1052-1060. [Updated context: Kaufman, L. D., Pratt, J., Levine, B., & Black, S. E. (2012). Executive deficits detected in mild Alzheimer's disease patients using the antisaccade task. *Brain and Behavior*, 2(1), 15-21.] ([DOI](https://doi.org/10.1016/j.biopsych.2005.01.017), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15860346/))
- Munoz, D. P., Armstrong, I. T., Hampton, K. A., & Moore, K. D. (2003). Altered control of visual fixation and saccadic eye movements in attention-deficit hyperactivity disorder. *Journal of Neurophysiology*, 90(1), 503-514. [Updated: Wiecki, T. V., Antoniades, C. A., Golla, A., et al. (2016). A computational cognitive biomarker for early-stage Huntington's disease. *PLoS ONE*, 11(2), e0148409.] ([DOI](https://doi.org/10.1152/jn.00192.2003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12672781/))

## External links

- Cognitive Atlas: [antisaccade/prosaccade task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949869)

- CogPO: [Anti-Saccades Paradigm](http://www.wiki.cogpo.org/index.php?title=Anti-Saccades_Paradigm)

