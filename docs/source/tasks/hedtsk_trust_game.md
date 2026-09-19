(hedtsk_trust_game)=
# Trust Game Task

**HED task ID:** `hedtsk_trust_game`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Trust Game, TG, Investment Game

Two-stage exchange in which an investor transfers a fraction of an endowment (multiplied on receipt), and a trustee returns some fraction; amounts transferred index trust and reciprocity.

## Description

A sequential two-player game in which the investor decides how much of an endowment to send to the trustee; the sent amount is multiplied (typically 3x), and the trustee decides how much to return. The investor faces a dilemma: trusting yields potentially higher mutual payoffs but risks exploitation. fMRI reveals that trust decisions engage theory-of-mind regions (medial PFC, temporoparietal junction) and reward regions (ventral striatum) that track mutual cooperation and reciprocity.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - An investor receives an endowment and chooses how much to send to a trustee; the amount is multiplied (typically tripled). The trustee decides how much to return to the investor.
* - **Manipulation**
  - Multiplication factor; endowment size; partner identity; reputation information; one-shot vs. repeated.
* - **Measurement**
  - Amount invested (trust); amount returned (trustworthiness); investment and return ratios.
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
* - Standard Two-Stage Trust Game

    `hedvar_trust_game__standard_two_stage_trust_game`
  - Investor sends, tripled, trustee returns portion.
  - Canonical Berg et al.: investor sends, trustee returns
* - One-Shot vs. Repeated

    `hedvar_trust_game__one_shot_vs_repeated`
  - Single interaction vs. multiple rounds with same partner.
  - Single vs. multiple rounds; repeated play enables reputation building
* - Multiplier Variation

    `hedvar_trust_game__multiplier_variation`
  - 2×, 3×, 4× multiplication factors.
  - Different multiplication factors; changes investment incentive
* - Trust Game with Reputation

    `hedvar_trust_game__trust_game_with_reputation`
  - Providing partner's history of returns.
  - Trustee reputation history visible; changes available social information
* - Partner Selection Trust Game

    `hedvar_trust_game__partner_selection_trust_game`
  - Choose which of several potential partners to trust.
  - Participant selects partner before trust game; adds partner choice
* - Anonymous vs. Face-to-Face

    `hedvar_trust_game__anonymous_vs_face_to_face`
  - Varying social presence.
  - Social identification manipulation changes accountability
* - Social Identity Manipulation

    `hedvar_trust_game__social_identity_manipulation`
  - In-group vs. out-group partners.
  - In-group vs. out-group trustee; tests trust as function of group membership
```

## Cognitive processes

This task is designed to engage the following processes:

- [Social decision making](../processes/social_cognition_and_strategic_social_choice.md#hed-social-decision-making)
- [Reciprocity](../processes/social_cognition_and_strategic_social_choice.md#hed-reciprocity)
- [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking)
- [Risk processing](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-risk-processing)
- [Cooperation](../processes/social_cognition_and_strategic_social_choice.md#hed-cooperation)

## Key references

- Berg, J., Dickhaut, J., & McCabe, K. (1995). Trust, reciprocity, and social history. *Games and Economic Behavior*, 10(1), 122-142. ([DOI](https://doi.org/10.1006/game.1995.1027))
- King-Casas, B., Tomlin, D., Anen, C., Camerer, C. F., Quartz, S. R., & Montague, P. R. (2005). Getting to know you: Reputation and trust in a two-person economic exchange. *Science*, 308(5718), 78-83. ([DOI](https://doi.org/10.1126/science.1108062), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15802598/))
- Rilling, J. K., Gutman, D. A., Zeh, T. R., Pagnoni, G., Berns, G. S., & Kilts, C. D. (2002). A neural basis for social cooperation. *Neuron*, 35(2), 395-405. ([DOI](https://doi.org/10.1016/s0896-6273(02)00755-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12160756/))

## Further references

- Johnson, N. D., & Mislin, A. A. (2011). Trust games: A meta-analysis. *Journal of Economic Psychology*, 32(5), 865–889. ([DOI](https://doi.org/10.1016/j.joep.2011.05.007))
- Bellucci, G., Chernyak, S. V., Goodyear, K., Eickhoff, S. B., & Krueger, F. (2017). Neural signatures of trust in reciprocity: A coordinate-based meta-analysis. *Human Brain Mapping*, 38(3), 1233–1248. ([DOI](https://doi.org/10.1002/hbm.23854), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29064617/))
- Krueger, F., & Meyer-Lindenberg, A. (2019). Toward a model of interpersonal trust drawn from neuroscience, psychology, and economics. *Trends in Neurosciences*, 42(2), 92–101. ([DOI](https://doi.org/10.1016/j.tins.2018.10.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30482606/))
- Chang, L. J., Doll, B. B., van't Wout, M., Frank, M. J., & Sanfey, A. G. (2010). Seeing is believing: Trustworthiness as a dynamic belief. *Cognitive Psychology*, 61(2), 87–105. ([DOI](https://doi.org/10.1016/j.cogpsych.2010.03.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20553763/))

## External links

- Cognitive Atlas: [Trust game (TG)](https://www.cognitiveatlas.org/task/id/tsk_uzol7erTzr9Ix)

