(hedtsk_affective_picture_viewing)=
# Affective Picture Viewing Task

**HED task ID:** `hedtsk_affective_picture_viewing`

**Family:** [Emotion elicitation and regulation tasks](families/emotion.md)

**Also known as:** IAPS Viewing, Passive Viewing Task

Passive or instructed viewing of emotionally valenced images (IAPS, GAPED, NAPS, OASIS) while physiological, neural, or rating responses to valence and arousal are recorded.

## Description

Participants passively view color photographs from the International Affective Picture System (IAPS), a validated database of 1,182 images varying in emotional valence (pleasant, unpleasant, neutral) and arousal (calm to exciting). Images are presented for 3-5 seconds each without requiring an overt response. Post-viewing, participants rate valence and arousal on 9-point scales. The task serves as a standardized emotion elicitation tool in neuroimaging, consistently activating amygdala (for high-arousal images), visual cortex (enhanced processing of emotional stimuli), and prefrontal regions.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-experience-passively">Experience passively</a> (`experience_passively`)
- **Game rules:** every rule takes the default of the game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
  - Emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>, <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Color photographs from a validated set such as the International Affective Picture System, varying in emotional valence (pleasant, unpleasant, neutral) and arousal.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants view emotionally valenced images (e.g., IAPS) presented for several seconds each.
    2. Participants may rate valence and arousal or simply view while physiological signals are recorded.
* - **Manipulations**
  - - Emotional valence (positive, negative, neutral) and arousal level of the images
    - Viewing instructions (passive, reappraise, suppress)
    - Picture selection (single discrete emotion per block vs. mixed valence and arousal)
* - **Measurements**
  - - Subjective valence and arousal ratings (SAM)
    - Skin conductance
    - Startle reflex magnitude
    - Corrugator and zygomatic EMG
    - ERP components (LPP)
    - fMRI amygdala/PFC activation
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
* - Category-Specific Selection

    `hedvar_affective_picture_viewing__category_specific_selection`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - Pictures are chosen to evoke one discrete emotion at a time and shown in blocks of a single emotion instead of a mixed valence-by-arousal set.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation)

## Key references

- Sabatinelli, D., Bradley, M. M., Fitzsimmons, J. R., & Lang, P. J. (2005). Parallel amygdala and inferotemporal activation reflect emotional intensity and fear relevance. *NeuroImage*, 24(4), 1265-1270. ([DOI](https://doi.org/10.1016/j.neuroimage.2004.12.015), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15670706/))
- Phan, K. L., Wager, T., Taylor, S. F., & Liberzon, I. (2002). Functional neuroanatomy of emotion: A meta-analysis of emotion activation studies in PET and fMRI. *NeuroImage*, 16(2), 331-348. ([DOI](https://doi.org/10.1006/nimg.2002.1087), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12030820/))

## Further references

- Lindquist, K. A., Wager, T. D., Kober, H., Bliss-Moreau, E., & Barrett, L. F. (2012). The brain basis of emotion: A meta-analytic review. *Behavioral and Brain Sciences*, 35(3), 121-143. ([DOI](https://doi.org/10.1017/s0140525x11000446), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22617651/))
- Wager, T. D., Kang, J., Johnson, T. D., Nichols, T. E., Satpute, A. B., & Barrett, L. F. (2015). A Bayesian model of category-specific emotional brain responses. *PLoS Computational Biology*, 11(4), e1004066. ([DOI](https://doi.org/10.1371/journal.pcbi.1004066), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25853490/))

## External links

- Cognitive Atlas: [International Affective Picture System](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949aca) (close match)

- CogPO: [Subjective Emotional Picture Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Subjective_Emotional_Picture_Discrimination_Paradigm) (close match)

