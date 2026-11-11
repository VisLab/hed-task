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
  - 1. Two stimuli (e.g., a threatening face and a neutral face) appear briefly on screen.
    2. One is replaced by a probe (dot or letter) that participants locate or classify.
* - **Manipulations**
  - - Stimulus valence (threat, positive, neutral)
    - Stimulus duration
    - Probe location (congruent with threat vs. incongruent)
* - **Measurements**
  - - RT difference between congruent and incongruent probe trials (attentional bias score)
    - Vigilance vs. avoidance patterns
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
  - Two faces appear side by side for about half a second, one emotional (usually threatening) and one neutral. They disappear and a small probe (a dot or arrow) appears where one of them was. The participant indicates the probe's location or identity as fast as possible. Faster responses to probes behind emotional faces indicate attention was drawn there.
  - Canonical: face pair followed by probe; measures attentional bias to faces
* - Word Dot-Probe

    `hedvar_dot_probe__word_dot_probe`
  - The pair consists of a threat-related word and a neutral word, one above the other or side by side, followed by the probe at one of the word locations.
  - Word stimuli instead of faces; different stimulus type
* - Pictorial Dot-Probe

    `hedvar_dot_probe__pictorial_dot_probe`
  - The pair consists of emotional and neutral photographs of scenes or objects, such as pictures from the International Affective Picture System, rather than faces or words.
  - Scene/object pictures; different stimulus class
* - Detection vs. Classification Probe

    `hedvar_dot_probe__detection_vs_classification_probe`
  - In the detection version the participant presses a single key as soon as the probe appears. In the classification version the probe has two possible forms (for example one or two dots, or an arrow pointing up or down) and the participant reports which it was.
  - Probe identity discrimination vs. simple detection; different response task
* - Subliminal/Masked Dot-Probe

    `hedvar_dot_probe__subliminal_masked_dot_probe`
  - The face or word pair is shown for only about 15 to 20 ms and immediately covered by a mask, so the participant cannot consciously see which side the emotional item was on, before the probe appears.
  - Primes below threshold; changes conscious awareness of cue
* - Positive Dot-Probe

    `hedvar_dot_probe__positive_dot_probe`
  - The emotional item in each pair is positive, such as a happy face or a pleasant picture, paired with a neutral item, to measure attention toward pleasant rather than threatening content.
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

