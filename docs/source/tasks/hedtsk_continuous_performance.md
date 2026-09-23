(hedtsk_continuous_performance)=
# Continuous Performance Task

**HED task ID:** `hedtsk_continuous_performance`

**Family:** [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md)

**Also known as:** CPT, CPT-II, AX-CPT variant also separate entry, Continuous Performance

Extended stream of stimuli in which a rare target requires a response; omission and commission errors index sustained attention and response control.

## Description

The Continuous Performance Task requires participants to continuously monitor a stream of stimuli and respond selectively to infrequent target stimuli while withholding responses to non-targets over an extended period (5-15 minutes). The standard version involves responding when the letter "X" appears; the AX-CPT variant requires responding only when "A" is immediately followed by "X." Target frequency is typically 5-25% of trials. Performance measures include hit rate, false alarm rate, d' (sensitivity), and vigilance decrement over time. The task is widely used in ADHD research and clinical neuropsychology.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A rapid sequence of stimuli is presented.
    2. Participants respond to infrequent target stimuli and withhold responses to non-targets over a prolonged session (10–20 min).
* - **Manipulations**
  - - Target probability
    - Stimulus presentation rate (ISI)
    - Session duration
    - Signal type (letters, digits, tones)
* - **Measurements**
  - - Hit rate, false alarm rate, d-prime (sensitivity)
    - Commission errors (impulsivity)
    - Omission errors (inattention)
    - RT variability
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
* - X-CPT (Simple)

    `hedvar_continuous_performance__x_cpt_simple`
  - Respond to target letter "X" among non-target letters; measures basic sustained attention.
  - Respond to single target letter; canonical simple vigilance paradigm
* - AX-CPT (Context Processing)

    `hedvar_continuous_performance__ax_cpt_context_processing`
  - Respond to "X" only when preceded by "A"; probes context maintenance and proactive/reactive control.
  - Context-dependent target requires tracking A→X sequence; different working memory demand
* - Identical Pairs CPT (IP-CPT)

    `hedvar_continuous_performance__identical_pairs_cpt_ip_cpt`
  - Respond when two consecutive stimuli are identical; taps working memory updating.
  - Respond when consecutive stimuli match; different stimulus-response rule
* - Gradual-Onset CPT (gradCPT)

    `hedvar_continuous_performance__gradual_onset_cpt_gradcpt`
  - Scene images fade in/out continuously; respond to one category, withhold to another; naturalistic sustained attention.
  - Stimuli gradually transition instead of discrete flashes; different perceptual and decision dynamics
* - Auditory CPT

    `hedvar_continuous_performance__auditory_cpt`
  - Auditory stimulus stream; respond to target phoneme or tone.
  - Auditory stimulus stream instead of visual; different sensory modality
* - Conners' CPT-3

    `hedvar_continuous_performance__conners_cpt_3`
  - Standardized commercial version with norms for ADHD assessment.
  - Standardized commercial CPT with letter stimuli and specific timing; named published instrument
* - TOVA (Test of Variables of Attention)

    `hedvar_continuous_performance__tova_test_of_variables_of_attention`
  - Commercial CPT variant with specific timing parameters and normative data.
  - Geometric stimuli, fixed ISI; distinct named instrument with different timing parameters
* - CPT with Emotional Distractors

    `hedvar_continuous_performance__cpt_with_emotional_distractors`
  - Task-irrelevant emotional stimuli during sustained attention.
  - Emotional stimuli as distractors; retained per §5.1 (EMOT retired)
```

## Cognitive processes

This task is designed to engage the following processes:

- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Alerting](../processes/selective_and_sustained_attention.md#hed-alerting)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Mind wandering](../processes/awareness_agency_and_metacognition.md#hed-mind-wandering)

## Key references

- Rosvold, H. E., Mirsky, A. F., Sarason, I., Bransome, E. D., & Beck, L. H. (1956). A continuous performance test of brain damage. *Journal of Consulting Psychology*, 20(5), 343-350. ([DOI](https://doi.org/10.1037/h0043220), [PubMed](https://pubmed.ncbi.nlm.nih.gov/13367264/))
- Nuechterlein, K. H., Parasuraman, R., & Jiang, Q. (1983). Visual sustained attention: Image degradation produces rapid sensitivity decrement over time. *Science*, 220(4594), 327-329. ([DOI](https://doi.org/10.1126/science.6836276), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6836276/))
- Carter, C. S., Braver, T. S., Barch, D. M., Botvinick, M. M., Noll, D., & Cohen, J. D. (1998). Anterior cingulate cortex, error detection, and the online monitoring of performance. *Science*, 280(5364), 747-749. ([DOI](https://doi.org/10.1126/science.280.5364.747), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9563953/))

## Further references

- Huang-Pollock, C. L., Karalunas, S. L., Tam, H., & Moore, A. N. (2012). Evaluating vigilance deficits in ADHD: A meta-analysis of CPT performance. *Journal of Abnormal Psychology*, 121(2), 360–371. ([DOI](https://doi.org/10.1037/a0027205), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22428793/))
- Esterman, M., Noonan, S. K., Rosenberg, M., & DeGutis, J. (2013). In the zone or zoning out? Tracking behavioral and neural fluctuations during sustained attention. *Cerebral Cortex*, 23(11), 2712–2723. ([DOI](https://doi.org/10.1093/cercor/bhs261))
- Fortenbaugh, F. C., DeGutis, J., & Esterman, M. (2017). Recent theoretical, neural, and clinical advances in sustained attention research. *Annals of the New York Academy of Sciences*, 1396(1), 70–91. ([DOI](https://doi.org/10.1111/nyas.13318), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28260249/))
- Weigard, A., & Huang-Pollock, C. (2017). The role of speed in ADHD-related working memory deficits: A time-based resource-sharing and diffusion model account. *Clinical Psychological Science*, 5(2), 195–211.

## External links

- Cognitive Atlas: [Continuous Performance Task](https://www.cognitiveatlas.org/task/id/trm_57c0c34e61fdf)

