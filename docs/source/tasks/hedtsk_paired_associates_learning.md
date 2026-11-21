(hedtsk_paired_associates_learning)=
# Paired Associates Learning Task

**HED task ID:** `hedtsk_paired_associates_learning`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** PAL, Paired Associate Learning, Paired Associates Learning

Study of cue-target pairs followed by cued recall; proportion recalled indexes associative encoding and retrieval.

## Description

Participants learn arbitrary associations between stimuli and their locations (or between word pairs). In a typical computerized version (CANTAB PAL), abstract patterns appear in boxes around the screen during the study phase, and during test, patterns are presented centrally and participants must identify the correct box location. Difficulty increases across stages from 1-2 to 6-8 pairs. Performance is measured by patterns correctly learned and errors made. The PAL task is particularly sensitive to hippocampal function and shows early sensitivity to amyloid-beta pathology in preclinical Alzheimer's disease.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">Study, then be tested</a> (`study_then_test`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is studied?* <a href="vocabulary.html#rule-study-then-test-studied-material-pairs">pairs</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-list-length">list length</a>, <a href="vocabulary.html#setting-number-of-repetitions">number of repetitions</a>
- **Material:** Pairs of items - related or unrelated word pairs, face-name pairs, or (in CANTAB PAL) abstract patterns in boxes around the screen.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants study pairs of items (word-word, face-name, object-location) and are later cued with one member to recall the other.
    2. Optional: The same pairs are studied and tested in alternation several times and accuracy per cycle gives a learning curve.
    3. Optional: A second list re-pairs the same cues with new responses, and memory for the first list after the second, or the second given the first, is tested.
* - **Manipulations**
  - - Pair relatedness (semantic, unrelated)
    - Number of pairs
    - Study-test cycles
    - Cue type
    - Pair type (word-word, face-name, object-location)
    - Encoding instruction (incidental vs. intentional)
* - **Measurements**
  - - Cued recall accuracy
    - Number of cycles to criterion
    - Intrusion errors
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
* - Face-Name Paired Associates

    `hedvar_paired_associates_learning__face_name_paired_associates`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
  - Each pair is a face photograph and a name, with the face as cue and the name recalled (or chosen from a list).
* - Object-Location Pairs

    `hedvar_paired_associates_learning__object_location_pairs`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
  - [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory)
  - Each pair is an object and a screen or scene location, with either member able to cue the other.
* - CANTAB PAL

    `hedvar_paired_associates_learning__cantab_pal`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-abstract-patterns">abstract patterns</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-touchscreen">touchscreen</a>
  - -
  - A named touchscreen instrument of the object-location form with the number of patterns rising across stages.
* - Cross-Modal Paired Associates

    `hedvar_paired_associates_learning__cross_modal_paired_associates`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-nonvocal-sounds">nonvocal sounds</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The two members of a pair arrive through different senses or formats, such as a sound with a picture.
* - Multi-Trial Learning Curves

    `hedvar_paired_associates_learning__multi_trial_learning_curves`
  - cycles: <a href="vocabulary.html#rule-study-then-test-cycles-repeated-lists">repeated lists</a>
  - -
  - The same pairs are studied and tested in alternation several times and accuracy per cycle gives a learning curve.
* - Retroactive/Proactive Interference Variants

    `hedvar_paired_associates_learning__retroactive_proactive_interference_variants`
  - interval filler: <a href="vocabulary.html#rule-study-then-test-interval-filler-interference-list">interference list</a>; cycles: <a href="vocabulary.html#rule-study-then-test-cycles-repeated-lists">repeated lists</a>
  - [Proactive interference](../processes/long_term_memory.md#hed-proactive-interference), [Retroactive interference](../processes/long_term_memory.md#hed-retroactive-interference)
  - A second list re-pairs the same cues with new responses, and memory for the first list after the second (or the second given the first) is tested.
* - Incidental vs. Intentional Encoding

    `hedvar_paired_associates_learning__incidental_vs_intentional_encoding`

    Cognitive Atlas: [Incidental encoding task](https://www.cognitiveatlas.org/task/id/trm_50df0dd9d0b6f) (close match)
  - study job: <a href="vocabulary.html#rule-study-then-test-study-job-incidental-judgment">incidental judgment</a>; retention interval: <a href="vocabulary.html#rule-study-then-test-retention-interval-surprise">surprise</a>
  - -
  - In the incidental condition the participant performs a cover judgment on the pairs (rating fit) and the memory test is a surprise.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)
- [Declarative memory](../processes/long_term_memory.md#hed-declarative-memory)

## Key references

- de Rover, M., Pironti, V. A., McCabe, J. A., et al. (2011). Hippocampal dysfunction in patients with mild cognitive impairment: A functional neuroimaging study of a visuospatial paired associates learning task. *Neuropsychologia*, 49(7), 2060-2070. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2011.03.037), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21477602/))

## Further references

- Atkinson, A. L., Berry, E. D. J., Waterman, A. H., Baddeley, A. D., Hitch, G. J., & Allen, R. J. (2018). Are there multiple ways to direct attention in working memory? *Annals of the New York Academy of Sciences*, 1424(1), 115-126. ([DOI](https://doi.org/10.1111/nyas.13634), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29635690/))
- Lim, S. J., Fiez, J. A., & Holt, L. L. (2014). How may the basal ganglia contribute to auditory categorization and speech perception? *Frontiers in Neuroscience*, 8, 230. ([DOI](https://doi.org/10.3389/fnins.2014.00230), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25136291/))
- Parra, M. A., Abrahams, S., Logie, R. H., Méndez, L. G., Lopera, F., & Della Sala, S. (2010). Visual short-term memory binding deficits in familial Alzheimer's disease. *Brain*, 133(9), 2702-2713. ([DOI](https://doi.org/10.1093/brain/awq148), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20624814/))
- Naveh-Benjamin, M. (2000). Adult age differences in memory performance: Tests of an associative deficit hypothesis. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 26(5), 1170-1187. [Updated: Old, S. R., & Naveh-Benjamin, M. (2008). Differential effects of age on item and associative measures of memory. *Psychology and Aging*, 23(1), 104-118.] ([DOI](https://doi.org/10.1037/0278-7393.26.5.1170), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11009251/))

## External links

- Cognitive Atlas: [paired associate learning](https://www.cognitiveatlas.org/task/id/trm_4da88a2a63d97)

- CogPO: [Paired Associate Recall Paradigm](http://www.wiki.cogpo.org/index.php?title=Paired_Associate_Recall_Paradigm)

