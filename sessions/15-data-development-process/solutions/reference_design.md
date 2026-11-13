# Design: weekly school attendance statistics (reference answer)

**Status:** example for facilitators. One good answer, not the only one.

## 1. Objective
Publish weekly pupil attendance rates by local authority, school phase and nationally, every Thursday 09:30, for the previous Monday–Friday. Reproducible, quality assured, and transparent about missing data.

## 2. Requirements
| # | Requirement | Type |
|---|---|---|
| R1 | Attendance rate = Σ attended ÷ Σ possible sessions, by LA, phase and nationally, per week | Functional |
| R2 | Published Thursday 09:30 for the previous school week | Constraint |
| R3 | Missing LAs are published as missing, not late | Quality |
| R4 | Corrected resubmissions replace earlier data for that LA-day | Functional |
| R5 | Figures reproducible for any past week | Quality |
| R6 | No disclosive figures (small special schools) | Governance |
| R7 | Runs on CDP now; minimal rework for GCP next year | Constraint |

**Out of scope:** pupil-level data, school-level publication, persistent absence measures.

## 3. Sources
| Source | Owner | Delivery | Grain | Update | Issues / questions |
|---|---|---|---|---|---|
| Daily returns | 22 LAs | CSV per LA per day on SFTP | school × day | Daily, sometimes late, sometimes resent | How do we identify a resend (same filename, version suffix)? Are bank holidays and INSET days sent as zero rows or omitted? |
| School register | Department | Monthly file | school (with history) | Monthly | Effective dates of phase or LA changes? Will they send history or only the current state? |

## 4. Output
- `attendance_weekly`: grain **week × LA × phase** (+ national and LA totals): sessions possible, attended, authorised absence, rate, `n_schools`, `las_reporting`, suppression flag.
- Data dictionary and dataset metadata as in session 14.

## 5. Design

```
 SFTP ──▶ [1 land raw] ──▶ [2 validate] ──▶ [3 latest per LA-day] ──▶ [4 attach register as at date]
                               │quarantine                                        │
                                                    [7 publish] ◀── [6 disclosure] ◀── [5 aggregate week]
```

1. **Land raw:** copy every file unchanged to `raw/la=<code>/date=<d>/received=<timestamp>/`. Never overwrite raw data, so a full audit trail is kept.
2. **Validate:** schema, types, `0 ≤ attended ≤ possible`, known `school_id`, date within the week. Failing rows are quarantined. An empty or unreadable file **fails that LA-day** and alerts.
3. **Latest per LA-day:** for each `(la, date)` keep the file with the **latest `received`** timestamp (resubmissions win, as in session 07's R3).
4. **Register as at date:** the school register is stored as **versioned reference data** (`valid_from` / `valid_to`, SCD2). Join on `school_id` **and** date.
5. **Aggregate** to week × LA × phase, keeping **additive parts** (sessions), and calculate rates at the end.
6. **Disclosure:** suppress cells with fewer than *N* schools or pupils (threshold agreed with the DisCO). Apply secondary suppression where totals would reveal it.
7. **Publish:** write the week's partition (overwrite), and the metadata including `las_reporting` and which LAs are missing.

**Late and corrected data:** each Thursday run **recomputes the whole target week** from raw (latest file per LA-day). Because steps 2–7 are **idempotent** and partitioned by week, a corrected file arriving later is handled by **re-running that week** (a backfill). Published revisions follow the revisions policy (open question).

## 6. Orchestration and operations
- **Schedule:** Thursday 06:00 (cut-off for late files), giving 3.5 hours of slack before 09:30. A daily ingest-only run Tue–Sat lands and validates files early, so problems surface during the week.
- **DAG:** land → validate → latest → register join → aggregate → disclosure → publish.
- **Retries:** SFTP pulls only (transient). **No retries** on validation failures, because those are data problems.
- **Alerting:** a missing LA by Wednesday 18:00 emails the analysis team. Pipeline failure alerts the on-call engineer.
- **Backfill:** `run(week=...)` is safe to re-run for any past week.
- **Run book:** what to check, who to call for each LA, how to re-run a week.

## 7. Technology
| Component | CDP today | GCP later |
|---|---|---|
| Landing | SFTP → HDFS/S3 raw zone | SFTP → **GCS** raw bucket |
| Processing | PySpark in CML jobs | PySpark on **Dataproc Serverless** (same code) |
| Reference and outputs | Hive tables (Parquet, partitioned by week) | **BigQuery** (partitioned by week) or GCS Parquet |
| Orchestration | Team scheduler / CML jobs | **Cloud Composer** (Airflow) |
| Code and CI | GitLab + CI | GitHub + Actions |

**Decisions now that ease migration:** all paths and table names in **config**; I/O in a thin layer (session 07); a packaged entry point with `--week` (session 03); idempotent, partitioned outputs (Composer retries and backfills will re-run tasks).

## 8. Governance and security
- Session counts aren't pupil records, but **small special schools** could be disclosive, so DisCO rules apply (step 6).
- IAO: the Education Analysis deputy director (to confirm). Access is limited to the team. Raw retention is 2 years (to confirm).

## 9. Testing
- **Unit:** validation rules, latest-file selection, the as-at-date register join, suppression (inline synthetic data).
- **Integration:** a run over a synthetic week with a late file, a resend, a phase change mid-week and a tiny school.
- **Runtime checks:** reconciliation (sessions in = sessions out + quarantined), `las_reporting` count, rate within 80–100%.

## 10. Risks, assumptions, open questions
| Item | Type | Owner |
|---|---|---|
| How are resubmissions identified on SFTP? | Question | LA data contacts |
| Revisions policy for published weeks when corrections arrive late | Question | Head of statistics |
| Disclosure threshold *N* | Question | DisCO |
| Register history: do we get effective dates? | Question | Department |
| Six-week deadline is tight for full DQ, so prioritise R1–R4 | Risk | Delivery manager |
