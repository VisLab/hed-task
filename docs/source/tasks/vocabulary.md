# Game vocabulary

The terms in which a task is modeled as a game; [the task model](../task_model.md)
explains them. A model has five parts. The standard form of a task is one
**game type**; it states the **game rules** on which it departs from the default,
the **game motivators** (why the player tries), any **game phases** beyond the
game's own structure, and one or more values of each **game facet** that applies.
A model may also name the **settings** a study chooses and other games it is
**combined** with. A variant states only what it changes. Each value below has its
own anchor, which the task pages link to. The source files are
`data/task_game_defs.json` and `data/task_facet_defs.json`.

## Game types

| Game type | Name | What the player does | Boundary |
|---|---|---|---|
| <span id="game-respond-to-rule"></span>`respond_to_rule` | Respond under a rule | A stimulus appears; the player applies a rule they were given and responds. | The answer depends only on the stimulus in front of the player and the rule, not on material studied earlier. |
| <span id="game-study-then-test"></span>`study_then_test` | Study, then be tested | The player takes material in, holds it over an interval, then shows what they kept. | There is material to keep and a later test of it, even when the interval is a second. |
| <span id="game-choose-for-outcomes"></span>`choose_for_outcomes` | Choose for a payoff | The player picks an option, sees what it pays, and picks again. | No option is correct by instruction; the options differ in what they pay. |
| <span id="game-interact-with-agent"></span>`interact_with_agent` | Play against another player | The player makes a move whose payoff depends on what another player does. | Another player, real or said to be real, has a stake in the outcome. |
| <span id="game-solve-problem"></span>`solve_problem` | Solve a puzzle | The player works out an answer or a sequence of moves. | The answer has to be worked out; it cannot be read off the stimulus by a rule. |
| <span id="game-produce-movement"></span>`produce_movement` | Make a movement | The player carries out or learns a movement pattern. | The movement itself is measured, not a choice it expresses. |
| <span id="game-undergo-stream"></span>`undergo_stream` | Watch or listen | The player takes in a stream; the measure is the response to the stream itself. | No answer is scored against a correct one as a main measure. |
| <span id="game-navigate"></span>`navigate` | Find the way | The player moves through a space to reach a goal. | The path through the space is the measure. |
| <span id="game-report-on-self"></span>`report_on_self` | Report on yourself | The player reports an internal state, a timing, or a memory of their own. | No answer can be checked against a correct one. |
| <span id="game-hold-state"></span>`hold_state` | Hold a state | The player keeps a bodily or mental state as instructed while the recording runs. | Nothing is presented that calls for a response and nothing is reported; holding the state is the whole job (rest, fixation). |

## Game rules

Each game type has its own rules. A rule a task does not state takes its default; a
task states a rule only to give another answer. 5 game types have no rules: Solve a puzzle, Make a movement, Find the way, Report on yourself, Hold a state.

### Respond under a rule

Rules of the game type `respond_to_rule`.

<span id="rule-respond-to-rule-competitor"></span>**What competes with the correct response?** Rule `competitor`, default `none`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-competitor-none"></span>`none` | Nothing competes with the correct response. |
| <span id="rule-respond-to-rule-competitor-neighbouring-items"></span>`neighbouring_items` | Items next to the target call for a different response (the flankers of a flanker display). |
| <span id="rule-respond-to-rule-competitor-irrelevant-dimension"></span>`irrelevant_dimension` | Another feature of the same item, which the player must ignore, calls for a different response (the word in Stroop). |
| <span id="rule-respond-to-rule-competitor-noise-or-mask"></span>`noise_or_mask` | Noise or a mask degrades the target. |
| <span id="rule-respond-to-rule-competitor-preceding-prime"></span>`preceding_prime` | An item shown just before the target favours one response. |
| <span id="rule-respond-to-rule-competitor-previous-rule"></span>`previous_rule` | The rule that was in force a moment ago still favours its own response. |

<span id="rule-respond-to-rule-cue"></span>**Does a cue come before the target?** Rule `cue`, default `none`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-cue-none"></span>`none` | No cue comes before the target. |
| <span id="rule-respond-to-rule-cue-location-cue"></span>`location_cue` | A cue says where the target will appear. |
| <span id="rule-respond-to-rule-cue-incentive-cue"></span>`incentive_cue` | A cue says what can be won or lost on the trial. |
| <span id="rule-respond-to-rule-cue-rule-cue"></span>`rule_cue` | A cue says which rule to apply. |
| <span id="rule-respond-to-rule-cue-alerting-cue"></span>`alerting_cue` | A cue says only that the target is about to appear. |
| <span id="rule-respond-to-rule-cue-demand-probability-cue"></span>`demand_probability_cue` | A cue says how likely it is that the player will have to respond or to hold back. |
| <span id="rule-respond-to-rule-cue-feature-cue"></span>`feature_cue` | A cue gives a feature of the coming target, such as its color or shape. |

<span id="rule-respond-to-rule-reference"></span>**Is something held in mind to compare against?** Rule `reference`, default `none`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-reference-none"></span>`none` | The response depends on the present stimulus alone. |
| <span id="rule-respond-to-rule-reference-held-in-mind"></span>`held_in_mind` | The stimulus is compared with something the player keeps in memory, such as the item n steps back. |

<span id="rule-respond-to-rule-response-demand"></span>**Must the player ever hold back?** Rule `response_demand`, default `always_respond`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-response-demand-always-respond"></span>`always_respond` | The player responds on every trial. |
| <span id="rule-respond-to-rule-response-demand-withhold-on-some"></span>`withhold_on_some` | The player makes no response on some trials (no-go trials). |
| <span id="rule-respond-to-rule-response-demand-cancel-on-signal"></span>`cancel_on_signal` | The player stops a response already under way when a signal comes. |
| <span id="rule-respond-to-rule-response-demand-respond-opposite"></span>`respond_opposite` | The player responds away from the stimulus, such as looking to the side opposite it. |

