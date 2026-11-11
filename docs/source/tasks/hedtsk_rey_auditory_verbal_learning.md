(hedtsk_rey_auditory_verbal_learning)=
# Rey Auditory Verbal Learning Task

**HED task ID:** `hedtsk_rey_auditory_verbal_learning`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** Rey Auditory Verbal Learning Test, RAVLT, Rey Verbal Learning

Repeated presentation of a 15-word list with immediate free recall over five trials, an interference list, and delayed recall; indexes verbal learning and forgetting.

## Description

The RAVLT is a comprehensive measure of verbal episodic memory. A list of 15 unrelated words (List A) is read aloud five times, with free recall tested after each presentation, yielding a learning curve. After the fifth trial, an interference list (List B) is presented once and recalled, followed by immediate recall of List A without re-presentation (retroactive interference). After a 20-30 minute delay, delayed recall and recognition of List A are tested. The RAVLT provides a rich profile of memory processes including acquisition rate, learning plateau, susceptibility to interference, retention over delay, and recognition discrimination.

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

## Variations

Named versions that change what the participant experiences or does. The identifier
of a variation is `hedvar_<task>__<variation>`.

```{list-table}
:widths: 25 40 35
:header-rows: 1

* - Variation
  - Description
  - Justification
* - Standard RAVLT (List A * 5 + List B + Recall + Delayed Recall)

    `hedvar_rey_auditory_verbal_learning__standard_ravlt_list_a_5_list_b_recall_delayed_recall`
  - A list of 15 unrelated words is read aloud and the participant recalls as many as possible, five times in a row. A second 15-word list is then read and recalled once. The participant then recalls the first list again without hearing it, and once more after a delay of 20 to 30 minutes.
  - Canonical multi-trial verbal learning with interference and delayed recall
* - Recognition Trial

    `hedvar_rey_auditory_verbal_learning__recognition_trial`
  - After the delayed recall, the participant hears or reads a longer list containing the first-list words mixed with second-list words and new words, and says yes or no to each. Separates failure to retrieve from failure to store.
  - Target list embedded in foil words for recognition test; different retrieval task
* - Shortened RAVLT

    `hedvar_rey_auditory_verbal_learning__shortened_ravlt`
  - Fewer learning trials (such as three instead of five) or a shorter word list, for participants who tire easily or when testing time is limited.
  - Fewer study trials; recognized abbreviated protocol
* - Proactive Interference Paradigm

    `hedvar_rey_auditory_verbal_learning__proactive_interference_paradigm`
  - The order is rearranged so that the second list is learned first, and the effect of that earlier learning on recall of the main list is measured, rather than the usual effect of the interference list on recall of what came before.
  - List B interference on List A recall; tests proactive interference effects
* - Cued Recall Addition

    `hedvar_rey_auditory_verbal_learning__cued_recall_addition`
  - After free recall, the participant is given category hints for words not recalled (for example 'one was a kind of animal'). Words produced with a hint were stored but could not be retrieved unaided.
  - Category cues added to recall phase; tests cueing benefit on verbal learning
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

