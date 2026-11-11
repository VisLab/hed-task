(hedtsk_think_no_think)=
# Think/No-Think Task

**HED task ID:** `hedtsk_think_no_think`

**Family:** [Memory control and prospective memory tasks](families/memory_control.md)

**Also known as:** TNT Task, Think No-Think

Cue words are presented with instructions to either retrieve or suppress their learned associate; later memory for suppressed items indexes retrieval-induced forgetting through inhibition.

## Description

Participants first learn cue-target word pairs (e.g., "ordeal-roach"). In the critical phase, cues are presented and participants are instructed either to recall the target (Think) or to prevent the target from coming to mind (No-Think). On a final test, suppressed (No-Think) items show reduced recall relative to baseline items that were learned but not presented during the critical phase. Anderson and Green (2001) introduced this paradigm as a memory analog of the Go/No-Go motor inhibition task, arguing that just as people can stop a motor action, they can suppress retrieval of unwanted memories. The paradigm has become central to research on memory suppression, PTSD, and the role of prefrontal control over hippocampal memory retrieval.

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
* - **Measurements**
  - - Suppression-induced forgetting (baseline - no-think recall)
    - Think benefit (think - baseline)
    - IP test (demonstrates inhibitory vs. associative interference account)
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
* - Standard Think/No-Think (TNT)

    `hedvar_think_no_think__standard_think_no_think_tnt`
  - The participant learns word pairs until they can give the second word for each first word. Then first words are shown in green (recall and think of the partner) or red (look at the word but keep the partner out of mind) many times. Finally all first words are given and the participant recalls every partner. Partners that were repeatedly kept out of mind are recalled less well than untrained pairs.
  - Canonical Anderson & Green: cue-directed recall suppression
* - Independent Probe Test

    `hedvar_think_no_think__independent_probe`
  - In the final test, instead of the learned first word, a new cue is given, such as a category plus a first letter ('insect R___' for 'roach'). If suppressed words are still harder to recall from a new cue, the memory itself has been weakened, not just the link from the trained cue.
  - Test with novel cues not seen in TNT phase; isolates suppression from retrieval practice
* - TNT with Intrusion Reporting

    `hedvar_think_no_think__tnt_with_intrusion_reporting`
  - After each suppress trial the participant reports whether the partner word came to mind anyway. The share of trials with intrusions falls across repetitions, tracking how suppression improves.
  - Participant signals intrusions during no-think; adds metacognitive monitoring report
* - Emotional TNT

    `hedvar_think_no_think__emotional_tnt`
  - The items to be suppressed are negative or trauma-related, such as unpleasant words or pairs of faces with disturbing scenes, to test whether distressing memories can be suppressed.
  - Emotional paired associates; retained per section 5.1 (EMOT retired)
* - TNT with Thought Substitution

    `hedvar_think_no_think__tnt_with_thought_substitution`
  - Instead of blocking the partner word directly, the participant is given a different word to think about whenever the red cue appears. Compares two strategies for keeping a memory out of mind.
  - Replace suppressed thought with substitute; different suppression strategy
* - Dose-Response TNT

    `hedvar_think_no_think__dose_response_tnt`
  - Different pairs are given different numbers of suppress trials (such as 0, 2, 4, 8, 12 or 16), and final recall is plotted against the number of suppressions.
  - Varies number of suppression repetitions; tests suppression as function of dose
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

