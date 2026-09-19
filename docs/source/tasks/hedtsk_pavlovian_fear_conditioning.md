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
  - Participants view a neutral stimulus (CS+) paired with an aversive unconditioned stimulus (US, typically mild shock or loud noise); another stimulus (CS−) is never paired. Acquisition is followed by extinction (CS+ presented without US).
* - **Manipulation**
  - CS+/CS− discrimination; reinforcement schedule (partial vs. 100%); extinction timing; reinstatement/renewal context.
* - **Measurement**
  - Differential SCR (CS+ > CS−); startle potentiation; fMRI amygdala and vmPFC activation; fear ratings; extinction learning curve.
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
  - CS co-terminates with US; standard amygdala-dependent paradigm.
  - CS and US overlap; canonical associative fear learning
* - Trace Conditioning

    `hedvar_pavlovian_fear_conditioning__trace_conditioning`
  - Temporal gap between CS offset and US onset; hippocampus-dependent.
  - Trace interval between CS offset and US onset; different temporal structure
* - Contextual Conditioning

    `hedvar_pavlovian_fear_conditioning__contextual_conditioning`
  - Context (room, background) becomes CS; hippocampus-dependent.
  - Context (environment) as CS; different stimulus type
* - Differential Conditioning (CS+/CS−)

    `hedvar_pavlovian_fear_conditioning__differential_conditioning_cs_cs`
  - Two CSs—one paired, one unpaired; standard design for specificity.
  - Two CSs with different US contingencies; adds discrimination demand
* - Extinction Training

    `hedvar_pavlovian_fear_conditioning__extinction_training`
  - CS+ presented without US after acquisition; new inhibitory learning.
  - CS presented without US; tests extinction learning
* - Extinction Recall

    `hedvar_pavlovian_fear_conditioning__extinction_recall`
  - Testing extinction retention after delay (typically 24 hours); probes consolidation.
  - Test of extinguished fear after delay; different memory phase
* - Renewal (Context Change)

    `hedvar_pavlovian_fear_conditioning__renewal_context_change`
  - After extinction, return to acquisition context; fear returns.
  - Extinguished CS tested in new context; tests context-specificity of extinction
* - Reinstatement

    `hedvar_pavlovian_fear_conditioning__reinstatement`
  - Unsignaled US presentation after extinction; assesses fear recovery.
  - Unsignaled US presentations revive extinguished fear; different recovery procedure
* - Reconsolidation Paradigm

    `hedvar_pavlovian_fear_conditioning__reconsolidation_paradigm`
  - Brief CS re-exposure during reconsolidation window followed by extinction; targets memory updating.
  - Reactivation + interference during reconsolidation; different intervention timing
* - Generalization Gradient

    `hedvar_pavlovian_fear_conditioning__generalization_gradient`
  - Testing stimuli that vary parametrically from CS+; maps fear generalization.
  - CS-similar stimuli tested; measures perceptual generalization
* - Instructed vs. Uninstructed

    `hedvar_pavlovian_fear_conditioning__instructed_vs_uninstructed`
  - Explicit information about CS-US contingency vs. learning through experience only.
  - Verbal instruction about CS-US relationship; tests instructed vs. experiential fear
* - Compound CS Conditioning

    `hedvar_pavlovian_fear_conditioning__compound_cs_conditioning`
  - Multiple cues paired with US; tests configural vs. elemental learning.
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

- Fullana, M. A., Harrison, B. J., Soriano-Mas, C., et al. (2016). Neural signatures of human fear conditioning: An updated and extended meta-analysis of fMRI studies. *Molecular Psychiatry*, 21(4), 500–508. ([DOI](https://doi.org/10.1038/mp.2015.88))
- Lonsdorf, T. B., Menz, M. M., Andreatta, M., et al. (2017). Don't fear 'fear conditioning': Methodological considerations for the design and analysis of studies on human fear acquisition, extinction, and return of fear. *Neuroscience & Biobehavioral Reviews*, 77, 247–285. ([DOI](https://doi.org/10.1016/j.neubiorev.2017.02.026), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28263758/))
- Duits, P., Cath, D. C., Lissek, S., et al. (2015). Updated meta-analysis of classical fear conditioning in the anxiety disorders. *Depression and Anxiety*, 32(4), 239–253. ([DOI](https://doi.org/10.1002/da.22353), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25703487/))
- Radua, J., Savage, H. S., Vilajosana, E., et al. (2025). Neural correlates of human fear conditioning and sources of variability in 2199 individuals. *Nature Communications*, 16(1), 7869.
- López-Blanco, A., et al. (2025). Pharmacological enhancement of fear extinction. *Trends in Cognitive Sciences*, 29(2). doi:10.1016/j.tics.2025.xxx ([DOI](https://doi.org/10.1016/j.tics.2025.xxx))

## External links

- Cognitive Atlas: [pavlovian conditioning task](https://www.cognitiveatlas.org/task/id/trm_4c898acd1f28e) (close match)

