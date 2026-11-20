(hedtsk_visual_masking)=
# Visual Masking Task

**HED task ID:** `hedtsk_visual_masking`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** Backward Masking, Metacontrast Masking, Pattern Masking

A brief target is rendered invisible or reduced in visibility by a preceding or following mask; variants include metacontrast, paracontrast, pattern, forward, backward, common-onset, and object-substitution masking.

## Description

Participants attempt to detect or discriminate brief, near-threshold visual stimuli that are rendered difficult to see through low contrast, brief duration, or metacontrast masking (a spatially adjacent, temporally trailing mask that suppresses visibility of the target without overlapping it spatially). The key dependent variable is not only accuracy but the relationship between trial-by-trial detection success and prestimulus brain states - particularly the phase and power of ongoing alpha (~10 Hz) and theta (~7 Hz) oscillations recorded via EEG. This paradigm demonstrates that conscious visual perception is not a passive, deterministic process but is gated by rhythmic fluctuations in cortical excitability, supporting pulsed-inhibition and perceptual-sampling theories.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What does the rule ask about each stimulus?** <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
- **What competes with the correct response?** <a href="vocabulary.html#rule-respond-to-rule-competitor-noise-or-mask">noise or mask</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-spatial-separation">spatial separation</a>, <a href="vocabulary.html#setting-stimulus-intensity">stimulus intensity</a>, <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** A brief, near-threshold target with a mask before or after it (metacontrast, pattern and other mask types).

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A brief target stimulus is rendered invisible or reduced in visibility by a temporally adjacent mask.
    2. Participants detect, identify, or discriminate the target.
* - **Manipulations**
  - - Mask type (metacontrast, pattern, backward, forward, common-onset, object-substitution, dichoptic suppression)
    - SOA/ISA between target and mask
    - Target-mask spatial relationship
    - Mask energy
    - Mask presence (no mask vs. masked target)
    - Stimulus origin (TMS-evoked vs. visual flash)
    - Preceding rhythmic flash train (target phase within the rhythm)
    - Masked prime for a visible target
* - **Measurements**
  - - Target detection/identification accuracy or d-prime as a function of SOA (U-shaped or monotonic masking functions)
    - Subjective visibility ratings
    - Priming effects from unseen targets
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
* - Phosphene Detection at Threshold

    `hedvar_visual_masking__phosphene_detection_at_threshold`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>; competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-none">none</a>
  - -
  - A faint flash at threshold on a plain background with no mask at all; the participant reports whether it was seen.
* - TMS-Evoked Phosphene Detection

    `hedvar_visual_masking__tms_evoked_phosphene_detection`
  - stimulus type: none; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-brain-stimulator">brain stimulator</a>; competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-none">none</a>
  - -
  - A magnetic pulse over the occipital cortex produces the spot of light, with no stimulus at the eye and no mask, and the participant reports whether it was seen.
* - Pattern Masking at Threshold

    `hedvar_visual_masking__pattern_masking_at_threshold`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-random-dots">random dots</a>, <a href="vocabulary.html#facet-stimulus-type-abstract-patterns">abstract patterns</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - -
  - The mask is a dense pattern covering the target's own location, presented just before or after it.
* - Continuous Flash Suppression Threshold

    `hedvar_visual_masking__continuous_flash_suppression_threshold`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-abstract-patterns">abstract patterns</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-stereoscopic-display">stereoscopic display</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - -
  - A flashing pattern to one eye suppresses a faint image to the other for seconds, and the participant reports when it breaks through or whether it was present.
* - Rhythmic Entrainment + Detection

    `hedvar_visual_masking__rhythmic_entrainment_detection`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-none">none</a>; cue: <a href="vocabulary.html#rule-respond-to-rule-cue-alerting-cue">alerting cue</a>
  - -
  - A regular train of flashes precedes a faint unmasked target and detection is measured against where the target falls in the rhythm; the train is coded as an alerting cue because it carries no information about the target.
* - Masked Priming Variant

    `hedvar_visual_masking__masked_priming_variant`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-classify">classify</a>; competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-preceding-prime">preceding prime</a>
  - -
  - The masked item is never reported but primes the response to a later visible target that is classified.
