# Homework: document the integrated dataset

**Time:** about 1.5 hours · **Due:** start of session 15

In session 13 you built **GP appointments by health board per month**. Before anyone outside the team uses it, it needs documenting. Undocumented data isn't finished.

## Part 1: data dictionary (machine-checkable)

Complete `homework/data_dictionary.csv`, with one row per **output column**:

| Heading | What to write |
|---|---|
| `column_name` | Exactly as in the output |
| `data_type` | Spark type as Spark reports it: `string`, `bigint`, `double`, … |
| `description` | What it means, for someone who's never seen the pipeline |
| `nullable` | `yes` / `no` |
| `allowed_values` | Optional: permitted values separated by `\|` |
| `example` | A real example value |
| `source` | Source system, table and column |
| `transformation` | What the pipeline does to it |

Then check it against the real data:

```bash
cd sessions/14-metadata-and-governance
python homework/check_dictionary.py homework/data_dictionary.csv
```

Keep going until you see **PASS**. (It runs the session 13 pipeline, which takes about 20s.)

## Part 2: source-to-target mapping

Complete `homework/source_to_target.md`: where every target column comes from, the row-level rules (standardisation, mergers, lookup versions, exclusions) and what must reconcile.

## Part 3: dataset-level metadata

Complete `homework/dataset_metadata.yaml`. Some fields need **governance** thinking:
- Who is the **Information Asset Owner**, and what do they approve?
- Is there any **personal data**? Explain your answer.
- What are the **disclosure** considerations? Would a practice-level version be different?
- What **quality notes** must a user know before using it? (Hint: what changed in April?)

## Reflect
- Which part of the metadata would have saved *you* the most time if it had existed for the session 13 sources?
- The checker treats metadata as **code**: tested on every run. What would break if the pipeline added a column and nobody updated the dictionary?

## Stretch
Add the check to a test (`tests/test_metadata.py`) so CI fails when the dictionary and the output drift apart.