<span id="rule-respond-to-rule-rule-asks"></span>**What does the rule ask about each stimulus?** Rule `rule_asks`, default `classify`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-rule-asks-classify"></span>`classify` | Say which category or feature the stimulus has. |
| <span id="rule-respond-to-rule-rule-asks-detect"></span>`detect` | Say whether a target is there. |
| <span id="rule-respond-to-rule-rule-asks-compare"></span>`compare` | Say whether the stimulus matches a reference or an earlier item. |
| <span id="rule-respond-to-rule-rule-asks-localize"></span>`localize` | Say where the stimulus is. |
| <span id="rule-respond-to-rule-rule-asks-generate"></span>`generate` | Produce an associated item, such as a verb for a noun. |
| <span id="rule-respond-to-rule-rule-asks-identify"></span>`identify` | Say which one the stimulus is, by name. |
| <span id="rule-respond-to-rule-rule-asks-count"></span>`count` | Say how many there are. |

<span id="rule-respond-to-rule-rule-source"></span>**Where does the rule come from?** Rule `rule_source`, default `instructed`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-rule-source-instructed"></span>`instructed` | The player is told the rule. |
| <span id="rule-respond-to-rule-rule-source-hidden-regularity"></span>`hidden_regularity` | A sequence or layout repeats and the player is not told. |
| <span id="rule-respond-to-rule-rule-source-learned-from-feedback"></span>`learned_from_feedback` | The player works the rule out from right-or-wrong feedback. |

<span id="rule-respond-to-rule-rule-stability"></span>**Does the rule change during play?** Rule `rule_stability`, default `fixed`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-rule-stability-fixed"></span>`fixed` | The rule stays the same throughout. |
| <span id="rule-respond-to-rule-rule-stability-shifts-unsignalled"></span>`shifts_unsignalled` | The rule changes without warning and the player finds out from feedback. |
| <span id="rule-respond-to-rule-rule-stability-switches-on-cue"></span>`switches_on_cue` | The rule changes and a cue says which rule applies. |

<span id="rule-respond-to-rule-stream"></span>**How do the stimuli arrive?** Rule `stream`, default `discrete_trials`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-stream-discrete-trials"></span>`discrete_trials` | One trial at a time, each with its own start and end, whether or not there is a pause between them. |
| <span id="rule-respond-to-rule-stream-continuous"></span>`continuous` | The stimulus runs continuously with no trial boundaries (tracking, drawing through a display). |
| <span id="rule-respond-to-rule-stream-rapid-stream"></span>`rapid_stream` | Items follow one another rapidly at one place, faster than one response per item. |

<span id="rule-respond-to-rule-target-rate"></span>**How often is there a target?** Rule `target_rate`, default `every_trial`.

| Value | Definition |
|---|---|
| <span id="rule-respond-to-rule-target-rate-every-trial"></span>`every_trial` | The main response is called for on most or all trials. |
| <span id="rule-respond-to-rule-target-rate-rare-target"></span>`rare_target` | The stimulus that calls for the main response appears on a minority of trials. |

### Study, then be tested

Rules of the game type `study_then_test`.

<span id="rule-study-then-test-cycles"></span>**How many study-test rounds?** Rule `cycles`, default `one`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-cycles-one"></span>`one` | Each set of material is studied once and tested once, however many sets there are. |
| <span id="rule-study-then-test-cycles-learn-to-criterion"></span>`learn_to_criterion` | Study and test repeat until the player reaches a set level of performance. |
| <span id="rule-study-then-test-cycles-repeated-lists"></span>`repeated_lists` | The same material is studied and tested again over several rounds. |

<span id="rule-study-then-test-inserted-judgment"></span>**Is a judgment about one's own memory added?** Rule `inserted_judgment`, default `none`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-inserted-judgment-none"></span>`none` | No judgment about the player's own memory is asked for. |
| <span id="rule-study-then-test-inserted-judgment-after-failed-recall"></span>`after_failed_recall` | After failing to recall an item, the player rates the chance of recognizing it later (feeling of knowing). |
| <span id="rule-study-then-test-inserted-judgment-at-study"></span>`at_study` | While studying, the player predicts how well each item will be remembered (judgment of learning). |

<span id="rule-study-then-test-interval-filler"></span>**What fills the interval?** Rule `interval_filler`, default `nothing`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-interval-filler-nothing"></span>`nothing` | The interval between study and test is unfilled. |
| <span id="rule-study-then-test-interval-filler-distraction"></span>`distraction` | An unrelated job fills the interval. |
| <span id="rule-study-then-test-interval-filler-interference-list"></span>`interference_list` | Another list to learn fills the interval. |

<span id="rule-study-then-test-study-and-test"></span>**Are study and test separate?** Rule `study_and_test`, default `separate`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-study-and-test-separate"></span>`separate` | Study comes first and the test follows. |
| <span id="rule-study-then-test-study-and-test-merged"></span>`merged` | Each item is both a test of earlier items and new material to keep (continuous recognition). |

<span id="rule-study-then-test-retention-interval"></span>**How long is it held?** Rule `retention_interval`, default `minutes`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-retention-interval-minutes"></span>`minutes` | The material is held for minutes. |
| <span id="rule-study-then-test-retention-interval-seconds"></span>`seconds` | The material is held for seconds. |
| <span id="rule-study-then-test-retention-interval-surprise"></span>`surprise` | The test comes unannounced; the player did not know the material would be tested. |
| <span id="rule-study-then-test-retention-interval-hours-or-days"></span>`hours_or_days` | The material is held for hours or days. |

<span id="rule-study-then-test-studied-material"></span>**What is studied?** Rule `studied_material`, default `items`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-studied-material-items"></span>`items` | Single items, such as words or pictures. |
| <span id="rule-study-then-test-studied-material-pairs"></span>`pairs` | Pairs of items to be linked. |
| <span id="rule-study-then-test-studied-material-sequence-order"></span>`sequence_order` | A sequence whose order must be kept. |
| <span id="rule-study-then-test-studied-material-items-with-context"></span>`items_with_context` | Items together with where or how each was presented. |

