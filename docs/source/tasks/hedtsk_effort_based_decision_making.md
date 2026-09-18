(hedtsk_effort_based_decision_making)=
# Effort-Based Decision-Making Task

**HED task ID:** `hedtsk_effort_based_decision_making`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** EEfRT, Effort Expenditure for Rewards Task, Effort Discounting Task, Effort-Cost Paradigm, Effort Choice Task

Participants choose between a low-effort/low-reward option and a high-effort/high-reward option on each trial; the indifference point indexes effort discounting and motivational willingness to exert effort for reward.

## Description

Effort-based decision-making tasks measure the willingness to exert physical or cognitive effort in exchange for reward. In the Effort Expenditure for Rewards Task (EEfRT; Treadway et al., 2009), participants on each trial choose between an easy task (e.g., pressing a button with the dominant index finger 30 times in 7 seconds for a small reward) and a hard task (pressing with the non-dominant pinky finger 100 times in 21 seconds for a larger, variable reward). Reward magnitude and probability are manipulated across trials to map the effort-reward tradeoff. The proportion of hard-task choices is the primary measure, indexing motivational drive. Effort discounting variants (Botvinick, Huffstetler, & McGuire, 2009) use a titration procedure to find the reward value at which effortful and easy options are equally preferred (the indifference point). The paradigm has become central to research on motivational anhedonia — the reduced willingness to exert effort for reward that characterizes depression, schizophrenia, and Parkinson's disease. Computational models decompose behavior into effort sensitivity, reward sensitivity, and probability weighting parameters. The framework connects to dopaminergic theories of motivation: effort willingness is modulated by dopamine function in the ventral striatum and anterior cingulate cortex.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - On each trial, participants choose between a low-effort/low-reward option and a high-effort/high-reward option, then execute the chosen action; trials vary reward magnitude and probability.
* - **Manipulation**
  - Reward magnitude (small vs. large); reward probability (high vs. low); effort demand level (physical vs. cognitive; graded difficulty); effort type (button pressing, grip force, N-back); block structure (fixed vs. adaptive staircase).
* - **Measurement**
  - Proportion of high-effort choices; effort indifference point (reward at which hard and easy options are equally chosen); RT for choice; completion rate on hard trials; computational model parameters (effort sensitivity, reward sensitivity, probability weighting).
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
* - EEfRT (Physical Effort)

    `hedvar_effort_based_decision_making__eefrt_physical_effort`
  - Treadway et al. (2009) paradigm: choose between easy (30 dominant-finger presses) and hard (100 pinky-finger presses) for variable reward and probability. The standard clinical paradigm for motivational anhedonia.
  - Canonical effort-reward task: grips vs. reward levels
* - Cognitive Effort Discounting

    `hedvar_effort_based_decision_making__cognitive_effort_discounting`
  - Choose between easy (e.g., 1-back) and hard (e.g., 3-back) cognitive tasks for different rewards. Westbrook et al. (2013). Indexes cognitive effort avoidance specifically.
  - Cognitive task difficulty vs. reward; different effort type
* - Grip-Force Effort Task

    `hedvar_effort_based_decision_making__grip_force_effort`
  - Choose between low and high grip-force requirements for varying rewards. Bonnelle et al. (2015). Continuous force measure enables parametric effort manipulation.
  - Graded grip force as effort measure; different motor requirement
* - Effort Discounting Titration

    `hedvar_effort_based_decision_making__effort_discounting_titration`
  - Staircase procedure adjusting reward until the participant is indifferent between easy and hard options. Yields a precise effort indifference point. Botvinick et al. (2009).
  - Adaptive titration of effort-reward indifference points; different method
* - Progressive Ratio Task

    `hedvar_effort_based_decision_making__progressive_ratio`
  - The number of responses required for reward increases across trials. The breakpoint (trial at which the participant stops responding) indexes maximum effort willingness.
  - Escalating effort requirement for each reward; different effort schedule
* - Demand Selection Task

    `hedvar_effort_based_decision_making__demand_selection`
  - Free choice between low-demand and high-demand task versions (Kool et al., 2010). Binary choice without explicit reward manipulation; indexes intrinsic effort avoidance.
  - Freely choose between high/low demand tasks; choice behavior reveals effort avoidance
* - Apple-Gathering Task

    `hedvar_effort_based_decision_making__apple_gathering`
  - Foraging paradigm: decide how many apples to pick from each tree before traveling to the next (effort = key presses, diminishing returns). Indexes vigor and willingness to sustain effort.
  - Virtual navigation effort for rewards; different effort modality (locomotion)
```

## Cognitive processes

This task is designed to engage the following processes:

- [Effort allocation](../processes/reward_anticipation_and_motivation.md#hed-effort-allocation)
- [Valuation](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-valuation)
- [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)

## Key references

- Treadway, M. T., Buckholtz, J. W., Schwartzman, A. N., Lambert, W. E., & Zald, D. H. (2009). Worth the 'EEfRT'? The Effort Expenditure for Rewards Task as an objective measure of motivation and anhedonia. *PLoS ONE*, 4(8), e6598.
- Botvinick, M. M., Huffstetler, S., & McGuire, J. T. (2009). Effort discounting in human nucleus accumbens. *Cognitive, Affective, & Behavioral Neuroscience*, 9(1), 16-27.
- Westbrook, A., & Braver, T. S. (2015). Cognitive effort: A neuroeconomic approach. *Cognitive, Affective, & Behavioral Neuroscience*, 15(2), 395-415.

## Recent references

- Chong, T. T.-J., Bonnelle, V., Manohar, S., et al. (2017). Dopamine enhances willingness to exert effort for reward in Parkinson's disease. *Cortex*, 69, 40-46.
- Reddy, L. F., Horan, W. P., Barch, D. M., Buchanan, R. W., et al. (2015). Effort-Based Decision-Making Paradigms for Clinical Trials in Schizophrenia: Part 1 — Psychometric Characteristics of 5 Paradigms. *Schizophrenia Bulletin*, 41(5), 1045-1054.
- Husain, M., & Roiser, J. P. (2018). Neuroscience of apathy and anhedonia: a transdiagnostic approach. *Nature Reviews Neuroscience*, 19(3), 164-178.
- Lopez-Gamundi, P., Yao, Y.-W., Chong, T. T.-J., Heekeren, H. R., Mas-Herrero, E., & Marco-Pallares, J. (2021). The neural basis of effort valuation: A meta-analysis of functional magnetic resonance imaging studies. *Neuroscience & Biobehavioral Reviews*, 131, 1275-1287.

