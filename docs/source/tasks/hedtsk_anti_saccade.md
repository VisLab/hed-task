(hedtsk_anti_saccade)=
# Anti-Saccade Task

**HED task ID:** `hedtsk_anti_saccade`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md)

**Also known as:** AST, Antisaccade, Anti-Saccade

Participants must suppress a prepotent saccade toward a peripheral cue and generate a voluntary saccade to the opposite location; errors and saccade latency index oculomotor inhibition.

## Description

The Anti-Saccade Task measures voluntary control over reflexive eye movements. Participants fixate centrally while a peripheral stimulus suddenly appears in the left or right visual field. Instead of looking toward the stimulus (the reflexive prosaccade), participants must look in the opposite direction (antisaccade). This requires inhibiting the automatic orienting response and generating a volitional saccade. Performance is measured by antisaccade accuracy, latency, and the rate of prosaccadic intrusions (errors). The task indexes voluntary oculomotor control and prefrontal inhibitory function.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-localize">localize</a>
  - *Must the player ever hold back?* <a href="vocabulary.html#rule-respond-to-rule-response-demand-respond-opposite">respond opposite</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-eye-tracker">eye tracker</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-eccentricity">eccentricity</a>, <a href="vocabulary.html#setting-retention-interval">retention interval</a>
- **Material:** A central fixation point and a stimulus that appears suddenly in the left or right periphery.
- **Combined with:** <a href="vocabulary.html#how-chained">chained</a>, [Fixate Task](hedtsk_fixate.md) (Gaze is held on the fixation target until the peripheral target appears)

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
    - Response release (delayed go signal vs. immediate)
    - Cue type (emotional face or picture vs. dot)
    - Memory delay before the saccade (memory-guided vs. visually guided)
    - Second cue or target jump during saccade planning (double step)
* - **Measurements**
  - - Saccade direction errors (% erroneous prosaccades on antisaccade trials)
    - Saccade latency
    - Corrective saccade latency
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
* - Prosaccade (Control Condition)

    `hedvar_anti_saccade__prosaccade_control_condition`

    Cognitive Atlas: [visually guided saccade task](https://www.cognitiveatlas.org/task/id/trm_4f24108555294) (close match)
  - response demand: <a href="vocabulary.html#rule-respond-to-rule-response-demand-always-respond">always respond</a>
  - -
  - The same display but the participant looks toward the cue, so the opposite-response demand is dropped.
* - Interleaved Pro/Anti-Saccade

    `hedvar_anti_saccade__interleaved_pro_anti_saccade`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>; rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>; cue: <a href="vocabulary.html#rule-respond-to-rule-cue-rule-cue">rule cue</a>
  - [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
  - Look-toward and look-away trials are mixed in one block and a per-trial cue (often fixation color) says which rule applies.
* - Blocked Pro/Anti-Saccade

    `hedvar_anti_saccade__blocked_pro_anti_saccade`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - Prosaccade and antisaccade trials are run in separate blocks, so within each block the rule is fixed and the task alternates between the standard form and the prosaccade control.
* - Emotional Anti-Saccade

    `hedvar_anti_saccade__emotional_anti_saccade`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
  - [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
  - The peripheral cue is an emotional face or picture instead of a dot; the look-away rule is unchanged.
* - Memory-Guided Anti-Saccade

    `hedvar_anti_saccade__memory_guided_anti_saccade`

    Cognitive Atlas: [memory guided saccade task](https://www.cognitiveatlas.org/task/id/trm_4f2457d94fd93)
  - reference: <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
  - [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory)
  - The cue disappears, its location is held in memory through a delay, and the look-away saccade is made to the remembered mirror location on a later signal.
* - Double-Step Anti-Saccade

    `hedvar_anti_saccade__double_step_anti_saccade`
  - named form
  - [Motor planning](../processes/motor_preparation_timing_and_execution.md#hed-motor-planning)
  - A second cue arrives, or the target jumps, while the first saccade is being planned or executed, so the participant must re-program a response already under way.
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

