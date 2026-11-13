# Reference solution: session 13

```bash
python solutions/integrate.py
```

Expected: 27 result rows (4 boards × Jan–Mar, 5 boards × Apr–Jun). Reconciliation **424,013 in = 421,780 out + 2,233 quarantined**. Re-run is identical.

## The three steps

```python
# 1. key standardisation
F.regexp_replace(F.upper(F.trim(F.col(col))), r"[\s\-]", "")

# 2. mergers: effective-dated mapping
df.join(mergers, (df.practice_code == mergers.old_code) & (df.month >= mergers.effective_month), "left")
  .withColumn("practice_code", F.coalesce("new_code", "practice_code"))

# 3. versioned lookup: the version valid THAT month
df.join(lookup, (df.practice_code == lookup.practice_code)
                & df.month.between(lookup.valid_from, lookup.valid_to), "left")
```

## Experiment results
| Mistake | Effect | Caught by |
|---|---|---|
| No key standardisation | 60 of 180 rows (a third) don't match, and **138,995** appointments are quarantined | Reconciliation (quarantine total is huge) |
| v2 for every month | HB05 appears in Jan–Mar and other boards are understated. **Totals still balance** (421,780 + 2,233) | Nothing automatic. Only domain knowledge ("HB05 didn't exist before April") or a check on board validity dates |
| Both versions, no month condition | Every row matches **twice**: out = **843,560**, about 2× | Reconciliation (in ≠ out + quarantined) |

Teaching point: **reconciliation catches losses and duplication, but not misallocation.** Misallocation needs **effective dating** and business checks.

## Discussion answers
- **Auto-fixing `W0001O`:** tempting, but it's a guess. Quarantine it and report it to the source owner. If the same typo keeps recurring, agree a **documented** correction rule with them.
- **Pre-merger codes:** we handle them (we must publish correctly today), *and* we tell the appointment team (fixing at source is cheaper for everyone). Integration work is half code, half **relationships**.

## Design principles shown
- **Standardise keys** before joining, in one shared function.
- **Effective-date** anything that changes over time (mergers, lookups). Never overwrite history.
- **Quarantine, don't drop.** Unmatched rows are counted and visible.
- **Reconcile:** totals in = out + quarantined, on every run.
- **Idempotent:** the same inputs give the same outputs, so it's safe to re-run (and to write with "overwrite partition", not "append").
- Reusable building blocks like these are what **de-utils**, **plumb-etl** and **DLH_Utils** provide. Check them before writing your own.
