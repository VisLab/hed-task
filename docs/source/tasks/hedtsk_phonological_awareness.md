(hedtsk_phonological_awareness)=
# Phonological Awareness Task

**HED task ID:** `hedtsk_phonological_awareness`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Rhyme Judgment, Phoneme Deletion

Rhyme judgment, phoneme deletion, or phoneme blending tasks index sensitivity to the sound structure of language.

## Description

Participants view or hear pairs of words and judge whether they rhyme. The task requires analysis of the sound structure of words, comparison of phonological representations, and a binary decision. Control conditions involve matching for orthographic similarity or judging word identity. fMRI reveals activation in left inferior frontal regions (pars opercularis), left temporoparietal areas, and left superior temporal cortex. The task is widely used in reading research and dyslexia studies, as phonological awareness is a strong predictor of reading ability.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-compare">compare</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-words">words</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Material:** Spoken words (or nonwords) of varying complexity, judged for rhyme, onset, blending or the sounds left when a phoneme is deleted.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants make explicit judgments about the sound structure of spoken words: rhyme detection, phoneme deletion, phoneme segmentation, or blending.
* - **Manipulations**
  - - Task type (rhyme, onset, phoneme deletion, blending)
    - Word complexity
    - Real word vs. nonword targets
* - **Measurements**
  - - Accuracy
    - RT
    - Correlation with reading ability in developmental populations
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
* - Rhyme Oddity

    `hedvar_phonological_awareness__rhyme_oddity`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-identify">identify</a>
  - -
  - Three or four words are heard and the participant picks the one that does not rhyme, instead of judging whether a pair rhymes.
* - Rhyme Production

    `hedvar_phonological_awareness__rhyme_production`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-generate">generate</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)
  - One word is heard and the participant produces words that rhyme with it instead of judging a given pair.
* - Onset Detection

    `hedvar_phonological_awareness__onset_detection`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-identify">identify</a>
  - -
  - The participant names the first sound of a spoken word (or, in a second form, judges whether two words share an onset, which keeps compare); the unit is the onset rather than the rhyme.
* - Phoneme Deletion

    `hedvar_phonological_awareness__phoneme_deletion`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-generate">generate</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)
  - The participant removes a named sound from a spoken word and says what is left, producing a new item rather than judging one.
* - Phoneme Substitution

    `hedvar_phonological_awareness__phoneme_substitution`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-generate">generate</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)
  - The participant replaces one sound in a spoken word with another and says the new word; a task type not enumerated in the list.
* - Phoneme Segmentation

    `hedvar_phonological_awareness__phoneme_segmentation`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-generate">generate</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)
  - The participant says each sound of a word separately and in order (in some versions counts them) instead of judging a pair.
* - Blending

    `hedvar_phonological_awareness__blending`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-generate">generate</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production)
  - The sounds of a word are played one at a time and the participant says the word they make, so the input is phonemes and the output a generated word.
* - Spoonerisms

    `hedvar_phonological_awareness__spoonerisms`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-generate">generate</a>
  - [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production), [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory)
  - Two words are heard and the participant swaps their first sounds and says the result, generating two new words while holding both in mind; a task type not enumerated in the list.
* - Syllable Awareness Tasks

    `hedvar_phonological_awareness__syllable_awareness_tasks`
  - population: <a href="vocabulary.html#facet-population-children">children</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-count">count</a>
  - -
  - The unit is the syllable rather than the phoneme and children count or tap them (the deletion and blending forms would be generate); an easier form for younger children.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Phonological awareness](../processes/language_comprehension_and_production.md#hed-phonological-awareness)
- [Phonological encoding](../processes/language_comprehension_and_production.md#hed-phonological-encoding)
- [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
- [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization)

## Key references

- Shaywitz, S. E., Shaywitz, B. A., Pugh, K. R., et al. (1998). Functional disruption in the organization of the brain for reading in dyslexia. *Proceedings of the National Academy of Sciences*, 95(5), 2636-2641. ([DOI](https://doi.org/10.1073/pnas.95.5.2636), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9482939/))
- Booth, J. R., Burman, D. D., Meyer, J. R., et al. (2004). Development of brain mechanisms for processing orthographic and phonological representations. *Journal of Cognitive Neuroscience*, 16(7), 1234-1249. ([DOI](https://doi.org/10.1162/0898929041920496), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15453976/))
- Pugh, K. R., Mencl, W. E., Jenner, A. R., et al. (2001). Neurobiological studies of reading and reading disability. *Journal of Communication Disorders*, 34(6), 479-492. ([DOI](https://doi.org/10.1016/s0021-9924(01)00060-0), [PubMed](https://pubmed.ncbi.nlm.nih.gov/11725860/))

## Further references

- Melby-Lervåg, M., Lyster, S. A. H., & Hulme, C. (2012). Phonological skills and their role in learning to read: A meta-analytic review. *Psychological Bulletin*, 138(2), 322-352. ([DOI](https://doi.org/10.1037/a0026744), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22250824/))
- Anthony, J. L., & Francis, D. J. (2005). Development of phonological awareness. *Current Directions in Psychological Science*, 14(5), 255-259. ([DOI](https://doi.org/10.1111/j.0963-7214.2005.00376.x))
- Boets, B., Op de Beeck, H. P., Vandermosten, M., et al. (2013). Intact but less accessible phonetic representations in adults with dyslexia. *Science*, 342(6163), 1251-1254. ([DOI](https://doi.org/10.1126/science.1244333), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24311693/))

## External links

- Cognitive Atlas: [rhyme verification task](https://www.cognitiveatlas.org/task/id/trm_4d949c5b0e380) (related match)

- CogPO: [Phonological Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Phonological_Discrimination_Paradigm)

