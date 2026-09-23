(hedtsk_mnemonic_similarity)=
# Mnemonic Similarity Task

**HED task ID:** `hedtsk_mnemonic_similarity`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** MST, Mnemonic Discrimination Task, Pattern Separation Task, Mnemonic Similarity

Incidental encoding of images followed by a test with old, new, and lure items; discrimination of lures from repetitions indexes pattern separation.

## Description

The Mnemonic Similarity Task measures hippocampal pattern separation—the ability to distinguish similar but not identical memory representations. During encoding, participants view a series of everyday object images. At test, they classify each image as "old" (previously seen), "similar" (a different exemplar of a studied object with slight visual changes), or "new" (novel). The critical measure is the ability to correctly identify "similar" lures as similar rather than incorrectly endorsing them as old. This discrimination (lure discrimination index) is thought to rely on dentate gyrus/CA3 pattern separation processes and is impaired in early-stage Alzheimer's disease and normal aging.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants study a set of images, then view old items, new items, and similar lures (items resembling studied items).
    2. They classify each as old, new, or similar.
* - **Manipulations**
  - - Lure similarity (mnemonic similarity parameter)
    - Encoding depth
    - Retention interval
    - Number of items
* - **Measurements**
  - - Lure discrimination index (LDI: p('similar'|lure) − p('similar'|foil))
    - Recognition d-prime
    - Pattern separation score
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
* - Standard Object MST

    `hedvar_mnemonic_similarity__standard_object_mst`
  - Indoor and outdoor objects; old/similar/new judgments.
  - Canonical everyday objects with lure pairs for pattern separation
* - Scene MST

    `hedvar_mnemonic_similarity__scene_mst`
  - Indoor/outdoor scene photographs as stimuli; spatial pattern separation.
  - Scene stimuli instead of objects; different stimulus class
* - Continuous MST

    `hedvar_mnemonic_similarity__continuous_mst`
  - Online recognition during a single continuous stream; no separate study/test phases.
  - Study and test interleaved; different trial structure
* - Parametric Similarity Manipulation

    `hedvar_mnemonic_similarity__parametric_similarity_manipulation`
  - Lures at graded levels of similarity (high, medium, low) to the studied items.
  - Graded lure similarity levels; tests pattern separation threshold
* - MST for Faces

    `hedvar_mnemonic_similarity__mst_for_faces`
  - Face stimuli to test pattern separation for social stimuli.
  - Face stimuli; different recognition domain
* - Spatial MST

    `hedvar_mnemonic_similarity__spatial_mst`
  - Objects in spatial contexts; measures spatial vs. object pattern separation.
  - Location-based similarity; tests spatial pattern separation
* - Short-Delay vs. Long-Delay MST

    `hedvar_mnemonic_similarity__short_delay_vs_long_delay_mst`
  - Varying retention interval between encoding and test.
  - Retention interval manipulation tests forgetting of pattern separation
```

## Cognitive processes

This task is designed to engage the following processes:

- [Pattern separation](../processes/long_term_memory.md#hed-pattern-separation)
- [Pattern completion](../processes/long_term_memory.md#hed-pattern-completion)
- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)
- [Familiarity](../processes/long_term_memory.md#hed-familiarity)

## Key references

- Kirwan, C. B., & Stark, C. E. L. (2007). Overcoming interference: An fMRI investigation of pattern separation in the medial temporal lobe. *Learning & Memory*, 14(9), 625–633. ([DOI](https://doi.org/10.1101/lm.663507), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17848502/))
- Stark, S. M., Yassa, M. A., Lacy, J. W., & Stark, C. E. L. (2013). A task to assess behavioral pattern separation (BPS) in humans: Data from healthy aging and mild cognitive impairment. *Neuropsychologia*, 51(12), 2442–2449. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2012.12.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23313292/))
- Yassa, M. A., & Stark, C. E. L. (2011). Pattern separation in the hippocampus. *Trends in Neurosciences*, 34(10), 515–525. ([DOI](https://doi.org/10.1016/j.tins.2011.06.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21788086/))

## Further references

- Lacy, J. W., Yassa, M. A., Stark, S. M., Muftuler, L. T., & Stark, C. E. L. (2011). Distinct pattern separation related transfer functions in human CA3/dentate and CA1 revealed using high-resolution fMRI and variable mnemonic similarity. *Learning & Memory*, 18(1), 15–18. ([DOI](https://doi.org/10.1101/lm.1971111))
- Bakker, A., Kirwan, C. B., Miller, M., & Stark, C. E. L. (2008). Pattern separation in the human hippocampal CA3 and dentate gyrus. *Science*, 319(5870), 1640–1642. ([DOI](https://doi.org/10.1126/science.1152882), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18356518/))
- Stark, S. M., & Stark, C. E. L. (2017). Age-related deficits in the mnemonic similarity task for objects and scenes. *Behavioural Brain Research*, 333, 109–117. ([DOI](https://doi.org/10.1016/j.bbr.2017.06.049), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28673769/))
- Reagh, Z. M., & Yassa, M. A. (2014). Object and spatial mnemonic interference differentially engage lateral and medial entorhinal cortex in humans. *Proceedings of the National Academy of Sciences*, 111(40), E4264–E4273. ([DOI](https://doi.org/10.1073/pnas.1411250111), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25246569/))

## External links

- Cognitive Atlas: [Mnemonic similarity task](https://www.cognitiveatlas.org/task/id/tsk_RXmB56vrYW66T)

