-- Session 12 reference: business questions answered from the star schema.

-- Q1. Journeys and revenue by operator and month
SELECT r.operator_name, d.year_month,
       SUM(f.journeys) AS journeys, ROUND(SUM(f.revenue_gbp), 2) AS revenue_gbp
FROM fact_ticket_sale f
JOIN dim_route r USING (route_key)
JOIN dim_date d  USING (date_key)
GROUP BY ALL ORDER BY ALL;

-- Q2. Share of journeys on concessionary fares, by area
SELECT s.area,
       ROUND(100.0 * SUM(f.journeys) FILTER (WHERE ft.is_concession) / SUM(f.journeys), 1) AS concession_pct
FROM fact_ticket_sale f
JOIN dim_stop s       USING (stop_key)
JOIN dim_fare_type ft USING (fare_type_key)
GROUP BY ALL ORDER BY concession_pct DESC;

-- Q3. Route 7 revenue by operator per month (SCD2 attributes each sale to the operator AT THE TIME)
SELECT d.year_month, r.operator_name, ROUND(SUM(f.revenue_gbp), 2) AS revenue_gbp
FROM fact_ticket_sale f
JOIN dim_route r USING (route_key)
JOIN dim_date d  USING (date_key)
WHERE r.route_id = 7
GROUP BY ALL ORDER BY ALL;
