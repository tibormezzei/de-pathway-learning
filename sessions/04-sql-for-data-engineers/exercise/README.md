# Exercise: answer business questions with SQL

**Time:** 20 minutes · **Work:** in pairs (one types, one reviews; swap after Q3)

You've been given a library service's data and a list of questions from the service manager.

## Setup

```bash
cd sessions/04-sql-for-data-engineers
python run_sql.py "SELECT * FROM loans LIMIT 5"
```

| Table | Rows | Grain (one row per…) |
|---|---|---|
| `branches` | 5 | branch |
| `branch_opening_hours` | 35 | branch **per day of week** |
| `members` | 200 | member |
| `books` | 80 | book in the catalogue |
| `loans` | 1,500 | loan (`return_date` is NULL if not yet returned) |

## Task

Write your answers in `exercise/questions.sql` and run it:

```bash
python run_sql.py exercise/questions.sql
```

Aim to finish **Q1–Q4** in the session. Q5–Q7 can be finished afterwards.

**Before you trust any answer, sanity-check it.** Does the total match `SELECT COUNT(*) FROM loans`? Is the number plausible?

## Discuss with your pair
- In Q3 and Q4, the queries **ran without errors** but gave the wrong numbers. How would you catch that in a real pipeline?
- In Q5, two books tie for a place. Which one should "win", and who decides?
