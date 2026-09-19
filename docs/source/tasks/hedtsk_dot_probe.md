(hedtsk_dot_probe)=
# Dot-Probe Task

**HED task ID:** `hedtsk_dot_probe`

**Family:** [Attentional cueing and orienting tasks](families/attentional_cueing.md)

**Also known as:** Visual Probe Task, Attentional Probe

A pair of cues (often threat/neutral) is followed by a probe at one cue location; RT difference by cue type indexes attentional bias.

## Description

The Dot-Probe Task measures attentional bias toward or away from emotionally salient stimuli. On each trial, a pair of stimuli (e.g., one threatening face and one neutral face) appears briefly (typically 500 ms), followed by a probe (dot or arrow) at the location of one stimulus. Participants respond to the probe (detect or classify it). Attentional bias is inferred from faster responses to probes replacing the emotional stimulus (vigilance toward threat) versus slower responses (avoidance). The task is a cornerstone of research on anxiety-related attentional biases and has been central to Attentional Bias Modification (ABM) treatments.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Two stimuli (e.g., a threatening face and a neutral face) appear briefly on screen; one is replaced by a probe (dot or letter) that participants locate or classify.
* - **Manipulation**
  - Stimulus valence (threat, positive, neutral); stimulus duration; probe location (congruent with threat vs. incongruent).
* - **Measurement**
  - RT difference between congruent and incongruent probe trials (attentional bias score); vigilance vs. avoidance patterns.
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
* - Standard Face Dot-Probe

    `hedvar_dot_probe__standard_face_dot_probe`
  - Emotional vs. neutral face pairs; probe replaces one face.
  - Canonical: face pair followed by probe; measures attentional bias to faces
* - Word Dot-Probe

    `hedvar_dot_probe__word_dot_probe`
  - Threat vs. neutral words paired horizontally or vertically.
  - Word stimuli instead of faces; different stimulus type
* - Pictorial Dot-Probe

    `hedvar_dot_probe__pictorial_dot_probe`
  - IAPS images or photographs as stimuli.
  - Scene/object pictures; different stimulus class
* - Detection vs. Classification Probe

    `hedvar_dot_probe__detection_vs_classification_probe`
  - Simple probe detection vs. probe identity classification.
  - Probe identity discrimination vs. simple detection; different response task
* - Subliminal/Masked Dot-Probe

    `hedvar_dot_probe__subliminal_masked_dot_probe`
  - Brief stimulus presentation with backward masks; tests preconscious bias.
  - Primes below threshold; changes conscious awareness of cue
* - Positive Dot-Probe

    `hedvar_dot_probe__positive_dot_probe`
  - Happy vs. neutral faces; measures bias toward positive stimuli.
  - Positive stimuli as cues; different emotional valence of attention capture stimuli
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
- [Orienting](../processes/selective_and_sustained_attention.md#hed-orienting)

## Key references

- MacLeod, C., Mathews, A., & Tata, P. (1986). Attentional bias in emotional disorders. *Journal of Abnormal Psychology*, 95(1), 15–20. ([DOI](https://doi.org/10.1037/0021-843x.95.1.15))
- Mogg, K., & Bradley, B. P. (1998). A cognitive-motivational analysis of anxiety. *Behaviour Research and Therapy*, 36(9), 809–848. ([DOI](https://doi.org/10.1016/s0005-7967(98)00063-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9701859/))
- Bar-Haim, Y., Lamy, D., Pergamin, L., Bakermans-Kranenburg, M. J., & van IJzendoorn, M. H. (2007). Threat-related attentional bias in anxious and nonanxious individuals: A meta-analytic study. *Psychological Bulletin*, 133(1), 1–24. ([DOI](https://doi.org/10.1037/0033-2909.133.1.1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17201568/))

## Further references

- Kruijt, A.-W., Parsons, S., & Fox, E. (2019). A meta-analysis of bias at baseline in RCTs of attention bias modification: No evidence for dot-probe bias towards threat in clinical anxiety and PTSD. *Journal of Abnormal Psychology*, 128(6), 563–573. ([DOI](https://doi.org/10.1037/abn0000406), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31368735/))
- Price, R. B., Kuckertz, J. M., Siegle, G. J., Ladouceur, C. D., Silk, J. S., Ryan, N. D., ... & Amir, N. (2015). Empirical recommendations for improving the stability of the dot-probe task in clinical research. *Psychological Assessment*, 27(2), 365–376. ([DOI](https://doi.org/10.1037/pas0000036), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25419646/))
- Zvielli, A., Bernstein, A., & Koster, E. H. W. (2015). Temporal dynamics of attentional bias. *Clinical Psychological Science*, 3(5), 772–788. ([DOI](https://doi.org/10.1177/2167702614551572))
- Schmukle, S. C. (2005). Unreliability of the dot probe task. *European Journal of Personality*, 19(7), 595–605. ([DOI](https://doi.org/10.1002/per.554))

## External links

- Cognitive Atlas: [attention bias](https://www.cognitiveatlas.org/task/id/trm_50df0d8dc717b) (close match)

