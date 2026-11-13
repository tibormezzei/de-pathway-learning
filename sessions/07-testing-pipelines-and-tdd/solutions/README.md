# Reference solution: session 07

```bash
python -m pytest -v solutions        # 13 passed (about 30s, mostly Spark start-up)
```

`meter_cleaning.py` is one possible end state. Pairs will get there by different routes, and that's fine.

## Points to draw out

**Hand-built test data.** Every test builds 1–4 rows inline. You can see the input and the expected output side by side, and each row has a reason to be there (e.g. "resubmitted later: wins"). Compare that with "run it on last month's extract and eyeball it".

**Dummy vs synthetic data.**
- *Dummy*: small, hand-made, chosen to hit specific cases. Best for unit tests.
- *Synthetic*: generated to look like real data statistically (Faker, SMOTE, etc.). Good for volume and integration tests and for sharing. **Label it clearly**, and remember it isn't automatically non-disclosive.

**I/O at the edges.** None of these functions reads or writes files. They take a DataFrame and return a DataFrame, so tests need no real data, paths or cluster. The read and write live in a thin entry point that's covered by an integration test. This is the idea behind "Stop using mocks" (a fake or in-memory input beats a mock of `spark.read`).

**The R4 trap.** If you flag first and then dedupe on "latest *valid*" reading, you get different results. Neither is "correct" until the business decides. The test **documents the decision**: `test_clean_readings_latest_submission_wins_even_if_invalid`.

**Spark testing hygiene.**
- One `SparkSession` per run (`scope="session"`) instead of one per test.
- `spark.sql.shuffle.partitions = 1` for tiny data. The default of 200 makes window and groupBy tests slow.
- `assertDataFrameEqual` checks schema **and** rows, ignoring order. Use `assertSchemaEqual` for schema only.
