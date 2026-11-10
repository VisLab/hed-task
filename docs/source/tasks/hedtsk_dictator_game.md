(hedtsk_dictator_game)=
# Dictator Game Task

**HED task ID:** `hedtsk_dictator_game`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Dictator Game, DG

One-shot allocation task in which a proposer unilaterally divides an endowment between self and a passive receiver; indexes altruism and social preferences.

## Description

One player (dictator) unilaterally decides how much of an endowment to give to an anonymous recipient, who has no power to reject. Despite having complete power, many dictators give 20-30% of their endowment, reflecting intrinsic fairness concerns. fMRI shows generous allocations activate reward regions (ventral striatum, OFC) and empathy regions (anterior insula, ACC), suggesting altruistic choices engage similar neural systems as personal reward.

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
* - **Measurements**
  - - Amount allocated to recipient
    - Proportion of fair (50-50) splits
    - Distribution of allocations across participants
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
* - Standard Dictator Game

    `hedvar_dictator_game__standard_dictator_game`
  - The participant is given a sum of money and decides how much of it, if any, to give to another anonymous person who has no say and cannot respond. The amount given is the measure of generosity.
  - Canonical: unilateral allocation from fixed endowment to anonymous recipient
* - Take Game

    `hedvar_dictator_game__take_game`
  - The other person starts with the money, and the participant decides how much to take from them rather than how much to give. The outcomes possible are the same, but the action is taking rather than giving.
  - Dictator can take from recipient; different action space
* - Give-or-Take Game

    `hedvar_dictator_game__give_or_take_game`
  - Both people start with money, and the participant may either give some of their own to the other person or take some of the other person's money. Any split within the combined total is possible.
  - Both giving and taking possible; combined action space
* - Double Dictator

    `hedvar_dictator_game__double_dictator`
  - Both participants are given money and each decides at the same time how much to give the other, without knowing the other's decision. Each person is a giver and a recipient.
  - Both players act as dictators simultaneously; distinct social structure
* - Earned vs. Windfall Endowment

    `hedvar_dictator_game__earned_vs_windfall_endowment`
  - Before the game, the participant either earns the money by doing a task (such as a quiz or typing job) or is simply handed it. People tend to give less when they earned the money themselves.
  - Endowment earned through effort vs. given randomly; changes perceived legitimacy
* - Audience/Observation Effects

    `hedvar_dictator_game__audience_observation_effects`
  - The decision is made while the experimenter or another person can see it, or will learn of it, compared with a fully anonymous decision where nobody can link the giver to the amount.
  - Observer present or aware of allocation; changes social context
* - N-Person Dictator

    `hedvar_dictator_game__n_person_dictator`
  - The participant divides the money among several recipients rather than one, and may give different amounts to different people.
  - Multiple recipients; changes social structure and distribution decision
* - Charitable Giving Dictator

    `hedvar_dictator_game__charitable_giving_dictator`
  - The recipient is a named charity instead of an anonymous person. The participant decides how much of the money to donate.
  - Recipient is charity; different social/moral framing
* - Exit Option

    `hedvar_dictator_game__exit_option`
  - Before dividing the money, the participant may choose not to play at all and keep a slightly smaller amount, so that the recipient never learns a game existed. Taking the exit shows that giving in the standard game is partly driven by not wanting to be seen as unfair.
  - Option to leave game rather than allocate; adds outside option to choice set
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
- Forsythe, R., Horowitz, J. L., Savin, N. E., & Sefton, M. (1994). Fairness in simple bargaining experiments. *Games and Economic Behavior*, 6(3), 347–369. ([DOI](https://doi.org/10.1006/game.1994.1021))

## Further references

- Engel, C. (2011). Dictator games: A meta study. *Experimental Economics*, 14(4), 583–610. ([DOI](https://doi.org/10.1007/s10683-011-9283-7))
- Rand, D. G., & Epstein, Z. G. (2014). Risking your life without a second thought: Intuitive decision-making and extreme altruism. *PLoS ONE*, 9(10), e109687. ([DOI](https://doi.org/10.1371/journal.pone.0109687), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25333876/))

