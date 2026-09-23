(hedtsk_go_no_go)=
# Go/No-Go Task

**HED task ID:** `hedtsk_go_no_go`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md)

**Also known as:** GNG, Go No-Go, Go/No-Go

Responses required to frequent "go" stimuli must be withheld on rare "no-go" stimuli; commission errors and N2/P3 ERPs index response inhibition.

## Description

The Go/No-Go Task measures response inhibition by requiring participants to respond quickly to frequent "go" stimuli while withholding responses to infrequent "no-go" stimuli. The typical ratio is 70-80% go and 20-30% no-go trials, creating a strong prepotent tendency to respond. Performance is measured by go-trial RT (engagement), go-trial accuracy (compliance), and no-go accuracy / false alarm rate (inhibitory control). The task is simpler than the Stop-Signal task as it measures the ability to withhold (rather than cancel) a response.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Stimuli appear one at a time.
    2. Participants respond (Go) to frequent targets and withhold (No-Go) responses to infrequent non-targets.
* - **Manipulations**
  - - Go/No-Go ratio (typically 70:30 or 80:20)
    - ISI
    - Stimulus type
    - Response deadline
* - **Measurements**
  - - Commission errors (false alarms to No-Go)
    - Omission errors
    - Go RT
    - No-Go N2 and P3 ERP components
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
* - Standard Go/No-Go

    `hedvar_go_no_go__standard_go_no_go`
  - Frequent go stimuli (75–80%), infrequent no-go stimuli (20–25%).
  - Canonical: respond to go, withhold to no-go; measures response inhibition
* - Emotional Go/No-Go

    `hedvar_go_no_go__emotional_go_no_go`
  - Emotional faces or words as go/no-go stimuli; probes emotion-cognition interaction.
  - Emotional stimuli as go/no-go signals; retained per §5.1 (EMOT retired)
* - Reward/Punishment Go/No-Go

    `hedvar_go_no_go__reward_punishment_go_no_go`
  - Pavlovian-instrumental transfer paradigm—reward biases go, punishment biases no-go.
  - Monetary outcomes for correct responses; motivation manipulation changes decision context
* - Probabilistic Go/No-Go

    `hedvar_go_no_go__probabilistic_go_no_go`
  - Varying go/no-go ratios (50/50 to 90/10) to manipulate prepotency.
  - Probabilistic rather than deterministic stimulus-response rules; different learning structure
* - Cued Go/No-Go

    `hedvar_go_no_go__cued_go_no_go`
  - Pre-trial cues signal likely go or no-go, allowing proactive control.
  - Preparatory cue precedes imperative signal; different temporal structure
* - Flanked Go/No-Go

    `hedvar_go_no_go__flanked_go_no_go`
  - Go/no-go stimuli flanked by distractors; combines inhibition and selective attention.
  - Go/no-go signal surrounded by flanking distractors; adds conflict component
* - Reversal Go/No-Go

    `hedvar_go_no_go__reversal_go_no_go`
  - Mid-task contingency reversal; previously-go stimuli become no-go.
  - Go/no-go assignments reverse mid-task; tests reversal of inhibitory mappings
* - Saccadic Go/No-Go

    `hedvar_go_no_go__saccadic_go_no_go`
  - Eye movements as responses; oculomotor inhibition.
  - Eye movement response instead of button press; different response effector
* - Multi-Stimulus Go/No-Go

    `hedvar_go_no_go__multi_stimulus_go_no_go`
  - Multiple go stimuli and multiple no-go stimuli; more complex stimulus-response mapping.
  - Multiple stimulus categories with different go/no-go rules; more complex rule set
```

## Cognitive processes

This task is designed to engage the following processes:

- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Donders, F. C. (1969/1868). On the speed of mental processes. *Acta Psychologica*, 30, 412-431. ([DOI](https://doi.org/10.1016/0001-6918(69)90065-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/5811531/))
- Garavan, H., Ross, T. J., & Stein, E. A. (1999). Right hemispheric dominance of inhibitory control: An event-related functional MRI study. *Proceedings of the National Academy of Sciences*, 96(14), 8301-8306. ([DOI](https://doi.org/10.1073/pnas.96.14.8301), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10393989/))
- Simmonds, D. J., Pekar, J. J., & Mostofsky, S. H. (2008). Meta-analysis of Go/No-go tasks demonstrating that fMRI activation associated with response inhibition is task-dependent. *Neuropsychologia*, 46(1), 224-232. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2007.07.015), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17850833/))

## Further references

- Wessel, J. R. (2018). Prepotent motor activity and inhibitory control demands in different variants of the go/no-go paradigm. *Psychophysiology*, 55(3), e12871. ([DOI](https://doi.org/10.1111/psyp.12871))
- Swick, D., Ashley, V., & Turken, U. (2011). Are the neural correlates of stopping and not going identical? Quantitative meta-analysis of two response inhibition tasks. *NeuroImage*, 56(3), 1655–1665. ([DOI](https://doi.org/10.1016/j.neuroimage.2011.02.070), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21376819/))
- Criaud, M., & Boulinguez, P. (2013). Have we been asking the right questions when assessing response inhibition in go/no-go tasks with fMRI? *Neuroscience & Biobehavioral Reviews*, 37(1), 11–23. ([DOI](https://doi.org/10.1016/j.neubiorev.2012.11.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23164813/))
- Littman, R., & Takács, Á. (2017). Do all inhibitions act alike? A study of Go/No-Go and stop-signal paradigms using drift-diffusion modeling. *PLOS ONE*, 12(10), e0186774. ([DOI](https://doi.org/10.1371/journal.pone.0186774), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29065184/))

## External links

- Cognitive Atlas: [go/no-go task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949a93)

- CogPO: [Go/No-Go Paradigm](http://www.wiki.cogpo.org/index.php?title=Go%2FNo-Go_Paradigm)

