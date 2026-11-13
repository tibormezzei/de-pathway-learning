---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 05"
footer: "From pandas to PySpark: thinking distributed"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# From pandas to PySpark
## thinking distributed

Session 05 · Module 1: Foundations of building

---

## Today

1. Three tools, one job
2. How Spark works: driver, executors, partitions
3. Lazy evaluation
4. Narrow vs wide transformations, and shuffles
5. pandas ↔ PySpark ↔ SQL
6. Anti-patterns
7. Reading `explain()`
8. **Exercise:** one transformation, three ways

---

## Three tools, one job

| | **pandas** | **PySpark** | **SQL engine** |
|---|---|---|---|
| Runs on | One machine, in memory | A cluster (or a laptop in local mode) | The database or warehouse |
| Comfortable size | Up to a few GB | GB → TB+ | GB → PB (BigQuery) |
| Strengths | Fast to explore, rich API | Scale, complex pipelines, Python + SQL | Declarative, set-based, often fastest |
| Watch out | Out of memory | Overheads on small data, harder to debug | Complex logic gets unreadable |

**Rule of thumb:** small → pandas or DuckDB. Big, or in production on the platform → PySpark or SQL.

---

## How Spark works

```
                ┌──────────────┐
  your code ──▶ │    DRIVER    │  plans the work, collects results
                └──────┬───────┘
          ┌────────────┼────────────┐
     ┌────▼────┐  ┌────▼────┐  ┌────▼────┐
     │EXECUTOR │  │EXECUTOR │  │EXECUTOR │   do the work in parallel
     │ p1  p2  │  │ p3  p4  │  │ p5  p6  │   one task per partition
     └─────────┘  └─────────┘  └─────────┘
```

- A DataFrame is split into **partitions**, which are chunks of rows.
- Each executor processes its partitions **independently**.
- The **driver** is one machine. Anything you `collect()` to it has to fit there.

---

## Lazy evaluation

**Transformations** build a plan, and nothing runs yet:
```python
valid  = trips.filter(F.col("duration_min") > 0)        # lazy
joined = valid.join(stations, "station_id")              # lazy
result = joined.groupBy("station_name").count()          # lazy
```

**Actions** run the whole plan:
```python
result.show()       result.count()      result.write.parquet(...)
result.collect()    result.toPandas()
```

Why lazy? Spark sees the **whole** plan and **optimises** it: it pushes filters down, prunes columns and picks join strategies.

⚠️ Each action re-runs the plan from scratch unless you `cache()`.

---

## Narrow vs wide transformations

**Narrow:** each output partition needs **one** input partition, so there's no data movement.
> `filter`, `select`, `withColumn`, `union`

**Wide:** output needs rows from **many** partitions, so data is **shuffled** across the network.
> `groupBy`, `join` (usually), `distinct`, `orderBy`, `window`

```
narrow:   p1 → p1'    p2 → p2'    p3 → p3'

wide:     p1 ─┐ ┌─▶ p1'
          p2 ─┼─┼─▶ p2'      ← every partition sends data to every other
          p3 ─┘ └─▶ p3'
```

**Shuffles are the most expensive part of most Spark jobs.**

---

## Joins: broadcast vs shuffle

| | Broadcast hash join | Sort-merge join |
|---|---|---|
| When | One side is **small** (lookup tables) | Both sides are large |
| How | Small table copied to every executor | Both sides shuffled by key, then merged |
| Cost | Cheap, no shuffle of the big table | Two shuffles |

```python
from pyspark.sql.functions import broadcast
trips.join(broadcast(stations), "station_id")      # hint, if Spark doesn't choose it itself
```

Session 04's lessons still apply: **check the grain**, and watch for **lost rows** and **fan-out**.

---

## pandas ↔ PySpark ↔ SQL

