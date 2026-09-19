(hedtsk_virtual_morris_water_maze)=
# Virtual Morris Water Maze Task

**HED task ID:** `hedtsk_virtual_morris_water_maze`

**Family:** [Spatial cognition and navigation tasks](families/spatial_navigation.md)

**Also known as:** vMWM, Morris Water Maze, Virtual Water Maze

Navigate a virtual circular arena to find a hidden platform using distal spatial cues; latency and search patterns index allocentric spatial learning and navigation ability.

## Description

In the Virtual Morris Water Maze, participants navigate a virtual environment to find a hidden goal location using environmental landmarks. During acquisition, participants start from different positions and learn the goal location across trials; performance is indexed by path length, latency, and heading error. Probe trials (goal removed) assess retention by measuring search distribution. The task engages hippocampal spatial mapping and is highly sensitive to hippocampal dysfunction. It dissociates place-based (allocentric) from response-based (egocentric) navigation strategies.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants navigate a virtual circular arena to find a hidden platform using distal visual cues. Across trials, they learn the platform's fixed spatial location.
* - **Manipulation**
  - Cue availability and configuration; platform position; probe trials (platform removed to assess spatial knowledge); visible vs. hidden platform.
* - **Measurement**
  - Path length and latency to find platform across trials (learning curve); probe trial: time in target quadrant, proximity to platform location; search strategy classification.
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
* - Hidden Platform (Allocentric)

    `hedvar_virtual_morris_water_maze__hidden_platform_allocentric`
  - Navigate to invisible goal using distal landmarks; hippocampal-dependent.
  - Canonical allocentric navigation to hidden platform using distal cues
* - Visible Platform (Cue-Based)

    `hedvar_virtual_morris_water_maze__visible_platform_cue_based`
  - Navigate to visible cue; striatal/response learning.
  - Platform marked visibly; cue-based navigation without spatial learning
* - Probe Trials

    `hedvar_virtual_morris_water_maze__probe_trials`
  - Platform removed; time in target quadrant measures spatial memory.
  - Platform removed; tests memory for trained location
* - Reversal

    `hedvar_virtual_morris_water_maze__reversal`
  - Platform relocated; tests behavioral flexibility.
  - Platform moved to opposite quadrant; tests behavioral flexibility
* - Dual-Solution Design

    `hedvar_virtual_morris_water_maze__dual_solution_design`
  - Task solvable by allocentric or egocentric strategy; probe trials disambiguate.
  - Landmark and allocentric routes both available; tests strategy preference
* - Virtual Star Maze

    `hedvar_virtual_morris_water_maze__virtual_star_maze`
  - Y-maze or T-maze alternatives for simpler allocentric/egocentric dissociation.
  - Star-shaped corridors in VR; different maze geometry
* - Path Integration Tasks

    `hedvar_virtual_morris_water_maze__path_integration_tasks`
  - Navigate to remembered location in darkness; tests dead reckoning.
  - Navigation without visual landmarks; dead reckoning demand
* - Large-Scale Virtual Cities

    `hedvar_virtual_morris_water_maze__large_scale_virtual_cities`
  - Naturalistic navigation in complex environments (e.g., Tube map task, Sea Hero Quest).
  - City-scale environment; different scale and complexity
* - Boundary-Based vs. Landmark-Based Navigation

    `hedvar_virtual_morris_water_maze__boundary_based_vs_landmark_based_navigation`
  - Distinguishing geometric/boundary cues from feature/landmark cues.
  - Systematically varies cue type; tests geometric vs. landmark navigation
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

- Epstein, R. A., Patai, E. Z., Julian, J. B., & Spiers, H. J. (2017). The cognitive map in humans: Spatial navigation and beyond. *Nature Neuroscience*, 20(11), 1504–1513. ([DOI](https://doi.org/10.1038/nn.4656), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29073650/))
- Ekstrom, A. D., & Isham, E. A. (2017). Human spatial navigation: Representations across dimensions and scales. *Current Opinion in Behavioral Sciences*, 17, 84–89. ([DOI](https://doi.org/10.1016/j.cobeha.2017.06.005), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29130062/))
- Coughlan, G., Laczó, J., Hort, J., Minihane, A. M., & Hornberger, M. (2018). Spatial navigation deficits—overlooked cognitive marker for preclinical Alzheimer disease? *Nature Reviews Neurology*, 14(8), 496–506. ([DOI](https://doi.org/10.1038/s41582-018-0031-x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29980763/))
- Spiers, H. J., & Barry, C. (2015). Neural systems supporting navigation. *Current Opinion in Behavioral Sciences*, 1, 47–55. ([DOI](https://doi.org/10.1016/j.cobeha.2014.08.005))

## External links

- Cognitive Atlas: [Morris water maze](https://www.cognitiveatlas.org/task/id/trm_4da890a9bd7a3) (close match)

