# Capstone reference solution: leisure centre visits

One possible solution. It isn't the only correct one. Use it to check your thinking after you've built your own.

## Run it

```bash
# from the repo root, with .venv active
python capstone/data/make_data.py            # once
cd capstone/solution
python -m leisure_pipeline                   # writes capstone/output/, prints the summary
python -m pytest tests -q                    # 27 tests
```

## Design

```
centres.csv ─────────────────────────────────────┐
members.csv ─► standardise_members ─► dim_member  │
               (trim/upper codes, latest version, │
                missing type -> Unknown)          ▼
visits.csv ──► drop exact dups ─► standardise_visits ─► split_valid ─┬─► fact_visit
               (counted)          (card -> member_id,                └─► quarantine_visits
                                   centre name -> code, duration)
                                                 + dim_centre, dim_date (generated)
checks before writing: reconciliation · fact grain unique · every date_key in dim_date
```

| Module | Responsibility (session) |
|---|---|
| `config.py` | Every setting and rule constant. Only the paths change on CDP or GCP (03, 15) |
| `io.py` | Explicit schemas, reading and writing. The only code that knows about paths (03, 05) |
| `transform.py` | Standardising keys so the two systems can be joined (13) |
| `validate.py` | Quarantine with **one reason per row**, null-safe rules (08) |
| `model.py` | Star schema: `fact_visit` + three dimensions (12) |
| `__main__.py` | Orchestration, logging, reconciliation, a non-zero exit code on failure (09, 13, 15) |
| `tests/` | Unit tests per rule plus an end-to-end test of reconciliation and idempotency (06, 07) |

## Results on the supplied data

```
members: 1540 rows in, 1500 after keeping latest version
members: 12 with missing membership_type -> 'Unknown'
visits: 30250 rows in, 250 exact duplicates removed
quarantine: unknown_member 300 · test_card 150 · exit_not_after_entry 80 · unknown_activity 60
reconciliation OK: 30250 = 250 duplicates + 29410 fact + 590 quarantined
```

| Output | Rows |
|---|---|
| fact_visit | 29,410 |
| dim_member | 1,500 |
| dim_centre | 8 |
| dim_date | 90 |
| quarantine_visits | 590 |

## The planted traps, and what happens if you miss them

| Trap | If you miss it |
|---|---|
| Centre **names** in visits, with upper-case and trailing-space variants | **2,094** visits fail to match a centre, and are lost (inner join) or quarantined |
| `card_number` has leading zeros, while CRM uses `M00123` | Read it as an int and you lose the zeros. Join on the raw strings and *nothing* matches |
| 40 members appear twice (older and newer version) | Joining visits to members **fans out by 777 rows** |
| 112 member centre codes are lower-case or padded | `home_centre_code` doesn't join to `dim_centre` |
| 250 exact duplicate visit rows | Visits are overcounted. If you drop them silently, reconciliation can't balance |
| Test card `9999999` (150 visits) | Engineers' testing appears in official figures |
| `activity` null or `UNK`; `~isin()` on null is null | Null activities slip through the filter (a test covers this) |
| Exit before entry (80) | Negative durations |

## Design decisions worth discussing in the presentation

- **Type 1 `dim_member`.** Visits are attributed to the member's *current* type and home centre. If a member moved from Junior to Standard mid-quarter, past visits are relabelled. Type 2 (session 12) would fix this but needs `valid_from`/`valid_to` from the CRM history, and we only receive the latest two versions for some members. **Trade-off: simplicity now, with an SCD2 upgrade on the backlog.**
- **Missing membership type → "Unknown" and warn, not quarantine.** The visit is still real; only the attribute is missing. Quarantining would undercount visits.
- **Orphan cards are quarantined, not loaded with an "unknown member".** That's a judgement call. Loading them under a `-1` unknown member would keep visit totals complete. Either is fine if it is **documented and reconciled**.
- **Age band fixed at period start**, so a member doesn't change band mid-quarter.
- **Windows write fallback.** `io.write_tables(engine="auto")` uses pandas and pyarrow on Windows because Spark's Parquet writer needs `hadoop.dll`. On CDP and Dataproc it uses the Spark writer.

## CDP today → GCP tomorrow

| Piece | CDP | GCP | Code change |
|---|---|---|---|
| Source files | HDFS / landing area | GCS bucket | `DATA_DIR` in config |
| Processing | Spark on CML | Dataproc (Serverless) | None |
| Output | Hive tables (Parquet) | BigQuery tables, or Parquet on GCS + external tables | `io.write_tables` only |
| Schedule | Cron / Oozie / CML jobs | Cloud Composer DAG: one task per step | Orchestration wrapper only |
| Data dictionary | Wiki or repo CSV | Repo CSV, optionally pushed to Dataplex | None |

Because I/O and settings are isolated, **the move touches two files**.

## Example 5-minute presentation outline

1. **The question** (30 s): monthly visits by local authority and membership type, for Jan–Mar 2026.
2. **The answer** (45 s): show the summary table. Northshire is busiest, February dips everywhere (a shorter month), and Junior share is roughly stable.
3. **What we found in the data** (90 s): 2.0% of visit rows not loaded, and why (show the quarantine counts). Name the worst trap (centre names) and how it's handled.
4. **How we know it's right** (60 s): reconciliation, 27 tests, idempotent re-run, grain checks.
5. **Limitations and next steps** (45 s): type 1 member dimension, orphan card policy to agree with the service, SCD2 and a Composer DAG for GCP.
6. **Questions** (30 s).
