(hedtsk_cambridge_face_memory)=
# Cambridge Face Memory Task

**HED task ID:** `hedtsk_cambridge_face_memory`

**Family:** [Recall and recognition memory tests](families/recall_and_recognition.md) (also [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md))

**Also known as:** Cambridge Face Memory Test, CFMT, Cambridge Face Test, Cambridge Face Memory

Learn target faces across viewpoints, then identify them among distractors under increasingly difficult conditions (novel viewpoints, visual noise); accuracy indexes face recognition ability and configural face processing.

## Description

The Cambridge Face Memory Test is the standard measure of face recognition ability for both clinical and individual-difference research. Participants study six target faces shown in three different viewpoints. Testing occurs in three phases of increasing difficulty: in Phase 1, targets are tested in studied viewpoints; in Phase 2, targets appear in novel viewpoints and lighting conditions; in Phase 3, Gaussian visual noise is added to the images. Each phase has 12 trials (one target face among five distractor faces), yielding a total score of 72. The CFMT specifically indexes holistic and configural face processing, is relatively culture-fair, and has become the benchmark for diagnosing prosopagnosia and studying "super-recognizers."

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
* - **Measurements**
  - - Total correct identifications across phases
    - Accuracy per phase
    - Comparison to prosopagnosia norms
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
* - CFMT-Original

    `hedvar_cambridge_face_memory__cfmt_original`
  - The participant learns six unfamiliar male faces, then picks each from sets of three in three stages: the same images, new images with different views and lighting, and new images degraded with visual noise. Seventy-two trials in all.
  - Canonical 72-item CFMT with novel face learning phases
* - CFMT-Australian (CFMT+)

    `hedvar_cambridge_face_memory__cfmt_australian_cfmt`
  - The same procedure with a different set of faces and an added fourth stage of harder, noisier trials, which prevents the best performers from hitting the maximum score.
  - Australian race face set; assesses own-race advantage with matched procedure
* - CFMT-Cars

    `hedvar_cambridge_face_memory__cfmt_cars`
  - The same learn-and-recognize procedure using images of cars instead of faces. Comparing it with the face version shows whether a person's difficulty is specific to faces or extends to visual memory in general.
  - Cars instead of faces; object recognition control condition with same task structure
* - CFMT-Inverted

    `hedvar_cambridge_face_memory__cfmt_inverted`
  - All face images are shown upside down throughout learning and testing. Upside-down faces are much harder to recognize, and the size of the drop measures how much the participant relies on seeing the face as a whole.
  - Inverted face stimuli; disrupts configural processing; distinct task demand
* - Cambridge Face Perception Test (CFPT)

    `hedvar_cambridge_face_memory__cambridge_face_perception_test_cfpt`
  - A companion task with no memory component. The participant sees a target face and six faces that have been morphed to resemble it to different degrees, and sorts the six by similarity to the target.
  - Morph-ordering perception task instead of recognition; different participant operation
* - Short-Form CFMT

    `hedvar_cambridge_face_memory__short_form_cfmt`
  - A shortened version with fewer trials for quick screening of face recognition ability, following the same learn-then-choose procedure.
  - Abbreviated item set for screening; recognized published short-form instrument
```

## Cognitive processes

This task is designed to engage the following processes:

- [Face identity recognition](../processes/face_and_object_perception.md#hed-face-identity-recognition)
- [Face perception](../processes/face_and_object_perception.md#hed-face-perception)
- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)

## Key references

- Duchaine, B., & Nakayama, K. (2006). The Cambridge Face Memory Test: Results for neurologically intact individuals and an investigation of its validity using inverted face stimuli and prosopagnosic participants. *Neuropsychologia*, 44(4), 576–585. ([DOI](https://doi.org/10.1016/j.neuropsychologia.2005.07.001), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16169565/))
- Kanwisher, N., McDermott, J., & Chun, M. M. (1997). The fusiform face area: A module in human extrastriate cortex specialized for face perception. *Journal of Neuroscience*, 17(11), 4302–4311. ([DOI](https://doi.org/10.1523/jneurosci.17-11-04302.1997), [PubMed](https://pubmed.ncbi.nlm.nih.gov/9151747/))
- McKone, E., Kanwisher, N., & Duchaine, B. C. (2007). Can generic expertise explain special processing for faces? *Trends in Cognitive Sciences*, 11(1), 8–15. ([DOI](https://doi.org/10.1016/j.tics.2006.11.002), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17129746/))

## Further references

- Bobak, A. K., Pampoulov, P., & Bate, S. (2016). Detecting superior face recognition skills in a large sample of young British adults. *Quarterly Journal of Experimental Psychology*, 69(2), 253–263. ([DOI](https://doi.org/10.3389/fpsyg.2016.01378), [PubMed](https://pubmed.ncbi.nlm.nih.gov/27713706/))
- Bowles, D. C., McKone, E., Dawel, A., Duchaine, B., Palermo, R., Schmalzl, L., ... & Yovel, G. (2009). Diagnosing prosopagnosia: Effects of ageing, sex, and participant-stimulus ethnic match on the Cambridge Face Memory Test and Cambridge Face Perception Test. *Cognitive Neuropsychology*, 26(5), 423–455. ([DOI](https://doi.org/10.1080/02643290903343149), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19921582/))
- Russell, R., Duchaine, B., & Nakayama, K. (2009). Super-recognizers: People with extraordinary face recognition ability. *Psychonomic Bulletin & Review*, 16(2), 252–257. ([DOI](https://doi.org/10.3758/pbr.16.2.252), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19293090/))
- Wilmer, J. B., Germine, L., Chabris, C. F., Chatterjee, G., Williams, M., Loken, E., ... & Duchaine, B. (2010). Human face recognition ability is specific and highly heritable. *Proceedings of the National Academy of Sciences*, 107(11), 5238–5241. ([DOI](https://doi.org/10.1073/pnas.0913053107), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20176944/))

## External links

- Cognitive Atlas: [Cambridge Face Memory Test](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949912)

