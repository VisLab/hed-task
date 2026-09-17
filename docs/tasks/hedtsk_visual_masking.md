(hedtsk_visual_masking)=

# Visual Masking Task

**HED Task ID:** `hedtsk_visual_masking`

**Also known as:** Backward Masking, Metacontrast Masking, Pattern Masking

A brief target is rendered invisible or reduced in visibility by a preceding or following mask; variants include metacontrast, paracontrast, pattern, forward, backward, common-onset, and object-substitution masking.

## Description

Participants attempt to detect or discriminate brief, near-threshold visual stimuli that are rendered difficult to see through low contrast, brief duration, or metacontrast masking (a spatially adjacent, temporally trailing mask that suppresses visibility of the target without overlapping it spatially). The key dependent variable is not only accuracy but the relationship between trial-by-trial detection success and prestimulus brain states — particularly the phase and power of ongoing alpha (~10 Hz) and theta (~7 Hz) oscillations recorded via EEG. This paradigm demonstrates that conscious visual perception is not a passive, deterministic process but is gated by rhythmic fluctuations in cortical excitability, supporting pulsed-inhibition and perceptual-sampling theories.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - A brief target stimulus is rendered invisible or reduced in visibility by a temporally adjacent mask. Participants detect, identify, or discriminate the target.
* - **Manipulation**
  - Mask type (metacontrast, pattern, backward, forward, common-onset, object-substitution); SOA/ISA between target and mask; target-mask spatial relationship; mask energy.
* - **Measurement**
  - Target detection/identification accuracy or d-prime as a function of SOA (U-shaped or monotonic masking functions); subjective visibility ratings; priming effects from unseen targets.
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
* - Standard Metacontrast Masking
  - Target followed by annular mask at variable SOAs; measure detection/discrimination accuracy.
  - Canonical metacontrast: annular mask suppresses disc
* - Phosphene Detection at Threshold
  - Near-threshold light flashes on uniform background; simplest version eliminating masking.
  - TMS-evoked phosphenes measured at perceptual threshold
* - TMS-Evoked Phosphene Detection
  - Transcranial magnetic stimulation to visual cortex at varying alpha phases; causal test of oscillatory gating.
  - Visual cortex stimulation produces phosphene; different masking mechanism
* - Object Substitution Masking
  - Four-dot mask surrounding target location; tests different masking mechanism than metacontrast.
  - Four-dot surround mask replaces object representation; different mechanism
* - Pattern Masking at Threshold
  - Random-dot or noise-pattern mask overlapping target spatially; distinguishes from metacontrast which is non-overlapping.
  - Pattern mask overlapping in space and time; different mask type
* - Continuous Flash Suppression Threshold
  - Mondrian-pattern masking to one eye while target presented to the other; binocular rivalry version.
  - Monocular suppression by rapidly alternating masks; binocular suppression paradigm
* - Rhythmic Entrainment + Detection
  - Presenting rhythmic visual streams before the target to entrain alpha and test whether entrained phase modulates detection.
  - Rhythmic stimulation before target; tests oscillatory effects on detection
* - Masked Priming Variant
  - Masked stimuli serve as primes for subsequent visible targets; measures subliminal processing below the consciousness threshold.
  - Masked prime before target; tests subliminal priming via masking
* - Backward Masking with Attentional Manipulation
  - Combining masking with dual-task or attentional-blink paradigms to examine attention × consciousness interactions.
  - Attention directed during masking; tests attentional modulation of masking
* - Auditory Backward Masking
  - Analogous paradigm in auditory modality; tone detection masked by noise burst at variable SOAs.
  - Auditory masking paradigm; different sensory modality
