(hedtsk_attention_network)=
# Attention Network Task

**HED task ID:** `hedtsk_attention_network`

**Family:** [Attentional cueing and orienting tasks](families/attentional_cueing.md) (also [Conflict and interference tasks](families/conflict_and_interference.md))

**Also known as:** Attention Network Test, ANT, Clinical Screening ANT

Identify the direction of a central arrow flanked by congruent or incongruent arrows, preceded by various cue types; RT differences across cue and flanker conditions index three independent attention networks (alerting, orienting, executive).

## Description

The Attention Network Test (ANT) combines elements of the Posner cueing paradigm and the Eriksen flanker task to provide separate measures of three attention networks in a single task. Participants respond to the direction of a central arrow flanked by congruent or incongruent flankers, with the target preceded by no cue, a center cue, a double cue, or a spatial cue. The ANT yields three independent efficiency scores: alerting (double cue benefit over no cue), orienting (spatial cue benefit over center cue), and executive control (incongruent flanker cost). The task operationalizes Posner's attention network model.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Flanker task with preceding spatial and temporal cues; participants identify the direction of a central arrow flanked by congruent or incongruent arrows.
* - **Manipulation**
  - Cue type (no cue, center cue, double cue, spatial cue) crossed with flanker congruency (congruent, incongruent).
* - **Measurement**
  - Three network scores derived from RT differences: alerting (double cue − no cue), orienting (center cue − spatial cue), executive (incongruent − congruent).
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
* - Standard ANT (Fan et al., 2002)

    `hedvar_attention_network__standard_ant_fan_et_al_2002`
  - Flanker + cueing combined; three network scores.
  - Canonical ANT with three cue types and flanker congruency; measures alerting, orienting, executive
* - ANT-I (Callejas et al.)

    `hedvar_attention_network__ant_i_callejas_et_al`
  - Measures inter-network interactions.
  - Revised cue design with interaction effects measure; different trial structure and network scoring
* - ANT-R (Revised)

    `hedvar_attention_network__ant_r_revised`
  - Improved reliability and additional conditions.
  - Revised version with separate conflict and inhibition measures; different trial protocol
* - Lateralized ANT (LANT)

    `hedvar_attention_network__lateralized_ant_lant`
  - Targets on horizontal axis; hemisphere-specific effects.
  - Stimuli presented laterally to test hemispheric contributions; different spatial arrangement
* - Child ANT

    `hedvar_attention_network__child_ant`
  - Fish stimuli and simplified responses for developmental studies.
  - Fish stimuli, simplified flanker; procedure genuinely adapted for children per §5.3
* - ANT with Emotional Stimuli

    `hedvar_attention_network__ant_with_emotional_stimuli`
  - Emotional flankers or targets.
  - Emotional flanker content; retained per §5.1 (EMOT retired)
```

## Cognitive processes

This task is designed to engage the following processes:

- [Alerting](../processes/selective_and_sustained_attention.md#hed-alerting)
- [Orienting](../processes/selective_and_sustained_attention.md#hed-orienting)
- [Executive attention](../processes/inhibitory_control_and_conflict_monitoring.md#hed-executive-attention)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)

## Key references

- Fan, J., McCandliss, B. D., Sommer, T., Raz, A., & Posner, M. I. (2002). Testing the efficiency and independence of attentional networks. *Journal of Cognitive Neuroscience*, 14(3), 340-347. ([DOI](https://doi.org/10.1162/089892902317361886), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11970796/))
- Fan, J., McCandliss, B. D., Fossella, J., Flombaum, J. I., & Posner, M. I. (2005). The activation of attentional networks. *NeuroImage*, 26(2), 471-479. ([DOI](https://doi.org/10.1016/j.neuroimage.2005.02.004), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15907304/))
- Petersen, S. E., & Posner, M. I. (2012). The attention system of the human brain: 20 years after. *Annual Review of Neuroscience*, 35, 73-89. ([DOI](https://doi.org/10.1146/annurev-neuro-062111-150525), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22524787/))

## Further references

- MacLeod, J. W., Lawrence, M. A., McConnell, M. M., Eskes, G. A., Klein, R. M., & Shore, D. I. (2010). Appraising the ANT: Psychometric and theoretical considerations of the Attention Network Test. *Neuropsychology*, 24(5), 637–651. ([DOI](https://doi.org/10.1037/a0019803), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20804252/))
- Arora, S., Lawrence, M. A., & Klein, R. M. (2020). The Attention Network Test database: ADHD and cross-cultural applications. *Frontiers in Psychology*, 11, 388. ([DOI](https://doi.org/10.3389/fpsyg.2020.00388), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32292363/))
- Ishigami, Y., & Klein, R. M. (2010). Repeated measurement of the components of attention using two versions of the Attention Network Test (ANT): Stability, isolability, robustness, and reliability. *Journal of Neuroscience Methods*, 190(1), 117–128. ([DOI](https://doi.org/10.1016/j.jneumeth.2010.04.019), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20435062/))

## External links

- Cognitive Atlas: [attention networks test](https://www.cognitiveatlas.org/task/id/trm_4da6304c9aa23)

