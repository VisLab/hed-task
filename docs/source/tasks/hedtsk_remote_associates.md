(hedtsk_remote_associates)=
# Remote Associates Task

**HED task ID:** `hedtsk_remote_associates`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md) (also [Language comprehension and production tasks](families/language.md))

**Also known as:** Remote Associates Test, RAT, Remote Associates

Three cue words linked to a single fourth word; solution rate and solution time index semantic search and insight.

## Description

The Remote Associates Test measures creative thinking through convergent semantic association. On each trial, participants are given three seemingly unrelated words (e.g., "cottage," "Swiss," "cake") and must find a single word that connects all three (answer: "cheese"). The task requires searching semantic memory broadly, suppressing dominant but incorrect associations, and recognizing the linking concept. RAT performance correlates with measures of creativity, insight problem-solving, and divergent thinking. The task has also been used to study the "Aha!" moment - the subjective experience of sudden insight - and its neural correlates in the right anterior superior temporal gyrus.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-solve-problem">Solve a puzzle</a> (`solve_problem`)
- **Game rules:** none are defined for this game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-trials">number of trials</a>, <a href="vocabulary.html#setting-response-deadline">response deadline</a>
- **Material:** Sets of three words (such as cottage, Swiss, cake) that each form a compound or phrase with one solution word, of varying associative strength.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Three seemingly unrelated words are presented (e.g., PINE, CRAB, SAUCE).
    2. Participants find a single word that forms a compound or common phrase with each (APPLE).
* - **Manipulations**
  - - Item difficulty (associative strength of solution to each cue)
    - Number of items
    - Time limit
    - Hint or masked prime before the item
* - **Measurements**
  - - Number correct
    - RT to solution
    - Solution probability as a function of associative strength
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
* - Compound RAT (CRAT)

    `hedvar_remote_associates__compound_rat_crat`
  - named form
  - -
  - Items are restricted to those whose answer forms a compound word or phrase with each cue, rather than being related by meaning alone.
* - Timed vs. Untimed RAT

    `hedvar_remote_associates__timed_vs_untimed_rat`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - -
  - Items are given with no time limit in one arm, sometimes with a break before unsolved items are retried, so the time-limit constraint is removed.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Insight](../processes/reasoning_and_problem_solving.md#hed-insight)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Semantic knowledge](../processes/language_comprehension_and_production.md#hed-semantic-knowledge)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)

## Key references

- Mednick, S. A. (1962). The associative basis of the creative process. *Psychological Review*, 69(3), 220-232. ([DOI](https://doi.org/10.1037/h0048850), [PubMed](https://pubmed.ncbi.nlm.nih.gov/14472013/))
- Bowden, E. M., & Jung-Beeman, M. (2003). Aha! Insight experience correlates with solution activation in the right hemisphere. *Psychonomic Bulletin & Review*, 10(3), 730-737. ([DOI](https://doi.org/10.3758/bf03196539), [PubMed](https://pubmed.ncbi.nlm.nih.gov/14620371/))
- Jung-Beeman, M., Bowden, E. M., Haberman, J., Frymiare, J. L., Arambel-Liu, S., Greenblatt, R., ... & Kounios, J. (2004). Neural activity when people solve verbal problems with insight. *PLoS Biology*, 2(4), e97. ([DOI](https://doi.org/10.1371/journal.pbio.0020097), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15094802/))

## Further references

- Beaty, R. E., Silvia, P. J., Nusbaum, E. C., Jauk, E., & Benedek, M. (2014). The roles of associative and executive processes in creative cognition. *Memory & Cognition*, 42(7), 1186-1197. ([DOI](https://doi.org/10.3758/s13421-014-0428-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24898118/))
- Salvi, C., Bricolo, E., Kounios, J., Bowden, E., & Beeman, M. (2016). Insight solutions are correct more often than analytic solutions. *Thinking & Reasoning*, 22(4), 443-460. ([DOI](https://doi.org/10.1080/13546783.2016.1141798), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27667960/))
- Kounios, J., & Beeman, M. (2014). The cognitive neuroscience of insight. *Annual Review of Psychology*, 65, 71-93. ([DOI](https://doi.org/10.1146/annurev-psych-010213-115154), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24405359/))
- Olteteanu, A. M., & Falomir, Z. (2015). comRAT-C: A computational compound Remote Associates Test solver based on language data and its comparison to human performance. *Pattern Recognition Letters*, 67, 81-90. ([DOI](https://doi.org/10.1016/j.patrec.2015.05.015))

## External links

- Cognitive Atlas: [Remote Associates Test](https://www.cognitiveatlas.org/task/id/tsk_ZMTNk4Oce5b2j)

