# Session 13: Data integration design

| | |
|---|---|
| Module | 3: Analysis and design |
| Wiki skill(s) | Data integration design (Working): joining and merging, keys, schema mismatches, SCDs, data linkage awareness; ons-python-template, de-utils, plumb-etl, DLH_Utils |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | Sessions 04 (joins), 05 (PySpark), 08 (quarantine), 12 (SCD2) |
| Dataset | Synthetic GP practice registry + appointments: `data/*.csv` (6 files), regenerate with `data/make_data.py` |

## Learning outcomes
By the end of the session, participants can:
1. Describe common integration patterns: lookup enrichment, union of like sources, and record linkage.
2. Identify and resolve key mismatches: formatting, code changes and mergers, missing keys.
3. Join to **effective-dated / versioned** reference data correctly.
4. Handle schema mismatches between sources.
5. Explain **full vs incremental** loads and **idempotency**.
6. Reconcile an integration (in = out + quarantined) and write a source-to-target mapping.
7. Recognise when a problem needs **data linkage** rather than a join, and know where to find help (DLH_Utils, linkage team).

## Concept outline
| Min | Section |
|---|---|
| 0–4 | Why integration is hard: different owners, different conventions |
| 4–9 | Integration patterns |
| 9–15 | Keys: natural vs surrogate, standardisation, code changes, mergers |
| 15–20 | Effective dating and versioned lookups |
| 20–23 | Schema mismatches: names, types, units, granularity |
| 23–27 | Deterministic joins vs probabilistic linkage |
| 27–31 | Loads: full vs incremental, idempotency, reconciliation |
| 31–35 | ONS reusable tools + CDP today → GCP tomorrow |
| 35–55 | Exercise |
| 55–60 | Experiments debrief: what reconciliation does and doesn't catch |

## Exercise
- **Task:** complete key standardisation, merger mapping and versioned lookup in a PySpark integration of appointments with a practice registry. Reconcile.
- **Starting files:** `exercise/README.md`, `exercise/integrate.py`
- **Done when:** reconciliation balances (424,013 = 421,780 + 2,233), the pipeline is idempotent, and HB05 appears only from April.
- **Reference solution:** `solutions/integrate.py`, `solutions/README.md` (including experiment results)

## Further learning (from the wiki)
- [Learning Hub: Awareness of Data Linkage](https://learninghub.ons.gov.uk/course/view.php?id=1190) · [Introduction to Data Linkage](https://learninghub.ons.gov.uk/course/view.php?id=1209) · [Data Linkage in Python](https://learninghub.ons.gov.uk/course/view.php?id=1212)
- [ONSdigital/de-utils](https://github.com/ONSdigital/de-utils/tree/main) · [ONSdigital/plumb-etl](https://github.com/ONSdigital/plumb-etl) · [Data-Linkage/dlh_utils](https://github.com/Data-Linkage/dlh_utils) · [ons-python-template](https://github.com/ONSdigital/ons-python-template)
- [Cloud Skills Boost: Building batch data pipelines on Google Cloud](https://www.cloudskillsboost.google/course_templates/53) (long, practitioner level, GCP)
- [Lab: ETL pipeline with Apache Beam and Dataflow (Python)](https://www.cloudskillsboost.google/focuses/64780) · [Basic Airflow lab](https://www.cloudskillsboost.google/focuses/3528)

## Facilitator notes
- The "v2 for every month" experiment is the key lesson: totals still balance, so reconciliation alone isn't enough. Make sure every pair hears it in the debrief.
- If someone in the room maintains de-utils or plumb-etl, ask them for two minutes on which helpers already exist for key standardisation and reconciliation.
- Spark start-up plus running the pipeline twice (for the idempotency check) takes about 30–40s locally.
