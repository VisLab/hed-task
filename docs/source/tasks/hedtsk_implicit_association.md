(hedtsk_implicit_association)=
# Implicit Association Task

**HED task ID:** `hedtsk_implicit_association`

**Family:** [Conflict and interference tasks](families/conflict_and_interference.md)

**Also known as:** Implicit Association Test, IAT, Implicit Association

Speeded categorization of stimuli belonging to two target concepts and two evaluative attributes using shared response keys; congruence-condition RT difference indexes implicit association.

## Description

Participants rapidly classify stimuli from four categories using two response keys. Two categories are target concepts (e.g., "flowers" vs. "insects") and two are evaluative attributes (e.g., "pleasant" vs. "unpleasant"). In the critical comparison, one block pairs congruent categories on the same key (flowers + pleasant) and another pairs incongruent categories (flowers + unpleasant). The IAT effect — faster responding in the congruent block — is interpreted as reflecting the strength of automatic associations between the concepts and attributes. Greenwald et al. (1998) introduced the IAT as a measure of implicit attitudes, and it has become one of the most widely administered psychological tests, with applications spanning racial bias, self-esteem, clinical anxiety, consumer preferences, and political attitudes.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants sort stimuli from two target categories (e.g., Black/White faces) and two attribute categories (e.g., pleasant/unpleasant words) using two response keys. Critical comparison is between compatible and incompatible pairings.
* - **Manipulation**
  - Target-attribute pairing (compatible vs. incompatible blocks); category exemplars; number of practice and test trials.
* - **Measurement**
  - IAT D-score (standardized RT difference between incompatible and compatible blocks); error rates.
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
* - Race IAT

    `hedvar_implicit_association__race_iat`
  - Black/White faces paired with pleasant/unpleasant words; the most studied version.
  - Canonical IAT measuring race-valence associations
* - Gender-Science IAT

    `hedvar_implicit_association__gender_science_iat`
  - Male/female paired with science/liberal arts; measures implicit gender-career stereotypes.
  - Gender-career associations; different conceptual domain
* - Self-Esteem IAT

    `hedvar_implicit_association__self_esteem_iat`
  - Self/other paired with pleasant/unpleasant; measures implicit self-evaluation.
  - Self-related vs. other category; different self-referential structure
* - Single-Category IAT (SC-IAT)

    `hedvar_implicit_association__single_category_iat_sc_iat`
  - Only one target category; measures absolute rather than relative associations.
  - One target category instead of two; different design structure
* - Brief IAT (BIAT)

    `hedvar_implicit_association__brief_iat_biat`
  - Shortened version with fewer trials; suited for battery administration.
  - Shorter version with different block structure; distinct published instrument
* - Go/No-Go Association Task (GNAT)

    `hedvar_implicit_association__go_no_go_association_task_gnat`
  - Related implicit measure using go/no-go responses rather than two-choice classification.
  - Detection response instead of categorization; different response structure
* - Recoding-Free IAT (IAT-RF)

    `hedvar_implicit_association__recoding_free_iat_iat_rf`
  - Eliminates recoding confound by using four response keys.
  - Response keys don't change across blocks; removes recoding confound
* - Personalized IAT (P-IAT)

    `hedvar_implicit_association__personalized_iat_p_iat`
  - Uses "I like" / "I don't like" labels instead of "pleasant" / "unpleasant"; reduces normative responding.
  - Self-relevant exemplars; different stimulus set and personal relevance
* - Developmental / Child IAT

    `hedvar_implicit_association__developmental_child_iat`
  - Simplified versions for children using pictures rather than words.
  - Picture-based categories for children; procedure adapted per §5.3
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

- Greenwald, A. G., McGhee, D. E., & Schwartz, J. L. K. (1998). Measuring individual differences in implicit cognition: The Implicit Association Test. *Journal of Personality and Social Psychology*, 74(6), 1464–1480. ([DOI](https://doi.org/10.1037/0022-3514.74.6.1464), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9654756/))
- Greenwald, A. G., Nosek, B. A., & Banaji, M. R. (2003). Understanding and using the Implicit Association Test: I. An improved scoring algorithm. *Journal of Personality and Social Psychology*, 85(2), 197–216. ([DOI](https://doi.org/10.1037/0022-3514.85.2.197), [PubMed](https://pubmed.ncbi.nlm.nih.gov/12916565/))
- Nosek, B. A., Greenwald, A. G., & Banaji, M. R. (2005). Understanding and using the Implicit Association Test: II. Method variables and construct validity. *Personality and Social Psychology Bulletin*, 31(2), 166–180. ([DOI](https://doi.org/10.1177/0146167204271418), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15619590/))

## Further references

- Greenwald, A. G., Banaji, M. R., & Nosek, B. A. (2015). Statistically small effects of the Implicit Association Test can have societally large effects. *Journal of Personality and Social Psychology*, 108(4), 553–561. ([DOI](https://doi.org/10.1037/pspa0000016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25402677/))
- Kurdi, B., Seitchik, A. E., Axt, J. R., Carroll, T. J., Karapetyan, A., Kaushik, N., ... & Banaji, M. R. (2019). Relationship between the Implicit Association Test and intergroup behavior: A meta-analysis. *American Psychologist*, 74(5), 569–586. ([DOI](https://doi.org/10.1037/amp0000364), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30550298/))
- Meissner, F., Grigutsch, L. A., Koranyi, N., Müller, F., & Rothermund, K. (2019). Predicting behavior with implicit measures: Disillusioning findings, reasonable explanations, and sophisticated solutions. *Frontiers in Psychology*, 10, 2483. ([DOI](https://doi.org/10.3389/fpsyg.2019.02483), [PubMed](https://pubmed.ncbi.nlm.nih.gov/31787912/))
- Charlesworth, T. E. S., & Banaji, M. R. (2019). Patterns of implicit and explicit attitudes: I. Long-term change and stability from 2007 to 2016. *Psychological Science*, 30(2), 174–192. ([DOI](https://doi.org/10.1177/0956797618813087), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30605364/))

## External links

- Cognitive Atlas: [Implicit Association Task](https://www.cognitiveatlas.org/task/id/trm_50b6660b1b847)

