(hedtsk_sentence_comprehension)=
# Sentence Comprehension Task

**HED task ID:** `hedtsk_sentence_comprehension`

**Family:** [Language comprehension and production tasks](families/language.md)

**Also known as:** Garden-Path Reading, Syntactic Ambiguity Task

Reading or listening to locally ambiguous sentences; reading-time disruptions and offline comprehension indexes syntactic reanalysis.

## Description

Participants read sentences containing temporary syntactic ambiguities (garden-path sentences) that initially lead to an incorrect parse before disambiguating information forces reanalysis. Classic example: "The horse raced past the barn fell." Sentences may be presented word-by-word (self-paced reading) or while eye movements are tracked. Comprehension is assessed via subsequent questions. Neuroimaging reveals left inferior frontal and temporal activation during syntactic reanalysis. The task probes how the parser uses syntactic, semantic, and probabilistic cues in real-time language processing.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants read sentences word-by-word or in regions; some sentences contain temporary syntactic ambiguities that lead the reader down a wrong parse (garden path) before disambiguation.
* - **Manipulation**
  - Ambiguity type (main verb/reduced relative, NP/S, etc.); disambiguation point; plausibility; context sentences.
* - **Measurement**
  - Reading time at disambiguating region (self-paced reading, eye tracking); regression probability; ERP (P600, N400); comprehension question accuracy.
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
* - Self-Paced Reading (Word-by-Word)

    `hedvar_sentence_comprehension__self_paced_reading_word_by_word`
  - Reader presses button to advance; reading times index difficulty.
  - Canonical sentence processing paradigm with reading time measure
* - Eye-Tracking Reading

    `hedvar_sentence_comprehension__eye_tracking_reading`
  - Natural reading with first-pass, regression, and total time measures.
  - Natural reading with eye-tracking; different response modality and richer time course
* - Main Verb/Reduced Relative Ambiguity

    `hedvar_sentence_comprehension__main_verb_reduced_relative_ambiguity`
  - "The horse raced past the barn fell."
  - Syntactic ambiguity at main verb/relative clause; canonical garden path structure
* - PP-Attachment Ambiguity

    `hedvar_sentence_comprehension__pp_attachment_ambiguity`
  - "Put the book on the table in the box."
  - Prepositional phrase attachment ambiguity; different syntactic decision point
* - NP/S Ambiguity

    `hedvar_sentence_comprehension__np_s_ambiguity`
  - "The doctor told the patient that he was having trouble with..."
  - Noun phrase vs. sentence ambiguity; different structural ambiguity type
* - Temporarily Ambiguous vs. Unambiguous Controls

    `hedvar_sentence_comprehension__temporarily_ambiguous_vs_unambiguous_controls`
  - Matched sentence pairs for isolating reanalysis costs.
  - Matched unambiguous controls; tests processing cost of ambiguity
* - Speed-Accuracy Tradeoff (SAT) Studies

    `hedvar_sentence_comprehension__speed_accuracy_tradeoff_sat_studies`
  - Response deadlines to map time course of sentence interpretation.
  - Response deadline method; different temporal measurement approach
```

## Cognitive processes

This task is designed to engage the following processes:

- [Syntactic parsing](../processes/language_comprehension_and_production.md#hed-syntactic-parsing)
- [Sentence comprehension](../processes/language_comprehension_and_production.md#hed-sentence-comprehension)
- [Language comprehension](../processes/language_comprehension_and_production.md#hed-language-comprehension)
- [Reading](../processes/language_comprehension_and_production.md#hed-reading)
- [Error detection](../processes/inhibitory_control_and_conflict_monitoring.md#hed-error-detection)
- [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring)

## Key references

- Frazier, L., & Rayner, K. (1982). Making and correcting errors during sentence comprehension: Eye movements in the analysis of structurally ambiguous sentences. *Cognitive Psychology*, 14(2), 178-210. ([DOI](https://doi.org/10.1016/0010-0285(82)90008-1))
- Friederici, A. D. (2002). Towards a neural basis of auditory sentence processing. *Trends in Cognitive Sciences*, 6(2), 78-84. ([DOI](https://doi.org/10.1016/s1364-6613(00)01839-8), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15866191/))
- Novick, J. M., Trueswell, J. C., & Thompson-Schill, S. L. (2005). Cognitive control and parsing: Reexamining the role of Broca's area in sentence comprehension. *Cognitive, Affective, & Behavioral Neuroscience*, 5(3), 263-281. ([DOI](https://doi.org/10.3758/cabn.5.3.263), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16396089/))

## Further references

- Levy, R. (2008). Expectation-based syntactic comprehension. *Cognition*, 106(3), 1126–1177. ([DOI](https://doi.org/10.1016/j.cognition.2007.05.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17662975/))
- Fedorenko, E., & Thompson-Schill, S. L. (2014). Reworking the language network. *Trends in Cognitive Sciences*, 18(3), 120–126. ([DOI](https://doi.org/10.1016/j.tics.2013.12.006), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24440115/))
- Staub, A. (2015). The effect of lexical predictability on eye movements in reading: Critical review and theoretical interpretation. *Language and Linguistics Compass*, 9(8), 311–327. ([DOI](https://doi.org/10.1111/lnc3.12151))

## External links

- CogPO: [Syntactic Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Syntactic_Discrimination_Paradigm) (close match)

