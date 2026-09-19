(hedtsk_iowa_gambling)=
# Iowa Gambling Task

**HED task ID:** `hedtsk_iowa_gambling`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** IGT, Iowa Gambling

Repeated choices among four decks with hidden reward and loss distributions; preference shift toward advantageous decks indexes affective decision making.

## Description

Participants choose cards from four decks to maximize winnings. Two decks (A, B) have high wins but higher losses (net loss); two decks (C, D) have smaller wins but minimal losses (net gain). Over 100 trials, healthy participants gradually learn to prefer advantageous decks. The IGT is particularly sensitive to ventromedial prefrontal cortex damage; vmPFC patients fail to develop a preference for advantageous decks despite normal intellectual functioning. The task operationalizes the Somatic Marker Hypothesis.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Four decks of cards are presented; participants draw one card at a time from any deck. Each draw yields a reward and sometimes a penalty. Two decks are advantageous (smaller rewards, smaller penalties, net positive) and two are disadvantageous (larger rewards, larger penalties, net negative).
* - **Manipulation**
  - Reward/penalty schedule; number of trials; deck position; variant payoff structures.
* - **Measurement**
  - Net score (advantageous − disadvantageous deck selections); learning curve across blocks; anticipatory SCR before deck selection.
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
* - Standard IGT

    `hedvar_iowa_gambling__standard_igt`
  - 100 trials, 4 decks, fixed payoff schedules (A/B disadvantageous, C/D advantageous).
  - Canonical four-deck IGT with covert payoff structure
* - Soochow Gambling Task (SGT)

    `hedvar_iowa_gambling__soochow_gambling_task_sgt`
  - Modified payoff structure separating frequency from magnitude of losses.
  - Reversed long-run structure; tests frequency vs. magnitude sensitivity
* - Child Versions

    `hedvar_iowa_gambling__child_versions`
  - Hungry Donkey Task, Children's Gambling Task; age-appropriate formats.
  - Simplified decks and stimuli for children; procedure adapted per §5.3
* - Extended IGT (150–200 trials)

    `hedvar_iowa_gambling__extended_igt_150_200_trials`
  - More trials to examine later learning phases.
  - Extended trial count; tests learning at longer timescales
* - IGT with Explicit Probabilities

    `hedvar_iowa_gambling__igt_with_explicit_probabilities`
  - Payoff information explicitly provided; separates learning from decision.
  - Payoff probabilities stated explicitly; changes information structure
* - Modified Payoff Variants

    `hedvar_iowa_gambling__modified_payoff_variants`
  - Equated frequency, equated magnitude, or reversed deck structures.
  - Different win/loss schedules; tests sensitivity to schedule structure
```

## Cognitive processes

This task is designed to engage the following processes:

- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)
- [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
- [Risk processing](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-risk-processing)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation)

## Key references

- Bechara, A., Damasio, A. R., Damasio, H., & Anderson, S. W. (1994). Insensitivity to future consequences following damage to human prefrontal cortex. *Cognition*, 50(1-3), 7-15. ([DOI](https://doi.org/10.1016/0010-0277(94)90018-3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8039375/))
- Bechara, A., Damasio, H., Tranel, D., & Damasio, A. R. (1997). Deciding advantageously before knowing the advantageous strategy. *Science*, 275(5304), 1293-1295. ([DOI](https://doi.org/10.1126/science.275.5304.1293), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9036851/))
- Li, X., Lu, Z. L., D'Argembeau, A., Ng, M., & Bechara, A. (2010). The Iowa Gambling Task in fMRI images. *Human Brain Mapping*, 31(3), 410-423. ([DOI](https://doi.org/10.1002/hbm.20875))

## Further references

- Steingroever, H., Wetzels, R., Horstmann, A., Neumann, J., & Wagenmakers, E. J. (2013). Performance of healthy participants on the Iowa Gambling Task. *Psychological Assessment*, 25(1), 180–193. ([DOI](https://doi.org/10.1037/a0029929), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22984804/))
- Haines, N., Vassileva, J., & Ahn, W. Y. (2018). The Outcome-Representation Learning Model: A novel reinforcement learning model of the Iowa Gambling Task. *Cognitive Science*, 42(Suppl 3), 1098–1122. ([DOI](https://doi.org/10.1111/cogs.12688), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30289167/))
- Buelow, M. T., & Suhr, J. A. (2009). Construct validity of the Iowa Gambling Task. *Neuropsychology Review*, 19(1), 102–114. ([DOI](https://doi.org/10.1007/s11065-009-9083-4), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19194801/))
- Ahn, W. Y., Busemeyer, J. R., Wagenmakers, E. J., & Stout, J. C. (2008). Comparison of decision learning models using the generalization criterion method. *Cognitive Science*, 32(8), 1376–1402. ([DOI](https://doi.org/10.1080/03640210802352992), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21585458/))
- Decision-making and performance in the Iowa Gambling Task: recent ERP findings and clinical implications. (2025). *Frontiers in Psychology*, 16, 1492471. doi:10.3389/fpsyg.2025.1492471 ([DOI](https://doi.org/10.3389/fpsyg.2025.1492471), [PubMed](https://pubmed.ncbi.nlm.nih.gov/40177039/))

## External links

- Cognitive Atlas: [Iowa Gambling Task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949ae5)

