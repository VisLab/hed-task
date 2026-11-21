(hedtsk_oddball)=
# Oddball Task

**HED task ID:** `hedtsk_oddball`

**Family:** [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md)

**Also known as:** P300 Task, Auditory Oddball, Visual Oddball

Sequence of standards with rare deviants or targets; deviants elicit a large positive ERP around 300 ms (P3a/P3b), indexing attention and context updating.

## Description

Participants are presented with a stimulus stream containing frequent standard stimuli (80% of trials) and infrequent target (oddball) stimuli (20%) that differ in some dimension (pitch, color, shape). Participants respond (button press) to targets. Target detection elicits the P3b ERP component (300-600 ms, parietal maximum), reflecting stimulus evaluation and working memory updating. Novel or unexpected stimuli also elicit the P3a component (frontocentral), reflecting automatic attention capture. The paradigm is widely used as a biomarker of cognitive function and has clinical applications in ADHD, schizophrenia, and traumatic brain injury.

## Game model

The standard form of the task, the one the inclusion test defines, as a game, in the terms
of the [game vocabulary](vocabulary.md). [The task model](../task_model.md) explains the
parts. A variant states only what it changes.

- **Game type:** <a href="vocabulary.html#game-respond-to-rule">Respond under a rule</a> (`respond_to_rule`)
- **Game rules:** the answers that differ from the defaults of the game type
  - *What does the rule ask about each stimulus?* <a href="vocabulary.html#rule-respond-to-rule-rule-asks-detect">detect</a>
  - *Must the player ever hold back?* <a href="vocabulary.html#rule-respond-to-rule-response-demand-withhold-on-some">withhold on some</a>
  - *How often is there a target?* <a href="vocabulary.html#rule-respond-to-rule-target-rate-rare-target">rare target</a>
- **Game motivators:**
  - *Why does the player try?* <a href="vocabulary.html#motivator-drive-instructions-only">instructions only</a>
- **Game phases:** none beyond the game's own structure
- **Game facets:**
  - Stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>
  - Stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>
  - Task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>
  - Trial structure: <a href="vocabulary.html#facet-trial-structure-fixed-time-trials">fixed time trials</a>
  - Population: <a href="vocabulary.html#facet-population-young-adults">young adults</a>
- **Settings:** <a href="vocabulary.html#setting-interstimulus-interval">interstimulus interval</a>, <a href="vocabulary.html#setting-target-probability">target probability</a>
- **Material:** A stream of frequent standard tones and rare target tones that differ in pitch, sometimes with novel non-target sounds.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - 1. A sequence of frequent standard stimuli is occasionally interrupted by rare target (and sometimes novel) stimuli.
    2. Participants count or respond to targets.
* - **Manipulations**
  - - Target probability (typically 10-20%)
    - Stimulus modality (auditory, visual)
    - Inclusion of novel non-target deviants
    - ISI
    - Response requirement (none vs. count or respond)
    - Standard tone (roving vs. fixed)
* - **Measurements**
  - - P3b amplitude and latency to targets
    - P3a to novels
    - Target detection accuracy and RT
    - N2 component
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
* - Three-Stimulus Novelty Oddball

    `hedvar_oddball__three_stimulus_novelty_oddball`
  - stimulus type: <a href="vocabulary.html#facet-stimulus-type-tones">tones</a>, <a href="vocabulary.html#facet-stimulus-type-nonvocal-sounds">nonvocal sounds</a>
  - -
  - Rare, varied novel sounds are added as a third event type that the participant ignores while still responding to the rare target.
