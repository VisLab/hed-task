(hedtsk_causal_learning)=
# Causal Learning Task

**HED task ID:** `hedtsk_causal_learning`

**Family:** [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md)

**Also known as:** Contingency Judgment Task, Contingency Learning Task, Causal Judgment Task, Causal Induction Task, Delta-P Task, Allergy Prediction Task

Participants observe cue-outcome pairings across trials and judge the causal strength of the relationship; judgment profiles across contingency conditions index causal induction and associative learning mechanisms.

## Description

Causal learning tasks measure how people acquire and represent causal relationships from observed co-occurrences. In the standard contingency judgment paradigm, participants observe a series of trials in which a candidate cause (e.g., a food, a medicine, a button press) is either present or absent and an outcome (e.g., an allergic reaction, a health improvement, a light turning on) either occurs or does not. After observing multiple trials, participants rate the causal strength of the relationship (typically -100 to +100 or 0 to 100). The normative benchmark is delta-P (P(outcome|cause) - P(outcome|no cause)), but human judgments systematically deviate: they are sensitive to outcome density, show cue competition effects (blocking, overshadowing), and are influenced by prior causal beliefs. Associative models (Rescorla-Wagner) and statistical models (causal power; Cheng, 1997) compete to explain these patterns. The paradigm bridges associative learning, causal reasoning, and Bayesian inference literatures. It is the human analogue of animal conditioning studies and is foundational for understanding how people learn cause-effect relationships in medicine, engineering, and everyday reasoning.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **What is studied?** <a href="vocabulary.html#rule-study-then-test-studied-material-pairs">pairs</a>
- **How long is it held?** <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-delay-to-outcome">delay to outcome</a>, <a href="vocabulary.html#setting-number-of-trials">number of trials</a>, <a href="vocabulary.html#setting-set-size">set size</a>, <a href="vocabulary.html#setting-target-probability">target probability</a>
- **Material:** Trials showing whether a candidate cause (a food, a medicine, a button press) is present and whether an outcome (an allergic reaction, a light turning on) follows.

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
    - Cue competition (blocking, backward blocking, overshadowing, relative validity)
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
* - Trial-by-Trial Prediction

    `hedvar_causal_learning__trial_by_trial_prediction`
  - feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>; combined with: <a href="vocabulary.html#how-interleaved">interleaved</a>, <a href="vocabulary.html#game-respond-to-rule">respond to rule</a> (The outcome is predicted on each trial before it is shown)
  - -
  - Before each outcome the participant predicts whether it will occur, adding a per-trial response with feedback to the stream.
* - Summary vs. Sequential Presentation

    `hedvar_causal_learning__summary_vs_sequential_presentation`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - -
  - In the summary version the four cell counts are shown at once in a table and rated, so there is no stream of trials.
* - Causal Direction Manipulation

    `hedvar_causal_learning__causal_direction_manipulation`
  - named form
  - -
  - The same trials are judged predictively (does the cause produce the effect) or diagnostically (given the effect, which cause).
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

