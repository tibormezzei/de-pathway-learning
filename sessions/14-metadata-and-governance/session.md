# Session 14: Metadata and data governance

| | |
|---|---|
| Module | 3: Analysis and design |
| Wiki skill(s) | Metadata management (Working): repositories, standards (SKOS, GSIM, DCAT, Dublin Core, PROV-O, ISO 11179); Problem resolution: IAO and DisCO roles; Data development process: governance and quality standards (GDPR, PII) |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 homework briefing + start the dictionary together / ~5 Q&A) |
| Follow-up | **Homework** |
| Prerequisites | Session 13 (the pipeline being documented) |
| Dataset | The output of the session 13 pipeline (the checker runs it) |

## Learning outcomes
By the end of the session, participants can:
1. Explain what metadata is and distinguish descriptive, structural, administrative and operational metadata.
2. Write a useful data dictionary entry and a source-to-target mapping.
3. Explain lineage and the role of catalogues.
4. Recognise the main metadata standards and when they matter.
5. Describe ONS governance roles (IAO, data steward, DisCO) and basic data protection principles (personal data, minimisation, classification, retention).
6. Treat metadata **as code**: version-controlled and tested against the data.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | "What does this column mean?": the cost of missing metadata |
| 4–9 | Kinds of metadata |
| 9–15 | Data dictionaries and source-to-target mappings |
| 15–19 | Lineage and catalogues |
| 19–22 | Standards at awareness level |
| 22–29 | Governance: roles, personal data, classification, disclosure, retention |
| 29–32 | Metadata as code |
| 32–35 | CDP today → GCP tomorrow |
| 35–50 | Homework briefing; write the `month` dictionary row together and run the checker |
| 50–60 | Q&A |

## Homework
- **Task:** write a data dictionary (machine-checked against the real output), a source-to-target mapping and dataset-level metadata for session 13's output.
- **Starting files:** `homework/README.md`, `homework/data_dictionary.csv`, `homework/source_to_target.md`, `homework/dataset_metadata.yaml`, `homework/check_dictionary.py`
- **Done when:** the checker prints PASS and all governance fields are answered (or marked "unknown: ask X").
- **Stretch:** turn the check into a CI test.
- **Reference:** `solutions/`

## Further learning (from the wiki)
- *Principles of Data Management* (Percipio), chapter 6: metadata overview
- DAB: metadata training summary and the *Guidance on understanding, compiling, organising and managing metadata* (ONS SharePoint, internal)
- Standards: [SKOS](https://www.w3.org/2004/02/skos/) · [GSIM](https://statswiki.unece.org/spaces/gsim/pages/431489200/Clickable+GSIM+v2.0) · [GSBPM](https://statswiki.unece.org/spaces/GSBPM/pages/243269812/GSBPM+v5.1) · [Dublin Core](https://www.dublincore.org/specifications/dublin-core/dcmi-terms/) · [DCAT](https://www.w3.org/TR/vocab-dcat-3/) · [PROV-O](https://www.w3.org/TR/prov-o/) · [Schema.org](https://schema.org) · ISO/IEC 11179
- [Learning Hub: DisCO training](https://learninghub.ons.gov.uk/course/view.php?id=659) · Data ethics: [Module 1](https://learninghub.ons.gov.uk/course/view.php?id=1185), [Module 2](https://learninghub.ons.gov.uk/course/view.php?id=1179)

## Facilitator notes
- The checker makes a "boring" topic concrete. Run it live on the nearly empty starter dictionary and let the failures show why documentation drifts.
- Governance answers vary by business area. Encourage "unknown: ask X" over guessing, which is itself a governance habit.
- Keep the standards slide at awareness level. Aim for recognising the names and knowing who to ask (DAB), not studying the specs.
