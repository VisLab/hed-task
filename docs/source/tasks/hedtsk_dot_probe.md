(hedtsk_dot_probe)=
# Dot-Probe Task

**HED task ID:** `hedtsk_dot_probe`

**Family:** [Attentional cueing and orienting tasks](families/attentional_cueing.md)

**Also known as:** Visual Probe Task, Attentional Probe

A pair of cues (often threat/neutral) is followed by a probe at one cue location; RT difference by cue type indexes attentional bias.

## Description

The Dot-Probe Task measures attentional bias toward or away from emotionally salient stimuli. On each trial, a pair of stimuli (e.g., one threatening face and one neutral face) appears briefly (typically 500 ms), followed by a probe (dot or arrow) at the location of one stimulus. Participants respond to the probe (detect or classify it). Attentional bias is inferred from faster responses to probes replacing the emotional stimulus (vigilance toward threat) versus slower responses (avoidance). The task is a cornerstone of research on anxiety-related attentional biases and has been central to Attentional Bias Modification (ABM) treatments.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-localize">localize</a>
  - *Does a cue come before the target?* <a href="vocabulary.html#rule-respond-to-rule-cue-location-cue">location cue</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>
  - Emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>
- **Material:** Pairs of stimuli, typically a threatening and a neutral face (threat, positive or neutral), followed by a dot or arrow probe at the location of one of them.
- **Combined with:** <a href="vocabulary.html#how-throughout">throughout</a>, [Fixate Task](hedtsk_fixate.md) (Gaze is held on the fixation target while the main game is played)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Two stimuli (e.g., a threatening face and a neutral face) appear briefly on screen.
    2. One is replaced by a probe (dot or letter) that participants locate or classify.
* - **Manipulations**
  - - Stimulus valence (threat, positive, neutral)
    - Stimulus duration
    - Probe location (congruent with threat vs. incongruent)
    - Stimulus type (faces, words, scenes or objects)
* - **Measurements**
  - - RT difference between congruent and incongruent probe trials (attentional bias score)
    - Vigilance vs. avoidance patterns
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
* - Word Dot-Probe

    `hedvar_dot_probe__word_dot_probe`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>; social aspect: none
  - -
  - A threat word and a neutral word form the pair instead of faces.
* - Pictorial Dot-Probe

    `hedvar_dot_probe__pictorial_dot_probe`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>; social aspect: none
  - -
  - Emotional and neutral photographs of scenes or objects form the pair instead of faces or words.
* - Detection vs. Classification Probe

    `hedvar_dot_probe__detection_vs_classification_probe`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
  - -
  - The probe job is either a single press when the probe appears (detect) or a report of which of two probe forms appeared (classify), replacing the standard localization.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
- [Orienting](../processes/selective_and_sustained_attention.md#hed-orienting)

## Key references

- MacLeod, C., Mathews, A., & Tata, P. (1986). Attentional bias in emotional disorders. *Journal of Abnormal Psychology*, 95(1), 15-20. ([DOI](https://doi.org/10.1037/0021-843x.95.1.15))
- Mogg, K., & Bradley, B. P. (1998). A cognitive-motivational analysis of anxiety. *Behaviour Research and Therapy*, 36(9), 809-848. ([DOI](https://doi.org/10.1016/s0005-7967(98)00063-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9701859/))
- Bar-Haim, Y., Lamy, D., Pergamin, L., Bakermans-Kranenburg, M. J., & van IJzendoorn, M. H. (2007). Threat-related attentional bias in anxious and nonanxious individuals: A meta-analytic study. *Psychological Bulletin*, 133(1), 1-24. ([DOI](https://doi.org/10.1037/0033-2909.133.1.1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17201568/))

## Further references

- Kruijt, A.-W., Parsons, S., & Fox, E. (2019). A meta-analysis of bias at baseline in RCTs of attention bias modification: No evidence for dot-probe bias towards threat in clinical anxiety and PTSD. *Journal of Abnormal Psychology*, 128(6), 563-573. ([DOI](https://doi.org/10.1037/abn0000406), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31368735/))
- Price, R. B., Kuckertz, J. M., Siegle, G. J., Ladouceur, C. D., Silk, J. S., Ryan, N. D., ... & Amir, N. (2015). Empirical recommendations for improving the stability of the dot-probe task in clinical research. *Psychological Assessment*, 27(2), 365-376. ([DOI](https://doi.org/10.1037/pas0000036), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25419646/))
- Zvielli, A., Bernstein, A., & Koster, E. H. W. (2015). Temporal dynamics of attentional bias. *Clinical Psychological Science*, 3(5), 772-788. ([DOI](https://doi.org/10.1177/2167702614551572))
- Schmukle, S. C. (2005). Unreliability of the dot probe task. *European Journal of Personality*, 19(7), 595-605. ([DOI](https://doi.org/10.1002/per.554))

## External links

- Cognitive Atlas: [attention bias](https://www.cognitiveatlas.org/task/id/trm_50df0d8dc717b) (close match)

