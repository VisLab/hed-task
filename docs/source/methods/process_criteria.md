# Process selection and definition criteria

**Purpose:** Reference document specifying how the 172-process HED cognitive process catalog was scoped, how processes were selected, and the rules for definitions, naming, categorization, references, and task linkage. Companion to the [task selection criteria](task_criteria.md). Per-category scope, out-of-scope and open-issue notes appear on each category page. The prior reference and categories documents have been archived.

---

## 1. Process selection criteria

### What counts as a process in this catalog?

A **cognitive process** is a mental operation hypothesized to occur in a participant during a trial — something with an identifiable onset, an eliciting condition, and an in-principle measurable signature. Concretely, a candidate is a cognitive process if we can plausibly answer three questions:

1. **When does it happen?** — at what point in a trial, relative to stimulus and response, would we expect this process to be engaged?
2. **How is it elicited?** — what stimulus structure, instruction, or contingency would drive it?
3. **How is it measured?** — what behavioral, physiological, or neural signature would index it (even if imperfectly)?

This is a **forward-looking plausibility test**, not a gating filter. We keep candidates where we expect the answers exist in the literature, even if we have not yet found them. The test exists to rule out things that are categorically the wrong kind of object — not to demand finished evidence.

A process row should sit at the level where the inclusion-test triple has a single answer. If the question "when does it happen" has multiple, non-reducible answers (e.g., "working memory" can mean encoding, maintenance, manipulation, or updating, each at different trial phases), the candidate is too coarse and should be either split into sub-processes or treated as a category label only.

### What is excluded?

The following do **not** count as cognitive processes in this catalog:

- **States and traits:** Fear, arousal, anxiety, empathy-as-a-trait, boredom, mood. HED handles these as stimulus/state labels.
- **Specific emotions as states:** Happiness, disgust, anger, sadness. These are what participants experience, not operations they perform. Emotion *recognition* and emotion *regulation* are processes; the emotions themselves are not.
- **Stimulus categories:** Faces, words, tones, music. These are inputs to processes, not processes themselves.
- **Individual-difference constructs:** Fluid intelligence, working-memory capacity as a score, impulsivity as a trait, handedness, dexterity. These describe between-person variation, not within-trial operations.
- **Dimensions and task parameters:** Valence, arousal as a dimension, working-memory load, stimulus-onset asynchrony. These are properties of stimuli or experimental designs.
- **Umbrella terms:** Attention, Memory, Language, Perception, Reasoning, Motivation, Social cognition, Consciousness, Emotion, Cognitive control, Motor control, Decision making. The category label carries the umbrella role; no process row should repeat it. Each umbrella that was in the original list has been either dropped entirely or split into concrete sub-processes that individually pass the inclusion test.
- **Analysis methods and modeling frameworks:** Drift-diffusion modeling, Bayesian inference, representational similarity analysis. These are ways of measuring or modeling processes, not processes themselves.
- **Paradigm names used as process labels:** A paradigm name (e.g., "Stroop effect") is not a process. The underlying operations (interference control, response conflict) are.

### Process vs. phenomenon

When the literature uses the same noun for both a phenomenon and the process producing it (extinction, directed forgetting, retroactive interference, masking), we treat it as a process and fold the phenomenon into the same row. We do not create separate rows for the process and the phenomenon it produces unless the distinction earns its keep.

### Modality-abstract vs. modality-specific

Processes at the process level are modality-abstract when the same mechanism operates across modalities. Masking is a single process row (modality-abstract); the Auditory Masking Task and Visual Masking Task carry the modality distinction on the task side. The same pattern applies to priming and similar constructs: one process row, multiple task rows.

---

## 2. Naming conventions

### Process IDs

Every process has an identifier of the form `hed_<slug>`, where `<slug>` is a snake_case string. Examples: `hed_response_inhibition`, `hed_visual_working_memory`, `hed_working_memory_updating`.

The `hed_` prefix is this catalog's working identifier — it is a naming choice, not a claim about HED-schema membership. How (or whether) these IDs relate to the HED schema in the future is a separate, downstream decision.

**Stability policy:** During the current audit phase, IDs are explicitly provisional. They may change when a definition is refined, a near-duplicate is merged, or a better slug is chosen. Every rename must cascade atomically through `process_details.json`, `task_details.json`, and every derived file (`task_names.json`, `process_task_index.json`, `process_task_crossref.md`). Post-stability (after a declared freeze milestone), IDs are frozen: renames become aliases, and ID reassignment is a breaking change.

### Process names

