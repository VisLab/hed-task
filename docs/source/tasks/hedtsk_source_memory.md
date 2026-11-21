(hedtsk_source_memory)=
# Source Memory Task

**HED task ID:** `hedtsk_source_memory`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** Source Monitoring Task, Reality Monitoring Task, Context Memory Task, Source Judgment Task

After studying items presented in distinct contexts (speaker, location, modality, time), participants judge each item's encoding source; source accuracy dissociates contextual recollection from item familiarity.

## Description

Source memory tests assess the ability to remember the contextual details of an encoding episode - not just whether an item was encountered (item memory) but where, when, how, or from whom it was learned. In the standard paradigm, items are presented under two or more source conditions (e.g., spoken by a male vs. female voice; shown on the left vs. right of the screen; read vs. imagined). At test, participants first make an old/new recognition judgment, then indicate the source of each recognized item. Source accuracy (correct source attributions conditional on item recognition) is the primary measure, dissociating recollection-based contextual retrieval from familiarity-based item recognition. Johnson's source monitoring framework (Johnson, Hashtroudi, & Lindsay, 1993) distinguishes external source monitoring (which person said it), internal source monitoring (did I do it or imagine it), and reality monitoring (internal vs. external origin). Source memory failures underlie false memories, eyewitness misattributions, and confabulation. The paradigm recruits prefrontal cortex (especially right and medial PFC for monitoring) and hippocampus (binding items to contexts), with a characteristic dissociation from item memory in aging and frontal lesion patients.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">Study, then be tested</a> (`study_then_test`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is studied?* <a href="vocabulary.html#rule-study-then-test-studied-material-items-with-context">items with context</a>
  - *What form does the test take?* <a href="vocabulary.html#rule-study-then-test-test-form-source-attribution">source attribution</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-alternatives">number of alternatives</a>, <a href="vocabulary.html#setting-stimulus-similarity">stimulus similarity</a>
- **Material:** Studied items presented under two or more sources, such as a male or a female voice or the left or the right of the screen.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Items are studied under two or more contextually distinct source conditions.
    2. At test, participants recognize studied items and judge the source (context) in which each item was encoded.
* - **Manipulations**
  - - Source type (voice, spatial location, temporal position, modality, cognitive operation)
    - Number of sources (2, 3, or more)
    - Encoding depth
    - Source similarity (easy-to-discriminate vs. similar sources)
    - Response format (forced-choice source vs. source confidence rating)
* - **Measurements**
  - - Source accuracy (proportion of recognized items with correct source attribution)
    - Source d' (signal detection)
    - Item-source conditional analysis
    - remember/know x source interaction
    - Source attribution errors (systematic misattributions)
    - PFC and hippocampal activation differences
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
* - Spatial Source Monitoring

    `hedvar_source_memory__spatial_source_monitoring`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory)
  - Each item is studied at one of several screen positions or places and the participant reports where it was.
* - Temporal Source Monitoring

    `hedvar_source_memory__temporal_source_monitoring`
  - cycles: <a href="vocabulary.html#rule-study-then-test-cycles-repeated-lists">repeated lists</a>
  - -
  - Items are studied in two or more separate lists or sessions and the participant reports which list or session each came from, so the study phase must itself be repeated lists.
* - Reality Monitoring

    `hedvar_source_memory__reality_monitoring`
  - named form
  - -
  - Some items are perceived and others are generated by the participant (for example completed from a word stem), and the test asks which was which.
* - Internal Source Monitoring

    `hedvar_source_memory__internal_source_monitoring`
  - named form
  - -
  - All items are generated by the participant in one of two ways (said aloud or only thought, written or only imagined), and the test asks which way each was produced.
* - Encoding Task Source Monitoring

    `hedvar_source_memory__encoding_task_source_monitoring`
  - study job: <a href="vocabulary.html#rule-study-then-test-study-job-incidental-judgment">incidental judgment</a>
  - -
  - Each item is studied under one of two judgments (pleasantness, letter count) and the test asks which judgment was made.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Source memory](../processes/long_term_memory.md#hed-source-memory)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Recollection](../processes/long_term_memory.md#hed-recollection)
- [Familiarity](../processes/long_term_memory.md#hed-familiarity)
- [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring)

## Key references

- Johnson, M. K., Hashtroudi, S., & Lindsay, D. S. (1993). Source monitoring. *Psychological Bulletin*, 114(1), 3-28. ([DOI](https://doi.org/10.1037/0033-2909.114.1.3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8346328/))
- Mitchell, K. J., & Johnson, M. K. (2009). Source monitoring 15 years later: What have we learned from fMRI about the neural mechanisms of source memory? *Psychological Bulletin*, 135(4), 638-677. ([DOI](https://doi.org/10.1037/a0015849), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19586165/))
- Glisky, E. L., Polster, M. R., & Routhieaux, B. C. (1995). Double dissociation between item and source memory. *Neuropsychology*, 9(2), 229-235. ([DOI](https://doi.org/10.1037/0894-4105.9.2.229))

## Further references

- Cansino, S., Trejo-Morales, P., & Hernandez-Ramos, E. (2010). Age-related changes in neural activity during source memory encoding in young, middle-aged and elderly adults. *Neuropsychologia*, 48(9), 2537-2549. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2010.04.032), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20441775/))
- Kurkela, K. A., & Dennis, N. A. (2016). Event-related fMRI studies of false memory: An Activation Likelihood Estimation meta-analysis. *Neuropsychologia*, 81, 149-167. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2015.12.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26683385/))
- Bookbinder, S. H., & Brainerd, C. J. (2016). Emotion and false memory: A critical review and meta-analysis. *Psychological Bulletin*, 142(12), 1-24. ([DOI](https://doi.org/10.1037/bul0000077), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27748610/))
- Ciaramelli, E., Faggi, G., Scarpazza, C., Mattioli, F., & Spaniol, J. (2017). Subjective recollection independent from multifeatural context retrieval following damage to the posterior parietal cortex. *Cortex*, 91, 168-179. ([DOI](https://doi.org/10.1016/j.cortex.2017.03.015), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28449939/))

## External links

- Cognitive Atlas: [source memory test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949dd6)

