(hedtsk_serial_reaction_time)=

# Serial Reaction Time Task

**HED Task ID:** `hedtsk_serial_reaction_time`

**Also known as:** SRTT, Serial RT

Sequential key-press responses to cued locations; RT speedup on repeating vs random sequences indexes implicit sequence learning.

## Description

The SRTT measures implicit motor sequence learning. Visual stimuli appear sequentially at different spatial locations, each corresponding to a response button. Participants respond as quickly as possible, unaware that stimuli follow a repeating sequence interspersed with random blocks. Learning is inferred from decreasing RT for the repeating sequence relative to random sequences. The dissociation between improved performance and lack of conscious awareness of the sequence structure is a hallmark of implicit learning and provides evidence for procedural memory systems.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - Stimuli appear at one of several spatial locations in a repeating (but covert) sequence; participants respond to each location with a spatially mapped keypress. Sequence awareness is typically not disclosed.
* - **Manipulation**
  - Sequence length and complexity; sequence vs. random blocks; explicit vs. implicit instruction; secondary task (dual-task interference).
* - **Measurement**
  - RT slowing when sequence is replaced by random order (sequence learning effect); explicit sequence knowledge (generation task, recognition); offline consolidation gains.
```

## Variations

```{list-table}
---
widths: 25 40 35
header-rows: 1
---
* - Variation
  - Description
  - Justification
* - Deterministic SRTT
  - Fixed repeating sequence (e.g., 10-element) embedded in random blocks.
  - Fixed repeating sequence; canonical implicit sequence learning
* - Probabilistic SRTT
  - Transition probabilities rather than fixed sequences; tests statistical learning.
  - High-probability sequence structure; tests learning under uncertainty
* - Alternating Serial Reaction Time (ASRT)
  - Pattern and random elements alternate in fixed schedule.
  - Alternating random and patterned elements; tests learning of alternating structure
* - SRTT with Awareness Assessment
  - Post-task sequence generation, recognition, or verbal report tests.
  - Explicit sequence knowledge probed after implicit learning; adds awareness component
* - Second-Order Conditional (SOC) Sequences
  - Sequence structure based on triplet dependencies rather than simple transitions.
  - Each response depends on two preceding; different sequence order
* - Arm-Reaching/Foot-Stepping SRTT
  - Non-finger responses to test effector-specific learning.
  - Full-limb movements instead of finger presses; different motor effector
* - Cross-Modal SRTT
  - Stimuli in different modalities (visual positions, auditory tones) to test modality specificity.
  - Auditory sequence instead of visual; different sensory modality