<span id="rule-study-then-test-study-instruction"></span>**What is the player told to remember?** Rule `study_instruction`, default `remember_all`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-study-instruction-remember-all"></span>`remember_all` | The player is told to remember everything presented. |
| <span id="rule-study-then-test-study-instruction-remember-or-forget-by-cue"></span>`remember_or_forget_by_cue` | A cue after each item or list says whether to remember it or forget it. |

<span id="rule-study-then-test-study-job"></span>**What does the player do while studying?** Rule `study_job`, default `view`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-study-job-view"></span>`view` | The player studies the material with no other job. |
| <span id="rule-study-then-test-study-job-incidental-judgment"></span>`incidental_judgment` | The player makes a judgment about each item, not knowing a test is coming. |
| <span id="rule-study-then-test-study-job-self-reference-judgment"></span>`self_reference_judgment` | The player judges whether each item describes themselves. |

<span id="rule-study-then-test-test-form"></span>**What form does the test take?** Rule `test_form`, default `cued_recall`.

| Value | Definition |
|---|---|
| <span id="rule-study-then-test-test-form-cued-recall"></span>`cued_recall` | Recall given a cue, such as one member of a studied pair. |
| <span id="rule-study-then-test-test-form-forced-choice"></span>`forced_choice` | Pick the studied item from a set of alternatives. |
| <span id="rule-study-then-test-test-form-free-recall"></span>`free_recall` | Recall as much as possible, in any order. |
| <span id="rule-study-then-test-test-form-serial-recall"></span>`serial_recall` | Recall in the order of presentation. |
| <span id="rule-study-then-test-test-form-old-new"></span>`old_new` | Say whether each item was studied. |
| <span id="rule-study-then-test-test-form-old-new-remember-know"></span>`old_new_remember_know` | Say whether each item was studied and, if so, whether it is remembered or only known. |
| <span id="rule-study-then-test-test-form-same-changed"></span>`same_changed` | Say whether a display is the same as the one studied or has changed. |
| <span id="rule-study-then-test-test-form-source-attribution"></span>`source_attribution` | Say where or how each item was studied. |

### Choose for a payoff

Rules of the game type `choose_for_outcomes`.

<span id="rule-choose-for-outcomes-contingency-cue"></span>**Does a cue say which payoffs are in force?** Rule `contingency_cue`, default `none`.

| Value | Definition |
|---|---|
| <span id="rule-choose-for-outcomes-contingency-cue-none"></span>`none` | No cue says which payoffs are in force. |
| <span id="rule-choose-for-outcomes-contingency-cue-per-trial-cue"></span>`per_trial_cue` | A cue on each trial says which payoffs are in force. |

<span id="rule-choose-for-outcomes-contingency-stability"></span>**Does what pays change?** Rule `contingency_stability`, default `fixed`.

| Value | Definition |
|---|---|
| <span id="rule-choose-for-outcomes-contingency-stability-fixed"></span>`fixed` | What each option pays stays the same throughout. |
| <span id="rule-choose-for-outcomes-contingency-stability-drifting"></span>`drifting` | What each option pays changes gradually. |
| <span id="rule-choose-for-outcomes-contingency-stability-reversal"></span>`reversal` | What the options pay is swapped at some point, without warning. |

<span id="rule-choose-for-outcomes-option-set"></span>**What are the options?** Rule `option_set`, default `k_hidden_outcome`.

| Value | Definition |
|---|---|
| <span id="rule-choose-for-outcomes-option-set-k-hidden-outcome"></span>`k_hidden_outcome` | Several options whose payoffs are learned by trying them (decks, arms). |
| <span id="rule-choose-for-outcomes-option-set-stimulus-pairs"></span>`stimulus_pairs` | Pairs of symbols whose values are learned. |
| <span id="rule-choose-for-outcomes-option-set-two-described"></span>`two_described` | Two options whose payoffs are stated. |
| <span id="rule-choose-for-outcomes-option-set-one-option-with-stop"></span>`one_option_with_stop` | One option to keep taking until the player chooses to stop (pumping a balloon). |

<span id="rule-choose-for-outcomes-outcome-knowledge"></span>**How does the player learn what pays?** Rule `outcome_knowledge`, default `experienced`.

| Value | Definition |
|---|---|
| <span id="rule-choose-for-outcomes-outcome-knowledge-experienced"></span>`experienced` | The player learns what an option pays by choosing it and seeing the outcome. |
| <span id="rule-choose-for-outcomes-outcome-knowledge-described"></span>`described` | The player is told what each option pays before choosing. |

<span id="rule-choose-for-outcomes-tradeoff"></span>**What is traded against what?** Rule `tradeoff`, default `amount_vs_risk`.

| Value | Definition |
|---|---|
| <span id="rule-choose-for-outcomes-tradeoff-amount-vs-risk"></span>`amount_vs_risk` | A bigger reward against a bigger risk of loss. |
| <span id="rule-choose-for-outcomes-tradeoff-amount-vs-effort"></span>`amount_vs_effort` | A bigger reward against more effort. |
| <span id="rule-choose-for-outcomes-tradeoff-explore-vs-exploit"></span>`explore_vs_exploit` | Trying other options against staying with the best known one, where values must be tracked. |
| <span id="rule-choose-for-outcomes-tradeoff-probability-learning"></span>`probability_learning` | Learning which option pays most often. |
| <span id="rule-choose-for-outcomes-tradeoff-amount-vs-delay"></span>`amount_vs_delay` | A bigger reward against a longer wait. |

### Play against another player

Rules of the game type `interact_with_agent`.

<span id="rule-interact-with-agent-exit-option"></span>**Can a player opt out?** Rule `exit_option`, default `none`.

| Value | Definition |
|---|---|
| <span id="rule-interact-with-agent-exit-option-none"></span>`none` | The player cannot leave the game. |
| <span id="rule-interact-with-agent-exit-option-available"></span>`available` | The player can leave the game, usually at a cost, without the other player learning of it. |

<span id="rule-interact-with-agent-move-order"></span>**In what order?** Rule `move_order`, default `sequential`.

