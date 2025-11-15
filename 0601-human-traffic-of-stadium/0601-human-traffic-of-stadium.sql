# Write your MySQL query statement below
WITH cte AS (
    SELECT
        *,
        id - ROW_NUMBER() OVER (ORDER BY id) AS grp
    FROM Stadium
    WHERE people >= 100
),
groups_with_3 AS (
    SELECT grp
    FROM cte
    GROUP BY grp
    HAVING COUNT(*) >= 3
)

SELECT id, visit_date, people
FROM cte
WHERE grp IN (SELECT grp FROM groups_with_3)
ORDER BY visit_date;

