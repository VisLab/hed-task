(hedtsk_emotional_stroop)=
# Emotional Stroop Task

**HED task ID:** `hedtsk_emotional_stroop`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Affective Stroop

Color-naming of emotionally valenced words; RT slowing on threat-related words indexes attentional bias to affective content.

## Description

A variant of the classic Stroop in which participants name the ink color of words that vary in emotional valence (threat-related, positive, neutral). Emotional interference is measured as the slowing of color naming for emotional relative to neutral words, indexing the degree to which emotional content captures attentional resources. The task is widely used in anxiety and PTSD research, where threat-related words produce disproportionate interference. The emotional interference effect reflects automatic processing of affectively significant information.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Color words are replaced by emotionally valenced or threat-related words; participants name the ink color while ignoring word meaning.
* - **Manipulation**
  - Word valence/threat relevance (disorder-specific, general threat, neutral); blocked vs. mixed presentation.
* - **Measurement**
  - RT slowing for threat/emotional words relative to neutral (emotional Stroop interference); accuracy.
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
* - Threat-Related Emotional Stroop

    `hedvar_emotional_stroop__threat_related_emotional_stroop`
  - Threat words (anxiety, death, danger) in different ink colors.
  - Threat words produce interference; canonical emotional Stroop design
* - Disorder-Specific Variants

    `hedvar_emotional_stroop__disorder_specific_variants`
  - Tailored word sets for PTSD (trauma words), depression (loss words), addiction (substance words), eating disorders (body words).
  - Stimulus set tailored to specific disorder (e.g., spider phobia words); different content domain
* - Positive vs. Negative Emotional Stroop

    `hedvar_emotional_stroop__positive_vs_negative_emotional_stroop`
  - Comparing interference from positive and negative words.
  - Positive stimuli alongside negative; tests valence symmetry of interference
* - Pictorial Emotional Stroop

    `hedvar_emotional_stroop__pictorial_emotional_stroop`
  - Emotional images rather than words with color overlays.
  - Emotional pictures instead of words; different stimulus modality
* - Subliminal Emotional Stroop

    `hedvar_emotional_stroop__subliminal_emotional_stroop`
  - Briefly masked emotional words to test unconscious processing.
  - Masked words below awareness; changes conscious access to emotional stimuli
* - Face-Word Emotional Stroop

    `hedvar_emotional_stroop__face_word_emotional_stroop`
  - Emotional faces with incongruent emotion labels.
  - Emotional faces paired with color words; cross-domain emotional conflict
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

- Phaf, R. H., & Kan, K. J. (2007). The automaticity of emotional Stroop: A meta-analysis. *Journal of Behavior Therapy and Experimental Psychiatry*, 38(2), 184–199. ([DOI](https://doi.org/10.1016/j.jbtep.2006.10.008), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17112461/))
- Cisler, J. M., & Koster, E. H. (2010). Mechanisms of attentional biases toward threat in anxiety disorders. *Clinical Psychology Review*, 30(2), 203–216. ([DOI](https://doi.org/10.1016/j.cpr.2009.11.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20005616/))
- Algom, D., Chajut, E., & Lev, S. (2004). A rational look at the emotional Stroop phenomenon: A generic slowdown, not a Stroop effect. *Journal of Experimental Psychology: General*, 133(3), 323–338. [Updated: Dalgleish, T. (2005). Putting some feeling into it—the conceptual and empirical relationships between the classic and emotional Stroop tasks: Comment on Algom et al. *Journal of Experimental Psychology: General*, 134(4), 585–591.] ([DOI](https://doi.org/10.1037/0096-3445.133.3.323), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15355142/))

## External links

- Cognitive Atlas: [Stroop task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949e27) (related match)

- CogPO: [Stroop Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Stroop_Task_Paradigm) (close match)

