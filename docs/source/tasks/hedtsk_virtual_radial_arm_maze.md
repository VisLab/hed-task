(hedtsk_virtual_radial_arm_maze)=
# Virtual Radial Arm Maze Task

**HED task ID:** `hedtsk_virtual_radial_arm_maze`

**Family:** [Spatial cognition and navigation tasks](families/spatial_navigation.md)

**Also known as:** Radial Arm Maze, vRAM, Virtual Radial Arm Maze, RAM

Virtual multi-arm maze in which participants retrieve rewards from each arm once; working-memory and reference-memory errors index spatial memory.

## Description

The Virtual Radial Arm Maze is a spatial memory task adapted from the rodent paradigm. Participants navigate a central platform connected to 8 (or more) radial arms, some of which contain rewards. They must visit all rewarded arms while avoiding revisits (working memory errors) and unbaited arms (reference memory errors). The task dissociates reference memory (knowing which arms are baited across trials) from working memory (remembering which arms have been visited within a trial). Virtual versions rendered on computer screens or in VR maintain the spatial navigation demands while enabling human testing with precise measurement. The task engages hippocampal spatial memory systems and has been used extensively in pharmacological and developmental research.

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
* - **Measurements**
  - - Reference memory errors (entering never-baited arms)
    - Working memory errors (re-entering already-visited baited arms)
    - Total errors to criterion
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
* - Standard 8-Arm Radial Maze

    `hedvar_virtual_radial_arm_maze__standard_8_arm_radial_maze`
  - The participant stands at the center of a virtual maze with eight corridors radiating outward, each with a reward at the far end. They visit arms to collect rewards; once an arm has been visited its reward is gone. Returning to an already emptied arm is a working-memory error.
  - Canonical 8-arm maze with bait at end of each arm
* - Partially Baited Maze (4 of 8)

    `hedvar_virtual_radial_arm_maze__partially_baited_maze_4_of_8`
  - Only four of the eight arms ever contain rewards, and it is always the same four across trials. Entering a never-rewarded arm is a reference-memory error (failing to learn the fixed rule), while re-entering an arm already emptied on this trial is a working-memory error.
  - Only subset of arms baited; tests working memory for visited arms
* - 12-Arm or 16-Arm Versions

    `hedvar_virtual_radial_arm_maze__12_arm_or_16_arm_versions`
  - The maze has twelve or sixteen arms instead of eight, so more locations have to be kept in mind before the trial is complete.
  - Increased arm number; higher memory load
* - Virtual Reality (Immersive VR)

    `hedvar_virtual_radial_arm_maze__virtual_reality_immersive_vr`
  - The maze is presented in a head-mounted display that updates with the participant's head and body movement, so they turn and look around as they would in a real maze.
  - Head-mounted display VR; full immersive spatial navigation
* - Desktop Virtual Maze

    `hedvar_virtual_radial_arm_maze__desktop_virtual_maze`
  - The maze is shown on an ordinary monitor from a first-person viewpoint and the participant moves with a keyboard, mouse or joystick.
  - Screen-based navigation; different motor control
* - Maze with Landmarks

    `hedvar_virtual_radial_arm_maze__maze_with_landmarks`
  - Distinctive objects or pictures are placed around the maze, either on the walls of the room (far landmarks) or within the arms (near landmarks), so that arms can be told apart and remembered by what is near them.
  - Salient landmarks aid navigation; tests landmark use
* - Cue-Removed Conditions

    `hedvar_virtual_radial_arm_maze__cue_removed_conditions`
  - After learning with landmarks, the landmarks are removed or the maze is rotated so that landmarks no longer help. The participant must rely on remembering their own movements.
  - Landmarks removed mid-experiment; tests spatial memory without cues
* - Delay Variants

    `hedvar_virtual_radial_arm_maze__delay_variants`
  - After visiting some of the arms, the participant is held at the center or taken out of the maze for a delay of minutes before being allowed to finish, so that the visited arms must be remembered across the delay.
  - Delay between choices tests retention
* - Probabilistic Reward Maze

    `hedvar_virtual_radial_arm_maze__probabilistic_reward_maze`
  - Each arm pays off only some of the time rather than always, so the participant must learn which arms are most often rewarded instead of simply avoiding arms already visited.
  - Arms probabilistically rather than deterministically rewarded
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

