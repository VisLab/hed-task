(associative_learning_and_reinforcement)=
# Associative Learning and Reinforcement

**Scope:** Learning of stimulus-stimulus, stimulus-response, and action-outcome contingencies under reinforcement; Pavlovian and instrumental conditioning; extinction; reversal; model-based and model-free reinforcement learning; reward prediction error.

**Out of scope:** Structure learning without scalar reinforcement (that is Implicit and Statistical Learning).

This category contains 13 processes.

| Process | Definition | Tasks |
|---|---|---|
| [Associative learning](#hed-associative-learning) | Learning of co-occurrence relations between stimuli or between stimuli and responses. | 7 |
| [Extinction](#hed-extinction) | Decrease in a previously reinforced response when reinforcement is withheld; a form of new inhibitory learning rather th... | 1 |
| [Goal-directed behavior](#hed-goal-directed-behavior) | Behavior that is sensitive to current outcome value, characteristic of action–outcome learning. | 1 |
| [Habit](#hed-habit) | Behavior that is insensitive to the current value of its outcome, characteristic of stimulus–response learning. | 1 |
| [Instrumental conditioning](#hed-instrumental-conditioning) | Learning that an action produces an outcome; also called operant conditioning. Encompasses both goal-directed (action–ou... | 1 |
| [Model-based learning](#hed-model-based-learning) | Reinforcement learning that uses an internal model of the environment's transition and reward structure to plan. | 1 |
| [Model-free learning](#hed-model-free-learning) | Reinforcement learning from cached value estimates updated by prediction errors, without an explicit model of the enviro... | 1 |
| [Pavlovian conditioning](#hed-pavlovian-conditioning) | Learning that a neutral stimulus predicts a biologically significant outcome, leading to conditioned responding. | 1 |
| [Policy learning](#hed-policy-learning) | Direct learning of a mapping from states to actions without necessarily estimating values. | 0 |
| [Reinforcement learning](#hed-reinforcement-learning) | Learning to select actions that maximize cumulative reward through experience with reward prediction errors. | 7 |
| [Reversal learning](#hed-reversal-learning) | Relearning after contingencies between stimuli (or responses) and outcomes are switched. | 1 |
| [Reward prediction error](#hed-reward-prediction-error) | Signed difference between received and expected reward, instantiated by phasic midbrain dopamine firing. | 7 |
| [Value learning](#hed-value-learning) | Acquisition of the expected value of stimuli, actions, or states from experience with outcomes. | 2 |

(hed-associative-learning)=
## Associative learning

**Process ID:** `hed_associative_learning`

Learning of co-occurrence relations between stimuli or between stimuli and responses.

**Tasks that engage this process:** [Causal Learning Task](../tasks/hedtsk_causal_learning.md), [Contextual Cueing Task](../tasks/hedtsk_contextual_cueing.md), [Digit Symbol Substitution Task](../tasks/hedtsk_digit_symbol_substitution.md), [Implicit Association Task](../tasks/hedtsk_implicit_association.md), [Paired Associates Learning Task](../tasks/hedtsk_paired_associates_learning.md), [Pavlovian Fear Conditioning Task](../tasks/hedtsk_pavlovian_fear_conditioning.md), [Probabilistic Classification Learning Task](../tasks/hedtsk_probabilistic_classification_learning.md)

**Further references**

- Shanks (2010) *Annual Review of Psychology* 61:273–301 ([DOI](https://doi.org/10.1146/annurev.psych.093008.100422))

(hed-extinction)=
## Extinction

**Process ID:** `hed_extinction`

**Also known as:** extinction learning

Decrease in a previously reinforced response when reinforcement is withheld; a form of new inhibitory learning rather than erasure.

**Tasks that engage this process:** [Pavlovian Fear Conditioning Task](../tasks/hedtsk_pavlovian_fear_conditioning.md)

**Fundamental references**

- Pavlov (1927) *Conditioned reflexes* Oxford University Press
- Bouton (2004) *Learning & Memory* 11:485–494 ([DOI](https://doi.org/10.1101/lm.78804), [PubMed](https://pubmed.ncbi.nlm.nih.gov/15466298/))

**Further references**

- Dunsmoor, Niv, Daw & Phelps (2015) *Neuron* 88:47–63 ([DOI](https://doi.org/10.1016/j.neuron.2015.09.028), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26447572/))

(hed-goal-directed-behavior)=
## Goal-directed behavior

**Process ID:** `hed_goal_directed_behavior`

**Also known as:** goal-directed action

Behavior that is sensitive to current outcome value, characteristic of action–outcome learning.

**Tasks that engage this process:** [Instrumental Conditioning Task](../tasks/hedtsk_instrumental_conditioning.md)

**Fundamental references**

- Dickinson & Balleine (1994) *Animal Learning & Behavior* 22:1–18 ([DOI](https://doi.org/10.3758/bf03199951))

**Further references**

- Balleine & O'Doherty (2010) *Neuropsychopharmacology* 35:48–69 ([DOI](https://doi.org/10.1038/npp.2009.131), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19776734/))

(hed-habit)=
## Habit

**Process ID:** `hed_habit`

**Also known as:** habit learning

Behavior that is insensitive to the current value of its outcome, characteristic of stimulus–response learning.

**Tasks that engage this process:** [Instrumental Conditioning Task](../tasks/hedtsk_instrumental_conditioning.md)

**Further references**

- Balleine & O'Doherty (2010) *Neuropsychopharmacology* 35:48–69 ([DOI](https://doi.org/10.1038/npp.2009.131), [PubMed](https://pubmed.ncbi.nlm.nih.gov/19776734/))

(hed-instrumental-conditioning)=
## Instrumental conditioning

**Process ID:** `hed_instrumental_conditioning`

**Also known as:** **Operant conditioning** - Skinnerian terminology; emphasizes the operant response and reinforcement schedules.

Learning that an action produces an outcome; also called operant conditioning. Encompasses both goal-directed (action–outcome) and habitual (stimulus–response) control, studied via reinforcement schedules and outcome-devaluation procedures.

**Tasks that engage this process:** [Instrumental Conditioning Task](../tasks/hedtsk_instrumental_conditioning.md)

**Further references**

- Staddon & Cerutti (2003) *Annual Review of Psychology* 54:115–144 ([DOI](https://doi.org/10.1146/annurev.psych.54.101601.145124))

(hed-model-based-learning)=
## Model-based learning

**Process ID:** `hed_model_based_learning`

**Also known as:** model-based reinforcement learning

Reinforcement learning that uses an internal model of the environment's transition and reward structure to plan.

**Tasks that engage this process:** [Two-Stage Decision Task](../tasks/hedtsk_two_stage_decision.md)

**Fundamental references**

- Daw, Niv & Dayan (2005) *Nature Neuroscience* 8:1704–1711 ([DOI](https://doi.org/10.1038/nn1560), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16286932/))
- Daw, Gershman, Seymour, Dayan & Dolan (2011) *Neuron* 69:1204–1215 ([DOI](https://doi.org/10.1016/j.neuron.2011.02.027), [PubMed](https://pubmed.ncbi.nlm.nih.gov/21435563/))

(hed-model-free-learning)=
## Model-free learning

**Process ID:** `hed_model_free_learning`

**Also known as:** model-free reinforcement learning

Reinforcement learning from cached value estimates updated by prediction errors, without an explicit model of the environment.

**Tasks that engage this process:** [Two-Stage Decision Task](../tasks/hedtsk_two_stage_decision.md)

**Fundamental references**

- Daw, Niv & Dayan (2005) *Nature Neuroscience* 8:1704–1711 ([DOI](https://doi.org/10.1038/nn1560), [PubMed](https://pubmed.ncbi.nlm.nih.gov/16286932/))

(hed-pavlovian-conditioning)=
## Pavlovian conditioning

**Process ID:** `hed_pavlovian_conditioning`

**Also known as:** classical conditioning; Pavlovian

Learning that a neutral stimulus predicts a biologically significant outcome, leading to conditioned responding.

**Tasks that engage this process:** [Pavlovian Fear Conditioning Task](../tasks/hedtsk_pavlovian_fear_conditioning.md)

**Fundamental references**

- Pavlov (1927) *Conditioned reflexes* Oxford University Press

**Further references**

- LeDoux (2014) *PNAS* 111:2871–2878 ([DOI](https://doi.org/10.1073/pnas.1400335111))

(hed-policy-learning)=
## Policy learning

**Process ID:** `hed_policy_learning`

Direct learning of a mapping from states to actions without necessarily estimating values.

**Tasks that engage this process:** none in the current catalog.

(hed-reinforcement-learning)=
## Reinforcement learning

**Process ID:** `hed_reinforcement_learning`

Learning to select actions that maximize cumulative reward through experience with reward prediction errors.

**Tasks that engage this process:** [Instrumental Conditioning Task](../tasks/hedtsk_instrumental_conditioning.md), [Iowa Gambling Task](../tasks/hedtsk_iowa_gambling.md), [Multi-Armed Bandit Task](../tasks/hedtsk_multi_armed_bandit.md), [Probabilistic Classification Learning Task](../tasks/hedtsk_probabilistic_classification_learning.md), [Probabilistic Selection Task](../tasks/hedtsk_probabilistic_selection.md), [Reversal Learning Task](../tasks/hedtsk_reversal_learning.md), [Two-Stage Decision Task](../tasks/hedtsk_two_stage_decision.md)

**Fundamental references**

- Schultz, Dayan & Montague (1997) *Science* 275:1593–1599 ([DOI](https://doi.org/10.1126/science.275.5306.1593))

**Further references**

- Niv (2009) *Journal of Mathematical Psychology* 53:139–154 ([DOI](https://doi.org/10.1016/j.jmp.2008.12.005))

(hed-reversal-learning)=
## Reversal learning

**Process ID:** `hed_reversal_learning`

Relearning after contingencies between stimuli (or responses) and outcomes are switched.

**Tasks that engage this process:** [Reversal Learning Task](../tasks/hedtsk_reversal_learning.md)

**Fundamental references**

- Iversen & Mishkin (1970) *Experimental Brain Research* 11:376–386 ([DOI](https://doi.org/10.1007/bf00237911), [PubMed](https://pubmed.ncbi.nlm.nih.gov/4993199/))
- Izquierdo, Brigman, Radke, Rudebeck & Holmes (2017) *Neuroscience* 345:12–26 ([DOI](https://doi.org/10.1016/j.neuroscience.2016.03.021), [PubMed](https://pubmed.ncbi.nlm.nih.gov/26979052/))

(hed-reward-prediction-error)=
## Reward prediction error

**Process ID:** `hed_reward_prediction_error`

Signed difference between received and expected reward, instantiated by phasic midbrain dopamine firing.

**Tasks that engage this process:** [Causal Learning Task](../tasks/hedtsk_causal_learning.md), [Instrumental Conditioning Task](../tasks/hedtsk_instrumental_conditioning.md), [Iowa Gambling Task](../tasks/hedtsk_iowa_gambling.md), [Multi-Armed Bandit Task](../tasks/hedtsk_multi_armed_bandit.md), [Probabilistic Selection Task](../tasks/hedtsk_probabilistic_selection.md), [Reversal Learning Task](../tasks/hedtsk_reversal_learning.md), [Two-Stage Decision Task](../tasks/hedtsk_two_stage_decision.md)

**Fundamental references**

- Schultz, Dayan & Montague (1997) *Science* 275:1593–1599 ([DOI](https://doi.org/10.1126/science.275.5306.1593))

**Further references**

- Glimcher (2011) *PNAS* 108(Suppl 3):15647–15654 ([DOI](https://doi.org/10.1073/pnas.1014269108))

(hed-value-learning)=
## Value learning

**Process ID:** `hed_value_learning`

Acquisition of the expected value of stimuli, actions, or states from experience with outcomes.

**Tasks that engage this process:** [Multi-Armed Bandit Task](../tasks/hedtsk_multi_armed_bandit.md), [Probabilistic Selection Task](../tasks/hedtsk_probabilistic_selection.md)

**Fundamental references**

- Rangel, Camerer & Montague (2008) *Nature Reviews Neuroscience* 9:545–556 ([DOI](https://doi.org/10.1038/nrn2357), [PubMed](https://pubmed.ncbi.nlm.nih.gov/18545266/))

