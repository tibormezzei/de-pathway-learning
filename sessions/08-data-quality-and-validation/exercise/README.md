# Exercise: validate, quarantine, report

**Time:** 20 minutes · **Work:** in pairs

The business survey team receives monthly returns. Before they go into the pipeline, every row must meet the team's rules. Bad rows go to **quarantine** for follow-up, and good rows carry on.

## Setup

```bash
cd sessions/08-data-quality-and-validation
python exercise/validate_returns.py
```

The starter schema checks `ru_ref` and `turnover` only, so it catches 7 bad rows. **There are more problems in the data than that.**

## Task

1. Open `exercise/validate_returns.py`. The rules are in the docstring at the top.
2. Complete the schema: `period`, `sic_code`, `region`, `employees`, uniqueness of `(ru_ref, period)`, and `strict=True`.
3. Run it after each addition and watch the quarantine count go up.
4. Look at the quarantined rows (`print(quarantined)`). For each kind of problem, decide:
   - **Can the pipeline fix it automatically and safely?** (e.g. trailing whitespace)
   - **Does it need to go back to the supplier or business area?**

## Questions
- Why does `read_returns()` read `sic_code` as text? What happens if you remove that?
- The duplicate check quarantines **both** copies of each duplicate. Is that right for *exact* duplicates? What about two *different* returns for the same business and period?
- `lazy=True`: what changes if you remove it?

## Stretch
1. Add the **cross-field** rule as a **warning**, not a failure:
   `pa.Check(lambda df: <boolean Series>, name="...", raise_warning=True)` at the DataFrame level (`checks=[...]`).
2. Write the failure report to CSV in a form the survey team could act on: one row per problem, with `ru_ref`, `period`, the column, the rule broken and the bad value.
