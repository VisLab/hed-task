(hedtsk_balloon_analog_risk)=
# Balloon Analog Risk Task

**HED task ID:** `hedtsk_balloon_analog_risk`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** BART, Balloon Task, Balloon Analog Risk

Sequential pumping of a virtual balloon for monetary reward with stochastic popping; average pumps per un-popped balloon indexes risk-taking.

## Description

Participants inflate a virtual balloon by clicking a pump button, earning money with each pump. The balloon may explode at any point, causing loss of all accumulated earnings for that trial. Participants can cash out at any time to save their earnings. The average number of pumps before cashing out indexes risk-taking propensity. BART risk-taking correlates with real-world risky behaviors. fMRI reveals activation in ventromedial PFC, anterior insula, and striatal regions during risk assessment.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants sequentially pump a virtual balloon for incremental monetary reward.
    2. Each pump risks the balloon popping and losing that trial's earnings.
    3. They can stop and bank at any time.
* - **Manipulations**
  - - Explosion probability function (risk schedule)
    - Reward per pump
    - Number of trials
* - **Measurements**
  - - Adjusted average pumps on un-popped balloons (risk-taking index)
    - Total earnings
    - Pump-by-pump decision sequences
    - Response rate across trial segments
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
* - Standard BART (30 balloons)

    `hedvar_balloon_analog_risk__standard_bart_30_balloons`
  - Pump button inflates balloon with increasing explosion probability.
  - Canonical BART: pump balloon for accumulating reward, risk of explosion
* - BART-Y (Youth Version)

    `hedvar_balloon_analog_risk__bart_y_youth_version`
  - Simplified point system for children/adolescents.
  - Modified pumping interface and simplified feedback for youth; procedure adapted per §5.3
* - Variable Explosion Probability

    `hedvar_balloon_analog_risk__variable_explosion_probability`
  - Different explosion point distributions (uniform, normal, skewed).
  - Explicitly communicated explosion probabilities; changes decision-making structure
* - High-Stakes vs. Low-Stakes

    `hedvar_balloon_analog_risk__high_stakes_vs_low_stakes`
  - Varying reward amounts per pump.
  - Reward magnitude manipulation changes risk-reward trade-off context
* - Social Context BART

    `hedvar_balloon_analog_risk__social_context_bart`
  - Playing in observed vs. private conditions.
  - Observer or peer performance information present; changes social decision-making context
* - Automatic BART

    `hedvar_balloon_analog_risk__automatic_bart`
  - Participant selects desired number of pumps in advance; eliminates sequential decision-making.
  - Balloon pumps automatically; removes active pumping decision, isolates risk tolerance
* - BART with Loss Domain

    `hedvar_balloon_analog_risk__bart_with_loss_domain`
  - Starting with balloon value that decreases with each pump; loss-frame analog.
  - Losses instead of gains; loss framing changes motivational structure of decisions
```

## Cognitive processes

This task is designed to engage the following processes:

- [Risk processing](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-risk-processing)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)
- [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)

## Key references

- Lejuez, C. W., Read, J. P., Kahler, C. W., et al. (2002). Evaluation of a behavioral measure of risk taking: The Balloon Analogue Risk Task (BART). *Journal of Experimental Psychology: Applied*, 8(2), 75-84. ([DOI](https://doi.org/10.1037/1076-898x.8.2.75), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12075692/))
- Rao, H., Korczykowski, M., Pluta, J., Hoang, A., & Detre, J. A. (2008). Neural correlates of voluntary and involuntary risk taking in the human brain. *NeuroImage*, 42(2), 902-910. ([DOI](https://doi.org/10.1016/j.neuroimage.2008.05.046), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18582578/))
- Schonberg, T., Fox, C. R., & Poldrack, R. A. (2011). Mind the gap: Bridging economic and naturalistic risk-taking with cognitive neuroscience. *Trends in Cognitive Sciences*, 15(1), 11-19. ([DOI](https://doi.org/10.1016/j.tics.2010.10.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21130018/))

## Further references

- Pleskac, T. J. (2008). Decision making and learning while taking sequential risks. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 34(1), 167–185. ([DOI](https://doi.org/10.1037/0278-7393.34.1.167), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18194061/))
- Wallsten, T. S., Pleskac, T. J., & Lejuez, C. W. (2005). Modeling behavior in a clinically diagnostic sequential risk-taking task. *Psychological Review*, 112(4), 862–880. ([DOI](https://doi.org/10.1037/0033-295x.112.4.862), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16262471/))
- Hunt, M. K., Hopko, D. R., Bare, R., Lejuez, C. W., & Robinson, E. V. (2005). Construct validity of the Balloon Analog Risk Task (BART). *Assessment*, 12(4), 416–428. ([DOI](https://doi.org/10.1177/1073191105278740), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16244122/))

## External links

- Cognitive Atlas: [balloon analogue risk task](https://www.cognitiveatlas.org/task/id/trm_4d559bcd67c18)

