(hedtsk_random_dot_kinematogram)=

# Random Dot Kinematogram Task

**HED Task ID:** `hedtsk_random_dot_kinematogram`

**Also known as:** Dot Motion, Random Dot Kinematogram, RDK, Dot Motion Task

A field of moving dots in which a variable fraction move coherently; direction judgments and RT under varying coherence support drift-diffusion modeling of perceptual decisions.

## Description

The random dot kinematogram presents a field of moving dots in which a variable proportion move coherently in one direction while the remainder move randomly. Participants judge the direction of coherent motion, and the proportion of coherently moving dots parametrically controls task difficulty. This paradigm is the foundational tool for studying perceptual decision-making and has been central to establishing the neural basis of evidence accumulation, linking single-neuron recordings in area MT/V5 and LIP to drift-diffusion models of choice. It bridges sensory processing and decision-making in a way no other paradigm does as cleanly.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - A field of moving dots is displayed; a proportion move coherently in one direction while the rest move randomly. Participants judge the direction of coherent motion.
* - **Manipulation**
  - Coherence level (% coherent dots); speed-accuracy instructions; number of alternatives; reward asymmetry.
* - **Measurement**
  - Accuracy and RT as functions of coherence; psychometric and chronometric functions; drift rate and threshold parameters from diffusion model fits.
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
* - Two-Alternative Forced Choice (Standard)
  - Leftward vs. rightward coherent motion; the canonical version used in monkey neurophysiology.
  - Canonical 2AFC motion direction discrimination
* - Free Response vs. Interrogation Protocol
  - Participant-initiated response vs. experimenter-controlled viewing duration; separates speed-accuracy tradeoff from evidence quality.
  - Self-paced vs. fixed-duration decision; different temporal control
* - Pulse Paradigm
  - Brief motion pulses embedded in noise to measure the time course of evidence accumulation.
  - Brief coherence pulses instead of sustained motion; different stimulus structure
* - Multi-Alternative Motion Discrimination
  - Four or more possible directions; tests extensions of drift-diffusion to multi-choice scenarios.
  - More than two motion directions; higher-order discrimination
