(hedtsk_monetary_incentive_delay)=
# Monetary Incentive Delay Task

**HED task ID:** `hedtsk_monetary_incentive_delay`

**Family:** [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md)

**Also known as:** MID, Monetary Incentive Delay

Cue predicts potential monetary gain or loss; speeded target response determines outcome. Striatal activity to cues indexes reward anticipation.

## Description

The Monetary Incentive Delay Task is the dominant paradigm for neuroimaging studies of reward anticipation and consumption. On each trial, a cue signals the potential outcome: reward (gain), loss avoidance, or neutral. After a variable delay period, participants respond to a briefly presented target; successful responses earn the reward (or avoid the loss). The critical contrast is neural activity during the anticipation period (cue-to-target), which robustly activates the ventral striatum/nucleus accumbens, versus the outcome period (after response), which more strongly engages ventromedial prefrontal cortex. The MID has been widely adopted in clinical neuroimaging of addiction, depression, and schizophrenia.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A cue signals potential reward, loss, or neutral outcome.
    2. After a delay, a target appears and participants make a speeded response.
    3. Outcome depends on response speed.
* - **Manipulations**
  - - Cue type (reward magnitude, loss magnitude, neutral)
    - Target duration (titrated to ~66% hit rate)
* - **Measurements**
  - - RT by cue condition
    - fMRI activation in ventral striatum (anticipation) and medial PFC (outcome)
    - Hit rate
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
* - Standard MID (Knutson)

    `hedvar_monetary_incentive_delay__standard_mid_knutson`
  - Gain, loss-avoidance, and neutral cues; target duration titrated to ~66% accuracy.
  - Canonical cue-anticipation-response structure with monetary reward/punishment
* - Graded Reward MID

    `hedvar_monetary_incentive_delay__graded_reward_mid`
  - Multiple reward magnitudes ($0.20, $1.00, $5.00) to parametrically modulate anticipatory activation.
  - Multiple reward magnitude levels; tests reward sensitivity parametrically
* - MID with Social Rewards

    `hedvar_monetary_incentive_delay__mid_with_social_rewards`
  - Smiling faces or positive social feedback replace monetary outcomes (see also SID, Task 75).
  - Social stimuli (faces) as rewards instead of money; different incentive type
* - MID with Drug Cues

    `hedvar_monetary_incentive_delay__mid_with_drug_cues`
  - Substance-related cues replacing monetary cues in addiction research.
  - Drug-associated cues as incentive stimuli; different cue content
* - Passive MID

    `hedvar_monetary_incentive_delay__passive_mid`
  - No motor response required; isolates anticipation without motor confounds.
  - No response required; isolates anticipatory processing from motor preparation
* - MID with Effort Component

    `hedvar_monetary_incentive_delay__mid_with_effort_component`
  - Effortful responses (grip strength) to earn rewards; integrates motivation and effort.
  - Effort required to obtain reward; adds effort-discounting to incentive structure
```

## Cognitive processes

This task is designed to engage the following processes:

- [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation)
- [Incentive salience](../processes/reward_anticipation_and_motivation.md#hed-incentive-salience)
- [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation)
- [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution)

## Key references

- Knutson, B., Westdorp, A., Kaiser, E., & Hommer, D. (2000). FMRI visualization of brain activity during a monetary incentive delay task. *NeuroImage*, 12(1), 20–27. ([DOI](https://doi.org/10.1006/nimg.2000.0593), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10875899/))
- Knutson, B., Adams, C. M., Fong, G. W., & Hommer, D. (2001). Anticipation of increasing monetary reward selectively recruits nucleus accumbens. *Journal of Neuroscience*, 21(16), RC159. ([DOI](https://doi.org/10.1523/jneurosci.21-16-j0002.2001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11459880/))
- Oldham, S., Murawski, C., Fornito, A., Youssef, G., Yücel, M., & Lorenzetti, V. (2018). The anticipation and outcome phases of reward and loss processing: A neuroimaging meta-analysis of the monetary incentive delay task. *Human Brain Mapping*, 39(8), 3398–3418. ([DOI](https://doi.org/10.1002/hbm.24184), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29696725/))

## Further references

- Wilson, R. P., Colizzi, M., Bossong, M. G., Allen, P., Kempton, M., & Bhattacharyya, S. (2018). The neural substrate of reward anticipation in health: A meta-analysis of fMRI findings in the monetary incentive delay task. *Neuropsychology Review*, 28(4), 496–506. ([DOI](https://doi.org/10.1007/s11065-018-9385-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30255220/))
- Balodis, I. M., & Potenza, M. N. (2015). Anticipatory reward processing in addicted populations: A focus on the monetary incentive delay task. *Biological Psychiatry*, 77(5), 434–444. ([DOI](https://doi.org/10.1016/j.biopsych.2014.08.020), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25481621/))
- Nees, F., Vollstädt-Klein, S., Fauth-Bühler, M., Steiner, S., Mann, K., & Poustka, L. (2012). A target sample size for studies of the monetary incentive delay task – power calculation and evaluation of existing studies. *Neuropsychobiology*, 66(3), 193–198.

## External links

- Cognitive Atlas: [monetary incentive delay task](https://www.cognitiveatlas.org/task/id/trm_4f23fc8c42d28)

- CogPO: [Reward Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Reward_Task_Paradigm) (close match)

