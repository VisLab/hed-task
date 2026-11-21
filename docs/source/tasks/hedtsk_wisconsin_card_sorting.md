(hedtsk_wisconsin_card_sorting)=
# Wisconsin Card Sorting Task

**HED task ID:** `hedtsk_wisconsin_card_sorting`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** Wisconsin Card Sorting Test, WCST, Card Sorting Task

Sort cards by a hidden rule (color, form, or number) using only correct/incorrect feedback; after runs of correct sorts the rule silently switches. Perseverative errors index set-shifting.

## Description

The WCST tests cognitive flexibility, set-shifting, and learning from feedback. Participants match cards displaying varying numbers of colored symbols to four reference cards according to an unannounced sorting rule (color, shape, or number). After 10 consecutive correct sorts, the rule changes without warning. Feedback ("correct"/"incorrect") is provided after each sort. The test measures categories completed, perseverative errors (continued use of the previous rule), non-perseverative errors, and the ability to maintain set. It is the gold-standard clinical test of prefrontal executive function.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-previous-rule">previous rule</a>
  - *Where does the rule come from?* <a href="vocabulary.html#rule-respond-to-rule-rule-source-learned-from-feedback">learned from feedback</a>
  - *Does the rule change during play?* <a href="vocabulary.html#rule-respond-to-rule-rule-stability-shifts-unsignalled">shifts unsignalled</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Feedback: <a href="vocabulary.html#facet-feedback-trial-feedback">trial feedback</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-alternatives">number of alternatives</a>
- **Material:** Cards that vary in the color, shape and number of their symbols, some ambiguous, sorted against four reference cards.

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
    - Rule-change signaling (explicit cue vs. silent change)
* - **Measurements**
  - - Categories completed
    - Perseverative errors (continuing to sort by old rule)
    - Total errors
    - Trials to first category
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
* - Short Form WCST (64 Cards)

    `hedvar_wisconsin_card_sorting__short_form_wcst_64_cards`
  - named form
  - -
  - A named instrument using only the first 64 cards with the same rules and scoring.
* - Modified WCST with Explicit Cues

    `hedvar_wisconsin_card_sorting__modified_wcst_with_explicit_cues`
  - rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>
  - -
  - The participant is told when the rule changes (and sometimes which rules are possible), so the rule change is signalled instead of silent while the rule itself is still found from feedback.
* - Berg Card Sorting Test

    `hedvar_wisconsin_card_sorting__berg_card_sorting`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>
  - -
  - A named simplified precursor with fewer cards and clearly separated sorting features, available as a computerized form.
* - Intra-/Extra-Dimensional Set Shifting (IED)

    `hedvar_wisconsin_card_sorting__intra_extra_dimensional_set_shifting_ied`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-abstract-patterns">abstract patterns</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-touchscreen">touchscreen</a>
  - -
  - A named CANTAB instrument in which the participant learns by feedback which of two shapes is correct and the rule shifts in stages, first within the same feature and then to a different feature.
* - Reversal-Only WCST

    `hedvar_wisconsin_card_sorting__reversal_only_wcst`
  - named form
  - [Reversal learning](../processes/associative_learning_and_reinforcement.md#hed-reversal-learning)
  - Only two sorting rules are used, so every silent rule change is a reversal to the other rule rather than discovery of a new rule among three.
* - Probabilistic WCST

    `hedvar_wisconsin_card_sorting__probabilistic_wcst`
  - named form
  - -
  - The feedback is wrong on a proportion of trials, so a "wrong" may be noise rather than a rule change.
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

- Lange, F., Seer, C., & Kopp, B. (2017). Cognitive flexibility in neurological disorders: Cognitive components and event-related potentials. *Neuroscience & Biobehavioral Reviews*, 83, 496-507. ([DOI](https://doi.org/10.1016/j.neubiorev.2017.09.011), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28903059/))
- Bishara, A. J., Kruschke, J. K., Stout, J. C., Bechara, A., McCabe, D. P., & Busemeyer, J. R. (2010). Sequential learning models for the Wisconsin Card Sorting Task: Assessing processes in substance dependent individuals. *Journal of Mathematical Psychology*, 54(1), 5-13. ([DOI](https://doi.org/10.1016/j.jmp.2008.10.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20495607/))
- Figueroa-Vargas, A., Cárcamo, C., Henríquez-Ch, R., et al. (2020). Frontoparietal connectivity correlates with cognitive flexibility during the Wisconsin Card Sorting Test. *NeuroImage*, 218, 116938.
- Kopp, B., Steinke, A., & Visalli, A. (2020). Cognitive flexibility and N2/P3 event-related brain potentials. *Scientific Reports*, 10, 9859. ([DOI](https://doi.org/10.1038/s41598-020-66781-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32555267/))

## External links

- Cognitive Atlas: [Wisconsin card sorting test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949f21)

- CogPO: [Wisconsin Card Sorting Test Paradigm](http://www.wiki.cogpo.org/index.php?title=Wisconsin_Card_Sorting_Test_Paradigm)