| Value | Definition |
|---|---|
| <span id="rule-interact-with-agent-move-order-sequential"></span>`sequential` | The players move in turn and the second sees the first move. |
| <span id="rule-interact-with-agent-move-order-simultaneous"></span>`simultaneous` | The players move at the same time, without seeing the other's move. |

<span id="rule-interact-with-agent-partner"></span>**Who is the other player?** Rule `partner`, default `human`.

| Value | Definition |
|---|---|
| <span id="rule-interact-with-agent-partner-human"></span>`human` | A person, real or said to be real. |
| <span id="rule-interact-with-agent-partner-computer"></span>`computer` | A computer, known by the player to be one. |
| <span id="rule-interact-with-agent-partner-group"></span>`group` | A group of people. |

<span id="rule-interact-with-agent-players-acting"></span>**Who makes a move?** Rule `players_acting`, default `both`.

| Value | Definition |
|---|---|
| <span id="rule-interact-with-agent-players-acting-both"></span>`both` | Two players, each of whom makes a move. |
| <span id="rule-interact-with-agent-players-acting-several"></span>`several` | More than two players make a move. |

<span id="rule-interact-with-agent-repetition"></span>**Is the game played once or repeatedly?** Rule `repetition`, default `one_shot`.

| Value | Definition |
|---|---|
| <span id="rule-interact-with-agent-repetition-one-shot"></span>`one_shot` | The game is played once with a given partner. |
| <span id="rule-interact-with-agent-repetition-iterated"></span>`iterated` | The game is played repeatedly with the same partner. |

<span id="rule-interact-with-agent-transfer-transformation"></span>**Is what is sent changed on the way?** Rule `transfer_transformation`, default `none`.

| Value | Definition |
|---|---|
| <span id="rule-interact-with-agent-transfer-transformation-none"></span>`none` | What one player sends is what the other receives. |
| <span id="rule-interact-with-agent-transfer-transformation-multiplied"></span>`multiplied` | What one player sends is multiplied before the other receives it. |

### Watch or listen

Rules of the game type `undergo_stream`.

<span id="rule-undergo-stream-instruction"></span>**What is the player told to do while it runs?** Rule `instruction`, default `attend`.

| Value | Definition |
|---|---|
| <span id="rule-undergo-stream-instruction-attend"></span>`attend` | The player is told to attend to the stream; covers 'simply view' and 'listen'. |
| <span id="rule-undergo-stream-instruction-none"></span>`none` | The player is told to ignore the stream or is given no instruction about it. |
| <span id="rule-undergo-stream-instruction-regulate"></span>`regulate` | The player is told to change their emotional response to the stream. |
| <span id="rule-undergo-stream-instruction-incidental-judgment"></span>`incidental_judgment` | The player is given a job that does not ask about the property being studied. |

<span id="rule-undergo-stream-report-after"></span>**Is anything asked afterwards?** Rule `report_after`, default `rating`.

| Value | Definition |
|---|---|
| <span id="rule-undergo-stream-report-after-rating"></span>`rating` | A rating, such as of fear, expectancy or pleasantness. |
| <span id="rule-undergo-stream-report-after-comprehension-question"></span>`comprehension_question` | A question about what was read or heard. |
| <span id="rule-undergo-stream-report-after-none"></span>`none` | Nothing is asked afterwards. |
| <span id="rule-undergo-stream-report-after-judgment"></span>`judgment` | A judgment about the content, such as how strongly one thing causes another. |

## Game motivators

Why the player tries. Every task answers the first question; the others are answered where they apply.

<span id="motivator-drive"></span>**Why does the player try?** Key `drive`. Every task answers it.

| Value | Definition |
|---|---|
| <span id="motivator-drive-instructions-only"></span>`instructions_only` | The player tries because they were asked to; nothing is won or lost. |
| <span id="motivator-drive-reward-goal"></span>`reward_goal` | Obtaining a reward or avoiding a loss is what the game is about. |
| <span id="motivator-drive-reward-stake"></span>`reward_stake` | A reward or loss is attached to performing well at a game that is about something else. |
| <span id="motivator-drive-unearned-outcome"></span>`unearned_outcome` | Something pleasant or unpleasant is delivered whatever the player does. |
| <span id="motivator-drive-instructed-emphasis"></span>`instructed_emphasis` | The instruction puts one of speed or accuracy first. The ordinary 'as fast and as accurately as you can' is `instructions_only`. |

<span id="motivator-sign"></span>**Can the player gain, lose, or both?** Key `sign`.

| Value | Definition |
|---|---|
| <span id="motivator-sign-gain"></span>`gain` | The player can only gain. |
| <span id="motivator-sign-loss"></span>`loss` | The player can only lose or receive something unpleasant. |
| <span id="motivator-sign-both"></span>`both` | The player can gain and can lose. |

<span id="motivator-earned-by"></span>**What earns the outcome?** Key `earned_by`.

| Value | Definition |
|---|---|
| <span id="motivator-earned-by-choice"></span>`choice` | The option the player chooses. |
| <span id="motivator-earned-by-performance"></span>`performance` | How fast or how accurately the player responds. |
| <span id="motivator-earned-by-joint-moves"></span>`joint_moves` | The player's move together with another player's move. |
| <span id="motivator-earned-by-nothing"></span>`nothing` | Nothing the player does; the outcome is delivered regardless. |

<span id="motivator-what"></span>**What is the outcome?** Key `what`.

| Value | Definition |
|---|---|
| <span id="motivator-what-money"></span>`money` | Money. |
| <span id="motivator-what-points"></span>`points` | Points with no stated money value. |
| <span id="motivator-what-food"></span>`food` | Food or drink. |
| <span id="motivator-what-social"></span>`social` | Approval, disapproval or another social outcome. |
| <span id="motivator-what-aversive"></span>`aversive` | An unpleasant stimulus, such as a shock or a loud noise. |
| <span id="motivator-what-effort-cost"></span>`effort_cost` | Effort the player must spend. |
| <span id="motivator-what-signal-only"></span>`signal_only` | A signal of right or wrong, or of win or loss, with nothing behind it. |

