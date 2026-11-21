(hedtsk_implicit_association)=
# Implicit Association Task

**HED task ID:** `hedtsk_implicit_association`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Implicit Association Test, IAT, Implicit Association

Speeded categorization of stimuli belonging to two target concepts and two evaluative attributes using shared response keys; congruence-condition RT difference indexes implicit association.

## Description

Participants rapidly classify stimuli from four categories using two response keys. Two categories are target concepts (e.g., "flowers" vs. "insects") and two are evaluative attributes (e.g., "pleasant" vs. "unpleasant"). In the critical comparison, one block pairs congruent categories on the same key (flowers + pleasant) and another pairs incongruent categories (flowers + unpleasant). The IAT effect - faster responding in the congruent block - is interpreted as reflecting the strength of automatic associations between the concepts and attributes. Greenwald et al. (1998) introduced the IAT as a measure of implicit attitudes, and it has become one of the most widely administered psychological tests, with applications spanning racial bias, self-esteem, clinical anxiety, consumer preferences, and political attitudes.

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
  - Emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - Social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>, <a href="vocabulary.html#facet-trial-structure-blocked-trials">blocked trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-number-of-trials">number of trials</a>
- **Material:** Exemplars of two target categories (such as flowers and insects, or Black and White faces) and two attribute categories (pleasant and unpleasant words).

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants sort stimuli from two target categories (e.g., Black/White faces) and two attribute categories (e.g., pleasant/unpleasant words) using two response keys.
    2. Critical comparison is between compatible and incompatible pairings.
* - **Manipulations**
  - - Target-attribute pairing (compatible vs. incompatible blocks)
    - Category exemplars
    - Number of practice and test trials
    - Target categories (social groups, gender-science, self-other)
    - Number of target categories (single-category vs. two-category)
    - Response format (go/no-go vs. two-key sort)
    - Response mapping (four keys, cued per trial vs. fixed per block)
* - **Measurements**
  - - IAT D-score (standardized RT difference between incompatible and compatible blocks)
    - Error rates
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
* - Gender-Science IAT

    `hedvar_implicit_association__gender_science_iat`
  - emotional aspect: none
  - -
  - Male and female names or faces are paired with science and liberal-arts words, so the contrast measures a gender-field stereotype rather than valence.
* - Self-Esteem IAT

    `hedvar_implicit_association__self_esteem_iat`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>; social aspect: none
  - [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing)
  - Self and other pronouns replace the social target categories, paired with pleasant and unpleasant words.
* - Brief IAT (BIAT)

    `hedvar_implicit_association__brief_iat_biat`
  - named form
  - -
  - A named shorter instrument in which each block has two focal categories on one key and everything else on the other.
* - Go/No-Go Association Task (GNAT)

    `hedvar_implicit_association__go_no_go_association_task_gnat`
  - response demand: <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
  - [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition)
  - The participant presses one key for items in the target pairing and withholds for everything else, so detection sensitivity replaces the two-key sort.
* - Recoding-Free IAT (IAT-RF)

    `hedvar_implicit_association__recoding_free_iat_iat_rf`
  - cue: <a href="vocabulary.html#rule-respond-to-rule-cue-rule-cue">rule cue</a>; rule stability: <a href="vocabulary.html#rule-respond-to-rule-rule-stability-switches-on-cue">switches on cue</a>
  - [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting)
  - Four keys, one per category, and a per-trial instruction says which keys are relevant, so the mapping is cued trial by trial instead of fixed for a block.
* - Developmental / Child IAT

    `hedvar_implicit_association__developmental_child_iat`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>, <a href="vocabulary.html#facet-task-io-device-touchscreen">touchscreen</a>; population: <a href="vocabulary.html#facet-population-children">children</a>
  - -
  - All categories are pictures, instructions are spoken, there are fewer trials, and children sort on large buttons or a touch screen.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Stereotyping](../processes/social_cognition_and_strategic_social_choice.md#hed-stereotyping)
- [In-group/out-group processing](../processes/social_cognition_and_strategic_social_choice.md#hed-in-group-out-group-processing)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)
- [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict)
- [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control)
- [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning)

## Key references

- Greenwald, A. G., McGhee, D. E., & Schwartz, J. L. K. (1998). Measuring individual differences in implicit cognition: The Implicit Association Test. *Journal of Personality and Social Psychology*, 74(6), 1464-1480. ([DOI](https://doi.org/10.1037/0022-3514.74.6.1464), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9654756/))
- Greenwald, A. G., Nosek, B. A., & Banaji, M. R. (2003). Understanding and using the Implicit Association Test: I. An improved scoring algorithm. *Journal of Personality and Social Psychology*, 85(2), 197-216. ([DOI](https://doi.org/10.1037/0022-3514.85.2.197), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12916565/))
- Nosek, B. A., Greenwald, A. G., & Banaji, M. R. (2005). Understanding and using the Implicit Association Test: II. Method variables and construct validity. *Personality and Social Psychology Bulletin*, 31(2), 166-180. ([DOI](https://doi.org/10.1177/0146167204271418), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15619590/))

## Further references

- Greenwald, A. G., Banaji, M. R., & Nosek, B. A. (2015). Statistically small effects of the Implicit Association Test can have societally large effects. *Journal of Personality and Social Psychology*, 108(4), 553-561. ([DOI](https://doi.org/10.1037/pspa0000016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25402677/))
- Kurdi, B., Seitchik, A. E., Axt, J. R., Carroll, T. J., Karapetyan, A., Kaushik, N., ... & Banaji, M. R. (2019). Relationship between the Implicit Association Test and intergroup behavior: A meta-analysis. *American Psychologist*, 74(5), 569-586. ([DOI](https://doi.org/10.1037/amp0000364), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30550298/))
- Meissner, F., Grigutsch, L. A., Koranyi, N., Müller, F., & Rothermund, K. (2019). Predicting behavior with implicit measures: Disillusioning findings, reasonable explanations, and sophisticated solutions. *Frontiers in Psychology*, 10, 2483. ([DOI](https://doi.org/10.3389/fpsyg.2019.02483), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31787912/))
- Charlesworth, T. E. S., & Banaji, M. R. (2019). Patterns of implicit and explicit attitudes: I. Long-term change and stability from 2007 to 2016. *Psychological Science*, 30(2), 174-192. ([DOI](https://doi.org/10.1177/0956797618813087), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30605364/))

## External links

- Cognitive Atlas: [Implicit Association Task](https://www.cognitiveatlas.org/task/id/trm_50b6660b1b847)