Process names use **sentence case**: the first word is capitalized, the remainder is lowercase except for proper nouns. Examples: "Associative learning", "Working memory updating", "Pavlovian conditioning".

Process names do not end in "process" or "mechanism" unless those words are part of the established term (none currently do).

### Aliases

When multiple names exist for the same process, one is designated **canonical** (`process_name`) and the others are recorded in an `aliases` array. Each alias carries a `name` and an optional `note` explaining the terminological distinction or the reason for the merge. An alias is not a separate process — it fails the test of having a distinct When/Elicited/Measured triple.

The `aliases` field parallels the task-side `aliases` array: it captures alternative names that a researcher might search for, preserving the terminological or theoretical distinction without creating a separate process row. Aliases do not affect process counts, task linkage, or category membership.

Schema:

```json
{
  "aliases": [
    {
      "name": "Operant conditioning",
      "note": "Skinnerian terminology; emphasizes the operant response and reinforcement schedules."
    }
  ]
}
```

Current resolved aliases:

| Canonical | Alias(es) | Rationale |
|-----------|-----------|-----------|
| Instrumental conditioning | Operant conditioning | Skinnerian terminology; emphasizes reinforcement schedules. Merged. |
| Perspective taking | Mentalizing, Theory of mind | Mentalizing is the process verb (neuroimaging); Theory of mind is the capacity noun (developmental). |
| Word recognition | Visual word recognition | "Visual" is the default modality; auditory word recognition has its own name. |
| Risk processing | Risky decision making | Risk processing names the cognitive operation; risky decision making names the task class. |
| Emotion recognition | Emotion perception | Recognition is operationalized (identification of a named category); perception is broader. |
| Working memory updating | Updating, Updating (WM) | Merged; plain "Updating" was memory-context-underspecified. |
| Active maintenance | Maintenance | Generic term for holding information over a delay; merged into active maintenance. |
| Set shifting | Cognitive flexibility | Cognitive flexibility is a capacity-level construct that fails the single-answer inclusion test; set shifting is its primary experimental operationalization. Dropped as separate process. |
| Deductive reasoning | Logical reasoning | Logical reasoning is an umbrella over deductive + inductive; dropped as separate process. |
| Gustatory perception | Gustation | Renamed for consistency with other modality-perception rows. |
| Somatosensory perception | Somatosensation | Renamed for consistency with other modality-perception rows. |
| Sustained attention | Vigilance | Synonymous when operationalized as a continuous-performance measure. |

---

## 3. Definition standards

### Requirements

Every process must have a **definition** field that is:

1. **Non-empty.** A blank definition is a data quality failure.
2. **One sentence minimum.** The definition should be a self-contained statement of what the process is, understandable to a researcher in a neighboring subfield.
3. **Operationally grounded.** The definition should connect to how the process is elicited or measured, not just what it "is" in the abstract.

### What makes a good definition

A good process definition states what the process does (or what the participant does), in terms that connect to observable paradigms. Compare:

- **Weak:** "The process of inhibiting responses." (Circular.)
- **Better:** "Suppression of a prepotent or already-initiated response when it becomes inappropriate, indexed behaviorally by stop-signal reaction time or commission errors."

Definitions that begin with "See 5.6" or cross-reference a section number from an earlier document are stale artifacts and should be rewritten.

### Cross-references in definitions

If a process definition says "See instrumental conditioning" or similar, this indicates a synonym relationship. The definition should still state what the process is, even if briefly, rather than being a bare pointer.

---

## 4. Category rules

### The 19 categories

The catalog organizes 172 processes into 19 categories. The categories, their process counts, and their scope are defined in the `categories` array of `process_details.json`. The 19 categories are:

1. Associative Learning and Reinforcement (13)
2. Auditory and Pre-Attentive Deviance Processing (4)
3. Awareness, Agency, and Metacognition (13)
4. Cognitive Flexibility and Higher-Order Executive Function (3)
5. Emotion Perception and Regulation (5)
6. Face and Object Perception (12)
7. Implicit and Statistical Learning (2)
8. Inhibitory Control and Conflict Monitoring (9)
9. Language Comprehension and Production (16)
10. Long-Term Memory (21)
11. Motor Preparation, Timing, and Execution (16)
12. Perceptual Decision-Making (Evidence Accumulation) (1)
13. Reasoning and Problem-Solving (11)
14. Reward Anticipation and Motivation (6)
15. Selective and Sustained Attention (11)
16. Short-Term and Working Memory (9)
17. Social Cognition and Strategic Social Choice (11)
18. Spatial Cognition and Navigation (2)
19. Value-Based Decision-Making Under Risk and Uncertainty (7)

