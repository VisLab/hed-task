(hedtsk_cambridge_face_memory)=
# Cambridge Face Memory Task

**HED task ID:** `hedtsk_cambridge_face_memory`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md) (also [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md))

**Also known as:** Cambridge Face Memory Test, CFMT, Cambridge Face Test, Cambridge Face Memory

Learn target faces across viewpoints, then identify them among distractors under increasingly difficult conditions (novel viewpoints, visual noise); accuracy indexes face recognition ability and configural face processing.

## Description

The Cambridge Face Memory Test is the standard measure of face recognition ability for both clinical and individual-difference research. Participants study six target faces shown in three different viewpoints. Testing occurs in three phases of increasing difficulty: in Phase 1, targets are tested in studied viewpoints; in Phase 2, targets appear in novel viewpoints and lighting conditions; in Phase 3, Gaussian visual noise is added to the images. Each phase has 12 trials (one target face among five distractor faces), yielding a total score of 72. The CFMT specifically indexes holistic and configural face processing, is relatively culture-fair, and has become the benchmark for diagnosing prosopagnosia and studying "super-recognizers."

## At a glance

The standard form of the task, the one the inclusion test defines, in the terms of the
[task vocabulary](vocabulary.md). A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-study-then-test">study then test</a>
- **What form does the test take?** <a href="vocabulary.html#rule-study-then-test-test-form-forced-choice">forced choice</a>
- **Why does the player try?** <a href="vocabulary.html#motivation-drive-instructions-only">instructions only</a>
- **Stimulus modality:** <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>
- **Stimulus type:** <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>
- **Social aspect:** <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>
- **Task I/O device:** <a href="vocabulary.html#facet-task-io-device-keyboard">keyboard</a>, <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>
- **Trial structure:** <a href="vocabulary.html#facet-trial-structure-self-paced-trials">self paced trials</a>
- **Population:** <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-set-size">set size</a>
- **Material:** Six target faces in three viewpoints, tested among distractor faces in the studied views, in novel views and lighting, and with added visual noise.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants learn a set of target faces during study, then identify them among distractor faces in increasingly difficult test phases (same image, novel viewpoint, plus noise).
* - **Manipulations**
  - - Test phase difficulty (same view, novel view, contrast-degraded)
    - Number of target/distractor faces
    - Stimulus type (cars vs. faces)
    - Face orientation (inverted vs. upright)
* - **Measurements**
  - - Total correct identifications across phases
    - Accuracy per phase
    - Comparison to prosopagnosia norms
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
* - CFMT-Australian (CFMT+)

    `hedvar_cambridge_face_memory__cfmt_australian_cfmt`
  - named form
  - -
  - A named instrument with a different face set and a fourth, harder stage added.
* - CFMT-Cars

    `hedvar_cambridge_face_memory__cfmt_cars`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>; social aspect: none
  - [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition)
  - Images of cars replace faces in the same learn-then-choose procedure, as a non-face control; the procedure is otherwise unchanged.
* - Short-Form CFMT

    `hedvar_cambridge_face_memory__short_form_cfmt`
  - named form
  - -
  - A named short form with fewer trials and the same learn-then-choose procedure.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Face identity recognition](../processes/face_and_object_perception.md#hed-face-identity-recognition)
- [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)

## Key references

- Duchaine, B., & Nakayama, K. (2006). The Cambridge Face Memory Test: Results for neurologically intact individuals and an investigation of its validity using inverted face stimuli and prosopagnosic participants. *Neuropsychologia*, 44(4), 576-585. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2005.07.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16169565/))
- Kanwisher, N., McDermott, J., & Chun, M. M. (1997). The fusiform face area: A module in human extrastriate cortex specialized for face perception. *Journal of Neuroscience*, 17(11), 4302-4311. ([DOI](https://doi.org/10.1523/jneurosci.17-11-04302.1997), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9151747/))
- McKone, E., Kanwisher, N., & Duchaine, B. C. (2007). Can generic expertise explain special processing for faces? *Trends in Cognitive Sciences*, 11(1), 8-15. ([DOI](https://doi.org/10.1016/j.tics.2006.11.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17129746/))

## Further references

- Bobak, A. K., Pampoulov, P., & Bate, S. (2016). Detecting superior face recognition skills in a large sample of young British adults. *Quarterly Journal of Experimental Psychology*, 69(2), 253-263. ([DOI](https://doi.org/10.3389/fpsyg.2016.01378), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27713706/))
- Bowles, D. C., McKone, E., Dawel, A., Duchaine, B., Palermo, R., Schmalzl, L., ... & Yovel, G. (2009). Diagnosing prosopagnosia: Effects of ageing, sex, and participant-stimulus ethnic match on the Cambridge Face Memory Test and Cambridge Face Perception Test. *Cognitive Neuropsychology*, 26(5), 423-455. ([DOI](https://doi.org/10.1080/02643290903343149), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19921582/))
- Russell, R., Duchaine, B., & Nakayama, K. (2009). Super-recognizers: People with extraordinary face recognition ability. *Psychonomic Bulletin & Review*, 16(2), 252-257. ([DOI](https://doi.org/10.3758/pbr.16.2.252), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19293090/))
- Wilmer, J. B., Germine, L., Chabris, C. F., Chatterjee, G., Williams, M., Loken, E., ... & Duchaine, B. (2010). Human face recognition ability is specific and highly heritable. *Proceedings of the National Academy of Sciences*, 107(11), 5238-5241. ([DOI](https://doi.org/10.1073/pnas.0913053107), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20176944/))

## External links

- Cognitive Atlas: [Cambridge Face Memory Test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949912)

