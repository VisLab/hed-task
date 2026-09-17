(hedtsk_prisoners_dilemma)=

# Prisoner's Dilemma Task

**HED Task ID:** `hedtsk_prisoners_dilemma`

**Also known as:** Prisoner's Dilemma, PD, Iterated Prisoner's Dilemma, Iterated PD

Two-player one-shot or iterated game with cooperate/defect choices and asymmetric payoffs; choice patterns index cooperation and strategic reasoning.

## Description

The Prisoner's Dilemma is a canonical game theory paradigm for studying cooperation and defection under strategic interdependence. Two players simultaneously choose to cooperate or defect. Mutual cooperation yields moderate rewards for both; mutual defection yields low rewards for both; but if one defects while the other cooperates, the defector receives the highest reward and the cooperator receives nothing (or a penalty). The dominant strategy in single-shot play is to defect, yet human participants frequently cooperate, particularly in iterated versions. The task is central to research on trust, reciprocity, altruism, and the neural substrates of social decision-making.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - Two players simultaneously choose to cooperate or defect; payoffs depend on both choices according to a matrix where mutual cooperation beats mutual defection but defection is individually tempting.
* - **Manipulation**
  - Payoff matrix values; one-shot vs. iterated; partner identity (human, computer, in-group); communication allowed or not.
* - **Measurement**
  - Cooperation rate; payoff earned; tit-for-tat and other strategy classification; first-move cooperation.
```

## Variations

```{list-table}
---
widths: 25 40 35
header-rows: 1
---
* - Variation
  - Description
  - Justification
* - Single-Shot (One-Round) PD
  - One simultaneous decision; tests baseline cooperation rates.
  - Canonical one-round anonymous PD; no reputation effects
* - Iterated PD (Repeated Games)
  - Multiple rounds with same partner; enables tit-for-tat strategies.
  - Multiple rounds with same partner; reputation and strategy accumulate
* - Sequential PD
  - One player decides first, then the other; introduces trust asymmetry.
  - One player acts before observing other's choice; different temporal structure
* - Multiplayer/Public Goods Version
  - N-player generalization; contribute to a common pool.
  - More than two players; group dilemma structure
* - PD with Communication
  - Cheap talk or binding communication before decisions.
  - Players communicate before deciding; cheap talk changes decision context
* - PD with Punishment Option
  - Third-party or second-party punishment of defectors.
  - Third-party punishment available; adds enforcement mechanism
* - PD with Varying Payoff Matrices
  - Manipulating temptation-to-defect and cooperation incentives parametrically.
  - Different temptation/sucker payoffs; tests sensitivity to game parameters
* - PD against Computer Opponents
  - Known strategies (always cooperate, always defect, tit-for-tat).
  - Computer opponent instead of human; per §5.6 structural change (deterministic vs. human partner)
* - PD with Reputation Information
  - Partners' cooperation histories visible; tests reputation effects.
  - Partner's past cooperation history visible; changes social information available
* - Continuous PD
  - Graded cooperation rather than binary cooperate/defect.
  - Continuous contribution instead of binary; different action space
* - Asymmetric Prisoner's Dilemma
  - Payoffs do not mirror each other; one player gains more or loses less from defection, introducing inequity into the strategic calculus.
  - Different payoff structures for each player; breaks symmetry of standard PD
* - Optional Prisoner's Dilemma
  - Players can opt out of the interaction entirely, receiving a safe intermediate payoff; opt-out availability typically increases cooperation among those who choose to play.
  - Third option to not participate; changes strategic choice set
