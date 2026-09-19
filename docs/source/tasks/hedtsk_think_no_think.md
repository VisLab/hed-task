(hedtsk_think_no_think)=
# Think/No-Think Task

**HED task ID:** `hedtsk_think_no_think`

**Family:** [Memory control and prospective memory tasks](families/memory_control.md)

**Also known as:** TNT Task, Think No-Think

Cue words are presented with instructions to either retrieve or suppress their learned associate; later memory for suppressed items indexes retrieval-induced forgetting through inhibition.

## Description

Participants first learn cue-target word pairs (e.g., "ordeal–roach"). In the critical phase, cues are presented and participants are instructed either to recall the target (Think) or to prevent the target from coming to mind (No-Think). On a final test, suppressed (No-Think) items show reduced recall relative to baseline items that were learned but not presented during the critical phase. Anderson and Green (2001) introduced this paradigm as a memory analog of the Go/No-Go motor inhibition task, arguing that just as people can stop a motor action, they can suppress retrieval of unwanted memories. The paradigm has become central to research on memory suppression, PTSD, and the role of prefrontal control over hippocampal memory retrieval.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants learn cue-target word pairs to criterion. In the critical phase, cues are presented and participants either actively recall the target (think) or suppress retrieval (no-think). A final test probes all pairs.
* - **Manipulation**
  - Think vs. no-think vs. baseline (not presented in critical phase); number of suppression repetitions; independent probe test (IP: novel cue for same target).
* - **Measurement**
  - Suppression-induced forgetting (baseline − no-think recall); think benefit (think − baseline); IP test (demonstrates inhibitory vs. associative interference account).
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
  - Word-pair learning followed by think/no-think phase and final cued recall; the Anderson & Green (2001) version.
  - Canonical Anderson & Green: cue-directed recall suppression
* - Independent Probe Test

    `hedvar_think_no_think__independent_probe`
  - Testing suppressed items with novel, category cues rather than the learned cue; demonstrates cue-independent forgetting indicative of inhibition.
  - Test with novel cues not seen in TNT phase; isolates suppression from retrieval practice
* - TNT with Intrusion Reporting

    `hedvar_think_no_think__tnt_with_intrusion_reporting`
  - Participants report whether the target came to mind despite suppression attempts; tracks suppression success over repetitions.
  - Participant signals intrusions during no-think; adds metacognitive monitoring report
* - Emotional TNT

    `hedvar_think_no_think__emotional_tnt`
  - Negative or trauma-related word pairs or scene-face pairs; tests suppression of emotional memories.
  - Emotional paired associates; retained per §5.1 (EMOT retired)
* - TNT with Thought Substitution

    `hedvar_think_no_think__tnt_with_thought_substitution`
  - Instructing participants to replace the unwanted memory with an alternative thought; contrasts direct suppression with thought substitution.
  - Replace suppressed thought with substitute; different suppression strategy
* - Dose-Response TNT

    `hedvar_think_no_think__dose_response_tnt`
  - Varying the number of suppression attempts (0, 2, 4, 8, 12, 16) to trace the dose-response curve of suppression.
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

- Anderson, M. C., & Green, C. (2001). Suppressing unwanted memories by executive control. *Nature*, 410, 366–369. ([DOI](https://doi.org/10.1038/35066572), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11268212/))
- Anderson, M. C., & Hanslmayr, S. (2014). Neural mechanisms of motivated forgetting. *Trends in Cognitive Sciences*, 18(6), 279–292. ([DOI](https://doi.org/10.1016/j.tics.2014.03.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24747000/))
- Levy, B. J., & Anderson, M. C. (2012). Purging of memories from conscious awareness tracked in the human brain. *Journal of Neuroscience*, 32(47), 16785–16794. ([DOI](https://doi.org/10.1523/jneurosci.2640-12.2012), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23175832/))

## Further references

- Gagnepain, P., Hulbert, J., & Anderson, M. C. (2017). Parallel regulation of memory and emotion supports the suppression of intrusive memories. *Journal of Neuroscience*, 37(27), 6423–6441. ([DOI](https://doi.org/10.1523/jneurosci.2732-16.2017), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28559378/))
- Benoit, R. G., & Anderson, M. C. (2012). Opposing mechanisms support the voluntary forgetting of unwanted memories. *Neuron*, 76(2), 450–460. ([DOI](https://doi.org/10.1016/j.neuron.2012.07.025), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23083745/))
- Stramaccia, D. F., Meyer, A.-K., Rischer, K. M., Fawcett, J. M., & Benoit, R. G. (2021). Memory suppression and its deficiency in psychological disorders: A focused review. *Journal of Experimental Psychology: General*, 150(5), 828–850. ([DOI](https://doi.org/10.1037/xge0000971), [PubMed](https://pubmed.ncbi.nlm.nih.gov/33090824/))
- Hu, X., Bergström, Z. M., Gagnepain, P., & Anderson, M. C. (2017). Suppressing unwanted memories reduces their unintended influences. *Current Directions in Psychological Science*, 26(2), 197–206. ([DOI](https://doi.org/10.1177/0963721417689881), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28458471/))

## External links

- Cognitive Atlas: [think/no-think task](https://www.cognitiveatlas.org/task/id/trm_54f93101b2fd8)

