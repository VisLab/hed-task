(hedtsk_wisconsin_card_sorting)=
# Wisconsin Card Sorting Task

**HED task ID:** `hedtsk_wisconsin_card_sorting`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** Wisconsin Card Sorting Test, WCST, Card Sorting Task

Sort cards by a hidden rule (color, form, or number) using only correct/incorrect feedback; after runs of correct sorts the rule silently switches. Perseverative errors index set-shifting.

## Description

The WCST tests cognitive flexibility, set-shifting, and learning from feedback. Participants match cards displaying varying numbers of colored symbols to four reference cards according to an unannounced sorting rule (color, shape, or number). After 10 consecutive correct sorts, the rule changes without warning. Feedback ("correct"/"incorrect") is provided after each sort. The test measures categories completed, perseverative errors (continued use of the previous rule), non-perseverative errors, and the ability to maintain set. It is the gold-standard clinical test of prefrontal executive function.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Cards vary on three dimensions (color, form, number).
    2. Participants sort cards to match a target according to an undisclosed rule (e.g., color), receiving feedback.
    3. After a run of correct sorts, the rule changes without warning.
* - **Manipulations**
  - - Number of sorting categories
    - Number of consecutive correct before shift
    - Ambiguous cards
    - Computerized vs. manual administration
* - **Measurements**
  - - Categories completed
    - Perseverative errors (continuing to sort by old rule)
    - Total errors
    - Trials to first category
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
* - Standard WCST (128 Cards)

    `hedvar_wisconsin_card_sorting__standard_wcst_128_cards`
  - Full version with 128 cards, sorting to four reference cards.
  - Canonical 128-card version with shifting sorting rules
* - Short Form WCST (64 Cards)

    `hedvar_wisconsin_card_sorting__short_form_wcst_64_cards`
  - Abbreviated version maintaining psychometric properties.
  - 64-card abbreviated version; recognized efficient form
* - Modified WCST with Explicit Cues

    `hedvar_wisconsin_card_sorting__modified_wcst_with_explicit_cues`
  - Varying amounts of information about sorting rules to decompose set-shifting components.
  - Explicit cues about sorting dimension; tests rule use vs. rule discovery
* - Berg Card Sorting Test

    `hedvar_wisconsin_card_sorting__berg_card_sorting`
  - Simplified version used in developmental research.
  - Simplified precursor with fewer cards and dimensions; named related instrument
* - Intra-/Extra-Dimensional Set Shifting (IED)

    `hedvar_wisconsin_card_sorting__intra_extra_dimensional_set_shifting_ied`
  - CANTAB version explicitly separating intra-dimensional (within-feature) from extra-dimensional (across-feature) shifts.
  - CANTAB analog with distinct dimension-shifting structure; different stimuli and shift types
* - Reversal-Only WCST

    `hedvar_wisconsin_card_sorting__reversal_only_wcst`
  - Simplified two-rule version focusing on reversal learning component.
  - Only reversal phase; isolates reversal from acquisition
* - Probabilistic WCST

    `hedvar_wisconsin_card_sorting__probabilistic_wcst`
  - Feedback is probabilistic rather than deterministic; increases learning difficulty.
  - Sorting feedback probabilistic rather than deterministic; different uncertainty structure
```

## Cognitive processes

This task is designed to engage the following processes:

- [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
- [Hypothesis testing](../processes/reasoning_and_problem_solving.md#hed-hypothesis-testing)
- [Error detection](../processes/inhibitory_control_and_conflict_monitoring.md#hed-error-detection)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)
- [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use)

## Key references

- Nyhus, E., & Barcelo, F. (2009). The Wisconsin Card Sorting Test and the cognitive assessment of prefrontal executive functions: A critical update. *Brain and Cognition*, 71(3), 437-451. ([DOI](https://doi.org/10.1016/j.bandc.2009.03.005), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19375839/))

## Further references

- Lange, F., Seer, C., & Kopp, B. (2017). Cognitive flexibility in neurological disorders: Cognitive components and event-related potentials. *Neuroscience & Biobehavioral Reviews*, 83, 496–507. ([DOI](https://doi.org/10.1016/j.neubiorev.2017.09.011), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28903059/))
- Bishara, A. J., Kruschke, J. K., Stout, J. C., Bechara, A., McCabe, D. P., & Busemeyer, J. R. (2010). Sequential learning models for the Wisconsin Card Sorting Task: Assessing processes in substance dependent individuals. *Journal of Mathematical Psychology*, 54(1), 5–13. ([DOI](https://doi.org/10.1016/j.jmp.2008.10.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20495607/))
- Figueroa-Vargas, A., Cárcamo, C., Henríquez-Ch, R., et al. (2020). Frontoparietal connectivity correlates with cognitive flexibility during the Wisconsin Card Sorting Test. *NeuroImage*, 218, 116938.
- Kopp, B., Steinke, A., & Visalli, A. (2020). Cognitive flexibility and N2/P3 event-related brain potentials. *Scientific Reports*, 10, 9859. ([DOI](https://doi.org/10.1038/s41598-020-66781-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32555267/))

## External links

- Cognitive Atlas: [Wisconsin card sorting test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949f21)

- CogPO: [Wisconsin Card Sorting Test Paradigm](http://www.wiki.cogpo.org/index.php?title=Wisconsin_Card_Sorting_Test_Paradigm)

