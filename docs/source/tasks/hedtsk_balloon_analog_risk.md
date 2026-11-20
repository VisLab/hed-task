(hedtsk_balloon_analog_risk)=
# Balloon Analog Risk Task

**HED task ID:** `hedtsk_balloon_analog_risk`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** BART, Balloon Task, Balloon Analog Risk

Sequential pumping of a virtual balloon for monetary reward with stochastic popping; average pumps per un-popped balloon indexes risk-taking.

## Description

Participants inflate a virtual balloon by clicking a pump button, earning money with each pump. The balloon may explode at any point, causing loss of all accumulated earnings for that trial. Participants can cash out at any time to save their earnings. The average number of pumps before cashing out indexes risk-taking propensity. BART risk-taking correlates with real-world risky behaviors. fMRI reveals activation in ventromedial PFC, anterior insula, and striatal regions during risk assessment.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-outcomes">choose for outcomes</a>
- **What are the options?** <a href="vocabulary.html#rule-choose-for-outcomes-option-set-one-option-with-stop">one option with stop</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-reward-goal">reward goal</a>
- **Can the player gain, lose, or both?** <a href="vocabulary.html#motivation-sign-both">both</a>
- **What earns the outcome?** <a href="vocabulary.html#motivation-earned-by-choice">choice</a>
- **What is the outcome?** <a href="vocabulary.html#motivation-what-money">money</a>
- **Is the outcome real?** <a href="vocabulary.html#motivation-real-paid">paid</a>, <a href="vocabulary.html#motivation-real-hypothetical">hypothetical</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>, <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Feedback:** <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-trials">number of trials</a>, <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>, <a href="vocabulary.html#setting-reward-probability">reward probability</a>
- **Material:** A virtual balloon that grows with each pump and may pop, with the money earned on the trial shown.

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
    - Pump decision (committed in advance vs. during inflation)
    - Outcome domain (loss vs. gain)
* - **Measurements**
  - - Adjusted average pumps on un-popped balloons (risk-taking index)
    - Total earnings
    - Pump-by-pump decision sequences
    - Response rate across trial segments
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
* - BART-Y (Youth Version)

    `hedvar_balloon_analog_risk__bart_y_youth_version`
  - population: <a href="vocabulary.html#facet-population-children">children</a>, <a href="vocabulary.html#facet-population-adolescents">adolescents</a>
  - -
  - A named children's instrument with points toward a prize, a simpler display and a progress meter; the pump-or-collect decision is unchanged.
* - Variable Explosion Probability

    `hedvar_balloon_analog_risk__variable_explosion_probability`
  - contingency cue: <a href="vocabulary.html#rule-choose-for-outcomes-contingency-cue-per-trial-cue">per trial cue</a>
  - [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
  - Balloon color signals which hidden pop schedule applies, so the participant learns within the session which colors are risky.
* - Social Context BART

    `hedvar_balloon_analog_risk__social_context_bart`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-being-observed">being observed</a>
  - -
  - The participant plays while observed, or sees how other people pumped, instead of playing alone.
* - BART with Loss Domain

    `hedvar_balloon_analog_risk__bart_with_loss_domain`
  - sign: <a href="vocabulary.html#motivation-sign-loss">loss</a>
  - [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation)
  - Each balloon starts full of money and every pump removes some while raising the chance of a larger loss, so the same pump-or-stop structure is framed as accepting loss rather than chasing gain.
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

- Pleskac, T. J. (2008). Decision making and learning while taking sequential risks. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 34(1), 167-185. ([DOI](https://doi.org/10.1037/0278-7393.34.1.167), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18194061/))
- Wallsten, T. S., Pleskac, T. J., & Lejuez, C. W. (2005). Modeling behavior in a clinically diagnostic sequential risk-taking task. *Psychological Review*, 112(4), 862-880. ([DOI](https://doi.org/10.1037/0033-295x.112.4.862), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16262471/))
- Hunt, M. K., Hopko, D. R., Bare, R., Lejuez, C. W., & Robinson, E. V. (2005). Construct validity of the Balloon Analog Risk Task (BART). *Assessment*, 12(4), 416-428. ([DOI](https://doi.org/10.1177/1073191105278740), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16244122/))

## External links

- Cognitive Atlas: [balloon analogue risk task](https://www.cognitiveatlas.org/task/id/trm_4d559bcd67c18)