### Purpose of categories

Categories serve as **organizational labels** for human browsing. They are not ontological commitments. A process belongs to the category whose scope best describes its primary research tradition. Categories do not imply inheritance or class membership.

### Category structure

Each category entry in `process_details.json` has:

- **`scope`:** What belongs here — a brief description of the process family.
- **`out_of_scope`** (optional): What tends to get put here but shouldn't.
- **`issues`** (optional): Open questions about boundaries, near-synonyms, or structural problems.


### Dual-category processes

Every process is assigned to exactly one category. When a process could fit two categories, the rule is:

- **File by primary research tradition.** Antisaccade is in Motor Preparation, Timing, and Execution because it is an oculomotor output measure, even though it centrally depends on prepotent-saccade inhibition (which would argue for Inhibitory Control).
- **File second-order processes by their second-order character.** Metacognitive monitoring, self-monitoring, feeling of knowing, and judgment of learning are in Awareness, Agency, and Metacognition (not in their "first-order" home categories) because the reportable content is what the participant consciously experiences about their own cognition.
- **Perceptual processes go by modality when modality-specific, by mechanism when modality-abstract.** Proprioception stays in Motor despite being perceptual, because it is tightly functionally coupled to motor control in the experimental literature.

### Category process counts

Each category entry in `process_details.json` carries a `process_count` field. This must match the actual number of processes assigned to that `category_id` in the `processes` array. Drift between the count and the actual membership is a data quality issue.

---

## 5. Reference standards

### Reference types

Each process carries two reference arrays:

- **`fundamental_references`:** Paradigm-defining or foundational references. These are the papers or books that established the process as a research construct. Typically pre-2000, often classic citations.
- **`recent_references`:** Recent or standard-review references. These are post-2010 papers (preferred) that provide modern entry points into the literature: reviews, meta-analyses, or influential empirical papers.

### Current state

all 407 reference entries in `process_details.json` have **empty `title` fields**. This is a known future-phase item. The `citation_string` field carries the human-readable citation (e.g., "Rescorla & Wagner (1972) in *Classical Conditioning II*"), and `journal` and `year` fields are populated. Title fill is deferred to a separate literature-lookup pass.

### Quality expectations

- Every process should have at least one fundamental reference and at least one recent reference.
- Citation strings should be clean — no embedded markdown headers, no stitched-together text fragments.
- References for the 6 Awareness/Agency/Metacognition rows added and the 5 problem-solving/valuation additions were written fresh; all inherited references come from the original Cognitive Atlas source documents.
- The Levy & Glimcher (2012) citation was corrected: journal is *Current Opinion in Neurobiology* 22:1027–1038, not *Journal of Neuroscience*.

### Reference provenance (proposed, not yet implemented)

A future enhancement would mark each reference with its source (`atlas`, `supplement`, `gap_analysis`, `claude_generated`, `user_provided`). Currently all references are indistinguishable in origin. Provenance is not a quality signal — `atlas` means "inherited from the Cognitive Atlas starting corpus" (uncurated), not "validated."

---

## 6. Task linkage rules

### How processes link to tasks

A process links to a task if the task's inclusion test (Procedure / Manipulation / Measurement) engages that process. The link is stored in the `tasks[]` array of each process entry in `process_details.json`, using `hedtsk_<slug>` IDs. The reverse direction (task → process) is stored in the `hed_process_ids` array of each task entry in `task_details.json`.

### When is a link justified?

A link from task T to process P should satisfy at least one of:

- **Canonical link:** The paradigm-defining paper(s) for T theorize that T engages P. Example: Stroop → interference control.
- **Contrast-based link:** Some condition contrast in T is standardly interpreted as isolating P. Example: congruent vs. incongruent in Stroop → conflict monitoring.
- **Measurement-based link:** T has a measure standardly interpreted as an index of P. Example: stop-signal reaction time in the Stop-Signal Task → response inhibition.

### What a link is not

- A link is not an ontology assertion (no `is-a`, no class hierarchy).
- A link is not an exclusion — other processes may be engaged; we list only those the task is designed to probe.
- A link is not symmetric in the sense that every process that lists T also makes T its primary paradigm. Some processes are engaged by a task but primarily studied with a different task.

### Unlinked processes

19 of 172 processes have `task_count = 0` (no linked tasks). Some of these are legitimate: the process is real but none of the 103 tasks in the current catalog are designed to study it (e.g., gustatory perception — no taste-perception task in the catalog). Others may signal problems: the process is too abstract, or a link was missed.
