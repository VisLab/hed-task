(hedtsk_stroop_color_word)=
# Stroop Color-Word Task

**HED task ID:** `hedtsk_stroop_color_word`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Stroop, Color-Word Interference Test, CWIT

Naming the ink color of color words while ignoring word meaning; RT and error costs on incongruent trials index selective attention and conflict control.

## Description

The Stroop Color-Word Task is a classic measure of selective attention and cognitive control that requires participants to identify the ink color of printed words while ignoring the semantic content. In the standard version, participants view color names (e.g., "RED," "BLUE") printed in incongruent ink colors and must respond with the ink color rather than reading the word. The task measures reaction time and accuracy across congruent trials (word and color match), incongruent trials (word and color conflict), and neutral trials. Performance reflects the ability to overcome automatic word-reading processes and requires engagement of executive control mechanisms. The Stroop interference effect (slowed RT on incongruent trials) is one of the most robust findings in cognitive psychology.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Color words (RED, BLUE) are printed in incongruent ink colors; participants name the ink color while ignoring the word.
* - **Manipulation**
  - Congruency (congruent, incongruent, neutral); proportion congruent; response modality (vocal, manual); stimulus type (classic, spatial, numerical).
* - **Measurement**
  - Stroop interference effect (incongruent − congruent RT); facilitation (neutral − congruent); error rate; conflict adaptation (Gratton effect).
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
* - Classic Color-Word Stroop

    `hedvar_stroop_color_word__classic_color_word_stroop`
  - Name ink color of incongruent color words; the canonical interference paradigm.
  - Canonical color naming of congruent/incongruent color words
* - Manual (Button-Press) Stroop

    `hedvar_stroop_color_word__manual_button_press_stroop`
  - Responses via key press rather than vocal naming; preferred in neuroimaging to reduce motion artifacts.
  - Button press instead of vocal response; different response modality
* - Vocal Response Stroop

    `hedvar_stroop_color_word__vocal_response_stroop`
  - Original format with spoken color-naming responses; produces larger interference due to response-channel overlap with word reading.
  - Vocal naming; distinct from manual version
* - Counting Stroop

    `hedvar_stroop_color_word__counting_stroop`
  - Count the number of items displayed while ignoring the number word printed; used extensively in fMRI.
  - Count number of words instead of naming color; different task dimension
* - Spatial Stroop

    `hedvar_stroop_color_word__spatial_stroop`
  - Conflict between stimulus location and directional word content (e.g., "LEFT" on right side).
  - Spatial word/location conflict; different conflict dimension
* - Numerical Stroop

    `hedvar_stroop_color_word__numerical_stroop`
  - Conflict between numerical magnitude and physical size of digits.
  - Number magnitude vs. physical size conflict; different domain
* - Reverse Stroop

    `hedvar_stroop_color_word__reverse_stroop`
  - Read the word while ignoring ink color; reverses the typical control demand.
  - Name the word rather than the color; reversed task demand
* - Proportion-Congruent Manipulation

    `hedvar_stroop_color_word__proportion_congruent_manipulation`
  - Varying the ratio of congruent-to-incongruent trials to study context-driven control adjustments.
  - Conflict frequency variation; adaptation context per §5.2
* - Face-Word Stroop

    `hedvar_stroop_color_word__face_word_stroop`
  - Emotional face images paired with congruent/incongruent emotion labels.
  - Face emotion vs. color word conflict; different stimulus domain
* - Color-Shape Stroop

    `hedvar_stroop_color_word__color_shape_stroop`
  - Shapes printed in colors that conflict with shape-color associations (e.g., a blue banana).
  - Color word/shape conflict instead of ink color; different conflict structure
* - Priming Stroop

    `hedvar_stroop_color_word__priming_stroop`
  - Preceded by neutral, congruent, or incongruent primes to study anticipatory control.
  - Prime precedes Stroop item; temporal context manipulation
* - Negative Priming Stroop

    `hedvar_stroop_color_word__negative_priming_stroop`
  - Measures inhibitory aftereffects when a previously ignored color word becomes the target on the next trial.
  - Previously ignored item becomes target; tests ignored repetition effect
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

- Stroop, J. R. (1935). Studies of interference in serial verbal reactions. *Journal of Experimental Psychology*, 18(6), 643-662.
- MacLeod, C. M. (1991). Half a century of research on the Stroop effect: An integrative review. *Psychological Bulletin*, 109(2), 163-203.
- Wager, T. D., Sylvester, C. Y. C., Lacey, S. C., Nee, D. E., Franklin, M., & Jonides, J. (2005). Common and unique components of response inhibition revealed by fMRI. *NeuroImage*, 27(3), 323-337.

## Recent references

- Egetemeyer, J., Rehme, A. K., Liebhaber, N., Eickhoff, S. B., & Grefkes, C. (2024). Not all Stroop-type tasks are alike: Assessing the impact of stimulus material, task design, and cognitive demand via meta-analyses across neuroimaging studies. *Neuropsychology Review*, 34, 687–714.
- Servant, M., Montagnini, A., & Burle, B. (2014). Conflict tasks and the diffusion framework: Insight in model constraints based on psychological laws. *Cognitive Psychology*, 72, 162–195.
- Algom, D., & Chajut, E. (2019). Reclaiming the Stroop effect back from control to input-driven attention and perception. *Frontiers in Psychology*, 10, 1683.
- Neumann, J., Lohmann, G., Derrfuss, J., & von Cramon, D. Y. (2005). Meta-analysis of functional imaging data using replicator dynamics. *Human Brain Mapping*, 25(1), 165–173. [Stroop neuroimaging meta-analysis]

## External links

- Cognitive Atlas: [color-word stroop task](https://www.cognitiveatlas.org/task/id/trm_4b1968619b00b)

