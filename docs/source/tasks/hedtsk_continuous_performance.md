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
  - - Hit rate
    - False alarm rate
    - d-prime (sensitivity)
    - RT and RT variability
    - Omission and commission errors
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
  - Single letters appear one at a time for several minutes, and the participant presses a key only when the letter X appears, which is rare. Missed Xs and presses to other letters are the measures.
  - Respond to single target letter; canonical simple vigilance paradigm
* - AX-CPT (Context Processing)

    `hedvar_continuous_performance__ax_cpt_context_processing`
  - Letters appear in pairs. The participant presses the target key only when an X follows an A; an X after any other letter, or any other letter after an A, gets the non-target key. The participant has to remember the previous letter to respond correctly, and A-then-X pairs are made frequent so that the A creates a strong expectation.
  - Context-dependent target requires tracking A→X sequence; different working memory demand
* - Identical Pairs CPT (IP-CPT)

    `hedvar_continuous_performance__identical_pairs_cpt_ip_cpt`
  - A stream of digits or shapes is shown, and the participant presses a key whenever an item is identical to the one just before it. Each item must be held briefly and compared with the next.
  - Respond when consecutive stimuli match; different stimulus-response rule
* - Gradual-Onset CPT (gradCPT)

    `hedvar_continuous_performance__gradual_onset_cpt_gradcpt`
  - Photographs of scenes fade continuously into one another with no blank gaps, about one every 800 ms. The participant presses a key for one category (for example cities) and withholds for the rare other category (mountains). The lack of abrupt onsets makes the task depend on steady attention rather than being prompted by each new stimulus.
  - Stimuli gradually transition instead of discrete flashes; different perceptual and decision dynamics
* - Auditory CPT

    `hedvar_continuous_performance__auditory_cpt`
  - The stream of items is heard rather than seen, for example spoken letters or tones through headphones, and the participant responds only to the rare target sound.
  - Auditory stimulus stream instead of visual; different sensory modality
* - Conners' CPT-3

    `hedvar_continuous_performance__conners_cpt_3`
  - A commercial standardized version in which the participant presses the space bar for every letter except X, which is withheld. The 14-minute task varies the pace between blocks and provides age norms used in attention-deficit assessment.
  - Standardized commercial CPT with letter stimuli and specific timing; named published instrument
* - TOVA (Test of Variables of Attention)

    `hedvar_continuous_performance__tova_test_of_variables_of_attention`
  - A commercial version using a simple geometric shape that appears at the top or bottom of the screen. The participant presses a button for the target position only. Targets are rare in the first half and frequent in the second, and timing and norms are fixed by the instrument.
  - Geometric stimuli, fixed ISI; distinct named instrument with different timing parameters
* - CPT with Emotional Distractors

    `hedvar_continuous_performance__cpt_with_emotional_distractors`
  - Emotional pictures or faces appear in the background or between items while the participant performs the usual target detection, so sustained attention is measured in the presence of emotional distraction.
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

