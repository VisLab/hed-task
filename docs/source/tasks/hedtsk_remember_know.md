(hedtsk_remember_know)=
# Remember/Know Task

**HED task ID:** `hedtsk_remember_know`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** R/K Paradigm, Remember-Know

Classify recognition hits as 'remember' (vivid recollection) or 'know' (familiarity without context); proportions index the relative contributions of recollection and familiarity to recognition memory.

## Description

During a recognition memory test, participants classify each item they judge as "old" according to the subjective quality of their memory: "remember" if they can recollect specific contextual details from the encoding episode (e.g., what they were thinking, where the item appeared), or "know" if the item feels familiar but retrieval of contextual details fails. Tulving (1985) introduced this distinction to operationalize the difference between episodic recollection and noetic familiarity. The paradigm has become the primary behavioral tool for dual-process theories of recognition memory and has been extensively validated with neuroimaging, revealing dissociable hippocampal (recollection) and perirhinal (familiarity) contributions.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - During a recognition memory test, participants first judge each item as old or new, then classify old responses as 'remember' (vivid recollection of encoding context) or 'know' (familiarity without recollection).
* - **Manipulation**
  - Encoding depth (deep vs. shallow processing); divided attention at encoding; item type (words, faces, scenes).
* - **Measurement**
  - Proportion remember and know responses for hits and false alarms; estimates of recollection and familiarity (dual-process model parameters).
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
* - Standard Remember/Know

    `hedvar_remember_know__standard_remember_know`
  - Binary R/K judgment on each recognized item; the canonical version.
  - Canonical R/K: recollection vs. familiarity distinction
* - Remember/Know/Guess (RKG)

    `hedvar_remember_know__remember_know_guess_rkg`
  - Three-way classification adding "guess" to capture below-threshold familiarity.
  - Third Guess category added; different response scale
* - Remember/Know with Source Memory

    `hedvar_remember_know__remember_know_with_source_memory`
  - R/K judgment followed by a source question (e.g., which list, which voice, which location).
  - Source judgment added to R/K; adds contextual memory component
* - Associative Remember/Know

    `hedvar_remember_know__associative_remember_know`
  - Applied to associative recognition (word pairs) rather than item recognition.
  - R/K for associative pairs; tests recollection of binding
```

## Cognitive processes

This task is designed to engage the following processes:

- [Recollection](../processes/long_term_memory.md#hed-recollection)
- [Familiarity](../processes/long_term_memory.md#hed-familiarity)
- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)
- [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)

## Key references

- Tulving, E. (1985). Memory and consciousness. *Canadian Psychology*, 26(1), 1–12. ([DOI](https://doi.org/10.1037/h0080017))
- Gardiner, J. M. (1988). Functional aspects of recollective experience. *Memory & Cognition*, 16(4), 309–313. ([DOI](https://doi.org/10.3758/bf03197041), [PubMed](https://pubmed.ncbi.nlm.nih.gov/3210971/))

## Further references

- Yonelinas, A. P., Aly, M., Wang, W.-C., & Koen, J. D. (2010). Recollection and familiarity: Examining controversial assumptions and new directions. *Hippocampus*, 20(11), 1178–1194. ([DOI](https://doi.org/10.1002/hipo.20864), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20848606/))
- Wixted, J. T., & Mickes, L. (2010). A continuous dual-process model of remember/know judgments. *Psychological Review*, 117(4), 1025–1054. ([DOI](https://doi.org/10.1037/a0020874), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20836613/))
- Migo, E. M., Mayes, A. R., & Montaldi, D. (2012). Measuring recollection and familiarity: Improving the remember/know procedure. *Consciousness and Cognition*, 21(3), 1435–1455. ([DOI](https://doi.org/10.1016/j.concog.2012.04.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22846231/))
- Bastin, C., Besson, G., Simon, J., Delhaye, E., Geurten, M., Willems, S., & Salmon, E. (2019). An integrative memory model of recollection and familiarity to understand memory deficits. *Behavioral and Brain Sciences*, 42, e281. ([DOI](https://doi.org/10.1017/s0140525x19000621), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30719958/))

## External links

- Cognitive Atlas: [remember/know task](https://www.cognitiveatlas.org/task/id/trm_4da63146f12d7)

