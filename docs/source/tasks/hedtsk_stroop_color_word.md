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
  - 1. Color words (RED, BLUE) are printed in incongruent ink colors.
    2. Participants name the ink color while ignoring the word.
* - **Manipulations**
  - - Congruency (congruent, incongruent, neutral)
    - Proportion congruent
    - Response modality (vocal, manual)
    - Stimulus type (classic, spatial, numerical)
* - **Measurements**
  - - Stroop interference effect (incongruent − congruent RT)
    - Facilitation (neutral − congruent)
    - Error rate
    - Conflict adaptation (Gratton effect)
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
  - Color words are printed in colored ink, for example RED printed in blue, and the participant names the ink color while ignoring the word. Naming is slower and more error-prone when the word and the ink disagree than when they agree or the item is a neutral string.
  - Canonical color naming of congruent/incongruent color words
* - Manual (Button-Press) Stroop

    `hedvar_stroop_color_word__manual_button_press_stroop`
  - The participant presses one of several keys, one per ink color, instead of saying the color aloud. Common in brain imaging where speaking would cause head movement.
  - Button press instead of vocal response; different response modality
* - Vocal Response Stroop

    `hedvar_stroop_color_word__vocal_response_stroop`
  - The participant says the ink color aloud, as in the original task, and voice onset is recorded with a microphone. Interference is larger than with key presses because reading and color naming both use speech.
  - Vocal naming; distinct from manual version
* - Counting Stroop

    `hedvar_stroop_color_word__counting_stroop`
  - A number word is printed one to four times (for example 'two' printed three times) and the participant reports how many words there are, ignoring what the word says. Neutral items use animal names.
  - Count number of words instead of naming color; different task dimension
* - Spatial Stroop

    `hedvar_stroop_color_word__spatial_stroop`
  - A direction word (such as LEFT or ABOVE) or an arrow appears at a position on the screen, and the participant reports either the word's meaning or its position while ignoring the other.
  - Spatial word/location conflict; different conflict dimension
* - Numerical Stroop

    `hedvar_stroop_color_word__numerical_stroop`
  - Two digits are shown in different physical sizes, and the participant chooses the one that is numerically larger (ignoring size) or physically larger (ignoring value). Responses slow when the larger number is printed smaller.
  - Number magnitude vs. physical size conflict; different domain
* - Reverse Stroop

    `hedvar_stroop_color_word__reverse_stroop`
  - The participant reads the word and ignores the ink color. Interference from the ink is usually small, but it appears when the response is made by pointing to a color patch rather than speaking.
  - Name the word rather than the color; reversed task demand
* - Proportion-Congruent Manipulation

    `hedvar_stroop_color_word__proportion_congruent_manipulation`
  - The share of trials on which word and ink agree is varied between blocks or between particular words, for example mostly agreeing in one block and mostly conflicting in another. Interference is smaller when conflict is expected.
  - Conflict frequency variation; adaptation context per §5.2
* - Face-Word Stroop

    `hedvar_stroop_color_word__face_word_stroop`
  - A face with an emotional expression has an emotion word written across it. The participant names the expression while ignoring the word, and responses slow when the word names a different emotion.
  - Face emotion vs. color word conflict; different stimulus domain
* - Color-Shape Stroop

    `hedvar_stroop_color_word__color_shape_stroop`
  - Objects with a strongly associated color are shown in the wrong color, such as a blue banana, and the participant names the displayed color while the known color of the object interferes.
  - Color word/shape conflict instead of ink color; different conflict structure
* - Priming Stroop

    `hedvar_stroop_color_word__priming_stroop`
  - Each color-word item is preceded by a prime, such as a word or cue that is neutral, matches or conflicts with the coming item, to study how advance information changes the interference.
  - Prime precedes Stroop item; temporal context manipulation
* - Negative Priming Stroop

    `hedvar_stroop_color_word__negative_priming_stroop`
  - Trials are arranged so that the word to be ignored on one trial is the ink color to be named on the next (for example RED in green, then any word in red). Naming the previously ignored color is slower, which shows it was suppressed.
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

- Stroop, J. R. (1935). Studies of interference in serial verbal reactions. *Journal of Experimental Psychology*, 18(6), 643-662. ([DOI](https://doi.org/10.1037/h0054651))
- MacLeod, C. M. (1991). Half a century of research on the Stroop effect: An integrative review. *Psychological Bulletin*, 109(2), 163-203. ([DOI](https://doi.org/10.1037/0033-2909.109.2.163), [PubMed](https://pubmed.ncbi.nlm.nih.gov/2034749/))
- Wager, T. D., Sylvester, C. Y. C., Lacey, S. C., Nee, D. E., Franklin, M., & Jonides, J. (2005). Common and unique components of response inhibition revealed by fMRI. *NeuroImage*, 27(3), 323-337. ([DOI](https://doi.org/10.1016/j.neuroimage.2005.01.054), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16019232/))

## Further references

- Egetemeyer, J., Rehme, A. K., Liebhaber, N., Eickhoff, S. B., & Grefkes, C. (2024). Not all Stroop-type tasks are alike: Assessing the impact of stimulus material, task design, and cognitive demand via meta-analyses across neuroimaging studies. *Neuropsychology Review*, 34, 687–714. ([DOI](https://doi.org/10.1007/s11065-024-09647-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/39264479/))
- Servant, M., Montagnini, A., & Burle, B. (2014). Conflict tasks and the diffusion framework: Insight in model constraints based on psychological laws. *Cognitive Psychology*, 72, 162–195. ([DOI](https://doi.org/10.1016/j.cogpsych.2014.03.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24762975/))
- Algom, D., & Chajut, E. (2019). Reclaiming the Stroop effect back from control to input-driven attention and perception. *Frontiers in Psychology*, 10, 1683. ([DOI](https://doi.org/10.3389/fpsyg.2019.01683), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31428008/))
- Neumann, J., Lohmann, G., Derrfuss, J., & von Cramon, D. Y. (2005). Meta-analysis of functional imaging data using replicator dynamics. *Human Brain Mapping*, 25(1), 165–173. [Stroop neuroimaging meta-analysis] ([DOI](https://doi.org/10.1002/hbm.20133), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15846812/))

## External links

- Cognitive Atlas: [color-word stroop task](https://www.cognitiveatlas.org/task/id/trm_4b1968619b00b)

- CogPO: [Stroop Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Stroop_Task_Paradigm)

