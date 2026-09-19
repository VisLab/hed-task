(hedtsk_tower_of_london)=
# Tower of London Task

**HED task ID:** `hedtsk_tower_of_london`

**Family:** [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md)

**Also known as:** TOL, Shallice Tower Task, Tower of London

Rearrange colored beads on pegs to match a goal state in the minimum number of moves; pre-execution latency and move efficiency index planning.

## Description

The Tower of London Task is a planning and problem-solving task. Participants are presented with two configurations of colored beads on pegs: a start state and a goal state. They must plan and execute a sequence of moves to transform the start state into the goal state in the minimum number of moves, following movement constraints (one bead at a time, peg capacity limits). Problem difficulty is manipulated by the minimum number of moves required (2-7). Performance is measured by moves to solution, planning time, and accuracy. The task is a key measure of prefrontal executive function, particularly planning and look-ahead.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Three pegs hold colored discs in a start configuration; participants move discs one at a time to reach a goal configuration in the minimum number of moves.
* - **Manipulation**
  - Problem difficulty (minimum moves: 2–7); number of discs; time constraints; one-touch (planning only) vs. execution versions.
* - **Measurement**
  - Number of problems solved in minimum moves; excess moves; planning time (first-move latency); total solution time.
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
* - Standard Tower of London (3 pegs, 3 balls)

    `hedvar_tower_of_london__standard_tower_of_london_3_pegs_3_balls`
  - Classic Shallice version; problems requiring 2–7 moves.
  - Canonical Shallice ToL: rearrange colored balls across pegs
* - Tower of Hanoi

    `hedvar_tower_of_london__tower_of_hanoi`
  - Related but distinct; uses graduated-size disks with size-ordering constraint; more moves required.
  - Different rule structure (disk size constraint); distinct classic puzzle
* - Tower of London – Drexel (TOL-DX)

    `hedvar_tower_of_london__tower_of_london_drexel_tol_dx`
  - Standardized version with 10 problems and psychometric norms.
  - Standardized 10-item version with normative data; published clinical instrument
* - Tower of London – Freiburg (TOL-F)

    `hedvar_tower_of_london__tower_of_london_freiburg_tol_f`
  - Research-optimized version with controlled problem parameters.
  - Computer version with different item set and constraints
* - Computerized vs. Physical Versions

    `hedvar_tower_of_london__computerized_vs_physical_versions`
  - Digital drag-and-drop vs. manual manipulation of beads.
  - Per §5.6: grasping 3D beads vs. drag-and-drop changes motor activity
* - Tower with Time Pressure

    `hedvar_tower_of_london__tower_with_time_pressure`
  - Imposing deadlines to study speed-accuracy tradeoffs in planning.
  - Response deadline imposed; changes planning strategy
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

- Kaller, C. P., Rahm, B., Spreer, J., Weiller, C., & Unterrainer, J. M. (2011). Dissociable contributions of left and right dorsolateral prefrontal cortex in planning. *Cerebral Cortex*, 21(2), 307–317. ([DOI](https://doi.org/10.1002/hbm.21423), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22002416/))
- Andrés, P. (2003). Frontal cortex as the central executive of working memory: Time to revise our view. *Cortex*, 39(4-5), 871–895. [Updated context: Newman, L. M., et al. (2021). Planning and tower tasks: A systematic review and meta-analysis of structural neuroimaging. *NeuroImage: Clinical*, 30, 102662.] ([DOI](https://doi.org/10.1016/s0010-9452(08)70868-2))
- Köstering, L., Nitschke, K., Schumacher, F. K., et al. (2015). Assessment of planning performance in clinical samples: Reliability and validity of the Tower of London task (TOL-F). *Neuropsychologia*, 75, 646–655. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2015.07.017), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26197091/))
- Unterrainer, J. M., Rahm, B., Kaller, C. P., et al. (2004). Planning abilities and the Tower of London: Is this task measuring a discrete cognitive function? *Journal of Clinical and Experimental Neuropsychology*, 26(6), 846–856. [Updated: Ward, G., & Morris, R. (2005). Introduction to the psychology of planning. In *The Cognitive Psychology of Planning* (pp. 1–34). Psychology Press.] ([DOI](https://doi.org/10.1080/13803390490509574), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15370380/))

## External links

- Cognitive Atlas: [Tower of London](https://www.cognitiveatlas.org/task/id/trm_4da87e439c411)

