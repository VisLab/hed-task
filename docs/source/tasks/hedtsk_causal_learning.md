(hedtsk_causal_learning)=
# Causal Learning Task

**HED task ID:** `hedtsk_causal_learning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Contingency Judgment Task, Contingency Learning Task, Causal Judgment Task, Causal Induction Task, Delta-P Task, Allergy Prediction Task

Participants observe cue-outcome pairings across trials and judge the causal strength of the relationship; judgment profiles across contingency conditions index causal induction and associative learning mechanisms.

## Description

Causal learning tasks measure how people acquire and represent causal relationships from observed co-occurrences. In the standard contingency judgment paradigm, participants observe a series of trials in which a candidate cause (e.g., a food, a medicine, a button press) is either present or absent and an outcome (e.g., an allergic reaction, a health improvement, a light turning on) either occurs or does not. After observing multiple trials, participants rate the causal strength of the relationship (typically -100 to +100 or 0 to 100). The normative benchmark is delta-P (P(outcome|cause) - P(outcome|no cause)), but human judgments systematically deviate: they are sensitive to outcome density, show cue competition effects (blocking, overshadowing), and are influenced by prior causal beliefs. Associative models (Rescorla-Wagner) and statistical models (causal power; Cheng, 1997) compete to explain these patterns. The paradigm bridges associative learning, causal reasoning, and Bayesian inference literatures. It is the human analogue of animal conditioning studies and is foundational for understanding how people learn cause-effect relationships in medicine, engineering, and everyday reasoning.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants observe a series of trials presenting the presence/absence of candidate causes and occurrence/non-occurrence of outcomes, then judge the causal strength of cause-outcome relationships.
* - **Manipulations**
  - - Contingency (delta-P value: positive, zero, negative)
    - Outcome base rate (common vs. rare outcomes)
    - Cue competition (blocking, overshadowing, relative validity)
    - Number of trials
    - Trial-by-trial vs. summary presentation
    - Number of candidate causes
    - Temporal contiguity between cause and outcome
* - **Measurements**
  - - Causal strength ratings
    - Trial-by-trial prediction accuracy
    - Judgment latency
    - Sensitivity to contingency components (P(O|C) and P(O|~C) separately)
    - Blocking magnitude
    - Correspondence between judgments and normative models (delta-P, causal power, Rescorla-Wagner)
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
* - Allergy Prediction Task

    `hedvar_causal_learning__allergy_prediction`
  - On each trial the participant sees which foods a fictional patient ate and then learns whether the patient had an allergic reaction. After many trials they rate how strongly each food causes the reaction. The most common framing for contingency learning.
  - Canonical food-allergy prediction: participant judges cause-effect contingencies
* - Blocking Paradigm

    `hedvar_causal_learning__blocking_paradigm`
  - First one cue (such as a food) is paired with the outcome on its own. Then that cue and a new cue are presented together with the outcome. The new cue receives low causal ratings because the outcome was already explained.
  - Pre-training on one cue blocks learning about second cue; distinct compound conditioning procedure
* - Outcome Density Manipulation

    `hedvar_causal_learning__outcome_density_manipulation`
  - How often the outcome occurs overall is varied while the actual relationship between cue and outcome is held at zero. When the outcome is common, participants rate the cue as causal even though it makes no difference.
  - Systematically varies base rate of outcomes; changes the statistical environment
* - Trial-by-Trial Prediction

    `hedvar_causal_learning__trial_by_trial_prediction`
  - Before seeing each trial's outcome, the participant predicts whether it will occur. The sequence of predictions tracks learning as it happens, in addition to any rating at the end.
  - Participant predicts on each trial before feedback; different response requirement from summary judgment
* - Summary vs. Sequential Presentation

    `hedvar_causal_learning__summary_vs_sequential_presentation`
  - In the summary version the counts of all four combinations (cue present or absent, outcome present or absent) are shown at once in a table and the participant rates the causal link from it. In the sequential version the same information arrives one trial at a time.
  - Summary table vs. trial-by-trial presentation; changes information format and cognitive demand
* - Multi-Cause (Relative Validity)

    `hedvar_causal_learning__multi_cause_relative_validity`
  - Several candidate causes appear in different combinations, some of which predict the outcome perfectly while others predict it only partially. The partially predictive cue receives lower ratings when a perfect predictor is present than when it is not.
  - Multiple competing cues; relative validity procedure changes causal inference structure
* - Causal Direction Manipulation

    `hedvar_causal_learning__causal_direction_manipulation`
  - The same trials are presented but the participant is asked either to predict the effect from the cause (does this food cause the reaction?) or to diagnose the cause from the effect (given the reaction, which food was eaten?).
  - Manipulates whether participant judges cause->effect or effect->cause; different reasoning direction
* - Backward Blocking / Retrospective Revaluation

    `hedvar_causal_learning__backward_blocking_retrospective_revaluation`
  - Two cues are first presented together with the outcome. Then one of them is presented alone with the outcome. Ratings for the other cue, which was never presented again, drop, showing that earlier learning was revised in the light of later information.
  - Post-training devaluation of compound changes prior learning; distinct temporal structure
```

## Cognitive processes

This task is designed to engage the following processes:

- [Causal reasoning](../processes/reasoning_and_problem_solving.md#hed-causal-reasoning)
- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)
- [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error)
- [Probability judgment](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-probability-judgment)

## Key references

- Shanks, D. R., & Dickinson, A. (1987). Associative accounts of causality judgment. *Psychology of Learning and Motivation*, 21, 229-261. ([DOI](https://doi.org/10.1016/s0079-7421(08)60030-4))
- Cheng, P. W. (1997). From covariation to causation: A causal power theory. *Psychological Review*, 104(2), 367-405. ([DOI](https://doi.org/10.1037/0033-295x.104.2.367))
- Dickinson, A., Shanks, D., & Evenden, J. (1984). Judgement of act-outcome contingency: The role of selective attribution. *Quarterly Journal of Experimental Psychology Section A*, 36(1), 29-50. ([DOI](https://doi.org/10.1080/14640748408401502))

## Further references

- De Houwer, J., & Beckers, T. (2002). A review of recent developments in research and theories on human contingency learning. *Quarterly Journal of Experimental Psychology Section B*, 55(4), 289-310. ([DOI](https://doi.org/10.1080/02724990244000034), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12350283/))
- Griffiths, T. L., & Tenenbaum, J. B. (2005). Structure and strength in causal induction. *Cognitive Psychology*, 51(4), 334-384. ([DOI](https://doi.org/10.1016/j.cogpsych.2005.05.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16168981/))
- Perales, J. C., Catena, A., Shanks, D. R., & Gonzalez, J. A. (2005). Dissociation between judgments and outcome-expectancy measures in covariation learning: A signal detection theory approach. *Journal of Experimental Psychology: Learning, Memory, and Cognition*, 31(5), 1105-1120. ([DOI](https://doi.org/10.1037/0278-7393.31.5.1105), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16248753/))
- Lu, H., Yuille, A. L., Liljeholm, M., Cheng, P. W., & Holyoak, K. J. (2008). Bayesian generic priors for causal learning. *Psychological Review*, 115(4), 955-984. ([DOI](https://doi.org/10.1037/a0013256), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18954210/))

