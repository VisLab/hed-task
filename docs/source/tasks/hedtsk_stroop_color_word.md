(hedtsk_stroop_color_word)=
# Stroop Color-Word Task

**HED task ID:** `hedtsk_stroop_color_word`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Stroop, Color-Word Interference Test, CWIT

Naming the ink color of color words while ignoring word meaning; RT and error costs on incongruent trials index selective attention and conflict control.

## Description

The Stroop Color-Word Task is a classic measure of selective attention and cognitive control that requires participants to identify the ink color of printed words while ignoring the semantic content. In the standard version, participants view color names (e.g., "RED," "BLUE") printed in incongruent ink colors and must respond with the ink color rather than reading the word. The task measures reaction time and accuracy across congruent trials (word and color match), incongruent trials (word and color conflict), and neutral trials. Performance reflects the ability to overcome automatic word-reading processes and requires engagement of executive control mechanisms. The Stroop interference effect (slowed RT on incongruent trials) is one of the most robust findings in cognitive psychology.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What competes with the correct response?** <a href="vocabulary.html#rule-respond-to-rule-competitor-irrelevant-dimension">irrelevant dimension</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-words">words</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-proportion-congruent">proportion congruent</a>
- **Material:** Color words (RED, BLUE) printed in ink of a matching or a different color.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Color words (RED, BLUE) are printed in incongruent ink colors.
    2. Participants name the ink color while ignoring the word.
* - **Manipulations**
  - - Congruency (congruent, incongruent, neutral)
    - Proportion congruent
    - Response modality (vocal, manual)
    - Stimulus type (classic, spatial, numerical, face-word)
    - Task rule (name the ink color, read the word, count the words)
    - Object color (typical vs. atypical)
    - Prime type (neutral, matching, conflicting)
    - Trial sequence (ignored word becomes next trial's ink color)
* - **Measurements**
  - - Stroop interference effect (incongruent - congruent RT)
    - Facilitation (neutral - congruent)
    - Error rate
    - Conflict adaptation (Gratton effect)
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
* - Manual (Button-Press) Stroop

    `hedvar_stroop_color_word__manual_button_press_stroop`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - -
  - The ink color is reported by key press, one key per color, instead of aloud.
* - Counting Stroop

    `hedvar_stroop_color_word__counting_stroop`

    Cognitive Atlas: [counting Stroop task](https://www.cognitiveatlas.org/task/id/trm_4da631be60291)
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-count">count</a>
  - -
  - A number word is printed one to four times and the participant reports how many words there are while ignoring the number named.
* - Spatial Stroop

    `hedvar_stroop_color_word__spatial_stroop`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-symbols">symbols</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-localize">localize</a>
  - [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention)
  - A direction word or arrow appears at a screen position and the participant reports its position while ignoring its meaning; some versions instead report the meaning while ignoring the position.
* - Numerical Stroop

    `hedvar_stroop_color_word__numerical_stroop`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-compare">compare</a>
  - -
  - Two digits of different physical sizes are shown and the participant picks the numerically larger (ignoring size) or physically larger (ignoring value), a comparison between two simultaneous items.
* - Face-Word Stroop

    `hedvar_stroop_color_word__face_word_stroop`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>, <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition), [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
  - An emotion word is written across an expressive face and the participant names the expression while ignoring the word.
* - Color-Shape Stroop

    `hedvar_stroop_color_word__color_shape_stroop`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
  - -
  - Objects with a strongly associated color are shown in the wrong color and the participant names the displayed color while the known color interferes.
* - Priming Stroop

    `hedvar_stroop_color_word__priming_stroop`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-feature-cue">feature cue</a>
  - -
  - Each item is preceded by a prime that is neutral, matches or conflicts with it, giving advance feature information that may be valid or invalid.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict)
- [Reading](../processes/language_comprehension_and_production.md#hed-reading)

## Key references

- Stroop, J. R. (1935). Studies of interference in serial verbal reactions. *Journal of Experimental Psychology*, 18(6), 643-662. ([DOI](https://doi.org/10.1037/h0054651))
- MacLeod, C. M. (1991). Half a century of research on the Stroop effect: An integrative review. *Psychological Bulletin*, 109(2), 163-203. ([DOI](https://doi.org/10.1037/0033-2909.109.2.163), [PubMed](https://pubmed.ncbi.nlm.nih.gov/2034749/))
- Wager, T. D., Sylvester, C. Y. C., Lacey, S. C., Nee, D. E., Franklin, M., & Jonides, J. (2005). Common and unique components of response inhibition revealed by fMRI. *NeuroImage*, 27(3), 323-337. ([DOI](https://doi.org/10.1016/j.neuroimage.2005.01.054), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16019232/))

## Further references

- Egetemeyer, J., Rehme, A. K., Liebhaber, N., Eickhoff, S. B., & Grefkes, C. (2024). Not all Stroop-type tasks are alike: Assessing the impact of stimulus material, task design, and cognitive demand via meta-analyses across neuroimaging studies. *Neuropsychology Review*, 34, 687-714. ([DOI](https://doi.org/10.1007/s11065-024-09647-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/39264479/))
- Servant, M., Montagnini, A., & Burle, B. (2014). Conflict tasks and the diffusion framework: Insight in model constraints based on psychological laws. *Cognitive Psychology*, 72, 162-195. ([DOI](https://doi.org/10.1016/j.cogpsych.2014.03.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24762975/))
- Algom, D., & Chajut, E. (2019). Reclaiming the Stroop effect back from control to input-driven attention and perception. *Frontiers in Psychology*, 10, 1683. ([DOI](https://doi.org/10.3389/fpsyg.2019.01683), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31428008/))
- Neumann, J., Lohmann, G., Derrfuss, J., & von Cramon, D. Y. (2005). Meta-analysis of functional imaging data using replicator dynamics. *Human Brain Mapping*, 25(1), 165-173. [Stroop neuroimaging meta-analysis] ([DOI](https://doi.org/10.1002/hbm.20133), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15846812/))

## External links

- Cognitive Atlas: [color-word stroop task](https://www.cognitiveatlas.org/task/id/trm_4b1968619b00b)

- CogPO: [Stroop Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Stroop_Task_Paradigm)

