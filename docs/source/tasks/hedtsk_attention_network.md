(hedtsk_attention_network)=
# Attention Network Task

**HED task ID:** `hedtsk_attention_network`

**Family:** [Attentional cueing and orienting tasks](families/attentional_cueing.md) (also [Conflict and interference tasks](families/conflict_and_interference.md))

**Also known as:** Attention Network Test, ANT, Clinical Screening ANT

Identify the direction of a central arrow flanked by congruent or incongruent arrows, preceded by various cue types; RT differences across cue and flanker conditions index three independent attention networks (alerting, orienting, executive).

## Description

The Attention Network Test (ANT) combines elements of the Posner cueing paradigm and the Eriksen flanker task to provide separate measures of three attention networks in a single task. Participants respond to the direction of a central arrow flanked by congruent or incongruent flankers, with the target preceded by no cue, a center cue, a double cue, or a spatial cue. The ANT yields three independent efficiency scores: alerting (double cue benefit over no cue), orienting (spatial cue benefit over center cue), and executive control (incongruent flanker cost). The task operationalizes Posner's attention network model.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What competes with the correct response?** <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
- **Does a cue come before the target?** <a href="vocabulary.html#rule-respond-to-rule-cue-location-cue">location cue</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-proportion-congruent">proportion congruent</a>, <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** A central arrow between flanking arrows that point the same or the opposite way, preceded by no cue, a center cue, a double cue or a spatial cue.
- **Combined with:** <a href="vocabulary.html#how-throughout">throughout</a>, [Fixate Task](hedtsk_fixate.md) (Gaze is held on the fixation target while the main game is played)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Flanker task with preceding spatial and temporal cues.
    2. Participants identify the direction of a central arrow flanked by congruent or incongruent arrows.
* - **Manipulations**
  - - Cue type (no cue, center cue, double cue, spatial cue)
    - Flanker congruency (congruent, incongruent)
    - Cue validity and cue-target interval (invalid spatial cues; varied interval)
    - Display position (lateralized left or right vs. above and below fixation)
    - Stimulus type (cartoon fish vs. arrows)
    - Emotional stimuli as cues or flankers
* - **Measurements**
  - - Alerting network score (double-cue minus no-cue RT)
    - Orienting network score (center-cue minus spatial-cue RT)
    - Executive network score (incongruent minus congruent RT)
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
* - ANT-I (Callejas et al.)

    `hedvar_attention_network__ant_i_callejas_et_al`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - The alerting cue becomes a tone and the location cue a separate visual cue, varied independently on every trial so the network effects can interact; the cue types are the same as the standard, only factorially crossed and partly auditory.
* - Child ANT

    `hedvar_attention_network__child_ant`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>; population: <a href="vocabulary.html#facet-population-children">children</a>
  - -
  - Cartoon fish replace the arrows, trials are slower, feedback is given and the task is framed as feeding the fish.
* - ANT with Emotional Stimuli

    `hedvar_attention_network__ant_with_emotional_stimuli`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
  - Emotional pictures or faces serve as cues or replace the neutral flankers; the task is unchanged.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Alerting](../processes/selective_and_sustained_attention.md#hed-alerting)
- [Orienting](../processes/selective_and_sustained_attention.md#hed-orienting)
- [Executive attention](../processes/inhibitory_control_and_conflict_monitoring.md#hed-executive-attention)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)

## Key references

- Fan, J., McCandliss, B. D., Sommer, T., Raz, A., & Posner, M. I. (2002). Testing the efficiency and independence of attentional networks. *Journal of Cognitive Neuroscience*, 14(3), 340-347. ([DOI](https://doi.org/10.1162/089892902317361886), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11970796/))
- Fan, J., McCandliss, B. D., Fossella, J., Flombaum, J. I., & Posner, M. I. (2005). The activation of attentional networks. *NeuroImage*, 26(2), 471-479. ([DOI](https://doi.org/10.1016/j.neuroimage.2005.02.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15907304/))
- Petersen, S. E., & Posner, M. I. (2012). The attention system of the human brain: 20 years after. *Annual Review of Neuroscience*, 35, 73-89. ([DOI](https://doi.org/10.1146/annurev-neuro-062111-150525), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22524787/))

## Further references

- MacLeod, J. W., Lawrence, M. A., McConnell, M. M., Eskes, G. A., Klein, R. M., & Shore, D. I. (2010). Appraising the ANT: Psychometric and theoretical considerations of the Attention Network Test. *Neuropsychology*, 24(5), 637-651. ([DOI](https://doi.org/10.1037/a0019803), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20804252/))
- Arora, S., Lawrence, M. A., & Klein, R. M. (2020). The Attention Network Test database: ADHD and cross-cultural applications. *Frontiers in Psychology*, 11, 388. ([DOI](https://doi.org/10.3389/fpsyg.2020.00388), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32292363/))
- Ishigami, Y., & Klein, R. M. (2010). Repeated measurement of the components of attention using two versions of the Attention Network Test (ANT): Stability, isolability, robustness, and reliability. *Journal of Neuroscience Methods*, 190(1), 117-128. ([DOI](https://doi.org/10.1016/j.jneumeth.2010.04.019), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20435062/))

## External links

- Cognitive Atlas: [attention networks test](https://www.cognitiveatlas.org/task/id/trm_4da6304c9aa23)

