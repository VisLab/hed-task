# Process crossref

Every correspondence between the 172 cognitive processes in this catalog and
the 918 concepts in the Cognitive Atlas, in both directions. The
[methodology](../methodology/atlas_mapping.md) page explains what the match types mean
and how each row was decided.

The source of record is `.working/mappings/`, not this page.

## Catalog to Atlas

One row per process in this catalog: 102 exact, 14 close, 23 related, 33 none. `Atlas tasks` counts the
Atlas task entries that assert the matched concept, which is a rough measure of how
much use the Atlas makes of it.

| Process | Match | Atlas concept | Concept ID | Atlas class | Atlas tasks | Notes |
|---|---|---|---|---|---|---|
| [Acoustic processing](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-acoustic-processing) | `close` | acoustic processing | `trm_4a3fd79d0971e` | Perception | 3 | Atlas definition describes underwater and atmospheric signal propagation, not auditory cognition |
| [Action initiation](../processes/motor_preparation_timing_and_execution.md#hed-action-initiation) | `exact` | action initiation | `trm_4a3fd79d0b5c0` | Action | - | - |
| [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance) | `exact` | active maintenance | `trm_4a3fd79d0ba0d` | Executive/Cognitive Control | 15 | - |
| [Affective priming](../processes/emotion_perception_and_regulation.md#hed-affective-priming) | `related` | priming | `trm_4e89aebaa311d` | Learning and Memory | - | Atlas has no affective or evaluative priming entry |
| [Alerting](../processes/selective_and_sustained_attention.md#hed-alerting) | `none` | - | - | (none) | - | Atlas has no alerting entry despite carrying the ANT |
| [Analogical reasoning](../processes/reasoning_and_problem_solving.md#hed-analogical-reasoning) | `exact` | analogical reasoning | `trm_4a3fd79d09810` | Reasoning and Decision Making | 1 | - |
| [Antisaccade](../processes/motor_preparation_timing_and_execution.md#hed-antisaccade) | `none` | - | - | (none) | - | No antisaccade concept; the Atlas registers it only as a task |
| [Approach motivation](../processes/reward_anticipation_and_motivation.md#hed-approach-motivation) | `none` | - | - | (none) | - | Only the BIS/BAS trait scale, not the process |
| [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning) | `exact` | association learning | `trm_4a3fd79d098c9` | Learning and Memory | 7 | - |
| [Attention shifting](../processes/selective_and_sustained_attention.md#hed-attention-shifting) | `exact` | attention shifting | `trm_4a3fd79d0b5fb` | Attention | 12 | - |
| [Attentional awareness](../processes/awareness_agency_and_metacognition.md#hed-attentional-awareness) | `related` | consciousness | `trm_4a3fd79d09e35` | (none) | - | Atlas has only the broader parent term |
| [Attentional capture](../processes/selective_and_sustained_attention.md#hed-attentional-capture) | `none` | - | - | (none) | - | No attentional capture entry |
| [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception) | `exact` | auditory perception | `trm_4a3fd79d09ab2` | Perception | 21 | - |
| [Auditory tone discrimination](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-tone-discrimination) | `exact` | auditory tone discrimination | `trm_557b476527a27` | Perception | 3 | - |
| [Autobiographical memory](../processes/long_term_memory.md#hed-autobiographical-memory) | `exact` | autobiographical memory | `trm_4a3fd79d09b10` | Learning and Memory | 2 | - |
| [Avoidance motivation](../processes/reward_anticipation_and_motivation.md#hed-avoidance-motivation) | `none` | - | - | (none) | - | Only the BIS/BAS trait scale, not the process |
| [Biological motion perception](../processes/face_and_object_perception.md#hed-biological-motion-perception) | `close` | biological motion | `trm_kYtw4QBOKCbsM` | (none) | - | - |
| [Body ownership](../processes/awareness_agency_and_metacognition.md#hed-body-ownership) | `close` | sense of body ownership | `trm_4e5faabfe8ce3` | (none) | 1 | - |
| [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization) | `exact` | categorization | `trm_4a3fd79d09c28` | Reasoning and Decision Making | 5 | - |
| [Causal reasoning](../processes/reasoning_and_problem_solving.md#hed-causal-reasoning) | `related` | reasoning | `trm_4a3fd79d0aec1` | Reasoning and Decision Making | 5 | Atlas has only the broader parent term |
| [Choice commitment](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-choice-commitment) | `none` | - | - | (none) | - | No entry for decision commitment |
| [Chunking](../processes/short_term_and_working_memory.md#hed-chunking) | `exact` | chunking | `trm_4a3fd79d09cae` | Executive/Cognitive Control | 4 | - |
| [Cognitive reappraisal](../processes/emotion_perception_and_regulation.md#hed-cognitive-reappraisal) | `close` | emotional reappraisal | `trm_557b4844ca14d` | (none) | - | Atlas entry has no definition |
| [Competition](../processes/social_cognition_and_strategic_social_choice.md#hed-competition) | `exact` | competition | `trm_4a3fd79d09daa` | (none) | - | - |
| [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring) | `related` | monitoring | `trm_4a3fd79d0a94f` | Executive/Cognitive Control | 1 | Atlas has only the broader parent term |
| [Consolidation](../processes/long_term_memory.md#hed-consolidation) | `exact` | consolidation | `trm_4a3fd79d0b8cd` | Learning and Memory | - | - |
| [Cooperation](../processes/social_cognition_and_strategic_social_choice.md#hed-cooperation) | `none` | - | - | (none) | - | No cooperation entry |
| [Declarative memory](../processes/long_term_memory.md#hed-declarative-memory) | `exact` | declarative memory | `trm_4a3fd79d0a04f` | Learning and Memory | 7 | - |
| [Deductive reasoning](../processes/reasoning_and_problem_solving.md#hed-deductive-reasoning) | `exact` | deductive reasoning | `trm_4a3fd79d0a072` | Reasoning and Decision Making | 1 | - |
| [Delay discounting](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-delay-discounting) | `exact` | delay discounting | `trm_a4WdpQW5JYPH0` | (none) | 3 | - |
| [Depth perception](../processes/face_and_object_perception.md#hed-depth-perception) | `exact` | depth perception | `trm_4a3fd79d0a0a1` | Perception | - | - |
| [Directed forgetting](../processes/long_term_memory.md#hed-directed-forgetting) | `close` | intentional forgetting | `trm_4a3fd79d0a689` | Learning and Memory | - | Atlas names the construct, not the paradigm effect |
| [Discourse processing](../processes/language_comprehension_and_production.md#hed-discourse-processing) | `exact` | discourse processing | `trm_4a3fd79d0b6f5` | Language | - | - |
| [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention) | `exact` | divided attention | `trm_4a3fd79d0a116` | Attention | 5 | - |
| [Effort allocation](../processes/reward_anticipation_and_motivation.md#hed-effort-allocation) | `related` | effort | `trm_4a3fd79d0a151` | (none) | - | Atlas has only the broader parent term |
| [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition) | `exact` | emotion recognition | `trm_4a3fd79d0b665` | Emotion | 2 | - |
| [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation) | `exact` | emotion regulation | `trm_51a690a7492eb` | (none) | 10 | - |
| [Encoding](../processes/long_term_memory.md#hed-encoding) | `exact` | encoding | `trm_4a3fd79d0b8e5` | Learning and Memory | 3 | - |
| [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory) | `exact` | episodic memory | `trm_4a3fd79d0a1f4` | Learning and Memory | 6 | - |
| [Error correction](../processes/inhibitory_control_and_conflict_monitoring.md#hed-error-correction) | `none` | - | - | (none) | - | No corresponding Atlas concept |
| [Error detection](../processes/inhibitory_control_and_conflict_monitoring.md#hed-error-detection) | `exact` | error detection | `trm_4a3fd79d0a20c` | Executive/Cognitive Control | 7 | - |
| [Executive attention](../processes/inhibitory_control_and_conflict_monitoring.md#hed-executive-attention) | `related` | attention | `trm_4a3fd79d09902` | Attention | 29 | Atlas has only the broader parent term |
| [Expressive suppression](../processes/emotion_perception_and_regulation.md#hed-expressive-suppression) | `none` | - | - | (none) | - | No corresponding Atlas concept |
| [Extinction](../processes/associative_learning_and_reinforcement.md#hed-extinction) | `exact` | extinction | `trm_4fe8edc62f613` | (none) | - | - |
| [Face identity recognition](../processes/face_and_object_perception.md#hed-face-identity-recognition) | `close` | face recognition | `trm_4a3fd79d0a30c` | Learning and Memory | 6 | Atlas entry does not separate identity from expression |
| [Face perception](../processes/face_and_object_perception.md#hed-face-perception) | `exact` | face perception | `trm_4a3fd79d0a300` | Perception | 1 | - |
| [Familiarity](../processes/long_term_memory.md#hed-familiarity) | `exact` | familiarity | `trm_4a3fd79d0b8fc` | Learning and Memory | - | - |
| [Feature-based attention](../processes/selective_and_sustained_attention.md#hed-feature-based-attention) | `exact` | feature-based attention | `trm_5524572b66764` | (none) | - | - |
| [Feeling of knowing](../processes/awareness_agency_and_metacognition.md#hed-feeling-of-knowing) | `none` | - | - | (none) | - | No feeling-of-knowing entry |
| [Fine motor control](../processes/motor_preparation_timing_and_execution.md#hed-fine-motor-control) | `related` | motor control | `trm_4a3fd79d0a972` | Action | 26 | Atlas does not separate fine motor control |
| [Forgetting](../processes/long_term_memory.md#hed-forgetting) | `exact` | forgetting | `trm_4a3fd79d0b908` | Learning and Memory | 4 | - |
| [Goal maintenance](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-goal-maintenance) | `exact` | goal maintenance | `trm_4a3fd79d0a431` | Executive/Cognitive Control | 3 | - |
| [Goal-directed behavior](../processes/associative_learning_and_reinforcement.md#hed-goal-directed-behavior) | `none` | - | - | (none) | - | No goal-directed control entry |
| [Grasping](../processes/motor_preparation_timing_and_execution.md#hed-grasping) | `none` | - | - | (none) | - | No grasping entry |
| [Gustatory perception](../processes/face_and_object_perception.md#hed-gustatory-perception) | `exact` | gustatory perception | `trm_4a3fd79d0a477` | Perception | - | - |
| [Habit](../processes/associative_learning_and_reinforcement.md#hed-habit) | `exact` | habit | `trm_4a3fd79d0a483` | Learning and Memory | - | - |
| [Hypothesis testing](../processes/reasoning_and_problem_solving.md#hed-hypothesis-testing) | `none` | - | - | (none) | - | No hypothesis testing entry |
| [Imitation](../processes/social_cognition_and_strategic_social_choice.md#hed-imitation) | `none` | - | - | (none) | - | No imitation entry |
| [Implicit memory](../processes/implicit_and_statistical_learning.md#hed-implicit-memory) | `exact` | implicit memory | `trm_4a3fd79d0a533` | Learning and Memory | 1 | - |
| [In-group/out-group processing](../processes/social_cognition_and_strategic_social_choice.md#hed-in-group-out-group-processing) | `none` | - | - | (none) | - | No in-group/out-group entry |
| [Incentive salience](../processes/reward_anticipation_and_motivation.md#hed-incentive-salience) | `exact` | incentive salience | `trm_QehTtEcwPuRtK` | (none) | - | - |
| [Inductive reasoning](../processes/reasoning_and_problem_solving.md#hed-inductive-reasoning) | `exact` | inductive reasoning | `trm_4a3fd79d0a590` | Reasoning and Decision Making | 1 | Atlas also has the narrower `induction` |
| [Insight](../processes/reasoning_and_problem_solving.md#hed-insight) | `exact` | insight | `trm_4a3fd79d0a62b` | Reasoning and Decision Making | - | - |
| [Instrumental conditioning](../processes/associative_learning_and_reinforcement.md#hed-instrumental-conditioning) | `exact` | instrumental conditioning | `trm_4a3fd79d0a642` | Learning and Memory | 1 | - |
| [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control) | `exact` | interference control | `trm_551f11bb8f6a8` | (none) | 5 | Atlas also has `interference resolution` |
| [Interoceptive awareness](../processes/awareness_agency_and_metacognition.md#hed-interoceptive-awareness) | `exact` | Interoceptive awareness | `trm_WoLBai9ycl8yE` | (none) | 1 | - |
| [Intertemporal choice](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-intertemporal-choice) | `exact` | intertemporal choice | `trm_558c73324a6ca` | (none) | 4 | - |
| [Joint attention](../processes/social_cognition_and_strategic_social_choice.md#hed-joint-attention) | `exact` | joint attention | `trm_4b75ed06c917d` | Attention | 5 | - |
| [Judgment of learning](../processes/awareness_agency_and_metacognition.md#hed-judgment-of-learning) | `none` | - | - | (none) | - | No judgment-of-learning entry |
| [Language comprehension](../processes/language_comprehension_and_production.md#hed-language-comprehension) | `exact` | language comprehension | `trm_4a3fd79d0a775` | Language | 13 | - |
| [Language production](../processes/language_comprehension_and_production.md#hed-language-production) | `exact` | language production | `trm_4a3fd79d0a78d` | Language | 6 | - |
| [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access) | `exact` | lexical access | `trm_4a3fd79d0b80f` | Language | 8 | - |
| [Manipulation](../processes/short_term_and_working_memory.md#hed-manipulation) | `exact` | manipulation | `trm_4a3fd79d0ba3c` | Executive/Cognitive Control | 1 | - |
| [Masking](../processes/awareness_agency_and_metacognition.md#hed-masking) | `close` | visual masking | `trm_4a3fd79d0b492` | Perception | 2 | Atlas splits masking by modality: visual, auditory, lateral |
| [Mathematical reasoning](../processes/reasoning_and_problem_solving.md#hed-mathematical-reasoning) | `exact` | mathematical reasoning | `trm_4a3fd79d0a862` | Reasoning and Decision Making | 3 | - |
| [Means-ends analysis](../processes/reasoning_and_problem_solving.md#hed-means-ends-analysis) | `none` | - | - | (none) | - | No means-ends analysis entry |
| [Mental rotation](../processes/spatial_cognition_and_navigation.md#hed-mental-rotation) | `exact` | mental rotation | `trm_4a3fd79d0a914` | Perception | 3 | - |
| [Metacognitive control](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-control) | `related` | metacognition | `trm_4a3fd79d0a920` | (none) | - | Atlas has no monitoring/control split |
| [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring) | `related` | metacognition | `trm_4a3fd79d0a920` | (none) | - | Atlas has no monitoring/control split |
| [Mind wandering](../processes/awareness_agency_and_metacognition.md#hed-mind-wandering) | `none` | - | - | (none) | - | No mind wandering entry |
| [Model-based learning](../processes/associative_learning_and_reinforcement.md#hed-model-based-learning) | `none` | - | - | (none) | - | Computational RL vocabulary post-dates the Atlas's curation |
| [Model-free learning](../processes/associative_learning_and_reinforcement.md#hed-model-free-learning) | `none` | - | - | (none) | - | Computational RL vocabulary post-dates the Atlas's curation |
| [Motion perception](../processes/face_and_object_perception.md#hed-motion-perception) | `none` | - | - | (none) | - | No motion perception entry; `emotion perception` is unrelated |
| [Motor memory](../processes/motor_preparation_timing_and_execution.md#hed-motor-memory) | `related` | memory | `trm_4a3fd79d0a891` | Learning and Memory | 4 | Atlas has no motor memory entry |
| [Motor planning](../processes/motor_preparation_timing_and_execution.md#hed-motor-planning) | `exact` | motor planning | `trm_4a3fd79d0a9a1` | Action | 6 | - |
| [Motor preparation](../processes/motor_preparation_timing_and_execution.md#hed-motor-preparation) | `none` | - | - | (none) | - | No motor preparation entry |
| [Motor sequence learning](../processes/motor_preparation_timing_and_execution.md#hed-motor-sequence-learning) | `exact` | motor sequence learning | `trm_4a3fd79d0a9b9` | Learning and Memory | 1 | - |
| [Motor timing](../processes/motor_preparation_timing_and_execution.md#hed-motor-timing) | `related` | timing | `trm_vqA8b1BrA6U4V` | (none) | - | Atlas has only the broader parent term |
| [Naming](../processes/language_comprehension_and_production.md#hed-naming) | `exact` | naming | `trm_4a3fd79d0a9dc` | Language | 3 | - |
| [Object-based attention](../processes/selective_and_sustained_attention.md#hed-object-based-attention) | `exact` | object-based attention | `trm_552185f5cda66` | Attention | - | - |
| [Olfactory perception](../processes/face_and_object_perception.md#hed-olfactory-perception) | `exact` | olfactory perception | `trm_4a3fd79d0aac8` | Perception | 5 | - |
| [Orienting](../processes/selective_and_sustained_attention.md#hed-orienting) | `none` | - | - | (none) | - | No corresponding Atlas concept |
| [Pattern completion](../processes/long_term_memory.md#hed-pattern-completion) | `none` | - | - | (none) | - | No corresponding Atlas concept |
| [Pattern recognition](../processes/face_and_object_perception.md#hed-pattern-recognition) | `exact` | pattern recognition | `trm_4a3fd79d0ab65` | Perception | 4 | - |
| [Pattern separation](../processes/long_term_memory.md#hed-pattern-separation) | `none` | - | - | (none) | - | No corresponding Atlas concept |
| [Pavlovian conditioning](../processes/associative_learning_and_reinforcement.md#hed-pavlovian-conditioning) | `exact` | pavlovian conditioning | `trm_4a3fd79d0ab70` | Learning and Memory | 1 | - |
| [Perceptual awareness](../processes/awareness_agency_and_metacognition.md#hed-perceptual-awareness) | `related` | consciousness | `trm_4a3fd79d09e35` | (none) | - | Atlas has only the broader parent term |
| [Perceptual decision making](../processes/perceptual_decision_making_evidence_accumulation.md#hed-perceptual-decision-making) | `related` | decision making | `trm_4a3fd79d0a038` | Reasoning and Decision Making | 12 | Atlas has only the broader parent term |
| [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking) | `close` | theory of mind | `trm_4a3fd79d0b392` | Social Function | 6 | Atlas has no perspective-taking entry; `worldview` is unrelated |
| [Phonological awareness](../processes/language_comprehension_and_production.md#hed-phonological-awareness) | `exact` | phonological awareness | `trm_5240fddc2e43e` | (none) | 2 | - |
| [Phonological encoding](../processes/language_comprehension_and_production.md#hed-phonological-encoding) | `exact` | phonological encoding | `trm_4a3fd79d0ac87` | Language | 6 | - |
| [Pitch perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-pitch-perception) | `exact` | pitch perception | `trm_H19qgUFFeZaLg` | (none) | - | - |
| [Planning](../processes/reasoning_and_problem_solving.md#hed-planning) | `exact` | planning | `trm_4a3fd79d0acc1` | Executive/Cognitive Control | 4 | - |
| [Policy learning](../processes/associative_learning_and_reinforcement.md#hed-policy-learning) | `related` | learning | `trm_4a3fd79d0a7bb` | Learning and Memory | 2 | Atlas has only the broader parent term |
| [Proactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-proactive-control) | `exact` | proactive control | `trm_557b49851e991` | Executive/Cognitive Control | 6 | - |
| [Proactive interference](../processes/long_term_memory.md#hed-proactive-interference) | `exact` | proactive interference | `trm_4a3fd79d0adab` | Learning and Memory | 3 | - |
| [Probability judgment](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-probability-judgment) | `related` | judgment | `trm_4a3fd79d0a723` | Reasoning and Decision Making | 1 | Atlas has only the generic `judgment` |
| [Procedural memory](../processes/implicit_and_statistical_learning.md#hed-procedural-memory) | `exact` | procedural memory | `trm_4a3fd79d0addc` | (none) | 4 | - |
| [Proprioception](../processes/motor_preparation_timing_and_execution.md#hed-proprioception) | `exact` | proprioception | `trm_4a3fd79d0ae3d` | Perception | 2 | - |
| [Prospective memory](../processes/long_term_memory.md#hed-prospective-memory) | `exact` | prospective memory | `trm_4a3fd79d0ae70` | Learning and Memory | - | - |
| [Reaching](../processes/motor_preparation_timing_and_execution.md#hed-reaching) | `none` | - | - | (none) | - | No corresponding Atlas concept |
| [Reactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-reactive-control) | `exact` | Reactive Control | `trm_0wLVVlkHaAov9` | (none) | 1 | - |
| [Reading](../processes/language_comprehension_and_production.md#hed-reading) | `exact` | reading | `trm_4a3fd79d0aeb6` | Language | 8 | - |
| [Recall](../processes/long_term_memory.md#hed-recall) | `exact` | recall | `trm_4a3fd79d0b95b` | Learning and Memory | 4 | - |
| [Reciprocity](../processes/social_cognition_and_strategic_social_choice.md#hed-reciprocity) | `exact` | reciprocity | `trm_seBaaqL9E7Q1v` | (none) | - | - |
| [Recognition](../processes/long_term_memory.md#hed-recognition) | `exact` | recognition | `trm_4a3fd79d0b967` | Learning and Memory | 3 | - |
| [Recollection](../processes/long_term_memory.md#hed-recollection) | `none` | - | - | (none) | - | No recollection entry despite the Atlas carrying `familiarity` |
| [Reconsolidation](../processes/long_term_memory.md#hed-reconsolidation) | `exact` | reconsolidation | `trm_4a3fd79d0b972` | Learning and Memory | - | - |
| [Rehearsal](../processes/short_term_and_working_memory.md#hed-rehearsal) | `exact` | rehearsal | `trm_4a3fd79d0ba54` | Learning and Memory | - | - |
| [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning) | `exact` | reinforcement learning | `trm_557b4993a0fdd` | Learning and Memory | 7 | - |
| [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict) | `exact` | response conflict | `trm_557b49ad14adf` | Executive/Cognitive Control | 3 | - |
| [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution) | `exact` | response execution | `trm_557b4a7315f1b` | Action | 24 | - |
| [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition) | `exact` | response inhibition | `trm_4a3fd79d0af66` | Executive/Cognitive Control | 19 | - |
| [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection) | `exact` | response selection | `trm_4a3fd79d0af71` | Action | 28 | - |
| [Retrieval](../processes/long_term_memory.md#hed-retrieval) | `exact` | retrieval | `trm_4a3fd79d0af94` | Learning and Memory | - | - |
| [Retroactive interference](../processes/long_term_memory.md#hed-retroactive-interference) | `exact` | retroactive interference | `trm_4a3fd79d0afab` | Learning and Memory | 1 | - |
| [Reversal learning](../processes/associative_learning_and_reinforcement.md#hed-reversal-learning) | `none` | - | - | (none) | - | No reversal learning concept; registered only as a task |
| [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation) | `exact` | reward anticipation | `trm_557b4a81a4a17` | (none) | 1 | - |
| [Reward consumption](../processes/reward_anticipation_and_motivation.md#hed-reward-consumption) | `related` | reward processing | `trm_4b6525253c63f` | Learning and Memory | 2 | Atlas has only the broader parent term |
| [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error) | `close` | monetary reward prediction error | `trm_559f0a5b4cd36` | Reasoning and Decision Making | 1 | Atlas has only the monetary-domain form, not a general RPE |
| [Risk processing](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-risk-processing) | `exact` | risk processing | `trm_557b4a913f8cc` | Reasoning and Decision Making | 3 | - |
| [Saccade](../processes/motor_preparation_timing_and_execution.md#hed-saccade) | `none` | - | - | (none) | - | No saccade entry |
| [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention) | `exact` | selective attention | `trm_4a3fd79d0b043` | Attention | 6 | - |
| [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring) | `exact` | self monitoring | `trm_4a3fd79d0b05e` | Executive/Cognitive Control | 4 | - |
| [Self-other distinction](../processes/social_cognition_and_strategic_social_choice.md#hed-self-other-distinction) | `none` | - | - | (none) | - | No self-other distinction entry |
| [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing) | `close` | self-reference effect | `trm_vK5imljyKMUAL` | (none) | - | Atlas names the effect rather than the process |
| [Semantic knowledge](../processes/language_comprehension_and_production.md#hed-semantic-knowledge) | `exact` | semantic knowledge | `trm_4a3fd79d0b077` | Language | 11 | Atlas also has `semantic information` |
| [Semantic memory](../processes/long_term_memory.md#hed-semantic-memory) | `exact` | semantic memory | `trm_4a3fd79d0b083` | Language | 6 | - |
| [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing) | `exact` | semantic processing | `trm_4a3fd79d0b87a` | Language | 6 | - |
| [Sense of agency](../processes/awareness_agency_and_metacognition.md#hed-sense-of-agency) | `close` | agency | `trm_5154b2f947fe9` | (none) | - | Atlas entry is broader than the action-effect sense |
| [Sentence comprehension](../processes/language_comprehension_and_production.md#hed-sentence-comprehension) | `exact` | sentence comprehension | `trm_4a3fd79d0b892` | Language | 4 | - |
| [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting) | `exact` | set shifting | `trm_4a3fd79d0b607` | Executive/Cognitive Control | 8 | - |
| [Social decision making](../processes/social_cognition_and_strategic_social_choice.md#hed-social-decision-making) | `related` | decision making | `trm_4a3fd79d0a038` | Reasoning and Decision Making | 12 | Atlas has no social decision-making entry |
| [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception) | `related` | perception | `trm_4a3fd79d0ab7c` | Perception | - | Atlas has no social perception entry |
| [Somatosensory perception](../processes/face_and_object_perception.md#hed-somatosensory-perception) | `close` | somatosensation | `trm_4a3fd79d0b160` | Perception | 6 | Atlas entry is framed anatomically |
| [Source memory](../processes/long_term_memory.md#hed-source-memory) | `exact` | source memory | `trm_4a3fd79d0b18f` | Learning and Memory | 1 | - |
| [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention) | `exact` | spatial attention | `trm_4a3fd79d0b1b2` | Attention | 2 | - |
| [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory) | `exact` | spatial memory | `trm_4a3fd79d0b1d5` | Learning and Memory | 5 | - |
| [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory) | `exact` | spatial working memory | `trm_4a3fd79d0b1e0` | Attention | 5 | - |
| [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception) | `exact` | speech perception | `trm_4a3fd79d0b1f7` | Language | 1 | - |
| [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production) | `exact` | speech production | `trm_4a3fd79d0b247` | Language | 6 | - |
| [Stereotyping](../processes/social_cognition_and_strategic_social_choice.md#hed-stereotyping) | `none` | - | - | (none) | - | No corresponding Atlas concept |
| [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use) | `related` | strategy | `trm_4a3fd79d0b29c` | (none) | 1 | Atlas names the object, not its use |
| [Subgoaling](../processes/reasoning_and_problem_solving.md#hed-subgoaling) | `none` | - | - | (none) | - | No corresponding Atlas concept |
| [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention) | `exact` | sustained attention | `trm_4a3fd79d0b311` | Attention | 7 | - |
| [Syntactic parsing](../processes/language_comprehension_and_production.md#hed-syntactic-parsing) | `exact` | syntactic parsing | `trm_4a3fd79d0b340` | Language | 4 | - |
| [Temporal attention](../processes/selective_and_sustained_attention.md#hed-temporal-attention) | `related` | attention | `trm_4a3fd79d09902` | Attention | 29 | Atlas has only the broader parent term |
| [Valuation](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-valuation) | `close` | reward valuation | `trm_5159c94667677` | (none) | 1 | - |
| [Value learning](../processes/associative_learning_and_reinforcement.md#hed-value-learning) | `related` | learning | `trm_4a3fd79d0a7bb` | Learning and Memory | 2 | Atlas has only the broader parent term |
| [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making) | `related` | decision making | `trm_4a3fd79d0a038` | Reasoning and Decision Making | 12 | Atlas has only the broader parent term |
| [Verbal fluency](../processes/language_comprehension_and_production.md#hed-verbal-fluency) | `exact` | verbal fluency | `trm_4a3fd79d0b44c` | Language | 9 | - |
| [Verbal memory](../processes/long_term_memory.md#hed-verbal-memory) | `exact` | verbal memory | `trm_4a3fd79d0b457` | Learning and Memory | 8 | - |
| [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory) | `close` | phonological working memory | `trm_4a3fd79d0ac9e` | Executive/Cognitive Control | 8 | Atlas frames verbal WM phonologically |
| [Visual form recognition](../processes/face_and_object_perception.md#hed-visual-form-recognition) | `exact` | visual form recognition | `trm_557b4b3a6a34d` | Perception | 11 | - |
| [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition) | `exact` | visual object recognition | `trm_4a3fd79d0b4a9` | Perception | 5 | - |
| [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception) | `exact` | visual perception | `trm_4a3fd79d0b4b5` | Perception | 40 | - |
| [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory) | `exact` | visual working memory | `trm_4a3fd79d0b4d8` | Attention | 6 | - |
| [Visuomotor adaptation](../processes/motor_preparation_timing_and_execution.md#hed-visuomotor-adaptation) | `none` | - | - | (none) | - | Atlas `adaptation` is sensory adaptation, not visuomotor recalibration |
| [Vocal-motor control](../processes/motor_preparation_timing_and_execution.md#hed-vocal-motor-control) | `related` | motor control | `trm_4a3fd79d0a972` | Action | 26 | Atlas has only the broader parent term |
| [Word recognition](../processes/language_comprehension_and_production.md#hed-word-recognition) | `exact` | word recognition | `trm_4a3fd79d0b58f` | Language | 5 | - |
| [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory) | `exact` | working memory | `trm_4a3fd79d0b5a7` | Executive/Cognitive Control | 27 | - |
| [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating) | `exact` | working memory updating | `trm_55b6b9a666604` | Learning and Memory | 1 | - |

## Atlas to catalog, matched concepts

132 Atlas concepts correspond to a process here, drawn on by 132 distinct
concept records. The count is lower than the number of matched processes because
several processes resolve to the same Atlas concept.

| Atlas concept | Concept ID | Match | Process | Atlas tasks | Relations |
|---|---|---|---|---|---|
| acoustic processing | `trm_4a3fd79d0971e` | `close` | [Acoustic processing](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-acoustic-processing) | 3 | 1 |
| action initiation | `trm_4a3fd79d0b5c0` | `exact` | [Action initiation](../processes/motor_preparation_timing_and_execution.md#hed-action-initiation) | - | - |
| active maintenance | `trm_4a3fd79d0ba0d` | `exact` | [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance) | 15 | 3 |
| priming | `trm_4e89aebaa311d` | `related` | [Affective priming](../processes/emotion_perception_and_regulation.md#hed-affective-priming) | - | 11 |
| analogical reasoning | `trm_4a3fd79d09810` | `exact` | [Analogical reasoning](../processes/reasoning_and_problem_solving.md#hed-analogical-reasoning) | 1 | 2 |
| association learning | `trm_4a3fd79d098c9` | `exact` | [Associative learning](../processes/associative_learning_and_reinforcement.md#hed-associative-learning) | 7 | 3 |
| attention shifting | `trm_4a3fd79d0b5fb` | `exact` | [Attention shifting](../processes/selective_and_sustained_attention.md#hed-attention-shifting) | 12 | - |
| auditory perception | `trm_4a3fd79d09ab2` | `exact` | [Auditory perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-perception) | 21 | 22 |
| auditory tone discrimination | `trm_557b476527a27` | `exact` | [Auditory tone discrimination](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-auditory-tone-discrimination) | 3 | 3 |
| autobiographical memory | `trm_4a3fd79d09b10` | `exact` | [Autobiographical memory](../processes/long_term_memory.md#hed-autobiographical-memory) | 2 | 2 |
| biological motion | `trm_kYtw4QBOKCbsM` | `close` | [Biological motion perception](../processes/face_and_object_perception.md#hed-biological-motion-perception) | - | 1 |
| sense of body ownership | `trm_4e5faabfe8ce3` | `close` | [Body ownership](../processes/awareness_agency_and_metacognition.md#hed-body-ownership) | 1 | 1 |
| categorization | `trm_4a3fd79d09c28` | `exact` | [Categorization](../processes/reasoning_and_problem_solving.md#hed-categorization) | 5 | 4 |
| reasoning | `trm_4a3fd79d0aec1` | `related` | [Causal reasoning](../processes/reasoning_and_problem_solving.md#hed-causal-reasoning) | 5 | 11 |
| chunking | `trm_4a3fd79d09cae` | `exact` | [Chunking](../processes/short_term_and_working_memory.md#hed-chunking) | 4 | 1 |
| emotional reappraisal | `trm_557b4844ca14d` | `close` | [Cognitive reappraisal](../processes/emotion_perception_and_regulation.md#hed-cognitive-reappraisal) | - | 3 |
| competition | `trm_4a3fd79d09daa` | `exact` | [Competition](../processes/social_cognition_and_strategic_social_choice.md#hed-competition) | - | - |
| monitoring | `trm_4a3fd79d0a94f` | `related` | [Conflict monitoring](../processes/inhibitory_control_and_conflict_monitoring.md#hed-conflict-monitoring) | 1 | 1 |
| consolidation | `trm_4a3fd79d0b8cd` | `exact` | [Consolidation](../processes/long_term_memory.md#hed-consolidation) | - | 3 |
| declarative memory | `trm_4a3fd79d0a04f` | `exact` | [Declarative memory](../processes/long_term_memory.md#hed-declarative-memory) | 7 | 9 |
| deductive reasoning | `trm_4a3fd79d0a072` | `exact` | [Deductive reasoning](../processes/reasoning_and_problem_solving.md#hed-deductive-reasoning) | 1 | 1 |
| delay discounting | `trm_a4WdpQW5JYPH0` | `exact` | [Delay discounting](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-delay-discounting) | 3 | - |
| depth perception | `trm_4a3fd79d0a0a1` | `exact` | [Depth perception](../processes/face_and_object_perception.md#hed-depth-perception) | - | 2 |
| intentional forgetting | `trm_4a3fd79d0a689` | `close` | [Directed forgetting](../processes/long_term_memory.md#hed-directed-forgetting) | - | 1 |
| discourse processing | `trm_4a3fd79d0b6f5` | `exact` | [Discourse processing](../processes/language_comprehension_and_production.md#hed-discourse-processing) | - | - |
| divided attention | `trm_4a3fd79d0a116` | `exact` | [Divided attention](../processes/selective_and_sustained_attention.md#hed-divided-attention) | 5 | 2 |
| effort | `trm_4a3fd79d0a151` | `related` | [Effort allocation](../processes/reward_anticipation_and_motivation.md#hed-effort-allocation) | - | 2 |
| emotion recognition | `trm_4a3fd79d0b665` | `exact` | [Emotion recognition](../processes/emotion_perception_and_regulation.md#hed-emotion-recognition) | 2 | 4 |
| emotion regulation | `trm_51a690a7492eb` | `exact` | [Emotion regulation](../processes/emotion_perception_and_regulation.md#hed-emotion-regulation) | 10 | 5 |
| encoding | `trm_4a3fd79d0b8e5` | `exact` | [Encoding](../processes/long_term_memory.md#hed-encoding) | 3 | 11 |
| episodic memory | `trm_4a3fd79d0a1f4` | `exact` | [Episodic memory](../processes/long_term_memory.md#hed-episodic-memory) | 6 | 6 |
| error detection | `trm_4a3fd79d0a20c` | `exact` | [Error detection](../processes/inhibitory_control_and_conflict_monitoring.md#hed-error-detection) | 7 | 1 |
| extinction | `trm_4fe8edc62f613` | `exact` | [Extinction](../processes/associative_learning_and_reinforcement.md#hed-extinction) | - | 5 |
| face recognition | `trm_4a3fd79d0a30c` | `close` | [Face identity recognition](../processes/face_and_object_perception.md#hed-face-identity-recognition) | 6 | 3 |
| face perception | `trm_4a3fd79d0a300` | `exact` | [Face perception](../processes/face_and_object_perception.md#hed-face-perception) | 1 | 2 |
| familiarity | `trm_4a3fd79d0b8fc` | `exact` | [Familiarity](../processes/long_term_memory.md#hed-familiarity) | - | 1 |
| feature-based attention | `trm_5524572b66764` | `exact` | [Feature-based attention](../processes/selective_and_sustained_attention.md#hed-feature-based-attention) | - | 1 |
| forgetting | `trm_4a3fd79d0b908` | `exact` | [Forgetting](../processes/long_term_memory.md#hed-forgetting) | 4 | 2 |
| goal maintenance | `trm_4a3fd79d0a431` | `exact` | [Goal maintenance](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-goal-maintenance) | 3 | 3 |
| gustatory perception | `trm_4a3fd79d0a477` | `exact` | [Gustatory perception](../processes/face_and_object_perception.md#hed-gustatory-perception) | - | - |
| habit | `trm_4a3fd79d0a483` | `exact` | [Habit](../processes/associative_learning_and_reinforcement.md#hed-habit) | - | 1 |
| implicit memory | `trm_4a3fd79d0a533` | `exact` | [Implicit memory](../processes/implicit_and_statistical_learning.md#hed-implicit-memory) | 1 | 2 |
| incentive salience | `trm_QehTtEcwPuRtK` | `exact` | [Incentive salience](../processes/reward_anticipation_and_motivation.md#hed-incentive-salience) | - | 1 |
| inductive reasoning | `trm_4a3fd79d0a590` | `exact` | [Inductive reasoning](../processes/reasoning_and_problem_solving.md#hed-inductive-reasoning) | 1 | 2 |
| insight | `trm_4a3fd79d0a62b` | `exact` | [Insight](../processes/reasoning_and_problem_solving.md#hed-insight) | - | - |
| instrumental conditioning | `trm_4a3fd79d0a642` | `exact` | [Instrumental conditioning](../processes/associative_learning_and_reinforcement.md#hed-instrumental-conditioning) | 1 | 2 |
| interference control | `trm_551f11bb8f6a8` | `exact` | [Interference control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-interference-control) | 5 | 1 |
| Interoceptive awareness | `trm_WoLBai9ycl8yE` | `exact` | [Interoceptive awareness](../processes/awareness_agency_and_metacognition.md#hed-interoceptive-awareness) | 1 | - |
| intertemporal choice | `trm_558c73324a6ca` | `exact` | [Intertemporal choice](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-intertemporal-choice) | 4 | 2 |
| joint attention | `trm_4b75ed06c917d` | `exact` | [Joint attention](../processes/social_cognition_and_strategic_social_choice.md#hed-joint-attention) | 5 | 1 |
| language comprehension | `trm_4a3fd79d0a775` | `exact` | [Language comprehension](../processes/language_comprehension_and_production.md#hed-language-comprehension) | 13 | 6 |
| language production | `trm_4a3fd79d0a78d` | `exact` | [Language production](../processes/language_comprehension_and_production.md#hed-language-production) | 6 | 2 |
| lexical access | `trm_4a3fd79d0b80f` | `exact` | [Lexical access](../processes/language_comprehension_and_production.md#hed-lexical-access) | 8 | - |
| manipulation | `trm_4a3fd79d0ba3c` | `exact` | [Manipulation](../processes/short_term_and_working_memory.md#hed-manipulation) | 1 | - |
| visual masking | `trm_4a3fd79d0b492` | `close` | [Masking](../processes/awareness_agency_and_metacognition.md#hed-masking) | 2 | 2 |
| mathematical reasoning | `trm_4a3fd79d0a862` | `exact` | [Mathematical reasoning](../processes/reasoning_and_problem_solving.md#hed-mathematical-reasoning) | 3 | 1 |
| mental rotation | `trm_4a3fd79d0a914` | `exact` | [Mental rotation](../processes/spatial_cognition_and_navigation.md#hed-mental-rotation) | 3 | - |
| metacognition | `trm_4a3fd79d0a920` | `related` | [Metacognitive monitoring](../processes/awareness_agency_and_metacognition.md#hed-metacognitive-monitoring) | - | 1 |
| memory | `trm_4a3fd79d0a891` | `related` | [Motor memory](../processes/motor_preparation_timing_and_execution.md#hed-motor-memory) | 4 | 23 |
| motor planning | `trm_4a3fd79d0a9a1` | `exact` | [Motor planning](../processes/motor_preparation_timing_and_execution.md#hed-motor-planning) | 6 | 1 |
| motor sequence learning | `trm_4a3fd79d0a9b9` | `exact` | [Motor sequence learning](../processes/motor_preparation_timing_and_execution.md#hed-motor-sequence-learning) | 1 | 1 |
| timing | `trm_vqA8b1BrA6U4V` | `related` | [Motor timing](../processes/motor_preparation_timing_and_execution.md#hed-motor-timing) | - | 1 |
| naming | `trm_4a3fd79d0a9dc` | `exact` | [Naming](../processes/language_comprehension_and_production.md#hed-naming) | 3 | 1 |
| object-based attention | `trm_552185f5cda66` | `exact` | [Object-based attention](../processes/selective_and_sustained_attention.md#hed-object-based-attention) | - | 1 |
| olfactory perception | `trm_4a3fd79d0aac8` | `exact` | [Olfactory perception](../processes/face_and_object_perception.md#hed-olfactory-perception) | 5 | 2 |
| pattern recognition | `trm_4a3fd79d0ab65` | `exact` | [Pattern recognition](../processes/face_and_object_perception.md#hed-pattern-recognition) | 4 | 2 |
| pavlovian conditioning | `trm_4a3fd79d0ab70` | `exact` | [Pavlovian conditioning](../processes/associative_learning_and_reinforcement.md#hed-pavlovian-conditioning) | 1 | 3 |
| consciousness | `trm_4a3fd79d09e35` | `related` | [Perceptual awareness](../processes/awareness_agency_and_metacognition.md#hed-perceptual-awareness) | - | 4 |
| theory of mind | `trm_4a3fd79d0b392` | `close` | [Perspective taking](../processes/social_cognition_and_strategic_social_choice.md#hed-perspective-taking) | 6 | 4 |
| phonological awareness | `trm_5240fddc2e43e` | `exact` | [Phonological awareness](../processes/language_comprehension_and_production.md#hed-phonological-awareness) | 2 | - |
| phonological encoding | `trm_4a3fd79d0ac87` | `exact` | [Phonological encoding](../processes/language_comprehension_and_production.md#hed-phonological-encoding) | 6 | 2 |
| pitch perception | `trm_H19qgUFFeZaLg` | `exact` | [Pitch perception](../processes/auditory_and_pre_attentive_deviance_processing.md#hed-pitch-perception) | - | 2 |
| planning | `trm_4a3fd79d0acc1` | `exact` | [Planning](../processes/reasoning_and_problem_solving.md#hed-planning) | 4 | 2 |
| proactive control | `trm_557b49851e991` | `exact` | [Proactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-proactive-control) | 6 | 4 |
| proactive interference | `trm_4a3fd79d0adab` | `exact` | [Proactive interference](../processes/long_term_memory.md#hed-proactive-interference) | 3 | - |
| judgment | `trm_4a3fd79d0a723` | `related` | [Probability judgment](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-probability-judgment) | 1 | 3 |
| procedural memory | `trm_4a3fd79d0addc` | `exact` | [Procedural memory](../processes/implicit_and_statistical_learning.md#hed-procedural-memory) | 4 | 1 |
| proprioception | `trm_4a3fd79d0ae3d` | `exact` | [Proprioception](../processes/motor_preparation_timing_and_execution.md#hed-proprioception) | 2 | 2 |
| prospective memory | `trm_4a3fd79d0ae70` | `exact` | [Prospective memory](../processes/long_term_memory.md#hed-prospective-memory) | - | 1 |
| Reactive Control | `trm_0wLVVlkHaAov9` | `exact` | [Reactive control](../processes/inhibitory_control_and_conflict_monitoring.md#hed-reactive-control) | 1 | 1 |
| reading | `trm_4a3fd79d0aeb6` | `exact` | [Reading](../processes/language_comprehension_and_production.md#hed-reading) | 8 | 5 |
| recall | `trm_4a3fd79d0b95b` | `exact` | [Recall](../processes/long_term_memory.md#hed-recall) | 4 | 4 |
| reciprocity | `trm_seBaaqL9E7Q1v` | `exact` | [Reciprocity](../processes/social_cognition_and_strategic_social_choice.md#hed-reciprocity) | - | - |
| recognition | `trm_4a3fd79d0b967` | `exact` | [Recognition](../processes/long_term_memory.md#hed-recognition) | 3 | 13 |
| reconsolidation | `trm_4a3fd79d0b972` | `exact` | [Reconsolidation](../processes/long_term_memory.md#hed-reconsolidation) | - | 2 |
| rehearsal | `trm_4a3fd79d0ba54` | `exact` | [Rehearsal](../processes/short_term_and_working_memory.md#hed-rehearsal) | - | 2 |
| reinforcement learning | `trm_557b4993a0fdd` | `exact` | [Reinforcement learning](../processes/associative_learning_and_reinforcement.md#hed-reinforcement-learning) | 7 | 4 |
| response conflict | `trm_557b49ad14adf` | `exact` | [Response conflict](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-conflict) | 3 | 2 |
| response execution | `trm_557b4a7315f1b` | `exact` | [Response execution](../processes/motor_preparation_timing_and_execution.md#hed-response-execution) | 24 | 10 |
| response inhibition | `trm_4a3fd79d0af66` | `exact` | [Response inhibition](../processes/inhibitory_control_and_conflict_monitoring.md#hed-response-inhibition) | 19 | 3 |
| response selection | `trm_4a3fd79d0af71` | `exact` | [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection) | 28 | 3 |
| retrieval | `trm_4a3fd79d0af94` | `exact` | [Retrieval](../processes/long_term_memory.md#hed-retrieval) | - | 4 |
| retroactive interference | `trm_4a3fd79d0afab` | `exact` | [Retroactive interference](../processes/long_term_memory.md#hed-retroactive-interference) | 1 | 1 |
| reward anticipation | `trm_557b4a81a4a17` | `exact` | [Reward anticipation](../processes/reward_anticipation_and_motivation.md#hed-reward-anticipation) | 1 | 3 |
| reward processing | `trm_4b6525253c63f` | `related` | [Reward consumption](../processes/reward_anticipation_and_motivation.md#hed-reward-consumption) | 2 | 5 |
| monetary reward prediction error | `trm_559f0a5b4cd36` | `close` | [Reward prediction error](../processes/associative_learning_and_reinforcement.md#hed-reward-prediction-error) | 1 | 2 |
| risk processing | `trm_557b4a913f8cc` | `exact` | [Risk processing](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-risk-processing) | 3 | 2 |
| selective attention | `trm_4a3fd79d0b043` | `exact` | [Selective attention](../processes/selective_and_sustained_attention.md#hed-selective-attention) | 6 | 4 |
| self monitoring | `trm_4a3fd79d0b05e` | `exact` | [Self-monitoring](../processes/awareness_agency_and_metacognition.md#hed-self-monitoring) | 4 | 1 |
| self-reference effect | `trm_vK5imljyKMUAL` | `close` | [Self-referential processing](../processes/awareness_agency_and_metacognition.md#hed-self-referential-processing) | - | 1 |
| semantic knowledge | `trm_4a3fd79d0b077` | `exact` | [Semantic knowledge](../processes/language_comprehension_and_production.md#hed-semantic-knowledge) | 11 | 2 |
| semantic memory | `trm_4a3fd79d0b083` | `exact` | [Semantic memory](../processes/long_term_memory.md#hed-semantic-memory) | 6 | 3 |
| semantic processing | `trm_4a3fd79d0b87a` | `exact` | [Semantic processing](../processes/language_comprehension_and_production.md#hed-semantic-processing) | 6 | 3 |
| agency | `trm_5154b2f947fe9` | `close` | [Sense of agency](../processes/awareness_agency_and_metacognition.md#hed-sense-of-agency) | - | 1 |
| sentence comprehension | `trm_4a3fd79d0b892` | `exact` | [Sentence comprehension](../processes/language_comprehension_and_production.md#hed-sentence-comprehension) | 4 | 4 |
| set shifting | `trm_4a3fd79d0b607` | `exact` | [Set shifting](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-set-shifting) | 8 | 3 |
| perception | `trm_4a3fd79d0ab7c` | `related` | [Social perception](../processes/social_cognition_and_strategic_social_choice.md#hed-social-perception) | - | 21 |
| somatosensation | `trm_4a3fd79d0b160` | `close` | [Somatosensory perception](../processes/face_and_object_perception.md#hed-somatosensory-perception) | 6 | 8 |
| source memory | `trm_4a3fd79d0b18f` | `exact` | [Source memory](../processes/long_term_memory.md#hed-source-memory) | 1 | 1 |
| spatial attention | `trm_4a3fd79d0b1b2` | `exact` | [Spatial attention](../processes/selective_and_sustained_attention.md#hed-spatial-attention) | 2 | 3 |
| spatial memory | `trm_4a3fd79d0b1d5` | `exact` | [Spatial memory](../processes/spatial_cognition_and_navigation.md#hed-spatial-memory) | 5 | 2 |
| spatial working memory | `trm_4a3fd79d0b1e0` | `exact` | [Spatial working memory](../processes/short_term_and_working_memory.md#hed-spatial-working-memory) | 5 | 2 |
| speech perception | `trm_4a3fd79d0b1f7` | `exact` | [Speech perception](../processes/language_comprehension_and_production.md#hed-speech-perception) | 1 | 5 |
| speech production | `trm_4a3fd79d0b247` | `exact` | [Speech production](../processes/language_comprehension_and_production.md#hed-speech-production) | 6 | 4 |
| strategy | `trm_4a3fd79d0b29c` | `related` | [Strategy use](../processes/cognitive_flexibility_and_higher_order_executive_function.md#hed-strategy-use) | 1 | - |
| sustained attention | `trm_4a3fd79d0b311` | `exact` | [Sustained attention](../processes/selective_and_sustained_attention.md#hed-sustained-attention) | 7 | 1 |
| syntactic parsing | `trm_4a3fd79d0b340` | `exact` | [Syntactic parsing](../processes/language_comprehension_and_production.md#hed-syntactic-parsing) | 4 | - |
| attention | `trm_4a3fd79d09902` | `related` | [Temporal attention](../processes/selective_and_sustained_attention.md#hed-temporal-attention) | 29 | 19 |
| reward valuation | `trm_5159c94667677` | `close` | [Valuation](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-valuation) | 1 | 2 |
| learning | `trm_4a3fd79d0a7bb` | `related` | [Value learning](../processes/associative_learning_and_reinforcement.md#hed-value-learning) | 2 | 6 |
| decision making | `trm_4a3fd79d0a038` | `related` | [Value-based decision making](../processes/value_based_decision_making_under_risk_and_uncertainty.md#hed-value-based-decision-making) | 12 | 14 |
| verbal fluency | `trm_4a3fd79d0b44c` | `exact` | [Verbal fluency](../processes/language_comprehension_and_production.md#hed-verbal-fluency) | 9 | - |
| verbal memory | `trm_4a3fd79d0b457` | `exact` | [Verbal memory](../processes/long_term_memory.md#hed-verbal-memory) | 8 | 1 |
| phonological working memory | `trm_4a3fd79d0ac9e` | `close` | [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory) | 8 | 3 |
| visual form recognition | `trm_557b4b3a6a34d` | `exact` | [Visual form recognition](../processes/face_and_object_perception.md#hed-visual-form-recognition) | 11 | 7 |
| visual object recognition | `trm_4a3fd79d0b4a9` | `exact` | [Visual object recognition](../processes/face_and_object_perception.md#hed-visual-object-recognition) | 5 | 6 |
| visual perception | `trm_4a3fd79d0b4b5` | `exact` | [Visual perception](../processes/face_and_object_perception.md#hed-visual-perception) | 40 | 24 |
| visual working memory | `trm_4a3fd79d0b4d8` | `exact` | [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory) | 6 | 4 |
| motor control | `trm_4a3fd79d0a972` | `related` | [Vocal-motor control](../processes/motor_preparation_timing_and_execution.md#hed-vocal-motor-control) | 26 | 3 |
| word recognition | `trm_4a3fd79d0b58f` | `exact` | [Word recognition](../processes/language_comprehension_and_production.md#hed-word-recognition) | 5 | 5 |
| working memory | `trm_4a3fd79d0b5a7` | `exact` | [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory) | 27 | 24 |
| working memory updating | `trm_55b6b9a666604` | `exact` | [Working memory updating](../processes/short_term_and_working_memory.md#hed-working-memory-updating) | 1 | 2 |

## Atlas to catalog, concepts with no counterpart

786 Atlas concepts have no process in this catalog. Roughly half of the
Atlas concept layer is asserted by no task either, so a concept appearing here is not
evidence that it matters to anyone.

| Atlas concept | Concept ID | Atlas class | Atlas tasks | Relations |
|---|---|---|---|---|
| abductive reasoning | `trm_4a3fd79d096be` | Reasoning and Decision Making | - | 1 |
| abstract analogy | `trm_4a3fd79d096e3` | Reasoning and Decision Making | - | 1 |
| abstract knowledge | `trm_4a3fd79d096f0` | Reasoning and Decision Making | 1 | 1 |
| acoustic coding | `trm_4a3fd79d096fc` | Perception | - | 1 |
| acoustic encoding | `trm_4a3fd79d09707` | Perception | 1 | 4 |
| acoustic phonetic processing | `trm_4a3fd79d09713` | Language | 4 | 3 |
| action | `trm_4a3fd79d09735` | Action | 1 | 4 |
| action perception | `trm_5159c00c3dac3` | (none) | - | 1 |
| action-outcome learning | `trm_BKfaKR4cv8MwD` | (none) | - | - |
| activation | `trm_4a3fd79d09741` | (none) | - | - |
| activation level | `trm_4a3fd79d0974d` | (none) | - | - |
| Active Cognitive Inhibition | `trm_gQBevhggQHGxG` | (none) | - | 4 |
| active recall | `trm_4a3fd79d0b8b5` | Learning and Memory | - | - |
| active retrieval | `trm_4a3fd79d0b8c1` | Learning and Memory | 1 | 1 |
| acuity | `trm_4a3fd79d0b98a` | Perception | - | - |
| adaptation | `trm_4a3fd79d09758` | Learning and Memory | 1 | - |
| adaptive control | `trm_4a3fd79d09764` | Action | 1 | - |
| addiction | `trm_4fafd1626bf2b` | (none) | - | 3 |
| aesthetic exprience | `trm_gSGrsqTOSBVRa` | (none) | - | 1 |
| affect perception | `trm_4a3fd79d09770` | Perception | - | - |
| affect recognition | `trm_4a3fd79d0977b` | Emotion | - | - |
| agreeableness | `trm_523f5ee64102c` | (none) | 1 | - |
| altruism | `trm_4a3fd79d097b4` | Motivation | - | 1 |
| altruistic motivation | `trm_4a3fd79d097bf` | Motivation | - | - |
| alveolar | `trm_4a3fd79d097cb` | Language | - | - |
| amodal representation | `trm_4a3fd79d097d6` | (none) | - | 1 |
| anaesthetised unresponsive | `trm_HLeH7ee55sYqJ` | (none) | - | 1 |
| analog representation | `trm_4a3fd79d097e2` | (none) | - | - |
| analogical encoding | `trm_4a3fd79d097ed` | (none) | - | 2 |
| analogical inference | `trm_4a3fd79d097f9` | (none) | - | 1 |
| analogical problem solving | `trm_4a3fd79d09804` | Reasoning and Decision Making | - | - |
| analogical transfer | `trm_4a3fd79d0981b` | Reasoning and Decision Making | - | - |
| analogy | `trm_4a3fd79d09827` | (none) | - | 2 |
| anchoring | `trm_4a3fd79d09833` | Reasoning and Decision Making | - | 1 |
| anhedonia | `trm_52583dceb345e` | (none) | 1 | - |
| animacy decision | `trm_557b471bc6cd8` | Reasoning and Decision Making | 1 | 2 |
| animacy perception | `trm_5159beaf80413` | Perception | 1 | 3 |
| anticipation | `trm_4a3fd79d09849` | (none) | 1 | 7 |
| antisocial personality | `trm_523e024c14df9` | (none) | 2 | - |
| anxiety | `trm_5022ef7599294` | Emotion | 9 | 1 |
| anxiety sensitivity | `trm_2aZtye4tjHl4U` | (none) | 1 | - |
| apparent motion | `trm_4a3fd79d09855` | Perception | - | 2 |
| apperception | `trm_4a3fd79d0986c` | (none) | - | - |
| appetite | `trm_52583e083c9ab` | (none) | 1 | - |
| appetitive motivation | `trm_4a3fd79d09877` | Motivation | 1 | 1 |
| arithmetic processing | `trm_558c7ae1eaf86` | (none) | 1 | 2 |
| arousal | `trm_4a3fd79d09883` | (none) | - | - |
| arousal (emotion) | `trm_59d184d09066b` | Emotion | 2 | - |
| arousal (physical) | `trm_59d184d0980bf` | (none) | - | - |
| articulation | `trm_4a3fd79d0988f` | Language | - | - |
| articulatory loop | `trm_4a3fd79d0ba19` | Learning and Memory | 1 | 2 |
| articulatory planning | `trm_4a3fd79d0989a` | Language | 1 | 1 |
| articulatory rehearsal | `trm_4a3fd79d098a6` | Learning and Memory | 4 | 2 |
| assimilation | `trm_4a3fd79d098b2` | (none) | - | 1 |
| association | `trm_4a3fd79d098bd` | (none) | 1 | 1 |
| associative priming | `trm_5521a5f310604` | (none) | - | 1 |
| attachment | `trm_4a3fd79d098e0` | Social Function | 2 | - |
| attended channel | `trm_4a3fd79d098eb` | (none) | 1 | - |
| attended stimulus | `trm_4a3fd79d098f7` | (none) | - | - |
| attention capacity | `trm_4a3fd79d0990e` | Attention | 2 | 1 |
| attention shift | `trm_4a3fd79d0b5d7` | Attention | 2 | 1 |
| attention span | `trm_4a3fd79d0b5e3` | Attention | 1 | 1 |
| attentional bias | `trm_510059e54b2cf` | (none) | 1 | - |
| attentional blink | `trm_4fea1aeaa7b17` | Attention | 2 | 1 |
| attentional effort | `trm_4a3fd79d09919` | Attention | - | 2 |
| attentional focusing | `trm_4a3fd79d0b5ef` | Attention | 12 | 1 |
| attentional resources | `trm_4a3fd79d09925` | Attention | - | 1 |
| attentional state | `trm_4a3fd79d09930` | Attention | - | 1 |
| attitude | `trm_4a3fd79d09947` | (none) | - | 2 |
| Attribution | `trm_i2BpAh3lWxDby` | (none) | 1 | - |
| audiovisual perception | `trm_4a3fd79d09953` | Perception | 1 | 3 |
| audition | `trm_4a3fd79d0995e` | Perception | 3 | 1 |
| auditory arithmetic processing | `trm_55b6b8e291dba` | (none) | 1 | 1 |
| auditory attention | `trm_4a3fd79d09a10` | Attention | 1 | 2 |
| auditory coding | `trm_4a3fd79d09a3d` | (none) | 1 | 4 |
| auditory encoding | `trm_4a3fd79d09a49` | Learning and Memory | 1 | 2 |
| auditory feedback | `trm_4a3fd79d09a55` | (none) | - | 1 |
| auditory grouping | `trm_4a3fd79d09a61` | Perception | - | 1 |
| auditory imagery | `trm_4a3fd79d09a6c` | (none) | - | - |
| auditory learning | `trm_4a3fd79d09a78` | Learning and Memory | - | - |
| auditory lexical access | `trm_4a3fd79d09a84` | Language | - | 1 |
| auditory localization | `trm_4a3fd79d09a8f` | Perception | - | 2 |
| auditory masking | `trm_4a3fd79d09a9b` | Perception | - | - |
| auditory memory | `trm_4a3fd79d09aa7` | Learning and Memory | 1 | 4 |
| auditory recognition | `trm_55ef687f48a9d` | (none) | - | 3 |
| auditory scene | `trm_4a3fd79d09abe` | Perception | - | - |
| auditory scene analysis | `trm_4a3fd79d09aca` | (none) | - | 1 |
| auditory sentence comprehension | `trm_4a3fd79d09ad5` | Language | - | 1 |
| auditory sentence recognition | `trm_558c7b14c076e` | (none) | 2 | 3 |
| auditory stream segregation | `trm_4a3fd79d09ae1` | Perception | - | 2 |
| auditory tone detection | `trm_557b474e2b578` | Perception | 2 | 3 |
| auditory tone perception | `trm_55ef273a77a86` | Perception | 1 | 1 |
| auditory word comprehension | `trm_4a3fd79d09aed` | Language | - | 3 |
| auditory word recognition | `trm_4a3fd79d09af8` | Language | 1 | 3 |
| auditory working memory | `trm_4a3fd79d09b04` | Learning and Memory | 4 | 3 |
| Autobiographical memory | `trm_wayqiZz3nFop1` | (none) | - | - |
| autobiographical recall | `trm_4a3fd79d09b1c` | (none) | 1 | 3 |
| automaticity | `trm_4a3fd79d09b28` | Learning and Memory | 2 | - |
| autonoesis | `trm_4ff1fc04e22e8` | (none) | 2 | 3 |
| availability heuristic | `trm_4a3fd79d09b33` | Reasoning and Decision Making | - | 1 |
| aversive learning | `trm_4a3fd79d09b3f` | Learning and Memory | - | 1 |
| aversive salience | `trm_om88i12KUeI1R` | (none) | - | 3 |
| Awareness | `trm_0eeP5Xfft6ofk` | (none) | 1 | - |
| backward chaining | `trm_4a3fd79d09b62` | Reasoning and Decision Making | - | - |
| balance | `trm_50eb56a7867db` | (none) | 2 | 1 |
| beat perception | `trm_7s8F8orjDstDt` | (none) | - | 1 |
| Behavioral Approach System | `trm_QlrVatUMhmg3s` | (none) | 1 | - |
| behavioral inhibition | `trm_4a3fd79d09b79` | (none) | 1 | 2 |
| behavioral inhibition (cognitive) | `trm_4b7c270940f9d` | Executive/Cognitive Control | 2 | 3 |
| behavioral inhibition (temperament) | `trm_4b7c27094a093` | (none) | - | - |
| Behavioral Inibition System | `trm_v97yWIWghz10Z` | (none) | 1 | - |
| belief | `trm_4a3fd79d09b85` | (none) | - | - |
| binocular convergence | `trm_4a3fd79d09b9c` | Perception | - | 1 |
| binocular depth cue | `trm_4fea04a02ce37` | (none) | - | 4 |
| binocular disparity | `trm_4a3fd79d09bb3` | Perception | - | 1 |
| binocular rivalry | `trm_500d8626d0770` | (none) | - | 2 |
| binocular vision | `trm_4a3fd79d09bbf` | Perception | 1 | 1 |
| bitterness | `trm_4a3fd79d09bcb` | Perception | - | - |
| blindsight | `trm_5029515e29f7f` | (none) | - | 2 |
| body maintenance | `trm_557b477b4a15f` | Learning and Memory | 1 | 1 |
| body orientation | `trm_4a3fd79d09be2` | (none) | 1 | 2 |
| body representation | `trm_4e5505361f160` | (none) | - | 3 |
| border ownership | `trm_502ab8dd991bf` | (none) | 1 | 3 |
| capacity limitation | `trm_4a3fd79d09bee` | Attention | 1 | 1 |
| cardinal orientation | `trm_lwnmyixYF0bNn` | (none) | - | 2 |
| cardinal-direction judgment | `trm_M4nBW4V1iS71l` | (none) | - | 5 |
| case based reasoning | `trm_4a3fd79d09bf9` | Reasoning and Decision Making | - | - |
| categorical clustering | `trm_4a3fd79d09c05` | Learning and Memory | - | - |
| categorical knowledge | `trm_4a3fd79d09c11` | Reasoning and Decision Making | - | 1 |
| categorical perception | `trm_4a3fd79d09c1c` | Perception | - | 4 |
| category based induction | `trm_4a3fd79d09c34` | Reasoning and Decision Making | - | - |
| category learning | `trm_4a3fd79d09c3f` | Learning and Memory | 1 | - |
| causal inference | `trm_4a3fd79d09c5b` | Reasoning and Decision Making | 1 | 1 |
| central attention | `trm_4a3fd79d09c69` | Attention | - | - |
| central coherence | `trm_4b82c75498408` | (none) | 4 | - |
| central executive | `trm_4a3fd79d0ba25` | Executive/Cognitive Control | 1 | 2 |
| central fixation | `trm_Ilz9RmdieE56K` | (none) | - | - |
| centration | `trm_4a3fd79d09c74` | (none) | - | - |
| change blindness | `trm_4fea238758d33` | (none) | - | 1 |
| chemonociception | `trm_4a3fd79d09c80` | Perception | - | - |
| chromatic contrast | `trm_4a3fd79d09c97` | Perception | - | - |
| Chronesthesia | `trm_59cd0184eb2bf` | (none) | - | - |
| chunk | `trm_4a3fd79d09ca3` | Learning and Memory | - | - |
| circadian rhythm | `trm_5159c382bd8d4` | (none) | - | - |
| Coercion | `trm_H5TZwxrcaUSBI` | (none) | 2 | - |
| cognitive control | `trm_4aae62e4ad209` | Executive/Cognitive Control | 27 | 15 |
| cognitive development | `trm_4a3fd79d09d35` | (none) | 6 | 1 |
| cognitive dissonance | `trm_4a3fd79d09d41` | (none) | - | - |
| cognitive distance | `trm_IatczRR1NRCb2` | (none) | - | 2 |
| cognitive effort | `trm_4a3fd79d09d4d` | (none) | 1 | 2 |
| cognitive heuristic | `trm_4a3fd79d09d58` | Reasoning and Decision Making | - | 2 |
| cognitive load | `trm_4a3fd79d09d64` | Executive/Cognitive Control | 4 | - |
| cognitive map | `trm_4a3fd79d09d70` | (none) | - | - |
| cognitive training | `trm_51a6905a3f021` | (none) | - | - |
| Cognitive warfare | `trm_7J8bZcxhab2mR` | (none) | - | - |
| Cognitive warfare | `trm_cz5r7bGDpqiwn` | (none) | - | - |
| color constancy | `trm_4fea09fac5316` | (none) | - | - |
| color perception | `trm_4a3fd79d09d93` | Perception | 2 | 3 |
| color recognition | `trm_557b478ce1c24` | Perception | 1 | 2 |
| combinatorial semantics | `trm_6BXoIuFvTg9zF` | (none) | - | 1 |
| communication | `trm_4a3fd79d09d9e` | Social Function | 8 | - |
| concept | `trm_4a3fd79d09db6` | (none) | - | - |
| concept learning | `trm_4a3fd79d09dc1` | Learning and Memory | - | - |
| conceptual category | `trm_4a3fd79d09dcd` | Learning and Memory | - | - |
| conceptual coherence | `trm_4a3fd79d09dd9` | (none) | - | - |
| conceptual combination | `trm_sqBGK5gOFZflZ` | (none) | - | - |
| conceptual metaphor | `trm_4d920c905d465` | (none) | - | - |
| conceptual planning | `trm_4a3fd79d09de4` | Language | 1 | 1 |
| conceptual priming | `trm_5521a2aa5b127` | (none) | - | 1 |
| conceptual skill | `trm_4a3fd79d09df0` | (none) | 1 | - |
| conceptualization | `trm_4a3fd79d09dfc` | (none) | - | - |
| conditional reasoning | `trm_4a3fd79d09e07` | Reasoning and Decision Making | 2 | 1 |
| conduct disorder | `trm_523e00f356226` | (none) | 2 | - |
| cone of confusion | `trm_500d8839c2877` | (none) | - | - |
| confidence judgment | `trm_55ef153d47bc0` | Reasoning and Decision Making | 1 | 2 |
| conflict adaptation effect | `trm_5358ede949107` | (none) | 1 | - |
| conflict detection | `trm_4a3fd79d09e13` | Perception | 4 | 1 |
| conjunction search | `trm_4a3fd79d09e1e` | Attention | 1 | 1 |
| connotation | `trm_4a3fd79d09e2a` | Language | - | - |
| constancy | `trm_4a3fd79d09e58` | (none) | - | - |
| constituent structure | `trm_4a3fd79d09e64` | (none) | - | - |
| context | `trm_4a3fd79d09e6f` | (none) | - | 1 |
| context dependent | `trm_4a3fd79d09e7b` | Learning and Memory | - | - |
| context memory | `trm_4a3fd79d09e87` | Learning and Memory | 2 | 2 |
| context representation | `trm_56798c5f25b0c` | Reasoning and Decision Making | 2 | 4 |
| contextual knowledge | `trm_4a3fd79d09e93` | (none) | - | - |
| contingency learning | `trm_4a3fd79d09e9e` | Learning and Memory | 1 | 1 |
| contrastive stress | `trm_4a3fd79d09eaa` | (none) | - | - |
| conventionality | `trm_4a3fd79d09eb6` | (none) | 1 | - |
| convergent thinking | `trm_4a3fd79d09ece` | (none) | 1 | - |
| conversation | `trm_4a3fd79d09eda` | Language | - | - |
| conversational skill | `trm_4a3fd79d09ee6` | Social Function | 1 | - |
| conversational speech | `trm_4a3fd79d09ef0` | Language | 1 | - |
| conversational structure | `trm_4a3fd79d09efb` | Language | - | - |
| coordination | `trm_4a3fd79d09f07` | (none) | - | - |
| Coping | `trm_hwkommxKgvKas` | (none) | 1 | - |
| coproduction | `trm_4a3fd79d09f12` | (none) | - | - |
| coreference | `trm_4a3fd79d09f1e` | Language | - | - |
| covert attention | `trm_4feb3ffa1ab51` | (none) | - | 1 |
| creative cognition | `trm_4a3fd79d09f2a` | (none) | 1 | - |
| creative problem solving | `trm_4a3fd79d09f36` | Reasoning and Decision Making | - | - |
| creative thinking | `trm_4a3fd79d09f42` | (none) | - | - |
| critical period | `trm_4a3fd79d09f4d` | (none) | - | - |
| crossmodal | `trm_4e31d2241319f` | (none) | - | - |
| crosstalk | `trm_4a3fd79d09f59` | (none) | - | - |
| crowding | `trm_502c139d5ed78` | (none) | - | 1 |
| crystallized intelligence | `trm_4a3fd79d09f64` | Reasoning and Decision Making | 3 | - |
| cue dependent forgetting | `trm_4a3fd79d09f70` | Learning and Memory | - | 1 |
| cue validity | `trm_4a3fd79d09f7c` | Attention | - | - |
| cueing | `trm_4a3fd79d09f87` | (none) | 1 | - |
| curiosity | `trm_4f3bdeedcc99d` | Motivation | - | - |
| dative shift | `trm_4a3fd79d0a006` | Language | - | - |
| decay of activation | `trm_4a3fd79d0a021` | Learning and Memory | - | 1 |
| deception | `trm_4a3fd79d0a02c` | Social Function | 1 | - |
| decision | `trm_4a3fd79d0b61f` | Reasoning and Decision Making | 1 | 1 |
| decision certainty | `trm_557b47abe9a34` | Reasoning and Decision Making | 1 | 2 |
| decision uncertainty | `trm_56798223b43b8` | (none) | - | - |
| decision under uncertainty | `trm_567982752ff4a` | Reasoning and Decision Making | 1 | 2 |
| declarative knowledge | `trm_4a3fd79d0a044` | Learning and Memory | - | 2 |
| declarative rule | `trm_4a3fd79d0a05b` | Learning and Memory | - | 2 |
| deductive inference | `trm_4a3fd79d0a066` | Reasoning and Decision Making | - | 1 |
| deep processing | `trm_4a3fd79d0a07e` | Learning and Memory | - | - |
| deep structure | `trm_4a3fd79d0a08a` | Language | - | - |
| defensive aggression | `trm_5159c885a7314` | (none) | - | - |
| defiance | `trm_523e034f9e69a` | (none) | 6 | - |
| deliberation | `trm_4fa28299dbddd` | Reasoning and Decision Making | 1 | - |
| delusion | `trm_4fa3afaeef512` | (none) | 2 | - |
| Demand | `trm_f01v8jugwrqHl` | (none) | 1 | - |
| depth cue | `trm_4a3fd79d0a095` | Perception | - | - |
| desire | `trm_4a3fd79d0a0ad` | Motivation | - | - |
| detection | `trm_55ce70b20186b` | Perception | - | 9 |
| difference threshold | `trm_4fe9fae4321e7` | (none) | - | 1 |
| diphthong | `trm_4a3fd79d0a0dc` | Language | - | - |
| discourse | `trm_4a3fd79d0b6c5` | Language | - | - |
| discourse comprehension | `trm_4a3fd79d0b6d1` | Language | - | 1 |
| discourse knowledge | `trm_4a3fd79d0b6dd` | Language | - | 1 |
| discourse planning | `trm_4a3fd79d0b6e9` | Language | - | 1 |
| discourse production | `trm_4a3fd79d0b701` | Language | - | - |
| discrimination | `trm_5519b7525d7a2` | Perception | - | 5 |
| dispositions | `trm_4a3fd79d0a0e7` | (none) | - | - |
| distraction | `trm_4a3fd79d0a0f3` | Attention | 1 | - |
| distributed coding | `trm_4a3fd79d0a0ff` | Learning and Memory | - | - |
| divergent thinking | `trm_4a3fd79d0a10a` | Reasoning and Decision Making | - | - |
| domain specificity | `trm_5021684cba96c` | (none) | 1 | - |
| dominant percept | `trm_KmaWWKCuIjtXG` | (none) | - | 2 |
| dream | `trm_4a3fd79d0a12d` | (none) | - | - |
| Dyadic Effect | `trm_pNo3F5h7B8Eg7` | (none) | 1 | - |
| Dynamic Executive Attention System | `trm_KCHAUcNX8814Z` | (none) | - | - |
| dynamic visual perception | `trm_VeGoH5wNnyl4Q` | (none) | - | - |
| Dyslexia | `trm_55e1b08e5b06c` | (none) | - | - |
| east cardinal-direction judgment | `trm_TDGJs2KaQIyc8` | (none) | - | 1 |
| eating | `trm_525d8b8908809` | (none) | 2 | - |
| echoic memory | `trm_4b185801de7a1` | Learning and Memory | - | 1 |
| echolocation | `trm_4a3fd79d0b996` | Perception | - | - |
| economic value processing | `trm_557b4817db34d` | (none) | 1 | 2 |
| edge detection | `trm_4a3fd79d0b9a1` | Perception | - | 1 |
| efficiency | `trm_4a3fd79d0a145` | (none) | - | - |
| effort valuation | `trm_5159c971bf444` | (none) | - | - |
| effortful processing | `trm_4a3fd79d0a15c` | (none) | 1 | - |
| egocentric | `trm_4a3fd79d0a168` | (none) | - | - |
| elaborative processing | `trm_4a3fd79d0a173` | (none) | - | - |
| elaborative rehearsal | `trm_4a3fd79d0b8d9` | Learning and Memory | 1 | - |
| embodied cognition | `trm_4f33e65d0daac` | (none) | - | 2 |
| emotion | `trm_4a3fd79d0a17f` | Emotion | 2 | 7 |
| emotion perception | `trm_4a3fd79d0b65a` | Emotion | 3 | - |
| emotional bonding | `trm_4a3fd79d0b671` | Social Function | - | - |
| emotional decision making | `trm_4a3fd79d0a18b` | Emotion | - | 1 |
| emotional enhancement | `trm_5679b0e9d8c20` | (none) | - | 2 |
| emotional expression | `trm_4a3fd79d0a196` | Emotion | 2 | 2 |
| emotional face recognition | `trm_557b482a7c62b` | Perception | 2 | 2 |
| emotional intelligence | `trm_4a3fd79d0a1a2` | Emotion | 1 | - |
| emotional memory | `trm_4a3fd79d0a1ae` | Learning and Memory | 2 | 2 |
| emotional mimicry | `trm_4a3fd79d0a1b9` | Emotion | - | - |
| emotional self-evaluation | `trm_557b4855a12b4` | (none) | 1 | 1 |
| emotional suppression | `trm_4a3fd79d0a1d1` | Emotion | 1 | 1 |
| empathy | `trm_4a3fd79d0b67d` | Emotion | 4 | 2 |
| enumeration | `trm_YYKKwXb10F0XQ` | (none) | - | - |
| episodic buffer | `trm_4a3fd79d0b8f0` | Learning and Memory | - | 1 |
| episodic future thinking | `trm_5a2852438fa35` | (none) | 1 | 5 |
| episodic intention | `trm_5a28604b01314` | (none) | - | 1 |
| episodic learning | `trm_4a3fd79d0a1e8` | Learning and Memory | - | - |
| episodic planning | `trm_5a2860fa6b59e` | (none) | - | 1 |
| episodic prediction | `trm_5a285482e89c2` | (none) | - | 1 |
| episodic simulation | `trm_5a285423171d9` | (none) | 1 | 1 |
| error signal | `trm_4a3fd79d0a218` | (none) | - | - |
| error trapping | `trm_4a3fd79d0a223` | (none) | - | - |
| excitation | `trm_4a3fd79d0a22f` | Emotion | 1 | - |
| exogenous attention | `trm_56006cb5a61ac` | (none) | - | 2 |
| expectancy | `trm_4ebfe9a465449` | Motivation | - | 1 |
| expertise | `trm_4a3fd79d0a25e` | Learning and Memory | - | - |
| explicit knowledge | `trm_4a3fd79d0a269` | (none) | - | 1 |
| explicit learning | `trm_4a3fd79d0a275` | Learning and Memory | - | 6 |
| explicit memory | `trm_4a3fd79d0a281` | Learning and Memory | 1 | 2 |
| externalizing | `trm_523ca883711cc` | (none) | 2 | - |
| extrinsic motivation | `trm_4a3fd79d0a28c` | Motivation | - | - |
| face maintenance | `trm_55c6f87595b39` | (none) | 1 | 1 |
| facial age recognition | `trm_5595bd6c61d78` | (none) | 1 | 1 |
| facial attractiveness recognition | `trm_5595bd89d77c6` | (none) | 1 | 2 |
| facial expression | `trm_4a3fd79d0a318` | Emotion | - | - |
| facial happiness recognition | `trm_5595bd2b92003` | (none) | 1 | 2 |
| facial recognition | `trm_5595bde6b2e95` | (none) | - | 6 |
| facial trustworthiness recognition | `trm_5595bda0c5dc3` | (none) | 1 | 2 |
| false memory | `trm_4a3fd79d0a323` | Learning and Memory | 1 | - |
| far spatial distance | `trm_yFJ2nfBcwqdpZ` | (none) | - | 1 |
| far temporal distance | `trm_nDqGvtJMseYIJ` | (none) | - | 1 |
| fatigue | `trm_52583e52d5e7a` | (none) | - | - |
| fear | `trm_4a3fd79d0b689` | Emotion | 6 | 2 |
| feature comparison | `trm_557b4891e9265` | Reasoning and Decision Making | 2 | 3 |
| feature detection | `trm_4a3fd79d0b9ad` | Perception | 1 | 6 |
| feature extraction | `trm_4a3fd79d0a32f` | Perception | - | 1 |
| feature integration | `trm_502954662d63e` | (none) | - | 1 |
| feature search | `trm_4fea18ec76bc9` | (none) | - | 1 |
| feedback processing | `trm_4a3fd79d0a33b` | (none) | 1 | 6 |
| figure ground reversal | `trm_4a3fd79d0b9d1` | Perception | - | - |
| figure ground segregation | `trm_4a3fd79d0b9dd` | Perception | 2 | 2 |
| filtering | `trm_4a3fd79d0a352` | (none) | - | - |
| fixation | `trm_4a3fd79d0a35e` | Attention | - | 1 |
| fixed action patterns | `trm_4a3fd79d0a36a` | (none) | - | - |
| flicker fusion threshold | `trm_mfw76CN2KbdFj` | (none) | - | - |
| fluid intelligence | `trm_4a3fd79d0a375` | Reasoning and Decision Making | 1 | 2 |
| focus | `trm_4a3fd79d0a381` | Attention | - | - |
| focused attention | `trm_4a3fd79d0a38d` | Attention | 1 | - |
| Food cue reactivity | `trm_BOD29Hs9qySTD` | (none) | 2 | - |
| form perception | `trm_4a3fd79d0a398` | Perception | 2 | 3 |
| framing | `trm_4a3fd79d0b636` | Reasoning and Decision Making | - | - |
| frustration | `trm_4a3fd79d0b695` | Emotion | 2 | - |
| functional fixedness | `trm_4a3fd79d0a3a4` | Reasoning and Decision Making | - | - |
| future time | `trm_XGQFZkDhrRRmm` | (none) | 5 | 1 |
| gaze | `trm_4a3fd79d0a3d2` | (none) | 2 | 1 |
| generalization | `trm_4a3fd79d0a3ea` | Learning and Memory | - | 1 |
| generic knowledge | `trm_4a3fd79d0a3f6` | Reasoning and Decision Making | 1 | - |
| gestalt | `trm_4a3fd79d0a402` | Perception | - | - |
| Gestalt grouping | `trm_4fb3f4d58aeb0` | (none) | 2 | 3 |
| global precedence | `trm_5021873f37abc` | (none) | 1 | - |
| goal | `trm_4a3fd79d0a419` | Executive/Cognitive Control | - | - |
| goal formation | `trm_4a3fd79d0a425` | Executive/Cognitive Control | - | - |
| goal management | `trm_4a3fd79d0a43c` | Executive/Cognitive Control | - | 1 |
| goal selection | `trm_5519b5f181edd` | (none) | - | 1 |
| goal state | `trm_4a3fd79d0a448` | Executive/Cognitive Control | - | - |
| grammatical encoding | `trm_4a3fd79d0b756` | Language | 2 | 1 |
| grapheme | `trm_4a3fd79d0b76e` | Language | - | - |
| graphemic buffer | `trm_4a3fd79d0b779` | Language | - | - |
| grief | `trm_4a3fd79d0b6a1` | Emotion | - | - |
| Grit | `trm_OogXjpJkhH7c3` | (none) | 1 | 2 |
| guilt | `trm_52583d9f2ad98` | (none) | 1 | - |
| gustation processing | `trm_4a3fd79d0b9e9` | Perception | 1 | 2 |
| gustatory learning | `trm_4a3fd79d0a460` | Learning and Memory | - | 2 |
| gustatory memory | `trm_4a3fd79d0a46b` | Learning and Memory | - | - |
| habit learning | `trm_4a3fd79d0a48e` | Learning and Memory | - | 1 |
| habit memory | `trm_4a3fd79d0a49a` | Learning and Memory | - | - |
| hallucination | `trm_4a3fd79d0a4a6` | (none) | - | - |
| happiness | `trm_4a3fd79d0b6ad` | Emotion | 3 | - |
| hedonism | `trm_4a3fd79d0a4b2` | (none) | - | - |
| heuristic search | `trm_4a3fd79d0a4be` | Reasoning and Decision Making | - | - |
| high energy density food recognition | `trm_55c298bbe56d5` | (none) | 2 | 2 |
| hill climbing | `trm_4a3fd79d0a4c9` | Reasoning and Decision Making | - | - |
| humiliation | `trm_4a3fd79d0a4e1` | Emotion | - | - |
| humor | `trm_4a3fd79d0a4ed` | Emotion | - | - |
| hyperactivity | `trm_523c7c13bc55f` | (none) | 6 | - |
| iconic memory | `trm_4a3fd79d0a4f9` | Learning and Memory | 3 | 1 |
| illocutionary force | `trm_4a3fd79d0b7b5` | Language | - | - |
| imageability | `trm_4a3fd79d0a504` | (none) | 1 | 1 |
| imagery | `trm_4a3fd79d0a510` | (none) | - | - |
| imagination | `trm_4f4511e519b53` | (none) | 4 | 3 |
| imagined emotional pain | `trm_AGb7jCLHtJ1sj` | (none) | - | 1 |
| imagined pain | `trm_LWGVPX20JubrD` | (none) | - | 2 |
| imagined physical pain | `trm_MIl7ueSc43aen` | (none) | - | 1 |
| implicit knowledge | `trm_4a3fd79d0a51c` | (none) | 1 | 1 |
| implicit learning | `trm_4a3fd79d0a527` | (none) | - | 1 |
| implicit learning | `trm_565bce2791089` | (none) | - | 7 |
| imprinting | `trm_4a3fd79d0a53f` | (none) | - | - |
| impulsivity | `trm_50070dce14554` | (none) | 17 | 1 |
| Inappropriate speech | `trm_523c7c886b614` | (none) | 1 | - |
| inattention | `trm_4a3fd79d0a54b` | Attention | 4 | 1 |
| inattentional blindness | `trm_4fe3861edc919` | (none) | 1 | 2 |
| incidental learning | `trm_4a3fd79d0a556` | Learning and Memory | - | 1 |
| incubation | `trm_4a3fd79d0a562` | Reasoning and Decision Making | - | - |
| indignation | `trm_4a3fd79d0a56e` | Emotion | - | - |
| induction | `trm_4a3fd79d0a579` | (none) | - | - |
| inference | `trm_4a3fd79d0a5ed` | Reasoning and Decision Making | - | 9 |
| inhibition | `trm_4a3fd79d0a613` | Executive/Cognitive Control | 5 | 4 |
| inhibition of return | `trm_4a3fd79d0a61f` | Executive/Cognitive Control | 2 | - |
| insomnia | `trm_ZwNxfQhvF1jVU` | (none) | - | - |
| instinct | `trm_4a3fd79d0a637` | (none) | 1 | - |
| instrumental learning | `trm_4a3fd79d0a64e` | Learning and Memory | 1 | - |
| integration | `trm_4a3fd79d0a65a` | (none) | - | - |
| intelligence | `trm_4a3fd79d0a666` | Reasoning and Decision Making | 6 | - |
| intention | `trm_4a3fd79d0a67d` | (none) | 1 | - |
| intentional learning | `trm_4a3fd79d0a695` | Learning and Memory | - | 1 |
| intentionality | `trm_4a3fd79d0a6a1` | (none) | - | - |
| interference | `trm_4a3fd79d0a6ad` | (none) | 1 | 1 |
| interference resolution | `trm_4c3e04d656f06` | Executive/Cognitive Control | 1 | 3 |
| intermediate-term memory | `trm_4a3fd79d0a6b9` | Learning and Memory | - | 1 |
| internal speech | `trm_4a3fd79d0a6c5` | Language | - | - |
| internalizing | `trm_523ca7e778c50` | (none) | 2 | - |
| interoception | `trm_4fe39e4388409` | (none) | 2 | 3 |
| interoceptive representation | `trm_4e5506161998c` | (none) | - | 2 |
| Interpersonal Conflict | `trm_30rzOgVoBsNqo` | (none) | 1 | - |
| interrogative | `trm_4a3fd79d0a6d0` | Language | - | - |
| intonation | `trm_4a3fd79d0a6dc` | Language | 1 | - |
| intrinsic motivation | `trm_4a3fd79d0a6e8` | Motivation | 1 | - |
| introspection | `trm_4a3fd79d0a6f4` | (none) | - | - |
| invariance | `trm_xJ2ikQmvjMzmI` | (none) | - | - |
| involuntary attention | `trm_4a3fd79d0a700` | Attention | 1 | - |
| irony | `trm_4a3fd79d0a70b` | (none) | - | - |
| irritability | `trm_523c7afe39f78` | (none) | 2 | - |
| kinaesthetic representation | `trm_4a3fd79d0a72e` | (none) | 2 | 2 |
| kindness priming | `trm_5521a6bc4db33` | (none) | - | 2 |
| kinesthesia | `trm_4a3fd79d0a73a` | Perception | - | 2 |
| knowledge | `trm_4a3fd79d0a746` | Learning and Memory | - | 9 |
| language | `trm_4a3fd79d0a769` | Language | 20 | 15 |
| language acquisition | `trm_4a3fd79d0b7f4` | Language | 2 | - |
| language learning | `trm_4a3fd79d0a781` | Language | 1 | 2 |
| language processing | `trm_4a3fd79d0b802` | Language | 6 | 5 |
| lateral masking | `trm_502bdc6bdaa2b` | (none) | 1 | 3 |
| left finger response execution | `trm_55b6b92c1fd76` | (none) | 1 | 1 |
| left hand response execution | `trm_558c7b707f606` | (none) | 1 | 1 |
| left toe response execution | `trm_55b6b96e77df6` | (none) | 1 | 1 |
| lemma | `trm_4a3fd79d0a7c7` | Language | - | - |
| lethargy | `trm_523c7ba79c2f1` | (none) | 2 | - |
| lexeme | `trm_502c343d20523` | (none) | - | 1 |
| lexical ambiguity | `trm_4a3fd79d0b81b` | Language | - | - |
| lexical encoding | `trm_4a3fd79d0a7d4` | Language | 2 | 1 |
| lexical processing | `trm_4a3fd79d0b826` | Language | 2 | 4 |
| lexical retrieval | `trm_4a3fd79d0a7e0` | Language | 2 | 2 |
| lexicon | `trm_4a3fd79d0a7ec` | Language | - | 3 |
| life satisfaction | `trm_50f3c0af04e37` | (none) | 1 | - |
| Limited Capacity | `trm_551f0f822d95e` | (none) | 11 | 1 |
| linguistic competence | `trm_4a3fd79d0a7f8` | Language | 2 | - |
| listening | `trm_4a3fd79d0a803` | (none) | 1 | 1 |
| localization | `trm_5521a0512df9a` | Perception | - | 4 |
| locomotion | `trm_50eb692db57eb` | (none) | 1 | 1 |
| logic | `trm_4a3fd79d0a80f` | Reasoning and Decision Making | 1 | - |
| logical reasoning | `trm_4a3fd79d0a81b` | Reasoning and Decision Making | 7 | 1 |
| loneliness | `trm_529d0d62290de` | (none) | 1 | - |
| long-term memory | `trm_4a3fd79d0a833` | Learning and Memory | 2 | 5 |
| loss | `trm_5159c80c1dd24` | (none) | 1 | 2 |
| loss anticipation | `trm_557b48a224b95` | (none) | 1 | 2 |
| loss aversion | `trm_4a3fd79d0a83f` | Reasoning and Decision Making | 1 | 2 |
| lying | `trm_4a3fd79d0a84a` | Social Function | - | - |
| maintenance | `trm_4a3fd79d0ba30` | Executive/Cognitive Control | 5 | 4 |
| Marital Conflict | `trm_s3yxeUMCHAo7j` | (none) | 1 | - |
| Mastery Orientation | `trm_LoNlAQafora4r` | (none) | 1 | - |
| meaning | `trm_4a3fd79d0a86e` | Language | 1 | - |
| mechanical reasoning | `trm_4a3fd79d0a87a` | Reasoning and Decision Making | - | 1 |
| melody | `trm_4a3fd79d0a886` | Perception | - | - |
| memory acquisition | `trm_4a3fd79d0b914` | Learning and Memory | - | - |
| memory consolidation | `trm_4a3fd79d0b920` | (none) | - | 2 |
| memory decay | `trm_4a3fd79d0b92c` | (none) | 2 | - |
| memory retrieval | `trm_4a3fd79d0ba01` | Learning and Memory | 4 | 3 |
| memory storage | `trm_4a3fd79d0b938` | Learning and Memory | 1 | 2 |
| memory trace | `trm_4a3fd79d0b943` | (none) | - | 1 |
| mental arithmetic | `trm_4a3fd79d0a8ed` | Reasoning and Decision Making | 1 | - |
| mental imagery | `trm_4a3fd79d0a8fc` | Perception | 1 | 1 |
| mental representation | `trm_4a3fd79d0a908` | (none) | 1 | 7 |
| mentalization | `trm_GefBol2cgYv34` | (none) | - | - |
| metacognitive skill | `trm_4a3fd79d0a92b` | Learning and Memory | - | 3 |
| metacomprehension | `trm_4d7fc763cf777` | (none) | - | - |
| metamemory | `trm_4a3fd79d0b94f` | Executive/Cognitive Control | - | 1 |
| metaphor | `trm_4a3fd79d0a937` | Language | - | - |
| meter | `trm_P4qxFaMb6wiZ1` | (none) | - | 1 |
| Mindfulness | `trm_wzUYYp7Av6Unt` | (none) | 2 | - |
| Mindset | `trm_o8gXkYlb58RBV` | (none) | - | 7 |
| misattribution | `trm_4a3fd79d0a943` | (none) | - | - |
| Monetary loss | `trm_aCwrPX04WLjIH` | (none) | - | 2 |
| mood | `trm_4a3fd79d0a95a` | Emotion | 6 | - |
| morphological processing | `trm_4a3fd79d0b832` | Language | 2 | - |
| morphology | `trm_4a3fd79d0b83e` | Language | - | - |
| motion aftereffect | `trm_4fea25630ffb5` | (none) | - | 1 |
| motion detection | `trm_557b48aeb7d58` | Perception | 1 | 1 |
| motivational salience | `trm_GfkAJLeHghfmp` | (none) | - | 3 |
| motor learning | `trm_4a3fd79d0a995` | Learning and Memory | 2 | - |
| Motor Praxis | `trm_56a2a4dbdf127` | (none) | - | - |
| motor program | `trm_4a3fd79d0a9ad` | Action | - | - |
| movement | `trm_4a3fd79d0a9c4` | Action | - | - |
| multisensory | `trm_4e31d3ba7d25b` | Perception | - | - |
| multisensory integration | `trm_4e31ced566649` | Perception | 1 | - |
| multistable perception | `trm_502abeab4e1d8` | (none) | 1 | 4 |
| music cognition | `trm_jK0qVisychW39` | (none) | - | 3 |
| music perception | `trm_yeQ7crXFocNza` | (none) | - | 7 |
| music semantics | `trm_utk2EAwtfI6x7` | (none) | - | 2 |
| music syntax | `trm_hsrxov4azQ6nM` | (none) | - | 3 |
| narrative | `trm_4a3fd79d0a9e8` | Language | - | - |
| narrative comprehension | `trm_55c6f58e77fbe` | (none) | 1 | 2 |
| Naturalistic Biological Motion | `trm_zECbJhkrvMYDQ` | (none) | - | - |
| Naturalistic Scenes | `trm_EibcrcPYJ86gd` | (none) | - | - |
| navigation | `trm_4a3fd79d0aa00` | Perception | - | - |
| near spatial distance | `trm_BscVyjZu0vFu1` | (none) | - | 2 |
| near temporal distance | `trm_w3kwvBmlVXDsm` | (none) | - | 1 |
| negative emotion | `trm_557b48d40d3cf` | Emotion | 2 | 3 |
| negative feedback processing | `trm_557b48e337218` | (none) | 3 | 2 |
| negative priming | `trm_5521a7a1376ed` | (none) | - | 1 |
| neologism | `trm_4d7fa2df05f23` | Language | - | - |
| neuroplasticity | `trm_51a690eeadcb7` | (none) | - | - |
| nociception | `trm_4a3fd79d0aa0c` | Perception | - | 3 |
| noesis | `trm_4ffdc96dc85b7` | (none) | - | 1 |
| noise sensitivity | `trm_525d8f3ed78a2` | (none) | 2 | - |
| nondeclarative knowledge | `trm_4a3fd79d0aa23` | (none) | - | - |
| nondeclarative memory | `trm_4a3fd79d0aa2f` | Learning and Memory | - | 2 |
| north cardinal-direction judgment | `trm_K5YMl5L5H2Xjj` | (none) | - | 1 |
| north-south orientation | `trm_0MvImupIHCn1e` | (none) | - | - |
| novelty detection | `trm_4a3fd79d0aa47` | (none) | 1 | 1 |
| numerical cognition | `trm_LDtOOxfCrEImf` | (none) | - | 2 |
| numerical comparison | `trm_5678a999f1c19` | Reasoning and Decision Making | 1 | 2 |
| numerical scale judgment | `trm_557b48f22ba99` | Reasoning and Decision Making | 2 | - |
| numerosity | `trm_Vn5ZVrIz7GedN` | (none) | - | 1 |
| object categorization | `trm_4a3fd79d0aa5e` | (none) | - | - |
| object centered representation | `trm_4a3fd79d0aa6a` | (none) | - | 2 |
| object detection | `trm_4a3fd79d0aa76` | Perception | - | 2 |
| object maintenance | `trm_557b4904ee26d` | Learning and Memory | 1 | 2 |
| object manipulation | `trm_4a3fd79d0aa8d` | Action | 1 | - |
| object perception | `trm_4a3fd79d0aaa4` | Perception | 2 | 2 |
| object recognition | `trm_4a3fd79d0aab0` | Perception | 2 | 5 |
| obsession | `trm_523e0419ec219` | (none) | 5 | 1 |
| oddball detection | `trm_557b491318742` | (none) | 4 | 4 |
| offensive aggression | `trm_5159c8a5d3d13` | (none) | 4 | - |
| olfaction | `trm_4a3fd79d0aabc` | Perception | - | 1 |
| openness | `trm_523f5f918cb2c` | (none) | 1 | - |
| optical illusion | `trm_4fb2c38960950` | (none) | - | 5 |
| orthographic lexicon | `trm_4a3fd79d0aad4` | Language | - | 1 |
| orthography | `trm_4a3fd79d0b84a` | Language | 1 | 1 |
| other-reference effect | `trm_BkEqTepYc5hbf` | (none) | - | 1 |
| overt attention | `trm_4feb3f8c551cb` | (none) | 2 | 1 |
| overt naming | `trm_558c74b165bb1` | (none) | - | 1 |
| pain | `trm_4b65259eeee34` | Emotion | 9 | 6 |
| pain habituation | `trm_4e6127bd91be9` | Emotion | 2 | 1 |
| pain sensitization | `trm_4e61264db33d4` | Emotion | 2 | 1 |
| paranoia | `trm_52405e33adafa` | (none) | 1 | - |
| paraphasia | `trm_4d7fa1a3e2a10` | Language | - | - |
| parsing | `trm_4a3fd79d0ab42` | Language | - | - |
| passive attention | `trm_4a3fd79d0ab4d` | Attention | - | 1 |
| past tense | `trm_4a3fd79d0ab59` | Language | - | 1 |
| past time | `trm_wTaB3Sl1dWvOW` | (none) | 1 | 1 |
| pattern maintenance | `trm_557b49206928b` | Learning and Memory | 1 | 1 |
| Pavlovian bias | `trm_MaWfLaH0xKHTK` | (none) | 1 | 4 |
| perceptual binding | `trm_4a3fd79d0ab88` | Perception | 1 | - |
| perceptual categorization | `trm_4a3fd79d0ab93` | Perception | - | - |
| perceptual fluency | `trm_4a3fd79d0ab9f` | Perception | - | - |
| perceptual identification | `trm_4a3fd79d0abaa` | Perception | 2 | 2 |
| perceptual learning | `trm_4a3fd79d0abb6` | Learning and Memory | 1 | 4 |
| perceptual priming | `trm_5519ba1746e95` | (none) | - | 3 |
| perceptual similarity | `trm_4a3fd79d0abc1` | Perception | 1 | - |
| perceptual skill | `trm_4a3fd79d0abcd` | Perception | - | - |
| perfectionism | `trm_525c58f9aabae` | (none) | 2 | - |
| performance monitoring | `trm_4a3fd79d0ac30` | Executive/Cognitive Control | 2 | 6 |
| phonation | `trm_4a3fd79d0ac4a` | Language | - | - |
| phonemic paraphasia | `trm_4d7fa1ee2f870` | Language | - | - |
| phonetics | `trm_4a3fd79d0b862` | Language | - | - |
| phonological assembly | `trm_558c74156b7ee` | (none) | 1 | 1 |
| phonological buffer | `trm_4a3fd79d0ac61` | Language | - | 1 |
| phonological code | `trm_4a3fd79d0ac7a` | (none) | - | - |
| phonological comparison | `trm_558c73b3663a6` | (none) | 1 | 3 |
| phonological loop | `trm_4a3fd79d0ba48` | Learning and Memory | 1 | 2 |
| phonological processing | `trm_52b5f1ef4f9cc` | (none) | - | 5 |
| phonological retrieval | `trm_4a3fd79d0ac93` | Language | 1 | 1 |
| phototransduction | `trm_5029751d118c4` | (none) | - | 1 |
| Physical Activity | `trm_t3L0j7X6p66JK` | (none) | 1 | - |
| pitch discrimination | `trm_p77NrG4CTxmPS` | (none) | - | 1 |
| place maintenance | `trm_557b493133416` | Learning and Memory | 1 | 1 |
| positive feedback processing | `trm_557b493e4203a` | (none) | 3 | 2 |
| positive priming | `trm_5521a3da10349` | (none) | - | 3 |
| potential monetary loss | `trm_557b494ca540d` | (none) | 1 | 3 |
| potential monetary reward | `trm_557b495cdde57` | (none) | 1 | 2 |
| pragmatic inference | `trm_4a3fd79d0ad12` | Reasoning and Decision Making | - | 1 |
| pragmatic knowledge | `trm_4a3fd79d0ad1d` | (none) | 1 | 1 |
| pragmatic reasoning | `trm_4a3fd79d0ad29` | Reasoning and Decision Making | - | 1 |
| preattentive processing | `trm_4a3fd79d0ad41` | Attention | 2 | - |
| preconscious perception | `trm_4a3fd79d0ad4c` | Perception | - | 1 |
| prejudice | `trm_4a3fd79d0ad64` | (none) | 1 | - |
| present time | `trm_dgZTWfjGK3RYq` | (none) | 1 | 1 |
| primary memory | `trm_4a3fd79d0ad94` | Learning and Memory | - | 1 |
| principle of cohesion | `trm_SbuNB0U1enr59` | (none) | - | - |
| problem solving | `trm_4a3fd79d0adb7` | Reasoning and Decision Making | 1 | 2 |
| procedural knowledge | `trm_4a3fd79d0adc3` | Learning and Memory | - | 1 |
| procedural learning | `trm_4a3fd79d0adcf` | Learning and Memory | - | 1 |
| procedural rule | `trm_4a3fd79d0ade8` | (none) | - | - |
| processing capacity | `trm_4a3fd79d0adf4` | (none) | 6 | 1 |
| processing speed | `trm_58575b0d3c548` | (none) | 3 | 1 |
| processing stage | `trm_4a3fd79d0ae00` | (none) | - | - |
| Production of non-facial communication | `trm_5154b23a3156a` | (none) | - | - |
| productive facial communication | `trm_5154aa9735134` | (none) | - | - |
| pronunciation | `trm_4a3fd79d0ae17` | Language | - | - |
| proper noun | `trm_4a3fd79d0ae2b` | Language | - | - |
| prosodic stress | `trm_4a3fd79d0ae58` | Language | - | - |
| prosody | `trm_4a3fd79d0ae64` | Language | - | - |
| prospection | `trm_5a285375c6a43` | (none) | - | 1 |
| prospective planning | `trm_4a3fd79d0ae7b` | (none) | 1 | 1 |
| prototype | `trm_4a3fd79d0ae87` | Learning and Memory | - | 1 |
| psychological refractory period | `trm_4ffca95528c88` | (none) | 2 | - |
| psychosis | `trm_52405de6b7a63` | (none) | 1 | - |
| punishment processing | `trm_5534111a8bc96` | (none) | 1 | 1 |
| quantitative skill | `trm_4a3fd79d0aeaa` | (none) | 2 | 1 |
| reception of facial communication | `trm_5154a9f45903f` | Social Function | - | - |
| Reception of non-facial communication | `trm_5154b049c279f` | (none) | - | - |
| regret | `trm_4a3fd79d0aecd` | Emotion | - | - |
| rehearsal loop | `trm_4a3fd79d0ba60` | Learning and Memory | - | 6 |
| reinstatement | `trm_502403240a2a2` | (none) | 1 | - |
| relational comparison | `trm_555cfb890d721` | (none) | 1 | 3 |
| relational learning | `trm_4a3fd79d0aed8` | Learning and Memory | - | 1 |
| remote memory | `trm_4a3fd79d0aee4` | Learning and Memory | - | 1 |
| repetition priming | `trm_5521a45a397a6` | (none) | - | 1 |
| repressed memory | `trm_4a3fd79d0aeef` | Learning and Memory | - | 1 |
| resistance to distractor inference | `trm_557b499fac085` | Executive/Cognitive Control | 3 | 1 |
| resource | `trm_4f3a72a028d90` | (none) | - | 1 |
| resource limit | `trm_4a3fd79d0af4c` | Executive/Cognitive Control | - | - |
| resource sharing | `trm_4a3fd79d0af5a` | Social Function | - | - |
| response alternatives | `trm_OMciWXS7bNM11` | (none) | - | - |
| response bias | `trm_559f0a129c136` | (none) | 1 | 2 |
| response priming | `trm_5521a663cd89c` | (none) | - | 1 |
| restricted behavior | `trm_52068e5bd9aa1` | (none) | 10 | - |
| retention | `trm_4a3fd79d0af7d` | Learning and Memory | 1 | 3 |
| retrieval cue | `trm_4a3fd79d0afa0` | Learning and Memory | 1 | - |
| reward learning | `trm_5159cb12a0f92` | (none) | 1 | 7 |
| rhythm | `trm_4a3fd79d0afc3` | Perception | 2 | 1 |
| right finger response execution | `trm_55b6b910b4b23` | (none) | 2 | 1 |
| right hand response execution | `trm_558c7b337080f` | (none) | 1 | 1 |
| right toe response execution | `trm_55b6b952c1b4c` | (none) | 1 | 1 |
| rigidity | `trm_523e0a4b443dc` | (none) | 1 | 1 |
| risk | `trm_4a3fd79d0afcf` | Reasoning and Decision Making | 3 | 1 |
| risk aversion | `trm_4a3fd79d0b642` | (none) | 4 | - |
| risk aversion | `trm_55ce71c47f37b` | (none) | - | 1 |
| Risk Perception | `trm_Ba49klQ9ApNSg` | (none) | 1 | - |
| risk seeking | `trm_4a3fd79d0b64e` | Reasoning and Decision Making | 10 | 1 |
| Risk Taking | `trm_4l7BDO8GJ3LdM` | (none) | 1 | - |
| route knowledge | `trm_4a3fd79d0afda` | (none) | - | 2 |
| routine | `trm_4a3fd79d0afe6` | (none) | - | - |
| rule | `trm_4a3fd79d0aff2` | (none) | - | - |
| rule learning | `trm_4a3fd79d0affd` | Learning and Memory | - | 3 |
| saccadic eye movement | `trm_aFgzEYVgvyimF` | (none) | - | 1 |
| sadness | `trm_4a3fd79d0b014` | Emotion | 8 | 2 |
| salience | `trm_4a3fd79d0b020` | (none) | - | 1 |
| schema | `trm_4a3fd79d0b02c` | Reasoning and Decision Making | - | 2 |
| search | `trm_4a3fd79d0b037` | Attention | - | 2 |
| selective control | `trm_557b4aa070c10` | Executive/Cognitive Control | 3 | 3 |
| self control | `trm_4ee8facd77dfc` | Executive/Cognitive Control | 6 | 3 |
| Self evaluation | `trm_jpDjcHLNr8Hko` | (none) | - | - |
| self knowledge | `trm_5154b39a3193d` | (none) | - | - |
| self talk | `trm_4f4672db34a46` | (none) | - | - |
| Self-Efficacy | `trm_Z1PwwmQJy6oB7` | (none) | 3 | - |
| semantic categorization | `trm_557b4ab076338` | (none) | 2 | 2 |
| semantic category | `trm_4a3fd79d0b06b` | Language | 1 | - |
| semantic information | `trm_4d2201d530697` | (none) | - | - |
| semantic network | `trm_51838baad343e` | Language | - | - |
| semantic priming | `trm_5521a51034353` | (none) | - | 1 |
| semantic working memory | `trm_4a3fd79d0b08f` | Executive/Cognitive Control | 3 | 1 |
| sense of ownership | `trm_4e5badf095692` | (none) | 1 | 2 |
| sensitivity to change | `trm_525d8e198e0da` | (none) | 1 | - |
| sensory defensiveness | `trm_525d8cd1c9cc3` | (none) | 1 | - |
| sensory memory | `trm_4a3fd79d0b09a` | Learning and Memory | - | 1 |
| sentence processing | `trm_4a3fd79d0b89e` | Language | 1 | 5 |
| sentence production | `trm_4a3fd79d0b8aa` | Language | - | - |
| sentence recognition | `trm_568427366401c` | (none) | - | 3 |
| sequence learning | `trm_4a3fd79d0b0a6` | Learning and Memory | 1 | 2 |
| serial learning | `trm_4a3fd79d0b0b1` | Learning and Memory | - | 1 |
| serial processing | `trm_4a3fd79d0b0bd` | (none) | 2 | - |
| serial search | `trm_4a3fd79d0b0c8` | Attention | 2 | 1 |
| shallow processing | `trm_4a3fd79d0b0df` | (none) | - | - |
| shame | `trm_4a3fd79d0b0eb` | Emotion | - | 1 |
| shape recognition | `trm_553967f006b70` | (none) | - | 1 |
| short-term memory | `trm_4a3fd79d0b0f7` | Learning and Memory | 1 | 2 |
| skepticism | `trm_4a3fd79d0b10e` | (none) | - | - |
| skill | `trm_4a3fd79d0b11a` | Learning and Memory | - | 1 |
| skill acquisition | `trm_4a3fd79d0b125` | Learning and Memory | - | 1 |
| sleep | `trm_5159c70d0e98e` | (none) | 3 | - |
| social cognition | `trm_4a3fd79d0b13d` | Social Function | 5 | 2 |
| social context | `trm_4a3fd79d0b148` | Social Function | 1 | - |
| social inference | `trm_5595be14a57c5` | Reasoning and Decision Making | - | 2 |
| social intelligence | `trm_4a3fd79d0b154` | Social Function | 9 | - |
| social motivation | `trm_52090251db8c8` | (none) | 9 | - |
| social norm processing | `trm_58c80b824c51b` | (none) | 1 | 1 |
| social phobia | `trm_523e053844495` | (none) | 2 | 1 |
| sound perception | `trm_586fd9dcd78e5` | (none) | - | 1 |
| source monitoring | `trm_4a3fd79d0b19b` | Learning and Memory | - | - |
| south cardinal-direction judgment | `trm_QNIy3cChBO4cA` | (none) | - | 1 |
| spatial ability | `trm_4a3fd79d0b1a6` | Perception | 13 | - |
| spatial cognition | `trm_4a3fd79d0b1bd` | (none) | 1 | - |
| spatial distance | `trm_6NJi93UzFFKBj` | (none) | - | 2 |
| spatial localization | `trm_5519bb7767d98` | (none) | - | 2 |
| spatial selective attention | `trm_557b4abe521af` | Attention | 1 | 2 |
| speech processing | `trm_4a3fd79d0b238` | Language | 1 | 2 |
| spontaneous recovery | `trm_5024002a85b1f` | Learning and Memory | 1 | 2 |
| spreading activation | `trm_4a3fd79d0b26d` | (none) | 1 | 2 |
| state consciousness | `trm_94lyXFzQH9ruD` | (none) | - | - |
| stereopsis | `trm_4a3fd79d0b279` | Perception | - | 2 |
| stereotypes | `trm_4a3fd79d0b285` | Social Function | - | - |
| stimulus detection | `trm_5519b80525e89` | Perception | - | 3 |
| strength | `trm_50eb5469ba37a` | (none) | 1 | 1 |
| stress | `trm_4a3fd79d0b2a8` | Emotion | 6 | - |
| string maintenance | `trm_557b4acdee820` | Learning and Memory | 1 | 1 |
| subconscious | `trm_4d21e9a7dd8ca` | (none) | - | 2 |
| subjective food value | `trm_559f09a5cdca9` | Reasoning and Decision Making | 3 | 2 |
| subjective value judgment | `trm_558c736199abd` | Reasoning and Decision Making | 1 | 6 |
| sublexical route | `trm_4a3fd79d0b2b4` | Language | 1 | 1 |
| subliminal perception | `trm_4a3fd79d0b2bf` | Perception | - | - |
| suicidal ideation | `trm_52583e8a46ded` | (none) | 1 | - |
| supervisory attentional system | `trm_4a3fd79d0b2fa` | Executive/Cognitive Control | - | - |
| Surface dyslexia | `trm_55e1b27f5655e` | (none) | - | - |
| surprise | `trm_4a3fd79d0b306` | Emotion | - | 1 |
| synchrony perception | `trm_4e31e6dca01ca` | Perception | 2 | 1 |
| syntactic processing | `trm_4a3fd79d0b34b` | Language | 1 | - |
| syntax | `trm_4a3fd79d0b357` | Language | 1 | 1 |
| tactile working memory | `trm_4e416f1373936` | Learning and Memory | - | 1 |
| task difficulty | `trm_557b4add1837e` | Motivation | 1 | 1 |
| task set | `trm_4c3e0646a2408` | Executive/Cognitive Control | 1 | - |
| task switching | `trm_4a3fd79d0b613` | Executive/Cognitive Control | 4 | 3 |
| taste aversion | `trm_4a3fd79d0b363` | Emotion | 1 | - |
| temporal categorization | `trm_MEjaEPF9qQveE` | (none) | - | 1 |
| temporal cognition | `trm_NLuhZFq5jY7Cq` | (none) | - | 5 |
| temporal depth | `trm_t4oxJAwl1xRzQ` | (none) | - | - |
| temporal discrimination | `trm_AU0Hu0wyHtKn4` | (none) | - | 1 |
| temporal distance | `trm_CN3u8GJWlTEUO` | (none) | - | 3 |
| test term | `trm_4a7b128b8b2d0` | (none) | - | - |
| text comprehension | `trm_4a3fd79d0b37a` | Language | 1 | 2 |
| text processing | `trm_4a3fd79d0b386` | Language | - | 2 |
| thermosensation | `trm_4a3fd79d0b39d` | Perception | 1 | 1 |
| Thirst | `trm_X4cTmFq0qpgRI` | (none) | - | - |
| thought | `trm_4fa295124a375` | (none) | - | - |
| time orientation | `trm_xMOwdL0Y58qYJ` | (none) | 3 | 4 |
| time perception | `trm_KcaEi0Mc9grrz` | (none) | - | 1 |
| tone recognition | `trm_55b6b8b8e7870` | (none) | - | 2 |
| tongue response execution | `trm_55b6b98b88f45` | (none) | 1 | 1 |
| tool maintenance | `trm_557b4aeaeb744` | Learning and Memory | 1 | 1 |
| top down processing | `trm_4a3fd79d0b3cb` | Executive/Cognitive Control | - | - |
| trait anxiety | `trm_50aff037c389f` | (none) | - | - |
| transduction | `trm_50297454e516b` | (none) | - | 1 |
| Transfer Data | `trm_KhnMZaVYVHe43` | (none) | - | - |
| transition | `trm_PbbDObBMoXj9X` | (none) | - | 2 |
| traumatic memory | `trm_4a3fd79d0b3ef` | Learning and Memory | - | 1 |
| trust | `trm_N7MLgAsJBIbiQ` | (none) | - | - |
| uncertainty | `trm_4a3fd79d0b3fa` | Reasoning and Decision Making | - | 2 |
| unconscious perception | `trm_4feb44e5ae25b` | (none) | 1 | 4 |
| unconscious process | `trm_4a3fd79d0b406` | Attention | - | 2 |
| understanding mental states | `trm_5159c0a633cda` | (none) | - | - |
| unisensory | `trm_4e31d365bc7e2` | Perception | - | - |
| updating | `trm_4c3e05903e4bb` | Executive/Cognitive Control | 9 | 3 |
| utility | `trm_4a3fd79d0b412` | Reasoning and Decision Making | - | - |
| valence | `trm_4a3fd79d0b429` | Emotion | 1 | - |
| vection | `trm_500d8aef38f2c` | (none) | - | 1 |
| Venturesomeness | `trm_2gvDOFhX4ILY3` | (none) | 1 | - |
| vestibular control | `trm_50f382d7abdff` | (none) | 2 | - |
| visual acuity | `trm_500d8bcf5f29a` | (none) | 2 | 1 |
| visual angle | `trm_500d8c8fcc520` | (none) | - | 1 |
| visual attention | `trm_4a3fd79d0b46f` | Attention | 5 | 2 |
| visual awareness | `trm_4ff36d79c26c6` | (none) | 3 | 2 |
| visual body recognition | `trm_557b4af7cc1cb` | (none) | 2 | 1 |
| visual buffer | `trm_4a3fd79d0b47b` | Perception | - | - |
| visual color discrimination | `trm_557b4b05ae470` | Perception | 2 | 2 |
| visual face recognition | `trm_557b4b154e0d9` | (none) | 1 | 3 |
| visual form discrimination | `trm_557b4b27dfd5e` | Perception | 1 | 3 |
| visual imagery | `trm_4a3fd79d0b487` | (none) | 2 | 1 |
| visual letter recognition | `trm_558c7439832d9` | (none) | 1 | 5 |
| visual localization | `trm_5519b92bde7dc` | Perception | - | 2 |
| visual memory | `trm_4a3fd79d0b49e` | Learning and Memory | 3 | 3 |
| visual number recognition | `trm_557b4b47d994a` | (none) | 4 | 2 |
| visual object detection | `trm_557b4b56de455` | (none) | 1 | 3 |
| visual object maintenance | `trm_559f0986182cc` | (none) | 1 | 1 |
| visual orientation | `trm_502ad54c11389` | (none) | 1 | 2 |
| visual pattern recognition | `trm_557b4b652cbec` | (none) | 3 | 2 |
| visual place recognition | `trm_557b4b7e68727` | Learning and Memory | 2 | 1 |
| visual pseudoword recognition | `trm_558c73f3c8c6f` | Language | 2 | 2 |
| visual recognition | `trm_557b4b7176394` | (none) | - | 9 |
| visual representation | `trm_4a3fd79d0b4c1` | Perception | - | 1 |
| visual scene perception | `trm_wrOXIUJWEWEYf` | (none) | - | 1 |
| visual search | `trm_4a3fd79d0b4cd` | Attention | 8 | 6 |
| visual sentence comprehension | `trm_ioHkrTU7owGjb` | (none) | - | 1 |
| visual sentence recognition | `trm_558c7b5228ed4` | (none) | 1 | 3 |
| visual shape recognition | `trm_5fjcydtc5dQY5` | (none) | - | 1 |
| visual string recognition | `trm_55ef1fd2bc418` | Language | 1 | 2 |
| visual tool recognition | `trm_557b4b8cd05ca` | (none) | 1 | 1 |
| visual word recognition | `trm_557b4b9ccdc4a` | Language | 11 | 5 |
| visuospatial sketch pad | `trm_4a3fd79d0b507` | Executive/Cognitive Control | 3 | 2 |
| vocal response execution | `trm_55ef3ba010121` | (none) | 2 | 2 |
| voice perception | `trm_586fda1743344` | (none) | - | 1 |
| west cardinal-direction judgment | `trm_OCCYobMYT2eky` | (none) | - | 1 |
| west-east orientation | `trm_izMVPVDOsJEkM` | (none) | - | 1 |
| wisdom | `trm_4a3fd79d0b530` | (none) | - | - |
| word comprehension | `trm_4a3fd79d0b548` | Language | - | 3 |
| word generation | `trm_4a3fd79d0b55f` | Language | - | 1 |
| word maintenance | `trm_557b4bb7cf05b` | Learning and Memory | 1 | 1 |
| word order | `trm_4a3fd79d0b56b` | Language | 1 | - |
| word pronunciation | `trm_4a3fd79d0b583` | Language | - | 2 |
| word repetition | `trm_4a3fd79d0b59b` | Language | 1 | - |
| working memory maintenance | `trm_55b6b9d7c9435` | Executive/Cognitive Control | 1 | 10 |
| working memory retrieval | `trm_4a3fd79d0ba6c` | Executive/Cognitive Control | 7 | 1 |
| working memory storage | `trm_4a3fd79d0ba77` | Executive/Cognitive Control | - | 1 |
| worldview | `trm_4f46753b8be4f` | (none) | - | - |
