(hedtsk_autobiographical_memory)=
# Autobiographical Memory Task

**HED task ID:** `hedtsk_autobiographical_memory`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md) (also [Self-report tasks](families/self_report.md))

**Also known as:** Autobiographical Memory Interview, AMI, Cue-Word Autobiographical Memory Task, Galton-Crovitz Task, Autobiographical Memory Test

Participants retrieve specific personal memories in response to cue words or structured prompts; specificity, detail, and temporal distribution of retrieved episodes index autobiographical memory function.

## Description

Autobiographical memory tasks assess the ability to retrieve specific personal episodes from one's past. The Galton-Crovitz cue-word task presents generic words (e.g., 'garden,' 'river,' 'knife') and asks participants to retrieve a specific personal memory associated with each and date it. The Autobiographical Memory Interview (Kopelman, Wilson, & Baddeley, 1989) uses a structured interview format probing both personal semantic knowledge (names, addresses) and autobiographical incidents across life periods (childhood, early adulthood, recent). The Autobiographical Memory Test (Williams & Broadbent, 1986) presents positive and negative cue words and measures whether participants retrieve specific episodes (bounded in time and place) vs. overgeneral memories (categories or extended periods). Overgeneral autobiographical memory - the tendency to retrieve categorical summaries rather than specific episodes - is a robust marker of depression, PTSD, and suicidality. The temporal distribution of memories typically shows a reminiscence bump (disproportionate recall of events from ages 10-30), recency effect, and childhood amnesia gradient. The paradigm engages a distributed network including hippocampus, medial prefrontal cortex, posterior cingulate, and lateral temporal cortex.

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-report-on-self">report on self</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-words">words</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-response-deadline">response deadline</a>
- **Material:** Cue words (such as garden, river, knife) of positive, negative or neutral valence, or structured interview questions.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. Participants retrieve specific personal memories in response to cue words, category prompts, or structured interview questions.
    2. Retrieved memories are scored for specificity, detail, emotional content, and temporal distribution.
* - **Manipulations**
  - - Cue type (word, sentence, photograph, odor)
    - Cue valence (positive, negative, neutral)
    - Retrieval instruction (specific episode vs. free retrieval)
    - Time period constraint (childhood, recent, specific decade)
    - Retrieval time limit
* - **Measurements**
  - - Specificity (proportion of specific vs. overgeneral memories)
    - Retrieval latency
    - Phenomenological detail ratings (vividness, emotional intensity, sensory detail)
    - Temporal distribution (reminiscence bump, recency)
    - Autobiographical Memory Interview scores (personal semantic + autobiographical incident)
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
* - Autobiographical Memory Test (Williams & Broadbent)

    `hedvar_autobiographical_memory__autobiographical_memory_test_williams_broadbent`
  - emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>
  - -
  - A named clinical instrument: positive and negative cue words, an instruction to describe an event from one particular day, and specific/general/non-memory scoring.
* - Autobiographical Memory Interview (Kopelman)

    `hedvar_autobiographical_memory__autobiographical_memory_interview_kopelman`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-text">text</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-examiner">examiner</a>
  - [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception)
  - A named clinical instrument: a structured spoken interview over three life periods, scored separately for personal facts and incidents.
* - Sentence-Cue Variant

    `hedvar_autobiographical_memory__sentence_cue_variant`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-text">text</a>
  - -
  - A sentence stem such as "A time when I felt proud was..." replaces the single cue word, steering retrieval toward a kind of event.
* - Odor-Cued Autobiographical Memory

    `hedvar_autobiographical_memory__odor_cued_autobiographical_memory`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-olfactory">olfactory</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-odor">odor</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-microphone">microphone</a>
  - [Olfactory perception](../processes/face_and_object_perception.md#hed-olfactory-perception)
  - The cue is a smell in a jar or on a strip rather than a word; the cue-then-retrieve structure is unchanged.
* - Future Episodic Simulation

    `hedvar_autobiographical_memory__future_episodic_simulation`
  - named form
  - -
  - Given the cue word, the participant imagines and describes a specific, plausible future event instead of recalling a past one.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Autobiographical memory](../processes/long_term_memory.md#hed-autobiographical-memory)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Recollection](../processes/long_term_memory.md#hed-recollection)
- [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing)

## Key references

- Williams, J. M. G., & Broadbent, K. (1986). Autobiographical memory in suicide attempters. *Journal of Abnormal Psychology*, 95(2), 144-149. ([DOI](https://doi.org/10.1037/0021-843x.95.2.144), [PubMed](https://pubmed.ncbi.nlm.nih.gov/3711438/))
- Kopelman, M. D., Wilson, B. A., & Baddeley, A. D. (1989). The autobiographical memory interview: A new assessment of autobiographical and personal semantic memory in amnesic patients. *Journal of Clinical and Experimental Neuropsychology*, 11(5), 724-744. ([DOI](https://doi.org/10.1080/01688638908400928), [PubMed](https://pubmed.ncbi.nlm.nih.gov/2808661/))
- Conway, M. A., & Pleydell-Pearce, C. W. (2000). The construction of autobiographical memories in the self-memory system. *Psychological Review*, 107(2), 261-288. ([DOI](https://doi.org/10.1037/0033-295x.107.2.261), [PubMed](https://pubmed.ncbi.nlm.nih.gov/10789197/))

## Further references

- Sumner, J. A., Griffith, J. W., & Mineka, S. (2010). Overgeneral autobiographical memory as a predictor of the course of depression: A meta-analysis. *Behaviour Research and Therapy*, 48(7), 614-625. ([DOI](https://doi.org/10.1016/j.brat.2010.03.013), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20399418/))
- Addis, D. R., Wong, A. T., & Schacter, D. L. (2007). Remembering the past and imagining the future: Common and distinct neural substrates during event construction and elaboration. *Neuropsychologia*, 45(7), 1363-1377. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2006.10.016), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17126370/))
- Hitchcock, C., Werner-Seidler, A., Blackwell, S. E., & Dalgleish, T. (2017). Autobiographical episodic memory-based training for the treatment of mood, anxiety and stress-related disorders: A systematic review and meta-analysis. *Clinical Psychology Review*, 52, 92-107. ([DOI](https://doi.org/10.1016/j.cpr.2016.12.003), [PubMed](https://pubmed.ncbi.nlm.nih.gov/28086133/))
- Rubin, D. C., & Schulkind, M. D. (1997). The distribution of autobiographical memories across the lifespan. *Memory & Cognition*, 25(6), 859-866. ([DOI](https://doi.org/10.3758/bf03211330), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9421572/))

## External links

- Cognitive Atlas: [autobiographical memory task](https://www.cognitiveatlas.org/task/id/trm_4f244d2a54e27)

- CogPO: [Episodic Recall Paradigm](http://www.wiki.cogpo.org/index.php?title=Episodic_Recall_Paradigm) (close match)