* - Backward Masking with Attentional Manipulation

    `hedvar_visual_masking__backward_masking_with_attentional_manipulation`
  - combined with: <a href="vocabulary.html#how-in-quick-succession">in quick succession</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (A second job draws attention away from the masked target)
  - [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
  - The masked target is embedded in a concurrent second task or a rapid stream so that attention is limited when it appears.
* - Auditory Backward Masking

    `hedvar_visual_masking__auditory_backward_masking`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>, <a href="vocabulary.html#facet-stimulus-type-noise">noise</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - A brief tone followed by a noise burst after a variable delay, presence reported.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Masking](../processes/awareness_agency_and_metacognition.md#hed-masking)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Perceptual awareness](../processes/awareness_agency_and_metacognition.md#hed-perceptual-awareness)
- [Attentional awareness](../processes/awareness_agency_and_metacognition.md#hed-attentional-awareness)

## Key references

- Mathewson, K. E., Gratton, G., Fabiani, M., Beck, D. M., & Ro, T. (2009). To see or not to see: Prestimulus alpha phase predicts visual awareness. *Journal of Neuroscience*, 29(9), 2725-2732. ([DOI](https://doi.org/10.1523/jneurosci.3963-08.2009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19261866/))
- Busch, N. A., Dubois, J., & VanRullen, R. (2009). The phase of ongoing EEG oscillations predicts visual perception. *Journal of Neuroscience*, 29(24), 7869-7876. ([DOI](https://doi.org/10.1523/jneurosci.0113-09.2009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19535598/))
- VanRullen, R., & Koch, C. (2003). Is perception discrete or continuous? *Trends in Cognitive Sciences*, 7(5), 207-213. ([DOI](https://doi.org/10.1016/s1364-6613(03)00095-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12757822/))
- Del Cul, A., Baillet, S., & Dehaene, S. (2007). Brain dynamics underlying the nonlinear threshold for access to consciousness. *PLoS Biology*, 5(10), e260. ([DOI](https://doi.org/10.1371/journal.pbio.0050260), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17896866/))
- Dehaene, S., & Changeux, J. P. (2011). Experimental and theoretical approaches to conscious processing. *Neuron*, 70(2), 200-227. ([DOI](https://doi.org/10.1016/j.neuron.2011.03.018), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21521609/))
- Sergent, C., & Dehaene, S. (2004). Is consciousness a gradual phenomenon? Evidence for an all-or-none bifurcation during the attentional blink. *Psychological Science*, 15(11), 720-728. ([DOI](https://doi.org/10.1111/j.0956-7976.2004.00748.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15482443/))

## Further references

- VanRullen, R. (2016). Perceptual cycles. *Trends in Cognitive Sciences*, 20(10), 723-735. ([DOI](https://doi.org/10.1016/j.tics.2016.07.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27567317/))
- Dugué, L., Marque, P., & VanRullen, R. (2011). The phase of ongoing oscillations mediates the causal relation between brain excitation and visual perception. *Journal of Neuroscience*, 31(33), 11889-11893. ([DOI](https://doi.org/10.1523/jneurosci.1161-11.2011), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21849549/))
- Iemi, L., Busch, N. A., Laudini, A., Haegens, S., Samaha, J., Villringer, A., & Nikulin, V. V. (2019). Multiple mechanisms link prestimulus neural oscillations to sensory responses. *eLife*, 8, e43620. ([DOI](https://doi.org/10.7554/elife.43620), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31188126/))
- Samaha, J., Iemi, L., Haegens, S., & Busch, N. A. (2020). Spontaneous brain oscillations and perceptual decision-making. *Trends in Cognitive Sciences*, 24(8), 639-653. ([DOI](https://doi.org/10.1016/j.tics.2020.05.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32513573/))
- Mashour, G. A., Roelfsema, P., Changeux, J. P., & Dehaene, S. (2020). Conscious processing and the global neuronal workspace hypothesis. *Neuron*, 105(5), 776-798. ([DOI](https://doi.org/10.1016/j.neuron.2020.01.026), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32135090/))
- Dehaene, S., Lau, H., & Kouider, S. (2017). What is consciousness, and could machines have it? *Science*, 358(6362), 486-492. ([DOI](https://doi.org/10.1126/science.aan8871), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29074769/))
- Del Cul, A., Dehaene, S., Reyes, P., Bravo, E., & Slachevsky, A. (2009). Causal role of prefrontal cortex in the threshold for access to consciousness. *Brain*, 132(9), 2531-2540. ([DOI](https://doi.org/10.1093/brain/awp111), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19433438/))
- King, J. R., Pescetelli, N., & Dehaene, S. (2016). Brain mechanisms underlying the brief maintenance of seen and unseen sensory information. *Neuron*, 92(5), 1122-1134. ([DOI](https://doi.org/10.1016/j.neuron.2016.10.051), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27930903/))

## External links

- Cognitive Atlas: [backward masking](https://www.cognitiveatlas.org/task/id/trm_4a3fd79d09b6d)