```

## Cognitive processes

This task engages the following cognitive processes:

- [Motor sequence learning](../processes/motor_preparation_timing_and_execution.md#hed-motor-sequence-learning)
- [Implicit memory](../processes/implicit_and_statistical_learning.md#hed-implicit-memory)
- [Procedural memory](../processes/implicit_and_statistical_learning.md#hed-procedural-memory)
- [Motor preparation](../processes/motor_preparation_timing_and_execution.md#hed-motor-preparation)
- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)

## Key references

- {'authors': 'Nissen, M. J., & Bullemer, P.', 'year': 1987, 'title': 'Attentional requirements of learning: Evidence from performance measures', 'venue': 'Cognitive Psychology', 'venue_type': 'journal', 'journal': 'Cognitive Psychology', 'volume': '19', 'issue': '1', 'pages': '1-32', 'doi': '10.1016/0010-0285(87)90002-8', 'openalex_id': None, 'pmid': None, 'citation_string': 'Nissen, M. J., & Bullemer, P. (1987). Attentional requirements of learning: Evidence from performance measures. *Cognitive Psychology*, 19(1), 1-32.', 'url': 'https://doi.org/10.1016/0010-0285(87)90002-8', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Robertson, E. M.', 'year': 2007, 'title': 'The Serial Reaction Time Task: Implicit Motor Skill Learning?: Figure 1.', 'venue': 'The Journal of Neuroscience', 'venue_type': 'journal', 'journal': 'The Journal of Neuroscience', 'volume': '27', 'issue': '38', 'pages': '10073-10075', 'doi': '10.1523/jneurosci.2747-07.2007', 'openalex_id': None, 'pmid': None, 'citation_string': 'Robertson, E. M. (2007). The serial reaction time task: Implicit motor skill learning? *Journal of Neuroscience*, 27(38), 10073-10075.', 'url': 'https://doi.org/10.1523/jneurosci.2747-07.2007', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Grafton, S. T., Hazeltine, E., & Ivry, R.', 'year': 1995, 'title': 'Functional Mapping of Sequence Learning in Normal Humans', 'venue': 'Journal of Cognitive Neuroscience', 'venue_type': 'journal', 'journal': 'Journal of Cognitive Neuroscience', 'volume': '7', 'issue': '4', 'pages': '497-510', 'doi': '10.1162/jocn.1995.7.4.497', 'openalex_id': None, 'pmid': None, 'citation_string': 'Grafton, S. T., Hazeltine, E., & Ivry, R. B. (1995). Functional mapping of sequence learning in normal humans. *Journal of Cognitive Neuroscience*, 7(4), 497-510.', 'url': 'https://doi.org/10.1162/jocn.1995.7.4.497', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'Janacsek, K., & Nemeth, D.', 'year': 2012, 'title': 'Predicting the future: From implicit learning to consolidation', 'venue': 'International Journal of Psychophysiology', 'venue_type': 'journal', 'journal': 'International Journal of Psychophysiology', 'volume': '83', 'issue': '2', 'pages': '213-221', 'doi': '10.1016/j.ijpsycho.2011.11.012', 'openalex_id': None, 'pmid': None, 'citation_string': 'Janacsek, K., & Nemeth, D. (2012). Predicting the future: From implicit learning to consolidation. *International Journal of Psychophysiology*, 83(2), 213–221.', 'url': 'https://doi.org/10.1016/j.ijpsycho.2011.11.012', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Abrahamse, E. L., Jiménez, L., Verwey, W. B., & Clegg, B. A.', 'year': 2010, 'title': 'Representing serial action and perception', 'venue': 'Psychonomic Bulletin & Review', 'venue_type': 'journal', 'journal': 'Psychonomic Bulletin & Review', 'volume': '17', 'issue': '5', 'pages': '603-623', 'doi': '10.3758/pbr.17.5.603', 'openalex_id': None, 'pmid': None, 'citation_string': 'Abrahamse, E. L., Jiménez, L., Verwey, W. B., & Clegg, B. A. (2010). Representing serial action and perception. *Psychonomic Bulletin & Review*, 17(5), 603–623.', 'url': 'https://doi.org/10.3758/pbr.17.5.603', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Siegert, R. J., Taylor, K. D., Weatherall, M., & Abernethy, D. A.', 'year': 2006, 'title': "Is implicit sequence learning impaired in Parkinson's disease? A meta-analysis.", 'venue': 'Neuropsychology', 'venue_type': 'journal', 'journal': 'Neuropsychology', 'volume': '20', 'issue': '4', 'pages': '490-495', 'doi': '10.1037/0894-4105.20.4.490', 'openalex_id': None, 'pmid': None, 'citation_string': "Siegert, R. J., Taylor, K. D., Weatherall, M., & Abernethy, D. A. (2006). Is implicit sequence learning impaired in Parkinson's disease? A meta-analysis. *Neuropsychology*, 20(4), 490–495. \[Updated: Clark, G. M., Lum, J. A., & Ullman, M. T. (2014). A meta-analysis and meta-regression of serial reaction time task performance in Parkinson's disease. *Neuropsychology*, 28(6), 945–958.\]", 'url': 'https://doi.org/10.1037/0894-4105.20.4.490', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [serial reaction time task](https://www.cognitiveatlas.org/task/id/trm_4f241c735e7f6)
