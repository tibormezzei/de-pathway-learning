-- Session 12 reference: build a star schema from the operational bus ticketing tables.
-- Run:  python solutions/build_star.py   (loads the CSVs, runs this file, then the questions)
--
-- Grain of the fact: ONE ROW PER TICKET SOLD.

-- dim_date: one row per calendar day
CREATE TABLE dim_date AS
SELECT
    CAST(strftime(d, '%Y%m%d') AS INTEGER)  AS date_key,
    CAST(d AS DATE)                         AS full_date,
    year(d)                                 AS year,
    month(d)                                AS month,
    strftime(d, '%Y-%m')                    AS year_month,
    strftime(d, '%A')                       AS day_name,
    isodow(d) IN (6, 7)                     AS is_weekend
FROM range(DATE '2026-01-01', DATE '2027-01-01', INTERVAL 1 DAY) AS t(d);

-- dim_stop: type 1 (overwrite). We don't need stop history.
CREATE TABLE dim_stop AS
SELECT ROW_NUMBER() OVER (ORDER BY stop_id) AS stop_key,
       stop_id, stop_name, area, fare_zone
FROM stops;

-- dim_fare_type: small, static
CREATE TABLE dim_fare_type AS
SELECT ROW_NUMBER() OVER (ORDER BY fare_type_code) AS fare_type_key,
       fare_type_code, fare_type_name, is_concession
FROM fare_types;

-- dim_route: TYPE 2 SCD. A new row each time a route changes operator, with validity dates.
-- The operator is folded into the route dimension (denormalised), so no snowflake is needed.
CREATE TABLE dim_route AS
SELECT ROW_NUMBER() OVER (ORDER BY r.route_id, r.valid_from)   AS route_key,
       r.route_id, r.route_name,
       o.operator_id, o.operator_name,
       CAST(r.valid_from AS DATE)                              AS valid_from,
       COALESCE(CAST(r.valid_to AS DATE), DATE '9999-12-31')   AS valid_to,
       r.valid_to IS NULL                                      AS is_current
FROM route_operator r
JOIN operators o USING (operator_id);

-- fact_ticket_sale: surrogate keys + measures
CREATE TABLE fact_ticket_sale AS
SELECT
    t.ticket_id,                                            -- degenerate dimension
    CAST(strftime(t.sold_at, '%Y%m%d') AS INTEGER)  AS date_key,
    dr.route_key,
    ds.stop_key,
    df.fare_type_key,
    t.payment_method,                                       -- low-cardinality: kept on the fact
    t.price_gbp                                     AS revenue_gbp,
    1                                               AS journeys
FROM tickets t
JOIN dim_route dr
  ON dr.route_id = t.route_id
 AND CAST(t.sold_at AS DATE) BETWEEN dr.valid_from AND dr.valid_to   -- pick the version valid THEN
JOIN dim_stop ds      ON ds.stop_id = t.boarding_stop_id
JOIN dim_fare_type df ON df.fare_type_code = t.fare_type_code;
