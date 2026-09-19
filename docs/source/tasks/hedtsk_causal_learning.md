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
* - **Manipulation**
  - Contingency (delta-P value: positive, zero, negative); outcome base rate (common vs. rare outcomes); cue competition (blocking, overshadowing, relative validity); number of trials; trial-by-trial vs. summary presentation; number of candidate causes; temporal contiguity between cause and outcome.
* - **Measurement**
  - Causal strength ratings; trial-by-trial prediction accuracy; judgment latency; sensitivity to contingency components (P(O|C) and P(O|~C) separately); blocking magnitude; correspondence between judgments and normative models (delta-P, causal power, Rescorla-Wagner).
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
  - Cover story: patients eat foods and develop (or don't develop) allergies. The most common contingency learning cover story. Naturalistic and intuitive framing.
  - Canonical food-allergy prediction: participant judges cause-effect contingencies
* - Blocking Paradigm

    `hedvar_causal_learning__blocking_paradigm`
  - Pre-train cause A → outcome, then present compound AB → outcome. Test causal rating for B. Blocking (low B ratings) demonstrates cue competition and supports associative models.
  - Pre-training on one cue blocks learning about second cue; distinct compound conditioning procedure
* - Outcome Density Manipulation

    `hedvar_causal_learning__outcome_density_manipulation`
  - Vary the base rate of the outcome (P(O|~C)). High outcome density inflates causal ratings even at zero contingency (outcome density bias).
  - Systematically varies base rate of outcomes; changes the statistical environment
* - Trial-by-Trial Prediction

    `hedvar_causal_learning__trial_by_trial_prediction`
  - Participants predict the outcome on each trial before seeing it. Prediction error drives learning. Allows modeling of trial-by-trial associative strength updating.
  - Participant predicts on each trial before feedback; different response requirement from summary judgment
* - Summary vs. Sequential Presentation

    `hedvar_causal_learning__summary_vs_sequential_presentation`
  - Summary: all contingency information presented simultaneously in a table. Sequential: one trial at a time. Different formats can produce different judgments (format effect).
  - Summary table vs. trial-by-trial presentation; changes information format and cognitive demand
* - Multi-Cause (Relative Validity)

    `hedvar_causal_learning__multi_cause_relative_validity`
  - Multiple candidate causes present; some perfectly predictive, others partially redundant. Tests relative validity and cue selection.
  - Multiple competing cues; relative validity procedure changes causal inference structure
* - Causal Direction Manipulation

    `hedvar_causal_learning__causal_direction_manipulation`
  - Predictive (cause → effect: given cause, judge effect likelihood) vs. diagnostic (effect → cause: given effect, judge cause likelihood). Tests asymmetry in causal reasoning.
  - Manipulates whether participant judges cause→effect or effect→cause; different reasoning direction
* - Backward Blocking / Retrospective Revaluation

    `hedvar_causal_learning__backward_blocking_retrospective_revaluation`
  - Post-training information about one cause changes judgments about a previously trained compound partner. Tests whether causal knowledge is updated retrospectively.
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

