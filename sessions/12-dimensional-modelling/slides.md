---
marp: true
theme: default
paginate: true
header: "DE Learning Sessions · 12"
footer: "Data modelling II: dimensional modelling"
---

<!-- _class: lead -->
<!-- _header: "" -->
<!-- _footer: "" -->

# Data modelling II
## dimensional modelling

Session 12 · Module 3: Analysis and design

---

## Today

1. Why analytical models are different
2. Facts, measures, dimensions
3. Grain first
4. Star vs snowflake
5. Keys and the date dimension
6. Slowly changing dimensions
7. Conformed dimensions
8. **Homework:** design and build a star schema

---

## 3NF is for writing, not for analysing

Session 11's normalised model is ideal for an **operational** system: no duplication, no anomalies.

But to answer *"revenue by operator by month"* you may need **six joins**, and every analyst writes them slightly differently.

**Dimensional modelling** reshapes data for **reading and analysis**:
- few, predictable joins
- business-friendly names
- consistent answers

It **deliberately denormalises**, and that's fine because analytical data is written by the pipeline, not edited by users.

---

## Facts and dimensions

**Facts** are *measurements of a business process*, the numbers.
> a ticket sold: revenue £2.00, 1 journey

**Dimensions** are *the context*: who, what, where, when, how.
> on Route 7, at Stop 12, on 3 March, adult single, paid contactless

| | Fact table | Dimension table |
|---|---|---|
| Rows | Many (millions) | Few (tens to thousands) |
| Columns | Foreign keys + measures | Descriptive attributes |
| Used for | `SUM`, `COUNT`, `AVG` | `GROUP BY`, `WHERE` |

---

## Measures: can you add them up?

| Type | Can sum across… | Example |
|---|---|---|
| **Additive** | every dimension | revenue, journeys |
| **Semi-additive** | some dimensions, **not time** | account balance, stock level, headcount |
| **Non-additive** | nothing: recalculate from parts | response rate, average fare, ratios |

```sql
-- ❌ AVG of daily rates          ✅ recalculate from additive parts
SUM(completed) / SUM(issued)
```

Store the **additive parts**, and calculate ratios at query time.

---

## Grain first: the four steps

1. **Choose the business process:** ticket sales.
2. **Declare the grain:** *one row per ticket sold.*
3. **Identify the dimensions:** date, route, stop, fare type.
4. **Identify the facts:** revenue, journeys.

> The grain is a **promise** about what one row means. Every dimension and measure must be true **at that grain**.

Choose the **lowest grain available**. You can always aggregate up, but you can never drill down.

---

## Star schema

```
                 dim_date
                    │
  dim_stop ── fact_ticket_sale ── dim_route
                    │
              dim_fare_type
```

```sql
SELECT r.operator_name, d.year_month, SUM(f.revenue_gbp)
FROM fact_ticket_sale f
JOIN dim_route r USING (route_key)
JOIN dim_date  d USING (date_key)
GROUP BY ALL;
```

**One join per dimension**, always the same shape. Easy for people, BI tools and query engines.

---

## Star vs snowflake

```
  STAR                                SNOWFLAKE
  dim_route                           dim_route ── dim_operator ── dim_operator_group
  (route, operator_name, ...)         (route, operator_key)
```

| | Star | Snowflake |
|---|---|---|
| Dimensions | Denormalised, flat | Normalised into sub-tables |
| Joins | Fewer | More |
| Storage | A bit more repetition | Less repetition |
| Usability | **Simpler** | More complex |

**Default to a star.** Snowflake only when a sub-dimension is large, shared or changes independently.

---

## Keys and special dimensions

- **Surrogate keys** (`route_key` 1, 2, 3…) on dimensions. They're needed for type 2 history, because the same `route_id` gets several rows.
- **Date dimension**: a generated calendar, one row per day, with month, quarter, weekday, bank holiday and so on. Every date exists, even with no sales.
- **Degenerate dimension**: an ID kept on the fact with no dimension table (`ticket_id`).
- **Junk dimension**: a few low-cardinality flags grouped together (`payment_method`, …).

---

## Slowly changing dimensions

Route 7 moved from **Valley Buses** to **Coastline Travel** on 1 April. What should January's revenue show?

| Type | Behaviour | January revenue credited to |
|---|---|---|
| **0** | Never change | Valley Buses, forever, even after the change |
| **1** | **Overwrite**: no history | **Coastline Travel** ❌ (rewrites the past) |
| **2** | **New row** with validity dates | **Valley Buses** ✅ (as it was at the time) |
| 3 | Extra "previous value" column | Limited history (rare) |

Choose **per attribute**, based on what the business needs to report.

---

## Type 2 in practice

```
dim_route
route_key route_id operator_name     valid_from  valid_to    is_current
    7        7     Valley Buses      2020-01-01  2026-03-31  false
    8        7     Coastline Travel  2026-04-01  9999-12-31  true
```

Look up the version **valid when the event happened**:

```sql
JOIN dim_route dr
  ON dr.route_id = t.route_id
 AND CAST(t.sold_at AS DATE) BETWEEN dr.valid_from AND dr.valid_to
```

⚠️ Forget the date condition and route 7's tickets **fan out ×2** (session 04 again). **Check: fact rows = source rows.**

---

## Conformed dimensions

Several fact tables, **shared** dimensions:

| | dim_date | dim_route | dim_stop | dim_fare_type |
|---|---|---|---|---|
| fact_ticket_sale | ✔ | ✔ | ✔ | ✔ |
| fact_tap_journey | ✔ | ✔ | ✔ | |
| fact_service_punctuality | ✔ | ✔ | ✔ | |

- The same `dim_route` everywhere, so "Route 7" means the same thing in every report.
- This **bus matrix** is a planning tool: rows are business processes, columns are dimensions.

---

## CDP today → GCP tomorrow

| | CDP today | GCP tomorrow |
|---|---|---|
| Where stars live | Hive / Impala tables, SQL Server | **BigQuery** datasets |
| Building them | PySpark or SQL jobs | PySpark on Dataproc, or **SQL in BigQuery** (ELT) |
| Physical tuning | Partition Hive tables by date | **Partition** the fact by date, **cluster** by common filters |
| Alternatives | Mostly stars | Stars **or** wide denormalised tables with **nested / repeated** fields |
| SCD2 | Hand-built in Spark | Hand-built, or `MERGE` statements in BigQuery |

**Carries over unchanged:** grain, facts, dimensions, SCD logic. All of today.
**Really changes:** BigQuery makes very wide tables cheap, so you'll see more "one big table" designs. The grain discipline still applies.

---

## Summary

- Analytical models **denormalise on purpose** for simple, consistent querying.
- **Facts** (measures) + **dimensions** (context). Store **additive** parts.
- **Declare the grain first**: the lowest available.
- **Star by default**, snowflake only with good reason.
- **SCD type 2** keeps history: new rows, validity dates, and a date-aware join.
- **Conformed dimensions** make every report agree.

---

## Homework

`homework/README.md`

1. **Design** a star schema for the bus ticketing system: grain, facts, dimensions, SCD types.
2. **Build** it in DuckDB from the operational tables.
3. **Answer** 3 business questions. One needs type 2 history.

Check: **fact rows = 20,000**, and Route 7 revenue is credited to the right operator.

**Next session:** data integration design.
