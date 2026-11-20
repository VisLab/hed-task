(hedtsk_n_back)=
# N-Back Task

**HED task ID:** `hedtsk_n_back`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** N-Back

Continuous stream in which each item must be compared to the one n items back; accuracy and RT index working memory updating and monitoring.

## Description

The N-Back task is a continuous performance paradigm in which participants view a sequence of stimuli (letters, numbers, or spatial locations) and judge whether each current stimulus matches the one presented n trials earlier. Difficulty scales parametrically with n (1-back, 2-back, 3-back). The task engages working memory maintenance, updating, and comparison processes. Performance typically shows decreased accuracy and increased RT with higher n values. The N-back is the most widely used working memory paradigm in neuroimaging, consistently activating dorsolateral prefrontal cortex and parietal regions.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What does the rule ask about each stimulus?** <a href="vocabulary.html#rule-respond-to-rule-rule-asks-compare">compare</a>
- **Must the player ever hold back?** <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
- **How often is there a target?** <a href="vocabulary.html#rule-respond-to-rule-target-rate-rare-target">rare target</a>
- **Is something held in mind to compare against?** <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** A stream of letters (or numbers or spatial locations), some of which match the item n back.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A continuous stream of stimuli is presented.
    2. Participants indicate when the current item matches the one presented N items back.
* - **Manipulations**
  - - Load level (N = 0, 1, 2, 3)
    - Stimulus type (letters, locations, faces)
    - Lure trials (N+/-1 matches)
* - **Measurements**
  - - Hit rate
    - False alarm rate
    - d-prime
    - RT
    - Load-dependent accuracy decline
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
* - Spatial N-Back

    `hedvar_n_back__spatial_n_back`

    Cognitive Atlas: [spatial n-back task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949df1)
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory)
  - A square appears at grid positions and the match is on position n back rather than identity.
* - Emotional N-Back

    `hedvar_n_back__emotional_n_back`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
  - The items are emotional faces or words and the match n back is on identity or on expression.
* - Fractal/Object N-Back

    `hedvar_n_back__fractal_object_n_back`

    Cognitive Atlas: [object n-back](https://www.cognitiveatlas.org/task/id/trm_4ebd477ab5a11)
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-fractals">fractals</a>, <a href="vocabulary.html#facet-stimulus-type-abstract-patterns">abstract patterns</a>
  - [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory)
  - The items are unnameable patterns so they cannot be rehearsed verbally.
* - Adaptive N-Back

    `hedvar_n_back__adaptive_n_back`

    Cognitive Atlas: [adaptive n-back task](https://www.cognitiveatlas.org/task/id/trm_56674133b666c)
  - trial structure: <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - -
  - The level n rises or falls between blocks to hold each participant near a target accuracy.
* - Auditory N-Back

    `hedvar_n_back__auditory_n_back`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception), [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The items are heard (tones or spoken letters) rather than seen.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating)
- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Jonides, J., Schumacher, E. H., Smith, E. E., Koeppe, R. A., Awh, E., Minoshima, S., & Mintun, M. A. (1997). The role of parietal cortex in verbal working memory. *Journal of Neuroscience*, 17(13), 5282-5288. ([DOI](https://doi.org/10.1523/jneurosci.18-13-05026.1998))
- Owen, A. M., McMillan, K. M., Laird, A. R., & Bullmore, E. (2005). N-back working memory paradigm: A meta-analysis of normative functional neuroimaging studies. *Human Brain Mapping*, 25(1), 46-59. ([DOI](https://doi.org/10.1002/hbm.20131), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15846822/))

## Further references

- Redick, T. S., & Lindsey, D. R. B. (2013). Complex span and n-back measures of working memory: A meta-analysis. *Psychonomic Bulletin & Review*, 20(6), 1102-1113. ([DOI](https://doi.org/10.3758/s13423-013-0453-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23733330/))
- Jaeggi, S. M., Buschkuehl, M., Perrig, W. J., & Meier, B. (2010). The concurrent validity of the N-back task as a working memory measure. *Memory*, 18(4), 394-412. ([DOI](https://doi.org/10.1080/09658211003702171), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20408039/))
- Chatham, C. H., Herd, S. A., Brant, A. M., Hazy, T. E., Miyake, A., O'Reilly, R., & Friedman, N. P. (2011). From an executive network to executive control: A computational model of the n-back task. *Journal of Cognitive Neuroscience*, 23(11), 3598-3619. ([DOI](https://doi.org/10.1162/jocn_a_00047), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21563882/))
- Soveri, A., Antfolk, J., Karlsson, L., Salo, B., & Laine, M. (2017). Working memory training revisited: A multi-level meta-analysis of n-back training studies. *Psychonomic Bulletin & Review*, 24(4), 1077-1096. ([DOI](https://doi.org/10.3758/s13423-016-1217-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28116702/))
- Exploring the n-back task: insights, applications, and future directions. (2025). *Frontiers in Human Neuroscience*, 19, 1721330. doi:10.3389/fnhum.2025.1721330 ([DOI](https://doi.org/10.3389/fnhum.2025.1721330), [PubMed](https://pubmed.ncbi.nlm.nih.gov/41426299/))

## External links

- Cognitive Atlas: [n-back task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949bcd)

- CogPO: [n-back Paradigm](http://www.wiki.cogpo.org/index.php?title=N-back_Paradigm)

