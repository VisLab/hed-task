(hedtsk_virtual_morris_water_maze)=
# Virtual Morris Water Maze Task

**HED task ID:** `hedtsk_virtual_morris_water_maze`

**Family:** [Spatial cognition and navigation tasks](families/spatial_navigation.md)

**Also known as:** vMWM, Morris Water Maze, Virtual Water Maze

Navigate a virtual circular arena to find a hidden platform using distal spatial cues; latency and search patterns index allocentric spatial learning and navigation ability.

## Description

In the Virtual Morris Water Maze, participants navigate a virtual environment to find a hidden goal location using environmental landmarks. During acquisition, participants start from different positions and learn the goal location across trials; performance is indexed by path length, latency, and heading error. Probe trials (goal removed) assess retention by measuring search distribution. The task engages hippocampal spatial mapping and is highly sensitive to hippocampal dysfunction. It dissociates place-based (allocentric) from response-based (egocentric) navigation strategies.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-navigate">navigate</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-joystick">joystick</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Experimental environment:** <a href="vocabulary.html#facet-experimental-environment-virtual-world">virtual world</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** A virtual circular arena with distal landmarks and a hidden (or visible) goal platform.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants navigate a virtual circular arena to find a hidden platform using distal visual cues.
    2. Across trials, they learn the platform's fixed spatial location.
    3. Optional: After the location is learned the platform is moved, usually to the opposite side.
* - **Manipulations**
  - - Cue availability and configuration
    - Platform position
    - Probe trials (platform removed to assess spatial knowledge)
    - Visible vs. hidden platform
    - Maze layout (radial corridors or Y/T maze vs. open pool)
    - Environment scale (large-scale virtual town vs. single arena)
* - **Measurements**
  - - Path length and latency to reach the hidden platform
    - Probe trial time in target quadrant
    - Probe trial proximity to platform location
    - Learning curve across trials
    - Heading error
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
* - Path Integration Tasks

    `hedvar_virtual_morris_water_maze__path_integration_tasks`
  - named form
  - -
  - After moving along a path the landmarks vanish or the scene goes dark, and the participant must return to or point to the start using self-motion alone, remembering the path just taken.
* - Boundary-Based vs. Landmark-Based Navigation

    `hedvar_virtual_morris_water_maze__boundary_based_vs_landmark_based_navigation`
  - named form
  - -
  - The environment provides the enclosure's shape, separate landmark objects, or both, and the two are moved independently at test to see which guides the participant.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory)
- [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use)

## Key references

- Morris, R. G. M. (1984). Developments of a water-maze procedure for studying spatial learning in the rat. *Journal of Neuroscience Methods*, 11(1), 47-60. ([DOI](https://doi.org/10.1016/0165-0270(84)90007-4), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6471907/))
- Maguire, E. A., Burgess, N., Donnett, J. G., Frackowiak, R. S. J., Frith, C. D., & O'Keefe, J. (1998). Knowing where and getting there: A human navigation network. *Science*, 280(5365), 921-924. ([DOI](https://doi.org/10.1126/science.280.5365.921), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9572740/))
- Hartley, T., Maguire, E. A., Spiers, H. J., & Burgess, N. (2003). The well-worn route and the path less traveled: Distinct neural bases of route following and wayfinding in humans. *Neuron*, 37(5), 877-888. ([DOI](https://doi.org/10.1016/s0896-6273(03)00095-3), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12628177/))

## Further references

- Epstein, R. A., Patai, E. Z., Julian, J. B., & Spiers, H. J. (2017). The cognitive map in humans: Spatial navigation and beyond. *Nature Neuroscience*, 20(11), 1504-1513. ([DOI](https://doi.org/10.1038/nn.4656), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29073650/))
- Ekstrom, A. D., & Isham, E. A. (2017). Human spatial navigation: Representations across dimensions and scales. *Current Opinion in Behavioral Sciences*, 17, 84-89. ([DOI](https://doi.org/10.1016/j.cobeha.2017.06.005), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29130062/))
- Coughlan, G., Laczó, J., Hort, J., Minihane, A. M., & Hornberger, M. (2018). Spatial navigation deficits - overlooked cognitive marker for preclinical Alzheimer disease? *Nature Reviews Neurology*, 14(8), 496-506. ([DOI](https://doi.org/10.1038/s41582-018-0031-x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29980763/))
- Spiers, H. J., & Barry, C. (2015). Neural systems supporting navigation. *Current Opinion in Behavioral Sciences*, 1, 47-55. ([DOI](https://doi.org/10.1016/j.cobeha.2014.08.005))

## External links

- Cognitive Atlas: [Morris water maze](https://www.cognitiveatlas.org/task/id/trm_4da890a9bd7a3) (close match)

