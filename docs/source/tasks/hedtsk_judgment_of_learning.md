(hedtsk_judgment_of_learning)=
# Judgment-of-Learning Task

**HED task ID:** `hedtsk_judgment_of_learning`

**Family:** [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md)

**Also known as:** JOL Task, Judgment-of-Learning Paradigm, Metacognitive Prediction Task

After studying each item, participants predict the likelihood they will recall it on a later test; calibration and resolution of these predictions index metacognitive monitoring of encoding.

## Description

The Judgment-of-Learning task measures the accuracy of metacognitive predictions made during or shortly after encoding. In the standard Nelson and Dunlosky (1991) paradigm, participants study word pairs and, after each pair (immediate) or after a delay (delayed), rate the likelihood (0-100%) that they will recall the target when given the cue on a later test. A cued recall test follows, and prediction accuracy is assessed through resolution (gamma correlation between judgments and recall) and calibration (mean judgment vs. mean recall). A landmark finding is the delayed-judgment-of-learning effect: predictions made after a brief delay are far more accurate than immediate ones, because delayed judgments rely on retrieval fluency (a valid cue) rather than short-term memory availability (a poor cue). Judgment-of-Learning research connects to self-regulated learning: learners use these judgments to allocate study time, select items for restudy, and decide when to terminate study. The paradigm is foundational in metamemory research and dissociates from Feeling-of-Knowing tasks in timing (post-encoding vs. post-retrieval-failure), prediction target (recall vs. recognition), and underlying basis (encoding fluency vs. partial retrieval).

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
  - - Judgment timing (immediate vs. delayed)
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

## Variations

Named versions that change what the participant experiences or does. The identifier
of a variation is `hedvar_<task>__<variation>`.

```{list-table}
:widths: 25 40 35
:header-rows: 1

* - Variation
  - Description
  - Justification
* - Immediate Judgment-of-Learning

    `hedvar_judgment_of_learning__immediate_judgment_of_learning`
  - The participant studies a word pair and, right after it, rates how likely they are to recall the second word when given the first on a later test. After all pairs, the recall test is given and ratings are compared with actual recall.
  - JOL made immediately after study; foresight-based monitoring
* - Delayed Judgment-of-Learning

    `hedvar_judgment_of_learning__delayed_judgment_of_learning`
  - The rating is made some time after studying the pair, typically after several other pairs have been studied, rather than right away. Delayed ratings predict later recall far better than immediate ones.
  - JOL made after delay; improves accuracy via delayed-JOL effect
* - Aggregate vs. Item-by-Item Judgments

    `hedvar_judgment_of_learning__aggregate_vs_item_by_item_judgments`
  - Instead of (or in addition to) rating each item, the participant estimates how many of the whole list they will recall. The overall estimate is compared with the number actually recalled.
  - Global confidence vs. per-item monitoring; different judgment granularity
* - Cue-Only vs. Cue-Target Delayed Judgment

    `hedvar_judgment_of_learning__cue_only_vs_cue_target_delayed_judgment`
  - When the delayed rating is made, either only the first word of the pair is shown, which forces the participant to try to retrieve the second word, or both words are shown. Ratings made from the cue alone are the most accurate.
  - JOL prompted by cue alone vs. cue+target; tests forward vs. backward recall fluency
* - Self-Regulated Study Paradigm

    `hedvar_judgment_of_learning__self_regulated_study_paradigm`
  - After rating the items, the participant chooses which items to study again, or how long to spend on each. Whether they choose items they rated as poorly learned shows how the ratings are used to guide study.
  - Participant allocates study time based on JOL; adds metacognitive control component
* - Pre-Study Judgment (Ease-of-Learning)

    `hedvar_judgment_of_learning__pre_study_judgment_ease_of_learning`
  - The participant sees each item briefly before studying it and rates how easy it will be to learn. These judgments are made before any learning and measure estimates of difficulty rather than of learning achieved.
  - Judgment made before study; different pre-learning prediction task
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

