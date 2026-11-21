(hedtsk_tower_of_london)=
# Tower of London Task

**HED task ID:** `hedtsk_tower_of_london`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** TOL, Shallice Tower Task, Tower of London

Rearrange colored beads on pegs to match a goal state in the minimum number of moves; pre-execution latency and move efficiency index planning.

## Description

The Tower of London Task is a planning and problem-solving task. Participants are presented with two configurations of colored beads on pegs: a start state and a goal state. They must plan and execute a sequence of moves to transform the start state into the goal state in the minimum number of moves, following movement constraints (one bead at a time, peg capacity limits). Problem difficulty is manipulated by the minimum number of moves required (2-7). Performance is measured by moves to solution, planning time, and accuracy. The task is a key measure of prefrontal executive function, particularly planning and look-ahead.

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
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-game-objects">game objects</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-set-size">set size</a>
- **Material:** Colored beads on three pegs, in a start configuration and a goal configuration.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Three pegs hold colored discs in a start configuration.
    2. Participants move discs one at a time to reach a goal configuration in the minimum number of moves.
* - **Manipulations**
  - - Problem difficulty (minimum moves: 2-7)
    - Number of discs
    - Time constraints
    - One-touch (planning only) vs. execution versions
* - **Measurements**
  - - Number of problems solved in minimum moves
    - Excess moves
    - Planning time (first-move latency)
    - Total solution time
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
* - Tower of London - Drexel (TOL-DX)

    `hedvar_tower_of_london__tower_of_london_drexel_tol_dx`
  - named form
  - -
  - A named clinical instrument with ten standard problems and norms.
* - Tower of London - Freiburg (TOL-F)

    `hedvar_tower_of_london__tower_of_london_freiburg_tol_f`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>
  - -
  - A named computerized research version with problems selected to control difficulty features.
* - Computerized vs. Physical Versions

    `hedvar_tower_of_london__computerized_vs_physical_versions`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-mouse">mouse</a>
  - -
  - The balls and pegs are shown on a screen and moved by mouse rather than being handled; the problem itself is unchanged.
* - Tower with Time Pressure

    `hedvar_tower_of_london__tower_with_time_pressure`
  - trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - -
  - A time limit per problem or an instruction to be fast is added on top of the requirement to use the fewest moves.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Planning](../processes/reasoning_and_problem_solving.md#hed-planning)
- [Means-ends analysis](../processes/reasoning_and_problem_solving.md#hed-means-ends-analysis)
- [Subgoaling](../processes/reasoning_and_problem_solving.md#hed-subgoaling)
- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
- [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use)

## Key references

- Shallice, T. (1982). Specific impairments of planning. *Philosophical Transactions of the Royal Society of London, Series B*, 298(1089), 199-209. ([DOI](https://doi.org/10.1098/rstb.1982.0082), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6125971/))
- Owen, A. M., Doyon, J., Petrides, M., & Evans, A. C. (1996). Planning and spatial working memory: A positron emission tomography study in humans. *European Journal of Neuroscience*, 8(2), 353-364. ([DOI](https://doi.org/10.1111/j.1460-9568.1996.tb01219.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/8714706/))
- Unterrainer, J. M., & Owen, A. M. (2006). Planning and problem solving: From neuropsychology to functional neuroimaging. *Journal of Physiology-Paris*, 99(4-6), 308-317. ([DOI](https://doi.org/10.1016/j.jphysparis.2006.03.014), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16750617/))

## Further references

- Kaller, C. P., Rahm, B., Spreer, J., Weiller, C., & Unterrainer, J. M. (2011). Dissociable contributions of left and right dorsolateral prefrontal cortex in planning. *Cerebral Cortex*, 21(2), 307-317. ([DOI](https://doi.org/10.1093/cercor/bhq096))
- Andrés, P. (2003). Frontal cortex as the central executive of working memory: Time to revise our view. *Cortex*, 39(4-5), 871-895. [Updated context: Newman, L. M., et al. (2021). Planning and tower tasks: A systematic review and meta-analysis of structural neuroimaging. *NeuroImage: Clinical*, 30, 102662.] ([DOI](https://doi.org/10.1016/s0010-9452(08)70868-2))
- Köstering, L., Nitschke, K., Schumacher, F. K., et al. (2015). Assessment of planning performance in clinical samples: Reliability and validity of the Tower of London task (TOL-F). *Neuropsychologia*, 75, 646-655. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2015.07.017), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26197091/))
- Unterrainer, J. M., Rahm, B., Kaller, C. P., et al. (2004). Planning abilities and the Tower of London: Is this task measuring a discrete cognitive function? *Journal of Clinical and Experimental Neuropsychology*, 26(6), 846-856. [Updated: Ward, G., & Morris, R. (2005). Introduction to the psychology of planning. In *The Cognitive Psychology of Planning* (pp. 1-34). Psychology Press.] ([DOI](https://doi.org/10.1080/13803390490509574), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15370380/))

## External links

- Cognitive Atlas: [Tower of London](https://www.cognitiveatlas.org/task/id/trm_4da87e439c411)

- CogPO: [Tower of London Paradigm](http://www.wiki.cogpo.org/index.php?title=Tower_of_London_Paradigm)

