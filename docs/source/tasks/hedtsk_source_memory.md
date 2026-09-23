(hedtsk_source_memory)=
# Source Memory Task

**HED task ID:** `hedtsk_source_memory`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** Source Monitoring Task, Reality Monitoring Task, Context Memory Task, Source Judgment Task

After studying items presented in distinct contexts (speaker, location, modality, time), participants judge each item's encoding source; source accuracy dissociates contextual recollection from item familiarity.

## Description

Source memory tests assess the ability to remember the contextual details of an encoding episode — not just whether an item was encountered (item memory) but where, when, how, or from whom it was learned. In the standard paradigm, items are presented under two or more source conditions (e.g., spoken by a male vs. female voice; shown on the left vs. right of the screen; read vs. imagined). At test, participants first make an old/new recognition judgment, then indicate the source of each recognized item. Source accuracy (correct source attributions conditional on item recognition) is the primary measure, dissociating recollection-based contextual retrieval from familiarity-based item recognition. Johnson's source monitoring framework (Johnson, Hashtroudi, & Lindsay, 1993) distinguishes external source monitoring (which person said it), internal source monitoring (did I do it or imagine it), and reality monitoring (internal vs. external origin). Source memory failures underlie false memories, eyewitness misattributions, and confabulation. The paradigm recruits prefrontal cortex (especially right and medial PFC for monitoring) and hippocampus (binding items to contexts), with a characteristic dissociation from item memory in aging and frontal lesion patients.

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
    - Remember/know × source interaction
    - Source attribution errors (systematic misattributions)
    - PFC and hippocampal activation differences
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
* - Voice Source Monitoring

    `hedvar_source_memory__voice_source_monitoring`
  - Items spoken by different voices (male/female, or specific speakers). The canonical auditory source paradigm; sensitive to frontal lobe function.
  - Speaker identity as source attribute; canonical source monitoring
* - Spatial Source Monitoring

    `hedvar_source_memory__spatial_source_monitoring`
  - Items presented in different screen locations or rooms. Tests spatial context binding.
  - Location as source attribute; different source dimension
* - Temporal Source Monitoring

    `hedvar_source_memory__temporal_source_monitoring`
  - Items from different study lists or temporal positions. Requires temporal order or list discrimination.
  - Time of occurrence as source; different temporal memory dimension
* - Reality Monitoring

    `hedvar_source_memory__reality_monitoring`
  - Discriminate self-generated items (imagined, spoken aloud) from externally presented items. Johnson & Raye (1981) framework; uses qualitative characteristics (perceptual detail vs. cognitive operations) as cues.
  - Internal vs. external origin judgment; distinct reality monitoring paradigm
* - Internal Source Monitoring

    `hedvar_source_memory__internal_source_monitoring`
  - Discriminate between two self-generated sources (e.g., imagined vs. spoken, thought vs. written). Tests monitoring of internal cognitive operations.
  - Self-generated vs. experimenter-presented items; different internal/external distinction
* - Modality Source Monitoring

    `hedvar_source_memory__modality_source_monitoring`
  - Discriminate auditory vs. visual presentation. Cross-modal binding measure.
  - Auditory vs. visual presentation as source; different sensory source
* - Encoding Task Source Monitoring

    `hedvar_source_memory__encoding_task_source_monitoring`
  - Items processed with different encoding tasks (e.g., pleasantness vs. concreteness rating). Source = cognitive operation performed at encoding.
  - Which encoding task was used as source; different procedural context
* - Multi-Source (3+ Sources)

    `hedvar_source_memory__multi_source_3_sources`
  - Three or more source conditions (e.g., three different speakers). Increases demand on monitoring precision; enables systematic misattribution analysis.
  - Three or more source attributes; higher discrimination demand
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

