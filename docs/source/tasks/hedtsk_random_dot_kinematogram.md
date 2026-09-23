(hedtsk_random_dot_kinematogram)=
# Random Dot Kinematogram Task

**HED task ID:** `hedtsk_random_dot_kinematogram`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** Dot Motion, Random Dot Kinematogram, RDK, Dot Motion Task

A field of moving dots in which a variable fraction move coherently; direction judgments and RT under varying coherence support drift-diffusion modeling of perceptual decisions.

## Description

The random dot kinematogram presents a field of moving dots in which a variable proportion move coherently in one direction while the remainder move randomly. Participants judge the direction of coherent motion, and the proportion of coherently moving dots parametrically controls task difficulty. This paradigm is the foundational tool for studying perceptual decision-making and has been central to establishing the neural basis of evidence accumulation, linking single-neuron recordings in area MT/V5 and LIP to drift-diffusion models of choice. It bridges sensory processing and decision-making in a way no other paradigm does as cleanly.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A field of moving dots is displayed.
    2. A proportion move coherently in one direction while the rest move randomly.
    3. Participants judge the direction of coherent motion.
* - **Manipulations**
  - - Coherence level (% coherent dots)
    - Speed-accuracy instructions
    - Number of alternatives
    - Reward asymmetry
* - **Measurements**
  - - Accuracy and RT as functions of coherence
    - Psychometric and chronometric functions
    - Drift rate and threshold parameters from diffusion model fits
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
* - Two-Alternative Forced Choice (Standard)

    `hedvar_random_dot_kinematogram__two_alternative_forced_choice_standard`
  - Leftward vs. rightward coherent motion; the canonical version used in monkey neurophysiology.
  - Canonical 2AFC motion direction discrimination
* - Free Response vs. Interrogation Protocol

    `hedvar_random_dot_kinematogram__free_response_vs_interrogation_protocol`
  - Participant-initiated response vs. experimenter-controlled viewing duration; separates speed-accuracy tradeoff from evidence quality.
  - Self-paced vs. fixed-duration decision; different temporal control
* - Pulse Paradigm

    `hedvar_random_dot_kinematogram__pulse_paradigm`
  - Brief motion pulses embedded in noise to measure the time course of evidence accumulation.
  - Brief coherence pulses instead of sustained motion; different stimulus structure
* - Multi-Alternative Motion Discrimination

    `hedvar_random_dot_kinematogram__multi_alternative_motion_discrimination`
  - Four or more possible directions; tests extensions of drift-diffusion to multi-choice scenarios.
  - More than two motion directions; higher-order discrimination
```

## Cognitive processes

This task is designed to engage the following processes:

- [Perceptual decision making](../processes/perceptual_decision_making_evidence_accumulation.md#hed-perceptual-decision-making)
- [Motion perception](../processes/face_and_object_perception.md#hed-motion-perception)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)

## Key references

- Britten, K. H., Shadlen, M. N., Newsome, W. T., & Movshon, J. A. (1992). The analysis of visual motion: A comparison of neuronal and psychophysical performance. *Journal of Neuroscience*, 12(12), 4745–4765. ([DOI](https://doi.org/10.1523/jneurosci.12-12-04745.1992), [PubMed](https://pubmed.ncbi.nlm.nih.gov/1464765/))
- Shadlen, M. N., & Newsome, W. T. (2001). Neural basis of a perceptual decision in the parietal cortex (area LIP) of the rhesus monkey. *Journal of Neurophysiology*, 86(4), 1916–1936. ([DOI](https://doi.org/10.1152/jn.2001.86.4.1916), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11600651/))
- Gold, J. I., & Shadlen, M. N. (2007). The neural basis of decision making. *Annual Review of Neuroscience*, 30, 535–574. ([DOI](https://doi.org/10.1146/annurev.neuro.29.051605.113038), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17600525/))

## Further references

- Ratcliff, R., Smith, P. L., Brown, S. D., & McKoon, G. (2016). Diffusion decision model: Current issues and history. *Trends in Cognitive Sciences*, 20(4), 260–281. ([DOI](https://doi.org/10.1016/j.tics.2016.01.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26952739/))
- Shooshtari, S. V., Sadrabadi, J. E., Azizi, Z., & Ebrahimpour, R. (2019). Confidence representation of perceptual decision by EEG and eye data in a random dot motion task. *Neuroscience*, 406, 510–527. ([DOI](https://doi.org/10.1016/j.neuroscience.2019.03.031), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30904664/))
- Steinemann, N. A., O'Connell, R. G., & Kelly, S. P. (2018). Decisions are expedited through multiple neural adjustments spanning the sensorimotor hierarchy. *Nature Communications*, 9, 3627. ([DOI](https://doi.org/10.1038/s41467-018-06117-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30194305/))
- Turner, B. M., van Maanen, L., Forstmann, B. U., & Brown, S. D. (2018). Approaches to analysis in model-based cognitive neuroscience. *Journal of Mathematical Psychology*, 76, 65–79. ([DOI](https://doi.org/10.1016/j.neubiorev.2018.04.011), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29660415/))

## External links

- Cognitive Atlas: [dot motion task](https://www.cognitiveatlas.org/task/id/trm_4f244ad7dcde7)