| pandas | PySpark | SQL |
|---|---|---|
| `df[df.x > 0]` | `df.filter(F.col("x") > 0)` | `WHERE x > 0` |
| `df[["a", "b"]]` | `df.select("a", "b")` | `SELECT a, b` |
| `df.assign(y=df.x * 2)` | `df.withColumn("y", F.col("x") * 2)` | `SELECT x * 2 AS y` |
| `df.merge(o, on="k", how="left")` | `df.join(o, "k", "left")` | `LEFT JOIN o USING (k)` |
| `df.groupby("k").agg(n=("x","count"))` | `df.groupBy("k").agg(F.count("x").alias("n"))` | `GROUP BY k` + `COUNT(x) AS n` |
| `df.sort_values("x", ascending=False)` | `df.orderBy(F.desc("x"))` | `ORDER BY x DESC` |
| `df.drop_duplicates(["k"])` | `df.dropDuplicates(["k"])` | `ROW_NUMBER() ... = 1` |

**Same concepts, different syntax.** Spark SQL and the DataFrame API compile to **the same plan**.

---

## Anti-patterns

| ❌ Don't | ✅ Do |
|---|---|
| `df.toPandas()` / `collect()` on big data | Aggregate first, or write the output |
| Python UDFs for things `F.` can do | Built-in `pyspark.sql.functions` |
| `for` loops calling `withColumn` 100 times | One `select` with a list of expressions |
| `count()` after every step "to check" | Count once, at the end, or log it |
| Writing thousands of tiny files | `repartition` / `coalesce` sensibly before writing |
| Row-by-row thinking | Columns and groups (session 03!) |
| CSV everywhere | Parquet: columnar, typed, filters pushed down |

---

## Reading `explain()`

```text
TakeOrderedAndProject(limit=10, ...)
+- HashAggregate(keys=[station_name, member_type], count, avg)
   +- Exchange hashpartitioning(station_name, member_type)    ← SHUFFLE
      +- HashAggregate(partial_count, partial_avg)            ← pre-aggregate
         +- BroadcastHashJoin LeftOuter                       ← small table broadcast
            :- Filter (duration_min > 0 ...)
            :  +- FileScan csv [4 columns] PushedFilters: [...]
            +- BroadcastExchange
```

Read it **bottom-up**. Look for:
- **`Exchange`** = shuffle. How many are there? Are they needed?
- **Join type**: broadcast or sort-merge?
- **`PushedFilters` / `ReadSchema`**: is Spark reading only what it needs?

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Where Spark runs | CML sessions on a shared, long-running cluster | **Dataproc** clusters (often **ephemeral**, per job) or **Dataproc Serverless** |
| Starting Spark | Session config in CML | Cluster or batch config: machine types, number of workers, autoscaling |
| Data | HDFS / S3 / Hive tables | `gs://` paths, **BigQuery** via the Spark BigQuery connector |
| Cost | Shared capacity | **You pay per cluster-minute**: oversized clusters and idle notebooks cost money |
| Spark UI | CML session UI | Dataproc web interfaces / persistent history server |

**Carries over unchanged:** the DataFrame API, laziness, shuffles, plans. Everything today.
**Really changes:** sizing and cost become **your** concern, and jobs must run without anyone at the keyboard.

---

## Summary

- **pandas** for small data, **PySpark/SQL** for scale and production.
- Spark: **driver + executors + partitions**.
- **Lazy**: transformations build a plan, and actions run it.
- **Wide transformations shuffle**, and shuffles are expensive. **Broadcast** small lookups.
- DataFrame API and Spark SQL are **the same thing underneath**.
- Read the plan **bottom-up** and look for `Exchange`.

---

## Exercise (20 min, in pairs)

```bash
python exercise/three_ways.py
```

- The **pandas** version of a bike-hire query is done.
- Write the **PySpark** version and **one SQL query** (it runs in DuckDB *and* Spark SQL).
- Done when all comparisons print **True**.
- Then answer the questions about the **physical plan**.

**Next session (Module 2):** testing fundamentals.
