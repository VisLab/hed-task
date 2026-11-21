(hedtsk_emotional_stroop)=
# Emotional Stroop Task

**HED task ID:** `hedtsk_emotional_stroop`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Affective Stroop

Color-naming of emotionally valenced words; RT slowing on threat-related words indexes attentional bias to affective content.

## Description

A variant of the classic Stroop in which participants name the ink color of words that vary in emotional valence (threat-related, positive, neutral). Emotional interference is measured as the slowing of color naming for emotional relative to neutral words, indexing the degree to which emotional content captures attentional resources. The task is widely used in anxiety and PTSD research, where threat-related words produce disproportionate interference. The emotional interference effect reflects automatic processing of affectively significant information.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-irrelevant-dimension">irrelevant dimension</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Emotionally valenced or threat-related words (disorder-specific, general threat or neutral) printed in colored ink.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Color words are replaced by emotionally valenced or threat-related words.
    2. Participants name the ink color while ignoring word meaning.
* - **Manipulations**
  - - Word valence/threat relevance (disorder-specific, general threat, positive, neutral)
    - Blocked vs. mixed presentation
    - Stimulus type (words, pictures, face-word compounds)
    - Awareness of the emotional word (subliminal masked prime vs. visible)
* - **Measurements**
  - - RT slowing for threat/emotional words relative to neutral (emotional Stroop interference)
    - Accuracy
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
* - Disorder-Specific Variants

    `hedvar_emotional_stroop__disorder_specific_variants`
  - population: <a href="vocabulary.html#facet-population-patients">patients</a>
  - -
  - The emotional word set is matched to the clinical concern of a patient group; the color-naming procedure is unchanged.
* - Pictorial Emotional Stroop

    `hedvar_emotional_stroop__pictorial_emotional_stroop`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
  - -
  - Emotional and neutral pictures carry a colored border or tint and the participant names that color while ignoring the picture.
* - Subliminal Emotional Stroop

    `hedvar_emotional_stroop__subliminal_emotional_stroop`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-preceding-prime">preceding prime</a>
  - -
  - The word is flashed below awareness and then covered by a colored mask whose color is named, so the emotional word acts as a masked prime before the judged item rather than as part of it.
* - Face-Word Emotional Stroop

    `hedvar_emotional_stroop__face_word_emotional_stroop`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>, <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - -
  - An emotion word is written across an expressive face and the participant names the expression while ignoring the word (or the reverse), so the competitor is now response-mapped as in the color-word Stroop.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)

## Key references

- Williams, J. M. G., Mathews, A., & MacLeod, C. (1996). The emotional Stroop task and psychopathology. *Psychological Bulletin*, 120(1), 3-24. ([DOI](https://doi.org/10.1037/0033-2909.120.1.3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8711015/))
- Compton, R. J., Banich, M. T., Mohanty, A., et al. (2003). Paying attention to emotion: An fMRI investigation of cognitive and emotional Stroop tasks. *Cognitive, Affective, & Behavioral Neuroscience*, 3(2), 81-96. ([DOI](https://doi.org/10.3758/cabn.3.2.81), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12943324/))
- Etkin, A., Egner, T., Peraza, D. M., Kandel, E. R., & Hirsch, J. (2006). Resolving emotional conflict: A role for the rostral anterior cingulate cortex in modulating activity in the amygdala. *Neuron*, 51(6), 871-882. ([DOI](https://doi.org/10.1016/j.neuron.2006.07.029), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16982430/))

## Further references

- Phaf, R. H., & Kan, K. J. (2007). The automaticity of emotional Stroop: A meta-analysis. *Journal of Behavior Therapy and Experimental Psychiatry*, 38(2), 184-199. ([DOI](https://doi.org/10.1016/j.jbtep.2006.10.008), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17112461/))
- Cisler, J. M., & Koster, E. H. (2010). Mechanisms of attentional biases toward threat in anxiety disorders. *Clinical Psychology Review*, 30(2), 203-216. ([DOI](https://doi.org/10.1016/j.cpr.2009.11.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20005616/))
- Algom, D., Chajut, E., & Lev, S. (2004). A rational look at the emotional Stroop phenomenon: A generic slowdown, not a Stroop effect. *Journal of Experimental Psychology: General*, 133(3), 323-338. [Updated: Dalgleish, T. (2005). Putting some feeling into it - the conceptual and empirical relationships between the classic and emotional Stroop tasks: Comment on Algom et al. *Journal of Experimental Psychology: General*, 134(4), 585-591.] ([DOI](https://doi.org/10.1037/0096-3445.133.3.323), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15355142/))

## External links

- Cognitive Atlas: [Stroop task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949e27) (related match)

- CogPO: [Stroop Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Stroop_Task_Paradigm) (close match)

