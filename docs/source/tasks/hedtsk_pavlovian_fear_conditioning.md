(hedtsk_pavlovian_fear_conditioning)=
# Pavlovian Fear Conditioning Task

**HED task ID:** `hedtsk_pavlovian_fear_conditioning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Fear Conditioning, Classical Conditioning, FC

A neutral CS is paired with an aversive US (shock, loud sound); conditioned responses (SCR, startle, amygdala BOLD) index fear learning.

## Description

A neutral conditioned stimulus (CS; auditory tone or visual cue) is paired with an aversive unconditioned stimulus (US; mild shock, loud noise). After conditioning, the CS alone elicits conditioned fear responses including skin conductance increases, heart rate changes, freezing (in animals), and subjective fear ratings (in humans). Extinction is measured in a subsequent phase where the CS is presented without the US. The task is fundamental to understanding emotional learning and has been used extensively to study the amygdala's role in fear acquisition and the prefrontal cortex's role in extinction.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-experience-passively">Experience passively</a> (`experience_passively`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is the player told to do while it runs?* <a href="vocabulary.html#rule-experience-passively-instruction-none">none</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-unearned-outcome">unearned outcome</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-loss">loss</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-nothing">nothing</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-aversive">aversive</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>
- **Game phases:** <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-extinction">extinction</a>
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-somatic">somatic</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-electrical">electrical</a>, <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>
  - Emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotion-induction">emotion induction</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-reward-probability">reward probability</a>, <a href="vocabulary.html#setting-stimulus-onset-asynchrony">stimulus onset asynchrony</a>
- **Material:** A neutral visual cue or tone (CS+) paired with a mild shock or loud noise, and a second cue (CS-) that is never paired.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants view a neutral stimulus (CS+) paired with an aversive unconditioned stimulus (US, typically mild shock or loud noise).
    2. Another stimulus (CS-) is never paired.
    3. Acquisition is followed by extinction (CS+ presented without US).
    4. Optional: A day or more after extinction the extinguished CS is tested again without the US to measure retention of extinction.
    5. Optional: A single reactivation presentation of the CS a day after acquisition is followed by extinction within a window of minutes to hours.
    6. Optional: After acquisition to one CS, cues differing from it by graded amounts are tested and fear is plotted against similarity.
* - **Manipulations**
  - - CS+/CS- discrimination
    - Reinforcement schedule (partial vs. 100%)
    - Extinction timing
    - reinstatement/renewal context
    - CS-US interval (trace gap vs. delay)
    - Predictive cue (context as the CS vs. discrete cue)
    - Number of conditioned cues (compound CS vs. single CS)
* - **Measurements**
  - - Differential SCR (CS+ > CS-)
    - Startle potentiation
    - fMRI amygdala and vmPFC activation
    - Fear ratings
    - Extinction learning curve
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
* - Contextual Conditioning

    `hedvar_pavlovian_fear_conditioning__contextual_conditioning`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>, <a href="vocabulary.html#facet-stimulus-type-electrical">electrical</a>
  - -
  - No discrete cue predicts the US; it arrives at unpredictable times within one of two settings, so the setting itself becomes the CS.
* - Extinction Recall

    `hedvar_pavlovian_fear_conditioning__extinction_recall`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-extinction">extinction</a>, <a href="vocabulary.html#phase-test">test</a>
  - [Consolidation](../processes/long_term_memory.md#hed-consolidation)
  - A day or more after extinction the extinguished CS is tested again without the US to measure retention of extinction.
* - Renewal (Context Change)

    `hedvar_pavlovian_fear_conditioning__renewal_context_change`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-extinction">extinction</a>
  - -
  - Acquisition in one setting, extinction in another, and the CS tested back in the original or a new setting where fear returns.
* - Reinstatement

    `hedvar_pavlovian_fear_conditioning__reinstatement`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-extinction">extinction</a>
  - -
  - After extinction a few unsignalled USs are given and the CS is then tested, where fear returns.
* - Reconsolidation Paradigm

    `hedvar_pavlovian_fear_conditioning__reconsolidation_paradigm`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-extinction">extinction</a>, <a href="vocabulary.html#phase-test">test</a>
  - [Reconsolidation](../processes/long_term_memory.md#hed-reconsolidation)
  - A single reactivation presentation of the CS a day after acquisition is followed by extinction within a window of minutes to hours.
* - Generalization Gradient

    `hedvar_pavlovian_fear_conditioning__generalization_gradient`
  - phases: <a href="vocabulary.html#phase-acquisition">acquisition</a>, <a href="vocabulary.html#phase-test">test</a>
  - -
  - After acquisition to one CS, cues differing from it by graded amounts are tested and fear is plotted against similarity.
* - Instructed vs. Uninstructed

    `hedvar_pavlovian_fear_conditioning__instructed_vs_uninstructed`
  - named form
  - -
  - Some participants are told in advance which cue predicts the US, so the contingency is given verbally rather than learned by exposure.
* - Compound CS Conditioning

    `hedvar_pavlovian_fear_conditioning__compound_cs_conditioning`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>, <a href="vocabulary.html#facet-stimulus-modality-somatic">somatic</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>, <a href="vocabulary.html#facet-stimulus-type-electrical">electrical</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - Two cues (a light and a tone) are presented together before the US and later tested as elements and as a compound.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Pavlovian conditioning](../processes/associative_learning_and_reinforcement.md#hed-pavlovian-conditioning)
- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
- [Extinction](../processes/associative_learning_and_reinforcement.md#hed-extinction)
- [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation)
- [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation)

## Key references

- LeDoux, J. E. (2000). Emotion circuits in the brain. *Annual Review of Neuroscience*, 23, 155-184. ([DOI](https://doi.org/10.1146/annurev.neuro.23.1.155), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10845062/))
- Phelps, E. A., Delgado, M. R., Nearing, K. I., & LeDoux, J. E. (2004). Extinction learning in humans: Role of the amygdala and vmPFC. *Neuron*, 43(6), 897-905. ([DOI](https://doi.org/10.1016/j.neuron.2004.08.042), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15363399/))
- Quirk, G. J., & Mueller, D. (2008). Neural mechanisms of extinction learning and retrieval. *Neuropsychopharmacology*, 33(1), 56-72. ([DOI](https://doi.org/10.1038/sj.npp.1301555))

## Further references

- Fullana, M. A., Harrison, B. J., Soriano-Mas, C., et al. (2016). Neural signatures of human fear conditioning: An updated and extended meta-analysis of fMRI studies. *Molecular Psychiatry*, 21(4), 500-508. ([DOI](https://doi.org/10.1038/mp.2015.88))
- Lonsdorf, T. B., Menz, M. M., Andreatta, M., et al. (2017). Don't fear 'fear conditioning': Methodological considerations for the design and analysis of studies on human fear acquisition, extinction, and return of fear. *Neuroscience & Biobehavioral Reviews*, 77, 247-285. ([DOI](https://doi.org/10.1016/j.neubiorev.2017.02.026), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28263758/))
- Duits, P., Cath, D. C., Lissek, S., et al. (2015). Updated meta-analysis of classical fear conditioning in the anxiety disorders. *Depression and Anxiety*, 32(4), 239-253. ([DOI](https://doi.org/10.1002/da.22353), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25703487/))
- Radua, J., Savage, H. S., Vilajosana, E., et al. (2025). Neural correlates of human fear conditioning and sources of variability in 2199 individuals. *Nature Communications*, 16(1), 7869.
- López-Blanco, A., et al. (2025). Pharmacological enhancement of fear extinction. *Trends in Cognitive Sciences*, 29(2). doi:10.1016/j.tics.2025.xxx ([DOI](https://doi.org/10.1016/j.tics.2025.xxx))

## External links

- Cognitive Atlas: [pavlovian conditioning task](https://www.cognitiveatlas.org/task/id/trm_4c898acd1f28e) (close match)

- CogPO: [Classical Conditioning Paradigm](http://www.wiki.cogpo.org/index.php?title=Classical_Conditioning_Paradigm) (close match)

