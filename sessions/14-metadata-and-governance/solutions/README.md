# Reference solution: session 14

```bash
python homework/check_dictionary.py solutions/data_dictionary.csv     # PASS
```

Files:
- `data_dictionary.csv`: 5 columns, types matching Spark's (`string`, `bigint`), allowed values for board code and name
- `source_to_target.md`: column mappings, row rules, reconciliation
- `dataset_metadata.yaml`: DCAT/Dublin Core-style dataset metadata with governance fields

## What good looks like
- **Descriptions** a newcomer could understand. "Total GP appointments recorded by practices in the board that month" beats "sum of appointments".
- **Transformations** that state business rules explicitly (lookup version by month, merger mapping) rather than "joined to lookup".
- **Quality notes** that warn users about real limitations: the April board change breaks like-for-like comparison, the quarantine volume, and the unconfirmed "booked vs attended" meaning.
- **Governance fields** answered properly or marked "unknown: ask X". Never guessed.

## Governance answers
- **Information Asset Owner:** a senior role accountable for the data asset. They approve its uses and sharing and accept the risks. Not the engineer.
- **Personal data:** no. The data is practice-level counts aggregated to board, with no patients or staff. (Practice *names* identify organisations, not people.)
- **Disclosure:** board-level counts are large, so the risk is low. A **practice-level** or small-area output would need a **DisCO** check before leaving the secure environment.
- **Security classification:** OFFICIAL is typical for aggregate operational data, but check your area's handling guidance.

## Common mistakes the checker catches
- `int` or `long` instead of Spark's `bigint`; `str` instead of `string`
- Documenting a column that was renamed, or missing a new one
- `nullable = no` on a column that actually has nulls
- An `allowed_values` list that's missing `HB05` (it only appears from April)
