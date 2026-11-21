(hedtsk_weapons_identification)=
# Weapons Identification Task

**HED task ID:** `hedtsk_weapons_identification`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md) (also [Social cognition and social choice tasks](families/social_cognition_and_games.md))

**Also known as:** Shooter Bias Task, Weapons Task, Payne Task

Speeded categorization of tools vs weapons primed by faces of varying race; congruence effects index implicit racial bias in perception.

## Description

Participants view face primes (typically Black and White faces, presented briefly) followed by target objects that are either weapons (guns, knives) or non-threatening objects (tools, household items). Participants must rapidly classify the target object while ignoring the face prime. The paradigm measures implicit racial bias through two routes: behavioral errors (misclassifying tools as weapons more often after Black face primes) and EEG markers of error monitoring (enhanced ERN on racially biased error trials). The ERN enhancement on bias-consistent errors indicates that the anterior cingulate cortex detects the conflict between egalitarian goals and automatic stereotype-driven responses, with ERN amplitude predicting subsequent behavioral correction. This paradigm bridges social psychology, implicit cognition, and cognitive neuroscience by providing a neural signature of bias detection.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What competes with the correct response?* <a href="vocabulary.html#rule-respond-to-rule-competitor-preceding-prime">preceding prime</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>, <a href="vocabulary.html#setting-response-deadline">response deadline</a>
- **Material:** A briefly shown Black or White face followed by a picture of a weapon (gun, knife) or a tool.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A face (Black or White) is flashed briefly, followed by an object (weapon or tool).
    2. Participants classify the object.
    3. Racial bias is indexed by differential accuracy or speed.
* - **Manipulations**
  - - Face race
    - Object type (weapon vs. tool)
    - Presentation duration
    - Response deadline
* - **Measurements**
  - - Signal-detection measures of racial bias (criterion shift)
    - Error rate for weapon/tool by face race
    - RT differences
    - Shooter bias (shoot/don't-shoot variants)
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
* - First-Person Shooter Task (Correll et al., 2002)

    `hedvar_weapons_identification__first_person_shooter_task_correll_et_al_2002`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; competitor: <a href="vocabulary.html#rule-respond-to-rule-competitor-irrelevant-dimension">irrelevant dimension</a>
  - -
  - Face and object are combined in one photograph of a man holding a gun or a harmless object, so the race competitor is an irrelevant dimension of the judged picture rather than a preceding prime, and the shoot/don't-shoot response is made within a deadline.
* - Weapons Task in Virtual Reality

    `hedvar_weapons_identification__weapons_task_in_virtual_reality`
  - experimental environment: <a href="vocabulary.html#facet-experimental-environment-virtual-world">virtual world</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-head-mounted-display">head mounted display</a>, <a href="vocabulary.html#facet-task-io-device-handheld-controller">handheld controller</a>
  - -
  - The shooter scenes are presented in an immersive virtual environment and the participant aims and pulls a trigger on a hand-held controller.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Stereotyping](../processes/social_cognition_and_strategic_social_choice.md#hed-stereotyping)
- [In-group/out-group processing](../processes/social_cognition_and_strategic_social_choice.md#hed-in-group-out-group-processing)
- [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
- [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition)
- [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict)
- [Perceptual decision making](../processes/perceptual_decision_making_evidence_accumulation.md#hed-perceptual-decision-making)

## Key references

- Amodio, D. M., Harmon-Jones, E., Devine, P. G., Curtin, J. J., Hartley, S. L., & Covert, A. E. (2004). Neural signals for the detection of unintentional race bias. *Psychological Science*, 15(2), 88-93. ([DOI](https://doi.org/10.1111/j.0963-7214.2004.01502003.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/14738514/))
- Payne, B. K. (2001). Prejudice and perception: The role of automatic and controlled processes in misperceiving a weapon. *Journal of Personality and Social Psychology*, 81(2), 181-192. ([DOI](https://doi.org/10.1037/0022-3514.81.2.181), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11519925/))
- Bartholow, B. D., Pearson, M. A., Dickter, C. L., Sher, K. J., Fabiani, M., & Gratton, G. (2005). Strategic control and medial frontal negativity: Beyond errors and response conflict. *Psychophysiology*, 42(1), 33-42. ([DOI](https://doi.org/10.1111/j.1469-8986.2005.00258.x), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15720579/))

## Further references

- Amodio, D. M. (2014). The neuroscience of prejudice and stereotyping. *Nature Reviews Neuroscience*, 15(10), 670-682. ([DOI](https://doi.org/10.1038/nrn3800), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25186236/))
- Correll, J., Park, B., Judd, C. M., & Wittenbrink, B. (2002). The police officer's dilemma: Using ethnicity to disambiguate potentially threatening individuals. *Journal of Personality and Social Psychology*, 83(6), 1314-1329. ([DOI](https://doi.org/10.1037/0022-3514.83.6.1314), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12500813/))
- Amodio, D. M., & Cikara, M. (2021). The social neuroscience of prejudice. *Annual Review of Psychology*, 72, 439-469. ([DOI](https://doi.org/10.1146/annurev-psych-010419-050928), [PubMed](https://pubmed.ncbi.nlm.nih.gov/32946320/))
- Correll, J., Hudson, S. M., Guillermo, S., & Ma, D. S. (2014). The police officer's dilemma: A decade of research on racial bias in the decision to shoot. *Social and Personality Psychology Compass*, 8(5), 201-213. ([DOI](https://doi.org/10.1111/spc3.12099))