<span id="motivator-real"></span>**Is the outcome real?** Key `real`.

| Value | Definition |
|---|---|
| <span id="motivator-real-paid"></span>`paid` | The outcome is delivered or paid. |
| <span id="motivator-real-hypothetical"></span>`hypothetical` | The player is asked to choose as if the outcome were real. |

## Game phases

Named parts of a game beyond the structure its game type already has, which a study
reports separately. A task with no such part names no phase.

| Phase | Definition |
|---|---|
| <span id="phase-acquisition"></span>`acquisition` | The phase in which a relation is first learned. |
| <span id="phase-extinction"></span>`extinction` | The learned relation is no longer in force: the cue comes without its outcome. |
| <span id="phase-transfer"></span>`transfer` | What was learned is tested on new material or under new conditions. |
| <span id="phase-devaluation"></span>`devaluation` | An outcome is made less valuable before responding is tested. |
| <span id="phase-test"></span>`test` | A later phase that measures what was learned, with no further learning intended. |

## Game facets

How the game is delivered: what the participant sees, uses and is, recorded as values
that are present (there are no 'none' values). There are 9 facets. The HED
tags column gives the tags a value corresponds to.

### Stimulus modality

<span id="facet-stimulus-modality"></span>**Which sense does the stimulus reach?** Facet `stimulus_modality`.

Which sense the stimulus reaches. One value per sense. A task that presents in two senses at once (a sound and a picture) lists both. The values are the seven children of the HED Sensory-presentation tag.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-stimulus-modality-visual"></span>`visual` | Seen with the eyes. | `Visual-presentation` Exact tag. |
| <span id="facet-stimulus-modality-auditory"></span>`auditory` | Heard with the ears. | `Auditory-presentation` Exact tag. |
| <span id="facet-stimulus-modality-tactile"></span>`tactile` | Felt through the skin by touch. | `Tactile-presentation` Exact tag. |
| <span id="facet-stimulus-modality-somatic"></span>`somatic` | Felt through the body's nervous system other than by touch: pain, heat, electrical stimulation, and signals from inside the body such as the heartbeat. | `Somatic-presentation` Exact tag; HED's definition is 'the nervous system is used in the presentation'. |
| <span id="facet-stimulus-modality-vestibular"></span>`vestibular` | Felt as balance or body motion (tilting, rotating the participant). | `Vestibular-presentation` Exact tag. |
| <span id="facet-stimulus-modality-olfactory"></span>`olfactory` | Smelled. | `Olfactory-presentation` Exact tag. |
| <span id="facet-stimulus-modality-gustatory"></span>`gustatory` | Tasted. | `Gustatory-presentation` Exact tag. |

### Stimulus type

<span id="facet-stimulus-type"></span>**What is the stimulus made of?** Facet `stimulus_type`.

