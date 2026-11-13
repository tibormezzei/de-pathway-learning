# Homework: design and build a star schema

**Time:** about 2 hours · **Due:** start of session 13

A regional transport authority wants a reporting model over its bus ticketing system. The operational tables are in `data/`:

| Table | Grain |
|---|---|
| `tickets` | one ticket sold (20,000, Jan–Jun 2026) |
| `route_operator` | one row per route **per period an operator ran it** (note route 7!) |
| `operators` | operator |
| `stops` | stop (with area and fare zone) |
| `fare_types` | fare type (with a concession flag) |

The authority's questions:
1. **Journeys and revenue by operator and month**
2. **Share of journeys on concessionary fares, by area**
3. **Route 7 changed operator on 1 April. Show route 7 revenue per month, credited to the operator running it at the time.**

## Part 1: design (on paper, about 45 min)

Fill in `design_template.md`:
1. **Grain:** what does one row in your fact table represent? (Decide this first.)
2. **Fact table:** foreign keys and **measures**. Are the measures additive?
3. **Dimensions:** which ones, and which attributes go in each?
4. **Slowly changing dimensions:** for each dimension, type 1 (overwrite) or type 2 (keep history)? Why?
5. Draw the star.

## Part 2: build it (DuckDB, about 1 hour)

Write `homework/my_star.sql` (CREATE TABLE … AS SELECT … from the operational tables) and `homework/my_questions.sql` (the 3 questions, using **only** your star tables), then:

```bash
python homework/run.py homework/my_star.sql homework/my_questions.sql
```

Checks:
- [ ] The fact table has **exactly as many rows as `tickets`** (no fan-out, nothing lost).
- [ ] Question 3 credits January–March to **Valley Buses** and April–June to **Coastline Travel**.

## Part 3: reflect (a few sentences)
- What would question 3 show if `dim_route` were **type 1**? Who would be misled?
- Where did you put `operator`: its own dimension, inside `dim_route`, or a snowflake? Why?

## Stretch
- Add a `dim_date` with weekday or weekend, and answer "weekend vs weekday journeys by area".
- What would change if the authority also wanted **passenger journeys from smartcard tap-in/tap-out data**? Is that a new fact table or the same one?
