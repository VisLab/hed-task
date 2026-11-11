(hedtsk_feeling_of_knowing)=
# Feeling-of-Knowing Task

**HED task ID:** `hedtsk_feeling_of_knowing`

**Family:** [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md)

**Also known as:** FOK Task, Feeling-of-Knowing Judgment, Hart FOK Paradigm

After failing to recall a studied item, participants rate the likelihood they could recognize the answer; the accuracy of these predictions (gamma correlation with recognition) indexes metacognitive monitoring of unretrieved memory.

## Description

The Feeling-of-Knowing task measures the accuracy of metacognitive judgments about information that cannot currently be recalled. In the standard Hart (1965) paradigm, participants study cue-target pairs, attempt cued recall, and then - for items they failed to recall - rate their confidence that they would recognize the correct answer among alternatives. A subsequent recognition test determines the accuracy of these predictions. The key dependent measure is resolution - the correspondence between feeling-of-knowing magnitude and recognition performance, typically quantified by the Goodman-Kruskal gamma correlation. Feeling-of-knowing judgments are thought to rely on partial retrieval of target attributes, cue familiarity, and accessibility of related information, rather than direct access to trace strength. The paradigm dissociates from Judgment-of-Learning tasks in timing (post-retrieval-failure vs. post-encoding), prediction target (recognition vs. recall), and cognitive basis (partial retrieval and cue familiarity vs. encoding fluency). Feeling-of-knowing accuracy is sensitive to frontal lobe damage, aging, Alzheimer's disease, and schizophrenia, and is more closely tied to executive functioning than Judgment-of-Learning accuracy.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants study cue-target pairs, attempt cued recall, and for each unrecalled item rate their feeling of knowing (likelihood of future recognition).
    2. a subsequent recognition test assesses prediction accuracy.
* - **Manipulations**
  - - Cue familiarity (high vs. low)
    - Target accessibility (related vs. unrelated cues)
    - Number of recognition alternatives
    - Delay between judgment and recognition test
    - Domain (episodic vs. semantic general knowledge)
* - **Measurements**
  - - Feeling-of-knowing magnitude (mean rating)
    - Resolution (gamma correlation between ratings and recognition accuracy)
    - Calibration (correspondence between predicted and actual recognition probabilities)
    - Response latency for feeling-of-knowing judgments
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
* - Episodic Feeling-of-Knowing

    `hedvar_feeling_of_knowing__episodic_feeling_of_knowing`
  - The participant studies word pairs. Later, given the first word, they try to recall the second. For each pair they cannot recall, they rate how likely they would be to recognize the answer if shown it. A recognition test follows, and the match between ratings and recognition is the measure.
  - FOK for episodic memories; unrecalled episode-specific items
* - Semantic / General-Knowledge Feeling-of-Knowing

    `hedvar_feeling_of_knowing__semantic_general_knowledge_feeling_of_knowing`
  - The questions are general-knowledge items such as 'What is the capital of Australia?' rather than studied pairs. For each answer the participant cannot recall, they rate the likelihood of recognizing it, and a multiple-choice test follows.
  - FOK for semantic facts; different memory system
* - Cue-Only vs. Cue-Target Paradigm

    `hedvar_feeling_of_knowing__cue_only_vs_cue_target_paradigm`
  - At the time of the rating, either only the question or cue word is shown, or the cue is shown together with some partial information about the answer. Compares ratings based on the cue alone with ratings that can draw on fragments of the answer.
  - Study with or without target; tests whether target exposure affects FOK accuracy
* - Tip-of-the-Tongue Variant

    `hedvar_feeling_of_knowing__tip_of_the_tongue_variant`
  - The participant indicates when they are in a tip-of-the-tongue state, feeling the answer is on the verge of coming, and may report partial information such as the first letter or number of syllables. These items are analyzed separately from ordinary failures to recall.
  - TOT state as extreme FOK; different phenomenology and partial information access
* - Feeling-of-Knowing with Feedback

    `hedvar_feeling_of_knowing__feeling_of_knowing_with_feedback`
  - After each recognition test the participant is told whether they were right, and the task continues with further items, to see whether the accuracy of their ratings improves with this information.
  - Accuracy feedback after recognition test; tests calibration learning
```

## Cognitive processes

This task is designed to engage the following processes:

- [Feeling of knowing](../processes/awareness_agency_and_metacognition.md#hed-feeling-of-knowing)
- [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Familiarity](../processes/long_term_memory.md#hed-familiarity)

## Key references

- Hart, J. T. (1965). Memory and the feeling-of-knowing experience. *Journal of Educational Psychology*, 56(4), 208-216. ([DOI](https://doi.org/10.1037/h0022263), [PubMed](https://pubmed.ncbi.nlm.nih.gov/5825050/))
- Nelson, T. O. (1984). A comparison of current measures of the accuracy of feeling-of-knowing predictions. *Psychological Bulletin*, 95(1), 109-133. ([DOI](https://doi.org/10.1037/0033-2909.95.1.109), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6544431/))
- Koriat, A. (1993). How do we know that we know? The accessibility model of the feeling of knowing. *Psychological Review*, 100(4), 609-639. ([DOI](https://doi.org/10.1037/0033-295x.100.4.609))

## Further references

- Hertzog, C., Dunlosky, J., & Sinclair, S. M. (2010). Episodic feeling-of-knowing resolution derives from the quality of original encoding. *Memory & Cognition*, 38(6), 771-784. ([DOI](https://doi.org/10.3758/mc.38.6.771), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20852240/))
- Schwartz, B. L., & Metcalfe, J. (2011). Tip-of-the-tongue (TOT) states: Retrieval, behavior, and experience. *Memory & Cognition*, 39(5), 737-749. ([DOI](https://doi.org/10.3758/s13421-010-0066-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21264637/))
- Izaute, M., & Bacon, E. (2005). Specific effects of an amnesic drug: Effect of midazolam on study time allocation and on judgment of learning. *Neuropsychopharmacology*, 30(6), 1132-1139. ([DOI](https://doi.org/10.1038/sj.npp.1300564))
- Reggev, N., Zuckerman, M., & Maril, A. (2011). Are all judgments created equal? An fMRI study of semantic and episodic metamemory predictions. *Neuropsychologia*, 49(5), 1332-1342. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2011.01.013), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21238468/))

