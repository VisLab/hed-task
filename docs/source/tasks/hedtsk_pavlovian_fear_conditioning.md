(hedtsk_pavlovian_fear_conditioning)=
# Pavlovian Fear Conditioning Task

**HED task ID:** `hedtsk_pavlovian_fear_conditioning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Fear Conditioning, Classical Conditioning, FC

A neutral CS is paired with an aversive US (shock, loud sound); conditioned responses (SCR, startle, amygdala BOLD) index fear learning.

## Description

A neutral conditioned stimulus (CS; auditory tone or visual cue) is paired with an aversive unconditioned stimulus (US; mild shock, loud noise). After conditioning, the CS alone elicits conditioned fear responses including skin conductance increases, heart rate changes, freezing (in animals), and subjective fear ratings (in humans). Extinction is measured in a subsequent phase where the CS is presented without the US. The task is fundamental to understanding emotional learning and has been used extensively to study the amygdala's role in fear acquisition and the prefrontal cortex's role in extinction.

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
* - **Manipulations**
  - - CS+/CS- discrimination
    - Reinforcement schedule (partial vs. 100%)
    - Extinction timing
    - reinstatement/renewal context
* - **Measurements**
  - - Differential SCR (CS+ > CS-)
    - Startle potentiation
    - fMRI amygdala and vmPFC activation
    - Fear ratings
    - Extinction learning curve
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
* - Delay Conditioning

    `hedvar_pavlovian_fear_conditioning__delay_conditioning`

    Cognitive Atlas: [delay conditioning](https://www.cognitiveatlas.org/task/id/trm_5023ef8eab626) (close match)
  - A neutral cue such as a colored shape or tone is presented for several seconds, and a mild electric shock or loud noise arrives at the end of the cue while it is still on. After several pairings the cue alone produces a fear response such as increased skin conductance.
  - CS and US overlap; canonical associative fear learning
* - Trace Conditioning

    `hedvar_pavlovian_fear_conditioning__trace_conditioning`

    Cognitive Atlas: [trace conditioning](https://www.cognitiveatlas.org/task/id/trm_4a3fd79d0b3d7) (close match)
  - The cue ends and there is a silent gap of a few seconds before the shock arrives, so the participant must bridge the gap in memory to link cue and shock. Harder to learn than the overlapping version.
  - Trace interval between CS offset and US onset; different temporal structure
* - Contextual Conditioning

    `hedvar_pavlovian_fear_conditioning__contextual_conditioning`
  - No discrete cue predicts the shock. Instead shocks occur at unpredictable times in a particular setting, such as one of two virtual rooms or a background color, and fear becomes attached to the setting itself.
  - Context (environment) as CS; different stimulus type
* - Differential Conditioning (CS+/CS-)

    `hedvar_pavlovian_fear_conditioning__differential_conditioning_cs_cs`
  - Two cues are used: one is followed by the shock and the other never is. Fear to the paired cue minus fear to the safe cue shows that the participant learned the specific prediction, not just a general wariness.
  - Two CSs with different US contingencies; adds discrimination demand
* - Extinction Training

    `hedvar_pavlovian_fear_conditioning__extinction_training`
  - After conditioning, the cue is presented many times without any shock. The fear response gradually fades as the participant learns that the cue no longer predicts the shock.
  - CS presented without US; tests extinction learning
* - Extinction Recall

    `hedvar_pavlovian_fear_conditioning__extinction_recall`
  - A day or more after extinction, the cue is presented again without shock. Whether the fear stays low or returns measures how well the extinction learning was retained.
  - Test of extinguished fear after delay; different memory phase
* - Renewal (Context Change)

    `hedvar_pavlovian_fear_conditioning__renewal_context_change`
  - Conditioning takes place in one setting and extinction in another. The cue is then tested back in the original setting (or a new one), where the fear response typically returns, showing extinction is tied to where it happened.
  - Extinguished CS tested in new context; tests context-specificity of extinction
* - Reinstatement

    `hedvar_pavlovian_fear_conditioning__reinstatement`
  - After extinction, a few shocks are given with no cue present. When the cue is then tested, the fear response comes back even though the cue was never paired again.
  - Unsignaled US presentations revive extinguished fear; different recovery procedure
* - Reconsolidation Paradigm

    `hedvar_pavlovian_fear_conditioning__reconsolidation_paradigm`
  - A day after conditioning, the cue is presented once to reactivate the memory, and extinction training follows within a window of about ten minutes to a few hours. Extinction given in this window can prevent fear from returning later.
  - Reactivation + interference during reconsolidation; different intervention timing
* - Generalization Gradient

    `hedvar_pavlovian_fear_conditioning__generalization_gradient`
  - After conditioning to one cue (for example a circle of a given size), cues that differ from it by increasing amounts are tested. Plotting fear against similarity shows how far fear spreads to similar things.
  - CS-similar stimuli tested; measures perceptual generalization
* - Instructed vs. Uninstructed

    `hedvar_pavlovian_fear_conditioning__instructed_vs_uninstructed`
  - Some participants are told in advance which cue will be followed by shock; others find out only by experience. Compares fear learned through words with fear learned through direct experience.
  - Verbal instruction about CS-US relationship; tests instructed vs. experiential fear
* - Compound CS Conditioning

    `hedvar_pavlovian_fear_conditioning__compound_cs_conditioning`
  - Two or more cues are presented together (such as a light and a tone) before the shock. Later the cues are tested separately and together to see whether the participant learned about each element or about the combination.
  - CS compound with multiple elements; different stimulus structure
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

