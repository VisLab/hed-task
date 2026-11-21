(hedtsk_delay_discounting)=
# Delay Discounting Task

**HED task ID:** `hedtsk_delay_discounting`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** Temporal Discounting, Delay of Gratification

Repeated choices between smaller-sooner and larger-later rewards at varying delays; indifference points estimate a temporal discount function.

## Description

Participants make repeated choices between a smaller immediate reward and a larger delayed reward (e.g., "$10 now or $25 in 1 week"). The immediate amount or delay is systematically varied to estimate indifference points, yielding a discount rate reflecting how steeply the subjective value of rewards declines with delay. Steeper discounting reflects greater impulsivity. fMRI reveals differential activation of ventromedial PFC and nucleus accumbens (immediate preference) versus dorsolateral PFC and posterior parietal cortex (delayed preference), supporting dual-system valuation models.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-payoff">Choose for a payoff</a> (`choose_for_payoff`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What are the options?* <a href="vocabulary.html#rule-choose-for-payoff-option-set-two-described">two described</a>
  - *How does the player learn what pays?* <a href="vocabulary.html#rule-choose-for-payoff-outcome-knowledge-described">described</a>
  - *What is traded against what?* <a href="vocabulary.html#rule-choose-for-payoff-tradeoff-amount-vs-delay">amount vs delay</a>
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
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>, <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-delay-to-outcome">delay to outcome</a>, <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>
- **Material:** Pairs of money offers, a smaller amount now against a larger amount after a delay (such as $10 now or $25 in 1 week).

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants choose between a smaller immediate reward and a larger delayed reward across many trials with varying amounts and delays.
* - **Manipulations**
  - - Reward magnitude
    - Delay duration
    - Ascending vs. descending adjustment procedures
    - Choice procedure (adjusting amount, adjusting delay, fixed list)
    - Real vs. hypothetical rewards
    - Delay type (experienced, waited out vs. described)
    - Outcome domain (gain vs. loss framing)
    - Reward uncertainty (probability vs. delay)
    - Reward type (money vs. other commodities)
* - **Measurements**
  - - Indifference point at each delay
    - Discount rate k (hyperbolic model)
    - Area under the discount curve (AUC)
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
* - 5-Trial Adjusting Delay

    `hedvar_delay_discounting__5_trial_adjusting_delay`

    Cognitive Atlas: [Five-Trial Adjusting Delay Discounting Task](https://www.cognitiveatlas.org/task/id/tsk_qBdQueJHSouuF)
  - named form
  - -
  - A named one-minute instrument that bisects the delay range in five fixed choices.
* - Fixed-Choice Discrete Trials

    `hedvar_delay_discounting__fixed_choice_discrete_trials`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - -
  - A fixed list of now-versus-later questions (for example the 27-item Monetary Choice Questionnaire) with no adjustment based on earlier answers.
* - Magnitude Manipulation

    `hedvar_delay_discounting__magnitude_manipulation`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - The whole procedure is run in separate blocks for small, medium and large reward magnitudes.
* - Experiential Discounting Task

    `hedvar_delay_discounting__experiential_discounting`
  - feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>; outcome knowledge: <a href="vocabulary.html#rule-choose-for-payoff-outcome-knowledge-experienced">experienced</a>
  - -
  - Delays are seconds to a minute and are actually waited out, with the reward delivered after each wait, so outcomes are experienced rather than only described.
* - Gain vs. Loss Framing

    `hedvar_delay_discounting__gain_vs_loss_framing`
  - sign: <a href="vocabulary.html#motivator-sign-both">both</a>
  - -
  - Choices between paying a smaller amount now or a larger amount later are added alongside the usual gain choices.
* - Probabilistic Discounting

    `hedvar_delay_discounting__probabilistic_discounting`
  - tradeoff: <a href="vocabulary.html#rule-choose-for-payoff-tradeoff-amount-vs-risk">amount vs risk</a>
  - [Risk processing](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-risk-processing)
  - The larger reward is uncertain rather than delayed, so the choice trades amount against probability instead of against delay.
* - Cross-Commodity Discounting

    `hedvar_delay_discounting__cross_commodity_discounting`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - -
  - The rewards are something other than money, or the two options are in different commodities, described in words.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Delay discounting](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-delay-discounting)
- [Intertemporal choice](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-intertemporal-choice)
- [Valuation](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-valuation)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)

## Key references

- McClure, S. M., Laibson, D. I., Loewenstein, G., & Cohen, J. D. (2004). Separate neural systems value immediate and delayed monetary rewards. *Science*, 306(5695), 503-507. ([DOI](https://doi.org/10.1126/science.1100907), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15486304/))
- Kable, J. W., & Glimcher, P. W. (2007). The neural correlates of subjective value during intertemporal choice. *Nature Neuroscience*, 10(12), 1625-1633. ([DOI](https://doi.org/10.1038/nn2007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17982449/))

## Further references

- Bickel, W. K., Koffarnus, M. N., Moody, L., & Wilson, A. G. (2014). The behavioral- and neuro-economic process of temporal discounting: A candidate behavioral marker of addiction. *Neuropharmacology*, 76, 518-527. ([DOI](https://doi.org/10.1016/j.neuropharm.2013.06.013), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23806805/))
- Kable, J. W. (2014). Valuation, intertemporal choice, and self-control. In *Neuroeconomics* (2nd ed., pp. 173-192). Academic Press. ([DOI](https://doi.org/10.1016/b978-0-12-416008-8.00010-3))
- Peters, J., & Büchel, C. (2011). The neural mechanisms of inter-temporal decision-making: Understanding variability. *Trends in Cognitive Sciences*, 15(5), 227-239. ([DOI](https://doi.org/10.1016/j.tics.2011.03.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21497544/))

## External links

- Cognitive Atlas: [temporal discounting task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949e98)

- CogPO: [Delay Discounting Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Delay_Discounting_Task_Paradigm)

