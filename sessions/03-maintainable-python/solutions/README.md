# Reference solution: session 03 homework

```bash
cd solutions
python -m survey_pipeline --input ../data/survey_responses.csv --output ../output/response_rates.csv
python ../homework/check_output.py ../output/response_rates.csv     # PASS
python -m pytest -q tests                                          # 4 passed
```

This is **one** good answer, not the only one. When reviewing learners' work, look for the principles, not for this exact layout.

## What changed and why

| Original | Refactored | Principle |
|---|---|---|
| One 80-line top-level script | `clean.py`, `metrics.py`, `config.py`, `__main__.py` | Separation of concerns |
| `df`, `df2`, `df3`, `tmp`, `rr` | Descriptive names, chained `.pipe()` steps | Readability (PEP 8, PEP 20) |
| `16`, `120`, `0.5`, `"sth"` buried in code | `config.py` | Business rules in one visible place |
| Hard-coded `../data/...` paths | `--input` / `--output` arguments | Runs anywhere: laptop, CML, Dataproc |
| Bare `except:` ×3 nested | `parse_date` loops over `DATE_FORMATS`, catching specific errors | Never swallow every error |
| Row loops (`for i in range(len(df))`) | Vectorised `.str`, `.replace`, `groupby().agg()` | Fast, idiomatic pandas, and it translates to PySpark |
| Nested loop over region × month | One `groupby` | Simpler and much faster |
| `print` debugging | `logging` | Configurable, visible in platform logs |
| Untestable | Small pure functions with tests | Testability (→ session 06) |

## Questionable things to spot (reflection question 2)
1. **Unparseable dates.** The original turns them into `None`, then `.strftime()` would crash on them. It only works because every date in this dataset happens to parse. That's fragile.
2. **Deduplication happens after the age filter.** If a case's first submission has an invalid age and the second is valid, the valid one is kept. If both are valid, the *first* is kept regardless of which is more complete. Is that the intended rule?
3. **"Issued"** is really "valid interviews recorded", not cases issued. The metric's name may mislead stakeholders.
4. **A partial counts as half a response.** Is this a documented, agreed definition?
5. **Silent zero.** `rr = 0` when `issued == 0` would show "0% response" for a region with no cases, which isn't the same thing.

Points 2–5 are **questions for stakeholders**, not things to fix on your own. This links to session 17 (communicating) and session 14 (documenting business rules).
