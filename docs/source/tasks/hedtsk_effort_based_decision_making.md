(hedtsk_effort_based_decision_making)=
# Effort-Based Decision-Making Task

**HED task ID:** `hedtsk_effort_based_decision_making`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** EEfRT, Effort Expenditure for Rewards Task, Effort Discounting Task, Effort-Cost Paradigm, Effort Choice Task

Participants choose between a low-effort/low-reward option and a high-effort/high-reward option on each trial; the indifference point indexes effort discounting and motivational willingness to exert effort for reward.

## Description

Effort-based decision-making tasks measure the willingness to exert physical or cognitive effort in exchange for reward. In the Effort Expenditure for Rewards Task (EEfRT; Treadway et al., 2009), participants on each trial choose between an easy task (e.g., pressing a button with the dominant index finger 30 times in 7 seconds for a small reward) and a hard task (pressing with the non-dominant pinky finger 100 times in 21 seconds for a larger, variable reward). Reward magnitude and probability are manipulated across trials to map the effort-reward tradeoff. The proportion of hard-task choices is the primary measure, indexing motivational drive. Effort discounting variants (Botvinick, Huffstetler, & McGuire, 2009) use a titration procedure to find the reward value at which effortful and easy options are equally preferred (the indifference point). The paradigm has become central to research on motivational anhedonia - the reduced willingness to exert effort for reward that characterizes depression, schizophrenia, and Parkinson's disease. Computational models decompose behavior into effort sensitivity, reward sensitivity, and probability weighting parameters. The framework connects to dopaminergic theories of motivation: effort willingness is modulated by dopamine function in the ventral striatum and anterior cingulate cortex.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-choose-for-payoff">Choose for a payoff</a> (`choose_for_payoff`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What are the options?* <a href="vocabulary.html#rule-choose-for-payoff-option-set-two-described">two described</a>
  - *How does the player learn what pays?* <a href="vocabulary.html#rule-choose-for-payoff-outcome-knowledge-described">described</a>
  - *What is traded against what?* <a href="vocabulary.html#rule-choose-for-payoff-tradeoff-amount-vs-effort">amount vs effort</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-goal">reward goal</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-gain">gain</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-choice">choice</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-money">money</a>, <a href="vocabulary.html#motivator-what-effort-cost">effort cost</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>, <a href="vocabulary.html#setting-reward-probability">reward probability</a>
- **Material:** Pairs of offers, an easy task for a small reward against a hard task (such as 100 button presses) for a larger reward of stated probability.
- **Combined with:** <a href="vocabulary.html#how-chained">chained</a>, <a href="vocabulary.html#game-produce-movement">produce movement</a> (The effort task chosen is carried out after each choice)

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. On each trial, participants choose between a low-effort/low-reward option and a high-effort/high-reward option, then execute the chosen action.
    2. Trials vary reward magnitude and probability.
* - **Manipulations**
  - - Reward magnitude (small vs. large)
    - Reward probability (high vs. low)
    - Effort demand level (physical vs. cognitive; graded difficulty)
    - Effort type (button pressing, grip force, N-back)
    - Block structure (fixed vs. adaptive staircase)
    - Effort schedule (progressive ratio vs. two-offer choice)
    - Reward (none vs. paid)
    - Choice structure (patch leaving with diminishing returns)
* - **Measurements**
  - - Proportion of high-effort choices
    - Effort indifference point (reward at which hard and easy options are equally chosen)
    - RT for choice
    - Completion rate on hard trials
    - Computational model parameters (effort sensitivity, reward sensitivity, probability weighting)
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
* - Cognitive Effort Discounting

    `hedvar_effort_based_decision_making__cognitive_effort_discounting`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
  - The effort is a level of the n-back task, experienced beforehand, rather than a bout of button pressing, and the amount offered for the easy option is adjusted until the participant is indifferent.
* - Grip-Force Effort Task

    `hedvar_effort_based_decision_making__grip_force_effort`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-grip-force-device">grip force device</a>
  - -
  - The effort is a hand-grip squeeze at a stated share of the participant's maximum, accepted or rejected offer by offer or chosen between offers.
* - Effort Discounting Titration

    `hedvar_effort_based_decision_making__effort_discounting_titration`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - -
  - For each effort level the easy-option reward is adjusted after each choice until the participant is indifferent.
