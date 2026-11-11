(hedtsk_visual_masking)=
# Visual Masking Task

**HED task ID:** `hedtsk_visual_masking`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** Backward Masking, Metacontrast Masking, Pattern Masking

A brief target is rendered invisible or reduced in visibility by a preceding or following mask; variants include metacontrast, paracontrast, pattern, forward, backward, common-onset, and object-substitution masking.

## Description

Participants attempt to detect or discriminate brief, near-threshold visual stimuli that are rendered difficult to see through low contrast, brief duration, or metacontrast masking (a spatially adjacent, temporally trailing mask that suppresses visibility of the target without overlapping it spatially). The key dependent variable is not only accuracy but the relationship between trial-by-trial detection success and prestimulus brain states - particularly the phase and power of ongoing alpha (~10 Hz) and theta (~7 Hz) oscillations recorded via EEG. This paradigm demonstrates that conscious visual perception is not a passive, deterministic process but is gated by rhythmic fluctuations in cortical excitability, supporting pulsed-inhibition and perceptual-sampling theories.

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
  - - Mask type (metacontrast, pattern, backward, forward, common-onset, object-substitution)
    - SOA/ISA between target and mask
    - Target-mask spatial relationship
    - Mask energy
* - **Measurements**
  - - Target detection/identification accuracy or d-prime as a function of SOA (U-shaped or monotonic masking functions)
    - Subjective visibility ratings
    - Priming effects from unseen targets
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
* - Standard Metacontrast Masking

    `hedvar_visual_masking__standard_metacontrast_masking`
  - A small shape (such as a disk) is flashed briefly, and after a short delay a ring that surrounds but does not touch its location is flashed. At delays of around 50 to 100 ms the disk becomes hard or impossible to see. The participant reports whether the disk was present or which shape it was.
  - Canonical metacontrast: annular mask suppresses disc
* - Phosphene Detection at Threshold

    `hedvar_visual_masking__phosphene_detection_at_threshold`
  - A faint flash of light at the edge of visibility is presented on a plain background with no mask, and the participant reports whether they saw it. Used to study the moment-to-moment state of the visual system without any masking.
  - TMS-evoked phosphenes measured at perceptual threshold
* - TMS-Evoked Phosphene Detection

    `hedvar_visual_masking__tms_evoked_phosphene_detection`
  - A magnetic pulse applied to the back of the head produces a brief spot of light in the participant's vision, and they report whether they saw it. The pulse is timed relative to the phase of the participant's brain rhythms.
  - Visual cortex stimulation produces phosphene; different masking mechanism
* - Object Substitution Masking

    `hedvar_visual_masking__object_substitution_masking`
  - The target appears among other items surrounded by four small dots. If the dots remain on screen after the target and the other items have disappeared, the target is hard to report, even though the dots never touch it.
  - Four-dot surround mask replaces object representation; different mechanism
* - Pattern Masking at Threshold

    `hedvar_visual_masking__pattern_masking_at_threshold`
  - The mask is a dense pattern of lines, letters or random dots that covers the same location as the target, presented just before or after it. The target is reported at reduced visibility.
  - Pattern mask overlapping in space and time; different mask type
* - Continuous Flash Suppression Threshold

    `hedvar_visual_masking__continuous_flash_suppression_threshold`
  - A rapidly changing colorful pattern is shown to one eye while a faint image is shown to the other. The flashing pattern dominates and the image stays invisible for seconds. The participant reports when the image finally breaks through or whether it was present.
  - Monocular suppression by rapidly alternating masks; binocular suppression paradigm
* - Rhythmic Entrainment + Detection

    `hedvar_visual_masking__rhythmic_entrainment_detection`
  - A regular series of flashes at a chosen rate is shown before the faint target, and whether the target is detected is measured as a function of when it falls relative to the rhythm.
  - Rhythmic stimulation before target; tests oscillatory effects on detection
* - Masked Priming Variant

    `hedvar_visual_masking__masked_priming_variant`
  - The masked item is not reported at all. Instead it serves as a prime for a later visible target, and its effect on the response to that target shows that the masked item was processed.
  - Masked prime before target; tests subliminal priming via masking
* - Backward Masking with Attentional Manipulation

    `hedvar_visual_masking__backward_masking_with_attentional_manipulation`
  - The masked target is embedded in a situation where attention is limited, such as a second task or a rapid stream of items, to see how attention changes what the mask hides.
  - Attention directed during masking; tests attentional modulation of masking
* - Auditory Backward Masking

    `hedvar_visual_masking__auditory_backward_masking`
  - A brief tone is followed by a burst of noise after a variable delay, and the participant reports whether the tone was heard. The sound version of the masking task.
  - Auditory masking paradigm; different sensory modality
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

