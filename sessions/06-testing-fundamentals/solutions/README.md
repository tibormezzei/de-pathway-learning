# Reference solution: session 06

```bash
python -m pytest -v solutions            # fixed module: 46 passed
python -m pytest -v solutions --buggy    # exercise module: 9 failed, 37 passed
```

## The 4 bugs

| Function | Bug | Test that catches it | Fix |
|---|---|---|---|
| `age_band` | 64 returns `"65+"` (`< 64` should be `<= 64`) | boundary case `(64, "45-64")` | `if age <= 64` |
| `response_rate` | `issued == 0` raises `ZeroDivisionError` instead of returning `None` | `response_rate(0, 0) is None` | guard clause |
| `parse_bool` | case-sensitive, so `"YES"` raises | parametrised upper/mixed-case values | `.strip().lower()` |
| `normalise_postcode` (sneaky) | only removes **spaces**, so a tab or newline (common in pasted or CSV data) survives | `"\tnp108xg\n"` | `"".join(raw.split())` |

## Teaching points
- **Boundaries find bugs.** The `age_band` bug is invisible to "typical" values like 30 or 70. Test both sides of every edge.
- **Test the spec, not the implementation.** Reading the code first leads you to test what it *does*. Reading the docstring leads you to test what it *should* do.
- **Error cases are part of the spec.** `pytest.raises` tests are as important as the happy path.
- **Coverage isn't correctness.** The starter tests already execute most lines of the buggy functions. Coverage tells you what *isn't* tested, never that what *is* tested is right.
- **The doctests in `normalise_postcode` pass** on the buggy code. Examples are useful documentation, but they rarely include the awkward cases.
