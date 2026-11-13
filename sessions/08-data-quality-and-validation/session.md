# Session 08: Data quality and validation

| | |
|---|---|
| Module | 2: Quality and reliability |
| Wiki skill(s) | Data development process (Awareness): Pandera and Great Expectations; data governance and quality standards |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | Sessions 03 (functions), 06 (testing) |
| Dataset | Synthetic business survey returns: `data/returns.csv` (404 rows, planted problems), regenerate with `data/make_data.py` (prints the answer key) |

## Learning outcomes
By the end of the session, participants can:
1. Name the main data quality dimensions and give an example of each.
2. Explain the difference between **testing code** and **validating data**.
3. Write a declarative validation schema (Pandera) covering types, nulls, ranges, allowed values, patterns, uniqueness and cross-field rules.
4. Choose between **fail**, **quarantine** and **warn** for a given problem.
5. Decide where validation belongs in a pipeline.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | Bad data costs: a few real-world style examples |
| 4–8 | Testing code vs validating data |
| 8–14 | Data quality dimensions |
| 14–18 | Where to validate: at ingest, between stages, before publishing |
| 18–27 | Declarative validation with Pandera (and the same ideas in Great Expectations) |
| 27–31 | Fail, quarantine or warn |
| 31–35 | CDP today → GCP tomorrow + summary |
| 35–55 | Exercise |
| 55–60 | Fix or refer back? Go through the decisions |

## Exercise
- **Task:** complete a Pandera schema for business survey returns, quarantine the failing rows, and decide how each kind of problem should be handled.
- **Starting files:** `exercise/README.md`, `exercise/validate_returns.py`
- **Done when:** the schema catches all planted problems (32 rows quarantined).
- **Stretch:** a cross-field warning; a failure report the business area could act on.
- **Reference solution:** `solutions/validate_returns.py`, `solutions/README.md` (answer key + handling table)

## Further learning (from the wiki)
- [Pandera docs](https://pandera.readthedocs.io/en/stable/index.html) · [Great Expectations docs](https://docs.greatexpectations.io/docs/)
- [Article: Pandera and Great Expectations compared](https://endjin.com/blog/2023/03/a-look-into-pandera-and-great-expectations-for-data-validation)
- [The Aqua Book](https://www.gov.uk/government/publications/the-aqua-book-guidance-on-producing-quality-analysis-for-government): quality assurance of analysis
- DAMA-DMBOK2, chapter on data quality (ONS Data Architecture SharePoint, internal)

## Facilitator notes
- Run `python data/make_data.py` yourself before the session. It prints the answer key.
- The "read codes as text" question often surprises people. Demonstrate it live by removing `dtype=` and showing `01110` becoming `1110`.
- Pandera also supports PySpark DataFrames (`pandera.pyspark`). Mention it so CDP users know the same approach scales.
