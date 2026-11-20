(hedtsk_rey_auditory_verbal_learning)=
# Rey Auditory Verbal Learning Task

**HED task ID:** `hedtsk_rey_auditory_verbal_learning`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** Rey Auditory Verbal Learning Test, RAVLT, Rey Verbal Learning

Repeated presentation of a 15-word list with immediate free recall over five trials, an interference list, and delayed recall; indexes verbal learning and forgetting.

## Description

The RAVLT is a comprehensive measure of verbal episodic memory. A list of 15 unrelated words (List A) is read aloud five times, with free recall tested after each presentation, yielding a learning curve. After the fifth trial, an interference list (List B) is presented once and recalled, followed by immediate recall of List A without re-presentation (retroactive interference). After a 20-30 minute delay, delayed recall and recognition of List A are tested. The RAVLT provides a rich profile of memory processes including acquisition rate, learning plateau, susceptibility to interference, retention over delay, and recognition discrimination.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **What fills the interval?** <a href="vocabulary.html#rule-study-then-test-interval-filler-interference-list">interference list</a>
- **How many study-test rounds?** <a href="vocabulary.html#rule-study-then-test-cycles-repeated-lists">repeated lists</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-words">words</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-examiner">examiner</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-repetitions">number of repetitions</a>, <a href="vocabulary.html#setting-retention-interval">retention interval</a>
- **Material:** A list of 15 unrelated words read aloud (List A), a second interference list (List B), and a recognition list mixing List A words with others.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A 15-word list (List A) is read aloud five times with free recall after each.
    2. A single interference list (List B) is then read once and recalled.
    3. Immediate and delayed recall of List A follow, plus a recognition test.
    4. Optional: The interference list is learned before the main list instead of after it.
    5. Optional: After each free recall the examiner gives category hints for unrecalled words.
* - **Manipulations**
  - - Number of learning trials
    - Interference list
    - Delay before delayed recall
    - Recognition list composition
* - **Measurements**
  - - Total learning (sum of trials 1-5)
    - Retroactive interference (trial 5 - post-interference recall)
    - Delayed recall
    - Recognition hits and false alarms
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
* - Recognition Trial

    `hedvar_rey_auditory_verbal_learning__recognition_trial`
  - named form
  - [Recognition](../processes/long_term_memory.md#hed-recognition)
  - A yes/no recognition list mixing List A, List B and new words is given after delayed recall.
* - Shortened RAVLT

    `hedvar_rey_auditory_verbal_learning__shortened_ravlt`
  - named form
  - -
  - A named short form with fewer learning trials or a shorter list.
* - Proactive Interference Paradigm

    `hedvar_rey_auditory_verbal_learning__proactive_interference_paradigm`
  - interval filler: <a href="vocabulary.html#rule-study-then-test-interval-filler-nothing">nothing</a>
  - -
  - The interference list is learned before the main list instead of after it, so earlier learning's effect on later recall is measured.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Recall](../processes/long_term_memory.md#hed-recall)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Verbal memory](../processes/long_term_memory.md#hed-verbal-memory)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)
- [Proactive interference](../processes/long_term_memory.md#hed-proactive-interference)
- [Retroactive interference](../processes/long_term_memory.md#hed-retroactive-interference)

## Key references

- Lezak, M. D., Howieson, D. B., Bigler, E. D., & Tranel, D. (2012). *Neuropsychological Assessment* (5th ed.). Oxford University Press.

## Further references

- Schoenberg, M. R., Dawson, K. A., Duff, K., Patton, D., Scott, J. G., & Adams, R. L. (2006). Test performance and classification statistics for the Rey Auditory Verbal Learning Test in selected clinical samples. *Archives of Clinical Neuropsychology*, 21(7), 693-703. ([DOI](https://doi.org/10.1016/j.acn.2006.06.010), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16987634/))
- Moradi, A. R., Doost, H. T. N., Taghavi, M. R., Yule, W., & Dalgleish, T. (1999). Everyday memory deficits in children and adolescents with PTSD: Performance on the Rivermead Behavioural Memory Test. *Journal of Child Psychology and Psychiatry*, 40(3), 357-361. ([DOI](https://doi.org/10.1111/1469-7610.00453), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10190337/))
- Tierney, M. C., Nores, A., Snow, W. G., Fisher, R. H., Zorzitto, M. L., & Reid, D. W. (1994). Use of the Rey Auditory Verbal Learning Test in differentiating normal aging from Alzheimer's and Parkinson's dementia. *Psychological Assessment*, 6(2), 129-134. ([DOI](https://doi.org/10.1037/1040-3590.6.2.129))

## External links

- Cognitive Atlas: [Rey Auditory Verbal Learning Task](https://www.cognitiveatlas.org/task/id/trm_4da88ae0f2952)

- CogPO: [Free Word List Recall Paradigm](http://www.wiki.cogpo.org/index.php?title=Free_Word_List_Recall_Paradigm) (close match)

