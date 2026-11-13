# Star schema design: bus ticketing

## 1. Grain
One row in the fact table represents:

## 2. Fact table: `fact_...`
| Column | Type | Foreign key to / measure | Additive? |
|---|---|---|---|
| | | | |

## 3. Dimensions
| Dimension | Attributes | Source table(s) | SCD type (1/2) and why |
|---|---|---|---|
| | | | |

## 4. Diagram

```
            dim_?
              │
  dim_? ── fact_? ── dim_?
              │
            dim_?
```

## 5. Decisions and assumptions
-
