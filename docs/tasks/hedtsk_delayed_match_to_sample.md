(hedtsk_delayed_match_to_sample)=

# Delayed Match-to-Sample Task

**HED Task ID:** `hedtsk_delayed_match_to_sample`

**Also known as:** DMTS, DMS

Sample stimulus followed by a delay and then a probe or choice array; response indicates whether the probe matches the sample. Indexes short-term memory maintenance.

## Description

The Delayed Match-to-Sample (DMTS) task consists of three phases: sample, delay, and choice. During the sample phase, a stimulus is presented. Following a delay period (0-30 seconds), the participant must identify which of several test stimuli matches the original sample. Memory demands are manipulated by varying delay duration or the number of choice alternatives. The task has been fundamental in primate neuroscience for identifying the neural substrates of working memory, particularly delay-period persistent activity in prefrontal cortex.

## Inclusion test

```{list-table}
---
widths: 15 85
header-rows: 0
---
* - **Procedure**
  - A sample stimulus is presented, followed by a retention interval (delay), then a test stimulus; participants indicate whether the test matches the sample.
* - **Manipulation**
  - Delay duration; sample complexity; number of test alternatives; interference during delay.
* - **Measurement**
  - Accuracy (proportion correct); RT; decay function across delay intervals.
```

## Variations

```{list-table}
---
widths: 25 40 35
header-rows: 1
---
* - Variation
  - Description
  - Justification
* - Standard DMTS
  - Single sample → delay → two-choice test (match vs. non-match).
  - Canonical: sample presented, delay, then match from array
* - Variable Delay DMTS
  - Delay ranging from 0 to 30 seconds; maps forgetting function.
  - Systematically varies delay length; tests forgetting function
* - Multi-Choice DMTS
  - More than two choice alternatives; increases memory precision demands.
  - More than two choices at test; increases decision complexity
* - DMTS with Distraction During Delay
  - Irrelevant stimuli during retention; measures interference resistance.
  - Interfering stimuli during retention interval; changes delay period structure
* - Spatial DMTS
  - Location-based matching rather than object-based.
  - Location rather than identity must be matched; different memory dimension
* - DMTS with Object Complexity Manipulation
  - Simple colors vs. complex patterns; manipulates encoding demands.
  - Varies object complexity; tests encoding difficulty directly
* - Delayed Non-Match-to-Sample (DNMS)
  - Select the novel stimulus; used extensively in primate lesion studies.
  - Respond to non-matching item; opposite stimulus-response mapping
```

## Cognitive processes

This task engages the following cognitive processes:

- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Recognition](../processes/long_term_memory.md#hed-recognition)
- [Encoding](../processes/long_term_memory.md#hed-encoding)
- [Visual working memory](../processes/short_term_and_working_memory.md#hed-visual-working-memory)

## Key references

- {'authors': 'Fuster, J. M., & Alexander, G. E.', 'year': 1971, 'title': 'Neuron Activity Related to Short-Term Memory', 'venue': 'Science', 'venue_type': 'journal', 'journal': 'Science', 'volume': '173', 'issue': '3997', 'pages': '652-654', 'doi': '10.1126/science.173.3997.652', 'openalex_id': None, 'pmid': None, 'citation_string': 'Fuster, J. M., & Alexander, G. E. (1971). Neuron activity related to short-term memory. *Science*, 173(3997), 652-654.', 'url': 'https://doi.org/10.1126/science.173.3997.652', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Miller, E. K., Erickson, C. A., & Desimone, R.', 'year': 1996, 'title': 'Neural Mechanisms of Visual Working Memory in Prefrontal Cortex of the Macaque', 'venue': 'The Journal of Neuroscience', 'venue_type': 'journal', 'journal': 'The Journal of Neuroscience', 'volume': '16', 'issue': '16', 'pages': '5154-5167', 'doi': '10.1523/jneurosci.16-16-05154.1996', 'openalex_id': None, 'pmid': None, 'citation_string': 'Miller, E. K., Erickson, C. A., & Desimone, R. (1996). Neural mechanisms of visual working memory in prefrontal cortex of the macaque. *Journal of Neuroscience*, 16(16), 5154-5167.', 'url': 'https://doi.org/10.1523/jneurosci.16-16-05154.1996', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Pessoa, L., Gutierrez, E., Bandettini, P. A., & Ungerleider, L. G.', 'year': 2002, 'title': 'Neural Correlates of Visual Working Memory', 'venue': 'Neuron', 'venue_type': 'journal', 'journal': 'Neuron', 'volume': '35', 'issue': '5', 'pages': '975-987', 'doi': '10.1016/s0896-6273(02)00817-6', 'openalex_id': None, 'pmid': None, 'citation_string': 'Pessoa, L., Gutierrez, E., Bandettini, P. A., & Ungerleider, L. G. (2002). Neural correlates of visual working memory: fMRI amplitude predicts task performance. *Neuron*, 35(5), 975-987.', 'url': 'https://doi.org/10.1016/s0896-6273(02)00817-6', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## Recent references

- {'authors': 'Lara, A. H., & Wallis, J. D.', 'year': 2015, 'title': 'The Role of Prefrontal Cortex in Working Memory: A Mini Review', 'venue': 'Frontiers in Systems Neuroscience', 'venue_type': 'journal', 'journal': 'Frontiers in Systems Neuroscience', 'volume': '9', 'issue': None, 'pages': None, 'doi': '10.3389/fnsys.2015.00173', 'openalex_id': None, 'pmid': None, 'citation_string': 'Lara, A. H., & Wallis, J. D. (2015). The role of prefrontal cortex in working memory: A mini review. *Frontiers in Systems Neuroscience*, 9, 173.', 'url': 'https://doi.org/10.3389/fnsys.2015.00173', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Constantinidis, C., Funahashi, S., Lee, D., Murray, J. D., Qi, X., Wang, M., & Arnsten, A. F.', 'year': 2018, 'title': 'Persistent Spiking Activity Underlies Working Memory', 'venue': 'The Journal of Neuroscience', 'venue_type': 'journal', 'journal': 'The Journal of Neuroscience', 'volume': '38', 'issue': '32', 'pages': '7020-7028', 'doi': '10.1523/jneurosci.2486-17.2018', 'openalex_id': None, 'pmid': None, 'citation_string': 'Constantinidis, C., Funahashi, S., Lee, D., Murray, J. D., Qi, X. L., Wang, M., & Arnsten, A. F. T. (2018). Persistent spiking activity underlies working memory. *Journal of Neuroscience*, 38(32), 7020–7028.', 'url': 'https://doi.org/10.1523/jneurosci.2486-17.2018', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Lundqvist, M., Herman, P., & Miller, E. K.', 'year': 2018, 'title': 'Working Memory: Delay Activity, Yes! Persistent Activity? Maybe Not', 'venue': 'The Journal of Neuroscience', 'venue_type': 'journal', 'journal': 'The Journal of Neuroscience', 'volume': '38', 'issue': '32', 'pages': '7013-7019', 'doi': '10.1523/jneurosci.2485-17.2018', 'openalex_id': None, 'pmid': None, 'citation_string': 'Lundqvist, M., Herman, P., & Miller, E. K. (2018). Working memory: Delay activity, yes! Persistent activity? Maybe not. *Journal of Neuroscience*, 38(32), 7013–7019.', 'url': 'https://doi.org/10.1523/jneurosci.2485-17.2018', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}
- {'authors': 'Stokes, M. G.', 'year': 2015, 'title': '‘Activity-silent’ working memory in prefrontal cortex: a dynamic coding framework', 'venue': 'Trends in Cognitive Sciences', 'venue_type': 'journal', 'journal': 'Trends in Cognitive Sciences', 'volume': '19', 'issue': '7', 'pages': '394-405', 'doi': '10.1016/j.tics.2015.05.004', 'openalex_id': None, 'pmid': None, 'citation_string': "Stokes, M. G. (2015). 'Activity-silent' working memory in prefrontal cortex: A dynamic coding framework. *Trends in Cognitive Sciences*, 19(7), 394–405.", 'url': 'https://doi.org/10.1016/j.tics.2015.05.004', 'source': 'crossref', 'confidence': 'high', 'verified_on': '2026-04-20'}

## External links

- Cognitive Atlas: [delayed match to sample task](https://www.cognitiveatlas.org/task/id/tsk_4a57abb9499e3)
