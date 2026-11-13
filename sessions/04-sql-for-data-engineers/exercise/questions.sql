-- Session 04 exercise: write a query under each question.
-- Run:  python run_sql.py exercise/questions.sql
--
-- Tables: branches, branch_opening_hours, members, books, loans
-- Start by looking:  SELECT * FROM loans LIMIT 5;   DESCRIBE loans;


-- Q1. How many loans has each branch made? Show branch_name, busiest first.



-- Q2. How many members have NEVER borrowed a book?
--     (Hint: which join keeps members with no matching loans?)



-- Q3. A colleague joined loans to books with an INNER JOIN and their total went down.
--     a) How many loans does an INNER JOIN to books lose?
--     b) List the loans whose book_id isn't in the catalogue.



-- Q4. This query is meant to show loans per branch plus the branch's Saturday
--     closing time. The loan counts are wrong. Run it, explain WHY, and fix it.
SELECT b.branch_name, h.closes AS saturday_closing, COUNT(*) AS loans
FROM loans AS l
JOIN branches AS b ON l.branch_id = b.branch_id
JOIN branch_opening_hours AS h ON h.branch_id = b.branch_id
GROUP BY b.branch_name, h.closes
ORDER BY loans DESC;



-- Q5. What are the top 3 most-borrowed books in EACH branch?
--     (Hint: window function. Watch out for ties: how does your query break them?)



-- Q6. As at 2026-07-01, how many books are still on loan, and how many of those
--     are overdue (on loan more than 28 days)?
--     (Hint: return_date is NULL for books still out. In DuckDB, date - date = days.)



-- Q7 (stretch). For branch 1: loans per month, and the change compared with the
--     previous month. (Hint: a CTE plus LAG.)