What kind of thing is shown, played or delivered: words, faces, tones, pictures, shapes, and so on. This is about what the stimulus is, not which sense it reaches (that is stimulus_modality), though the two overlap in practice: a tone is always auditory.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-stimulus-type-words"></span>`words` | Real words, printed or spoken. | `Word` Exact tag. |
| <span id="facet-stimulus-type-letters"></span>`letters` | Single letters of an alphabet. | `Character` Nearest tag; HED's Letter means a piece of correspondence. |
| <span id="facet-stimulus-type-digits"></span>`digits` | Single digits 0 to 9. | `Character` Nearest tag; HED has no digit item. |
| <span id="facet-stimulus-type-syllables"></span>`syllables` | Single spoken syllables. | `Syllable` Exact tag. |
| <span id="facet-stimulus-type-pseudowords"></span>`pseudowords` | Made-up pronounceable non-words. | `Pseudoword` Exact tag. |
| <span id="facet-stimulus-type-text"></span>`text` | Language longer than a single word - a phrase, a sentence or a passage of any length, written or spoken; stimulus_modality says which. | `Sentence`, `Textblock` Sentence for one sentence, Textblock for longer text (both exact). |
| <span id="facet-stimulus-type-asian-characters"></span>`asian_characters` | Chinese, Japanese or Korean characters. | `Character` Nearest tag; no script distinction. |
| <span id="facet-stimulus-type-false-fonts"></span>`false_fonts` | Letter-like shapes that are not letters. | `Glyph` Nearest tag. |
| <span id="facet-stimulus-type-symbols"></span>`symbols` | Signs such as arrows, plus signs, asterisks. | `Glyph`, `Arrow` Glyph in general; Arrow for arrows (exact). |
| <span id="facet-stimulus-type-shapes"></span>`shapes` | Simple outlines: circles, squares, triangles. | `2D-shape` Exact tag; its children name the shapes. |
| <span id="facet-stimulus-type-abstract-patterns"></span>`abstract_patterns` | Complex geometric patterns with no meaning. | `Pattern` Exact tag. |
| <span id="facet-stimulus-type-pictures"></span>`pictures` | Drawings, paintings or photographs of things. | `Image` Exact tag; Photograph, Drawing, Painting and Cartoon are its children. |
| <span id="facet-stimulus-type-scenes"></span>`scenes` | Photographs or renderings of a place. | `Photograph` Nearest tag; HED has no scene item. |
| <span id="facet-stimulus-type-faces"></span>`faces` | Human faces. | `Face` Exact tag. |
| <span id="facet-stimulus-type-film-clips"></span>`film_clips` | Short videos. | `Video-clip` Exact tag. |
| <span id="facet-stimulus-type-real-objects"></span>`real_objects` | Real objects given to the participant to hold or handle. | `3D-shape` Nearest tag; HED means a geometric solid. |
| <span id="facet-stimulus-type-points-of-light"></span>`points_of_light` | Dots placed on a moving body to show motion without form. | `Point-light-visualization`, `Dots` Point-light-visualization is exact for biological motion; Dots otherwise. |
| <span id="facet-stimulus-type-random-dots"></span>`random_dots` | Fields of many dots, often moving. | `Dots` Exact tag. |
| <span id="facet-stimulus-type-fractals"></span>`fractals` | Self-similar patterns. | `Pattern` Nearest tag. |
| <span id="facet-stimulus-type-flashing-checkerboard"></span>`flashing_checkerboard` | A checkerboard whose squares swap color at a set rate. | `Pattern` Nearest tag. |
| <span id="facet-stimulus-type-game-objects"></span>`game_objects` | Cards, dice, tokens, pegs, blocks, discs or boards used to play a game or puzzle, real or on a screen. Covers Wisconsin Card Sorting, Iowa Gambling, Wason Selection, Weather Prediction cards, Tower of London and Hanoi, Corsi blocks. | `Game-object` Proposed for HED 8.6.0 (agreed 2026-11-06, Kay to add). |
| <span id="facet-stimulus-type-value-amounts"></span>`value_amounts` | An amount of money, points, tokens or other worth, shown as a number, a score, coins or bills; offered, won or lost. | `Quantity/# dollar`, `Quantity/# euro`, `Quantity/# point` Quantity takes any unit, and the worth units are dollar, euro and point. The role is Reward or Penalty. No new tag needed. |
| <span id="facet-stimulus-type-food"></span>`food` | Something to eat or drink. | `Ingestible-object` Exact tag. |
| <span id="facet-stimulus-type-tones"></span>`tones` | Pure tones of one frequency. | `Tone` Exact tag. |
| <span id="facet-stimulus-type-clicks"></span>`clicks` | Brief ticks. | `Click` Exact tag. |
| <span id="facet-stimulus-type-chord-sequences"></span>`chord_sequences` | Musical chords. | `Musical-sound` Nearest tag. |
| <span id="facet-stimulus-type-music"></span>`music` | Music. | `Musical-sound` Exact tag. |
| <span id="facet-stimulus-type-noise"></span>`noise` | Broadband noise. | `Signal-noise` Exact tag. |
| <span id="facet-stimulus-type-nonverbal-vocal-sounds"></span>`nonverbal_vocal_sounds` | Laughs, cries, screams, sighs. | `Vocalized-sound` Exact tag. |
| <span id="facet-stimulus-type-nonvocal-sounds"></span>`nonvocal_sounds` | Sounds of animals, machines, nature. | `Environmental-sound` Exact tag. |
| <span id="facet-stimulus-type-reversed-speech"></span>`reversed_speech` | Speech played backwards. | `Vocalized-sound` Nearest tag. |
| <span id="facet-stimulus-type-odor"></span>`odor` | A smell. | No standard tag; catalog only. |
| <span id="facet-stimulus-type-braille-dots"></span>`braille_dots` | Braille read by touch. | `Braille` Exact tag. |
| <span id="facet-stimulus-type-thermal"></span>`thermal` | Heat or cold applied to the skin. | `Tactile-temperature` Exact tag, with Hot or Cold as the level. |
| <span id="facet-stimulus-type-vibration"></span>`vibration` | Vibration applied to the skin. | `Tactile-vibration` Exact tag. |
| <span id="facet-stimulus-type-pressure"></span>`pressure` | Touch or pressure on the skin, including an air puff. | `Tactile-pressure` Exact tag, with High or Low as the level. |
| <span id="facet-stimulus-type-texture"></span>`texture` | A surface felt for roughness or pattern. | `Tactile-texture` Exact tag. |
| <span id="facet-stimulus-type-electrical"></span>`electrical` | An electric current applied to the skin. | `Tactile-electrical` Proposed for HED 8.6.0 (agreed 2026-11-06, Kay to add); intensity is High or Low, a painful shock adds Pain. |
| <span id="facet-stimulus-type-pain"></span>`pain` | A stimulus delivered to hurt, whatever produces it. | `Pain` Exact tag, under Somatic-attribute. |

### Emotional aspect

<span id="facet-emotional-aspect"></span>**How is emotion built into the experiment?** Facet `emotional_aspect`.

How emotion is built into the experiment, if it is. The facet says that an emotional aspect is present and in what form, at the design level. Which emotion is involved is not a value: HED has the tags for that (Agent-emotional-state children, and Threat), and they go on the events.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-emotional-aspect-emotional-stimuli"></span>`emotional_stimuli` | The stimuli themselves carry emotion: faces, words, pictures, film clips chosen for their emotional content. | No standard tag for the design; the emotion goes on the event (Agent-emotional-state child, Threat). Catalog only. |
| <span id="facet-emotional-aspect-emotion-induction"></span>`emotion_induction` | A mood or state is induced before or during the task: a film, music, autobiographical recall, a stress procedure, threat of shock. | No standard tag for the design; the induced state goes on the participant. Catalog only. |
| <span id="facet-emotional-aspect-explicit-emotion-task"></span>`explicit_emotion_task` | The participant's job is about the emotion, as against the implicit version where the same emotional stimuli are judged for something else (gender, color). | No standard tag; catalog only. |
| <span id="facet-emotional-aspect-regulation-instruction"></span>`regulation_instruction` | The participant is told to change their emotional response: reappraise, suppress, distance. | No standard tag; catalog only. |

### Social aspect

<span id="facet-social-aspect"></span>**How are other people built into the experiment?** Facet `social_aspect`.

How other people are built into the experiment, if they are. As with emotion, the facet says the aspect is present and in what form; who the people are and what they do goes on the events.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-social-aspect-social-stimuli"></span>`social_stimuli` | The stimuli depict people as people: faces, bodies, interactions, eyes to read. | No standard tag; catalog only. |
| <span id="facet-social-aspect-social-interaction"></span>`social_interaction` | A real or simulated other person takes part: a partner or opponent, a confederate, a computer agent presented as a person. | No standard tag; catalog only. |
| <span id="facet-social-aspect-being-observed"></span>`being_observed` | The participant is watched or judged while doing the task: an audience, an observer, being recorded. | No standard tag; catalog only. |
| <span id="facet-social-aspect-explicit-social-task"></span>`explicit_social_task` | The participant's job is about the people: judge trustworthiness, infer what someone thinks or feels, rate attractiveness. The implicit version judges the same stimuli for something else (age, gender). | No standard tag; catalog only. |

