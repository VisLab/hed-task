(hedtsk_think_no_think)=
# Think/No-Think Task

**HED task ID:** `hedtsk_think_no_think`

**Family:** [Memory control and prospective memory tasks](families/memory_control.md)

**Also known as:** TNT Task, Think No-Think

Cue words are presented with instructions to either retrieve or suppress their learned associate; later memory for suppressed items indexes retrieval-induced forgetting through inhibition.

## Description

Participants first learn cue-target word pairs (e.g., "ordeal-roach"). In the critical phase, cues are presented and participants are instructed either to recall the target (Think) or to prevent the target from coming to mind (No-Think). On a final test, suppressed (No-Think) items show reduced recall relative to baseline items that were learned but not presented during the critical phase. Anderson and Green (2001) introduced this paradigm as a memory analog of the Go/No-Go motor inhibition task, arguing that just as people can stop a motor action, they can suppress retrieval of unwanted memories. The paradigm has become central to research on memory suppression, PTSD, and the role of prefrontal control over hippocampal memory retrieval.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">Study, then be tested</a> (`study_then_test`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What is studied?* <a href="vocabulary.html#rule-study-then-test-studied-material-pairs">pairs</a>
  - *How many study-test rounds?* <a href="vocabulary.html#rule-study-then-test-cycles-learn-to-criterion">learn to criterion</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-interleaved-trials">interleaved trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-repetitions">number of repetitions</a>
- **Material:** Cue-target word pairs (such as ordeal-roach) whose cues are later shown alone with an instruction to recall the target or keep it from mind.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants learn cue-target word pairs to criterion.
    2. In the critical phase, cues are presented and participants either actively recall the target (think) or suppress retrieval (no-think).
    3. A final test probes all pairs.
* - **Manipulations**
  - - Think vs. no-think vs. baseline (not presented in critical phase)
    - Number of suppression repetitions
    - Independent probe test (IP: novel cue for same target)
    - Intrusion report after each no-think trial
    - Material valence (negative vs. neutral)
    - Suppression strategy (thought substitution vs. direct blocking)
* - **Measurements**
  - - Suppression-induced forgetting (baseline - no-think recall)
    - Think benefit (think - baseline)
    - IP test (demonstrates inhibitory vs. associative interference account)
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
* - TNT with Intrusion Reporting

    `hedvar_think_no_think__tnt_with_intrusion_reporting`
  - named form
  - [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)
  - After each no-think trial the participant reports whether the partner word came to mind anyway.
* - Emotional TNT

    `hedvar_think_no_think__emotional_tnt`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation)
  - The suppressed material is negative or trauma-related (unpleasant words, or faces paired with disturbing scenes) and is compared with neutral material.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Directed forgetting](../processes/long_term_memory.md#hed-directed-forgetting)
- [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
- [Recall](../processes/long_term_memory.md#hed-recall)
- [Metacognitive control](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-control)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)

## Key references

- Anderson, M. C., & Green, C. (2001). Suppressing unwanted memories by executive control. *Nature*, 410, 366-369. ([DOI](https://doi.org/10.1038/35066572), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11268212/))
- Anderson, M. C., & Hanslmayr, S. (2014). Neural mechanisms of motivated forgetting. *Trends in Cognitive Sciences*, 18(6), 279-292. ([DOI](https://doi.org/10.1016/j.tics.2014.03.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24747000/))
- Levy, B. J., & Anderson, M. C. (2012). Purging of memories from conscious awareness tracked in the human brain. *Journal of Neuroscience*, 32(47), 16785-16794. ([DOI](https://doi.org/10.1523/jneurosci.2640-12.2012), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23175832/))

## Further references

- Gagnepain, P., Hulbert, J., & Anderson, M. C. (2017). Parallel regulation of memory and emotion supports the suppression of intrusive memories. *Journal of Neuroscience*, 37(27), 6423-6441. ([DOI](https://doi.org/10.1523/jneurosci.2732-16.2017), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28559378/))
- Benoit, R. G., & Anderson, M. C. (2012). Opposing mechanisms support the voluntary forgetting of unwanted memories. *Neuron*, 76(2), 450-460. ([DOI](https://doi.org/10.1016/j.neuron.2012.07.025), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23083745/))
- Stramaccia, D. F., Meyer, A.-K., Rischer, K. M., Fawcett, J. M., & Benoit, R. G. (2021). Memory suppression and its deficiency in psychological disorders: A focused review. *Journal of Experimental Psychology: General*, 150(5), 828-850. ([DOI](https://doi.org/10.1037/xge0000971), [PubMed](https://pubmed.ncbi.nlm.nih.gov/33090824/))
- Hu, X., Bergström, Z. M., Gagnepain, P., & Anderson, M. C. (2017). Suppressing unwanted memories reduces their unintended influences. *Current Directions in Psychological Science*, 26(2), 197-206. ([DOI](https://doi.org/10.1177/0963721417689881), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28458471/))

## External links

- Cognitive Atlas: [think/no-think task](https://www.cognitiveatlas.org/task/id/trm_54f93101b2fd8)

