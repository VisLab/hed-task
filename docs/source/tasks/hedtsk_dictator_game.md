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
  - Participants in the dictator role are endowed with a sum and decide how much (if any) to give to an anonymous recipient; the recipient has no choice but to accept.
* - **Manipulation**
  - Endowment size; anonymity conditions; social distance; framing (give vs. take); group identity.
* - **Measurement**
  - Amount allocated to recipient; proportion of fair (50-50) splits; distribution of allocations across participants.
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
  - Unilateral allocation with no recipient power.
  - Canonical: unilateral allocation from fixed endowment to anonymous recipient
* - Take Game

    `hedvar_dictator_game__take_game`
  - Dictator can take from recipient's endowment.
  - Dictator can take from recipient; different action space
* - Give-or-Take Game

    `hedvar_dictator_game__give_or_take_game`
  - Option to give or take; reveals true preferences.
  - Both giving and taking possible; combined action space
* - Double Dictator

    `hedvar_dictator_game__double_dictator`
  - Both players simultaneously dictate allocations to each other.
  - Both players act as dictators simultaneously; distinct social structure
* - Earned vs. Windfall Endowment

    `hedvar_dictator_game__earned_vs_windfall_endowment`
  - Working for the endowment vs. receiving it freely.
  - Endowment earned through effort vs. given randomly; changes perceived legitimacy
* - Audience/Observation Effects

    `hedvar_dictator_game__audience_observation_effects`
  - Dictating while observed vs. in private.
  - Observer present or aware of allocation; changes social context
* - N-Person Dictator

    `hedvar_dictator_game__n_person_dictator`
  - Distributing to multiple recipients.
  - Multiple recipients; changes social structure and distribution decision
* - Charitable Giving Dictator

    `hedvar_dictator_game__charitable_giving_dictator`
  - Recipient is a charity rather than individual.
  - Recipient is charity; different social/moral framing
* - Exit Option

    `hedvar_dictator_game__exit_option`
  - Participants can opt out of participation entirely.
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

