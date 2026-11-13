-- Session 04: reference answers
-- Run:  python run_sql.py solutions/answers.sql


-- Q1. Loans per branch, busiest first
SELECT b.branch_name, COUNT(*) AS loans
FROM loans AS l
JOIN branches AS b ON l.branch_id = b.branch_id
GROUP BY b.branch_name
ORDER BY loans DESC;


-- Q2. Members who have never borrowed (anti-join)
SELECT COUNT(*) AS never_borrowed
FROM members AS m
LEFT JOIN loans AS l ON m.member_id = l.member_id
WHERE l.loan_id IS NULL;


-- Q3a. Lost rows: an INNER JOIN to books silently drops loans
SELECT
    (SELECT COUNT(*) FROM loans)                                  AS all_loans,
    (SELECT COUNT(*) FROM loans l JOIN books b USING (book_id))   AS after_inner_join;

-- Q3b. Which loans are orphans?
SELECT l.loan_id, l.book_id, l.loan_date
FROM loans AS l
LEFT JOIN books AS b ON l.book_id = b.book_id
WHERE b.book_id IS NULL
ORDER BY l.loan_id;


-- Q4. Fan-out: fixed by filtering the lookup to one row per branch BEFORE joining
SELECT b.branch_name, h.closes AS saturday_closing, COUNT(*) AS loans
FROM loans AS l
JOIN branches AS b ON l.branch_id = b.branch_id
JOIN branch_opening_hours AS h
  ON h.branch_id = b.branch_id
 AND h.day_of_week = 'Sat'
GROUP BY b.branch_name, h.closes
ORDER BY loans DESC;


-- Q5. Top 3 books in each branch (window function)
WITH book_counts AS (
    SELECT l.branch_id, bk.title, COUNT(*) AS loans
    FROM loans AS l
    JOIN books AS bk ON l.book_id = bk.book_id
    GROUP BY l.branch_id, bk.title
),
ranked AS (
    SELECT *,
           ROW_NUMBER() OVER (PARTITION BY branch_id ORDER BY loans DESC, title) AS rn
    FROM book_counts
)
SELECT br.branch_name, r.rn, r.title, r.loans
FROM ranked AS r
JOIN branches AS br USING (branch_id)
WHERE r.rn <= 3
ORDER BY br.branch_name, r.rn;


-- Q6. Overdue books as at 2026-07-01 (on loan > 28 days)
SELECT
    COUNT(*)                                                          AS still_on_loan,
    COUNT(*) FILTER (WHERE DATE '2026-07-01' - loan_date > 28)        AS overdue
FROM loans
WHERE return_date IS NULL;


-- Q7 (stretch). Monthly loans per branch and change vs previous month
WITH monthly AS (
    SELECT branch_id, date_trunc('month', loan_date) AS month, COUNT(*) AS loans
    FROM loans
    GROUP BY branch_id, month
)
SELECT
    branch_id,
    strftime(month, '%Y-%m')                                             AS month,
    loans,
    loans - LAG(loans) OVER (PARTITION BY branch_id ORDER BY month)      AS change_vs_prev
FROM monthly
WHERE branch_id = 1
ORDER BY month;
