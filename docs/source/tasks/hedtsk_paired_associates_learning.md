(hedtsk_paired_associates_learning)=
# Paired Associates Learning Task

**HED task ID:** `hedtsk_paired_associates_learning`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** PAL, Paired Associate Learning

Study of cue-target pairs followed by cued recall; proportion recalled indexes associative encoding and retrieval.

## Description

Participants learn arbitrary associations between stimuli and their locations (or between word pairs). In a typical computerized version (CANTAB PAL), abstract patterns appear in boxes around the screen during the study phase, and during test, patterns are presented centrally and participants must identify the correct box location. Difficulty increases across stages from 1-2 to 6-8 pairs. Performance is measured by patterns correctly learned and errors made. The PAL task is particularly sensitive to hippocampal function and shows early sensitivity to amyloid-beta pathology in preclinical Alzheimer's disease.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants study pairs of items (word-word, face-name, object-location) and are later cued with one member to recall the other.
* - **Manipulation**
  - Pair relatedness (semantic, unrelated); number of pairs; study-test cycles; cue type.
* - **Measurement**
  - Cued recall accuracy; number of cycles to criterion; intrusion errors.
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
* - Verbal Paired Associates (Cued Recall)

    `hedvar_paired_associates_learning__verbal_paired_associates_cued_recall`
  - Word pairs; cue with first word, recall second.
  - Canonical word-word pairs with cued recall test
* - Face-Name Paired Associates

    `hedvar_paired_associates_learning__face_name_paired_associates`
  - Naturalistic variant; sensitive to aging and early AD.
  - Face-name binding; social memory domain
* - Object-Location Pairs

    `hedvar_paired_associates_learning__object_location_pairs`
  - Associate objects with spatial locations; engages hippocampal binding.
  - Object-location binding; spatial memory component
* - CANTAB PAL

    `hedvar_paired_associates_learning__cantab_pal`
  - Computerized abstract pattern-location associations; graded difficulty.
  - Touchscreen object-location paradigm; named computerized instrument
* - Arbitrary vs. Semantically Related Pairs

    `hedvar_paired_associates_learning__arbitrary_vs_semantically_related_pairs`
  - Unrelated pairs tax hippocampal binding; related pairs benefit from semantic support.
  - Relatedness manipulation changes encoding strategy
* - Cross-Modal Paired Associates

    `hedvar_paired_associates_learning__cross_modal_paired_associates`
  - Pair across modalities (sound-image, word-location).
  - Pairs span sensory modalities; cross-modal binding demand
* - Multi-Trial Learning Curves

    `hedvar_paired_associates_learning__multi_trial_learning_curves`
  - Repeated study-test cycles; tracks acquisition rate.
  - Repeated study-test cycles; tests learning rate over trials
* - Retroactive/Proactive Interference Variants

    `hedvar_paired_associates_learning__retroactive_proactive_interference_variants`
  - Overlapping pairs (A-B, A-C) to study interference mechanisms.
  - Competing pairs introduced; tests interference in associative memory
* - Incidental vs. Intentional Encoding

    `hedvar_paired_associates_learning__incidental_vs_intentional_encoding`
  - With or without awareness of upcoming test.
  - Encoding goal manipulation; tests depth and intentionality of encoding
```

## Cognitive processes

This task is designed to engage the following processes:

- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)
- [Declarative memory](../processes/long_term_memory.md#hed-declarative-memory)

## Key references

- de Rover, M., Pironti, V. A., McCabe, J. A., et al. (2011). Hippocampal dysfunction in patients with mild cognitive impairment: A functional neuroimaging study of a visuospatial paired associates learning task. *Neuropsychologia*, 49(7), 2060-2070.

## Recent references

- Atkinson, A. L., Berry, E. D. J., Waterman, A. H., Baddeley, A. D., Hitch, G. J., & Allen, R. J. (2018). Are there multiple ways to direct attention in working memory? *Annals of the New York Academy of Sciences*, 1424(1), 115–126.
- Lim, S. J., Fiez, J. A., & Holt, L. L. (2014). How may the basal ganglia contribute to auditory categorization and speech perception? *Frontiers in Neuroscience*, 8, 230.
- Parra, M. A., Abrahams, S., Logie, R. H., Méndez, L. G., Lopera, F., & Della Sala, S. (2010). Visual short-term memory binding deficits in familial Alzheimer's disease. *Brain*, 133(9), 2702–2713.
- Naveh-Benjamin, M. (2000). Adult age differences in memory performance: Tests of an associative deficit hypothesis. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 26(5), 1170–1187. [Updated: Old, S. R., & Naveh-Benjamin, M. (2008). Differential effects of age on item and associative measures of memory. *Psychology and Aging*, 23(1), 104–118.]

## External links

- Cognitive Atlas: [paired associate learning](https://www.cognitiveatlas.org/task/id/trm_4da88a2a63d97)

