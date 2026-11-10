(hedtsk_phonological_awareness)=
# Phonological Awareness Task

**HED task ID:** `hedtsk_phonological_awareness`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Rhyme Judgment, Phoneme Deletion

Rhyme judgment, phoneme deletion, or phoneme blending tasks index sensitivity to the sound structure of language.

## Description

Participants view or hear pairs of words and judge whether they rhyme. The task requires analysis of the sound structure of words, comparison of phonological representations, and a binary decision. Control conditions involve matching for orthographic similarity or judging word identity. fMRI reveals activation in left inferior frontal regions (pars opercularis), left temporoparietal areas, and left superior temporal cortex. The task is widely used in reading research and dyslexia studies, as phonological awareness is a strong predictor of reading ability.

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

## Variations

Named versions that change what the participant experiences or does. The identifier
of a variation is `hedvar_<task>__<variation>`.

```{list-table}
:widths: 25 40 35
:header-rows: 1

* - Variation
  - Description
  - Justification
* - Rhyme Detection

    `hedvar_phonological_awareness__rhyme_detection`
  - Two spoken words are presented and the participant says whether they rhyme, for example 'cat' and 'hat' (yes) or 'cat' and 'cup' (no).
  - Participant judges whether words rhyme; canonical phonological awareness task
* - Rhyme Oddity

    `hedvar_phonological_awareness__rhyme_oddity`
  - Three or four spoken words are presented, all but one rhyming, and the participant picks the one that does not rhyme, such as 'book' from 'cat, hat, book'.
  - Identify non-rhyming word in set; different task structure from detection
* - Rhyme Production

    `hedvar_phonological_awareness__rhyme_production`
  - A word is spoken and the participant produces one or more words that rhyme with it.
  - Generate rhyming words; different output requirement
* - Onset Detection

    `hedvar_phonological_awareness__onset_detection`
  - A word is spoken and the participant says its first sound, or judges whether two words begin with the same sound.
  - Judge initial consonant; different phonological unit (onset)
* - Phoneme Deletion

    `hedvar_phonological_awareness__phoneme_deletion`
  - A word is spoken and the participant says what is left when a given sound is removed, for example 'boat' without the /b/ gives 'oat'.
  - Delete specified phoneme and report result; manipulation task
* - Phoneme Substitution

    `hedvar_phonological_awareness__phoneme_substitution`
  - A word is spoken and the participant replaces one sound with another, for example changing the /k/ in 'cat' to /h/ to give 'hat'.
  - Replace phoneme in word; different manipulation operation
* - Phoneme Segmentation

    `hedvar_phonological_awareness__phoneme_segmentation`
  - A word is spoken and the participant says each of its sounds separately in order, or counts them, for example 'dog' has three sounds: /d/, /o/, /g/.
  - Segment word into constituent phonemes; decomposition task
* - Blending

    `hedvar_phonological_awareness__blending`
  - The sounds of a word are spoken one at a time with gaps (/s/ ... /u/ ... /n/) and the participant says the word they make ('sun').
  - Combine phonemes to form word; synthesis operation
* - Spoonerisms

    `hedvar_phonological_awareness__spoonerisms`
  - Two words are spoken and the participant swaps their first sounds, for example 'fed bull' becomes 'bed full'. Requires holding both words while rearranging them.
  - Transpose onset phonemes of two words; complex transposition manipulation
* - Alliteration Detection

    `hedvar_phonological_awareness__alliteration_detection`
  - Two or more spoken words are presented and the participant says whether they begin with the same sound, or picks the one that does not.
  - Detect shared onset consonant; different phonological judgment
* - Syllable Awareness Tasks

    `hedvar_phonological_awareness__syllable_awareness_tasks`
  - The units are syllables rather than single sounds: the participant counts the syllables in a word, taps them out, deletes one ('sunshine' without 'sun'), or blends syllables into a word. Easier than the sound-level tasks and used with younger children.
  - Syllable-level operations instead of phoneme-level; different linguistic unit
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

- Melby-Lervåg, M., Lyster, S. A. H., & Hulme, C. (2012). Phonological skills and their role in learning to read: A meta-analytic review. *Psychological Bulletin*, 138(2), 322–352. ([DOI](https://doi.org/10.1037/a0026744), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22250824/))
- Anthony, J. L., & Francis, D. J. (2005). Development of phonological awareness. *Current Directions in Psychological Science*, 14(5), 255–259. ([DOI](https://doi.org/10.1111/j.0963-7214.2005.00376.x))
- Boets, B., Op de Beeck, H. P., Vandermosten, M., et al. (2013). Intact but less accessible phonetic representations in adults with dyslexia. *Science*, 342(6163), 1251–1254. ([DOI](https://doi.org/10.1126/science.1244333), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24311693/))

## External links

- Cognitive Atlas: [rhyme verification task](https://www.cognitiveatlas.org/task/id/trm_4d949c5b0e380) (related match)

- CogPO: [Phonological Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Phonological_Discrimination_Paradigm)

