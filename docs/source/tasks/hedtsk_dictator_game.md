(hedtsk_dictator_game)=
# Dictator Game Task

**HED task ID:** `hedtsk_dictator_game`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Dictator Game, DG

One-shot allocation task in which a proposer unilaterally divides an endowment between self and a passive receiver; indexes altruism and social preferences.

## Description

One player (dictator) unilaterally decides how much of an endowment to give to an anonymous recipient, who has no power to reject. Despite having complete power, many dictators give 20-30% of their endowment, reflecting intrinsic fairness concerns. fMRI shows generous allocations activate reward regions (ventral striatum, OFC) and empathy regions (anterior insula, ACC), suggesting altruistic choices engage similar neural systems as personal reward.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-interact-with-agent">Play against another player</a> (`interact_with_agent`)
- **Game rules:** every rule takes the default of the game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-goal">reward goal</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-gain">gain</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-choice">choice</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-money">money</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>, <a href="vocabulary.html#motivator-real-hypothetical">hypothetical</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>
- **Material:** An endowment of money, of which the participant gives any share to an anonymous recipient.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants in the dictator role are endowed with a sum and decide how much (if any) to give to an anonymous recipient.
    2. The recipient has no choice but to accept.
* - **Manipulations**
  - - Endowment size
    - Anonymity conditions
    - Social distance
    - Framing (give vs. take)
    - Group identity
    - Role structure (both players give and receive vs. one giver)
    - Number of recipients (several vs. one)
    - Exit option (opt out for a fixed payoff vs. none)
* - **Measurements**
  - - Amount allocated to recipient
    - Proportion of fair (50-50) splits
    - Distribution of allocations across participants
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
* - Double Dictator

    `hedvar_dictator_game__double_dictator`
  - move order: <a href="vocabulary.html#rule-interact-with-agent-move-order-simultaneous">simultaneous</a>
  - -
  - Both players are endowed and each decides at the same time how much to give the other, so every participant is both giver and recipient.
* - Earned vs. Windfall Endowment

    `hedvar_dictator_game__earned_vs_windfall_endowment`
  - named form
  - -
  - The participant either earns the endowment in a prior task or is simply handed it before making the same allocation.
* - Audience/Observation Effects

    `hedvar_dictator_game__audience_observation_effects`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>, <a href="vocabulary.html#facet-social-aspect-being-observed">being observed</a>
  - -
  - The allocation is made where the experimenter or another person can see or will learn of it instead of under full anonymity.
* - N-Person Dictator

    `hedvar_dictator_game__n_person_dictator`
  - partner: <a href="vocabulary.html#rule-interact-with-agent-partner-group">group</a>
  - -
  - The money is divided among several recipients rather than one, possibly in different amounts.
* - Charitable Giving Dictator

    `hedvar_dictator_game__charitable_giving_dictator`
  - named form
  - -
  - The recipient is a named charity rather than an anonymous person, so the other party is an organization.
* - Exit Option

    `hedvar_dictator_game__exit_option`
  - exit option: <a href="vocabulary.html#rule-interact-with-agent-exit-option-available">available</a>
  - -
  - Before allocating, the participant may decline to play and keep a slightly smaller sum, and the recipient never learns that a game existed.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Social decision making](../processes/social_cognition_and_strategic_social_choice.md#hed-social-decision-making)
- [Valuation](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-valuation)
- [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking)
- [Reciprocity](../processes/social_cognition_and_strategic_social_choice.md#hed-reciprocity)

## Key references

- Harbaugh, W. T., Mayr, U., & Burghart, D. R. (2007). Neural responses to taxation and voluntary giving reveal motives for charitable donations. *Science*, 316(5831), 1622-1625. ([DOI](https://doi.org/10.1126/science.1140738), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17569866/))
- Moll, J., Krueger, F., Zahn, R., Pardini, M., de Oliveira-Souza, R., & Grafman, J. (2006). Human fronto-mesolimbic networks guide decisions about charitable donation. *Proceedings of the National Academy of Sciences*, 103(42), 15623-15628. ([DOI](https://doi.org/10.1073/pnas.0604475103), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17030808/))
- Forsythe, R., Horowitz, J. L., Savin, N. E., & Sefton, M. (1994). Fairness in simple bargaining experiments. *Games and Economic Behavior*, 6(3), 347-369. ([DOI](https://doi.org/10.1006/game.1994.1021))

## Further references

- Engel, C. (2011). Dictator games: A meta study. *Experimental Economics*, 14(4), 583-610. ([DOI](https://doi.org/10.1007/s10683-011-9283-7))
- Rand, D. G., & Epstein, Z. G. (2014). Risking your life without a second thought: Intuitive decision-making and extreme altruism. *PLoS ONE*, 9(10), e109687. ([DOI](https://doi.org/10.1371/journal.pone.0109687), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25333876/))

