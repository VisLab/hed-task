(hedtsk_false_belief)=
# False Belief Task

**HED task ID:** `hedtsk_false_belief`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** Sally-Anne Task, Theory of Mind Task, ToM Task

Wimmer & Perner–style narrative in which a protagonist holds a belief the participant knows to be false; correct prediction of the protagonist's action indexes mentalizing.

## Description

The False Belief Task assesses the ability to attribute mental states to others that differ from reality. In the classic Sally-Anne version, Sally places an object in location A and leaves; Anne moves the object to location B. Participants are asked where Sally will look for the object. Correct performance (location A) requires representing Sally's false belief rather than the true state of the world. Adult neuroimaging versions use animated vignettes requiring belief reasoning. fMRI consistently activates medial prefrontal cortex, precuneus, and right temporoparietal junction.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants hear or read vignettes in which a character holds a belief that conflicts with reality (e.g., Sally-Anne scenario), then predict the character's behavior.
* - **Manipulation**
  - True belief vs. false belief conditions; first-order vs. second-order belief attribution; verbal vs. nonverbal response; story complexity.
* - **Measurement**
  - Accuracy on false-belief vs. true-belief questions; RT; pass/fail classification in developmental studies.
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
* - Sally-Anne / Change-of-Location

    `hedvar_false_belief__sally_anne_change_of_location`
  - Classic location-change false belief.
  - Classic change-of-location false belief; canonical ToM paradigm
* - Unexpected Contents (Smarties/Crayon Box)

    `hedvar_false_belief__unexpected_contents_smarties_crayon_box`
  - Deceptive container contents; test belief prediction.
  - Container with unexpected content; different scenario structure
* - Second-Order False Belief

    `hedvar_false_belief__second_order_false_belief`
  - "She thinks that he thinks..." Multi-level recursion.
  - Belief about another's belief; higher-order recursive ToM
* - Diverse Beliefs Task

    `hedvar_false_belief__diverse_beliefs`
  - Multiple agents with different beliefs.
  - Two agents with different beliefs about same object; tests belief diversity understanding
* - Implicit False Belief (Looking Time)

    `hedvar_false_belief__implicit_false_belief_looking_time`
  - Violation-of-expectation paradigms for preverbal infants.
  - Looking time measure of anticipation; no verbal response required
* - Anticipatory Looking

    `hedvar_false_belief__anticipatory_looking`
  - Eye-tracking measures of predictive belief processing.
  - Eye-tracking where agent will look; different response modality
* - Animated Triangles (Heider-Simmel)

    `hedvar_false_belief__animated_triangles_heider_simmel`
  - Social attribution from geometric motion.
  - Geometric shapes with attributed mental states; different stimulus and attribution task
* - Cartoon/Story Vignette Tasks

    `hedvar_false_belief__cartoon_story_vignette_tasks`
  - Belief reasoning from narrative contexts.
  - Story-based false belief; different presentation format
* - Belief-Desire Reasoning

    `hedvar_false_belief__belief_desire_reasoning`
  - Combining false beliefs with differing desires.
  - Combines belief and desire attribution; more complex ToM reasoning
* - Adult False Belief with Reaction Time

    `hedvar_false_belief__adult_false_belief_with_reaction_time`
  - Adapted for adults using stories or videos with reaction-time dependent measures.
  - RT version for adults; measures implicit processing speed alongside accuracy
* - Competitive False Belief (Deception)

    `hedvar_false_belief__competitive_false_belief_deception`
  - Participant must deceive another agent by exploiting their false belief; tests active use of ToM.
  - Strategic deception context; tests belief reasoning under competitive motivation
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
- Wimmer, H., & Perner, J. (1983). Beliefs about beliefs: Representation and constraining function of wrong beliefs in young children's understanding of deception. *Cognition*, 13(1), 103–128. ([DOI](https://doi.org/10.1016/0010-0277(83)90004-5), [PubMed](https://pubmed.ncbi.nlm.nih.gov/6681741/))

## Further references

- Schurz, M., Radua, J., Aichhorn, M., Richlan, F., & Perner, J. (2014). Fractionating theory of mind: A meta-analysis of functional brain imaging studies. *Neuroscience & Biobehavioral Reviews*, 42, 9–34. ([DOI](https://doi.org/10.1016/j.neubiorev.2014.01.009), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24486722/))
- Apperly, I. A. (2012). What is "theory of mind"? Concepts, cognitive processes and individual differences. *Quarterly Journal of Experimental Psychology*, 65(5), 825–839. ([DOI](https://doi.org/10.1080/17470218.2012.676055), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22533318/))
- Wellman, H. M., Cross, D., & Watson, J. (2001). Meta-analysis of theory-of-mind development: The truth about false belief. *Child Development*, 72(3), 655–684. ([DOI](https://doi.org/10.1111/1467-8624.00304), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11405571/))
- Onishi, K. H., & Baillargeon, R. (2005). Do 15-month-old infants understand false beliefs? *Science*, 308(5719), 255–258. [Updated: Baillargeon, R., Scott, R. M., & Bian, L. (2016). Psychological reasoning in infancy. *Annual Review of Psychology*, 67, 159–186.] ([DOI](https://doi.org/10.1126/science.1107621), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15821091/))
- Apperly, I. A., & Butterfill, S. A. (2009). Do humans have two systems to track beliefs and belief-like states? *Psychological Review*, 116(4), 953–970. ([DOI](https://doi.org/10.1037/a0016923), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19839692/))
- Kulke, L., & Rakoczy, H. (2018). Implicit Theory of Mind: An overview of current replications and non-replications. *Data in Brief*, 16, 101–104. ([DOI](https://doi.org/10.1016/j.dib.2017.11.016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/29188228/))

## External links

- Cognitive Atlas: [false belief task](https://www.cognitiveatlas.org/task/id/trm_4f2456027809f)

