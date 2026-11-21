(hedtsk_trail_making)=
# Trail Making Task

**HED task ID:** `hedtsk_trail_making`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md) (also [Motor performance and speeded response tasks](families/motor_performance.md))

**Also known as:** Trail Making Test, TMT, Trails A/B, Trail Making

Paper-and-pencil sequencing: connect numbered circles (Part A) or alternate numbers and letters (Part B) as fast as possible. B-A difference indexes set switching.

## Description

The Trail Making Test is a widely used neuropsychological assessment consisting of two parts. In Part A, participants draw lines connecting consecutively numbered circles (1->2->3->...) as quickly as possible, measuring visual scanning and psychomotor speed. In Part B, participants alternate between numbers and letters (1->A->2->B->3->C->...), adding demands for cognitive flexibility and task-switching. The derived score (B-A) isolates the switching cost from baseline motor and visual search speed. The TMT is among the most sensitive measures of general brain dysfunction and is included in virtually every neuropsychological test battery. Digital tablet versions now capture rich kinematic data (velocity, pressure, pauses).

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-localize">localize</a>
  - *How do the stimuli arrive?* <a href="vocabulary.html#rule-respond-to-rule-stream-continuous">continuous</a>
  - *Is something held in mind to compare against?* <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructed-emphasis">instructed emphasis</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-writing-device">writing device</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-targets">number of targets</a>
- **Material:** Circles numbered from 1 (Part A), or numbered and lettered circles to connect alternately (Part B), on paper or a tablet.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants connect numbered circles in order (Part A: 1-2-3...) or alternate between numbers and letters (Part B: 1-A-2-B-3-C...), drawing lines as quickly as possible.
* - **Manipulations**
  - - Part A vs. Part B
    - Number of targets
    - Digital vs. paper administration
* - **Measurements**
  - - Completion time for Part A and Part B
    - B-minus-A difference (executive component)
    - B/A ratio
    - Errors
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
* - Oral Trail Making Test

    `hedvar_trail_making__oral_trail_making`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: none; task I/O device: <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production), [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - The alternating sequence is said aloud with no page, so the answer is spoken rather than drawn and there is no visual search.
* - Color Trails Test

    `hedvar_trail_making__color_trails`

    Cognitive Atlas: [Color Trails Test](https://www.cognitiveatlas.org/task/id/trm_4da633fe917c4)
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>
  - -
  - A named instrument in which letters are replaced by a second colored number set so the test is language-free.
* - Comprehensive Trail Making Test (CTMT)

    `hedvar_trail_making__comprehensive_trail_making_test_ctmt`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - -
  - A named five-subtest battery that adds distractor circles and number-word switching.
* - D-KEFS Trail Making

    `hedvar_trail_making__d_kefs_trail_making`
  - named form
  - -
  - A named five-condition instrument that separates scanning, sequencing, switching and motor speed.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)
- [Motor planning](../processes/motor_preparation_timing_and_execution.md#hed-motor-planning)
- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)

## Key references

- Reitan, R. M. (1958). Validity of the Trail Making Test as an indicator of organic brain damage. *Perceptual and Motor Skills*, 8(3), 271-276. ([DOI](https://doi.org/10.2466/pms.1958.8.3.271))
- Bowie, C. R., & Harvey, P. D. (2006). Administration and interpretation of the Trail Making Test. *Nature Protocols*, 1(5), 2277-2281. ([DOI](https://doi.org/10.1038/nprot.2006.390), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17406468/))

## Further references

- Salthouse, T. A. (2011). What cognitive abilities are involved in trail-making performance? *Intelligence*, 39(4), 222-232. ([DOI](https://doi.org/10.1016/j.intell.2011.03.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21789028/))
- Sánchez-Cubillo, I., Periáñez, J. A., Adrover-Roig, D., Rodríguez-Sánchez, J. M., Ríos-Lago, M., Tirapu, J., & Barceló, F. (2009). Construct validity of the Trail Making Test: Role of task-switching, working memory, inhibition/interference control, and visuomotor abilities. *Journal of the International Neuropsychological Society*, 15(3), 438-450. ([DOI](https://doi.org/10.1017/s1355617709090626), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19402930/))
- Cangoz, B., Karakoc, E., & Selekler, K. (2009). Trail Making Test: Normative data for Turkish elderly population by age, sex, and education. *Journal of the Neurological Sciences*, 283(1-2), 73-78. ([DOI](https://doi.org/10.1016/j.jns.2009.02.313), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19264326/))

## External links

- Cognitive Atlas: [Trail Making Test A and B](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949ec0)

