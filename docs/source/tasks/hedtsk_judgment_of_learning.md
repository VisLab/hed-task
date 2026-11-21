(hedtsk_judgment_of_learning)=
# Judgment-of-Learning Task

**HED task ID:** `hedtsk_judgment_of_learning`

**Family:** [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md)

**Also known as:** JOL Task, Judgment-of-Learning Paradigm, Metacognitive Prediction Task

After studying each item, participants predict the likelihood they will recall it on a later test; calibration and resolution of these predictions index metacognitive monitoring of encoding.

## Description

The Judgment-of-Learning task measures the accuracy of metacognitive predictions made during or shortly after encoding. In the standard Nelson and Dunlosky (1991) paradigm, participants study word pairs and, after each pair (immediate) or after a delay (delayed), rate the likelihood (0-100%) that they will recall the target when given the cue on a later test. A cued recall test follows, and prediction accuracy is assessed through resolution (gamma correlation between judgments and recall) and calibration (mean judgment vs. mean recall). A landmark finding is the delayed-judgment-of-learning effect: predictions made after a brief delay are far more accurate than immediate ones, because delayed judgments rely on retrieval fluency (a valid cue) rather than short-term memory availability (a poor cue). Judgment-of-Learning research connects to self-regulated learning: learners use these judgments to allocate study time, select items for restudy, and decide when to terminate study. The paradigm is foundational in metamemory research and dissociates from Feeling-of-Knowing tasks in timing (post-encoding vs. post-retrieval-failure), prediction target (recall vs. recognition), and underlying basis (encoding fluency vs. partial retrieval).

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">Study, then be tested</a> (`study_then_test`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is studied?* <a href="vocabulary.html#rule-study-then-test-studied-material-pairs">pairs</a>
  - *Is a judgment about one's own memory added?* <a href="vocabulary.html#rule-study-then-test-inserted-judgment-at-study">at study</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-repetitions">number of repetitions</a>
- **Material:** Cue-target word pairs, related or unrelated, each followed by a prompt to rate the chance of later recall.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants study items (typically word pairs), then predict the likelihood of recalling each item on a future test.
    2. a subsequent recall test assesses prediction accuracy.
* - **Manipulations**
  - - Judgment timing (before study, immediate, delayed)
    - Item difficulty (related vs. unrelated pairs)
    - Encoding conditions (number of presentations, elaborative vs. rote)
    - Cue type (cue-only vs. cue-target at judgment)
    - Self-paced vs. fixed study time
    - Reactivity (whether making judgments alters learning)
* - **Measurements**
  - - Resolution (gamma correlation between judgments and recall)
    - Calibration (mean judgment - mean recall)
    - over/underconfidence (signed calibration)
    - Absolute accuracy
    - Judgment latency
    - Study-time allocation as a behavioral consequence of judgments
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
* - Aggregate vs. Item-by-Item Judgments

    `hedvar_judgment_of_learning__aggregate_vs_item_by_item_judgments`
  - named form
  - -
  - Instead of, or as well as, rating each pair, the participant estimates how many items of the whole list they will recall.
* - Self-Regulated Study Paradigm

    `hedvar_judgment_of_learning__self_regulated_study_paradigm`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - -
  - After rating the items the participant chooses which to study again or how long to spend on each, adding a participant-controlled restudy phase.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Judgment of learning](../processes/awareness_agency_and_metacognition.md#hed-judgment-of-learning)
- [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)
- [Metacognitive control](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-control)
- [Encoding](../processes/long_term_memory.md#hed-encoding)

## Key references

- Nelson, T. O., & Dunlosky, J. (1991). When people's judgments of learning (JOLs) are extremely accurate at predicting subsequent recall: The 'delayed-JOL effect'. *Psychological Science*, 2(4), 267-270. ([DOI](https://doi.org/10.1111/j.1467-9280.1991.tb00147.x))
- Koriat, A. (1997). Monitoring one's own knowledge during study: A cue-utilization approach to judgments of learning. *Journal of Experimental Psychology: General*, 126(4), 349-370. ([DOI](https://doi.org/10.1037/0096-3445.126.4.349))
- Dunlosky, J., & Nelson, T. O. (1992). Importance of the kind of cue for judgments of learning (JOL) and the delayed-JOL effect. *Memory & Cognition*, 20(4), 374-380. ([DOI](https://doi.org/10.3758/bf03210921), [PubMed](https://pubmed.ncbi.nlm.nih.gov/1495399/))

## Further references

- Rhodes, M. G., & Tauber, S. K. (2011). The influence of delaying judgments of learning on metacognitive accuracy: A meta-analytic review. *Psychological Bulletin*, 137(1), 131-148. ([DOI](https://doi.org/10.1037/a0021705), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21219059/))
- Undorf, M., & Erdfelder, E. (2015). The relatedness effect on judgments of learning: A closer look at the contribution of processing fluency. *Memory & Cognition*, 43(3), 480-493. ([DOI](https://doi.org/10.3758/s13421-014-0479-x))
- Soderstrom, N. C., & Bjork, R. A. (2015). Learning versus performance: An integrative review. *Perspectives on Psychological Science*, 10(2), 176-199. ([DOI](https://doi.org/10.1177/1745691615569000), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25910388/))
- Double, K. S., Birney, D. P., & Walker, S. A. (2018). A meta-analysis and systematic review of reactivity to judgments of learning. *Memory*, 26(6), 741-750. ([DOI](https://doi.org/10.1080/09658211.2017.1404111))

