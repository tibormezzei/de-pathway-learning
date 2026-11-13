# Reference solution: session 12

```bash
python solutions/build_star.py
```

## Design

**Grain:** one row per **ticket sold**, the lowest level available. You can always aggregate up, but you can never drill down below the grain.

```
                    dim_date
                (date_key, year_month,
                 day_name, is_weekend)
                        │
 dim_stop ───── fact_ticket_sale ───── dim_route  (TYPE 2)
 (area,         ticket_id (degenerate)  (route_id, operator_name,
  fare_zone)    date_key, route_key,     valid_from, valid_to,
                stop_key, fare_type_key, is_current)
                payment_method
                revenue_gbp, journeys
                        │
                  dim_fare_type
                 (is_concession)
```

| Decision | Choice | Why |
|---|---|---|
| Measures | `revenue_gbp`, `journeys` (= 1 per ticket) | Both **fully additive**, so they can be summed across any dimension |
| `dim_route` | **Type 2**, with operator **folded in** | The business needs revenue credited to the operator *at the time*. Folding operator in avoids a snowflake join |
| `dim_stop`, `dim_fare_type` | Type 1 | No requirement for history |
| `ticket_id` | Degenerate dimension (on the fact, no dim table) | Useful for tracing back to source, and has no other attributes |
| `payment_method` | Kept on the fact | Only 4 values, no other attributes (a "junk dimension" is the formal alternative) |
| `dim_date` | Generated calendar, `date_key` = yyyymmdd | Every date exists even with no sales, and month and weekend attributes are ready to use |

## Expected results
- **Fact rows = 20,000 = tickets.** The type 2 join (`sold_at BETWEEN valid_from AND valid_to`) matches exactly one route version per ticket.
- **Q3:** Valley Buses Jan £1,501.50 · Feb £1,476.30 · Mar £1,495.80. Coastline Travel Apr £1,590.60 · May £1,708.50 · Jun £1,454.60.
- **If `dim_route` were type 1** (current operator only), all of Jan–Mar (£4,473.60) would be credited to **Coastline Travel**, an operator that didn't run the route then. That would affect operator payments and performance reports.
- **Q2:** concession share is about 32% in every area (the synthetic data isn't area-dependent; real data would be).

## Teaching points
- **Grain first.** Most star-schema bugs are grain bugs, the same lesson as session 04.
- **Type 2 joins need the date.** Joining on `route_id` alone would fan out route 7's tickets ×2. The fact row count check catches it.
- **Denormalise deliberately.** `dim_route` repeats the operator name on several routes. That's fine in an analytical model: fewer joins and simpler queries.
- **Stretch:** smartcard tap-in/tap-out is a **different business process** with a **different grain** (one journey leg), so it's a **new fact table** sharing **conformed dimensions** (`dim_date`, `dim_stop`, `dim_route`).
