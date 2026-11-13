# Reference solution: session 05

```bash
python solutions/three_ways.py
```

Expected: all three comparisons print `True`. Top row: **Museum North, member, 3,142 trips, 16.0 min**.

## Reading the plan (abridged)

```text
TakeOrderedAndProject(limit=10, orderBy=[trips DESC, ...])         ← orderBy + limit fused: top-10 per partition, then merged
+- HashAggregate(keys=[station_name, member_type], count, avg)     ← final aggregate
   +- Exchange hashpartitioning(station_name, member_type, 4)      ← THE SHUFFLE
      +- HashAggregate(... partial_count, partial_avg)             ← pre-aggregate on each partition first
         +- BroadcastHashJoin LeftOuter, BuildRight                ← small table copied to every executor
            :- Filter (duration_min > 0 AND <= 180)
            :  +- FileScan csv [trip_id, start_station_id, duration_min, member_type]
            :       PushedFilters: [...]   ReadSchema: only 4 columns     ← filter pushdown + column pruning
            +- BroadcastExchange
               +- FileScan csv [station_id, station_name]
```

| Question | Answer |
|---|---|
| Exchange | `groupBy` needs all rows for one key in the same partition, so data is redistributed by hash of the key. This is a **wide** transformation. |
| Two HashAggregates | Spark **pre-aggregates** within each partition (partial count/sum) so less data is shuffled, then combines the partial results. |
| Join type | **Broadcast hash join**: `stations` is tiny, so it's copied to every executor and `trips` doesn't need shuffling for the join. |
| Pushed filters / ReadSchema | Spark reads only the 4 columns it needs and applies the filter as early as possible. With **Parquet** this skips data on disk; with CSV it still has to parse each line. |

## Discussion points
- **Lazy evaluation:** nothing ran until `.toPandas()` (an *action*). `.explain()` shows the plan without running it.
- **The plans are identical:** Spark SQL and the DataFrame API compile to the **same plan**. Choose whichever is clearer for the team.
- **Scale:** pandas needs everything in one machine's memory. Spark and SQL engines distribute the work.
- **`toPandas()` is safe here** because the result is 10 rows. On a full dataset it pulls everything onto the driver, which is the classic out-of-memory error.

## Stretch answers
1. **Cache:** the first `count()` reads the CSV and fills the cache, and the second reads from memory. It's worth it only when the same DataFrame is reused several times. Otherwise it wastes memory.
2. **Python UDF:** the plan shows `BatchEvalPython`, which means rows are serialised from the JVM to Python and back. It's much slower than built-in `F.` functions, so check `pyspark.sql.functions` before writing a UDF.
