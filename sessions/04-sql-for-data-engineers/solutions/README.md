# Reference answers: session 04

```bash
python run_sql.py solutions/answers.sql
```

Expected results (with the data from `make_data.py`, seed 4):

| Q | Answer |
|---|---|
| 1 | Riverside 343 · Harbourside 306 · Hilltop 304 · Central 286 · Old Town 261 (total 1,500 ✔) |
| 2 | **30** members have never borrowed |
| 3 | INNER JOIN keeps 1,487 of 1,500, so **13 orphan loans** (book_ids 9xx, not in the catalogue) |
| 4 | Broken query gives **7×** counts (e.g. Riverside 2,401 = 343 × 7). Fix: `AND h.day_of_week = 'Sat'` in the join |
| 5 | e.g. Riverside: The Hidden Archive 17, then **a tie at 12** (The Broken Orchard / The Broken River) |
| 6 | **173** still on loan, **19** overdue |
| 7 | Branch 1: Jan 50, Feb 35 (−15), Mar 43 (+8), Apr 45 (+2), May 52 (+7), Jun 61 (+9) |

## Teaching points

**Q2: anti-join.** `LEFT JOIN ... WHERE right.key IS NULL` finds "things with no match". `NOT EXISTS` also works and is often clearer:
```sql
SELECT COUNT(*) FROM members m
WHERE NOT EXISTS (SELECT 1 FROM loans l WHERE l.member_id = m.member_id);
```

**Q3: INNER JOINs drop rows silently.** No error is raised. In pipelines, **compare row counts before and after joins**, and check for orphans explicitly. This comes back in sessions 8 (validation) and 13 (integration).

**Q4: fan-out.** `branch_opening_hours` has grain *branch × day*, so each loan matches 7 rows. Before joining, always ask: **"what's the grain of each table, and is my join key unique on the right-hand side?"** A quick check:
```sql
SELECT branch_id, COUNT(*) FROM branch_opening_hours GROUP BY 1 HAVING COUNT(*) > 1;
```

**Q5: ties.** `ROW_NUMBER` picks one arbitrarily unless you add a tie-breaker (here `title`). `RANK` gives both tied rows the same rank (and could return 4 rows), and `DENSE_RANK` doesn't skip ranks. Which one is right is a **business decision**: ask, then document it.

**Q6: NULLs.** `COUNT(return_date)` ignores NULLs, while `COUNT(*)` doesn't. `WHERE return_date = NULL` never matches, so you have to use `IS NULL`.
