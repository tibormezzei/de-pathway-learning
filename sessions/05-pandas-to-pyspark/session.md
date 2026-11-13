# Session 05: From pandas to PySpark: thinking distributed

| | |
|---|---|
| Module | 1: Foundations of building |
| Wiki skill(s) | Data analysis & synthesis (Working): Python & PySpark, PySpark vs pandas |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | Sessions 03 (functions, vectorising) and 04 (joins, grain, GROUP BY). Java 17/21 installed for local Spark |
| Dataset | Synthetic city bike hire: `data/trips.csv` (60k rows), `data/stations.csv` (20 rows), regenerate with `data/make_data.py` |

## Learning outcomes
By the end of the session, participants can:
1. Choose between pandas, PySpark and SQL for a given task and data size.
2. Explain the driver/executor/partition model and why Spark is **lazy** (transformations vs actions).
3. Tell **narrow** from **wide** transformations and explain why shuffles are expensive.
4. Translate common operations between pandas, PySpark and SQL.
5. Read the key parts of `explain()` output and avoid the classic PySpark anti-patterns.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | Three tools, one job: when to use which |
| 4–10 | Single machine vs distributed: driver, executors, partitions |
| 10–15 | Lazy evaluation: transformations vs actions |
| 15–21 | Narrow vs wide, shuffles, broadcast joins |
| 21–25 | The translation table: pandas ↔ PySpark ↔ SQL |
| 25–30 | Anti-patterns |
| 30–35 | Reading `explain()` + CDP today → GCP tomorrow |
| 35–55 | Exercise |
| 55–60 | Walk through the plan together |

## Exercise
- **Task:** the pandas version of a bike-hire query is given. Write it in PySpark and in SQL (one query that runs in both DuckDB and Spark SQL), check all three agree, then interpret the Spark physical plan.
- **Starting files:** `exercise/README.md`, `exercise/three_ways.py`
- **Done when:** all three comparisons print `True` and the plan questions are answered.
- **Stretch:** caching; Python UDF vs built-in function.
- **Reference solution:** `solutions/three_ways.py`, `solutions/README.md` (annotated plan)

## Further learning (from the wiki)
- [Article: PySpark vs pandas](https://www.codeconquest.com/blog/pyspark-vs-pandas-performance-memory-consumption-and-use-cases/)
- [Learning Hub: Introduction to PySpark](https://learninghub.ons.gov.uk/course/view.php?id=1161) · [Intermediate Level Spark](https://learninghub.ons.gov.uk/course/view.php?id=583) (practitioner)
- [Learning Hub: Python: DataFrames, Manipulation and Cleaning](https://learninghub.ons.gov.uk/course/view.php?id=1156)
- [Spark Playground: coding](https://www.sparkplayground.com/tutorials/pyspark) and [theory](https://www.sparkplayground.com/tutorials/spark-theory)
- [DAPCATS wiki](https://gitlab-app-l-01/DAP_CATS/cdp-guidance-wiki/-/wikis/home) (internal: Spark on CDP)
- [YouTube: Dataproc in a minute](https://www.youtube.com/watch?v=Jj6mp7Sam10) (GCP preparation)

## Facilitator notes
- Run the solution once before the session. The first Spark start-up on a laptop takes 10–20 seconds, and Windows prints harmless warnings.
- Everyone uses Spark on CDP already, so the focus is the *why* (laziness, shuffles, plans) rather than syntax.
- Rounding: pandas rounds half to even and Spark rounds half up. It doesn't affect this dataset, but it's a real-world gotcha worth mentioning if anyone sees a 0.1 difference.
