# Homework: evaluate one emerging tool or technique

**Time:** about 2 hours · **Work:** on your own, or in pairs · **Share:** a 2-minute summary at the next team meeting or community of practice

## The task

Pick **one** tool or technique you haven't used at work. Evaluate whether *your team* should adopt it, trial it, watch it or ignore it, using `evaluation_template.md`.

You must:
1. **Try it.** Spend at least 30 minutes with it on a small example, using synthetic or public data only, never real data. One of the datasets from this series is fine.
2. **Fill in every section of the template**, including the ethics and risks section.
3. **End with one recommendation:** Adopt / Trial / Assess / Hold, and say *why now* or *why not now*.

## Ideas, if you're stuck

| Area | Candidates |
|---|---|
| Processing | Polars · DuckDB (beyond session 04) · Apache Arrow · Spark Connect |
| Data quality | Great Expectations · Soda · Pandera on PySpark |
| Modelling and transformation | dbt · SQLMesh |
| Table formats | Delta Lake · Apache Iceberg |
| Orchestration | Airflow (local) · Dagster · Prefect |
| Developer tooling | Ruff · uv · pre-commit · GitHub Actions |
| Metadata | OpenLineage · DataHub · Dataplex (docs only) |
| AI-assisted | Code assistants for writing tests or docs · LLM-based data profiling |
| Techniques | Synthetic data generation · Data contracts · Privacy-enhancing technologies |
| GCP | BigQuery · Dataproc Serverless · Cloud Composer (using the free tier or docs, **not** a work project without approval) |

## Rules
- **No real or personal data** goes into a tool you're evaluating, especially an online or AI tool.
- Don't install anything on a work machine that isn't approved. Use your local venv or read the docs instead.
- "We should hold" is a perfectly good recommendation if you justify it.

## Done when
- [ ] The template is complete, including ethics and risks.
- [ ] There's a small working example, or a note explaining why you couldn't run one.
- [ ] There's a clear recommendation with a reason tied to *timing*.
- [ ] You can summarise it in 2 minutes.

See `solutions/example_evaluation.md` for a worked example (Polars).
