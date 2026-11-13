# Session 12: Data modelling II: dimensional modelling

| | |
|---|---|
| Module | 3: Analysis and design |
| Wiki skill(s) | Data modelling (Working); Data development process: star vs snowflake, fact and dimension tables; Data integration: slowly changing dimensions |
| HEO target level | Working |
| Duration | 60 min (~35 concept / ~20 homework briefing + worked mini-example / ~5 Q&A) |
| Follow-up | **Homework** (design + build takes longer than 20 min) |
| Prerequisites | Sessions 04 (SQL, grain, windows) and 11 (normalisation, keys) |
| Dataset | Synthetic bus ticketing system: `data/*.csv` (5 tables, 20k tickets), regenerate with `data/make_data.py` |

## Learning outcomes
By the end of the session, participants can:
1. Explain why analytical models differ from operational (3NF) models.
2. Identify facts, measures (additive, semi-additive, non-additive) and dimensions.
3. **Declare the grain** of a fact table and explain why it comes first.
4. Compare star and snowflake schemas.
5. Choose between slowly changing dimension types 1 and 2, and implement a type 2 join.
6. Explain conformed dimensions.

## Concept outline
| Min | Section |
|---|---|
| 0–4 | 3NF is great for writing data, painful for analysing it |
| 4–9 | Facts, measures, dimensions |
| 9–14 | Grain: the four-step design process |
| 14–19 | Star vs snowflake |
| 19–22 | Surrogate keys, the date dimension, degenerate dimensions |
| 22–29 | Slowly changing dimensions: types 0, 1, 2 (and 3) |
| 29–32 | Conformed dimensions, bus matrix |
| 32–35 | CDP today → GCP tomorrow |
| 35–50 | Homework briefing + design the grain and dimensions together on the whiteboard (no SQL) |
| 50–60 | Q&A |

## Homework
- **Task:** design a star schema for a bus ticketing system, build it in DuckDB from the operational tables, and answer 3 business questions, one of which needs a type 2 dimension.
- **Starting files:** `homework/README.md`, `homework/design_template.md`, `homework/run.py`
- **Done when:** fact rows = tickets (20,000), and Q3 credits Jan–Mar to Valley Buses and Apr–Jun to Coastline Travel.
- **Stretch:** date dimension questions; tap-in/tap-out as a second fact table.
- **Reference:** `solutions/build_star.sql`, `solutions/questions.sql`, `solutions/build_star.py`, `solutions/README.md`

## Further learning (from the wiki)
- [Star schema vs snowflake schema (GeeksforGeeks)](https://www.geeksforgeeks.org/difference-between-star-schema-and-snowflake-schema/)
- Hoberman, *Data Modelling Made Simple*: dimensional chapters
- DAMA-DMBOK2: data warehousing and BI chapter (ONS Data Architecture SharePoint)
- Kimball & Ross, *The Data Warehouse Toolkit*: the classic reference (not on the wiki, but widely available)
- [Cloud Skills Boost: BigQuery data warehousing labs](https://www.cloudskillsboost.google/) (GCP preparation)

## Facilitator notes
- In the briefing, agree the **grain** as a room before anyone leaves. It prevents most homework problems.
- Don't reveal route 7's change. Let people find it in `route_operator.csv`, which reinforces session 10 (profile first!).
- People who join on `route_id` alone get 20,000+ fact rows. The README's row-count check is there to catch exactly that.
