(hedtsk_ultimatum_game)=
# Ultimatum Game Task

**HED task ID:** `hedtsk_ultimatum_game`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Ultimatum Game, UG

Proposer offers a division of an endowment; responder accepts or rejects. Rejection of unfair offers indexes inequity aversion and strategic punishment.

## Description

Two players divide a sum of money. The proposer suggests a division; the responder accepts (both get the proposed split) or rejects (both get nothing). Typically played with computer-controlled offers varying from fair (50-50) to unfair (90-10). Unfair offers activate the anterior insula (negative emotion, inequity aversion) and are rejected at high rates, even at personal cost. The task demonstrates the interplay between emotional reactions and rational economic considerations in social decision-making.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-interact-with-agent">Play against another player</a> (`interact_with_agent`)
- **Game rules:** every rule takes the default of the game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-goal">reward goal</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-gain">gain</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-joint-moves">joint moves</a>
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
- **Settings:** <a href="vocabulary.html#setting-number-of-trials">number of trials</a>, <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>
- **Material:** A proposed split of a sum of money, from fair (50-50) to unfair (90-10).

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A proposer splits a sum of money.
    2. The responder can accept (both keep their shares) or reject (neither gets anything).
* - **Manipulations**
  - - Offer fairness (proportion offered)
    - Endowment size
    - Proposer identity (human, computer)
    - Cultural context
    - Response method (strategy method vs. direct response)
    - Number of rounds (repeated play vs. one shot)
    - Punishment by a third party (observer pays to reduce earnings)
    - Number of proposers (competing offers)
    - Information about the sum (asymmetric vs. shared)
* - **Measurements**
  - - Rejection rate as function of offer
    - Minimum acceptable offer
    - Proposer strategy (modal offer)
    - fMRI anterior insula activation to unfair offers
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
* - Strategy Method

    `hedvar_ultimatum_game__strategy_method`
  - move order: <a href="vocabulary.html#rule-interact-with-agent-move-order-simultaneous">simultaneous</a>
  - -
  - The responder commits to a minimum acceptable offer, or an accept/reject answer for every possible offer, before seeing the actual offer, so the two moves are effectively made without knowledge of each other.
* - Multi-Round Ultimatum

    `hedvar_ultimatum_game__multi_round_ultimatum`
  - feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>; repetition: <a href="vocabulary.html#rule-interact-with-agent-repetition-iterated">iterated</a>
  - -
  - The same two players repeat the game over several rounds with outcomes shown, possibly swapping roles.
* - Third-Party Punishment

    `hedvar_ultimatum_game__third_party_punishment`
  - players acting: <a href="vocabulary.html#rule-interact-with-agent-players-acting-several">several</a>; sign: <a href="vocabulary.html#motivator-sign-both">both</a>
  - -
  - A third player who is not part of the split can pay from their own money to reduce the proposer's earnings after an unfair offer; this observer is usually the participant of interest.
* - Proposer Competition

    `hedvar_ultimatum_game__proposer_competition`
  - players acting: <a href="vocabulary.html#rule-interact-with-agent-players-acting-several">several</a>
  - -
  - Several proposers each make an offer to one responder, who may accept at most one.
* - Anonymous vs. Identified Partners

    `hedvar_ultimatum_game__anonymous_vs_identified_partners`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>, <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - -
  - Players either stay anonymous or learn who the partner is, see a photo or meet them before playing.
* - Ultimatum with Earned vs. Windfall Endowment

    `hedvar_ultimatum_game__ultimatum_with_earned_vs_windfall_endowment`
  - named form
  - -
  - The proposer either earns the sum in a prior task or is simply given it before the same game is played.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Social decision making](../processes/social_cognition_and_strategic_social_choice.md#hed-social-decision-making)
- [Reciprocity](../processes/social_cognition_and_strategic_social_choice.md#hed-reciprocity)
- [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation)
- [Valuation](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-valuation)

## Key references

- Guth, W., Schmittberger, R., & Schwarze, B. (1982). An experimental analysis of ultimatum bargaining. *Journal of Economic Behavior & Organization*, 3(4), 367-388. ([DOI](https://doi.org/10.1016/0167-2681(82)90011-7))
- Sanfey, A. G., Rilling, J. K., Aronson, J. A., Nystrom, L. E., & Cohen, J. D. (2003). The neural basis of economic decision-making in the Ultimatum Game. *Science*, 300(5626), 1755-1758. ([DOI](https://doi.org/10.1126/science.1082976), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12805551/))
- Feng, C., Luo, Y. J., & Krueger, F. (2015). Neural signatures of fairness-related normative decision-making in the ultimatum game: A coordinate-based meta-analysis. *Human Brain Mapping*, 36(2), 591-602. ([DOI](https://doi.org/10.1002/hbm.22649))

## Further references

- Gabay, A. S., Radua, J., Kempton, M. J., & Mehta, M. A. (2014). The Ultimatum Game and the brain: A meta-analysis of neuroimaging studies. *Neuroscience & Biobehavioral Reviews*, 47, 549-558. ([DOI](https://doi.org/10.1016/j.neubiorev.2014.10.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25454357/))
- Henrich, J., Boyd, R., Bowles, S., et al. (2005). "Economic man" in cross-cultural perspective: Behavioral experiments in 15 small-scale societies. *Behavioral and Brain Sciences*, 28(6), 795-815. ([DOI](https://doi.org/10.1017/s0140525x05000142), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16372952/))

## External links

- Cognitive Atlas: [Ultimatum Game (UG)](https://www.cognitiveatlas.org/task/id/trm_553e8882e3cb6)