* - Progressive Ratio Task

    `hedvar_effort_based_decision_making__progressive_ratio`
  - option set: <a href="vocabulary.html#rule-choose-for-payoff-option-set-one-option-with-stop">one option with stop</a>
  - -
  - The two-offer choice is replaced by a single escalating response requirement that the participant may abandon at any time; the breakpoint is the measure.
* - Demand Selection Task

    `hedvar_effort_based_decision_making__demand_selection`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>; option set: <a href="vocabulary.html#rule-choose-for-payoff-option-set-k-hidden-outcome">k hidden outcome</a>; outcome knowledge: <a href="vocabulary.html#rule-choose-for-payoff-outcome-knowledge-experienced">experienced</a>; sign: <a href="vocabulary.html#motivator-sign-loss">loss</a>; what: <a href="vocabulary.html#motivator-what-effort-cost">effort cost</a>; drive: <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
  - -
  - Two unlabeled options lead to the same kind of task, differing only in how often the task switches; nothing is paid and the difference is learned by experience, so the choice weighs effort alone.
* - Apple-Gathering Task

    `hedvar_effort_based_decision_making__apple_gathering`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>; option set: <a href="vocabulary.html#rule-choose-for-payoff-option-set-one-option-with-stop">one option with stop</a>; outcome knowledge: <a href="vocabulary.html#rule-choose-for-payoff-outcome-knowledge-experienced">experienced</a>
  - -
  - A foraging structure in which each press on a tree yields fewer apples than the last and the participant decides when to leave for the next tree at a travel-time cost, so the choice is stay-or-leave with experienced diminishing returns.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Effort allocation](../processes/reward_anticipation_and_motivation.md#hed-effort-allocation)
- [Valuation](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-valuation)
- [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making)

## Key references

- Treadway, M. T., Buckholtz, J. W., Schwartzman, A. N., Lambert, W. E., & Zald, D. H. (2009). Worth the 'EEfRT'? The Effort Expenditure for Rewards Task as an objective measure of motivation and anhedonia. *PLoS ONE*, 4(8), e6598. ([DOI](https://doi.org/10.1371/journal.pone.0006598), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19672310/))
- Botvinick, M. M., Huffstetler, S., & McGuire, J. T. (2009). Effort discounting in human nucleus accumbens. *Cognitive, Affective, & Behavioral Neuroscience*, 9(1), 16-27. ([DOI](https://doi.org/10.3758/cabn.9.1.16), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19246324/))
- Westbrook, A., & Braver, T. S. (2015). Cognitive effort: A neuroeconomic approach. *Cognitive, Affective, & Behavioral Neuroscience*, 15(2), 395-415. ([DOI](https://doi.org/10.3758/s13415-015-0334-y), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25673005/))

## Further references

- Chong, T. T.-J., Bonnelle, V., Manohar, S., et al. (2015). Dopamine enhances willingness to exert effort for reward in Parkinson's disease. *Cortex*, 69, 40-46. ([DOI](https://doi.org/10.1016/j.cortex.2015.04.003))
- Reddy, L. F., Horan, W. P., Barch, D. M., Buchanan, R. W., et al. (2015). Effort-Based Decision-Making Paradigms for Clinical Trials in Schizophrenia: Part 1 - Psychometric Characteristics of 5 Paradigms. *Schizophrenia Bulletin*, 41(5), 1045-1054. ([DOI](https://doi.org/10.1093/schbul/sbv089), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26142081/))
- Husain, M., & Roiser, J. P. (2018). Neuroscience of apathy and anhedonia: a transdiagnostic approach. *Nature Reviews Neuroscience*, 19(3), 164-178. ([DOI](https://doi.org/10.1038/s41583-018-0029-9), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29946157/))
- Lopez-Gamundi, P., Yao, Y.-W., Chong, T. T.-J., Heekeren, H. R., Mas-Herrero, E., & Marco-Pallares, J. (2021). The neural basis of effort valuation: A meta-analysis of functional magnetic resonance imaging studies. *Neuroscience & Biobehavioral Reviews*, 131, 1275-1287. ([DOI](https://doi.org/10.1016/j.neubiorev.2021.10.024), [PubMed](https://pubmed.ncbi.nlm.nih.gov/34710515/))

