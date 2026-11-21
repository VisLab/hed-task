(hedtsk_trust_game)=
# Trust Game Task

**HED task ID:** `hedtsk_trust_game`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Trust Game, TG, Investment Game

Two-stage exchange in which an investor transfers a fraction of an endowment (multiplied on receipt), and a trustee returns some fraction; amounts transferred index trust and reciprocity.

## Description

A sequential two-player game in which the investor decides how much of an endowment to send to the trustee; the sent amount is multiplied (typically 3x), and the trustee decides how much to return. The investor faces a dilemma: trusting yields potentially higher mutual payoffs but risks exploitation. fMRI reveals that trust decisions engage theory-of-mind regions (medial PFC, temporoparietal junction) and reward regions (ventral striatum) that track mutual cooperation and reciprocity.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-interact-with-agent">Play against another player</a> (`interact_with_agent`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *Is what is sent changed on the way?* <a href="vocabulary.html#rule-interact-with-agent-transfer-transformation-multiplied">multiplied</a>
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
- **Settings:** <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>
- **Material:** An endowment of money, the amount sent (multiplied, typically tripled) and the amount returned.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. An investor receives an endowment and chooses how much to send to a trustee.
    2. The amount is multiplied (typically tripled).
    3. The trustee decides how much to return to the investor.
* - **Manipulations**
  - - Multiplication factor
    - Endowment size
    - Partner identity
    - Reputation information
    - One-shot vs. repeated
* - **Measurements**
  - - Amount invested (trust)
    - Amount returned (trustworthiness)
    - Investment and return ratios
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
* - One-Shot vs. Repeated

    `hedvar_trust_game__one_shot_vs_repeated`
  - feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>; repetition: <a href="vocabulary.html#rule-interact-with-agent-repetition-iterated">iterated</a>
  - -
  - The exchange is repeated with the same partner over several rounds with each return shown, rather than played once with a stranger.
* - Partner Selection Trust Game

    `hedvar_trust_game__partner_selection_trust_game`
  - named form
  - -
  - The investor first chooses which of several possible trustees to play with, from information about them, and then plays the usual game.
* - Anonymous vs. Face-to-Face

    `hedvar_trust_game__anonymous_vs_face_to_face`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>, <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - -
  - Players either learn nothing about each other or meet, see a photograph or interact over video before playing.
* - Social Identity Manipulation

    `hedvar_trust_game__social_identity_manipulation`
  - named form
  - [In-group/out-group processing](../processes/social_cognition_and_strategic_social_choice.md#hed-in-group-out-group-processing)
  - The investor is told the trustee is an in-group or an out-group member and transfers to the two are compared.
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

- Johnson, N. D., & Mislin, A. A. (2011). Trust games: A meta-analysis. *Journal of Economic Psychology*, 32(5), 865-889. ([DOI](https://doi.org/10.1016/j.joep.2011.05.007))
- Bellucci, G., Chernyak, S. V., Goodyear, K., Eickhoff, S. B., & Krueger, F. (2017). Neural signatures of trust in reciprocity: A coordinate-based meta-analysis. *Human Brain Mapping*, 38(3), 1233-1248. ([DOI](https://doi.org/10.1002/hbm.23451))
- Krueger, F., & Meyer-Lindenberg, A. (2019). Toward a model of interpersonal trust drawn from neuroscience, psychology, and economics. *Trends in Neurosciences*, 42(2), 92-101. ([DOI](https://doi.org/10.1016/j.tins.2018.10.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30482606/))
- Chang, L. J., Doll, B. B., van't Wout, M., Frank, M. J., & Sanfey, A. G. (2010). Seeing is believing: Trustworthiness as a dynamic belief. *Cognitive Psychology*, 61(2), 87-105. ([DOI](https://doi.org/10.1016/j.cogpsych.2010.03.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20553763/))

## External links

- Cognitive Atlas: [Trust game (TG)](https://www.cognitiveatlas.org/task/id/tsk_uzol7erTzr9Ix)

