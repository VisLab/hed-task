# Task mapping tables

Every correspondence between the 103 tasks in this catalog and the
857 task entries in the Cognitive Atlas, in both directions. The
[methodology](../methods/atlas_mapping/index.md) page explains what the match types mean
and how each row was decided.

The source of record is `.working/mappings/`, not this page.

Atlas entry names are reproduced exactly as the API returns them. A few carry a curly
apostrophe or an en dash, and one (`Penn` + a mis-encoded apostrophe + `s Logical
Reasoning Test`) carries a double-encoding defect present in the Atlas itself. These are
left uncorrected so that a name here matches the source byte for byte.

## Catalog to Atlas

One row per task in this catalog: 70 exact, 11 close, 4 related, 18 none.

| Task | Match | Atlas entry | Atlas ID | Definition chars | Concepts | Notes |
|---|---|---|---|---|---|---|
| [Affective Picture Viewing Task](../tasks/hedtsk_affective_picture_viewing.md) | `close` | International Affective Picture System | `tsk_4a57abb949aca` | 51 | 1 | Atlas entry is the IAPS stimulus database, not the viewing procedure |
| [Affective Priming Task](../tasks/hedtsk_affective_priming.md) | `none` | - | - | - | - | No affective or evaluative priming entry; Atlas has negative and semantic priming only |
| [Anti-Saccade Task](../tasks/hedtsk_anti_saccade.md) | `exact` | antisaccade/prosaccade task | `tsk_4a57abb949869` | 173 | 2 | - |
| [Artificial Grammar Learning Task](../tasks/hedtsk_artificial_grammar_learning.md) | `exact` | artificial grammar learning task | `trm_4f244a88013ae` | 246 | - | Atlas entry has zero concepts |
| [Attention Network Task](../tasks/hedtsk_attention_network.md) | `exact` | attention networks test | `trm_4da6304c9aa23` | 345 | 4 | Second entry ANT task trm_551f0857e1db8 duplicates this |
| [Auditory Masking Task](../tasks/hedtsk_auditory_masking.md) | `exact` | auditory masking task | `trm_551b1b6f6a262` | 102 | 1 | - |
| [Autobiographical Memory Task](../tasks/hedtsk_autobiographical_memory.md) | `exact` | autobiographical memory task | `trm_4f244d2a54e27` | 256 | 2 | - |
| [Balloon Analog Risk Task](../tasks/hedtsk_balloon_analog_risk.md) | `exact` | balloon analogue risk task | `trm_4d559bcd67c18` | 400 | 12 | Best-annotated Atlas task entry: 12 concepts |
| [Biological Motion Perception Task](../tasks/hedtsk_biological_motion_perception.md) | `exact` | biological motion task | `trm_4f245326e2eaf` | 150 | 1 | Canonical entry; trm_58a5d31f5c72d is a passive-viewing variant |
| [Body Ownership Illusion Task](../tasks/hedtsk_body_ownership_illusion.md) | `close` | rubber hand illusion | `trm_4e5bb14d814a8` | 403 | 2 | Atlas covers the rubber hand illusion only, not the wider family |
| [Cambridge Face Memory Task](../tasks/hedtsk_cambridge_face_memory.md) | `exact` | Cambridge Face Memory Test | `tsk_4a57abb949912` | 110 | 1 | - |
| [Causal Learning Task](../tasks/hedtsk_causal_learning.md) | `none` | - | - | - | - | No causal or contingency learning entry |
| [Change Detection Task](../tasks/hedtsk_change_detection.md) | `exact` | Change Detection Task | `trm_5154906cbead5` | 460 | 4 | - |
| [Contextual Cueing Task](../tasks/hedtsk_contextual_cueing.md) | `exact` | contextual cueing task | `trm_4f24492504ca0` | 287 | 2 | - |
| [Continuous Performance Task](../tasks/hedtsk_continuous_performance.md) | `exact` | Continuous Performance Task | `trm_57c0c34e61fdf` | 4 | - | Name-exact but a stub: 4-char definition, zero concepts; Penn CPT trm_4b4a537644d76 is better annotated |
| [Corsi Block-Tapping Task](../tasks/hedtsk_corsi_block_tapping.md) | `exact` | Corsi Blocks | `trm_4da881dace79c` | 1093 | - | Eponymous entry; block tapping test tsk_4a57abb9498df is the same paradigm |
| [Delay Discounting Task](../tasks/hedtsk_delay_discounting.md) | `exact` | temporal discounting task | `tsk_4a57abb949e98` | 123 | 6 | Atlas name is temporal discounting task, alias delay discounting |
| [Delayed Match-to-Sample Task](../tasks/hedtsk_delayed_match_to_sample.md) | `exact` | delayed match to sample task | `tsk_4a57abb9499e3` | 226 | 7 | - |
| [Dictator Game Task](../tasks/hedtsk_dictator_game.md) | `none` | - | - | - | - | Atlas has ultimatum, trust and prisoner's dilemma but no dictator game |
| [Digit Span Task](../tasks/hedtsk_digit_span.md) | `exact` | digit span task | `tsk_4a57abb949a0d` | 218 | 4 | Forward and backward variants exist as separate Atlas entries |
| [Digit Symbol Substitution Task](../tasks/hedtsk_digit_symbol_substitution.md) | `exact` | symbol-digit substitution | `tsk_4a57abb949e44` | 491 | - | Atlas name is symbol-digit substitution |
| [Directed Forgetting Task](../tasks/hedtsk_directed_forgetting.md) | `exact` | directed forgetting task | `trm_4da87f383435b` | 275 | 4 | - |
| [Dot-Probe Task](../tasks/hedtsk_dot_probe.md) | `close` | attention bias | `trm_50df0d8dc717b` | 217 | - | Atlas names the construct (attention bias) with dot-probe as an alias |
| [Effort-Based Decision-Making Task](../tasks/hedtsk_effort_based_decision_making.md) | `none` | - | - | - | - | No effort-based entry; value-based decision making is a different construct |
| [Emotion Regulation Task](../tasks/hedtsk_emotion_regulation.md) | `exact` | Emotion Regulation Task | `trm_56bbea82c12bb` | 510 | - | 510-char definition but zero concepts |
| [Emotional Stroop Task](../tasks/hedtsk_emotional_stroop.md) | `related` | Stroop task | `tsk_4a57abb949e27` | 176 | 4 | Atlas has eight Stroop entries but no emotional or affective Stroop |
| [Eriksen Flanker Task](../tasks/hedtsk_eriksen_flanker.md) | `exact` | Eriksen flanker task | `tsk_4a57abb949a4f` | 536 | 7 | - |
| [Face Processing Task](../tasks/hedtsk_face_processing.md) | `none` | - | - | - | - | Atlas has generic fMRI localizer entries but no face or FFA localizer |
| [Facial Emotion Recognition Task](../tasks/hedtsk_facial_emotion_recognition.md) | `close` | Emotion Recognition Task | `trm_50f734f86b11a` | 867 | 2 | Atlas Emotion Recognition Task is not Ekman-faces specific |
| [False Belief Task](../tasks/hedtsk_false_belief.md) | `exact` | false belief task | `trm_4f2456027809f` | 625 | 1 | Duplicated in the Atlas as trm_5845a809e30d5 |
| [Feeling-of-Knowing Task](../tasks/hedtsk_feeling_of_knowing.md) | `none` | - | - | - | - | No feeling-of-knowing entry |
| [Finger Tapping Task](../tasks/hedtsk_finger_tapping.md) | `exact` | finger tapping task | `trm_4c898f079d05e` | 70 | 3 | - |
| [Free Recall Task](../tasks/hedtsk_free_recall.md) | `close` | recall test | `trm_4f2411c91ae5e` | 83 | 1 | Atlas recall test is generic, not free recall specifically |
| [Go/No-Go Task](../tasks/hedtsk_go_no_go.md) | `exact` | go/no-go task | `tsk_4a57abb949a93` | 389 | 3 | - |
| [Heartbeat Detection Task](../tasks/hedtsk_heartbeat_detection.md) | `none` | - | - | - | - | No heartbeat detection entry; Atlas interoception entries are an fMRI task and a questionnaire |
| [Imitation-Inhibition Task](../tasks/hedtsk_imitation_inhibition.md) | `related` | action observation task | `tsk_4a57abb949846` | 72 | 1 | Atlas action observation task is not the imitation-compatibility paradigm |
| [Implicit Association Task](../tasks/hedtsk_implicit_association.md) | `exact` | Implicit Association Task | `trm_50b6660b1b847` | 596 | 3 | - |
| [Instrumental Conditioning Task](../tasks/hedtsk_instrumental_conditioning.md) | `exact` | instrumental learning task | `trm_4f2414059baa8` | 60 | - | operant task trm_50240f06af135 is an alias entry with more concepts |
| [Intentional Binding Task](../tasks/hedtsk_intentional_binding.md) | `related` | Interval Estimation Task | `tsk_YShVp2KOuWrSS` | 447 | - | Interval Estimation Task measures cue-to-outcome timing, not action-effect agency |
| [Iowa Gambling Task](../tasks/hedtsk_iowa_gambling.md) | `exact` | Iowa Gambling Task | `tsk_4a57abb949ae5` | 1005 | 2 | - |
| [Judgment-of-Learning Task](../tasks/hedtsk_judgment_of_learning.md) | `none` | - | - | - | - | No judgment-of-learning entry; Judgment of Line Orientation shares the JOL abbreviation only |
| [Lexical Decision Task](../tasks/hedtsk_lexical_decision.md) | `exact` | lexical decision task | `tsk_4a57abb949b38` | 459 | 2 | - |
| [Mental Rotation Task](../tasks/hedtsk_mental_rotation.md) | `exact` | mental rotation task | `trm_4c8990810541d` | 113 | 2 | - |
| [Mirror Tracing Task](../tasks/hedtsk_mirror_tracing.md) | `exact` | mirror tracing task | `trm_4f244a67d5b17` | 99 | - | - |
| [Mismatch Negativity Task](../tasks/hedtsk_mismatch_negativity.md) | `none` | - | - | - | - | No MMN entry despite its size in the ERP literature |
| [Mnemonic Similarity Task](../tasks/hedtsk_mnemonic_similarity.md) | `exact` | Mnemonic similarity task | `tsk_RXmB56vrYW66T` | 464 | - | Added to the Atlas after the 2025 harvest |
| [Monetary Incentive Delay Task](../tasks/hedtsk_monetary_incentive_delay.md) | `exact` | monetary incentive delay task | `trm_4f23fc8c42d28` | 137 | - | Zero concepts |
| [Motor Sequence Learning Task](../tasks/hedtsk_motor_sequence_learning.md) | `close` | sequence recall/learning | `trm_4c8a83cac75f5` | 137 | 2 | Atlas sequence recall/learning is broader than motor sequence learning |
| [Multi-Armed Bandit Task](../tasks/hedtsk_multi_armed_bandit.md) | `close` | Volatile Bandit | `trm_5696b180169bd` | 179 | - | Atlas has Volatile and contextual bandit variants but no canonical bandit entry |
| [Multiple Object Tracking Task](../tasks/hedtsk_multiple_object_tracking.md) | `none` | - | - | - | - | No MOT entry; visual pursuit/tracking is smooth pursuit, a different paradigm |
| [N-Back Task](../tasks/hedtsk_n_back.md) | `exact` | n-back task | `tsk_4a57abb949bcd` | 190 | 8 | Eight n-back variants exist as separate Atlas entries |
| [Navon Task](../tasks/hedtsk_navon.md) | `exact` | global-local task | `trm_4f241d7adf14e` | 173 | 4 | Atlas name is global-local task, alias Navon |
| [Oddball Task](../tasks/hedtsk_oddball.md) | `exact` | oddball task | `tsk_4a57abb949bf6` | 290 | 6 | - |
| [Old/New Recognition Memory Task](../tasks/hedtsk_old_new_recognition_memory.md) | `exact` | recognition memory test | `tsk_4a57abb949d40` | 2015 | 2 | - |
| [Operation Span Task](../tasks/hedtsk_operation_span.md) | `exact` | operation span task | `trm_4c40d10cd776e` | 273 | 2 | - |
| [Paired Associates Learning Task](../tasks/hedtsk_paired_associates_learning.md) | `exact` | paired associate learning | `trm_4da88a2a63d97` | 306 | 1 | - |
| [Pavlovian Fear Conditioning Task](../tasks/hedtsk_pavlovian_fear_conditioning.md) | `close` | pavlovian conditioning task | `trm_4c898acd1f28e` | 450 | 5 | Atlas entry is Pavlovian conditioning generally, not fear conditioning |
| [Phonological Awareness Task](../tasks/hedtsk_phonological_awareness.md) | `related` | rhyme verification task | `trm_4d949c5b0e380` | 146 | 6 | Rhyme verification is one component; no general phonological awareness entry |
| [Picture Naming Task](../tasks/hedtsk_picture_naming.md) | `exact` | picture naming task | `tsk_4a57abb949cfb` | 74 | 3 | - |
| [Posner Spatial Cueing Task](../tasks/hedtsk_posner_spatial_cueing.md) | `exact` | Posner cueing task | `tsk_4a57abb949d17` | 309 | 5 | - |
| [Prisoner's Dilemma Task](../tasks/hedtsk_prisoners_dilemma.md) | `exact` | prisoner's dilemma (PD) | `tsk_KRl3zbyaJcKWM` | 1366 | - | 1366-char definition but zero concepts |
| [Probabilistic Classification Learning Task](../tasks/hedtsk_probabilistic_classification_learning.md) | `exact` | Probabilistic classification task | `trm_4cacf22a22d80` | 386 | 9 | Three weather-prediction variants exist separately |
| [Probabilistic Selection Task](../tasks/hedtsk_probabilistic_selection.md) | `exact` | Probabilistic Selection Task | `trm_5667483dcc371` | 1316 | 1 | - |
| [Prospective Memory Task](../tasks/hedtsk_prospective_memory.md) | `exact` | prospective memory task | `trm_4f244860c702c` | 187 | - | Zero concepts |
| [Psychological Refractory Period Task](../tasks/hedtsk_psychological_refractory_period.md) | `exact` | psychological refractory period (PRP) paradigm | `trm_51c453f64d2a6` | 235 | 3 | - |
| [Psychomotor Vigilance Task](../tasks/hedtsk_psychomotor_vigilance.md) | `close` | PEBL Perceptual Vigilance Task | `trm_50b55d8a6da00` | 340 | 1 | Atlas entry is the PEBL software implementation, not the generic PVT |
| [Random Dot Kinematogram Task](../tasks/hedtsk_random_dot_kinematogram.md) | `exact` | dot motion task | `trm_4f244ad7dcde7` | 131 | 4 | - |
| [Rapid Serial Visual Presentation Task](../tasks/hedtsk_rapid_serial_visual_presentation.md) | `exact` | rapid serial visual presentation task | `tsk_4a57abb949879` | 203 | 3 | Attentional blink is a separate Atlas entry trm_551f06a08dcc4 |
| [Raven's Progressive Matrices Task](../tasks/hedtsk_ravens_progressive_matrices.md) | `exact` | Raven’s Progressive Matrices Test | `tsk_SJ4Q7gOYfy25Y` | 492 | 1 | Missed by the 2025 harvest, which dropped entries with non-ASCII names |
| [Reading the Mind in the Eyes Task](../tasks/hedtsk_reading_the_mind_in_the_eyes.md) | `none` | - | - | - | - | No RMET entry |
| [Remember/Know Task](../tasks/hedtsk_remember_know.md) | `exact` | remember/know task | `trm_4da63146f12d7` | 28 | - | 28-char definition, zero concepts |
| [Remote Associates Task](../tasks/hedtsk_remote_associates.md) | `exact` | Remote Associates Test | `tsk_ZMTNk4Oce5b2j` | 843 | - | 843-char definition but zero concepts |
| [Reversal Learning Task](../tasks/hedtsk_reversal_learning.md) | `exact` | reversal learning task | `tsk_4a57abb949d4e` | 337 | 2 | - |
| [Rey Auditory Verbal Learning Task](../tasks/hedtsk_rey_auditory_verbal_learning.md) | `exact` | Rey Auditory Verbal Learning Task | `trm_4da88ae0f2952` | 591 | 1 | - |
| [Self-Paced Reading Task](../tasks/hedtsk_self_paced_reading.md) | `none` | - | - | - | - | No self-paced or moving-window reading entry |
| [Self-Referential Encoding Task](../tasks/hedtsk_self_referential_encoding.md) | `none` | - | - | - | - | No self-referential encoding entry |
| [Semantic Priming Task](../tasks/hedtsk_semantic_priming.md) | `close` | contextual semantic priming task | `trm_553e73e29cf7d` | 1040 | 1 | Atlas entry is contextual semantic priming, a narrower paradigm |
| [Sentence Comprehension Task](../tasks/hedtsk_sentence_comprehension.md) | `none` | - | - | - | - | Atlas syntactic task is generic; Birkbeck test is a clinical instrument |
| [Serial Reaction Time Task](../tasks/hedtsk_serial_reaction_time.md) | `exact` | serial reaction time task | `trm_4f241c735e7f6` | 4 | 1 | Definition is absent, stored as the string None |
| [Simon Task](../tasks/hedtsk_simon.md) | `exact` | Simon task | `tsk_4a57abb949dbb` | 264 | 7 | - |
| [Social Incentive Delay Task](../tasks/hedtsk_social_incentive_delay.md) | `none` | - | - | - | - | Only the monetary version exists in the Atlas |
| [Source Memory Task](../tasks/hedtsk_source_memory.md) | `exact` | source memory test | `tsk_4a57abb949dd6` | 386 | 4 | - |
| [Sternberg Item Recognition Task](../tasks/hedtsk_sternberg_item_recognition.md) | `exact` | Sternberg Item Recognition Task | `trm_551f0a8b5ba2c` | 278 | 3 | Four Sternberg variants exist; none is marked canonical |
| [Stop-Signal Task](../tasks/hedtsk_stop_signal.md) | `exact` | stop signal task | `tsk_4a57abb949e1a` | 369 | 8 | Eight stop-signal entries exist |
| [Stroop Color-Word Task](../tasks/hedtsk_stroop_color_word.md) | `exact` | color-word stroop task | `trm_4b1968619b00b` | 269 | 2 | Generic Stroop task tsk_4a57abb949e27 also exists |
| [Sustained Attention to Response Task](../tasks/hedtsk_sustained_attention_to_response.md) | `exact` | sustained attention to response task | `trm_4da86cfe8cf1b` | 118 | 3 | - |
| [Task Switching Task](../tasks/hedtsk_task_switching.md) | `exact` | task-switching | `tsk_4a57abb949e8a` | 172 | 2 | Set-shifting and alternating-runs exist as separate entries |
| [Think/No-Think Task](../tasks/hedtsk_think_no_think.md) | `exact` | think/no-think task | `trm_54f93101b2fd8` | 131 | - | Zero concepts |
| [Tower of London Task](../tasks/hedtsk_tower_of_london.md) | `exact` | Tower of London | `trm_4da87e439c411` | 138 | 2 | - |
| [Trail Making Task](../tasks/hedtsk_trail_making.md) | `exact` | Trail Making Test A and B | `tsk_4a57abb949ec0` | 466 | 3 | - |
| [Trust Game Task](../tasks/hedtsk_trust_game.md) | `exact` | Trust game (TG) | `tsk_uzol7erTzr9Ix` | 1497 | - | 1497-char definition but zero concepts |
| [Two-Stage Decision Task](../tasks/hedtsk_two_stage_decision.md) | `exact` | 2-stage decision task | `trm_5667451917a34` | 778 | - | Duplicated as Two-Stage Task tsk_Jdo0KE737b9N8 |
| [Ultimatum Game Task](../tasks/hedtsk_ultimatum_game.md) | `exact` | Ultimatum Game (UG) | `trm_553e8882e3cb6` | 185 | - | Zero concepts |
| [Useful Field of View Task](../tasks/hedtsk_useful_field_of_view.md) | `none` | - | - | - | - | No UFOV entry |
| [Verb Generation Task](../tasks/hedtsk_verb_generation.md) | `exact` | verb generation task | `trm_4f24183fe80c6` | 82 | - | Zero concepts |
| [Verbal Fluency Task](../tasks/hedtsk_verbal_fluency.md) | `exact` | verbal fluency task | `trm_4f240f1c740da` | 48 | - | Six fluency entries exist: verbal, semantic, phonemic, category, letter, word |
| [Virtual Morris Water Maze Task](../tasks/hedtsk_virtual_morris_water_maze.md) | `close` | Morris water maze | `trm_4da890a9bd7a3` | 174 | 1 | Atlas entry is the animal Morris water maze, not the virtual human version |
| [Virtual Radial Arm Maze Task](../tasks/hedtsk_virtual_radial_arm_maze.md) | `none` | - | - | - | - | No radial arm maze entry; Atlas navigation entries are Morris, Porteus and zoo map |
| [Visual Masking Task](../tasks/hedtsk_visual_masking.md) | `exact` | backward masking | `trm_4a3fd79d09b6d` | 226 | 3 | Atlas name is backward masking |
| [Visual Search Task](../tasks/hedtsk_visual_search.md) | `exact` | visual search task | `trm_4f2447fe67fb9` | 4 | 3 | Definition is absent, stored as the string None |
| [Wason Selection Task](../tasks/hedtsk_wason_selection.md) | `exact` | Wason card selection task | `trm_4f2449bdcb0b1` | 99 | 2 | - |
| [Weapons Identification Task](../tasks/hedtsk_weapons_identification.md) | `none` | - | - | - | - | No weapons identification or shooter bias entry |
| [Wisconsin Card Sorting Task](../tasks/hedtsk_wisconsin_card_sorting.md) | `exact` | Wisconsin card sorting test | `tsk_4a57abb949f21` | 516 | 5 | - |

## Atlas to catalog, matched entries

183 Atlas entries correspond to something in this catalog, covering
88 of its 103 tasks. 17 of them resolve to a named variation
rather than to the task itself, which is how the Atlas's habit of registering each
implementation separately is absorbed.

| Atlas entry | Atlas ID | Match | Task | Variation | Notes |
|---|---|---|---|---|---|
| International Affective Picture System | `tsk_4a57abb949aca` | `close` | [Affective Picture Viewing Task](../tasks/hedtsk_affective_picture_viewing.md) | - | Primary match from hed_task_to_atlas.tsv |
| passive viewing | `trm_4c899211a965c` | `related` | [Affective Picture Viewing Task](../tasks/hedtsk_affective_picture_viewing.md) | - | Generic passive viewing, not affective specifically |
| antisaccade/prosaccade task | `tsk_4a57abb949869` | `exact` | [Anti-Saccade Task](../tasks/hedtsk_anti_saccade.md) | - | Primary match from hed_task_to_atlas.tsv |
| memory guided saccade task | `trm_4f2457d94fd93` | `exact` | [Anti-Saccade Task](../tasks/hedtsk_anti_saccade.md) | `hedvar_anti_saccade__memory_guided_anti_saccade` | - |
| visually guided saccade task | `trm_4f24108555294` | `close` | [Anti-Saccade Task](../tasks/hedtsk_anti_saccade.md) | `hedvar_anti_saccade__prosaccade_control_condition` | - |
| artificial grammar learning task | `trm_4f244a88013ae` | `exact` | [Artificial Grammar Learning Task](../tasks/hedtsk_artificial_grammar_learning.md) | - | Primary match from hed_task_to_atlas.tsv |
| ANT task | `trm_551f0857e1db8` | `exact` | [Attention Network Task](../tasks/hedtsk_attention_network.md) | - | Duplicate of trm_4da6304c9aa23 |
| attention networks test | `trm_4da6304c9aa23` | `exact` | [Attention Network Task](../tasks/hedtsk_attention_network.md) | - | Primary match from hed_task_to_atlas.tsv |
| auditory masking task | `trm_551b1b6f6a262` | `exact` | [Auditory Masking Task](../tasks/hedtsk_auditory_masking.md) | - | Primary match from hed_task_to_atlas.tsv |
| Tone Detection (JND) | `trm_5519c5f2ad56f` | `related` | [Auditory Masking Task](../tasks/hedtsk_auditory_masking.md) | - | Tone detection threshold |
| autobiographical memory task | `trm_4f244d2a54e27` | `exact` | [Autobiographical Memory Task](../tasks/hedtsk_autobiographical_memory.md) | - | Primary match from hed_task_to_atlas.tsv |
| balloon analogue risk task | `trm_4d559bcd67c18` | `exact` | [Balloon Analog Risk Task](../tasks/hedtsk_balloon_analog_risk.md) | - | Primary match from hed_task_to_atlas.tsv |
| biological motion task | `trm_4f245326e2eaf` | `exact` | [Biological Motion Perception Task](../tasks/hedtsk_biological_motion_perception.md) | - | Primary match from hed_task_to_atlas.tsv |
| Biological Motion Perception (Passive Viewing) Paradigm | `trm_58a5d31f5c72d` | `close` | [Biological Motion Perception Task](../tasks/hedtsk_biological_motion_perception.md) | - | Passive-viewing variant |
| gender discrimination task | `trm_4f241c8d4a75c` | `close` | [Biological Motion Perception Task](../tasks/hedtsk_biological_motion_perception.md) | `hedvar_biological_motion_perception__gender_identity_discrimination` | - |
| rubber hand illusion | `trm_4e5bb14d814a8` | `close` | [Body Ownership Illusion Task](../tasks/hedtsk_body_ownership_illusion.md) | - | Primary match from hed_task_to_atlas.tsv |
| Cambridge Face Memory Test | `tsk_4a57abb949912` | `exact` | [Cambridge Face Memory Task](../tasks/hedtsk_cambridge_face_memory.md) | - | Primary match from hed_task_to_atlas.tsv |
| Penn Face Memory Test | `trm_50f99e56117fe` | `close` | [Cambridge Face Memory Task](../tasks/hedtsk_cambridge_face_memory.md) | - | Penn face memory instrument |
| Change Detection Task | `trm_5154906cbead5` | `exact` | [Change Detection Task](../tasks/hedtsk_change_detection.md) | - | Primary match from hed_task_to_atlas.tsv |
| Regularity and Change Detection | `trm_5519c329eb334` | `related` | [Change Detection Task](../tasks/hedtsk_change_detection.md) | - | Regularity and change detection |
| contextual cueing task | `trm_4f24492504ca0` | `exact` | [Contextual Cueing Task](../tasks/hedtsk_contextual_cueing.md) | - | Primary match from hed_task_to_atlas.tsv |
| Continuous Performance Task | `trm_57c0c34e61fdf` | `exact` | [Continuous Performance Task](../tasks/hedtsk_continuous_performance.md) | - | Primary match from hed_task_to_atlas.tsv |
| Continuous Performance Test - AX version | `trm_551f0c294ce23` | `exact` | [Continuous Performance Task](../tasks/hedtsk_continuous_performance.md) | `hedvar_continuous_performance__ax_cpt_context_processing` | - |
| AX-DPX | `trm_515495b718cd6` | `close` | [Continuous Performance Task](../tasks/hedtsk_continuous_performance.md) | `hedvar_continuous_performance__ax_cpt_context_processing` | AX-DPX is a CPT variant, not a dot-probe task |
| Penn continuous performance task | `trm_4b4a537644d76` | `close` | [Continuous Performance Task](../tasks/hedtsk_continuous_performance.md) | - | Penn implementation |
| Corsi Blocks | `trm_4da881dace79c` | `exact` | [Corsi Block-Tapping Task](../tasks/hedtsk_corsi_block_tapping.md) | - | Primary match from hed_task_to_atlas.tsv |
| block tapping test | `tsk_4a57abb9498df` | `close` | [Corsi Block-Tapping Task](../tasks/hedtsk_corsi_block_tapping.md) | - | Same paradigm under a different name |
| spatial span test | `trm_4da86b539924c` | `close` | [Corsi Block-Tapping Task](../tasks/hedtsk_corsi_block_tapping.md) | - | Atlas spatial span test |
| Five-Trial Adjusting Delay Discounting Task | `tsk_qBdQueJHSouuF` | `exact` | [Delay Discounting Task](../tasks/hedtsk_delay_discounting.md) | `hedvar_delay_discounting__5_trial_adjusting_delay` | - |
| temporal discounting task | `tsk_4a57abb949e98` | `exact` | [Delay Discounting Task](../tasks/hedtsk_delay_discounting.md) | - | Primary match from hed_task_to_atlas.tsv |
| Delay Discounting Titration | `trm_566748c929afc` | `close` | [Delay Discounting Task](../tasks/hedtsk_delay_discounting.md) | - | Titration procedure |
| Kirby Delay Discounting Task | `trm_56bbee951f161` | `close` | [Delay Discounting Task](../tasks/hedtsk_delay_discounting.md) | - | Kirby monetary choice |
| delayed match to sample task | `tsk_4a57abb9499e3` | `exact` | [Delayed Match-to-Sample Task](../tasks/hedtsk_delayed_match_to_sample.md) | - | Primary match from hed_task_to_atlas.tsv |
| delayed nonmatch to sample task | `tsk_4a57abb9499f1` | `close` | [Delayed Match-to-Sample Task](../tasks/hedtsk_delayed_match_to_sample.md) | - | Non-match rule |
| match to sample visual search | `trm_50f852c084fde` | `related` | [Delayed Match-to-Sample Task](../tasks/hedtsk_delayed_match_to_sample.md) | - | Match-to-sample embedded in visual search |
| backward digit span task | `tsk_4a57abb94989b` | `exact` | [Digit Span Task](../tasks/hedtsk_digit_span.md) | `hedvar_digit_span__backward_digit_span` | - |
| digit span task | `tsk_4a57abb949a0d` | `exact` | [Digit Span Task](../tasks/hedtsk_digit_span.md) | - | Primary match from hed_task_to_atlas.tsv |
| forward digit span task | `tsk_4a57abb949a85` | `exact` | [Digit Span Task](../tasks/hedtsk_digit_span.md) | `hedvar_digit_span__forward_digit_span` | - |
| span/supra-span test | `tsk_4a57abb949de3` | `close` | [Digit Span Task](../tasks/hedtsk_digit_span.md) | `hedvar_digit_span__supra_span_lists` | - |
| WAIS Digit Span | `trm_5106eee90937a` | `close` | [Digit Span Task](../tasks/hedtsk_digit_span.md) | - | WAIS subtest form |
| symbol-digit substitution | `tsk_4a57abb949e44` | `exact` | [Digit Symbol Substitution Task](../tasks/hedtsk_digit_symbol_substitution.md) | - | Primary match from hed_task_to_atlas.tsv |
| digit/symbol coding test | `tsk_4a57abb949a25` | `close` | [Digit Symbol Substitution Task](../tasks/hedtsk_digit_symbol_substitution.md) | - | Digit/symbol coding |
| directed forgetting task | `trm_4da87f383435b` | `exact` | [Directed Forgetting Task](../tasks/hedtsk_directed_forgetting.md) | - | Primary match from hed_task_to_atlas.tsv |
| Sternberg Directed Forgetting | `trm_56674c7c2fa4f` | `close` | [Directed Forgetting Task](../tasks/hedtsk_directed_forgetting.md) | - | Sternberg directed forgetting |
| attention bias | `trm_50df0d8dc717b` | `close` | [Dot-Probe Task](../tasks/hedtsk_dot_probe.md) | - | Primary match from hed_task_to_atlas.tsv |
| Emotion Regulation Task | `trm_56bbea82c12bb` | `exact` | [Emotion Regulation Task](../tasks/hedtsk_emotion_regulation.md) | - | Primary match from hed_task_to_atlas.tsv |
| Stroop task | `tsk_4a57abb949e27` | `related` | [Emotional Stroop Task](../tasks/hedtsk_emotional_stroop.md) | - | Primary match from hed_task_to_atlas.tsv |
| Eriksen flanker task | `tsk_4a57abb949a4f` | `exact` | [Eriksen Flanker Task](../tasks/hedtsk_eriksen_flanker.md) | - | Primary match from hed_task_to_atlas.tsv |
| multi-source interference task | `trm_5696b61ff253e` | `related` | [Eriksen Flanker Task](../tasks/hedtsk_eriksen_flanker.md) | - | MSIT combines flanker, Simon and Stroop conflict; not a listed flanker variation |
| Emotion Recognition Task | `trm_50f734f86b11a` | `close` | [Facial Emotion Recognition Task](../tasks/hedtsk_facial_emotion_recognition.md) | - | Primary match from hed_task_to_atlas.tsv |
| facial expression of emotion | `tsk_4HuWbAQzF0tgZ` | `close` | [Facial Emotion Recognition Task](../tasks/hedtsk_facial_emotion_recognition.md) | - | Facial expression of emotion |
| Penn Emotion Recognition Task | `trm_56a2a6ce24586` | `close` | [Facial Emotion Recognition Task](../tasks/hedtsk_facial_emotion_recognition.md) | - | Penn implementation |
| false belief task | `trm_4f2456027809f` | `exact` | [False Belief Task](../tasks/hedtsk_false_belief.md) | - | Primary match from hed_task_to_atlas.tsv |
| False Belief task | `trm_5845a809e30d5` | `exact` | [False Belief Task](../tasks/hedtsk_false_belief.md) | - | Duplicate of trm_4f2456027809f |
| theory of mind task | `trm_4c8a8467304e2` | `close` | [False Belief Task](../tasks/hedtsk_false_belief.md) | - | Generic theory-of-mind entry |
| finger tapping task | `trm_4c898f079d05e` | `exact` | [Finger Tapping Task](../tasks/hedtsk_finger_tapping.md) | - | Primary match from hed_task_to_atlas.tsv |
| Continuous Tapping Task | `tsk_zaClbCwuCeWt2` | `close` | [Finger Tapping Task](../tasks/hedtsk_finger_tapping.md) | - | Continuous tapping |
| Tapping task | `trm_534692ef3b5df` | `close` | [Finger Tapping Task](../tasks/hedtsk_finger_tapping.md) | - | Generic tapping |
| delayed recall test | `tsk_4a57abb9499ff` | `close` | [Free Recall Task](../tasks/hedtsk_free_recall.md) | - | Delayed recall |
| episodic recall | `trm_4c898c8bf1b4f` | `close` | [Free Recall Task](../tasks/hedtsk_free_recall.md) | - | Episodic recall |
| immediate recall test | `tsk_4a57abb949abc` | `close` | [Free Recall Task](../tasks/hedtsk_free_recall.md) | - | Immediate recall |
| recall test | `trm_4f2411c91ae5e` | `close` | [Free Recall Task](../tasks/hedtsk_free_recall.md) | - | Primary match from hed_task_to_atlas.tsv |
| go/no-go task | `tsk_4a57abb949a93` | `exact` | [Go/No-Go Task](../tasks/hedtsk_go_no_go.md) | - | Primary match from hed_task_to_atlas.tsv |
| Go-No-Go Zoo Task | `tsk_k6MaDfNGbHqDx` | `close` | [Go/No-Go Task](../tasks/hedtsk_go_no_go.md) | - | Child version |
| motivational go/no-go learning task | `tsk_uzbPk1YB47Iqd` | `close` | [Go/No-Go Task](../tasks/hedtsk_go_no_go.md) | - | Adds reward motivation |
| action observation task | `tsk_4a57abb949846` | `related` | [Imitation-Inhibition Task](../tasks/hedtsk_imitation_inhibition.md) | - | Primary match from hed_task_to_atlas.tsv |
| Implicit Association Task | `trm_50b6660b1b847` | `exact` | [Implicit Association Task](../tasks/hedtsk_implicit_association.md) | - | Primary match from hed_task_to_atlas.tsv |
| instrumental learning task | `trm_4f2414059baa8` | `exact` | [Instrumental Conditioning Task](../tasks/hedtsk_instrumental_conditioning.md) | - | Primary match from hed_task_to_atlas.tsv |
| operant task | `trm_50240f06af135` | `exact` | [Instrumental Conditioning Task](../tasks/hedtsk_instrumental_conditioning.md) | - | Alias entry of trm_4f2414059baa8 |
| Interval Estimation Task | `tsk_YShVp2KOuWrSS` | `related` | [Intentional Binding Task](../tasks/hedtsk_intentional_binding.md) | - | Primary match from hed_task_to_atlas.tsv |
| Iowa Gambling Task | `tsk_4a57abb949ae5` | `exact` | [Iowa Gambling Task](../tasks/hedtsk_iowa_gambling.md) | - | Primary match from hed_task_to_atlas.tsv |
| gambling fMRI task paradigm | `trm_550b5c1a7f4db` | `related` | [Iowa Gambling Task](../tasks/hedtsk_iowa_gambling.md) | - | Generic gambling fMRI paradigm |
| gambling task | `trm_4f24496a80587` | `related` | [Iowa Gambling Task](../tasks/hedtsk_iowa_gambling.md) | - | Generic gambling task |
| lexical decision task | `tsk_4a57abb949b38` | `exact` | [Lexical Decision Task](../tasks/hedtsk_lexical_decision.md) | - | Primary match from hed_task_to_atlas.tsv |
| mental rotation task | `trm_4c8990810541d` | `exact` | [Mental Rotation Task](../tasks/hedtsk_mental_rotation.md) | - | Primary match from hed_task_to_atlas.tsv |
| mirror tracing task | `trm_4f244a67d5b17` | `exact` | [Mirror Tracing Task](../tasks/hedtsk_mirror_tracing.md) | - | Primary match from hed_task_to_atlas.tsv |
| Mnemonic similarity task | `tsk_RXmB56vrYW66T` | `exact` | [Mnemonic Similarity Task](../tasks/hedtsk_mnemonic_similarity.md) | - | Primary match from hed_task_to_atlas.tsv |
| monetary incentive delay task | `trm_4f23fc8c42d28` | `exact` | [Monetary Incentive Delay Task](../tasks/hedtsk_monetary_incentive_delay.md) | - | Primary match from hed_task_to_atlas.tsv |
| sequence recall/learning | `trm_4c8a83cac75f5` | `close` | [Motor Sequence Learning Task](../tasks/hedtsk_motor_sequence_learning.md) | - | Primary match from hed_task_to_atlas.tsv |
| Volatile Bandit | `trm_5696b180169bd` | `close` | [Multi-Armed Bandit Task](../tasks/hedtsk_multi_armed_bandit.md) | - | Primary match from hed_task_to_atlas.tsv |
| adaptive n-back task | `trm_56674133b666c` | `exact` | [N-Back Task](../tasks/hedtsk_n_back.md) | `hedvar_n_back__adaptive_n_back` | - |
| n-back task | `tsk_4a57abb949bcd` | `exact` | [N-Back Task](../tasks/hedtsk_n_back.md) | - | Primary match from hed_task_to_atlas.tsv |
| face n-back task | `tsk_4a57abb949a6a` | `close` | [N-Back Task](../tasks/hedtsk_n_back.md) | - | Face n-back; no matching HED variation |
| letter n-back task | `tsk_4a57abb949b1c` | `close` | [N-Back Task](../tasks/hedtsk_n_back.md) | `hedvar_n_back__verbal_n_back` | Letter n-back is the verbal form |
| global-local task | `trm_4f241d7adf14e` | `exact` | [Navon Task](../tasks/hedtsk_navon.md) | - | Primary match from hed_task_to_atlas.tsv |
| oddball task | `tsk_4a57abb949bf6` | `exact` | [Oddball Task](../tasks/hedtsk_oddball.md) | - | Primary match from hed_task_to_atlas.tsv |
| roving somatosensory oddball task | `trm_566db10532583` | `close` | [Oddball Task](../tasks/hedtsk_oddball.md) | - | Somatosensory roving oddball |
| P300 BCI | `tsk_GxjZBNiJorj1K` | `related` | [Oddball Task](../tasks/hedtsk_oddball.md) | - | P300 brain-computer interface |
| recognition memory test | `tsk_4a57abb949d40` | `exact` | [Old/New Recognition Memory Task](../tasks/hedtsk_old_new_recognition_memory.md) | - | Primary match from hed_task_to_atlas.tsv |
| Spatial Recognition Memory | `trm_50f733d7305a1` | `close` | [Old/New Recognition Memory Task](../tasks/hedtsk_old_new_recognition_memory.md) | - | Spatial recognition memory |
| operation span task | `trm_4c40d10cd776e` | `exact` | [Operation Span Task](../tasks/hedtsk_operation_span.md) | - | Primary match from hed_task_to_atlas.tsv |
| complex span test | `trm_4da86ad02b3ea` | `close` | [Operation Span Task](../tasks/hedtsk_operation_span.md) | - | Complex span, the family OSPAN belongs to |
| paired associate learning | `trm_4da88a2a63d97` | `exact` | [Paired Associates Learning Task](../tasks/hedtsk_paired_associates_learning.md) | - | Primary match from hed_task_to_atlas.tsv |
| paired associate recall | `trm_4c8991e6e8597` | `close` | [Paired Associates Learning Task](../tasks/hedtsk_paired_associates_learning.md) | - | Recall phase of PAL |
| pavlovian conditioning task | `trm_4c898acd1f28e` | `close` | [Pavlovian Fear Conditioning Task](../tasks/hedtsk_pavlovian_fear_conditioning.md) | - | Primary match from hed_task_to_atlas.tsv |
| phonological task | `trm_4f241b751c5a0` | `related` | [Phonological Awareness Task](../tasks/hedtsk_phonological_awareness.md) | - | Generic phonological task |
| rhyme verification task | `trm_4d949c5b0e380` | `related` | [Phonological Awareness Task](../tasks/hedtsk_phonological_awareness.md) | - | Primary match from hed_task_to_atlas.tsv |
| picture naming task | `tsk_4a57abb949cfb` | `exact` | [Picture Naming Task](../tasks/hedtsk_picture_naming.md) | - | Primary match from hed_task_to_atlas.tsv |
| naming (covert) | `trm_4c8990c87035d` | `close` | [Picture Naming Task](../tasks/hedtsk_picture_naming.md) | - | Covert naming |
| naming (overt) | `trm_4c8990e187dc7` | `close` | [Picture Naming Task](../tasks/hedtsk_picture_naming.md) | - | Overt naming |
| object naming task | `trm_4f2448d02d4d9` | `close` | [Picture Naming Task](../tasks/hedtsk_picture_naming.md) | - | Object naming |
| Naming tasks | `trm_552174863d51e` | `related` | [Picture Naming Task](../tasks/hedtsk_picture_naming.md) | - | Generic naming-task grouping |
| Posner cueing task | `tsk_4a57abb949d17` | `exact` | [Posner Spatial Cueing Task](../tasks/hedtsk_posner_spatial_cueing.md) | - | Primary match from hed_task_to_atlas.tsv |
| prisoner's dilemma (PD) | `tsk_KRl3zbyaJcKWM` | `exact` | [Prisoner's Dilemma Task](../tasks/hedtsk_prisoners_dilemma.md) | - | Primary match from hed_task_to_atlas.tsv |
| Probabilistic classification task | `trm_4cacf22a22d80` | `exact` | [Probabilistic Classification Learning Task](../tasks/hedtsk_probabilistic_classification_learning.md) | - | Primary match from hed_task_to_atlas.tsv |
| dual-task weather prediction | `trm_4ebc98cc77e7b` | `close` | [Probabilistic Classification Learning Task](../tasks/hedtsk_probabilistic_classification_learning.md) | - | Dual-task weather prediction |
| reversal weather prediction | `trm_5181fb7bf350b` | `close` | [Probabilistic Classification Learning Task](../tasks/hedtsk_probabilistic_classification_learning.md) | - | Reversal weather prediction |
| single-task weather prediction | `trm_4ebc728326a13` | `close` | [Probabilistic Classification Learning Task](../tasks/hedtsk_probabilistic_classification_learning.md) | - | Single-task weather prediction |
| Probabilistic Selection Task | `trm_5667483dcc371` | `exact` | [Probabilistic Selection Task](../tasks/hedtsk_probabilistic_selection.md) | - | Primary match from hed_task_to_atlas.tsv |
| prospective memory task | `trm_4f244860c702c` | `exact` | [Prospective Memory Task](../tasks/hedtsk_prospective_memory.md) | - | Primary match from hed_task_to_atlas.tsv |
| psychological refractory period (PRP) paradigm | `trm_51c453f64d2a6` | `exact` | [Psychological Refractory Period Task](../tasks/hedtsk_psychological_refractory_period.md) | - | Primary match from hed_task_to_atlas.tsv |
| PEBL Perceptual Vigilance Task | `trm_50b55d8a6da00` | `close` | [Psychomotor Vigilance Task](../tasks/hedtsk_psychomotor_vigilance.md) | - | Primary match from hed_task_to_atlas.tsv |
| vigilance | `trm_4da88a8e13f26` | `related` | [Psychomotor Vigilance Task](../tasks/hedtsk_psychomotor_vigilance.md) | - | Vigilance as a construct entry |
| dot motion task | `trm_4f244ad7dcde7` | `exact` | [Random Dot Kinematogram Task](../tasks/hedtsk_random_dot_kinematogram.md) | - | Primary match from hed_task_to_atlas.tsv |
| motion discrimination task | `trm_553fc63a54ae6` | `close` | [Random Dot Kinematogram Task](../tasks/hedtsk_random_dot_kinematogram.md) | `hedvar_random_dot_kinematogram__multi_alternative_motion_discrimination` | - |
| rapid serial visual presentation task | `tsk_4a57abb949879` | `exact` | [Rapid Serial Visual Presentation Task](../tasks/hedtsk_rapid_serial_visual_presentation.md) | - | Primary match from hed_task_to_atlas.tsv |
| attentional blink paradigm | `trm_551f06a08dcc4` | `close` | [Rapid Serial Visual Presentation Task](../tasks/hedtsk_rapid_serial_visual_presentation.md) | - | Attentional blink is an RSVP paradigm |
| target detection task | `trm_4f242499b8952` | `related` | [Rapid Serial Visual Presentation Task](../tasks/hedtsk_rapid_serial_visual_presentation.md) | - | Generic target detection |
| Raven’s Progressive Matrices Test | `tsk_SJ4Q7gOYfy25Y` | `exact` | [Raven's Progressive Matrices Task](../tasks/hedtsk_ravens_progressive_matrices.md) | - | Primary match from hed_task_to_atlas.tsv |
| Raven's Advanced Progressive Matrices | `trm_4f24211a03b07` | `close` | [Raven's Progressive Matrices Task](../tasks/hedtsk_ravens_progressive_matrices.md) | - | Advanced form; definition absent |
| remember/know task | `trm_4da63146f12d7` | `exact` | [Remember/Know Task](../tasks/hedtsk_remember_know.md) | - | Primary match from hed_task_to_atlas.tsv |
| Remote Associates Test | `tsk_ZMTNk4Oce5b2j` | `exact` | [Remote Associates Task](../tasks/hedtsk_remote_associates.md) | - | Primary match from hed_task_to_atlas.tsv |
| reversal learning task | `tsk_4a57abb949d4e` | `exact` | [Reversal Learning Task](../tasks/hedtsk_reversal_learning.md) | - | Primary match from hed_task_to_atlas.tsv |
| probabilistic reversal learning task | `trm_4da6318f7381b` | `close` | [Reversal Learning Task](../tasks/hedtsk_reversal_learning.md) | - | Probabilistic variant |
| Rey Auditory Verbal Learning Task | `trm_4da88ae0f2952` | `exact` | [Rey Auditory Verbal Learning Task](../tasks/hedtsk_rey_auditory_verbal_learning.md) | - | Primary match from hed_task_to_atlas.tsv |
| California Verbal Learning Test | `trm_4da6331cdeeb5` | `close` | [Rey Auditory Verbal Learning Task](../tasks/hedtsk_rey_auditory_verbal_learning.md) | - | CVLT, same word-list paradigm |
| California Verbal Learning Test-II | `tsk_4a57abb949900` | `close` | [Rey Auditory Verbal Learning Task](../tasks/hedtsk_rey_auditory_verbal_learning.md) | - | CVLT-II |
| Eye tracking paradigms | `trm_55217b48995ce` | `related` | [Self-Paced Reading Task](../tasks/hedtsk_self_paced_reading.md) | - | Eye-tracking reading methods |
| contextual semantic priming task | `trm_553e73e29cf7d` | `close` | [Semantic Priming Task](../tasks/hedtsk_semantic_priming.md) | - | Primary match from hed_task_to_atlas.tsv |
| semantic task | `trm_4f241b50caaf7` | `related` | [Semantic Priming Task](../tasks/hedtsk_semantic_priming.md) | - | Generic semantic task |
| syntactic task | `trm_4f244a453522b` | `related` | [Sentence Comprehension Task](../tasks/hedtsk_sentence_comprehension.md) | - | Generic syntactic task |
| serial reaction time task | `trm_4f241c735e7f6` | `exact` | [Serial Reaction Time Task](../tasks/hedtsk_serial_reaction_time.md) | - | Primary match from hed_task_to_atlas.tsv |
| choice reaction time task | `tsk_4a57abb949934` | `related` | [Serial Reaction Time Task](../tasks/hedtsk_serial_reaction_time.md) | - | Choice RT is a component, not the SRT paradigm |
| simple reaction time task | `tsk_4a57abb949dc8` | `related` | [Serial Reaction Time Task](../tasks/hedtsk_serial_reaction_time.md) | - | Simple RT is a component, not the SRT paradigm |
| Simon task | `tsk_4a57abb949dbb` | `exact` | [Simon Task](../tasks/hedtsk_simon.md) | - | Primary match from hed_task_to_atlas.tsv |
| source memory test | `tsk_4a57abb949dd6` | `exact` | [Source Memory Task](../tasks/hedtsk_source_memory.md) | - | Primary match from hed_task_to_atlas.tsv |
| Sternberg Item Recognition Task | `trm_551f0a8b5ba2c` | `exact` | [Sternberg Item Recognition Task](../tasks/hedtsk_sternberg_item_recognition.md) | - | Primary match from hed_task_to_atlas.tsv |
| Sternberg Recent Probes | `trm_56674987c8f0c` | `exact` | [Sternberg Item Recognition Task](../tasks/hedtsk_sternberg_item_recognition.md) | `hedvar_sternberg_item_recognition__recent_probes_sternberg` | - |
| item recognition task | `trm_4da869646e5d1` | `close` | [Sternberg Item Recognition Task](../tasks/hedtsk_sternberg_item_recognition.md) | - | Item recognition |
| Sternberg delayed recognition task | `tsk_4a57abb949e0c` | `close` | [Sternberg Item Recognition Task](../tasks/hedtsk_sternberg_item_recognition.md) | - | Delayed recognition form |
| stop signal task | `tsk_4a57abb949e1a` | `exact` | [Stop-Signal Task](../tasks/hedtsk_stop_signal.md) | - | Primary match from hed_task_to_atlas.tsv |
| conditional stop signal task | `trm_4cacf3fbc503b` | `close` | [Stop-Signal Task](../tasks/hedtsk_stop_signal.md) | - | Conditional variant |
| Motor Selective Stop Signal Task | `trm_56bbe45003cf7` | `close` | [Stop-Signal Task](../tasks/hedtsk_stop_signal.md) | - | Motor-selective variant |
| stimulus selective stop signal task | `trm_56a9123fe580f` | `close` | [Stop-Signal Task](../tasks/hedtsk_stop_signal.md) | - | Stimulus-selective variant |
| stop signal task with letter naming | `trm_5181f83b77fa4` | `close` | [Stop-Signal Task](../tasks/hedtsk_stop_signal.md) | - | Stop-signal with letter naming |
| stop signal walking task with stroop | `trm_553fcbbe974ba` | `close` | [Stop-Signal Task](../tasks/hedtsk_stop_signal.md) | - | Walking stop-signal with Stroop |
| color-word stroop task | `trm_4b1968619b00b` | `exact` | [Stroop Color-Word Task](../tasks/hedtsk_stroop_color_word.md) | - | Primary match from hed_task_to_atlas.tsv |
| counting Stroop task | `trm_4da631be60291` | `exact` | [Stroop Color-Word Task](../tasks/hedtsk_stroop_color_word.md) | `hedvar_stroop_color_word__counting_stroop` | - |
| chimeric animal Stroop task | `trm_4b843655d5d75` | `close` | [Stroop Color-Word Task](../tasks/hedtsk_stroop_color_word.md) | - | Chimeric animal Stroop |
| color-word stroop with task switching | `trm_5542841f3dcd5` | `close` | [Stroop Color-Word Task](../tasks/hedtsk_stroop_color_word.md) | - | Stroop with task switching |
| picture-word Stroop test | `trm_4dadbfd771a54` | `close` | [Stroop Color-Word Task](../tasks/hedtsk_stroop_color_word.md) | - | Picture-word Stroop |
| Stroop-like Arrows Task | `tsk_ZnDT4SbTZ2Bye` | `close` | [Stroop Color-Word Task](../tasks/hedtsk_stroop_color_word.md) | - | Arrow Stroop-like task |
| sustained attention to response task | `trm_4da86cfe8cf1b` | `exact` | [Sustained Attention to Response Task](../tasks/hedtsk_sustained_attention_to_response.md) | - | Primary match from hed_task_to_atlas.tsv |
| alternating runs paradigm | `trm_4da88b8b60ffb` | `exact` | [Task Switching Task](../tasks/hedtsk_task_switching.md) | `hedvar_task_switching__alternating_runs_aabb` | - |
| task-switching | `tsk_4a57abb949e8a` | `exact` | [Task Switching Task](../tasks/hedtsk_task_switching.md) | - | Primary match from hed_task_to_atlas.tsv |
| set-shifting task | `tsk_4a57abb949dad` | `close` | [Task Switching Task](../tasks/hedtsk_task_switching.md) | - | Set shifting |
| task switching (3x2) | `trm_566745bbf272a` | `close` | [Task Switching Task](../tasks/hedtsk_task_switching.md) | - | 3x2 design |
| attention switching task | `trm_4f241614d4a25` | `related` | [Task Switching Task](../tasks/hedtsk_task_switching.md) | - | Attention switching, a broader construct |
| think/no-think task | `trm_54f93101b2fd8` | `exact` | [Think/No-Think Task](../tasks/hedtsk_think_no_think.md) | - | Primary match from hed_task_to_atlas.tsv |
| Tower of London | `trm_4da87e439c411` | `exact` | [Tower of London Task](../tasks/hedtsk_tower_of_london.md) | - | Primary match from hed_task_to_atlas.tsv |
| Tower of London Imagine | `trm_5696bcf1b5c64` | `close` | [Tower of London Task](../tasks/hedtsk_tower_of_london.md) | - | Imagined-move variant |
| Tower of Hanoi | `trm_4da87e7282f92` | `related` | [Tower of London Task](../tasks/hedtsk_tower_of_london.md) | - | Tower of Hanoi, a sibling planning task |
| Trail Making Test A and B | `tsk_4a57abb949ec0` | `exact` | [Trail Making Task](../tasks/hedtsk_trail_making.md) | - | Primary match from hed_task_to_atlas.tsv |
| Trust game (TG) | `tsk_uzol7erTzr9Ix` | `exact` | [Trust Game Task](../tasks/hedtsk_trust_game.md) | - | Primary match from hed_task_to_atlas.tsv |
| 2-stage decision task | `trm_5667451917a34` | `exact` | [Two-Stage Decision Task](../tasks/hedtsk_two_stage_decision.md) | - | Primary match from hed_task_to_atlas.tsv |
| Two-Stage Task | `tsk_Jdo0KE737b9N8` | `exact` | [Two-Stage Decision Task](../tasks/hedtsk_two_stage_decision.md) | - | Duplicate of trm_5667451917a34 |
| Ultimatum Game (UG) | `trm_553e8882e3cb6` | `exact` | [Ultimatum Game Task](../tasks/hedtsk_ultimatum_game.md) | - | Primary match from hed_task_to_atlas.tsv |
| verb generation task | `trm_4f24183fe80c6` | `exact` | [Verb Generation Task](../tasks/hedtsk_verb_generation.md) | - | Primary match from hed_task_to_atlas.tsv |
| Covert verb generation task | `trm_5346927710e88` | `close` | [Verb Generation Task](../tasks/hedtsk_verb_generation.md) | - | Covert form |
| category fluency test | `tsk_4a57abb949923` | `exact` | [Verbal Fluency Task](../tasks/hedtsk_verbal_fluency.md) | `hedvar_verbal_fluency__semantic_category_fluency` | - |
| letter fluency test | `tsk_4a57abb949b0e` | `exact` | [Verbal Fluency Task](../tasks/hedtsk_verbal_fluency.md) | `hedvar_verbal_fluency__phonemic_letter_fluency_fas` | - |
| verbal fluency task | `trm_4f240f1c740da` | `exact` | [Verbal Fluency Task](../tasks/hedtsk_verbal_fluency.md) | - | Primary match from hed_task_to_atlas.tsv |
| phonemic fluency task | `trm_4f241be43458e` | `close` | [Verbal Fluency Task](../tasks/hedtsk_verbal_fluency.md) | `hedvar_verbal_fluency__phonemic_letter_fluency_fas` | - |
| semantic fluency task | `trm_4f241bd52b509` | `close` | [Verbal Fluency Task](../tasks/hedtsk_verbal_fluency.md) | `hedvar_verbal_fluency__semantic_category_fluency` | - |
| word fluency test | `trm_4da633dbb5817` | `close` | [Verbal Fluency Task](../tasks/hedtsk_verbal_fluency.md) | - | Word fluency |
| Morris water maze | `trm_4da890a9bd7a3` | `close` | [Virtual Morris Water Maze Task](../tasks/hedtsk_virtual_morris_water_maze.md) | - | Primary match from hed_task_to_atlas.tsv |
| Porteus maze test | `trm_4da87fdd7820e` | `related` | [Virtual Radial Arm Maze Task](../tasks/hedtsk_virtual_radial_arm_maze.md) | - | Porteus maze, a planning maze |
| backward masking | `trm_4a3fd79d09b6d` | `exact` | [Visual Masking Task](../tasks/hedtsk_visual_masking.md) | - | Primary match from hed_task_to_atlas.tsv |
| conjunction search task | `trm_4f24194bce29f` | `exact` | [Visual Search Task](../tasks/hedtsk_visual_search.md) | `hedvar_visual_search__conjunction_search` | - |
| visual search task | `trm_4f2447fe67fb9` | `exact` | [Visual Search Task](../tasks/hedtsk_visual_search.md) | - | Primary match from hed_task_to_atlas.tsv |
| Parallel/serial search | `trm_551b06cf9783b` | `close` | [Visual Search Task](../tasks/hedtsk_visual_search.md) | - | Parallel/serial search framing |
| Wason card selection task | `trm_4f2449bdcb0b1` | `exact` | [Wason Selection Task](../tasks/hedtsk_wason_selection.md) | - | Primary match from hed_task_to_atlas.tsv |
| Wisconsin card sorting test | `tsk_4a57abb949f21` | `exact` | [Wisconsin Card Sorting Task](../tasks/hedtsk_wisconsin_card_sorting.md) | - | Primary match from hed_task_to_atlas.tsv |

## Atlas to catalog, entries with no counterpart

The remaining 674 Atlas entries have no counterpart here. Most are not
experimental paradigms at all; the rest are paradigms this catalog does not cover. The
grouping below is derived from each entry's name by rule, so treat it as an aid to
navigation rather than a classification.

### Experimental paradigms not in the task catalog (481)

| Atlas entry | Atlas ID | Definition chars | Concepts |
|---|---|---|---|
| - | `trm_4f244f46ebf58` | 4 | 2 |
| 2nd-order rule acquisition | `trm_5667441c338a7` | 571 | - |
| abstract/concrete judgment: bilingual | `trm_4ebd44cd88360` | 152 | 5 |
| abstract/concrete task | `trm_4f24126c22011` | 71 | - |
| acquired equivalence | `trm_551f151f7347e` | 210 | 1 |
| action imitation task | `tsk_4a57abb94981d` | 343 | 3 |
| action-perception loop | `trm_551b15af981c6` | 4 | 2 |
| Adaptation of marshmellow test | `trm_56674e49d15e9` | 691 | - |
| adult attachment interview | `tsk_4a57abb949858` | 75 | - |
| ambiguous figure task | `trm_502abd109f255` | 128 | 3 |
| American National Adult Reading Test | `trm_5798fa39b4315` | 309 | 2 |
| analogical reasoning task | `trm_4f244f0286947` | 120 | 1 |
| Angling Risk Task | `trm_5667488d52ccc` | 761 | 2 |
| Angling Risk Task – Always Sunny | `tsk_zhAW4G31jTPrw` | 637 | 2 |
| animal naming task | `trm_4da88bd4412da` | 89 | 2 |
| apparent verticality judgment | `trm_502ad907e3299` | 107 | 2 |
| articulatory suppression task | `trm_50f5822624e53` | 117 | 1 |
| associative memory encoding task | `trm_553ec64e6cb1b` | 393 | 2 |
| Ataxia | `trm_56a2a8d78dd39` | 355 | 1 |
| attribute amnesia | `tsk_YrmQX6rtPeujt` | 223 | - |
| audio narrative | `trm_5550e5011ce10` | 303 | - |
| audio-visual target detection task | `tsk_4a57abb949889` | 226 | 4 |
| auditory scene perception | `trm_551b1460e89a3` | 80 | 1 |
| auditory temporal discrimination task | `trm_4f240e7f989f8` | 93 | 1 |
| autism diagnostic interview - revised | `trm_525d847e2bd0b` | 248 | 16 |
| autism diagnostic observation schedule | `trm_4da891a546d8c` | 214 | 6 |
| autism spectrum quotient | `trm_51d6fe3f3942f` | 1433 | 5 |
| AX-CPT task | `trm_4c40d2a93ea15` | 558 | 4 |
| Becker-Degroot-Marschak (BDM) procedure | `trm_553e77887abc7` | 282 | 1 |
| beery-buktenica developmental test of visual-motor integration | `trm_523f58d91f2c0` | 358 | 2 |
| behavioral approach/inhibition systems | `trm_56a9137d9dce1` | 419 | 4 |
| behavioral investment allocation strategy | `trm_4d54b8361e93e` | 330 | - |
| Benton facial recognition test | `tsk_4a57abb9498bc` | 53 | 1 |
| Bickel Titrator | `trm_5696a599bfcb6` | 266 | - |
| big/little circle | `trm_50f72fafa53ec` | 431 | 1 |
| bimanual coordination task | `trm_4f244f997615c` | 108 | 1 |
| Birkbeck Reversible Sentence Comprehension Test | `trm_579640ddba2c0` | 109 | 1 |
| Bistability | `trm_5519c4bb1d1ee` | 139 | 2 |
| Bistable percept paradigm | `trm_553fce5d21da7` | 285 | - |
| block design test | `trm_4b7497a289534` | 209 | 1 |
| Blocked channel-selection task | `trm_551f0757982bc` | 4 | 1 |
| body image self-reflection task | `trm_5879199fde201` | 454 | - |
| boston naming test | `tsk_4a57abb9498ef` | 214 | 2 |
| Boston Naming Test | `tsk_ovuQxhbAPPMLs` | 881 | - |
| braille reading task | `trm_4c898a20eb254` | 55 | 3 |
| breath-holding | `trm_4c898a680e424` | 92 | - |
| Brixton spatial anticipation test | `trm_4da88c5302e06` | 28 | - |
| Cambridge Gambling Task | `trm_4d54b2cc0f943` | 312 | 3 |
| Cambridge risk task | `trm_4f242042e5805` | 271 | 1 |
| CatBat task | `trm_4da88bff0507c` | 292 | 1 |
| categorization task | `trm_4f24112057e90` | 74 | 1 |
| CAToon (cognitive and affective Theory of Mind Cartoon Task) | `tsk_37y3EdRertJba` | 2016 | - |
| Cattell's Culture Fair Intelligence Test | `trm_4da86c6808ddd` | 190 | - |
| center of mass approximation | `tsk_iSDZtD6pTyB2c` | 225 | - |
| chewing/swallowing | `trm_4c898a8fd3afb` | 198 | 1 |
| Chicken Game task | `tsk_l7ApDPhpQkcmT` | 980 | - |
| choice task between risky and non-risky options | `trm_4d55a2bbcfdff` | 152 | 1 |
| classification probe without feedback | `trm_4ebc9d2e397f2` | 181 | 5 |
| Clinical Evaluation of Language Fundamentals-3 | `tsk_4a57abb9499a8` | 128 | 7 |
| clock drawing task | `trm_5798d2693915d` | 133 | 4 |
| Cognitive Reflection Test | `trm_56675359b663a` | 225 | 2 |
| coherent motion | `trm_551b0c616de16` | 4 | 1 |
| Coherent/Incoherent discourse distinction task | `trm_55217860a9dea` | 87 | 1 |
| color naming task | `trm_4f244c1f6b53f` | 4 | - |
| Color Trails Test | `trm_4da633fe917c4` | 254 | 2 |
| color-discrimination task | `tsk_4a57abb9499b8` | 229 | 1 |
| Columbia Card Task | `trm_5667492c555b7` | 670 | 3 |
| Communication and Symbolic Behavior Scales Development Profile | `trm_52718631bc934` | 193 | 8 |
| Compensatory Tracking Task | `tsk_eDRFWNl1ktVsf` | 348 | - |
| complex trait judgment task | `trm_553fd2fc7a648` | 461 | - |
| Comprehensive Test of Phonological Processing | `trm_526027c99b726` | 314 | 2 |
| Conners 3rd Edition | `trm_525c4cb94bfff` | 504 | 9 |
| Conners Comprehensive Behavior Rating Scales | `trm_524b563fb87c8` | 232 | 5 |
| consensus decision-making task | `trm_553fc858cacc5` | 520 | 1 |
| contextual bandit | `tsk_3ICXMd8R3ekcb` | 622 | - |
| continuous recognition paradigm | `tsk_4a57abb9499c7` | 525 | 3 |
| contour integration task | `trm_5519c85ed1e8d` | 142 | 1 |
| contour interpolation task | `trm_551b0bb59173d` | 105 | 1 |
| contrast detection task | `trm_502be67697201` | 115 | 2 |
| contrast sensitivity test | `trm_551efdcd10677` | 132 | 1 |
| Convex Time Budgets | `tsk_mUMzkG2xVn82g` | 505 | 2 |
| copying task | `trm_4fbd2ac1cd035` | 56 | - |
| Corpus analysis | `trm_5521752956bb2` | 51 | 1 |
| correlated bandits | `tsk_r8koF3we48jcA` | 502 | - |
| counterconditioning | `trm_50240427b4c1b` | 116 | 1 |
| Counting/Calculation | `trm_4c898b02722d2` | 94 | - |
| Couples Conflict Task | `tsk_zj7EaCdOZ1dae` | 618 | 1 |
| covert naming task | `trm_4f240d346320c` | 49 | - |
| criteria task | `trm_512e7621189ad` | 724 | - |
| cross modality | `trm_551b0e17c6c76` | 4 | 2 |
| cue approach task | `trm_553e77e53497d` | 463 | 1 |
| cue-based expectancy paradigm combining emotion regulation task | `tsk_9UB5vNDvAKzYw` | - | - |
| cue-based expectation task | `tsk_kQEU3vjgDNcJP` | 137 | - |
| cued explicit recognition | `trm_4c898b29660b0` | 200 | 2 |
| cups task | `tsk_4a57abb9499d5` | 402 | 3 |
| cyberball task | `trm_4f24189031a4a` | 153 | - |
| deception task | `trm_4c898b4b463aa` | 86 | 2 |
| deductive reasoning task | `trm_4c898b8c2d071` | 84 | 6 |
| delay conditioning | `trm_5023ef8eab626` | 262 | 1 |
| delayed intention task | `trm_5736095d91380` | 229 | 2 |
| delayed memory task | `trm_4fba85a597ca9` | 197 | 2 |
| delayed response task | `trm_4dadbdd0b2b8c` | 28 | - |
| deterministic classification | `trm_4e8dd3831f0cc` | 173 | 7 |
| Deviance Detection | `trm_5519c2d8d7b1d` | 55 | 1 |
| devil's task | `trm_4d559d2703bae` | 443 | 1 |
| dichotic listening task | `trm_4da87e9c79847` | 139 | 2 |
| Dietary Decisions Task | `trm_56674d6aa9faf` | 497 | 2 |
| Differential Ability Scales | `trm_5272806688e63` | 385 | 9 |
| digit cancellation task | `trm_4da89077f19ae` | 190 | 1 |
| Dimensions task | `trm_566747c3d757f` | 614 | - |
| Discourse content questions | `trm_55217a446eb3b` | 4 | 1 |
| Distraction paradigm (capture) | `trm_551f07a281283` | 1 | 1 |
| divided auditory attention | `trm_4c898bbab4fd4` | 212 | 3 |
| Donation task | `tsk_wmFvpdB0Y6UYl` | 73 | - |
| doors and people test | `tsk_4a57abb949a33` | 214 | 7 |
| DOSPERT | `trm_5696abecf2569` | 440 | 4 |
| dot pattern expectancy task | `trm_4da86c2a70a7d` | 280 | 4 |
| drawing | `trm_4c898be57fcbc` | 64 | 2 |
| drawing from memory task | `trm_4fbd2e5614028` | 95 | - |
| dual sensitization | `trm_4e5e7ac84c2e5` | 196 | 2 |
| dual-task paradigm | `trm_4da634216ebbc` | 45 | 3 |
| Early Development Interview (EDI) | `trm_5298ed1336e43` | 250 | 4 |
| Early Social and Communication Scales | `trm_4da8911e715e3` | 178 | 1 |
| eating/drinking | `trm_4c898c0786246` | 4 | 3 |
| Ecological Momentary Assessment of Stressful Events | `tsk_c6667oSpAnrBT` | 505 | 1 |
| embedded figures test | `trm_4b749b8829eee` | 258 | 3 |
| emotion expression identification | `trm_551efd8a98162` | 100 | 1 |
| Emotion Identification Task | `tsk_A1AEVp7clZsCB` | 511 | 2 |
| emotional regulation task | `trm_4da890594742a` | 114 | 8 |
| encoding task | `trm_4c898c33ee5f8` | 85 | 10 |
| Enumeration task | `tsk_wiCMUNujvVRCR` | 138 | - |
| episodic recombination paradigm | `trm_59ed1f7a0ac9c` | 990 | 4 |
| error awareness task | `tsk_nzi0bkdoO8a23` | 1389 | - |
| Expressive One Word-Picture Vocabulary Test | `trm_5262c98a09546` | 232 | 1 |
| Expressive One-Word Picture Vocabulary Test | `trm_5298f15fe0fcf` | 349 | - |
| Expressive Vocabulary Test | `trm_52602e2e0c43b` | 96 | 1 |
| extradimensional shift task | `tsk_4a57abb949a5d` | 398 | 3 |
| Face Identification task | `trm_551efdfd1a356` | 4 | 1 |
| face matching task | `trm_4f24247912761` | 233 | 1 |
| face monitor/discrimination | `trm_4c898cb4ada49` | 266 | - |
| face working memory task | `trm_4f2421a62cdf8` | 212 | - |
| Facial Expression Display Task | `tsk_xQrUFIhZsBUFE` | 115 | - |
| facial expression observation | `tsk_02fiuOOFboHmh` | 57 | - |
| Facial Expression Observing Task | `tsk_JaF5u33GgYRT3` | 143 | - |
| facial recognition task | `trm_5090b32d6b376` | 213 | - |
| Fagerstrom Test for Nicotine Dependence | `tsk_4a57abb949a78` | 84 | - |
| fame judgment task | `trm_4f241fe40a950` | 132 | - |
| Fictitious event ordering | `trm_59cd03eeeab30` | 303 | - |
| figure ground task | `trm_551b0d687ee33` | 75 | - |
| film viewing | `trm_4c898da401420` | 107 | - |
| Fitts task | `trm_4f24226fa2903` | 201 | 1 |
| fixation task | `trm_4c898f72228f3` | 35 | 5 |
| flexion/extension | `trm_4c898fad429ed` | 81 | 1 |
| following commands | `trm_5798cb6027f28` | 231 | 3 |
| Food viewing (passive) | `tsk_rjSJbUa5Jk2Mb` | 129 | 1 |
| foreshortened view task | `trm_4fbd2dc0273d9` | 137 | - |
| free word list recall | `trm_4c898fc6722f4` | 99 | 3 |
| Frustration in Timed Backwards Math | `tsk_m9ZOG13yjvsPV` | 497 | 6 |
| Future Events Structured Interview | `tsk_5UPYiqtoX3yUf` | 596 | 2 |
| gating | `trm_551b14d7d5882` | 4 | 1 |
| general knowledge task | `trm_4f24237f2ed47` | 203 | - |
| Generalization of Instrumental Avoidance Task | `tsk_BuPIiFcjBo2aX` | 1394 | - |
| gm Paradigm | `trm_569d6eef27433` | 71 | - |
| Graded Naming Test | `trm_50f741a965470` | 800 | 1 |
| grasping task | `trm_4c898ff0bea97` | 181 | 2 |
| Gray Oral Reading Test - 4 | `tsk_4a57abb949aa1` | 400 | 3 |
| hand chirality recognition | `trm_586fd907e4fc6` | 57 | 1 |
| hand side  recognition | `trm_586fd8a2c77ca` | 56 | - |
| haptic illusion task | `trm_4da88c205b16b` | 95 | 1 |
| Hayling sentence completion test | `trm_4da88c904862b` | 359 | 3 |
| Hidden Path Learning Task | `tsk_o32s7ULZu8ATo` | 434 | - |
| Hidden State Decision Making Task | `trm_58335e885873f` | 638 | 1 |
| hierarchical rule task | `trm_5696bb7166121` | 156 | - |
| Hierarchical Task | `tsk_EaAMakeLSEYxm` | 717 | 1 |
| Holt and Laury Risk Titrator | `trm_56674f71483b0` | 457 | 1 |
| Hooper visual organization test | `tsk_4a57abb949aae` | 225 | 4 |
| Hungry Donkey Task | `trm_50b40bca8cf83` | 500 | 3 |
| ideational praxis task | `trm_5798d0fbe2bd1` | 592 | 2 |
| image monitoring | `trm_5667436296862` | 181 | - |
| imagined movement | `trm_4c899005b11d5` | 75 | 3 |
| imagined objects/scenes | `trm_4c89903149aeb` | 128 | 2 |
| immediate memory task | `trm_4fba857ad04ac` | 194 | 2 |
| incentive modulated antisaccade task | `trm_565a2e79b22f2` | 2526 | 2 |
| Incidental encoding task | `trm_50df0dd9d0b6f` | 226 | - |
| inductive reasoning aptitude | `trm_4d8a48e403c78` | 48 | 2 |
| Information Sampling Task | `trm_50f73d557c967` | 1558 | 2 |
| Inter-dimensional/Extra-dimensional Shift Task | `trm_5667476fc14dd` | 971 | - |
| Inter-modal selective attention task | `trm_551f0713a5a17` | 57 | 1 |
| intermodal preferential looking paradigm | `trm_4eb1f3a8ec119` | 320 | 1 |
| Internal menu choice task | `tsk_3KF7rOdrBGivs` | 469 | - |
| Internal Self-Efficacy Task | `tsk_nHhIFQgl91Nkc` | 755 | 1 |
| intradimensional shift task | `tsk_4a57abb949ad7` | 346 | 3 |
| Ishihara plates for color blindness | `tsk_4a57abb949af3` | 361 | 1 |
| isometric force | `trm_4c8990480ad0f` | 95 | 1 |
| Joint Attention / Social and Nonsocial Orienting Task | `trm_529ce04b778b6` | 252 | 2 |
| Judgment of Line Orientation Task | `trm_529ce3d22be3e` | 134 | - |
| Kanizsa figures | `tsk_4a57abb949b00` | 327 | 3 |
| Kaufman Brief Intelligence Test | `trm_529ce6ecb35f8` | 209 | 2 |
| keep-track task | `trm_4c40d4054f38b` | 341 | 4 |
| Landmark task | `trm_5346938eed092` | 484 | - |
| Language Rule Learning | `tsk_KVUZHlsv8pesh` | 4074 | - |
| lateral facilitation | `trm_551b0c0a742d2` | 4 | 1 |
| length match task | `trm_4fbd2b16e7aff` | 132 | - |
| letter case judgment task | `trm_4f241001dfcee` | 79 | - |
| letter comparison task | `trm_4da86c8bb3b04` | 114 | - |
| letter matching task | `tsk_PNUOMlNOAajsT` | 300 | - |
| letter memory | `trm_5696a9cfe45b1` | 248 | - |
| letter naming task | `tsk_4a57abb949b2b` | 131 | 2 |
| letter number sequencing | `trm_4c3e0a9576c3b` | 88 | 5 |
| Listening and reading task | `trm_55217a9f473f0` | 77 | 1 |
| listening span task | `trm_4c40d1d16071e` | 177 | 2 |
| living-nonliving task | `trm_4f24258b51e2c` | 127 | 1 |
| living/nonliving judgment on mirror-reversed and plain-text words | `trm_5176cf9d3d512` | 302 | - |
| local computation | `trm_551b1004bc652` | 4 | 1 |
| logical reasoning task | `trm_4f24154867d84` | 165 | 1 |
| MacArthur Communicative Development Inventories | `trm_4da891794859f` | 261 | 2 |
| Manipulation of coherence and cohesion | `trm_552181d7be45e` | 100 | 1 |
| Manipulation of individual words | `trm_55218116cbf40` | 108 | 1 |
| Manipulation of ISI | `trm_551efeacb9deb` | 116 | 3 |
| Manipulation of language and non-verbal behaviors | `trm_55217e77441b0` | 85 | 1 |
| Manipulation of predictability | `trm_55492d262a847` | 4 | - |
| Manipulation of predictability and acceptability | `trm_55217d7fbfdba` | 112 | 1 |
| matching familiar figures test | `trm_4da87b8bf1511` | 221 | 1 |
| matching pennies game | `tsk_4a57abb949b46` | 542 | 2 |
| Maze | `tsk_uh2RnLbc0PU3v` | 610 | 1 |
| McGurk effect | `trm_51a637dfeffd5` | 152 | 2 |
| Measured Emotion Differentiation Test | `trm_56a2a74ab3ef6` | 1084 | - |
| meditation task | `trm_4fb4175126374` | 159 | 3 |
| Memory encoding task | `tsk_mFS3uwUMAhXxe` | 91 | - |
| memory span test | `trm_4da869e68b5c4` | 28 | - |
| mental arithmetic task | `trm_4f24179122380` | 112 | - |
| mental imagery task | `trm_4f240edf92865` | 45 | - |
| Mental time travel task | `tsk_xxVr20Bf4zyme` | 164 | - |
| mentalizing task | `trm_4f241ab50513b` | 224 | - |
| MicroCog | `trm_4b9568b2865c2` | 111 | 5 |
| micturition task | `trm_4c89909cc1f33` | 87 | - |
| Mindstrong for Regulation of Cognition | `tsk_zfiXINJdIc1DM` | 588 | 4 |
| Mindstrong for Regulation of Emotion | `tsk_kBYLTvZx59uOC` | 764 | 2 |
| Mindstrong for Regulation of Self-Focused Reflection | `tsk_aojKzJ2tvdhGZ` | 649 | 1 |
| Mini Mental State Examination | `tsk_4a57abb949bb1` | 452 | 1 |
| minimal feature match task | `trm_4fbd2d71adf87` | 155 | - |
| mirror reading task | `trm_5176cf2c19e89` | 114 | - |
| mixed event-related probe | `trm_4e8dd3dfd9fff` | 280 | - |
| mixed gambles task | `trm_4cacee4a1d875` | 457 | 10 |
| Montreal Cognitive Assessment | `trm_57964b8a66aed` | 523 | 7 |
| Moral Dilemma Task | `trm_57ebe6583f52d` | 223 | - |
| Motion processing | `trm_5536be03400e7` | 4 | 1 |
| Motor Screening Task | `trm_50f72e93ea9e3` | 394 | 1 |
| motor sequencing task | `tsk_4a57abb949bbf` | 72 | 3 |
| motorphotic | `trm_5975f939336c0` | 376 | - |
| Mouse tracking paradigms | `trm_55217bd86ee12` | 77 | - |
| movie watching task | `tsk_jbg1oF4D9OTkO` | 67 | - |
| Mullen Scales of Early Learning | `trm_5262d6d7b2097` | 230 | 4 |
| Muller-Lyer Illusion | `trm_5535623c2536a` | 51 | 1 |
| multi-attribute decision making task | `trm_4f244fee7d195` | 171 | - |
| multi-attribute reward-guided decision task | `trm_553eb28436233` | 911 | - |
| Multi-class n-back task | `trm_558c324478d22` | 73 | - |
| Multidimensional Assessment of Interoceptive Awareness | `tsk_2wRB9XpiA4xMN` | 989 | 2 |
| Multiplication task | `trm_5696c2c063222` | 166 | - |
| multisource interference task | `trm_4f2419c4a1646` | 73 | - |
| multistability | `trm_551b0cdcde976` | 4 | 1 |
| music comprehension/production | `trm_4c8990b07a037` | 64 | 4 |
| NART-R | `trm_5798f94752841` | 351 | 2 |
| National Adult Reading Test | `trm_5798f5c57048d` | 836 | 2 |
| navigation task | `trm_4f241173868a3` | 55 | - |
| negative priming task | `trm_4f244d64e45bc` | 260 | 1 |
| network traversal task | `trm_597249e1ec9d3` | 151 | - |
| nine-hole peg test | `tsk_4a57abb949bdb` | 182 | 2 |
| non-choice task | `trm_4d55997cd3edb` | 533 | 1 |
| Non-instrumental information seeking task | `tsk_xFpgex9zOvlOu` | 1221 | - |
| non-spatial cuing paradigm | `trm_55295382db2c5` | 286 | 1 |
| nonword repetition task | `trm_4da88b17b985b` | 113 | 1 |
| Novelty detection task | `trm_551eff0fdab74` | 4 | 1 |
| NPU-threat test | `trm_502420a682976` | 141 | 2 |
| Numerical Working Memory Task | `trm_553ec40d44c51` | 129 | - |
| numerosity estimation task | `trm_4f2457454e458` | 39 | 1 |
| object alternation task | `trm_4da88bb3c2462` | 136 | - |
| object classification | `trm_551b107c5c111` | 4 | 1 |
| object decision task | `trm_4fbd2c18e1dd9` | 99 | - |
| object n-back | `trm_4ebd477ab5a11` | 65 | - |
| object one-back task | `trm_4ebd47b8bab6b` | 65 | 5 |
| object perception task | `trm_551b0ee81fb6b` | 4 | 2 |
| Object Rating Task | `trm_553fbba5d5327` | 97 | - |
| object recognition task | `trm_551b0f2b930ab` | 271 | 1 |
| object working memory task | `trm_4f2421c391b83` | 139 | - |
| object-discrimination task | `tsk_4a57abb949be9` | 410 | 2 |
| oculomotor delayed response | `trm_4c3e0add96550` | 80 | 2 |
| odd-even task | `trm_4f2452adb7d23` | 88 | - |
| olfactory monitoring/discrimination | `trm_4c89912c79030` | 179 | 1 |
| One Touch Stockings of Cambridge | `trm_50f84bbdcfa4e` | 1251 | 2 |
| orientation match task | `trm_4fbd2b4bb165c` | 97 | 1 |
| orientation test | `trm_5798d7ba0197d` | 187 | - |
| orthographic discrimination | `trm_4c89913f80802` | 173 | 3 |
| orthographic task | `trm_4f24250e0137e` | 51 | - |
| Other evaluation task | `tsk_i6bcjHSADB30O` | 108 | - |
| overlapping figures task | `trm_4fbd2b964d3ec` | 93 | - |
| Overt word repetition | `trm_534690b0e9dc5` | 76 | 3 |
| Paced Auditory Serial Addition Test | `trm_4da87fb28978e` | 116 | - |
| pantomime task | `tsk_4a57abb949c04` | 130 | 2 |
| Parent-Child Interaction Protocol | `tsk_HJI7NLY38yZgx` | 982 | 1 |
| parity judgment task | `trm_4f24572cb42e4` | 91 | - |
| Partial Report Procedure | `trm_50b65ef129e23` | 506 | 1 |
| passive avoidance task | `trm_4f241fd47f16b` | 147 | - |
| passive listening | `trm_4c8991fadfe01` | 221 | 2 |
| pattern comparison task | `trm_4da86cb034ff6` | 382 | 1 |
| Peabody Picture Vocabulary Test | `trm_5266bebe14d2e` | 128 | 1 |
| Pennâs Logical Reasoning Test | `trm_56a2a7750ffd0` | 549 | - |
| perceptual closure task | `trm_551b05e03be48` | 173 | 1 |
| perceptual discrimination task | `trm_553ebfc390256` | 286 | 1 |
| perceptual organization | `trm_551b0e6b88363` | 4 | 1 |
| phoneme detection task | `trm_4f24479b0db8f` | 105 | - |
| phonetic discrimination task | `trm_4f2414a1bab77` | 77 | - |
| phonological discrimination | `trm_4c89922cb6402` | 165 | 4 |
| Piaget's Water Jar Task | `trm_5206bf053acf4` | 378 | 1 |
| pitch/monitor discrimination | `trm_4c89924414c69` | 333 | 1 |
| pleasantness rating task | `tsk_Jb7hdmvDY3rLV` | 159 | - |
| Plus-minus | `trm_5696b316c220a` | 109 | - |
| point subtraction aggression paradigm | `tsk_zMlmDcfxjld0K` | 109 | - |
| pointing task | `trm_4c89926767870` | 92 | 4 |
| position of gap match task | `trm_4fbd2b6fd33c5` | 93 | - |
| Positive and Negative Affect Schedule (PANAS)- Child Version | `tsk_bc6vIpoShChdF` | 505 | 3 |
| Positive and Negative Images Task | `tsk_pl4uqVGM1uj3Z` | 148 | - |
| predictive-inference helicopter task | `trm_553e6b8e33da4` | 722 | - |
| Probabilistic gambling task | `trm_4d54b61a14a14` | 454 | 1 |
| problem solving task | `trm_4f241325579c6` | 57 | - |
| prospective sequential decision making task | `tsk_VokAidevRX1Vs` | 423 | - |
| prototype distortion task | `trm_4f24550fc5f38` | 184 | - |
| pseudoword naming task | `tsk_4a57abb949d25` | 340 | 3 |
| psychophysics task | `trm_502985b4baaed` | 137 | - |
| pursuit rotor task | `trm_4da88b63787d6` | 436 | - |
| Pursuit Tracking Task | `tsk_GdteOhkqZJLYg` | 294 | - |
| pyramids and palm trees task | `tsk_4a57abb949d32` | 317 | 1 |
| random number generation task | `trm_4f2417d4a63ae` | 65 | - |
| rapid automatized naming test | `trm_4b86c2e871b14` | 389 | 3 |
| Rapid Marital Interaction Coding System (RMICS) | `tsk_QN7TaO3lQgQpv` | 758 | 2 |
| rapid serial object transformation | `trm_4b86dbcd8ff78` | 291 | 3 |
| Rapid Visual Information Processing | `trm_50f8516279419` | 663 | 1 |
| Re-entrant processing | `trm_551efd39a74dd` | 4 | 1 |
| Reaction Time | `trm_50f84e8ab7af8` | 585 | 1 |
| reading (covert) | `trm_4c8a82ba8a538` | 99 | - |
| reading (overt) | `trm_4c8a82eeaa58f` | 88 | 2 |
| reading span task | `trm_4c40d168898db` | 592 | 2 |
| reappraisal task | `trm_4f2420b042165` | 71 | - |
| recency judgment task | `trm_4f241fb95918f` | 180 | - |
| Reciprocal Artwork Evaluation Task | `tsk_zcuAj6VrsFmfV` | 340 | - |
| recitation/repetition (covert) | `trm_4c8a830dec136` | 136 | 2 |
| recitation/repetition (overt) | `trm_4c8a8329cb8ff` | 133 | 3 |
| relational reasoning task | `trm_4f2454dfca337` | 4 | - |
| Relative Reinforcing Efficacy Purchase Task | `tsk_dn4ejmrGGaUAZ` | 533 | 1 |
| response mapping task | `trm_4da88b3b0cbcc` | 28 | - |
| rest eyes closed | `trm_54e69c642d89b` | 104 | - |
| rest eyes open | `trm_4c8a834779883` | 102 | - |
| retrieval-induced forgetting task | `trm_4da87f81bc2c8` | 28 | - |
| Rey-Ostereith Complex Figure Test | `trm_4da880396c76b` | 28 | - |
| Reynell Developmental Language Scales | `trm_4da8914987ee2` | 270 | 2 |
| Risk Preferences Task | `tsk_22KTtBdDDjZrU` | 473 | 3 |
| risky decision-making under social influence | `tsk_d9vPgovlo7aJU` | 252 | - |
| risky gains task | `tsk_4a57abb949d5b` | 585 | 1 |
| risky lotteries task | `tsk_wPIAFIkSlX3Tm` | 684 | - |
| Rivermead Behavioural Memory Test | `trm_4da8885b33375` | 162 | - |
| route learning | `trm_58ab8a6131c5a` | 1448 | - |
| Running Memory | `trm_551f0b18d7ca0` | 93 | 3 |
| Salthouse and Babcock Listening Span task | `tsk_4a57abb949d69` | 276 | 4 |
| same-different task | `trm_4b75ea4ddd896` | 709 | 4 |
| scene recognition task | `trm_4da6327154fd4` | 114 | 1 |
| selective attention task | `tsk_4a57abb949d76` | 92 | 2 |
| Self evaluation task | `tsk_29IL64WzhiO9u` | 93 | - |
| self monitoring task | `trm_551b153bc78fc` | 4 | 1 |
| self ordered pointing task | `trm_4c40d325977f0` | 147 | 5 |
| semantic anomaly judgement task | `tsk_4a57abb949d84` | 345 | 4 |
| semantic association task | `tsk_4a57abb949d92` | 110 | 2 |
| semantic classification task | `trm_4f2412d4c3b88` | 138 | 1 |
| semantic decision task | `trm_4f240cb09f8e5` | 75 | - |
| semantic memory task | `trm_4f241c0737cc0` | 77 | - |
| semantic relatedness task | `trm_4f240d7664628` | 79 | - |
| Sensory Profile | `trm_526943e3cbaaf` | 856 | 9 |
| sentence completion test | `tsk_4a57abb949d9f` | 530 | - |
| sentence-picture matching task | `trm_4f241e8a01052` | 109 | - |
| Sentence/discourse content test | `trm_5521807e50549` | 85 | 1 |
| Sequence encoding | `trm_551f0cc82ed49` | 111 | 2 |
| Sequence reproduction | `trm_551f103b3edeb` | 151 | 1 |
| sequential shape matching | `trm_4e8a0dd29ec7b` | 369 | 2 |
| shadowing task | `trm_4f2456932f11b` | 128 | - |
| Shift Task | `trm_5696c3fa0061a` | 243 | 1 |
| short-term memory task | `trm_4f24239cc239e` | 4 | - |
| Simple span task | `trm_551f0b9654d23` | 175 | 2 |
| Single item food choice task | `trm_55c686e0824e8` | 1731 | 1 |
| size match task | `trm_4fbd2af083332` | 79 | - |
| social decision-making task | `tsk_Ncknr0soiM4IV` | 251 | - |
| social influence for food preferences task | `trm_553fbbf79ebc5` | 623 | - |
| Social influence on emotion task | `tsk_ec4xbqynlG1uR` | 939 | - |
| social judgment of faces task | `trm_553eb45e2b709` | 342 | 6 |
| social judgment task | `trm_4f2453ce33f16` | 210 | - |
| Social Norm Processing Task | `trm_58c80c3376c95` | 239 | 1 |
| social vs physical perception task | `tsk_ASxfTzukfK3Te` | 492 | - |
| Space Fortress | `trm_50df1c0d946b8` | 1068 | - |
| Space Fortress with Oddball | `trm_50df1dd534ff2` | 71 | - |
| Spatial cuing paradigm | `trm_551f0634b2607` | 211 | 1 |
| spatial delayed response task | `trm_4dadbe225bdf1` | 307 | 1 |
| spatial location/discrimination | `trm_4c8a83f27ac55` | 145 | 1 |
| spatial n-back task | `tsk_4a57abb949df1` | 309 | 2 |
| spatial working memory task | `trm_4f2453b806fe1` | 1159 | 1 |
| Speech Detection | `trm_5519c3eaa3fb7` | 4 | - |
| spelling task | `trm_4f24135453d65` | 50 | 1 |
| Stanford Leisure-Time Activity Categorical Item | `trm_56bbe12994926` | 187 | - |
| Stanford-Binet Intelligence Scales | `trm_526af65b16c82` | 516 | 5 |
| Stockings of Cambridge Task | `trm_4da890cf99b9e` | 461 | 1 |
| Stop signal task with dot motion discrimination | `trm_558c3350c6a9f` | 80 | - |
| stop signal task with pseudo word naming | `trm_5181f863d24f4` | 110 | 5 |
| stop-change task | `trm_4f2447dfa5947` | 138 | - |
| Structured Clinical Interview for Diagnostic and Statistical Manual of Mental Disorders (DSM-IV) | `tsk_4a57abb949e35` | 495 | 1 |
| subjective emotional picture discrimination | `trm_4c8a840d6f969` | 189 | 1 |
| Surface properties of object paradigms | `trm_552184243d7ab` | 183 | 1 |
| Symbol Counter Task | `trm_50b66c50ca2ac` | 825 | - |
| synchrony judgment task | `trm_4e31d031bc8c2` | 183 | 1 |
| syntactic acceptability judgement task | `tsk_4a57abb949e7c` | 158 | 3 |
| syntactic discrimination | `trm_4c8a842512a33` | 194 | 2 |
| tactile monitor/discrimination | `trm_4c8a843d8d352` | 336 | 1 |
| task-set learning | `tsk_n4koOyLJMyobG` | 205 | - |
| temporal order judgment task | `trm_4e31d69b7f422` | 304 | 1 |
| Test of Adolescent and Adult Language | `trm_52713c85c0bd2` | 425 | 2 |
| Test of Early Language Development | `trm_527138126fb20` | 235 | 3 |
| Test of Language Development | `trm_527143a263937` | 263 | 1 |
| test of variables of attention | `trm_4da86cdbd9eeb` | 105 | 2 |
| Test of Word Reading Efficiency | `tsk_4a57abb949ea5` | 360 | 2 |
| Thirst perception | `tsk_lihqGPC9Y8ge0` | 123 | - |
| Time Wall | `trm_50c0f3e6c596e` | 333 | - |
| Time-series of response time | `trm_55218536d1710` | 52 | 1 |
| tone counting | `trm_4ebc6a6b75ebf` | 120 | 6 |
| Tone Matching | `trm_5519c2645167e` | 232 | 1 |
| tone monitor/discrimination | `trm_4c8a84825c4e4` | 196 | 1 |
| trace conditioning | `trm_4a3fd79d0b3d7` | 168 | 1 |
| Transitive inference task | `trm_551f1491a2fe8` | 323 | 1 |
| tri-modal roving stimulus paradigm | `tsk_QyZsV96fiVlT1` | 332 | - |
| Trier Social Stress Test | `tsk_Qa4kXAzvUyaGL` | 563 | - |
| Two item food choice task | `trm_55c691909c580` | 2366 | - |
| underlining test | `trm_4b86c473a7166` | 284 | 4 |
| updating task | `trm_4f242172aea5d` | 250 | - |
| Uznadze haptic illusion task | `trm_4da88ec6735ad` | 200 | 1 |
| value-based decision making | `tsk_QM81yNuuioVho` | 184 | - |
| Vandenberg & Kuse Tasks | `trm_4af89b3a925ca` | 313 | 2 |
| Verbal description of visual depiction | `trm_552174d3b61fb` | 61 | 1 |
| Verbal Interference Test | `tsk_ccTKYnmv7tOZY` | 795 | 3 |
| verbal working memory task | `trm_4f2457a8b0bc8` | 752 | 1 |
| Vernier discrimination task | `trm_5519c7f17de9f` | 74 | 1 |
| vibrotactile monitor/discrimination | `trm_4c8a84afdd863` | 83 | 1 |
| video games | `trm_4c8a84d4c4157` | 4 | - |
| Video-Mediated Affective Recall | `tsk_161qcskOyTlfY` | 531 | 1 |
| Vineland Adaptive Behavior Scales | `trm_52717a95a3b03` | 285 | 6 |
| violation-of-expectation task | `tsk_2lU25qYLrwkfj` | 1189 | - |
| visual alignment task | `tsk_4a57abb949edb` | 196 | 2 |
| Visual Analogue Scales | `trm_50f7370ace495` | 399 | 1 |
| visual attention task | `trm_4c8a84f20dde2` | 399 | 5 |
| visual illusion susceptibility | `trm_551b0dc4e4359` | 4 | 1 |
| Visual Object Learning Test | `trm_50f9daf1c3834` | 361 | 1 |
| Visual Patterns Test | `trm_4da886fc2bc46` | 403 | - |
| visual pursuit/tracking | `trm_4c8a85534241d` | 112 | 3 |
| Visual short term memory task | `tsk_1eLUszKc87tI1` | 181 | - |
| Visual Statistical Learning | `tsk_NOaQmzjqHM4iO` | 721 | - |
| Visual world paradigm | `trm_55217c8179b00` | 91 | 1 |
| Visuomotor rotation task | `tsk_iLPEMA3QRsS3K` | 1251 | - |
| visuospatial cueing task | `tsk_4a57abb949ee9` | 182 | 2 |
| Warrington's Face/Word Recognition Test | `tsk_4a57abb949ef7` | 810 | - |
| whistling | `trm_4c8a8575d1e55` | 114 | 1 |
| why/how task | `trm_53c4465b0466f` | 788 | 3 |
| willingness to wait task | `trm_569989ef8cff4` | 435 | - |
| word attack | `tsk_4a57abb949f2f` | 215 | 3 |
| word comprehension task | `trm_4f240fbdf1601` | 55 | - |
| word generation task | `tsk_4a57abb949f3d` | 772 | 2 |
| word identification | `tsk_4a57abb949f4a` | 270 | 4 |
| word one-back task | `trm_4ebd482eba5b1` | 79 | 9 |
| word recognition task | `trm_5798c6a933abc` | 224 | 2 |
| word stem completion (covert) | `trm_4c8a858da803d` | 78 | 2 |
| word stem completion (overt) | `trm_4c8a85a4564b2` | 77 | 3 |
| word-picture matching task | `trm_4f241ee9c4e37` | 4 | - |
| word-picture verification task | `trm_4b65e5e2ab3ca` | 263 | 2 |
| WRAT-4 Math Computation | `trm_5696d061adfb5` | 63 | - |
| WRAT-4 Word Reading | `trm_5696d0a4902df` | 59 | - |
| writing task | `trm_4c8a85c5c75eb` | 68 | 4 |
| Yellow Light Game | `trm_59668f09db813` | 2481 | - |
| zoo map test | `trm_4da89089ce0af` | 190 | - |
### Rating scales, questionnaires and inventories (107)

| Atlas entry | Atlas ID | Definition chars | Concepts |
|---|---|---|---|
| aberrant behavior checklist - community | `trm_523c7a0a73cf5` | 594 | 5 |
| adolescent symptom inventory | `trm_523df616da8a6` | 253 | 11 |
| Adult ADHD Clinical Diagnostic Scale | `trm_5586ff878155d` | 419 | 6 |
| Adult ADHD Self-Report Scale | `trm_55a6a79b55c8b` | 199 | - |
| adult behavior checklist | `trm_523ca67b786d5` | 210 | 2 |
| Aesthetic Exprience Questionnaire (AEQ) | `tsk_STbROQuOk0Qo5` | 389 | - |
| Anxiety Sensitivity Index - 3 (ASI-3) | `tsk_L1akyyjEGdiUs` | 459 | 2 |
| Barratt Impulsiveness Scale | `trm_55a6a8e81b7f4` | 406 | 3 |
| battelle developmental inventory | `trm_523e10cad0ce6` | 248 | 1 |
| behavioral rating inventory of executive function | `tsk_4a57abb9498ab` | 529 | 7 |
| big five questionnaire | `trm_523f5c17d7edb` | 267 | 5 |
| Brief Psychiatric Rating Scale | `trm_55a6a52537c2b` | 482 | - |
| Brief Risk-Resilience Index for Screening (BRISC) | `tsk_NrSniDhXY2NKm` | 760 | 2 |
| brief self control scale | `trm_56a915461cd91` | 142 | 1 |
| brief symptom inventory | `trm_52405b6f7ebe9` | 281 | 9 |
| broad autism phenotype questionnaire | `trm_523dfd5b7a9f1` | 394 | 3 |
| broader phenotype autism symptom scale | `trm_524055ac4fecf` | 263 | 4 |
| Center for Epidemiologic Studies Depression Scale | `trm_5258346e72223` | 198 | 8 |
| Chapman Infrequency Scale | `trm_57c0c015b603c` | 4 | - |
| Chapman Magical Ideation Scale | `trm_57c0c570473d3` | 259 | - |
| Chapman Perceptual Aberration Scale | `trm_57c0c146e0019` | 259 | - |
| Chapman Physical Anhedonia Scale | `trm_57c0c1af018a5` | 291 | - |
| Chapman Social Anhedonia Scale | `trm_57c0c186b07d4` | 300 | - |
| Child Behavior Checklist | `trm_524b4a402c87e` | 396 | 11 |
| Children's Communication Checklist | `trm_5255c99be1e53` | 233 | 11 |
| Children's Memory Scale | `trm_52167db323438` | 433 | 6 |
| Children's Psychiatric Rating Scale | `trm_525c56680c13c` | 648 | 8 |
| Children's Yale-Brown Obsessive Compulsive Scale | `trm_52602c143d3a9` | 87 | 1 |
| Consideration of Future Consequences Scale | `tsk_LURJ93Bk1echa` | 241 | 1 |
| Couple Coercion Scale | `tsk_QEgcdL3G9d3fp` | 195 | 1 |
| Daily Inventory of Stressful Events (DISE) | `tsk_eDDTJCIrL19Qj` | 674 | 1 |
| Dickman Impulsivity Inventory | `trm_55a6a95f66508` | 571 | 1 |
| duckworth's short grit scale | `trm_56a9166421494` | 213 | 1 |
| Early Childhood Behavioral Questionnaire | `trm_5298e7a465b41` | 363 | 11 |
| Eating questionnaire | `trm_56aac5f6e4702` | 103 | 1 |
| Eckblad and Chapman's Hypomanic Personality Scale | `trm_57c0bf6b14b90` | 4 | - |
| Edinburgh Handedness Inventory | `tsk_4a57abb949a41` | 486 | 1 |
| Emotion Regulation Questionnaire | `trm_56bbead1a7ed4` | 250 | 1 |
| Emotion Regulation Strategies Scale | `tsk_EeJGKBAbpHkIm` | 471 | - |
| Eysenck Personality Questionnaire | `trm_55a6ae8f44ac3` | 314 | - |
| Five Facet Mindfulness Questionnaire | `trm_56ab12e0f1a61` | 105 | 1 |
| Future Orientation Scale of the Time Perspective Survey (child version) | `tsk_gskvlEiCHg899` | 623 | 2 |
| future time perspective questionnaire | `trm_56a915fe77945` | 342 | 1 |
| Generalized Self-Efficacy Scale | `tsk_p7cabUkVvQPBS` | 525 | 1 |
| Glasgow Coma Scale | `trm_4da890f978492` | 392 | - |
| Godin Leisure-Time Exercise Questionnaire | `tsk_7f8coV4TPvTeZ` | 512 | - |
| Hamilton Psychiatric Rating Scale for Depression | `trm_559e2af1cc0ce` | 563 | - |
| Hopkins Symptom Checklist | `trm_55a6a860a7088` | 364 | - |
| Hypomanic Personality Scale | `trm_55a6c92db12b0` | 166 | - |
| I7 impulsiveness and venturesomeness questionnaire | `trm_56a91e3e982f9` | 279 | 3 |
| Immersive Virtual Reality Assay for Target: Regulation of Cognition (Behavioral and Self-Report) | `tsk_H2hu4WmHYl8Tu` | 672 | 1 |
| Immersive Virtual Reality Assay for Target: Regulation of Emotion (Behavioral and Self-Report) | `tsk_Sgb6i1nFqMVjQ` | 803 | 1 |
| Immersive Virtual Reality Assay for Target: Regulation of Self-Reflection (Behavioral and Self-Report) | `tsk_ZaJZLqgqcXCLq` | 622 | 1 |
| International Physical Activity Questionnaire – Short Form (IPAQ-SF) | `tsk_QlXQe5gup7UFj` | 440 | 1 |
| Kessler Psychological Distress Scale (K6+) | `tsk_OA90UJX5qwTyc` | 596 | 1 |
| Leiter International Performance Scale | `trm_5262cb3d852c0` | 1266 | 10 |
| Loneliness Rating Scale | `trm_529d087705bfa` | 140 | 1 |
| Maudsley Obsessive Compulsive Inventory | `tsk_4a57abb949b54` | 234 | 2 |
| Mindful Attention and Awareness Scale | `trm_56abcba3df89b` | 129 | 3 |
| Minnesota Multiphasic Personality Inventory | `trm_55a6c80b2c1d6` | 555 | - |
| modified Erickson Scale of Communication Attitudes | `trm_4da891d43240c` | 114 | - |
| Multidimensional Personality Questionnaire | `trm_55a6aa62c54f8` | 281 | - |
| Multidimensional Personality Questionnaire: Control vs. Impulsivity Scale | `tsk_tp1574mCRYbWD` | 577 | 2 |
| NIH Self-Efficacy Scale | `tsk_UwGwPHdQkMJqi` | 481 | 1 |
| NIH Toolbox General Life Satisfaction Survey | `trm_50f3c003327c4` | 531 | 1 |
| NIH Toolbox Hearing Handicap Inventory | `trm_50f37767e2958` | 559 | 1 |
| NIH Toolbox Meaning and Purpose Survey | `trm_50f5bfef58abb` | 371 | 1 |
| NIH Toolbox Pain Intensity Survey | `trm_50f385a8269ce` | 308 | - |
| NIH Toolbox Pain Interference Survey | `trm_50f3862422509` | 399 | - |
| NIH Toolbox Positive Affect Survey | `trm_50f3bc06cae36` | 468 | 1 |
| NIH Toolbox Vision-Related Quality of Life Survey | `trm_50f37f231aa4c` | 480 | 1 |
| Parent Cognition Scale | `tsk_dwOdvcER9RnBx` | 439 | 1 |
| Parent-Child Coercion Scale | `tsk_alz5hjlUXp4WY` | 132 | 1 |
| Parent-Rated Stress (NIH Perceived Stress Scale) | `tsk_m9ORBitZNadcZ` | 347 | 1 |
| Parrott Scale | `tsk_4a57abb949ce9` | 110 | - |
| Patient health questionnaire (PHQ-9) | `tsk_Y0LwjRqYtJSQO` | 19 | - |
| PDD Behavior Inventory | `trm_5262d903ae91d` | 653 | 8 |
| Pearlin Mastery Scale | `tsk_osfnJ7DNe8DB0` | 402 | 2 |
| Pittsburgh Sleep Quality Index | `trm_5585c83d15fad` | 494 | 1 |
| Positive and Negative Affect Scale | `tsk_4a57abb949d09` | 742 | 3 |
| Preschool Language Scale | `trm_5266bc6473fd8` | 190 | 2 |
| Scale for the Assessment of Negative Symptoms | `trm_55a6a36d9c3f9` | 520 | - |
| Scale for the Assessment of Positive Symptoms | `trm_55a6cffbcb5f7` | 517 | - |
| Selection-Optimization-Compensation (SOC) questionnaire | `trm_56ac06bac9334` | 431 | 3 |
| self regulation questionnaire | `trm_56a91ed5f1ccc` | 563 | - |
| SIDES Affect Dysregulation Scale (Child-Reported) | `tsk_HfEOU5RLqcxAD` | 385 | 1 |
| Social Communication Questionnaire | `trm_521687032f822` | 886 | 3 |
| Social Competence Questionnaire | `trm_525c4a78089ad` | 56 | 1 |
| Social Responsiveness Scale | `trm_5208fe678c652` | 703 | 5 |
| Spielberger's State-Trait Anxiety Questionnaire | `tsk_4a57abb949dfe` | 169 | - |
| State-Trait Anger Expression Inventory–2 (STAXI-2) | `tsk_FV3SD73LtdfUc` | 453 | - |
| Symptom Checklist-90-Revised | `tsk_4a57abb949e5b` | 274 | 1 |
| Temperament and Character Inventory | `trm_55a6cb4f951ea` | 437 | - |
| ten item personality questionnaire | `trm_56a919a478935` | 408 | - |
| theories of willpower scale | `trm_56a91a3082c31` | 338 | - |
| Tobacco Craving Questionnaire | `tsk_4a57abb949eb3` | 690 | - |
| treatment self-regulation questionnaire | `trm_56aa9833c4be2` | 517 | - |
| Unified Parkinson's Disease Rating Scale | `tsk_4a57abb949ece` | 413 | - |
| UPPS-P Impulsivity Scale | `trm_56a91a92043bc` | 270 | 1 |
| Wechsler Abbreviated Scale of Intelligence | `trm_4b94affc43245` | 481 | 7 |
| Wechsler Adult Intelligence Scale - Revised | `tsk_4a57abb949f12` | 239 | 6 |
| Wechsler Adult Intelligence Scale-Revised | `tsk_4a57abb949f04` | 379 | - |
| Wechsler Intelligence Scale for Children - Revised | `trm_4da6338803ed2` | 143 | - |
| Wechsler Memory Scale Fourth Edition | `trm_4b94b12bf0eb2` | 2000 | 5 |
| Young Mania Rating Scale | `trm_558702243da12` | 669 | - |
| zimbardo time perspective inventory | `trm_56a91e92eab46` | 270 | 4 |
| Zuckerman Sensation Seeking Scale | `trm_56abebfe9aaa3` | 423 | - |
### Standardized tests and batteries (41)

| Atlas entry | Atlas ID | Definition chars | Concepts |
|---|---|---|---|
| Adult's Penn Word Memory Test Delayed Memory | `trm_56a2a665baeb1` | 681 | - |
| Birmingham object recognition battery | `tsk_4a57abb9498ce` | 555 | 4 |
| Cambridge Neuropsychological Test Automated Battery | `trm_4da880ff8fd4a` | 808 | - |
| Halstead-Reitan Battery | `trm_529911569b592` | 478 | 1 |
| NIH Toolbox 2-Minute Walk Endurance Test | `trm_50eb69a57bc96` | 346 | 1 |
| NIH Toolbox 4-Meter Walk Gait Speed Test | `trm_50eb585f62f24` | 376 | 2 |
| NIH Toolbox 9-Hole Pegboard Dexterity Test | `trm_50eb4d3d96ff8` | 358 | 1 |
| NIH Toolbox Dimensional Change Card Sort Test | `trm_50eb115b6c476` | 731 | 2 |
| NIH Toolbox Dynamic Visual Acuity Test | `trm_50f38098952cb` | 1637 | 2 |
| NIH Toolbox Grip Strength Test | `trm_50eb51c2cd9fe` | 511 | 1 |
| NIH Toolbox Hearing Threshold Test | `trm_50f374718a91c` | 476 | - |
| NIH Toolbox List Sorting Working Memory Test | `trm_50eb17385e9a6` | 472 | 2 |
| NIH Toolbox Odor Identification Test | `trm_50f383e76e03b` | 622 | 1 |
| NIH Toolbox Oral Reading Recognition Test | `trm_50eb3b2d1de11` | 410 | 2 |
| NIH Toolbox Oral Symbol Digit Test | `trm_50eb461d446e1` | 699 | 1 |
| NIH Toolbox Picture Sequence Memory Test | `trm_4da88cb222308` | 843 | 1 |
| NIH Toolbox Picture Vocabulary Test | `trm_50eb0dc6668e1` | 485 | 2 |
| NIH Toolbox Standing Balance Test | `trm_50eb54d78841b` | 586 | 1 |
| NIH Toolbox Taste Intensity Test | `trm_50f379c6c9ea9` | 960 | 1 |
| NIH Toolbox Visual Acuity Test | `trm_50f37caf81432` | 1196 | 1 |
| NIH Toolbox Words-in Noise Test | `trm_50eb0a01bfd05` | 599 | 1 |
| Penn Conditional Exclusion Test | `trm_50f9952c2311a` | 606 | 1 |
| Penn Facial Memory Test Delayed Memory | `trm_56a2a622cdfbd` | 703 | - |
| Penn Fractal N-Back | `trm_569fc84bd541d` | 746 | 2 |
| Penn Matrix Reasoning Test | `trm_56a2a5f8315c5` | 1007 | - |
| Penn Motor Praxis | `trm_56a2abffcfae3` | 457 | - |
| Penn Visual Object Learning Test | `trm_56a2a6ad6edee` | 1126 | - |
| Penn Visual Object Learning Test Delayed Memory | `trm_56a2a98785453` | 935 | - |
| Penn Vocabulary Test | `trm_5696e10fcd36a` | 47 | - |
| Penn Word Memory Test | `trm_50f998dcbfcc8` | 394 | 2 |
| Pittsburgh Stress Battery | `tsk_U9gDp8utahAfO` | 441 | 1 |
| Short Penn Continuous Performance Test-Number and Letter Version | `trm_56a2b7c08a279` | 688 | - |
| WAIS Arithmetic | `trm_5106f4dfe08b1` | 318 | 1 |
| WAIS Comprehension | `trm_5106f82530aff` | 322 | - |
| WAIS Object Assembly | `trm_51071fc87a61f` | 113 | - |
| WAIS Picture Arrangement | `trm_51070ae889d95` | 87 | 1 |
| WAIS Picture Completion | `trm_5107067241007` | 260 | 1 |
| WAIS Similarities | `trm_510703e93367e` | 223 | - |
| WAIS Vocabulary | `trm_5106f17025386` | 333 | 1 |
| WAIS-Information | `trm_5106eae236c21` | 185 | 1 |
| WISC-R Mazes | `trm_4b86c55f3d5df` | 69 | 4 |
### Imaging protocol labels (26)

| Atlas entry | Atlas ID | Definition chars | Concepts |
|---|---|---|---|
| emotion processing fMRI task paradigm | `trm_550b5b066d37b` | 1117 | 5 |
| emotional localizer fMRI task paradigm | `trm_5873d0be34b8f` | 722 | - |
| flashing checkerboard | `trm_4c898f8f297ac` | 38 | - |
| fMRI Facial Emotion Paradigm | `tsk_qsprWaphqkwim` | 728 | 2 |
| fMRI localizer for the frontotemporal language system | `tsk_ORAzdOO86kNfM` | 521 | 1 |
| functional localizer fMRI tasks | `trm_553e85265f51e` | 536 | 9 |
| Go-NoGo fMRI paradigm | `tsk_tTKd4o04KpUDA` | 860 | 1 |
| horizontal checkerboard | `trm_586fd4fd8754a` | 293 | - |
| Interoceptive Attentiveness fMRI Task | `tsk_Rpfz9hVRPtUcq` | 812 | 1 |
| language processing fMRI task paradigm | `trm_550b54a8b30f4` | 1728 | 3 |
| motor fMRI task paradigm | `trm_550b53d7dd674` | 1007 | 8 |
| multi-object localizer task | `trm_558c33e7714ba` | 209 | - |
| Pain-matrix narrative localizer | `tsk_vbkfbu486lzDr` | 112 | - |
| relational processing fMRI task paradigm | `trm_550b5a47aa23e` | 1869 | 6 |
| retinotopic mapping task | `trm_558c4d3105abf` | 187 | - |
| retinotopic representation | `trm_551b0fd03d7d8` | 4 | 1 |
| Sentence/nonword language localizer | `trm_558c35979a284` | 202 | - |
| social bargaining fMRI task | `trm_553e88a66b676` | 592 | - |
| social cognition (theory of mind) fMRI task paradigm | `trm_550b557e5f90e` | 1111 | 7 |
| Social localizer fMRI task paradigm | `trm_5873d014bcfc8` | 1331 | - |
| spatial localizer fMRI task paradigm | `trm_5873ce8e77d1d` | 1259 | - |
| spatial working memory localizer task | `trm_558c36935a0e9` | 204 | - |
| standard localizer fMRI task paradigm | `trm_5873cd1c9d4c4` | 650 | - |
| synatcting and semantic fMRI task paradigm | `trm_5873e2469dd0d` | 667 | - |
| vertical checkerboard | `trm_586fd45d1bd21` | 270 | - |
| working memory fMRI task paradigm | `trm_550b50095d4a3` | 1417 | 11 |
### Physiological procedures (19)

| Atlas entry | Atlas ID | Definition chars | Concepts |
|---|---|---|---|
| acupuncture task | `trm_4c8989e1f3df7` | 126 | 2 |
| capsaicin-evoked pain | `trm_4e6a2f61b17b0` | 157 | 1 |
| cold pressor test | `trm_4e6a44ee854f8` | 147 | 1 |
| cold stimulation | `trm_4e664d3718e1b` | 126 | - |
| electric stimulation | `trm_4e68e08950157` | 116 | 1 |
| Gustatory stimulation with liquid tastes or flavors | `trm_5887c029d46f4` | 1397 | 1 |
| heat sensitization/adaptation | `trm_4e5662373bc89` | 158 | 2 |
| heat stimulation | `trm_4e550887d92de` | 117 | 1 |
| intensity for somatosensory stimulation | `trm_551b17b190582` | 4 | 1 |
| mechanical stimulation | `trm_4e5d07565b68e` | 124 | 1 |
| Narrative-based Pain Empathy Task | `tsk_tlatUto2tMCYC` | 318 | - |
| non-painful electrical stimulation | `trm_4c8990f59266f` | 58 | 1 |
| non-painful thermal stimulation | `trm_4c89910b7f8bc` | 68 | 2 |
| optogenetic stimulation | `tsk_pmvG0R2l7APPE` | 150 | - |
| pain monitor/discrimination task | `trm_4c8991c5beb0a` | 77 | 1 |
| phasic pain stimulation | `trm_4e6114e7b1ff2` | 216 | 1 |
| regulated heat stimulation | `trm_565a31fa6f444` | 588 | 1 |
| thermal grill illusion | `trm_4e5fcd75efb58` | 181 | - |
| tonic pain stimulation | `trm_4e6112759926e` | 236 | 1 |
