(hedtsk_autobiographical_memory)=
# Autobiographical Memory Task

**HED task ID:** `hedtsk_autobiographical_memory`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md)

**Also known as:** Autobiographical Memory Interview, AMI, Cue-Word Autobiographical Memory Task, Galton-Crovitz Task, Autobiographical Memory Test

Participants retrieve specific personal memories in response to cue words or structured prompts; specificity, detail, and temporal distribution of retrieved episodes index autobiographical memory function.

## Description

Autobiographical memory tasks assess the ability to retrieve specific personal episodes from one's past. The Galton-Crovitz cue-word task presents generic words (e.g., 'garden,' 'river,' 'knife') and asks participants to retrieve a specific personal memory associated with each and date it. The Autobiographical Memory Interview (Kopelman, Wilson, & Baddeley, 1989) uses a structured interview format probing both personal semantic knowledge (names, addresses) and autobiographical incidents across life periods (childhood, early adulthood, recent). The Autobiographical Memory Test (Williams & Broadbent, 1986) presents positive and negative cue words and measures whether participants retrieve specific episodes (bounded in time and place) vs. overgeneral memories (categories or extended periods). Overgeneral autobiographical memory — the tendency to retrieve categorical summaries rather than specific episodes — is a robust marker of depression, PTSD, and suicidality. The temporal distribution of memories typically shows a reminiscence bump (disproportionate recall of events from ages 10-30), recency effect, and childhood amnesia gradient. The paradigm engages a distributed network including hippocampus, medial prefrontal cortex, posterior cingulate, and lateral temporal cortex.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants retrieve specific personal memories in response to cue words, category prompts, or structured interview questions; retrieved memories are scored for specificity, detail, emotional content, and temporal distribution.
* - **Manipulation**
  - Cue type (word, sentence, photograph, odor); cue valence (positive, negative, neutral); retrieval instruction (specific episode vs. free retrieval); time period constraint (childhood, recent, specific decade); retrieval time limit.
* - **Measurement**
  - Specificity (proportion of specific vs. overgeneral memories); retrieval latency; phenomenological detail ratings (vividness, emotional intensity, sensory detail); temporal distribution (reminiscence bump, recency); Autobiographical Memory Interview scores (personal semantic + autobiographical incident).
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
* - Cue-Word Task (Galton-Crovitz)

    `hedvar_autobiographical_memory__cue_word_task_galton_crovitz`
  - Single words as retrieval cues; participants generate a specific memory and date it. Simple, flexible, widely used. Measures specificity and retrieval latency.
  - Single word cues; participant freely generates memories in response
* - Autobiographical Memory Test (Williams & Broadbent)

    `hedvar_autobiographical_memory__autobiographical_memory_test_williams_broadbent`
  - Positive and negative cue words with instructions to retrieve specific episodes. Coded for specificity (specific, categoric, extended, semantic associate). The standard clinical measure of overgeneral memory.
  - Cued recall with specificity scoring and suicidal ideation variant; named standardized instrument
* - Autobiographical Memory Interview (Kopelman)

    `hedvar_autobiographical_memory__autobiographical_memory_interview_kopelman`
  - Structured interview across life periods (childhood, early adult, recent). Separate scores for personal semantic and autobiographical incidents. Used in amnesia and dementia assessment.
  - Structured interview with childhood, early adult, and recent life sections; different retrieval protocol
* - Sentence-Cue Variant

    `hedvar_autobiographical_memory__sentence_cue_variant`
  - Sentence stems as cues (e.g., 'A time when I felt proud was...'). More constrained than single words; can target specific emotional themes.
  - Sentence-length cues instead of single words; richer cueing structure
* - Odor-Cued Autobiographical Memory

    `hedvar_autobiographical_memory__odor_cued_autobiographical_memory`
  - Odors as retrieval cues (Proust phenomenon). Odor-cued memories tend to be older, more emotional, and more vivid than word-cued memories.
  - Olfactory cues evoke memories; different sensory modality and involuntary retrieval characteristics
* - Future Episodic Simulation

    `hedvar_autobiographical_memory__future_episodic_simulation`
  - Imagine specific future events in response to cues (Schacter & Addis, 2007). Tests the constructive episodic simulation hypothesis — that autobiographical memory supports future thinking.
  - Participant imagines future events instead of recalling past; different cognitive operation (projection vs. retrieval)
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