```

## Cognitive processes

This task engages the following cognitive processes:

- [Perceptual decision making](../processes/perceptual_decision_making_evidence_accumulation.md#hed-perceptual-decision-making)
- [Motion perception](../processes/face_and_object_perception.md#hed-motion-perception)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)

## Key references

- {'authors': 'Britten, K., Shadlen, M., Newsome, W., & Movshon, J.', 'year': 1992, 'title': 'The analysis of visual motion: a comparison of neuronal and psychophysical performance', 'venue': 'The Journal of Neuroscience', 'venue_type': 'journal', 'journal': 'The Journal of Neuroscience', 'volume': '12', 'issue': '12', 'pages': '4745-4765', 'doi': '10.1523/jneurosci.12-12-04745.1992', 'openalex_id': None, 'pmid': None, 'citation_string': 'Britten, K. H., Shadlen, M. N., Newsome, W. T., & Movshon, J. A. (1992). The analysis of visual motion: A comparison of neuronal and psychophysical performance. *Journal of Neuroscience*, 12(12), 4745–4765.', 'url': 'https://doi.org/10.1523/jneurosci.12-12-04745.1992', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Shadlen, M. N., & Newsome, W. T.', 'year': 2001, 'title': 'Neural Basis of a Perceptual Decision in the Parietal Cortex (Area LIP) of the Rhesus Monkey', 'venue': 'Journal of Neurophysiology', 'venue_type': 'journal', 'journal': 'Journal of Neurophysiology', 'volume': '86', 'issue': '4', 'pages': '1916-1936', 'doi': '10.1152/jn.2001.86.4.1916', 'openalex_id': None, 'pmid': None, 'citation_string': 'Shadlen, M. N., & Newsome, W. T. (2001). Neural basis of a perceptual decision in the parietal cortex (area LIP) of the rhesus monkey. *Journal of Neurophysiology*, 86(4), 1916–1936.', 'url': 'https://doi.org/10.1152/jn.2001.86.4.1916', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Gold, J. I., & Shadlen, M. N.', 'year': 2007, 'title': 'The Neural Basis of Decision Making', 'venue': 'Annual Review of Neuroscience', 'venue_type': 'journal', 'journal': 'Annual Review of Neuroscience', 'volume': '30', 'issue': '1', 'pages': '535-574', 'doi': '10.1146/annurev.neuro.29.051605.113038', 'openalex_id': None, 'pmid': None, 'citation_string': 'Gold, J. I., & Shadlen, M. N. (2007). The neural basis of decision making. *Annual Review of Neuroscience*, 30, 535–574.', 'url': 'https://doi.org/10.1146/annurev.neuro.29.051605.113038', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'Ratcliff, R., Smith, P. L., Brown, S. D., & McKoon, G.', 'year': 2016, 'title': 'Diffusion Decision Model: Current Issues and History', 'venue': 'Trends in Cognitive Sciences', 'venue_type': 'journal', 'journal': 'Trends in Cognitive Sciences', 'volume': '20', 'issue': '4', 'pages': '260-281', 'doi': '10.1016/j.tics.2016.01.007', 'openalex_id': None, 'pmid': None, 'citation_string': 'Ratcliff, R., Smith, P. L., Brown, S. D., & McKoon, G. (2016). Diffusion decision model: Current issues and history. *Trends in Cognitive Sciences*, 20(4), 260–281.', 'url': 'https://doi.org/10.1016/j.tics.2016.01.007', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Vafaei Shooshtari, S., Esmaily Sadrabadi, J., Azizi, Z., & Ebrahimpour, R.', 'year': 2019, 'title': 'Confidence Representation of Perceptual Decision by EEG and Eye Data in a Random Dot Motion Task', 'venue': 'Neuroscience', 'venue_type': 'journal', 'journal': 'Neuroscience', 'volume': '406', 'issue': None, 'pages': '510-527', 'doi': '10.1016/j.neuroscience.2019.03.031', 'openalex_id': None, 'pmid': None, 'citation_string': 'Shooshtari, S. V., Sadrabadi, J. E., Azizi, Z., & Ebrahimpour, R. (2019). Confidence representation of perceptual decision by EEG and eye data in a random dot motion task. *Neuroscience*, 406, 510–527.', 'url': 'https://doi.org/10.1016/j.neuroscience.2019.03.031', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Steinemann, N. A., O’Connell, R. G., & Kelly, S. P.', 'year': 2018, 'title': 'Decisions are expedited through multiple neural adjustments spanning the sensorimotor hierarchy', 'venue': 'Nature Communications', 'venue_type': 'journal', 'journal': 'Nature Communications', 'volume': '9', 'issue': '1', 'pages': None, 'doi': '10.1038/s41467-018-06117-0', 'openalex_id': None, 'pmid': None, 'citation_string': "Steinemann, N. A., O'Connell, R. G., & Kelly, S. P. (2018). Decisions are expedited through multiple neural adjustments spanning the sensorimotor hierarchy. *Nature Communications*, 9, 3627.", 'url': 'https://doi.org/10.1038/s41467-018-06117-0', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Sebastian, A., Forstmann, B. U., & Matzke, D.', 'year': 2018, 'title': 'Towards a model-based cognitive neuroscience of stopping – a neuroimaging perspective', 'venue': 'Neuroscience & Biobehavioral Reviews', 'venue_type': 'journal', 'journal': 'Neuroscience & Biobehavioral Reviews', 'volume': '90', 'issue': None, 'pages': '130-136', 'doi': '10.1016/j.neubiorev.2018.04.011', 'openalex_id': None, 'pmid': None, 'citation_string': 'Turner, B. M., van Maanen, L., Forstmann, B. U., & Brown, S. D. (2018). Approaches to analysis in model-based cognitive neuroscience. *Journal of Mathematical Psychology*, 76, 65–79.', 'url': 'https://doi.org/10.1016/j.neubiorev.2018.04.011', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [dot motion task](https://www.cognitiveatlas.org/task/id/trm_4f244ad7dcde7)