```

## Cognitive processes

This task engages the following cognitive processes:

- [Masking](../processes/awareness_agency_and_metacognition.md#hed-masking)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Perceptual awareness](../processes/awareness_agency_and_metacognition.md#hed-perceptual-awareness)
- [Attentional awareness](../processes/awareness_agency_and_metacognition.md#hed-attentional-awareness)

## Key references

- {'authors': 'Mathewson, K. E., Gratton, G., Fabiani, M., Beck, D. M., & Ro, T.', 'year': 2009, 'title': 'To See or Not to See: Prestimulus α Phase Predicts Visual Awareness', 'venue': 'The Journal of Neuroscience', 'venue_type': 'journal', 'journal': 'The Journal of Neuroscience', 'volume': '29', 'issue': '9', 'pages': '2725-2732', 'doi': '10.1523/jneurosci.3963-08.2009', 'openalex_id': None, 'pmid': None, 'citation_string': 'Mathewson, K. E., Gratton, G., Fabiani, M., Beck, D. M., & Ro, T. (2009). To see or not to see: Prestimulus alpha phase predicts visual awareness. *Journal of Neuroscience*, 29(9), 2725–2732.', 'url': 'https://doi.org/10.1523/jneurosci.3963-08.2009', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Busch, N. A., Dubois, J., & VanRullen, R.', 'year': 2009, 'title': 'The Phase of Ongoing EEG Oscillations Predicts Visual Perception', 'venue': 'Journal of Neuroscience', 'venue_type': 'journal', 'journal': 'Journal of Neuroscience', 'volume': '29', 'issue': '24', 'pages': '7869-7876', 'doi': '10.1523/jneurosci.0113-09.2009', 'openalex_id': None, 'pmid': None, 'citation_string': 'Busch, N. A., Dubois, J., & VanRullen, R. (2009). The phase of ongoing EEG oscillations predicts visual perception. *Journal of Neuroscience*, 29(24), 7869–7876.', 'url': 'https://doi.org/10.1523/jneurosci.0113-09.2009', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'VanRullen, R., & Koch, C.', 'year': 2003, 'title': 'Is perception discrete or continuous?', 'venue': 'Trends in Cognitive Sciences', 'venue_type': 'journal', 'journal': 'Trends in Cognitive Sciences', 'volume': '7', 'issue': '5', 'pages': '207-213', 'doi': '10.1016/s1364-6613(03)00095-0', 'openalex_id': None, 'pmid': None, 'citation_string': 'VanRullen, R., & Koch, C. (2003). Is perception discrete or continuous? *Trends in Cognitive Sciences*, 7(5), 207–213.', 'url': 'https://doi.org/10.1016/s1364-6613(03)00095-0', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Del Cul, A., Baillet, S., & Dehaene, S.', 'year': 2007, 'title': 'Brain Dynamics Underlying the Nonlinear Threshold for Access to Consciousness', 'venue': 'PLoS Biology', 'venue_type': 'journal', 'journal': 'PLoS Biology', 'volume': '5', 'issue': '10', 'pages': 'e260', 'doi': '10.1371/journal.pbio.0050260', 'openalex_id': None, 'pmid': None, 'citation_string': 'Del Cul, A., Baillet, S., & Dehaene, S. (2007). Brain dynamics underlying the nonlinear threshold for access to consciousness. *PLoS Biology*, 5(10), e260.', 'url': 'https://doi.org/10.1371/journal.pbio.0050260', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Dehaene, S., & Changeux, J.', 'year': 2011, 'title': 'Experimental and Theoretical Approaches to Conscious Processing', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '70', 'issue': '2', 'pages': '200-227', 'doi': '10.1016/j.neuron.2011.03.018', 'openalex_id': None, 'pmid': None, 'citation_string': 'Dehaene, S., & Changeux, J. P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200–227.', 'url': 'https://doi.org/10.1016/j.neuron.2011.03.018', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Sergent, C., & Dehaene, S.', 'year': 2004, 'title': 'Is Consciousness a Gradual Phenomenon?', 'venue': 'Psychological Science', 'venue_type': 'journal', 'journal': 'Psychological Science', 'volume': '15', 'issue': '11', 'pages': '720-728', 'doi': '10.1111/j.0956-7976.2004.00748.x', 'openalex_id': None, 'pmid': None, 'citation_string': 'Sergent, C., & Dehaene, S. (2004). Is consciousness a gradual phenomenon? Evidence for an all-or-none bifurcation during the attentional blink. *Psychological Science*, 15(11), 720–728.', 'url': 'https://doi.org/10.1111/j.0956-7976.2004.00748.x', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'VanRullen, R.', 'year': 2016, 'title': 'Perceptual Cycles', 'venue': 'Trends in Cognitive Sciences', 'venue_type': 'journal', 'journal': 'Trends in Cognitive Sciences', 'volume': '20', 'issue': '10', 'pages': '723-735', 'doi': '10.1016/j.tics.2016.07.006', 'openalex_id': None, 'pmid': None, 'citation_string': 'VanRullen, R. (2016). Perceptual cycles. *Trends in Cognitive Sciences*, 20(10), 723–735.', 'url': 'https://doi.org/10.1016/j.tics.2016.07.006', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Dugué, L., Marque, P., & VanRullen, R.', 'year': 2011, 'title': 'The Phase of Ongoing Oscillations Mediates the Causal Relation between Brain Excitation and Visual Perception', 'venue': 'The Journal of Neuroscience', 'venue_type': 'journal', 'journal': 'The Journal of Neuroscience', 'volume': '31', 'issue': '33', 'pages': '11889-11893', 'doi': '10.1523/jneurosci.1161-11.2011', 'openalex_id': None, 'pmid': None, 'citation_string': 'Dugué, L., Marque, P., & VanRullen, R. (2011). The phase of ongoing oscillations mediates the causal relation between brain excitation and visual perception. *Journal of Neuroscience*, 31(33), 11889–11893.', 'url': 'https://doi.org/10.1523/jneurosci.1161-11.2011', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Iemi, L., Busch, N. A., Laudini, A., Haegens, S., Samaha, J., Villringer, A., & Nikulin, V. V.', 'year': 2019, 'title': 'Multiple mechanisms link prestimulus neural oscillations to sensory responses', 'venue': 'eLife', 'venue_type': 'journal', 'journal': 'eLife', 'volume': '8', 'issue': None, 'pages': None, 'doi': '10.7554/elife.43620', 'openalex_id': None, 'pmid': None, 'citation_string': 'Iemi, L., Busch, N. A., Laudini, A., Haegens, S., Samaha, J., Villringer, A., & Nikulin, V. V. (2019). Multiple mechanisms link prestimulus neural oscillations to sensory responses. *eLife*, 8, e43620.', 'url': 'https://doi.org/10.7554/elife.43620', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Samaha, J., Iemi, L., Haegens, S., & Busch, N. A.', 'year': 2020, 'title': 'Spontaneous Brain Oscillations and Perceptual Decision-Making', 'venue': 'Trends in Cognitive Sciences', 'venue_type': 'journal', 'journal': 'Trends in Cognitive Sciences', 'volume': '24', 'issue': '8', 'pages': '639-653', 'doi': '10.1016/j.tics.2020.05.004', 'openalex_id': None, 'pmid': None, 'citation_string': 'Samaha, J., Iemi, L., Haegens, S., & Busch, N. A. (2020). Spontaneous brain oscillations and perceptual decision-making. *Trends in Cognitive Sciences*, 24(8), 639–653.', 'url': 'https://doi.org/10.1016/j.tics.2020.05.004', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Mashour, G. A., Roelfsema, P., Changeux, J., & Dehaene, S.', 'year': 2020, 'title': 'Conscious Processing and the Global Neuronal Workspace Hypothesis', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '105', 'issue': '5', 'pages': '776-798', 'doi': '10.1016/j.neuron.2020.01.026', 'openalex_id': None, 'pmid': None, 'citation_string': 'Mashour, G. A., Roelfsema, P., Changeux, J. P., & Dehaene, S. (2020). Conscious processing and the global neuronal workspace hypothesis. *Neuron*, 105(5), 776–798.', 'url': 'https://doi.org/10.1016/j.neuron.2020.01.026', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Dehaene, S., Lau, H., & Kouider, S.', 'year': 2017, 'title': 'What is consciousness, and could machines have it?', 'venue': 'Science', 'venue_type': 'journal', 'journal': 'Science', 'volume': '358', 'issue': '6362', 'pages': '486-492', 'doi': '10.1126/science.aan8871', 'openalex_id': None, 'pmid': None, 'citation_string': 'Dehaene, S., Lau, H., & Kouider, S. (2017). What is consciousness, and could machines have it? *Science*, 358(6362), 486–492.', 'url': 'https://doi.org/10.1126/science.aan8871', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Del Cul, A., Dehaene, S., Reyes, P., Bravo, E., & Slachevsky, A.', 'year': 2009, 'title': 'Causal role of prefrontal cortex in the threshold for access to consciousness', 'venue': 'Brain', 'venue_type': 'journal', 'journal': 'Brain', 'volume': '132', 'issue': '9', 'pages': '2531-2540', 'doi': '10.1093/brain/awp111', 'openalex_id': None, 'pmid': None, 'citation_string': 'Del Cul, A., Dehaene, S., Reyes, P., Bravo, E., & Slachevsky, A. (2009). Causal role of prefrontal cortex in the threshold for access to consciousness. *Brain*, 132(9), 2531–2540.', 'url': 'https://doi.org/10.1093/brain/awp111', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'King, J., Pescetelli, N., & Dehaene, S.', 'year': 2016, 'title': 'Brain Mechanisms Underlying the Brief Maintenance of Seen and Unseen Sensory Information', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '92', 'issue': '5', 'pages': '1122-1134', 'doi': '10.1016/j.neuron.2016.10.051', 'openalex_id': None, 'pmid': None, 'citation_string': 'King, J. R., Pescetelli, N., & Dehaene, S. (2016). Brain mechanisms underlying the brief maintenance of seen and unseen sensory information. *Neuron*, 92(5), 1122–1134.', 'url': 'https://doi.org/10.1016/j.neuron.2016.10.051', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [backward masking](https://www.cognitiveatlas.org/task/id/trm_4a3fd79d09b6d)
