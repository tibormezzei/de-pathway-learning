# Exercise: model the survey field operation

**Time:** 20 minutes · **Work:** in groups of 3–4, on a whiteboard, paper or a shared diagram

Read `scenario.md`. Look at the first rows of `data/case_visits_flat.csv`.

## Part 1: conceptual model (about 7 min)

From the scenario **only**, with no columns yet:
1. List the **entities** (the nouns that matter to the business).
2. Draw the **relationships** between them and label each with a verb ("an interviewer *makes* visits").
3. Mark the **cardinality** of each relationship: one-to-one, one-to-many or many-to-many.

Check: can your diagram answer *"who visited this address, for which survey, and what happened?"*

## Part 2: logical model by normalising the spreadsheet (about 13 min)

The flat file has one row per visit and 14 columns. Normalise it to **third normal form**:
1. Which columns **repeat** the same values over and over? Which groups of columns describe the same "thing"?
2. Split them into tables. For each table, choose a **primary key** and add **foreign keys**.
3. Test each non-key column: does it depend on **the key, the whole key, and nothing but the key**?

Check against your conceptual model. Do the tables match the entities? If not, which one is wrong?

## Questions to discuss
- Is `case` the same thing as `address`? Why does that distinction matter?
- What is the primary key of a **visit**?
- Interviewers have a region and addresses have a region. Are those the same relationship? What happens when someone covers a neighbouring region?
- What *isn't* in the data that the scenario mentions (e.g. the visit limit, a name change over time)?

## Stretch: physical model
Write `CREATE TABLE` statements (DuckDB) with types, primary keys, foreign keys and `NOT NULL`. Then load the flat file into your tables and prove you haven't lost anything by rebuilding the flat view with joins.

```python
import duckdb
con = duckdb.connect()
con.execute(open("exercise/my_schema.sql").read())          # your CREATE TABLEs
con.execute("CREATE VIEW flat AS SELECT * FROM read_csv_auto('data/case_visits_flat.csv', all_varchar=true)")
# INSERT INTO ... SELECT DISTINCT ... FROM flat;  then rebuild the flat view with joins and compare
```
