(hedtsk_sternberg_item_recognition)=
# Sternberg Item Recognition Task

**HED task ID:** `hedtsk_sternberg_item_recognition`

**Family:** [Short-term and working memory tasks](families/working_memory_span.md)

**Also known as:** Sternberg Memory Scanning, Memory Search Task

Short memory set followed by a probe; yes/no judgment of set membership. RT typically scales linearly with set size.

## Description

The Sternberg task measures the speed of short-term memory scanning. On each trial, participants encode a brief study list of 1-6 items, then after a retention interval, judge whether a test probe was in the studied list. The critical finding is that RT increases linearly with memory set size for both positive and negative probes, suggesting serial exhaustive scanning. The slope of the RT-by-set-size function indexes memory scanning speed, while the intercept indexes stimulus encoding and response execution time.

## Inclusion test

An experiment is an instance of this task when its procedure matches, it manipulates at
least one of the listed variables, and it records at least one of the listed measures.

```{list-table}
:widths: 15 85
:header-rows: 0

* - **Procedure**
  - Participants memorize a small set of items (1–6 digits or letters), then a probe appears and they indicate whether it was in the memory set.
* - **Manipulation**
  - Set size (1–6); probe type (positive/present vs. negative/absent); degraded probes; varied vs. fixed set across trials.
* - **Measurement**
  - RT as a function of set size (slope = scanning rate, ~38 ms/item); intercept; accuracy.
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
* - Visual Sternberg

    `hedvar_sternberg_item_recognition__visual_sternberg`
  - Letters/digits presented visually; visual probe comparison.
  - Canonical memory set presented visually; recognition probe after delay
* - Auditory Sternberg

    `hedvar_sternberg_item_recognition__auditory_sternberg`
  - Items presented acoustically; tests modality-specific memory.
  - Auditory memory set; different sensory modality
* - Cross-Modal Sternberg

    `hedvar_sternberg_item_recognition__cross_modal_sternberg`
  - Encoding in one modality, probe in another; tests amodal representation.
  - Study in one modality, test in another; cross-modal recognition
* - Sternberg with Irrelevant Items

    `hedvar_sternberg_item_recognition__sternberg_with_irrelevant_items`
  - Memory set includes to-be-ignored items; tests directed forgetting.
  - Distractors added during retention; tests interference resistance
* - Recent-Probes Sternberg

    `hedvar_sternberg_item_recognition__recent_probes_sternberg`
  - Negative probes that were in the previous (but not current) set; measures proactive interference.
  - Probes match previous trials; tests proactive interference
```

## Cognitive processes

This task is designed to engage the following processes:

- [Active maintenance](../processes/short_term_and_working_memory.md#hed-active-maintenance)
- [Retrieval](../processes/long_term_memory.md#hed-retrieval)
- [Working memory](../processes/short_term_and_working_memory.md#hed-working-memory)
- [Verbal working memory](../processes/short_term_and_working_memory.md#hed-verbal-working-memory)
- [Response selection](../processes/motor_preparation_timing_and_execution.md#hed-response-selection)

## Key references

- Sternberg, S. (1966). High-speed scanning in human memory. *Science*, 153(3736), 652-654. ([DOI](https://doi.org/10.1126/science.153.3736.652), [PubMed](https://pubmed.ncbi.nlm.nih.gov/5939936/))
- Sternberg, S. (1969). Memory-scanning: Mental processes revealed by reaction-time experiments. *American Scientist*, 57(4), 421-457.

## Further references

- Donkin, C., & Nosofsky, R. M. (2012). A power-law model of psychological memory strength in short-term and long-term recognition. *Psychological Science*, 23(6), 625–634. ([DOI](https://doi.org/10.1177/0956797611430961), [PubMed](https://pubmed.ncbi.nlm.nih.gov/22527527/))
- Van Vugt, M. K., Schulze-Bonhage, A., Litt, B., Brandt, A., & Kahana, M. J. (2010). Hippocampal gamma oscillations increase with memory load. *Journal of Neuroscience*, 30(7), 2694–2699. ([DOI](https://doi.org/10.1523/jneurosci.0567-09.2010), [PubMed](https://pubmed.ncbi.nlm.nih.gov/20164353/))
- Oberauer, K., Lewandowsky, S., Awh, E., Brown, G. D., Conway, A., et al. (2018). Benchmarks for models of short-term and working memory. *Psychological Bulletin*, 144(9), 885–958. ([DOI](https://doi.org/10.1037/bul0000153), [PubMed](https://pubmed.ncbi.nlm.nih.gov/30148379/))

## External links

- Cognitive Atlas: [Sternberg Item Recognition Task](https://www.cognitiveatlas.org/task/id/trm_551f0a8b5ba2c)