* - Visual Oddball

    `hedvar_oddball__visual_oddball`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-shapes">shapes</a>, <a href="vocabulary.html#facet-stimulus-type-letters">letters</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>
  - [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - The common and rare events are shapes or letters on a screen instead of tones.
* - Passive Oddball

    `hedvar_oddball__passive_oddball`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>
  - -
  - No response or count is required and the participant may do something else while the sounds play, so there is no job at all.
* - Active Counting vs. Button-Press Response

    `hedvar_oddball__active_counting_vs_button_press_response`
  - task I/O device: <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>; rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-count">count</a>
  - -
  - The participant keeps a silent count of the rare events and reports the total at the end instead of pressing to each one; the standard procedure already allows either.
* - Duration Deviance Oddball

    `hedvar_oddball__duration_deviance_oddball`
  - named form
  - -
  - The rare tone differs from the common one in duration rather than pitch.
* - Cross-Modal Oddball

    `hedvar_oddball__cross_modal_oddball`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-auditory">auditory</a>, <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-headphones">headphones</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>
  - [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - Common and rare events come in different senses, or the stream mixes senses and the participant responds to rare events in either.
* - Emotional Oddball

    `hedvar_oddball__emotional_oddball`
  - stimulus modality: <a href="vocabulary.html#facet-stimulus-modality-visual">visual</a>; stimulus type: <a href="vocabulary.html#facet-stimulus-type-pictures">pictures</a>, <a href="vocabulary.html#facet-stimulus-type-faces">faces</a>; emotional aspect: <a href="vocabulary.html#facet-emotional-aspect-emotional-stimuli">emotional stimuli</a>; social aspect: <a href="vocabulary.html#facet-social-aspect-social-stimuli">social stimuli</a>; task I/O device: <a href="vocabulary.html#facet-task-io-device-computer-screen">computer screen</a>, <a href="vocabulary.html#facet-task-io-device-button-box">button box</a>
  - [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception)
  - The rare events are emotional pictures or faces in a stream of neutral ones, shown on a screen.
* - Roving Paradigm

    `hedvar_oddball__roving_paradigm`
  - rule asks: <a href="vocabulary.html#rule-respond-to-rule-rule-asks-compare">compare</a>; reference: <a href="vocabulary.html#rule-respond-to-rule-reference-held-in-mind">held in mind</a>
  - -
  - A tone repeats and is then replaced by a new tone that becomes the new standard, so any response is to a change from the preceding tone rather than to a fixed rare stimulus; the description does not say whether a response is required.
```

## Cognitive processes

This task is designed to engage the following processes:

- [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention)
- [Temporal attention](../processes/selective_and_sustained_attention.md#hed-temporal-attention)
- [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture)
- [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention)
- [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating)

## Key references

- Sutton, S., Braren, M., Zubin, J., & John, E. R. (1965). Evoked-potential correlates of stimulus uncertainty. *Science*, 150(3700), 1187-1188. ([DOI](https://doi.org/10.1126/science.150.3700.1187), [PubMed](https://pubmed.ncbi.nlm.nih.gov/5852977/))
- Donchin, E., & Coles, M. G. H. (1988). Is the P300 component a manifestation of context updating? *Behavioral and Brain Sciences*, 11(3), 357-374. ([DOI](https://doi.org/10.1017/s0140525x00058027))
- Polich, J. (2007). Updating P300: An integrative theory of P3a and P3b. *Clinical Neurophysiology*, 118(10), 2128-2148. ([DOI](https://doi.org/10.1016/j.clinph.2007.04.019), [PubMed](https://pubmed.ncbi.nlm.nih.gov/17573239/))

## Further references

- Linden, D. E. J. (2005). The P300: Where in the brain is it produced and what does it tell us? *Neuroscientist*, 11(6), 563-576. [Updated: Bledowski, C., et al. (2004). Localizing P300 generators in visual target and distractor processing: A combined event-related potential and functional magnetic resonance imaging study. *Journal of Neuroscience*, 24(42), 9353-9360.] ([DOI](https://doi.org/10.1177/1073858405280524), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16282597/))
- Twomey, D. M., Murphy, P. R., Kelly, S. P., & O'Connell, R. G. (2015). The classic P300 encodes a build-to-threshold decision variable. *European Journal of Neuroscience*, 42(1), 1636-1643. ([DOI](https://doi.org/10.1111/ejn.12936), [PubMed](https://pubmed.ncbi.nlm.nih.gov/25925534/))
- Kelly, S. P., & O'Connell, R. G. (2013). Internal and external influences on the rate of sensory evidence accumulation in the human brain. *Journal of Neuroscience*, 33(50), 19434-19441. ([DOI](https://doi.org/10.1523/jneurosci.3355-13.2013), [PubMed](https://pubmed.ncbi.nlm.nih.gov/24336710/))

## External links

- Cognitive Atlas: [oddball task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb949bf6)

- CogPO: [Oddball Discrimination Paradigm](http://www.wiki.cogpo.org/index.php?title=Oddball_Discrimination_Paradigm)

