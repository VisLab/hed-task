(hedtsk_iowa_gambling)=
# Iowa Gambling Task

**HED task ID:** `hedtsk_iowa_gambling`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** IGT, Iowa Gambling

Repeated choices among four decks with hidden reward and loss distributions; preference shift toward advantageous decks indexes affective decision making.

## Description

Participants choose cards from four decks to maximize winnings. Two decks (A, B) have high wins but higher losses (net loss); two decks (C, D) have smaller wins but minimal losses (net gain). Over 100 trials, healthy participants gradually learn to prefer advantageous decks. The IGT is particularly sensitive to ventromedial prefrontal cortex damage; vmPFC patients fail to develop a preference for advantageous decks despite normal intellectual functioning. The task operationalizes the Somatic Marker Hypothesis.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-payoff">Choose for a payoff</a> (`choose_for_payoff`)
- **Game rules:** every rule takes the default of the game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-goal">reward goal</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-both">both</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-choice">choice</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-money">money</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>, <a href="vocabulary.html#motivator-real-hypothetical">hypothetical</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>, <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-trials">number of trials</a>, <a href="vocabulary.html#setting-reward-probability">reward probability</a>
- **Material:** Four decks of cards, each draw showing a money win and sometimes a loss, two decks with large wins and larger losses and two with small wins and small losses.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Four decks of cards are presented.
    2. Participants draw one card at a time from any deck.
    3. Each draw yields a reward and sometimes a penalty.
    4. Two decks are advantageous (smaller rewards, smaller penalties, net positive) and two are disadvantageous (larger rewards, larger penalties, net negative).
* - **Manipulations**
  - - Reward/penalty schedule
    - Number of trials
    - Deck position
    - Variant payoff structures
    - Outcome information (stated probabilities vs. discovered by experience)
* - **Measurements**
  - - Net score (advantageous - disadvantageous deck selections)
    - Learning curve across blocks
    - Anticipatory SCR before deck selection
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
* - Soochow Gambling Task (SGT)

    `hedvar_iowa_gambling__soochow_gambling_task_sgt`
  - named form
  - -
  - A named redesign whose only change is a payoff schedule that pits win frequency against win amount.
* - Child Versions

    `hedvar_iowa_gambling__child_versions`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>, <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>; population: <a href="vocabulary.html#facet-population-children">children</a>
  - -
  - Named children's instruments (Hungry Donkey, Children's Gambling Task) with a cartoon character, fewer trials and simpler feedback on the same payoff structure.
* - IGT with Explicit Probabilities

    `hedvar_iowa_gambling__igt_with_explicit_probabilities`
  - outcome knowledge: <a href="vocabulary.html#rule-choose-for-payoff-outcome-knowledge-described">described</a>
  - -
  - The win and loss amounts and probabilities of each deck are stated before play, so the options are described rather than discovered.
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

- Steingroever, H., Wetzels, R., Horstmann, A., Neumann, J., & Wagenmakers, E. J. (2013). Performance of healthy participants on the Iowa Gambling Task. *Psychological Assessment*, 25(1), 180-193. ([DOI](https://doi.org/10.1037/a0029929), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22984804/))
- Haines, N., Vassileva, J., & Ahn, W. Y. (2018). The Outcome-Representation Learning Model: A novel reinforcement learning model of the Iowa Gambling Task. *Cognitive Science*, 42(Suppl 3), 1098-1122. ([DOI](https://doi.org/10.1111/cogs.12688), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30289167/))
- Buelow, M. T., & Suhr, J. A. (2009). Construct validity of the Iowa Gambling Task. *Neuropsychology Review*, 19(1), 102-114. ([DOI](https://doi.org/10.1007/s11065-009-9083-4), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19194801/))
- Ahn, W. Y., Busemeyer, J. R., Wagenmakers, E. J., & Stout, J. C. (2008). Comparison of decision learning models using the generalization criterion method. *Cognitive Science*, 32(8), 1376-1402. ([DOI](https://doi.org/10.1080/03640210802352992), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21585458/))
- Decision-making and performance in the Iowa Gambling Task: recent ERP findings and clinical implications. (2025). *Frontiers in Psychology*, 16, 1492471. doi:10.3389/fpsyg.2025.1492471 ([DOI](https://doi.org/10.3389/fpsyg.2025.1492471), [PubMed](https://pubmed.ncbi.nlm.nih.gov/40177039/))

## External links

- Cognitive Atlas: [Iowa Gambling Task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949ae5)

