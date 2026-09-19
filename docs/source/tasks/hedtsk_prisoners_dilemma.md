(hedtsk_prisoners_dilemma)=
# Prisoner's Dilemma Task

**HED task ID:** `hedtsk_prisoners_dilemma`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Prisoner's Dilemma, PD, Iterated Prisoner's Dilemma, Iterated PD

Two-player one-shot or iterated game with cooperate/defect choices and asymmetric payoffs; choice patterns index cooperation and strategic reasoning.

## Description

The Prisoner's Dilemma is a canonical game theory paradigm for studying cooperation and defection under strategic interdependence. Two players simultaneously choose to cooperate or defect. Mutual cooperation yields moderate rewards for both; mutual defection yields low rewards for both; but if one defects while the other cooperates, the defector receives the highest reward and the cooperator receives nothing (or a penalty). The dominant strategy in single-shot play is to defect, yet human participants frequently cooperate, particularly in iterated versions. The task is central to research on trust, reciprocity, altruism, and the neural substrates of social decision-making.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Two players simultaneously choose to cooperate or defect; payoffs depend on both choices according to a matrix where mutual cooperation beats mutual defection but defection is individually tempting.
* - **Manipulation**
  - Payoff matrix values; one-shot vs. iterated; partner identity (human, computer, in-group); communication allowed or not.
* - **Measurement**
  - Cooperation rate; payoff earned; tit-for-tat and other strategy classification; first-move cooperation.
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
* - Single-Shot (One-Round) PD

    `hedvar_prisoners_dilemma__single_shot_one_round_pd`
  - One simultaneous decision; tests baseline cooperation rates.
  - Canonical one-round anonymous PD; no reputation effects
* - Iterated PD (Repeated Games)

    `hedvar_prisoners_dilemma__iterated_pd_repeated_games`
  - Multiple rounds with same partner; enables tit-for-tat strategies.
  - Multiple rounds with same partner; reputation and strategy accumulate
* - Sequential PD

    `hedvar_prisoners_dilemma__sequential_pd`
  - One player decides first, then the other; introduces trust asymmetry.
  - One player acts before observing other's choice; different temporal structure
* - Multiplayer/Public Goods Version

    `hedvar_prisoners_dilemma__multiplayer_public_goods_version`
  - N-player generalization; contribute to a common pool.
  - More than two players; group dilemma structure
* - PD with Communication

    `hedvar_prisoners_dilemma__pd_with_communication`
  - Cheap talk or binding communication before decisions.
  - Players communicate before deciding; cheap talk changes decision context
* - PD with Punishment Option

    `hedvar_prisoners_dilemma__pd_with_punishment_option`
  - Third-party or second-party punishment of defectors.
  - Third-party punishment available; adds enforcement mechanism
* - PD with Varying Payoff Matrices

    `hedvar_prisoners_dilemma__pd_with_varying_payoff_matrices`
  - Manipulating temptation-to-defect and cooperation incentives parametrically.
  - Different temptation/sucker payoffs; tests sensitivity to game parameters
* - PD against Computer Opponents

    `hedvar_prisoners_dilemma__pd_against_computer_opponents`
  - Known strategies (always cooperate, always defect, tit-for-tat).
  - Computer opponent instead of human; per §5.6 structural change (deterministic vs. human partner)
* - PD with Reputation Information

    `hedvar_prisoners_dilemma__pd_with_reputation_information`
  - Partners' cooperation histories visible; tests reputation effects.
  - Partner's past cooperation history visible; changes social information available
* - Continuous PD

    `hedvar_prisoners_dilemma__continuous_pd`
  - Graded cooperation rather than binary cooperate/defect.
  - Continuous contribution instead of binary; different action space
* - Asymmetric Prisoner's Dilemma

    `hedvar_prisoners_dilemma__asymmetric_prisoners_dilemma`
  - Payoffs do not mirror each other; one player gains more or loses less from defection, introducing inequity into the strategic calculus.
  - Different payoff structures for each player; breaks symmetry of standard PD
* - Optional Prisoner's Dilemma

    `hedvar_prisoners_dilemma__optional_prisoners_dilemma`
  - Players can opt out of the interaction entirely, receiving a safe intermediate payoff; opt-out availability typically increases cooperation among those who choose to play.
  - Third option to not participate; changes strategic choice set
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

- Rilling, J. K., Gutman, D. A., Zeh, T. R., Pagnoni, G., Berns, G. S., & Kilts, C. D. (2002). A neural basis for social cooperation. *Neuron*, 35(2), 395–405. ([DOI](https://doi.org/10.1016/s0896-6273(02)00755-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12160756/))
- Fehr, E., & Fischbacher, U. (2003). The nature of human altruism. *Nature*, 425(6960), 785–791. ([DOI](https://doi.org/10.1038/nature02043), [PubMed](https://pubmed.ncbi.nlm.nih.gov/14574401/))

## Further references

- Rand, D. G., & Nowak, M. A. (2013). Human cooperation. *Trends in Cognitive Sciences*, 17(8), 413–425. ([DOI](https://doi.org/10.1016/j.tics.2013.06.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23856025/))
- Engel, C., & Zhurakhovska, L. (2016). When is the risk of cooperation worth taking? The prisoner's dilemma as a game of multiple motives. *Applied Economics Letters*, 23(16), 1157–1161. ([DOI](https://doi.org/10.1080/13504851.2016.1139672))
- Declerck, C. H., Boone, C., & Emonds, G. (2013). When do people cooperate? The neuroeconomics of prosocial decision making. *Brain and Cognition*, 81(1), 95–117. ([DOI](https://doi.org/10.1016/j.bandc.2012.09.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23174433/))
- Peysakhovich, A., Nowak, M. A., & Rand, D. G. (2014). Humans display a 'cooperative phenotype' that is domain general and temporally stable. *Nature Communications*, 5, 4939. ([DOI](https://doi.org/10.1038/ncomms5939), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25225950/))

## External links

- Cognitive Atlas: [prisoner's dilemma (PD)](https://www.cognitiveatlas.org/task/id/tsk_KRl3zbyaJcKWM)