### Task I/O device

<span id="facet-task-io-device"></span>**What equipment delivers the task and collects the response?** Facet `task_io_device`.

The equipment the task is delivered on and the response is collected through: the screen and keyboard of a computer task, a button box, a touchscreen tablet, a microphone for spoken answers, an eye tracker, a pen and paper. A task lists every device it has been run with. Values come from HED's IO-device tree plus Writing-device.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-task-io-device-keyboard"></span>`keyboard` | A full computer keyboard. | `Keyboard` Exact tag. |
| <span id="facet-task-io-device-keypad"></span>`keypad` | A small block of keys. | `Keypad` Exact tag. |
| <span id="facet-task-io-device-button-box"></span>`button_box` | A response box with one or more buttons. | `Push-button` Exact tag. |
| <span id="facet-task-io-device-mouse"></span>`mouse` | A computer mouse. | `Computer-mouse` Exact tag. |
| <span id="facet-task-io-device-touchscreen"></span>`touchscreen` | A touch-sensitive screen, including phones and tablets. | `Touchscreen` Exact tag. |
| <span id="facet-task-io-device-joystick"></span>`joystick` | A joystick or similar handle. | `Joystick` Exact tag. |
| <span id="facet-task-io-device-pedal"></span>`pedal` | A foot pedal or foot switch. | `Pedal` Proposed for HED 8.6.0 under Input-device. |
| <span id="facet-task-io-device-stylus"></span>`stylus` | A pen-like pointer on a tablet or digitizer. | `Stylus` Proposed for HED 8.6.0 under Input-device. |
| <span id="facet-task-io-device-writing-device"></span>`writing_device` | A pen or pencil on paper. | `Writing-device` Exact tag; Pen and Pencil are its children. |
| <span id="facet-task-io-device-microphone"></span>`microphone` | Records spoken answers. | `Microphone` Exact tag. |
| <span id="facet-task-io-device-eye-tracker"></span>`eye_tracker` | Records gaze position. | `Eye-tracker` Proposed for HED 8.6.0 under Recording-device. |
| <span id="facet-task-io-device-motion-capture"></span>`motion_capture` | Records limb or body movement. | `Motion-capture` Exact tag. |
| <span id="facet-task-io-device-computer-screen"></span>`computer_screen` | A monitor or laptop screen. | `Computer-screen` Exact tag. |
| <span id="facet-task-io-device-head-mounted-display"></span>`head_mounted_display` | A headset display, as in virtual reality. | `Head-mounted-display` Exact tag. |
| <span id="facet-task-io-device-headphones"></span>`headphones` | Sound through headphones. | `Headphones` Exact tag. |
| <span id="facet-task-io-device-loudspeaker"></span>`loudspeaker` | Sound through a speaker. | `Loudspeaker` Exact tag. |
| <span id="facet-task-io-device-examiner"></span>`examiner` | A person presents the items and records the answers, with no equipment between examiner and participant. | No standard tag; catalog only. |
| <span id="facet-task-io-device-handheld-controller"></span>`handheld_controller` | A hand-held game or virtual-reality controller. | No standard tag; catalog only. |
| <span id="facet-task-io-device-brain-stimulator"></span>`brain_stimulator` | A device that stimulates the brain directly, such as a transcranial magnetic stimulation coil. | No standard tag; catalog only. |
| <span id="facet-task-io-device-stereoscopic-display"></span>`stereoscopic_display` | A display that shows each eye its own image, such as a stereoscope or shutter glasses. | No standard tag; catalog only. |
| <span id="facet-task-io-device-grip-force-device"></span>`grip_force_device` | A hand grip that measures how hard the participant squeezes. | No standard tag; catalog only. |

### Trial structure

<span id="facet-trial-structure"></span>**How is the run of trials delivered?** Facet `trial_structure`.

How the run of trials is delivered to the participant: one trial after another at a set pace, or when the participant is ready, or as an unbroken stream; conditions kept apart in blocks or mixed together; difficulty fixed or tracking performance. A task lists every form the literature reports.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-trial-structure-continuous-recording"></span>`continuous_recording` | No trial boundaries: a stream of stimuli or a continuous task, with responses recorded throughout. | `Continuous` Temporal attribute. |
| <span id="facet-trial-structure-fixed-time-trials"></span>`fixed_time_trials` | Trials come at a set pace with fixed timing, whatever the participant does. | `Discrete` Nearest tag; Discrete is a temporal attribute. |
| <span id="facet-trial-structure-self-paced-trials"></span>`self_paced_trials` | The participant starts each trial when ready. | No standard tag; catalog only. |
| <span id="facet-trial-structure-blocked-trials"></span>`blocked_trials` | Each condition is run in its own block of trials. | No standard tag; catalog only (Time-block and Condition-variable mark runs in a dataset). |
| <span id="facet-trial-structure-interleaved-trials"></span>`interleaved_trials` | Conditions are mixed trial by trial within a block. | No standard tag; catalog only. |
| <span id="facet-trial-structure-adaptive-trials"></span>`adaptive_trials` | Difficulty changes with the participant's performance, as in a staircase. | No standard tag; catalog only. |

### Feedback

<span id="facet-feedback"></span>**Does the participant learn how they did, and when?** Facet `feedback`.

Whether the participant finds out how they did, and when. A task that gives no feedback has no value here. Some say right or wrong after every trial; some show a score at the end of a block.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-feedback-trial-feedback"></span>`trial_feedback` | Right or wrong after each trial. | `Feedback`, `Correct-action`, `Incorrect-action` Exact tags: Feedback with Correct-action or Incorrect-action. |
| <span id="facet-feedback-block-feedback"></span>`block_feedback` | A score or summary at the end of a run. | `Feedback` Exact tag; HED has no tag for the timing. |

### Experimental environment

<span id="facet-experimental-environment"></span>**Where is the participant while doing the task?** Facet `experimental_environment`.

