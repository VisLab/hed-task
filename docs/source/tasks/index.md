# Tasks

The task catalog holds 110 traditional cognitive and behavioral neuroscience tasks, the
starting point of the HED task models. They were drawn from the Cognitive Atlas, with gaps
filled from the literature, and each is modeled as a game. Each task page gives the canonical
name and aliases, a description, the game model of the standard form of the task (its game
type, rules, motivators, phases and facets, in the terms of the
[game vocabulary](vocabulary.md)), the inclusion test that decides whether an experiment is
an instance of the task, its variants, the cognitive processes it engages, and references.
[The task model](../task_model.md) explains the parts.

Tasks are filed under 20 **task families** by what the participant does,
not by which process the task is thought to measure. The list of cognitive processes covers that
other axis, and the two cross-link. Families are organizational, not a hierarchy. Every
task has one **primary** family, where its page is filed, and may be cross-listed under
others as a **secondary** member; 15 tasks are cross-listed at present. The
assignments are curation decisions and are expected to change as the task catalog grows;
15 memberships are marked `review`. The
[task family assignment rules](../methods/task_criteria/06_task_family_assignment.md)
say how families are assigned.

A `review` mark means the assignment is a judgement call the curator has flagged for a
second opinion. On the family an entry is filed under it means "not sure this is the right
home"; on a cross-listing it means "not sure this belongs here at all". The note names
the alternative or the doubt. Comments go to the
[issue tracker](https://github.com/hed-standard/hed-task/issues).

Ways in:

- [Tasks by family](tasks_by_family.md) lists every task under its family, with the
  family's scope statement.
- [Tasks alphabetically](tasks_alphabetically.md) lists every task in name order, for when you
  know the name and not the family.
- [Tasks by game type](by_game_type.md) lists the tasks under the game their standard form is.
- [Tasks by facet](by_facet.md) lists, for each facet value, the tasks and variants that carry it.
- The [game vocabulary](vocabulary.md) defines every game type, rule, motivator, phase and facet
  value used on the task pages, with the settings and the ways of combining games.

## Families at a glance

| Family | Tasks filed | Cross-listed |
|---|---|---|
| [Conflict and interference tasks](families/conflict_and_interference.md) | 8 | 2 |
| [Response inhibition and stopping tasks](families/response_inhibition.md) | 5 | - |
| [Attentional cueing and orienting tasks](families/attentional_cueing.md) | 3 | 1 |
| [Visual search and tracking tasks](families/visual_search_and_tracking.md) | 4 | 2 |
| [Oddball, vigilance and continuous performance tasks](families/oddball_and_vigilance.md) | 6 | 1 |
| [Perceptual judgment and psychophysics tasks](families/perceptual_judgment.md) | 5 | 3 |
| [Short-term and working memory tasks](families/working_memory_span.md) | 8 | - |
| [Recall and recognition memory tests](families/recall_and_recognition.md) | 9 | - |
| [Memory control and prospective memory tasks](families/memory_control.md) | 4 | - |
| [Metacognition, agency and interoception tasks](families/metacognition_and_interoception.md) | 5 | - |
| [Conditioning, reinforcement and implicit learning tasks](families/conditioning_and_reinforcement.md) | 10 | 1 |
| [Motor performance and speeded response tasks](families/motor_performance.md) | 5 | 2 |
| [Rule use, planning and reasoning tasks](families/executive_and_reasoning.md) | 8 | - |
| [Reward, risk and value-based choice tasks](families/reward_and_value_choice.md) | 6 | - |
| [Social cognition and social choice tasks](families/social_cognition_and_games.md) | 6 | 1 |
| [Emotion elicitation and regulation tasks](families/emotion.md) | 4 | - |
| [Language comprehension and production tasks](families/language.md) | 9 | 1 |
| [Spatial cognition and navigation tasks](families/spatial_navigation.md) | 3 | - |
| [Spontaneous thought tasks](families/spontaneous_thought.md) | 1 | 1 |
| [Self-report tasks](families/self_report.md) | 1 | 2 |

```{toctree}
:hidden:
:maxdepth: 3

Tasks by family <tasks_by_family>
Tasks alphabetically <tasks_alphabetically>
Tasks by game type <by_game_type>
Tasks by facet <by_facet>
Game vocabulary <vocabulary>
```
