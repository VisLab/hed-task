(hedtsk_prisoners_dilemma)=
# Prisoner's Dilemma Task

**HED task ID:** `hedtsk_prisoners_dilemma`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Prisoner's Dilemma, PD, Iterated Prisoner's Dilemma, Iterated PD

Two-player one-shot or iterated game with cooperate/defect choices and asymmetric payoffs; choice patterns index cooperation and strategic reasoning.

## Description

The Prisoner's Dilemma is a canonical game theory paradigm for studying cooperation and defection under strategic interdependence. Two players simultaneously choose to cooperate or defect. Mutual cooperation yields moderate rewards for both; mutual defection yields low rewards for both; but if one defects while the other cooperates, the defector receives the highest reward and the cooperator receives nothing (or a penalty). The dominant strategy in single-shot play is to defect, yet human participants frequently cooperate, particularly in iterated versions. The task is central to research on trust, reciprocity, altruism, and the neural substrates of social decision-making.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-interact-with-agent">interact with agent</a>
- **In what order?** <a href="vocabulary.html#rule-interact-with-agent-move-order-simultaneous">simultaneous</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-reward-goal">reward goal</a>
- **Can the player gain, lose, or both?** <a href="vocabulary.html#motivation-sign-gain">gain</a>
- **What earns the outcome?** <a href="vocabulary.html#motivation-earned-by-joint-moves">joint moves</a>
- **What is the outcome?** <a href="vocabulary.html#motivation-what-money">money</a>
- **Is the outcome real?** <a href="vocabulary.html#motivation-real-paid">paid</a>, <a href="vocabulary.html#motivation-real-hypothetical">hypothetical</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>
- **Social aspect:** <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>
- **Material:** A payoff matrix of money amounts for each combination of the two players' choices to cooperate or defect.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Two players simultaneously choose to cooperate or defect.
    2. Payoffs depend on both choices according to a matrix where mutual cooperation beats mutual defection but defection is individually tempting.
* - **Manipulations**
  - - Payoff matrix values
    - One-shot vs. iterated
    - Partner identity (human, computer, in-group)
    - Communication allowed or not
    - Move order (sequential vs. simultaneous)
    - Number of players and move granularity (public goods contribution)
    - Punishment option after choices are revealed
    - Exit option (opt out for a guaranteed small payoff vs. none)
* - **Measurements**
  - - Cooperation rate
    - Payoff earned
    - Tit-for-tat and other strategy classification
    - First-move cooperation
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
* - Iterated PD (Repeated Games)

    `hedvar_prisoners_dilemma__iterated_pd_repeated_games`
  - feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>; repetition: <a href="vocabulary.html#rule-interact-with-agent-repetition-iterated">iterated</a>
  - -
  - The same two players choose repeatedly and see each other's past choices after every round, so conditional strategies become possible.
* - Sequential PD

    `hedvar_prisoners_dilemma__sequential_pd`
  - move order: <a href="vocabulary.html#rule-interact-with-agent-move-order-sequential">sequential</a>
  - -
  - One player chooses first and the second sees that choice before choosing.
* - Multiplayer/Public Goods Version

    `hedvar_prisoners_dilemma__multiplayer_public_goods_version`
  - players acting: <a href="vocabulary.html#rule-interact-with-agent-players-acting-several">several</a>; partner: <a href="vocabulary.html#rule-interact-with-agent-partner-group">group</a>; transfer transformation: <a href="vocabulary.html#rule-interact-with-agent-transfer-transformation-multiplied">multiplied</a>
  - -
  - Several players each contribute an amount to a shared pool that is multiplied and divided equally among all, so there are many players and each chooses an amount rather than simply cooperating or defecting.
* - PD with Punishment Option

    `hedvar_prisoners_dilemma__pd_with_punishment_option`
  - sign: <a href="vocabulary.html#motivation-sign-both">both</a>
  - -
  - After the choices are revealed, a player or an observing third party can pay from their own money to reduce a defector's earnings.
* - PD against Computer Opponents

    `hedvar_prisoners_dilemma__pd_against_computer_opponents`
  - partner: <a href="vocabulary.html#rule-interact-with-agent-partner-computer">computer</a>
  - -
  - The other player is a program following a fixed strategy such as always cooperate, always defect or tit-for-tat, and the participant may or may not be told.
* - PD with Reputation Information

    `hedvar_prisoners_dilemma__pd_with_reputation_information`
  - named form
  - -
  - Before choosing, the participant is shown how often the current partner cooperated in earlier games with other people.
* - Continuous PD

    `hedvar_prisoners_dilemma__continuous_pd`
  - named form
  - -
  - Each player chooses how much to cooperate on a scale, for example how much of an endowment to transfer to the partner, rather than making a yes-or-no choice.
* - Optional Prisoner's Dilemma

    `hedvar_prisoners_dilemma__optional_prisoners_dilemma`
  - exit option: <a href="vocabulary.html#rule-interact-with-agent-exit-option-available">available</a>
  - -
  - Each player may opt out for a guaranteed small payoff, and those who play face the usual choice.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Social decision making](../processes/social_cognition_and_strategic_social_choice.md#hed-social-decision-making)
- [Cooperation](../processes/social_cognition_and_strategic_social_choice.md#hed-cooperation)
- [Competition](../processes/social_cognition_and_strategic_social_choice.md#hed-competition)
- [Reciprocity](../processes/social_cognition_and_strategic_social_choice.md#hed-reciprocity)
- [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use)
- [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking)

## Key references

- Rilling, J. K., Gutman, D. A., Zeh, T. R., Pagnoni, G., Berns, G. S., & Kilts, C. D. (2002). A neural basis for social cooperation. *Neuron*, 35(2), 395-405. ([DOI](https://doi.org/10.1016/s0896-6273(02)00755-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12160756/))
- Fehr, E., & Fischbacher, U. (2003). The nature of human altruism. *Nature*, 425(6960), 785-791. ([DOI](https://doi.org/10.1038/nature02043), [PubMed](https://pubmed.ncbi.nlm.nih.gov/14574401/))

## Further references

- Rand, D. G., & Nowak, M. A. (2013). Human cooperation. *Trends in Cognitive Sciences*, 17(8), 413-425. ([DOI](https://doi.org/10.1016/j.tics.2013.06.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23856025/))
- Engel, C., & Zhurakhovska, L. (2016). When is the risk of cooperation worth taking? The prisoner's dilemma as a game of multiple motives. *Applied Economics Letters*, 23(16), 1157-1161. ([DOI](https://doi.org/10.1080/13504851.2016.1139672))
- Declerck, C. H., Boone, C., & Emonds, G. (2013). When do people cooperate? The neuroeconomics of prosocial decision making. *Brain and Cognition*, 81(1), 95-117. ([DOI](https://doi.org/10.1016/j.bandc.2012.09.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23174433/))
- Peysakhovich, A., Nowak, M. A., & Rand, D. G. (2014). Humans display a 'cooperative phenotype' that is domain general and temporally stable. *Nature Communications*, 5, 4939. ([DOI](https://doi.org/10.1038/ncomms5939), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25225950/))

## External links

- Cognitive Atlas: [prisoner's dilemma (PD)](https://www.cognitiveatlas.org/task/id/tsk_KRl3zbyaJcKWM)

