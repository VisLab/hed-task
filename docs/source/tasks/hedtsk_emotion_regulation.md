(hedtsk_emotion_regulation)=
# Emotion Regulation Task

**HED task ID:** `hedtsk_emotion_regulation`

**Family:** [Emotion elicitation and regulation tasks](families/emotion.md)

**Also known as:** Cognitive Reappraisal Task, ER Task

View affective images under instructions to reappraise or passively view; self-reported affect, physiological responses, and neural activity index emotion regulation ability.

## Description

Participants view emotionally evocative stimuli (typically IAPS images) and are instructed to either passively view them ("look" condition) or regulate their emotional response using cognitive reappraisal (e.g., reinterpreting a car accident as a movie scene). After each trial, participants rate their emotional experience. Reappraisal successfully reduces subjective negative affect and modulates neural activity: it increases dorsolateral and ventrolateral PFC activation while decreasing amygdala activation, demonstrating top-down prefrontal regulation of emotion generation systems.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-undergo-stream">undergo stream</a>
- **What is the player told to do while it runs?** <a href="vocabulary.html#rule-undergo-stream-instruction-regulate">regulate</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
- **Emotional aspect:** <a href="vocabulary.html#facet-emotional-aspect-regulation-instruction">regulation instruction</a>, <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>, <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Emotionally evocative photographs, typically from the IAPS, of negative or positive valence.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants view emotionally evocative images and are instructed to regulate their emotional response using a specified strategy (e.g., cognitive reappraisal, suppression, or distraction) or to simply attend.
* - **Manipulations**
  - - Regulation strategy (reappraise, distance, suppress, distract, accept, attend)
    - Image valence (negative, positive)
    - Regulation timing (before vs. during viewing)
    - Exposure control (choice or early termination vs. assigned exposure)
    - Regulation instruction (none vs. explicit)
* - **Measurements**
  - - Self-reported affect (valence, arousal)
    - Physiological responses (SCR, corrugator EMG, startle)
    - fMRI prefrontal-amygdala modulation
    - ERP (LPP reduction)
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
* - Distraction/Attentional Deployment

    `hedvar_emotion_regulation__distraction_attentional_deployment`
  - combined with: <a href="vocabulary.html#how-throughout">throughout</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (An arithmetic or letter task is done during viewing)
  - [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention)
  - A second task (mental arithmetic or letter memory) runs while the picture is on screen, so regulation works through the competing task rather than an instruction about the picture.
* - Expressive Suppression

    `hedvar_emotion_regulation__expressive_suppression`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>
  - -
  - The instruction is to keep face and body still while viewing a picture or film clip.
* - Situation Selection/Modification

    `hedvar_emotion_regulation__situation_selection_modification`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>
  - -
  - The participant chooses which picture or clip to be exposed to or ends a clip early, so regulation happens through choice over exposure rather than through a stance toward a stimulus already present.
* - Up-Regulation

    `hedvar_emotion_regulation__up_regulation`
  - named form
  - -
  - The participant is told to make the feeling stronger rather than weaker.
* - Implicit Emotion Regulation

    `hedvar_emotion_regulation__implicit_emotion_regulation`
  - emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>, <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>; instruction: <a href="vocabulary.html#rule-undergo-stream-instruction-none">none</a>
  - -
  - No regulation instruction is given; regulation is inferred from responses after a self-control prime or from spontaneous recovery.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation)
- [Cognitive reappraisal](../processes/emotion_perception_and_regulation.md#hed-cognitive-reappraisal)
- [Expressive suppression](../processes/emotion_perception_and_regulation.md#hed-expressive-suppression)
- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Executive attention](../processes/inhibitory_control_and_conflict_monitoring.md#hed-executive-attention)

## Key references

- Gross, J. J. (1998). The emerging field of emotion regulation: An integrative review. *Review of General Psychology*, 2(3), 271-299. ([DOI](https://doi.org/10.1037/1089-2680.2.3.271))
- Ochsner, K. N., Bunge, S. A., Gross, J. J., & Gabrieli, J. D. E. (2002). Rethinking feelings: An fMRI study of the cognitive regulation of emotion. *Journal of Cognitive Neuroscience*, 14(8), 1215-1229. ([DOI](https://doi.org/10.1162/089892902760807212), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12495527/))
- Ochsner, K. N., Silvers, J. A., & Buhle, J. T. (2012). Functional imaging studies of emotion regulation: A synthetic review and evolving model of the cognitive control of emotion. *Annals of the New York Academy of Sciences*, 1251, E1-E24. ([DOI](https://doi.org/10.1111/j.1749-6632.2012.06751.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23025352/))

## Further references

- Buhle, J. T., Silvers, J. A., Wager, T. D., et al. (2014). Cognitive reappraisal of emotion: A meta-analysis of human neuroimaging studies. *Cerebral Cortex*, 24(11), 2981-2990. ([DOI](https://doi.org/10.1093/cercor/bht154))
- Kohn, N., Eickhoff, S. B., Scheller, M., Laird, A. R., Fox, P. T., & Habel, U. (2014). Neural network of cognitive emotion regulation: An ALE meta-analysis and MACM analysis. *NeuroImage*, 87, 345-355. ([DOI](https://doi.org/10.1016/j.neuroimage.2013.11.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24220041/))
- Dörfel, D., Lamke, J. P., Hummel, F., Wagner, U., Ott, S., & Sammer, G. (2014). Common and differential neural networks of emotion regulation by detachment, reinterpretation, distraction, and expressive suppression. *NeuroImage*, 101, 298-309. ([DOI](https://doi.org/10.1016/j.neuroimage.2014.06.051), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24993897/))
- Morawetz, C., Bode, S., Derntl, B., & Heekeren, H. R. (2017). The effect of strategies, goals and stimulus material on the neural mechanisms of emotion regulation: A meta-analysis of fMRI studies. *Neuroscience & Biobehavioral Reviews*, 72, 111-128. ([DOI](https://doi.org/10.1016/j.neubiorev.2016.11.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27894828/))

## External links

- Cognitive Atlas: [Emotion Regulation Task](https://www.cognitiveatlas.org/task/id/trm_56bbea82c12bb)

