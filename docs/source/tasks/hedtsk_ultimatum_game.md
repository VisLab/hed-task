(hedtsk_ultimatum_game)=
# Ultimatum Game Task

**HED task ID:** `hedtsk_ultimatum_game`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Ultimatum Game, UG

Proposer offers a division of an endowment; responder accepts or rejects. Rejection of unfair offers indexes inequity aversion and strategic punishment.

## Description

Two players divide a sum of money. The proposer suggests a division; the responder accepts (both get the proposed split) or rejects (both get nothing). Typically played with computer-controlled offers varying from fair (50-50) to unfair (90-10). Unfair offers activate the anterior insula (negative emotion, inequity aversion) and are rejected at high rates, even at personal cost. The task demonstrates the interplay between emotional reactions and rational economic considerations in social decision-making.

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
* - **Measurements**
  - - Rejection rate as function of offer
    - Minimum acceptable offer
    - Proposer strategy (modal offer)
    - FMRI anterior insula activation to unfair offers
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
* - Standard Ultimatum

    `hedvar_ultimatum_game__standard_ultimatum`
  - Two-player, single-shot; proposer offers, responder accepts/rejects.
  - Canonical: proposer offers split, responder accepts/rejects
* - Strategy Method

    `hedvar_ultimatum_game__strategy_method`
  - Responder specifies minimum acceptable offer for all possible offers.
  - Responder states acceptance threshold for all possible offers; different elicitation
* - Multi-Round Ultimatum

    `hedvar_ultimatum_game__multi_round_ultimatum`
  - Repeated interactions with same partner; reputation effects.
  - Repeated rounds; tests learning and adaptation
* - Third-Party Punishment

    `hedvar_ultimatum_game__third_party_punishment`
  - Observer can punish unfair proposer at personal cost.
  - Observer can punish unfair proposer; adds external enforcement
* - Proposer Competition

    `hedvar_ultimatum_game__proposer_competition`
  - Multiple proposers compete with offers to one responder.
  - Multiple proposers compete for responder; changes market structure
* - Asymmetric Information

    `hedvar_ultimatum_game__asymmetric_information`
  - Endowment size unknown to one party.
  - Responder does not know pie size; different information structure
* - Stake Variation

    `hedvar_ultimatum_game__stake_variation`
  - Varying endowment size from $1 to $100+.
  - Systematically varies total pie size; tests stake sensitivity
* - Anonymous vs. Identified Partners

    `hedvar_ultimatum_game__anonymous_vs_identified_partners`
  - Varying social distance and information about partner.
  - Social identification changes accountability
* - Ultimatum with Earned vs. Windfall Endowment

    `hedvar_ultimatum_game__ultimatum_with_earned_vs_windfall_endowment`
  - Effort-based vs. random allocation.
  - Endowment from effort vs. luck; changes perceived legitimacy
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

- Gabay, A. S., Radua, J., Kempton, M. J., & Mehta, M. A. (2014). The Ultimatum Game and the brain: A meta-analysis of neuroimaging studies. *Neuroscience & Biobehavioral Reviews*, 47, 549–558. ([DOI](https://doi.org/10.1016/j.neubiorev.2014.10.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25454357/))
- Henrich, J., Boyd, R., Bowles, S., et al. (2005). "Economic man" in cross-cultural perspective: Behavioral experiments in 15 small-scale societies. *Behavioral and Brain Sciences*, 28(6), 795–815. ([DOI](https://doi.org/10.1017/s0140525x05000142), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16372952/))

## External links

- Cognitive Atlas: [Ultimatum Game (UG)](https://www.cognitiveatlas.org/task/id/trm_553e8882e3cb6)

