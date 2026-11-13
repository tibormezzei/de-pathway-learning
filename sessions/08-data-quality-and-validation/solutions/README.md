# Reference solution: session 08

```bash
python solutions/validate_returns.py
```

Expected result: **404 rows → 372 valid, 32 quarantined**, plus one warning.

## Answer key (from `data/make_data.py`)

| Planted problem | Rows | Caught by |
|---|---|---|
| `ru_ref` not 11 digits | 4 | `str_matches(^\d{11}$)` |
| `period` invalid (`202613`, `2026-03`, `202612`) | 3 | `isin(VALID_PERIODS)` |
| `sic_code` lost its leading zero (`1110`) | 5 | `str_matches(^\d{5}$)` |
| `region` misspelt or badly formatted (`Londn`, `wales`, `Scotland `) | 4 | `isin(REGIONS)` |
| `employees` missing | 6 | `nullable=False` |
| `turnover` negative | 3 | `ge(0)` |
| Duplicate `(ru_ref, period)` | 4 pairs (8 rows) | `unique=[...]`, `report_duplicates="all"` |
| Zero employees, turnover > £1m | 3 | DataFrame-level check, `raise_warning=True` |

32 quarantined rather than 33 because one row has two problems.

## Discussion answers

**Fix automatically or refer back?**
| Problem | Suggested handling |
|---|---|
| `"Scotland "`, `"wales"` | **Auto-fix** (trim, standardise case) *before* validation, and log that you did |
| `"Londn"` | Refer back. Fuzzy-matching is guessing |
| `sic_code` `1110` | Probably a lost leading zero, but **refer back or fix only under an agreed, documented rule** |
| Missing `employees`, negative turnover, bad `ru_ref` / `period` | Refer back to the supplier |
| Exact duplicates | **Auto-dedupe** (keep one) before validation |
| Conflicting duplicates (same key, different values) | Quarantine both, because you can't know which is right |
| Zero employees, high turnover | **Warn**. It may be legitimate (e.g. a holding company). A human decides |

**Reading codes as text.** Without `dtype=str`, pandas reads `01110` as the integer `1110`. The data loses information **on read**, before any check can see it. Codes, IDs and postcodes are **text**, even when they look like numbers. (Excel does the same thing, which is likely how the real-world `1110`s arose.)

**`lazy=True`.** Without it, Pandera stops at the **first** failing check. With it, you get **every** failure in one report, which is what you want for quarantining and for sending feedback to suppliers.

## Fail, quarantine or warn?
- **Fail the whole run:** the problem makes *everything* untrustworthy (schema changed, file empty, wrong period delivered).
- **Quarantine rows:** individual records are bad, but the rest are fine.
- **Warn:** plausible but unusual, so it needs a human eye.

Agree these with the business area and **document them** (→ session 14).
