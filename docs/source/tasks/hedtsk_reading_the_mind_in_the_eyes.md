(hedtsk_reading_the_mind_in_the_eyes)=
# Reading the Mind in the Eyes Task

**HED task ID:** `hedtsk_reading_the_mind_in_the_eyes`

**Family:** [Social cognition and social choice tasks](families/social_cognition_and_games.md)

**Also known as:** RMET, Eyes Test, Baron-Cohen Eyes Task, Reading the Mind in the Eyes Test

Choice of the best-matching mental-state word for a photograph of the eye region; accuracy indexes complex emotion and mental-state inference.

## Description

Participants view photographs showing only the eye and eyebrow region of actors and select which of four mental state descriptors best describes the person's thoughts or feelings. The revised version contains 36 photographs, each with four choices ranging from basic emotions to complex cognitive states (e.g., "sarcastic," "despondent"). The task indexes affective theory of mind and shows deficits in autism spectrum conditions. Performance correlates with amygdala and left inferior frontal gyrus activity.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** every rule takes the default of the game type
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>
  - Emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-explicit-emotion-task">explicit emotion task</a>, <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-explicit-social-task">explicit social task</a>, <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-alternatives">number of alternatives</a>, <a href="vocabulary.html#setting-number-of-trials">number of trials</a>, <a href="vocabulary.html#setting-presentation-duration">presentation duration</a>
- **Material:** Photographs of the eye region of actors' faces, each with four mental-state words ranging from basic emotions to complex states.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants view photographs of the eye region of faces and select the mental state (from four word options) that best describes what the person is thinking or feeling.
* - **Manipulations**
  - - Number of items (typically 36)
    - Response options
    - Presentation duration
    - Basic vs. complex mental states
    - Stimulus format (dynamic video vs. still photograph)
* - **Measurements**
  - - Total correct
    - Comparison to normative data
    - Errors by emotion category
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
* - RMET Short Form (15-18 items)

    `hedvar_reading_the_mind_in_the_eyes__rmet_short_form_15_18_items`
  - named form
  - -
  - A named short instrument of 15 to 18 of the same items; no design change.
* - RMET Child Version

    `hedvar_reading_the_mind_in_the_eyes__rmet_child_version`
  - population: <a href="vocabulary.html#facet-population-children">children</a>
  - -
  - A named 28-item instrument with simpler words and photographs chosen for children; no design change.
* - Dynamic Eyes Task

    `hedvar_reading_the_mind_in_the_eyes__dynamic_eyes`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>, <a href="vocabulary.html#facet-stimulus-type-film-clips">film clips</a>, <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - -
  - Short video clips of the eye region in motion replace the still photographs; the four-word choice is unchanged.
* - Full-Face vs. Eyes-Only

    `hedvar_reading_the_mind_in_the_eyes__full_face_vs_eyes_only`
  - named form
  - -
  - The same choices are made for whole faces in one condition and the eye region alone in another, to measure what is lost when only the eyes are visible.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking)
- [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition)
- [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception)
- [Face perception](../processes/face_and_object_perception.md#hed-face-perception)

## Key references

- Baron-Cohen, S., Wheelwright, S., Hill, J., Raste, Y., & Plumb, I. (2001). The "Reading the Mind in the Eyes" test revised version: A study with normal adults, and adults with Asperger syndrome or high-functioning autism. *Journal of Child Psychology and Psychiatry*, 42(2), 241-251. ([DOI](https://doi.org/10.1111/1469-7610.00715), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11280420/))
- Adams, R. B., Rule, N. O., Franklin, R. G., et al. (2010). Cross-cultural reading the mind in the eyes: An fMRI investigation. *Journal of Cognitive Neuroscience*, 22(1), 97-108. ([DOI](https://doi.org/10.1162/jocn.2009.21187), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19199419/))
- Oakley, B. F. M., Brewer, R., Bird, G., & Catmur, C. (2016). Theory of mind is not theory of emotion: A cautionary note on the Reading the Mind in the Eyes Test. *Journal of Abnormal Psychology*, 125(6), 818-823. ([DOI](https://doi.org/10.1037/abn0000182), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27505409/))

## Further references

- Olderbak, S., Wilhelm, O., Olaru, G., et al. (2015). A psychometric analysis of the Reading the Mind in the Eyes test: Toward a brief form. *Frontiers in Psychology*, 6, 1503. ([DOI](https://doi.org/10.3389/fpsyg.2015.01503), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26500578/))
- Warrier, V., Grasby, K. L., Uzefovsky, F., et al. (2018). Genome-wide meta-analysis of cognitive empathy: Heritability and correlates with sex, neuropsychiatric conditions and cognition. *Molecular Psychiatry*, 23(6), 1402-1409. ([DOI](https://doi.org/10.1038/mp.2017.122))
- Vellante, M., Baron-Cohen, S., Melis, M., et al. (2013). The "Reading the Mind in the Eyes" test: Systematic review of psychometric properties and a validation study in Italy. *Cognitive Neuropsychiatry*, 18(4), 326-354. ([DOI](https://doi.org/10.1080/13546805.2012.721728), [PubMed](https://pubmed.ncbi.nlm.nih.gov/23106125/))

## External links

- CogPO: [Theory of Mind Task Paradigm](http://www.wiki.cogpo.org/index.php?title=Theory_of_Mind_Task_Paradigm) (close match)

