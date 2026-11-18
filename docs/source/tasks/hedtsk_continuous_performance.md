(hedtsk_continuous_performance)=
# Continuous Performance Task

**HED task ID:** `hedtsk_continuous_performance`

**Family:** [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md)

**Also known as:** CPT, CPT-II, Continuous Performance

Extended stream of stimuli in which a rare target requires a response; omission and commission errors index sustained attention and response control.

## Description

The Continuous Performance Task requires participants to continuously monitor a stream of stimuli and respond selectively to infrequent target stimuli while withholding responses to non-targets over an extended period (5-15 minutes). The standard version involves responding when the letter "X" appears; the AX Continuous Performance Task, a separate task, requires responding only when "A" is immediately followed by "X." Target frequency is typically 5-25% of trials. Performance measures include hit rate, false alarm rate, d' (sensitivity), and vigilance decrement over time. The task is widely used in ADHD research and clinical neuropsychology.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">respond to rule</a>
- **What does the rule ask about each stimulus?** <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
- **Must the player ever hold back?** <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
- **How often is there a target?** <a href="vocabulary.html#rule-respond-to-rule-target-rate-rare-target">rare target</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-presentation-rate">presentation rate</a>, <a href="vocabulary.html#setting-session-duration">session duration</a>, <a href="vocabulary.html#setting-target-probability">target probability</a>
- **Material:** A stream of single letters (or digits or tones) in which one item, usually the letter X, is the rare target.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A rapid sequence of stimuli is presented.
    2. Participants respond to infrequent target stimuli and withhold responses to non-targets over a prolonged session (10-20 min).
* - **Manipulations**
  - - Target probability
    - Stimulus presentation rate (ISI)
    - Session duration
    - Signal type (letters, digits, tones)
    - Emotional distractors during detection
* - **Measurements**
  - - Hit rate
    - False alarm rate
    - d-prime (sensitivity)
    - RT and RT variability
    - Omission and commission errors
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
* - Identical Pairs CPT (IP-CPT)

    `hedvar_continuous_performance__identical_pairs_cpt_ip_cpt`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-digits">digits</a>, <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-compare">compare</a>; reference: <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
  - [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating)
  - The target is any item identical to the one just before it, so each item is compared with the previous one instead of with a fixed letter.
* - Gradual-Onset CPT (gradCPT)

    `hedvar_continuous_performance__gradual_onset_cpt_gradcpt`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-continuous-recording">continuous recording</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-classify">classify</a>; stream: <a href="vocabulary.html#rule-respond-to-rule-stream-continuous">continuous</a>
  - -
  - Scenes fade into one another with no gaps; the participant classifies each as city or mountain, pressing for the frequent category and withholding for the rare one.
* - Auditory CPT

    `hedvar_continuous_performance__auditory_cpt`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception)
  - The same rare-target detection with spoken letters or tones through headphones instead of letters on a screen.
* - Conners' CPT-3

    `hedvar_continuous_performance__conners_cpt_3`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - A commercial instrument that reverses the usual go rate (press for every letter except X, withhold for X) and varies the pace between blocks.
* - TOVA (Test of Variables of Attention)

    `hedvar_continuous_performance__tova_test_of_variables_of_attention`

    Cognitive Atlas: [test of variables of attention](https://www.cognitiveatlas.org/task/id/trm_4da86cdbd9eeb)
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - A commercial instrument with a position-defined shape target and a rare-then-frequent target probability across halves; a named form.
* - CPT with Emotional Distractors

    `hedvar_continuous_performance__cpt_with_emotional_distractors`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>; competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
  - [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
  - Emotional pictures or faces appear in the background or between items as distractors while the usual rare-target detection continues.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Alerting](../processes/selective_and_sustained_attention.md#hed-alerting)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Spontaneous thought](../processes/awareness_agency_and_metacognition.md#hed-mind-wandering)

## Key references

- Rosvold, H. E., Mirsky, A. F., Sarason, I., Bransome, E. D., & Beck, L. H. (1956). A continuous performance test of brain damage. *Journal of Consulting Psychology*, 20(5), 343-350. ([DOI](https://doi.org/10.1037/h0043220), [PubMed](https://pubmed.ncbi.nlm.nih.gov/13367264/))
- Nuechterlein, K. H., Parasuraman, R., & Jiang, Q. (1983). Visual sustained attention: Image degradation produces rapid sensitivity decrement over time. *Science*, 220(4594), 327-329. ([DOI](https://doi.org/10.1126/science.6836276), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6836276/))
- Carter, C. S., Braver, T. S., Barch, D. M., Botvinick, M. M., Noll, D., & Cohen, J. D. (1998). Anterior cingulate cortex, error detection, and the online monitoring of performance. *Science*, 280(5364), 747-749. ([DOI](https://doi.org/10.1126/science.280.5364.747), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9563953/))

## Further references

- Huang-Pollock, C. L., Karalunas, S. L., Tam, H., & Moore, A. N. (2012). Evaluating vigilance deficits in ADHD: A meta-analysis of CPT performance. *Journal of Abnormal Psychology*, 121(2), 360-371. ([DOI](https://doi.org/10.1037/a0027205), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22428793/))
- Esterman, M., Noonan, S. K., Rosenberg, M., & DeGutis, J. (2013). In the zone or zoning out? Tracking behavioral and neural fluctuations during sustained attention. *Cerebral Cortex*, 23(11), 2712-2723. ([DOI](https://doi.org/10.1093/cercor/bhs261))
- Fortenbaugh, F. C., DeGutis, J., & Esterman, M. (2017). Recent theoretical, neural, and clinical advances in sustained attention research. *Annals of the New York Academy of Sciences*, 1396(1), 70-91. ([DOI](https://doi.org/10.1111/nyas.13318), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28260249/))
- Weigard, A., & Huang-Pollock, C. (2017). The role of speed in ADHD-related working memory deficits: A time-based resource-sharing and diffusion model account. *Clinical Psychological Science*, 5(2), 195-211.

## External links

- Cognitive Atlas: [Continuous Performance Task](https://www.cognitiveatlas.org/task/id/trm_57c0c34e61fdf)

