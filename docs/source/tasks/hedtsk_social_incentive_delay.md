(hedtsk_social_incentive_delay)=
# Social Incentive Delay Task

**HED task ID:** `hedtsk_social_incentive_delay`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** SID, Social Incentive Delay

MID variant in which cues predict potential social (smiling/frowning face) rather than monetary outcomes; indexes social reward anticipation.

## Description

The Social Incentive Delay Task is a variant of the Monetary Incentive Delay Task (Task 63) that replaces monetary outcomes with social rewards and punishments. Cues signal the potential for positive social feedback (e.g., a smiling face with a thumbs-up), negative social feedback (e.g., a frowning face with a thumbs-down), or neutral outcomes. Participants then respond to a target stimulus, and outcome delivery depends on response speed. The SID was developed to compare the neural substrates of social versus non-social reward anticipation and consumption, testing whether social rewards engage the same striatal dopaminergic circuitry as monetary rewards. The task has been particularly impactful in autism spectrum disorder research, where reduced social reward sensitivity is hypothesized.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Cues signal potential social reward (smiling face), social non-reward (neutral face), or control (geometric shape). After a delay, participants respond to a target; outcome is contingent on response speed.
* - **Manipulation**
  - Cue type (social reward, social non-reward, non-social control); target duration (titrated); reward magnitude.
* - **Measurement**
  - RT by cue type; fMRI ventral striatum activation; comparison of social vs. monetary reward anticipation signals.
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
* - Standard SID (Smiling Face Reward)

    `hedvar_social_incentive_delay__standard_sid_smiling_face_reward`
  - Happy face/approval cue as social reward; frowning face as social punishment.
  - Canonical SID with face as social incentive
* - SID with Personalized Social Stimuli

    `hedvar_social_incentive_delay__sid_with_personalized_social_stimuli`
  - Faces of familiar people (peers, family) as reward stimuli.
  - Stimuli customized to individual's social network; different stimulus content
* - SID vs. MID within-Subjects

    `hedvar_social_incentive_delay__sid_vs_mid_within_subjects`
  - Both social and monetary versions in the same scanning session for direct comparison.
  - Both social and monetary incentives in same session; direct contrast paradigm
* - SID with Graded Social Reward

    `hedvar_social_incentive_delay__sid_with_graded_social_reward`
  - Different intensities of social feedback (mild smile vs. enthusiastic approval).
  - Multiple social reward magnitudes; tests social reward sensitivity
* - SID with Real Social Interaction

    `hedvar_social_incentive_delay__sid_with_real_social_interaction`
  - Social reward delivered by actual experimenters or confederates.
  - Actual social partner rather than photograph; different social context
```

## Cognitive processes

This task is designed to engage the following processes:

- [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)
- [Incentive salience](../processes/reward_anticipation_and_motivation.md#hed-incentive-salience)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)

## Key references

- Spreckelmeyer, K. N., Krach, S., Kohls, G., Rademacher, L., Irmak, A., Konrad, K., ... & Gründer, G. (2009). Anticipation of monetary and social reward differently activates mesolimbic brain structures in men and women. *Social Cognitive and Affective Neuroscience*, 4(2), 158–165. ([DOI](https://doi.org/10.1093/scan/nsn051), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19174537/))
- Rademacher, L., Krach, S., Kohls, G., Irmak, A., Gründer, G., & Spreckelmeyer, K. N. (2010). Dissociation of neural networks for anticipation and consumption of monetary and social rewards. *NeuroImage*, 49(4), 3276–3285. ([DOI](https://doi.org/10.1016/j.neuroimage.2009.10.089), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19913621/))
- Kohls, G., Perino, M. T., Taylor, J. M., Madva, E. N., Cayber, S. J., Troiani, V., ... & Schultz, R. T. (2013). The nucleus accumbens is involved in both the pursuit of social reward and the avoidance of social punishment. *Neuropsychologia*, 51(11), 2062–2069. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2013.07.020), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23911778/))

## Further references

- Flores, L. E., Jr., Eckstrand, K. L., Silk, J. S., Allen, N. B., Ambrosia, M., Healey, K. L., & Forbes, E. E. (2018). Adolescents' neural response to social reward and real-world emotional closeness and positive affect. *Cognitive, Affective, & Behavioral Neuroscience*, 18(5), 705–717. ([DOI](https://doi.org/10.3758/s13415-018-0598-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29943174/))
- Richey, J. A., Rittenberg, A., Hughes, L., Damiano, C. R., Sabatino, A., Miller, S., ... & Dichter, G. S. (2014). Common and distinct neural features of social and non-social reward processing in autism and social anxiety disorder. *Social Cognitive and Affective Neuroscience*, 9(3), 367–377. ([DOI](https://doi.org/10.1093/scan/nss146))
- Cremers, H. R., Veer, I. M., Spinhoven, P., Rombouts, S. A. R. B., & Roelofs, K. (2015). Neural sensitivity to social reward and punishment anticipation in social anxiety disorder. *Frontiers in Behavioral Neuroscience*, 8, 439. ([DOI](https://doi.org/10.3389/fnbeh.2014.00439), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25601830/))

