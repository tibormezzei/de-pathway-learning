# Session 09: Problem resolution: debugging and logging

| | |
|---|---|
| Module | 2: Quality and reliability |
| Wiki skill(s) | Problem resolution (data): print debugging, rubber ducking, documentation, pair programming, AI, logging |
| HEO target level | Awareness (the wiki's HEO target), stretching to Working |
| Duration | 60 min (~35 concept / ~20 exercise / ~5 Q&A) |
| Follow-up | **Exercise** (in session) |
| Prerequisites | Sessions 03, 04 (fan-out), 08 (expectations as checks) |
| Dataset | Synthetic air-quality readings: `data/readings.csv` (600 rows), `data/stations.csv` (11 rows, one renamed station), regenerate with `data/make_data.py` |

## Learning outcomes
By the end of the session, participants can:
1. Judge how severe a problem is and who it affects, and decide how urgently to act and whom to tell.
2. Read Python tracebacks and recognise the useful part of a PySpark error.
3. Debug systematically: reproduce, read, hypothesise, inspect, fix, verify.
4. Catch **silent** bugs by writing expectations down and turning them into checks.
5. Use Python `logging` with sensible levels and content, and know what not to log.
6. Use AI assistants responsibly, in line with ONS policy.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | When things break: severity, impact, who to tell |
| 4–10 | Reading errors: Python tracebacks, PySpark errors |
| 10–17 | A debugging method + techniques (print/inspect, breakpoint, shrink the input, rubber duck, pair) |
| 17–21 | Silent bugs: expectations, assertions, invariants |
| 21–28 | Logging: why not print, levels, what to log, what never to log |
| 28–31 | AI assistants: good uses, risks, ONS policy |
| 31–35 | CDP today → GCP tomorrow + summary |
| 35–55 | Exercise |
| 55–60 | Bug reveal; severity discussion |

## Exercise
- **Task:** fix a broken air-quality report with 2 crashing and 2 silent bugs, then add logging and a safeguard.
- **Starting files:** `exercise/README.md`, `exercise/air_quality_report.py`
- **Done when:** 10 stations × 31 days, and logging shows counts at each step plus a warning for below-detection values.
- **Reference solution:** `solutions/air_quality_report.py`, `solutions/README.md`

## Further learning (from the wiki)
- [Using print statements to debug](https://dev.to/nickjj/using-print-statements-are-a-handy-way-to-debug-and-explore-code-54ne) · [Rubber duck debugging](https://rubberduckdebugging.com/) ([cyberduck](https://rubberduckdebugging.com/cyberduck/))
- [Breaking down problems](https://nickjanetakis.com/blog/breaking-down-problems-is-the-number-1-software-developer-skill)
- [Pair programming (Datadog)](https://www.datadoghq.com/knowledge-center/pair-programming/) · [Codecademy](https://www.codecademy.com/resources/blog/what-is-pair-programming/)
- [Pluralsight: AI in software development](https://www.pluralsight.com/resources/blog/business-and-leadership/AI-in-software-development) · UKSA AI policy (intranet)
- Logging: [YouTube: Logging](https://www.youtube.com/watch?v=pxuXaaT1u3k) · [PySpark logger docs](https://spark.apache.org/docs/4.0.0-preview2/api/python/development/logger.html) · [Writing PySpark logs (Medium)](https://polarpersonal.medium.com/writing-pyspark-logs-in-apache-spark-and-databricks-8590c28d1d51)
- [YouTube: Cloud Logging in a minute](https://www.youtube.com/watch?v=hpUHZixlHiA) (GCP preparation)

## Facilitator notes
- Don't tell people there are silent bugs until they say they're "done". Then ask them to compare against the README's "what correct looks like".
- Spark errors: CDP users see long Java stack traces every week. The slide on finding the Python error and `Caused by:` is often the most valued five minutes of the session.
- Severity framing matches the wiki's "strategic / tactical / operational" levels. Keep it practical: *who would notice, and what would they do with the wrong number?*