```

## Cognitive processes

This task engages the following cognitive processes:

- [Social decision making](../processes/social_cognition_and_strategic_social_choice.md#hed-social-decision-making)
- [Cooperation](../processes/social_cognition_and_strategic_social_choice.md#hed-cooperation)
- [Competition](../processes/social_cognition_and_strategic_social_choice.md#hed-competition)
- [Reciprocity](../processes/social_cognition_and_strategic_social_choice.md#hed-reciprocity)
- [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use)
- [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking)

## Key references

- {'authors': 'Rilling, J. K., Gutman, D. A., Zeh, T. R., Pagnoni, G., Berns, G. S., & Kilts, C. D.', 'year': 2002, 'title': 'A Neural Basis for Social Cooperation', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '35', 'issue': '2', 'pages': '395-405', 'doi': '10.1016/s0896-6273(02)00755-9', 'openalex_id': None, 'pmid': None, 'citation_string': 'Rilling, J. K., Gutman, D. A., Zeh, T. R., Pagnoni, G., Berns, G. S., & Kilts, C. D. (2002). A neural basis for social cooperation. *Neuron*, 35(2), 395–405.', 'url': 'https://doi.org/10.1016/s0896-6273(02)00755-9', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Fehr, E., & Fischbacher, U.', 'year': 2003, 'title': 'The nature of human altruism', 'venue': 'Nature', 'venue_type': 'journal', 'journal': 'Nature', 'volume': '425', 'issue': '6960', 'pages': '785-791', 'doi': '10.1038/nature02043', 'openalex_id': None, 'pmid': None, 'citation_string': 'Fehr, E., & Fischbacher, U. (2003). The nature of human altruism. *Nature*, 425(6960), 785–791.', 'url': 'https://doi.org/10.1038/nature02043', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'Rand, D. G., & Nowak, M. A.', 'year': 2013, 'title': 'Human cooperation', 'venue': 'Trends in Cognitive Sciences', 'venue_type': 'journal', 'journal': 'Trends in Cognitive Sciences', 'volume': '17', 'issue': '8', 'pages': '413-425', 'doi': '10.1016/j.tics.2013.06.003', 'openalex_id': None, 'pmid': None, 'citation_string': 'Rand, D. G., & Nowak, M. A. (2013). Human cooperation. *Trends in Cognitive Sciences*, 17(8), 413–425.', 'url': 'https://doi.org/10.1016/j.tics.2013.06.003', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Engel, C., & Zhurakhovska, L.', 'year': 2016, 'title': 'When is the risk of cooperation worth taking? The prisoner’s dilemma as a game of multiple motives', 'venue': 'Applied Economics Letters', 'venue_type': 'journal', 'journal': 'Applied Economics Letters', 'volume': '23', 'issue': '16', 'pages': '1157-1161', 'doi': '10.1080/13504851.2016.1139672', 'openalex_id': None, 'pmid': None, 'citation_string': "Engel, C., & Zhurakhovska, L. (2016). When is the risk of cooperation worth taking? The prisoner's dilemma as a game of multiple motives. *Applied Economics Letters*, 23(16), 1157–1161.", 'url': 'https://doi.org/10.1080/13504851.2016.1139672', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Declerck, C. H., Boone, C., & Emonds, G.', 'year': 2013, 'title': 'When do people cooperate? The neuroeconomics of prosocial decision making', 'venue': 'Brain and Cognition', 'venue_type': 'journal', 'journal': 'Brain and Cognition', 'volume': '81', 'issue': '1', 'pages': '95-117', 'doi': '10.1016/j.bandc.2012.09.009', 'openalex_id': None, 'pmid': None, 'citation_string': 'Declerck, C. H., Boone, C., & Emonds, G. (2013). When do people cooperate? The neuroeconomics of prosocial decision making. *Brain and Cognition*, 81(1), 95–117.', 'url': 'https://doi.org/10.1016/j.bandc.2012.09.009', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Peysakhovich, A., Nowak, M. A., & Rand, D. G.', 'year': 2014, 'title': 'Humans display a ‘cooperative phenotype’ that is domain general and temporally stable', 'venue': 'Nature Communications', 'venue_type': 'journal', 'journal': 'Nature Communications', 'volume': '5', 'issue': '1', 'pages': None, 'doi': '10.1038/ncomms5939', 'openalex_id': None, 'pmid': None, 'citation_string': "Peysakhovich, A., Nowak, M. A., & Rand, D. G. (2014). Humans display a 'cooperative phenotype' that is domain general and temporally stable. *Nature Communications*, 5, 4939.", 'url': 'https://doi.org/10.1038/ncomms5939', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [prisoner's dilemma (PD)](https://www.cognitiveatlas.org/task/id/tsk_KRl3zbyaJcKWM)
