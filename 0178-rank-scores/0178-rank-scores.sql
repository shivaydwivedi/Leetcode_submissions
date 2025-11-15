# Write your MySQL query statement below
SELECT
  s.score,
  (
    SELECT COUNT(DISTINCT t.score) 
    FROM Scores t
    WHERE t.score > s.score
  ) + 1 AS `rank`
FROM Scores s
ORDER BY s.score DESC;
