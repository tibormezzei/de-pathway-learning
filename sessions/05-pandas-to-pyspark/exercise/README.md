# Exercise: one transformation, three ways

**Time:** 20 minutes · **Work:** in pairs

A city bike-hire scheme wants to know:

> For valid trips (duration above 0 and at most 180 minutes), what are the **trip count** and **average duration** for each **start station** and **member type**? Show the 10 busiest combinations.

| File | Rows | Columns |
|---|---|---|
| `data/trips.csv` | 60,000 | trip_id, start_station_id, end_station_id, start_time, duration_min, member_type |
| `data/stations.csv` | 20 | station_id, station_name, capacity |

## Task

`exercise/three_ways.py` already has a **pandas** version. Write:

1. **PySpark:** fill in `with_pyspark()`.
2. **SQL:** write one query in `SQL`. The same query runs in both **DuckDB** and **Spark SQL**.

Then run:

```bash
python exercise/three_ways.py
```

You're done when all three comparisons print `True`.

## Then read the plan

The script prints `spark_df.explain()`. Find:
- [ ] The **`Exchange`**: where is data shuffled between partitions, and why?
- [ ] **`HashAggregate`** appears **twice**. Why? (Hint: `partial_count`.)
- [ ] What kind of **join** did Spark choose? Why is that sensible for a 20-row table?
- [ ] **`PushedFilters`** and **`ReadSchema`**: what is Spark avoiding reading?

## Discuss
- Which version was easiest to write? Easiest to read? Easiest to test?
- At 60,000 rows, pandas is probably fastest. At 600 million rows, which versions still work?

## Stretch
1. Add `.cache()` and call `.count()` twice. Then remove it. What changes, and when is caching worth it?
2. Replace `F.round(F.avg(...), 1)` with a Python UDF that does the same thing. Compare the plan, and time it if you can.
