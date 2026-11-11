(hedtsk_delay_discounting)=
# Delay Discounting Task

**HED task ID:** `hedtsk_delay_discounting`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** Temporal Discounting, Delay of Gratification

Repeated choices between smaller-sooner and larger-later rewards at varying delays; indifference points estimate a temporal discount function.

## Description

Participants make repeated choices between a smaller immediate reward and a larger delayed reward (e.g., "$10 now or $25 in 1 week"). The immediate amount or delay is systematically varied to estimate indifference points, yielding a discount rate reflecting how steeply the subjective value of rewards declines with delay. Steeper discounting reflects greater impulsivity. fMRI reveals differential activation of ventromedial PFC and nucleus accumbens (immediate preference) versus dorsolateral PFC and posterior parietal cortex (delayed preference), supporting dual-system valuation models.

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
* - **Measurements**
  - - Indifference point at each delay
    - Discount rate k (hyperbolic model)
    - Area under the discount curve (AUC)
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
* - Adjusting-Amount Method

    `hedvar_delay_discounting__adjusting_amount_method`
  - For each delay (for example one week, one month, one year) the participant repeatedly chooses between a smaller amount now and a fixed larger amount later. The immediate amount is raised or lowered after each choice until the participant is indifferent. That amount is the present value of the delayed reward.
  - Adjusts smaller-sooner amount until indifferent; adaptive titration procedure
* - Adjusting-Delay Method

    `hedvar_delay_discounting__adjusting_delay_method`
  - The two amounts are fixed, and it is the waiting time for the larger amount that is adjusted after each choice until the participant is indifferent between the two options.
  - Adjusts delay until indifferent; different dimension titrated
* - 5-Trial Adjusting Delay

    `hedvar_delay_discounting__5_trial_adjusting_delay`

    Cognitive Atlas: [Five-Trial Adjusting Delay Discounting Task](https://www.cognitiveatlas.org/task/id/tsk_qBdQueJHSouuF)
  - A very short version that finds the delay at which a reward loses half its value in just five choices, each halving the range of possible delays. It takes about a minute.
  - Rapid 5-trial protocol; distinct abbreviated titration method
* - Fixed-Choice Discrete Trials

    `hedvar_delay_discounting__fixed_choice_discrete_trials`
  - The participant answers a fixed list of now-versus-later questions, such as the 27-item Monetary Choice Questionnaire, with no adjustment based on earlier answers. The pattern of choices is fitted afterwards to estimate the discount rate.
  - Fixed set of choices without adaptation; different decision structure
* - Magnitude Manipulation

    `hedvar_delay_discounting__magnitude_manipulation`
  - The whole procedure is run separately for small, medium and large rewards (for example 10, 100 and 1000 dollars). Larger amounts are usually discounted less steeply.
  - Systematically varies reward magnitude; tests magnitude effect on discounting
* - Real vs. Hypothetical Rewards

    `hedvar_delay_discounting__real_vs_hypothetical_rewards`
  - In the real version one of the participant's choices is selected and paid for real, including the actual wait for a delayed reward. In the hypothetical version the participant imagines the choices and nothing is paid.
  - Real monetary payoff vs. hypothetical; changes incentive structure and motivation
* - Experiential Discounting Task

    `hedvar_delay_discounting__experiential_discounting`
  - The delays are short (seconds to a minute) and are actually waited out during the session, with the reward delivered at the end of each wait, rather than being described in words and imagined.
  - Delays experienced in real time; different temporal structure from verbal/hypothetical
* - Gain vs. Loss Framing

    `hedvar_delay_discounting__gain_vs_loss_framing`
  - Alongside the usual choices between gains, the participant chooses between paying a smaller amount now or a larger amount later. Delayed losses are usually discounted less steeply than delayed gains.
  - Loss domain discounting; different valence changes decision context
* - Probabilistic Discounting

    `hedvar_delay_discounting__probabilistic_discounting`
  - The larger reward is uncertain rather than delayed: the participant chooses between a smaller sure amount and a larger amount with some probability. The same adjusting procedures find the probability at which the two are equal.
  - Reward probability instead of delay; tests probability rather than temporal discounting
* - Cross-Commodity Discounting

    `hedvar_delay_discounting__cross_commodity_discounting`
  - The rewards are something other than money, such as food, a drug of abuse, or time with friends, or the two options are in different commodities. Shows whether the discount rate depends on what is being delayed.
  - Non-monetary rewards (food, drugs); different commodity changes motivational basis
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

