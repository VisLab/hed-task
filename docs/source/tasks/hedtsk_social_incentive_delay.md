(hedtsk_social_incentive_delay)=
# Social Incentive Delay Task

**HED task ID:** `hedtsk_social_incentive_delay`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** SID, Social Incentive Delay

MID variant in which cues predict potential social (smiling/frowning face) rather than monetary outcomes; indexes social reward anticipation.

## Description

The Social Incentive Delay Task is a variant of the Monetary Incentive Delay Task (Task 63) that replaces monetary outcomes with social rewards and punishments. Cues signal the potential for positive social feedback (e.g., a smiling face with a thumbs-up), negative social feedback (e.g., a frowning face with a thumbs-down), or neutral outcomes. Participants then respond to a target stimulus, and outcome delivery depends on response speed. The SID was developed to compare the neural substrates of social versus non-social reward anticipation and consumption, testing whether social rewards engage the same striatal dopaminergic circuitry as monetary rewards. The task has been particularly impactful in autism spectrum disorder research, where reduced social reward sensitivity is hypothesized.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
  - *Does a cue come before the target?* <a href="vocabulary.html#rule-respond-to-rule-cue-incentive-cue">incentive cue</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-reward-stake">reward stake</a>
  - *Can the player gain, lose, or both?* <a href="vocabulary.html#motivator-sign-both">both</a>
  - *What earns the outcome?* <a href="vocabulary.html#motivator-earned-by-performance">performance</a>
  - *What is the outcome?* <a href="vocabulary.html#motivator-what-social">social</a>
  - *Is the outcome real?* <a href="vocabulary.html#motivator-real-paid">paid</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>
  - Emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>
  - Feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>, <a href="vocabulary.html#setting-reward-magnitude">reward magnitude</a>
- **Material:** A cue (a smiling face, a neutral face or a geometric shape), a target, and feedback faces such as a smiling face with a thumbs-up or a frowning face with a thumbs-down.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Cues signal potential social reward (smiling face), social non-reward (neutral face), or control (geometric shape).
    2. After a delay, participants respond to a target.
    3. Outcome is contingent on response speed.
* - **Manipulations**
  - - Cue type (social reward, social non-reward, non-social control)
    - Target duration (titrated)
    - Reward magnitude
    - Reward type within session (social vs. monetary, cued per trial)
* - **Measurements**
  - - RT by cue type
    - fMRI ventral striatum activation
    - Comparison of social vs. monetary reward anticipation signals
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
* - SID with Personalized Social Stimuli

    `hedvar_social_incentive_delay__sid_with_personalized_social_stimuli`
  - named form
  - -
  - The reward faces are photographs of people the participant knows rather than strangers.
* - SID vs. MID within-Subjects

    `hedvar_social_incentive_delay__sid_vs_mid_within_subjects`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-value-amounts">value amounts</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-adaptive-trials">adaptive trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - -
  - Social and monetary trials are run in the same session with the cue saying which kind of reward is at stake.
* - SID with Real Social Interaction

    `hedvar_social_incentive_delay__sid_with_real_social_interaction`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>, <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-loudspeaker">loudspeaker</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - The social reward is delivered live by an experimenter or confederate over a video link instead of by a stored photograph.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)
- [Incentive salience](../processes/reward_anticipation_and_motivation.md#hed-incentive-salience)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)

## Key references

- Spreckelmeyer, K. N., Krach, S., Kohls, G., Rademacher, L., Irmak, A., Konrad, K., ... & Gründer, G. (2009). Anticipation of monetary and social reward differently activates mesolimbic brain structures in men and women. *Social Cognitive and Affective Neuroscience*, 4(2), 158-165. ([DOI](https://doi.org/10.1093/scan/nsn051), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19174537/))
- Rademacher, L., Krach, S., Kohls, G., Irmak, A., Gründer, G., & Spreckelmeyer, K. N. (2010). Dissociation of neural networks for anticipation and consumption of monetary and social rewards. *NeuroImage*, 49(4), 3276-3285. ([DOI](https://doi.org/10.1016/j.neuroimage.2009.10.089), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19913621/))
- Kohls, G., Perino, M. T., Taylor, J. M., Madva, E. N., Cayber, S. J., Troiani, V., ... & Schultz, R. T. (2013). The nucleus accumbens is involved in both the pursuit of social reward and the avoidance of social punishment. *Neuropsychologia*, 51(11), 2062-2069. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2013.07.020), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23911778/))

## Further references

- Flores, L. E., Jr., Eckstrand, K. L., Silk, J. S., Allen, N. B., Ambrosia, M., Healey, K. L., & Forbes, E. E. (2018). Adolescents' neural response to social reward and real-world emotional closeness and positive affect. *Cognitive, Affective, & Behavioral Neuroscience*, 18(5), 705-717. ([DOI](https://doi.org/10.3758/s13415-018-0598-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29943174/))
- Richey, J. A., Rittenberg, A., Hughes, L., Damiano, C. R., Sabatino, A., Miller, S., ... & Dichter, G. S. (2014). Common and distinct neural features of social and non-social reward processing in autism and social anxiety disorder. *Social Cognitive and Affective Neuroscience*, 9(3), 367-377. ([DOI](https://doi.org/10.1093/scan/nss146))
- Cremers, H. R., Veer, I. M., Spinhoven, P., Rombouts, S. A. R. B., & Roelofs, K. (2015). Neural sensitivity to social reward and punishment anticipation in social anxiety disorder. *Frontiers in Behavioral Neuroscience*, 8, 439. ([DOI](https://doi.org/10.3389/fnbeh.2014.00439), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25601830/))

