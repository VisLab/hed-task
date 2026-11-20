(hedtsk_free_recall)=
# Free Recall Task

**HED task ID:** `hedtsk_free_recall`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** Recall Task

Study of a list of items followed by unaided recall in any order; serial-position curves dissociate primacy and recency.

## Description

Participants study a list of items (typically words) presented sequentially, then attempt to recall all items in any order during an extended recall period. Performance is analyzed via serial position curves showing primacy effects (enhanced recall of early items, attributed to long-term memory consolidation) and recency effects (enhanced recall of recent items, attributed to short-term memory). Clustering analyses examine whether semantically or contextually related items are recalled together, revealing the organization of memory search. The task engages prefrontal, parietal, and temporal memory networks.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **How long is it held?** <a href="vocabulary.html#rule-study-then-test-retention-interval-seconds">seconds</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-free-recall">free recall</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-words">words</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-list-length">list length</a>, <a href="vocabulary.html#setting-presentation-rate">presentation rate</a>, <a href="vocabulary.html#setting-retention-interval">retention interval</a>
- **Material:** A list of words (or pictures) presented one at a time, its semantic organization varied.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants study a list of items (words, pictures) presented one at a time, then recall as many as possible in any order after the last item.
    2. Optional: After many lists have each been studied and recalled, the participant is asked without warning to recall every word from every list.
    3. Optional: The same list is recalled several times in succession without being studied again.
* - **Manipulations**
  - - List length
    - Presentation rate
    - Semantic organization
    - Encoding task (deep vs. shallow)
    - Retention interval (immediate vs. delayed)
    - Distractor interval (after every study item vs. before recall only)
* - **Measurements**
  - - Total items recalled
    - Serial position curve (primacy, recency)
    - Temporal clustering
    - Semantic clustering
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
* - Delayed Free Recall (DFR)

    `hedvar_free_recall__delayed_free_recall_dfr`
  - interval filler: <a href="vocabulary.html#rule-study-then-test-interval-filler-distraction">distraction</a>
  - -
  - A filled delay of 15 to 30 seconds of mental arithmetic is inserted between the end of the list and recall.
* - Final Free Recall

    `hedvar_free_recall__final_free_recall`
  - cycles: <a href="vocabulary.html#rule-study-then-test-cycles-repeated-lists">repeated lists</a>; retention interval: <a href="vocabulary.html#rule-study-then-test-retention-interval-surprise">surprise</a>; interval filler: <a href="vocabulary.html#rule-study-then-test-interval-filler-interference-list">interference list</a>
  - -
  - After many lists have each been studied and recalled, the participant is unexpectedly asked to recall every word from every list.
* - Externalized Free Recall

    `hedvar_free_recall__externalized_free_recall`
  - named form
  - -
  - The participant says every word that comes to mind, including ones they believe are wrong, and flags each one they reject.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Recall](../processes/long_term_memory.md#hed-recall)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Rehearsal](../processes/short_term_and_working_memory.md#hed-rehearsal)

## Key references

- Polyn, S. M., Natu, V. S., Cohen, J. D., & Norman, K. A. (2005). Category-specific cortical activity precedes retrieval during memory search. *Science*, 310(5749), 1963-1966. ([DOI](https://doi.org/10.1126/science.1117645), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16373577/))
- Sederberg, P. B., Gauthier, L. V., Terushkin, V., Miller, J. F., Barnathan, J. A., & Kahana, M. J. (2006). Oscillatory correlates of the primacy effect in episodic memory. *NeuroImage*, 32(3), 1422-1431. ([DOI](https://doi.org/10.1016/j.neuroimage.2006.04.223), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16814568/))

## Further references

- Kahana, M. J. (2012). *Foundations of Human Memory*. Oxford University Press. [Updated: Kahana, M. J. (2020). Computational models of memory search. *Annual Review of Psychology*, 71, 107-138.]
- Polyn, S. M., Norman, K. A., & Kahana, M. J. (2009). A context maintenance and retrieval model of organizational processes in free recall. *Psychological Review*, 116(1), 129-156. ([DOI](https://doi.org/10.1037/a0014420), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19159151/))
- Lohnas, L. J., Polyn, S. M., & Kahana, M. J. (2015). Expanding the scope of memory search: Modeling intralist and interlist effects in free recall. *Psychological Review*, 122(2), 337-363. ([DOI](https://doi.org/10.1037/a0039036), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25844876/))
- Morton, N. W., Sherrill, K. R., & Preston, A. R. (2017). Memory integration constructs maps of space, time, and concepts. *Current Opinion in Behavioral Sciences*, 17, 161-168. ([DOI](https://doi.org/10.1016/j.cobeha.2017.08.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28924579/))

## External links

- Cognitive Atlas: [recall test](https://www.cognitiveatlas.org/task/id/trm_4f2411c91ae5e) (close match)

- CogPO: [Free Word List Recall Paradigm](http://www.wiki.cogpo.org/index.php?title=Free_Word_List_Recall_Paradigm)

