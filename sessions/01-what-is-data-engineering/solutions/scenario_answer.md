# Facilitator answer: business register scenario

There's no single right answer. Use this to prompt discussion, and reward reasoning over tool names.

## 1. Lifecycle → component → tool

| Stage | What happens | Component | Example (GCP / CDP) |
|---|---|---|---|
| Generate | Businesses submit returns; the web form writes to a transactional DB | Source system (OLTP) | Cloud SQL / SQL Server |
| Ingest | Weekly extract of new or changed returns since the last run (incremental) | Compute + orchestration | Dataproc job / CML job |
| Store (raw) | Extract landed unchanged, partitioned by extract date | Data lake | Cloud Storage / S3 |
| Ingest (lookup) | Classifications lookup published to an agreed location **with a version and effective date**, not emailed | Data lake / reference store | GCS / S3 / Hive table |
| Transform | Deduplicate submissions, validate, standardise, join to the **correct version** of the lookup | Compute | PySpark |
| Serve | Curated tables for the quarterly report; the report reads from these | Warehouse | BigQuery / Hive |
| Orchestration | Weekly schedule; extract → validate → transform → publish; stop and alert on failure | Orchestrator | Cloud Composer / team scheduler |
| Version control | Pipeline code, tests and configuration | Git host | GitHub / GitLab |
| Metadata | Data dictionary, lookup version used in each run, lineage from source to report | Catalogue / docs | Dataplex / docs in repo |
| Monitoring | Row counts, duplicate counts, validation failures, run success or failure | Logging + alerts | Cloud Logging / logs + email |

## 2. Classification
- **OLTP → OLAP:** yes, from a transactional form database to analytical tables.
- **Batch:** a weekly report doesn't need streaming.
- **ETL / ELT:** either works. Landing raw data first (ELT-style) means past weeks can be reprocessed if the dedup or lookup logic changes.
- **Formats:** Parquet for the raw and curated layers. Keep CSV only if someone downstream really needs it.

## 3. Risks to listen for
- **Duplicates:** what makes two submissions duplicates? This is a business rule to agree with stakeholders (→ sessions 8, 13).
- **Wrong lookup version:** fix it with versioned reference data, record which version each run used, and fail if the lookup is older than expected (→ 13, 14).
- **Silent failure:** without monitoring, a run that loads 0 rows "succeeds" (→ 9).
- **Schema change at source:** the web form adds a field (→ 8).
- **Re-running:** a re-run must not double-count. The pipeline needs to be idempotent (→ 13, 15).
- **People:** analysts need to trust the new output. Run the old and new processes side by side for a while (→ 17).

## 4. CDP → GCP: what really changes
- **Only the name changes:** S3 → Cloud Storage, Hive → BigQuery, GitLab → GitHub, PySpark code (mostly unchanged).
- **Something really changes:**
  - **Cost:** BigQuery charges per query and Dataproc per cluster-minute, so scans need care (partition the data and select only the columns you need).
  - **IAM:** the team sets up service accounts and permissions, where on CDP the platform team did this.
  - **Cluster lifecycle:** ephemeral Dataproc clusters (or serverless) replace a long-running CML session, so the job must be fully scripted, not run by hand in a notebook.
  - **Orchestration:** Cloud Composer (Airflow) DAGs, likely written by the team.

## Teaching points
- The original problems (duplicates and a stale lookup) are **engineering problems**, not analyst errors. Pipelines make rules explicit and testable.
- Most of the design is **platform-neutral**. Only the right-hand column changes between GCP, CDP and a laptop.
