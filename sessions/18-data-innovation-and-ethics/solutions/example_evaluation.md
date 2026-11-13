# Worked example: evaluating Polars

**Name:** Polars  **Version evaluated:** 1.x  **Evaluated by:** (example)  **Date:** 2026-11

## 1. What is it?
A DataFrame library for Python, like pandas, written in Rust. It's multi-threaded and has a **lazy** mode, so it can optimise a query before running it (the same idea as Spark in session 05, but on one machine).

## 2. What problem would it solve for us?
Our **profiling and ad-hoc checks** on extracts of 1–20 GB are slow in pandas and sometimes run out of memory. Spinning up a Spark session for them feels heavy. Polars could fill the gap between "pandas is too slow" and "this needs Spark".

## 3. What I tried
- **Example:** session 05's bike trips (60k rows, scaled ×100 to 6M rows synthetically). Task: duration by station and member type, the "three ways" question.
- **Time to get working:** 25 minutes. The syntax is closer to PySpark than to pandas (`pl.col`, `group_by().agg()`).
- **Result:** the same answer as the pandas and PySpark versions. On 6M rows: pandas ~4.1 s, Polars lazy ~0.6 s, local PySpark ~9 s including startup. *(These are illustrative timings from one laptop. Measure your own.)*

## 4. Assessment

| Criterion | Score | Evidence |
|---|---|---|
| Fit | 4 | A real gap for medium-sized local work |
| Maturity | 4 | 1.0 released in 2024, widely used, frequent releases |
| Community | 4 | Good docs, active development, commercial backing |
| Skills | 4 | PySpark users pick it up quickly; pandas habits need unlearning |
| Integration | 3 | Fine for local or single-node work. **Not** a distributed engine, so it doesn't replace Spark on CDP or Dataproc. It does read Parquet, which helps on GCP (GCS) |
| Cost | 5 | MIT licence, no compute cost |
| Security / approval | 4 | Open source, runs locally, no data leaves. Needs adding to the approved package list |
| Exit cost | 4 | Code is isolated in scripts; converting back to pandas is easy |

## 5. Ethics and risks
- No data leaves the environment, and it doesn't change who has access.
- Risk: **two DataFrame libraries** in one team means more to learn and review. Mitigation: use it only for profiling and checks at first, not production pipelines.
- Risk: subtle **behaviour differences** from pandas (null handling, integer overflow) could change results. Mitigation: existing tests should pass, and compare outputs on a known dataset.

## 6. Recommendation
**Trial.**
**Why now:** profiling work is growing, and it's low risk because nothing goes to production.
**Pilot:** rewrite the session 10 profiling helper in Polars for one real extract (with approval). **Success measure:** a 3× faster run, same results, and two team members comfortable with it. **Review:** in 6 weeks.

## 7. Two-minute summary
"Polars is a fast, local DataFrame library. It's about 7× faster than pandas on our test and feels like PySpark. It's not a Spark replacement. I recommend a six-week trial for profiling only, with no production code, then a review."

---

## Facilitator notes: ethics scenarios

| # | Issue | Principle(s) | Good response |
|---|---|---|---|
| 1 | Personal data sent to a third party | Confidentiality, data protection (UK GDPR), security | Stop. Report it as a possible data incident. Use approved tools with synthetic data only |
| 2 | Purpose creep beyond the agreement | Lawful and transparent use, public good | Don't do it without a new legal basis or agreement and an ethics review. Raise it as an *idea* |
| 3 | Concealing an error | Trustworthiness, Code of Practice for Statistics (honesty, revisions policy) | Revise and explain openly. Use PACE if you're pressured (session 17) |
| 4 | Proxy discrimination | Fairness, consider bias | Assess the impact and test alternatives. Document it and get an ethics review |
| 5 | Production data in dev | Security, minimisation | Use better synthetic data (sessions 06–07), or masked data under an approved process |
| 6 | Vendor access to all data | Security, procurement, data leaving the environment | Not without security approval and a DPIA. Evaluate on synthetic data |
