(hedtsk_go_no_go)=
# Go/No-Go Task

**HED task ID:** `hedtsk_go_no_go`

**Family:** [Response inhibition and stopping tasks](families/response_inhibition.md)

**Also known as:** GNG, Go No-Go, Go/No-Go

Responses required to frequent "go" stimuli must be withheld on rare "no-go" stimuli; commission errors and N2/P3 ERPs index response inhibition.

## Description

The Go/No-Go Task measures response inhibition by requiring participants to respond quickly to frequent "go" stimuli while withholding responses to infrequent "no-go" stimuli. The typical ratio is 70-80% go and 20-30% no-go trials, creating a strong prepotent tendency to respond. Performance is measured by go-trial RT (engagement), go-trial accuracy (compliance), and no-go accuracy / false alarm rate (inhibitory control). The task is simpler than the Stop-Signal task as it measures the ability to withhold (rather than cancel) a response.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *Must the player ever hold back?* <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-interstimulus-interval">interstimulus interval</a>, <a href="vocabulary.html#setting-response-deadline">response deadline</a>, <a href="vocabulary.html#setting-target-probability">target probability</a>
- **Material:** A series of single stimuli, typically letters, of which 70-80% are go items and the rest no-go items.

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
    - Incentive cue and outcome (win vs. avoid loss, by action)
    - Cue before each stimulus (predicting go or no-go)
    - Flankers around the go or no-go item
    - Reversal of go and no-go roles (signaled vs. unsignaled)
    - Number of go and no-go stimuli (mapping size)
* - **Measurements**
  - - Commission errors (false alarms to No-Go)
    - Omission errors
    - Go RT
    - No-Go N2 and P3 ERP components
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
* - Emotional Go/No-Go

    `hedvar_go_no_go__emotional_go_no_go`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
  - Go and no-go are defined by facial expression or emotional word, with the assignment reversed in other blocks; the structure is unchanged.
* - Reward/Punishment Go/No-Go

    `hedvar_go_no_go__reward_punishment_go_no_go`
  - feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>; cue: <a href="vocabulary.html#rule-respond-to-rule-cue-incentive-cue">incentive cue</a>; drive: <a href="vocabulary.html#motivator-drive-reward-stake">reward stake</a>; sign: <a href="vocabulary.html#motivator-sign-both">both</a>; earned by: <a href="vocabulary.html#motivator-earned-by-performance">performance</a>; what: <a href="vocabulary.html#motivator-what-money">money</a>; real: <a href="vocabulary.html#motivator-real-paid">paid</a>
  - [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation), [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation)
  - Each stimulus signals which of four action-by-outcome cells applies (go or no-go, to win or to avoid loss), so the stimulus carries an incentive cue and outcomes are paid per trial.
* - Probabilistic Go/No-Go

    `hedvar_go_no_go__probabilistic_go_no_go`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - -
  - The go proportion is set per block from 50 to 90 percent; this is the ratio manipulation run in blocks.
* - Cued Go/No-Go

    `hedvar_go_no_go__cued_go_no_go`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-demand-probability-cue">demand probability cue</a>
  - [Proactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-proactive-control)
  - A cue before each stimulus says whether a go or a no-go stimulus is likely.
* - Flanked Go/No-Go

    `hedvar_go_no_go__flanked_go_no_go`
  - competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-neighbouring-items">neighbouring items</a>
  - [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
  - The go or no-go item is surrounded by congruent or incongruent flankers, adding neighbouring items as a competitor.
* - Reversal Go/No-Go

    `hedvar_go_no_go__reversal_go_no_go`
  - rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-shifts-unsignalled">shifts unsignalled</a>
  - [Reversal learning](../processes/associative_learning_and_reinforcement.md#hed-reversal-learning)
  - Partway through, go and no-go stimuli swap roles, with or without warning; coded as an unsignalled shift, but switches_on_cue applies when the swap is announced.
* - Saccadic Go/No-Go

    `hedvar_go_no_go__saccadic_go_no_go`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-eye-tracker">eye tracker</a>
  - [Saccade](../processes/motor_preparation_timing_and_execution.md#hed-saccade)
  - The go response is an eye movement to the target and no-go means holding fixation; only the effector and recording device change.
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
- Swick, D., Ashley, V., & Turken, U. (2011). Are the neural correlates of stopping and not going identical? Quantitative meta-analysis of two response inhibition tasks. *NeuroImage*, 56(3), 1655-1665. ([DOI](https://doi.org/10.1016/j.neuroimage.2011.02.070), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21376819/))
- Criaud, M., & Boulinguez, P. (2013). Have we been asking the right questions when assessing response inhibition in go/no-go tasks with fMRI? *Neuroscience & Biobehavioral Reviews*, 37(1), 11-23. ([DOI](https://doi.org/10.1016/j.neubiorev.2012.11.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23164813/))
- Littman, R., & Takács, Á. (2017). Do all inhibitions act alike? A study of Go/No-Go and stop-signal paradigms using drift-diffusion modeling. *PLOS ONE*, 12(10), e0186774. ([DOI](https://doi.org/10.1371/journal.pone.0186774), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29065184/))

## External links

- Cognitive Atlas: [go/no-go task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949a93)

- CogPO: [Go/No-Go Paradigm](http://www.wiki.cogpo.org/index.php?title=Go%2FNo-Go_Paradigm)