Where the participant is while doing the task. The ordinary lab setting is the default and gets no value. The values come from HED's Environmental-property list.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-experimental-environment-virtual-world"></span>`virtual_world` | An immersive computer-generated scene, usually through a headset. | `Virtual-world` Exact tag. |
| <span id="facet-experimental-environment-augmented-reality"></span>`augmented_reality` | Digital overlays on the real surroundings. | `Augmented-reality` Exact tag. |
| <span id="facet-experimental-environment-real-world"></span>`real_world` | Carried out in daily life under realistic conditions: an errand, a phone call to make. | `Real-world` Exact tag. |
| <span id="facet-experimental-environment-outdoors"></span>`outdoors` | Outside a building, as in walking or navigation versions. | `Outdoors` Exact tag. |

### Population

<span id="facet-population"></span>**Who is there a version for?** Facet `population`.

Who the task has a version for. This facet records that such a version exists, not who was tested in any dataset. The standard young-adult form is stated in the positive, so every task carries at least one value. Age ranges are approximate because papers draw the lines differently.

| Value | Definition | HED tags |
|---|---|---|
| <span id="facet-population-infants"></span>`infants` | A version for infants, under about 2 years, usually measured by looking time. | No standard tag; catalog only. |
| <span id="facet-population-children"></span>`children` | A version for children, about 2 to 12 years: simpler instructions, fewer trials, child-friendly stimuli. | No standard tag; catalog only. |
| <span id="facet-population-adolescents"></span>`adolescents` | A version for adolescents, about 13 to 17 years. | No standard tag; catalog only. |
| <span id="facet-population-young-adults"></span>`young_adults` | The standard form, about 18 to 30 years, typically college-age participants. | No standard tag; catalog only. |
| <span id="facet-population-adults"></span>`adults` | A version for adults of about 31 to 59 years. | No standard tag; catalog only. |
| <span id="facet-population-older-adults"></span>`older_adults` | A version for older adults, about 60 years and over. | No standard tag; catalog only. |
| <span id="facet-population-patients"></span>`patients` | A version adapted for a clinical group of any age, such as shortened or simplified for patients. | No standard tag; catalog only (Sick is a state, not an adaptation). |
| <span id="facet-population-bilinguals"></span>`bilinguals` | A version for people who use two languages. | No standard tag; catalog only. |

## Settings

Quantities a study chooses when it runs the game. A task model names them; a model of
the task in one paper gives their values.

| Setting | Definition |
|---|---|
| <span id="setting-retention-interval"></span>`retention_interval` | Time between study and test, or sample and probe. |
| <span id="setting-stimulus-onset-asynchrony"></span>`stimulus_onset_asynchrony` | Time from one stimulus onset to the next (prime to target, cue to target, task 1 to task 2). |
| <span id="setting-presentation-duration"></span>`presentation_duration` | How long a stimulus is shown. |
| <span id="setting-reward-magnitude"></span>`reward_magnitude` | Size of a reward, loss, endowment or stake. |
| <span id="setting-block-duration"></span>`block_duration` | Length of a block or run. |
| <span id="setting-set-size"></span>`set_size` | Number of items in a display, memory set or option set. |
| <span id="setting-number-of-alternatives"></span>`number_of_alternatives` | Response options or choice alternatives. |
| <span id="setting-list-length"></span>`list_length` | Number of items in a studied list or sequence. |
| <span id="setting-number-of-trials"></span>`number_of_trials` | Trials per block or in total. |
| <span id="setting-target-probability"></span>`target_probability` | How often the target or rare item appears. |
| <span id="setting-stimulus-similarity"></span>`stimulus_similarity` | Target-distractor or lure-target similarity. |
| <span id="setting-response-deadline"></span>`response_deadline` | Time allowed to respond. |
| <span id="setting-number-of-repetitions"></span>`number_of_repetitions` | How many times a list or sequence is presented. |
| <span id="setting-interstimulus-interval"></span>`interstimulus_interval` | Blank time between two stimuli. |
| <span id="setting-number-of-targets"></span>`number_of_targets` | Targets per display or stream. |
| <span id="setting-reward-probability"></span>`reward_probability` | Chance an option pays off. |
| <span id="setting-stimulus-intensity"></span>`stimulus_intensity` | Contrast, loudness, coherence, signal-to-noise, noise density. |
| <span id="setting-presentation-rate"></span>`presentation_rate` | Items per second in a stream. |
| <span id="setting-proportion-congruent"></span>`proportion_congruent` | Share of congruent or valid or related trials (cue validity, relatedness proportion). |
| <span id="setting-feedback-reliability"></span>`feedback_reliability` | Share of feedback that is correct. |
| <span id="setting-delay-to-outcome"></span>`delay_to_outcome` | Time until a reward or outcome is delivered. |
| <span id="setting-eccentricity"></span>`eccentricity` | Distance from fixation. |
| <span id="setting-spatial-separation"></span>`spatial_separation` | Distance between items or sources. |
| <span id="setting-session-duration"></span>`session_duration` | Length of the whole session, or number of sessions. |
| <span id="setting-number-of-distractors"></span>`number_of_distractors` | Distractors per display. |
| <span id="setting-viewpoint-angle"></span>`viewpoint_angle` | Rotation or viewing angle. |
| <span id="setting-number-of-rules"></span>`number_of_rules` | Number of relational rules to integrate. |

## Ways of combining games

How a second game is played alongside the main one.

| Way | Definition |
|---|---|
| <span id="how-in-quick-succession"></span>`in_quick_succession` | The second game's stimulus follows the first's so closely that the two responses overlap. |
| <span id="how-throughout"></span>`throughout` | The second game runs for the whole of the main game (holding fixation, a concurrent load). |
| <span id="how-interleaved"></span>`interleaved` | Trials of the two games alternate or are mixed. |
| <span id="how-inserted"></span>`inserted` | The second game is placed inside each trial or between the phases of the main game. |
| <span id="how-chained"></span>`chained` | The outcome of one game is the starting point of the next. |
