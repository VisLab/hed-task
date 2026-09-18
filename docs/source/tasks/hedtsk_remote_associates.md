(hedtsk_remote_associates)=
# Remote Associates Task

**HED task ID:** `hedtsk_remote_associates`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** Remote Associates Test, RAT, Remote Associates

Three cue words linked to a single fourth word; solution rate and solution time index semantic search and insight.

## Description

The Remote Associates Test measures creative thinking through convergent semantic association. On each trial, participants are given three seemingly unrelated words (e.g., "cottage," "Swiss," "cake") and must find a single word that connects all three (answer: "cheese"). The task requires searching semantic memory broadly, suppressing dominant but incorrect associations, and recognizing the linking concept. RAT performance correlates with measures of creativity, insight problem-solving, and divergent thinking. The task has also been used to study the "Aha!" moment—the subjective experience of sudden insight—and its neural correlates in the right anterior superior temporal gyrus.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Three seemingly unrelated words are presented (e.g., PINE, CRAB, SAUCE); participants find a single word that forms a compound or common phrase with each (APPLE).
* - **Manipulation**
  - Item difficulty (associative strength of solution to each cue); number of items; time limit.
* - **Measurement**
  - Number correct; RT to solution; solution probability as a function of associative strength.
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
* - Standard RAT (Mednick)

    `hedvar_remote_associates__standard_rat_mednick`
  - 30-item test with three cue words per item; timed at 15-40 seconds per item.
  - Canonical three-word compound remote associate task
* - Compound RAT (CRAT)

    `hedvar_remote_associates__compound_rat_crat`
  - Solutions form compound words or phrases with each cue (e.g., "cottage cheese," "Swiss cheese," "cheesecake").
  - Compound word solutions instead of single words; different solution structure
* - Timed vs. Untimed RAT

    `hedvar_remote_associates__timed_vs_untimed_rat`
  - Strict time limits vs. self-paced to study incubation effects.
  - Time pressure changes solving strategy
* - RAT with Hint/Priming

    `hedvar_remote_associates__rat_with_hint_priming`
  - Subliminal or suprathreshold presentation of the answer or related words.
  - Semantic prime precedes problem; changes solution accessibility
```

## Cognitive processes

This task is designed to engage the following processes:

- [Insight](../processes/reasoning_and_problem_solving.md#hed-insight)
- [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing)
- [Semantic knowledge](../processes/language_comprehension_and_production.md#hed-semantic-knowledge)
- [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access)

## Key references

- Mednick, S. A. (1962). The associative basis of the creative process. *Psychological Review*, 69(3), 220–232.
- Bowden, E. M., & Jung-Beeman, M. (2003). Aha! Insight experience correlates with solution activation in the right hemisphere. *Psychonomic Bulletin & Review*, 10(3), 730–737.
- Jung-Beeman, M., Bowden, E. M., Haberman, J., Frymiare, J. L., Arambel-Liu, S., Greenblatt, R., ... & Kounios, J. (2004). Neural activity when people solve verbal problems with insight. *PLoS Biology*, 2(4), e97.

## Recent references

- Beaty, R. E., Silvia, P. J., Nusbaum, E. C., Jauk, E., & Benedek, M. (2014). The roles of associative and executive processes in creative cognition. *Memory & Cognition*, 42(7), 1186–1197.
- Salvi, C., Bricolo, E., Kounios, J., Bowden, E., & Beeman, M. (2016). Insight solutions are correct more often than analytic solutions. *Thinking & Reasoning*, 22(4), 443–460.
- Kounios, J., & Beeman, M. (2014). The cognitive neuroscience of insight. *Annual Review of Psychology*, 65, 71–93.
- Olteteanu, A. M., & Falomir, Z. (2015). comRAT-C: A computational compound Remote Associates Test solver based on language data and its comparison to human performance. *Pattern Recognition Letters*, 67, 81–90.

## External links

- Cognitive Atlas: [Remote Associates Test](https://www.cognitiveatlas.org/task/id/tsk_ZMTNk4Oce5b2j)

