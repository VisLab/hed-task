(hedtsk_virtual_radial_arm_maze)=
# Virtual Radial Arm Maze Task

**HED task ID:** `hedtsk_virtual_radial_arm_maze`

**Family:** [Spatial cognition and navigation tasks](families/spatial_navigation.md)

**Also known as:** Radial Arm Maze, vRAM, Virtual Radial Arm Maze, RAM

Virtual multi-arm maze in which participants retrieve rewards from each arm once; working-memory and reference-memory errors index spatial memory.

## Description

The Virtual Radial Arm Maze is a spatial memory task adapted from the rodent paradigm. Participants navigate a central platform connected to 8 (or more) radial arms, some of which contain rewards. They must visit all rewarded arms while avoiding revisits (working memory errors) and unbaited arms (reference memory errors). The task dissociates reference memory (knowing which arms are baited across trials) from working memory (remembering which arms have been visited within a trial). Virtual versions rendered on computer screens or in VR maintain the spatial navigation demands while enabling human testing with precise measurement. The task engages hippocampal spatial memory systems and has been used extensively in pharmacological and developmental research.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-navigate">navigate</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-reward-stake">reward stake</a>
- **Can the player gain, lose, or both?** <a href="vocabulary.html#motivation-sign-gain">gain</a>
- **What earns the outcome?** <a href="vocabulary.html#motivation-earned-by-performance">performance</a>
- **What is the outcome?** <a href="vocabulary.html#motivation-what-points">points</a>
- **Is the outcome real?** <a href="vocabulary.html#motivation-real-hypothetical">hypothetical</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-scenes">scenes</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-joystick">joystick</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Experimental environment:** <a href="vocabulary.html#facet-experimental-environment-virtual-world">virtual world</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-alternatives">number of alternatives</a>, <a href="vocabulary.html#setting-number-of-targets">number of targets</a>, <a href="vocabulary.html#setting-retention-interval">retention interval</a>
- **Material:** A virtual maze of eight or more arms radiating from a central platform, some baited with rewards, with cues inside or outside the maze.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. In a virtual radial arm maze (typically 8 arms radiating from a center), some arms are baited with reward.
    2. Participants visit arms to collect rewards, using spatial cues to remember which arms have been visited.
* - **Manipulations**
  - - Number of arms
    - Number of baited arms
    - Intra-maze vs. extra-maze cues
    - Delay between visits
    - Reward schedule (probabilistic vs. deterministic arm baiting)
* - **Measurements**
  - - Reference memory errors (entering never-baited arms)
    - Working memory errors (re-entering already-visited baited arms)
    - Total errors to criterion
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
* - Partially Baited Maze (4 of 8)

    `hedvar_virtual_radial_arm_maze__partially_baited_maze_4_of_8`
  - named form
  - -
  - Only the same four arms are ever baited, so the participant must also learn across trials which arms are worth entering, on top of remembering which arms were already visited in the trial.
* - Virtual Reality (Immersive VR)

    `hedvar_virtual_radial_arm_maze__virtual_reality_immersive_vr`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-head-mounted-display">head mounted display</a>, <a href="vocabulary.html#facet-task-io-device-motion-capture">motion capture</a>
  - -
  - The maze is shown in a head-mounted display that tracks head and body movement instead of on a monitor steered by joystick.
* - Maze with Landmarks

    `hedvar_virtual_radial_arm_maze__maze_with_landmarks`
  - named form
  - -
  - Distinctive objects are placed on the room walls (far) or inside the arms (near), so arms can be told apart by both distal and proximal cues.
* - Probabilistic Reward Maze

    `hedvar_virtual_radial_arm_maze__probabilistic_reward_maze`
  - named form
  - [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning)
  - Each arm pays off only some of the time, so the participant learns across trials which arms are most often rewarded rather than avoiding arms already emptied.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory)
- [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)

## Key references

- Olton, D. S., & Samuelson, R. J. (1976). Remembrance of places passed: Spatial memory in rats. *Journal of Experimental Psychology: Animal Behavior Processes*, 2(2), 97-116. ([DOI](https://doi.org/10.1037/0097-7403.2.2.97))
- Levy, L. J., Astur, R. S., & Frick, K. M. (2005). Men and women differ in object memory but not performance of a virtual radial maze. *Behavioral Neuroscience*, 119(4), 853-862. ([DOI](https://doi.org/10.1037/0735-7044.119.4.853), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16187814/))
- Astur, R. S., Tropp, J., Sava, S., Constable, R. T., & Markus, E. J. (2004). Sex differences and correlations in a virtual Morris water task, a virtual radial arm maze, and mental rotation. *Behavioural Brain Research*, 151(1-2), 103-115. ([DOI](https://doi.org/10.1016/j.bbr.2003.08.024), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15084426/))

## Further references

- Bohbot, V. D., Lerch, J., Bherer, L., Bhatt, P., & Graham, S. (2007). Gray matter differences correlate with spontaneous strategies in a human virtual navigation task. *Journal of Neuroscience*, 27(38), 10078-10083. ([DOI](https://doi.org/10.1523/JNEUROSCI.1763-07.2007))
- Korthauer, L. E., Nowak, N. T., Frahmand, M., & Driscoll, I. (2017). Cognitive correlates of spatial navigation: Associations between executive function and the virtual radial arm maze. *Behavioural Brain Research*, 317, 82-92. ([DOI](https://doi.org/10.1016/j.bbr.2016.10.007), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27720743/))
- Cánovas, R., Espínola, M., Iribarne, L., & Cimadevilla, J. M. (2008). A new virtual task to evaluate human place learning. *Behavioural Brain Research*, 190(1), 112-118. ([DOI](https://doi.org/10.1016/j.bbr.2008.02.024), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18374426/))
- Wiener, J. M., de Condappa, O., Harris, M. A., & Wolbers, T. (2013). Maladaptive bias for extrahippocampal navigation strategies in aging humans. *Journal of Neuroscience*, 33(14), 6012-6017. ([DOI](https://doi.org/10.1523/jneurosci.0717-12.2013), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23554482/))

