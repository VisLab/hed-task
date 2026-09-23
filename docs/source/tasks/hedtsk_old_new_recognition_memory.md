(hedtsk_old_new_recognition_memory)=
# Old/New Recognition Memory Task

**HED task ID:** `hedtsk_old_new_recognition_memory`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** Recognition Memory Test, Yes/No Recognition

Studied items mixed with new lures at test; hit and false-alarm rates yield d' and can be decomposed into recollection and familiarity via ROC or remember/know.

## Description

Participants study a list of stimuli (words, pictures, or faces) during an encoding phase. In the test phase, they view a mixture of studied (old) and unstudied (new) items and make binary old/new recognition judgments. Performance is analyzed using signal detection measures (hits, false alarms, d') and can be further decomposed into familiarity-based (rapid, automatic) and recollection-based (slower, effortful) processes using confidence ratings or remember/know judgments. Neuroimaging consistently implicates the hippocampus, angular gyrus, and default mode network in successful recognition.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants study a list of items, then view a test list containing studied (old) items and unstudied (new) items and classify each as old or new.
* - **Manipulations**
  - - Study list length
    - Encoding depth (levels of processing)
    - Retention interval
    - Confidence judgment
    - Response deadline
* - **Measurements**
  - - Hit rate, false alarm rate, d-prime (discriminability), criterion (response bias)
    - ROC curves
    - Remember/know judgments (when combined)
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
* - Standard Old/New

    `hedvar_old_new_recognition_memory__standard_old_new`
  - Binary old/new judgments to studied and unstudied items.
  - Canonical yes/no recognition judgment
* - Remember-Know (R/K)

    `hedvar_old_new_recognition_memory__remember_know_r_k`
  - Subjective classification of old items as recollected or familiar.
  - Participant distinguishes recollection from familiarity; different response scale
* - Source Memory

    `hedvar_old_new_recognition_memory__source_memory`
  - Report item + encoding context (which list, voice, location).
  - Identify source context of recognized item; adds contextual retrieval judgment
* - Associative Recognition

    `hedvar_old_new_recognition_memory__associative_recognition`
  - Test whether pairs were studied together; probes binding/relational memory.
  - Judge intact vs. rearranged pairs; tests associative vs. item memory
* - Forced-Choice Recognition

    `hedvar_old_new_recognition_memory__forced_choice_recognition`
  - Choose which of two alternatives was studied; reduces criterion effects.
  - Select target from foil array; different response structure
* - Continuous Recognition

    `hedvar_old_new_recognition_memory__continuous_recognition`
  - Items repeat within a long list at varying lags; combines encoding and retrieval.
  - Study and test interleaved in ongoing stream; different trial structure
* - DRM (Deese-Roediger-McDermott) False Memory Variant

    `hedvar_old_new_recognition_memory__drm_deese_roediger_mcdermott_false_memory_variant`
  - Includes highly associated lures that produce robust false recognition.
  - Semantically related lures elicit false recognition; distinct false memory paradigm
```

## Cognitive processes

This task is designed to engage the following processes:

- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Recollection](../processes/long_term_memory.md#hed-recollection)
- [Familiarity](../processes/long_term_memory.md#hed-familiarity)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)

## Key references

- Mandler, G. (1980). Recognizing: The judgment of previous occurrence. *Psychological Review*, 87(3), 252-271. ([DOI](https://doi.org/10.1037/0033-295x.87.3.252))
- Henson, R. N., Rugg, M. D., Shallice, T., Josephs, O., & Dolan, R. J. (1999). Recollection and familiarity in recognition memory: An event-related functional magnetic resonance imaging study. *Journal of Neuroscience*, 19(10), 3962-3972. ([DOI](https://doi.org/10.1523/jneurosci.19-10-03962.1999), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10234026/))
- Rugg, M. D., & Curran, T. (2007). Event-related potentials and recognition memory. *Trends in Cognitive Sciences*, 11(6), 251-257. ([DOI](https://doi.org/10.1016/j.tics.2007.04.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17481940/))

## Further references

- Wixted, J. T. (2007). Dual-process theory and signal-detection theory of recognition memory. *Psychological Review*, 114(1), 152–176. ([DOI](https://doi.org/10.1037/0033-295x.114.1.152), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17227185/))
- Rugg, M. D., & Vilberg, K. L. (2013). Brain networks underlying episodic memory retrieval. *Current Opinion in Neurobiology*, 23(2), 255–260. ([DOI](https://doi.org/10.1016/j.conb.2012.11.005), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23206590/))
- Wixted, J. T., & Mickes, L. (2014). A signal-detection-based diagnostic-feature-detection model of eyewitness identification. *Psychological Review*, 121(4), 588–607. ([DOI](https://doi.org/10.1037/a0035940), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24730600/))

## External links

- Cognitive Atlas: [recognition memory test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949d40)

- CogPO: [Cued Explicit Recognition Paradigm](http://www.wiki.cogpo.org/index.php?title=Cued_Explicit_Recognition_Paradigm)

