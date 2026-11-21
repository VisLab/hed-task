(hedtsk_random_dot_kinematogram)=
# Random Dot Kinematogram Task

**HED task ID:** `hedtsk_random_dot_kinematogram`

**Family:** [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md)

**Also known as:** Dot Motion, Random Dot Kinematogram, RDK, Dot Motion Task

A field of moving dots in which a variable fraction move coherently; direction judgments and RT under varying coherence support drift-diffusion modeling of perceptual decisions.

## Description

The random dot kinematogram presents a field of moving dots in which a variable proportion move coherently in one direction while the remainder move randomly. Participants judge the direction of coherent motion, and the proportion of coherently moving dots parametrically controls task difficulty. This paradigm is the foundational tool for studying perceptual decision-making and has been central to establishing the neural basis of evidence accumulation, linking single-neuron recordings in area MT/V5 and LIP to drift-diffusion models of choice. It bridges sensory processing and decision-making in a way no other paradigm does as cleanly.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-noise-or-mask">noise or mask</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-random-dots">random dots</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-alternatives">number of alternatives</a>, <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>, <a href="vocabulary.html#setting-stimulus-intensity">stimulus intensity</a>
- **Material:** A field of moving dots, a variable proportion moving coherently in one direction and the rest randomly.
- **Combined with:** <a href="vocabulary.html#how-throughout">throughout</a>, [Fixate Task](hedtsk_fixate.md) (Gaze is held on the fixation target while the main game is played)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A field of moving dots is displayed.
    2. a proportion move coherently in one direction while the rest move randomly.
    3. Participants judge the direction of coherent motion.
* - **Manipulations**
  - - Coherence level (% coherent dots)
    - Speed-accuracy instructions
    - Number of alternatives
    - Reward asymmetry
    - Stimulus duration (free response vs. fixed-duration interrogation)
* - **Measurements**
  - - Accuracy and RT as functions of coherence
    - Psychometric and chronometric functions
    - Drift rate and threshold parameters from diffusion model fits
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
* - Pulse Paradigm

    `hedvar_random_dot_kinematogram__pulse_paradigm`
  - named form
  - -
  - The display stays at zero or low coherence and a brief 100 ms burst of coherent motion is inserted at a chosen moment.
* - Multi-Alternative Motion Discrimination

    `hedvar_random_dot_kinematogram__multi_alternative_motion_discrimination`

    Cognitive Atlas: [motion discrimination task](https://www.cognitiveatlas.org/task/id/trm_553fc63a54ae6) (close match)
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-eye-tracker">eye tracker</a>
  - -
  - The coherent motion can be in one of four or more directions and the participant indicates which, often with an eye movement.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Perceptual decision making](../processes/perceptual_decision_making_evidence_accumulation.md#hed-perceptual-decision-making)
- [Motion perception](../processes/face_and_object_perception.md#hed-motion-perception)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)

## Key references

- Britten, K. H., Shadlen, M. N., Newsome, W. T., & Movshon, J. A. (1992). The analysis of visual motion: A comparison of neuronal and psychophysical performance. *Journal of Neuroscience*, 12(12), 4745-4765. ([DOI](https://doi.org/10.1523/jneurosci.12-12-04745.1992), [PubMed](https://pubmed.ncbi.nlm.nih.gov/1464765/))
- Shadlen, M. N., & Newsome, W. T. (2001). Neural basis of a perceptual decision in the parietal cortex (area LIP) of the rhesus monkey. *Journal of Neurophysiology*, 86(4), 1916-1936. ([DOI](https://doi.org/10.1152/jn.2001.86.4.1916), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11600651/))
- Gold, J. I., & Shadlen, M. N. (2007). The neural basis of decision making. *Annual Review of Neuroscience*, 30, 535-574. ([DOI](https://doi.org/10.1146/annurev.neuro.29.051605.113038), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17600525/))

## Further references

- Ratcliff, R., Smith, P. L., Brown, S. D., & McKoon, G. (2016). Diffusion decision model: Current issues and history. *Trends in Cognitive Sciences*, 20(4), 260-281. ([DOI](https://doi.org/10.1016/j.tics.2016.01.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26952739/))
- Shooshtari, S. V., Sadrabadi, J. E., Azizi, Z., & Ebrahimpour, R. (2019). Confidence representation of perceptual decision by EEG and eye data in a random dot motion task. *Neuroscience*, 406, 510-527. ([DOI](https://doi.org/10.1016/j.neuroscience.2019.03.031), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30904664/))
- Steinemann, N. A., O'Connell, R. G., & Kelly, S. P. (2018). Decisions are expedited through multiple neural adjustments spanning the sensorimotor hierarchy. *Nature Communications*, 9, 3627. ([DOI](https://doi.org/10.1038/s41467-018-06117-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30194305/))
- Turner, B. M., van Maanen, L., Forstmann, B. U., & Brown, S. D. (2018). Approaches to analysis in model-based cognitive neuroscience. *Journal of Mathematical Psychology*, 76, 65-79. ([DOI](https://doi.org/10.1016/j.neubiorev.2018.04.011), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29660415/))

## External links

- Cognitive Atlas: [dot motion task](https://www.cognitiveatlas.org/task/id/trm_4f244ad7dcde7)

