(hedtsk_false_belief)=
# False Belief Task

**HED task ID:** `hedtsk_false_belief`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Sally-Anne Task, Theory of Mind Task, ToM Task

Wimmer & Perner-style narrative in which a protagonist holds a belief the participant knows to be false; correct prediction of the protagonist's action indexes mentalizing.

## Description

The False Belief Task assesses the ability to attribute mental states to others that differ from reality. In the classic Sally-Anne version, Sally places an object in location A and leaves; Anne moves the object to location B. Participants are asked where Sally will look for the object. Correct performance (location A) requires representing Sally's false belief rather than the true state of the world. Adult neuroimaging versions use animated vignettes requiring belief reasoning. fMRI consistently activates medial prefrontal cortex, precuneus, and right temporoparietal junction.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-solve-problem">solve problem</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>, <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-text">text</a>, <a href="vocabulary.html#facet-stimulus-type-real-objects">real objects</a>
- **Social aspect:** <a href="vocabulary.html#facet-social-aspect-explicit-social-task">explicit social task</a>, <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-examiner">examiner</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Population:** <a href="vocabulary.html#facet-population-children">children</a>
- **Material:** Short stories, told, read or acted out with pictures or objects, in which a character believes an object is where it no longer is (the Sally-Anne scenario).

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants hear or read vignettes in which a character holds a belief that conflicts with reality (e.g., Sally-Anne scenario), then predict the character's behavior.
* - **Manipulations**
  - - True belief vs. false belief conditions
    - First-order vs. second-order belief attribution
    - Verbal vs. nonverbal response
    - Story complexity
    - Story type (unexpected contents vs. moved object)
    - Belief structure (two differing beliefs, neither false)
    - Task type (animated shapes described vs. false belief question)
    - Story format (text, speech or cartoon vs. acted with props)
    - Competition (planting a false belief against an opponent)
* - **Measurements**
  - - Accuracy on false-belief vs. true-belief questions
    - RT
    - pass/fail classification in developmental studies
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
* - Implicit False Belief (Looking Time)

    `hedvar_false_belief__implicit_false_belief_looking_time`
  - population: <a href="vocabulary.html#facet-population-infants">infants</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-eye-tracker">eye tracker</a>
  - -
  - Infants watch an actor search where the actor should believe the object is or where it really is, and looking time is recorded; no question is asked.
* - Anticipatory Looking

    `hedvar_false_belief__anticipatory_looking`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-eye-tracker">eye tracker</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>
  - -
  - The answer is where the participant looks just before the character acts, recorded by an eye tracker, instead of a spoken answer.
* - Animated Triangles (Heider-Simmel)

    `hedvar_false_belief__animated_triangles_heider_simmel`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>, <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-explicit-social-task">explicit social task</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - -
  - The participant watches shapes move as if with intentions and describes what happened, scored for mental-state language; there is no false belief and no correct answer.
* - Cartoon/Story Vignette Tasks

    `hedvar_false_belief__cartoon_story_vignette_tasks`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-text">text</a>, <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>
  - -
  - The false-belief story is given as text, speech or a cartoon strip rather than acted with props.
* - Adult False Belief with Reaction Time

    `hedvar_false_belief__adult_false_belief_with_reaction_time`
  - population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-text">text</a>, <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>; trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - -
  - Adults answer many short scenarios by speeded key press, so the answer is a choice among keys and response time is the measure.
* - Competitive False Belief (Deception)

    `hedvar_false_belief__competitive_false_belief_deception`
  - social aspect: <a href="vocabulary.html#facet-social-aspect-social-interaction">social interaction</a>, <a href="vocabulary.html#facet-social-aspect-explicit-social-task">explicit social task</a>; drive: <a href="vocabulary.html#motivation-drive-reward-goal">reward goal</a>; sign: <a href="vocabulary.html#motivation-sign-gain">gain</a>; earned by: <a href="vocabulary.html#motivation-earned-by-joint-moves">joint moves</a>; combined with: <a href="vocabulary.html#how-chained">chained</a>, <a href="vocabulary.html#game-interact-with-agent">interact with agent</a> (The belief worked out decides the move against an opponent)
  - [Competition](../processes/social_cognition_and_strategic_social_choice.md#hed-competition)
  - The participant plays against a real opponent and wins by planting a false belief, for example by pointing to the wrong hiding place, so the answer becomes a move in a game rather than a report.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking)
- [Self-other distinction](../processes/social_cognition_and_strategic_social_choice.md#hed-self-other-distinction)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)
- [Language comprehension](../processes/language_comprehension_and_production.md#hed-language-comprehension)

## Key references

- Baron-Cohen, S., Leslie, A. M., & Frith, U. (1985). Does the autistic child have a "theory of mind"? *Cognition*, 21(1), 37-46. ([DOI](https://doi.org/10.1016/0010-0277(85)90022-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/2934210/))
- Saxe, R., & Kanwisher, N. (2003). People thinking about thinking people: The role of the temporo-parietal junction in "theory of mind." *NeuroImage*, 19(4), 1835-1842. ([DOI](https://doi.org/10.1016/s1053-8119(03)00230-1), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12948738/))
- Wimmer, H., & Perner, J. (1983). Beliefs about beliefs: Representation and constraining function of wrong beliefs in young children's understanding of deception. *Cognition*, 13(1), 103-128. ([DOI](https://doi.org/10.1016/0010-0277(83)90004-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6681741/))

## Further references

- Schurz, M., Radua, J., Aichhorn, M., Richlan, F., & Perner, J. (2014). Fractionating theory of mind: A meta-analysis of functional brain imaging studies. *Neuroscience & Biobehavioral Reviews*, 42, 9-34. ([DOI](https://doi.org/10.1016/j.neubiorev.2014.01.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24486722/))
- Apperly, I. A. (2012). What is "theory of mind"? Concepts, cognitive processes and individual differences. *Quarterly Journal of Experimental Psychology*, 65(5), 825-839. ([DOI](https://doi.org/10.1080/17470218.2012.676055), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22533318/))
- Wellman, H. M., Cross, D., & Watson, J. (2001). Meta-analysis of theory-of-mind development: The truth about false belief. *Child Development*, 72(3), 655-684. ([DOI](https://doi.org/10.1111/1467-8624.00304), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11405571/))
- Onishi, K. H., & Baillargeon, R. (2005). Do 15-month-old infants understand false beliefs? *Science*, 308(5719), 255-258. [Updated: Baillargeon, R., Scott, R. M., & Bian, L. (2016). Psychological reasoning in infancy. *Annual Review of Psychology*, 67, 159-186.] ([DOI](https://doi.org/10.1126/science.1107621), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15821091/))
- Apperly, I. A., & Butterfill, S. A. (2009). Do humans have two systems to track beliefs and belief-like states? *Psychological Review*, 116(4), 953-970. ([DOI](https://doi.org/10.1037/a0016923), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19839692/))
- Kulke, L., & Rakoczy, H. (2018). Implicit Theory of Mind: An overview of current replications and non-replications. *Data in Brief*, 16, 101-104. ([DOI](https://doi.org/10.1016/j.dib.2017.11.016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29188228/))

## External links

- Cognitive Atlas: [false belief task](https://www.cognitiveatlas.org/task/id/trm_4f2456027809f)

- CogPO: [Theory of Mind Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Theory_of_Mind_Task_Paradigm) (close match)

