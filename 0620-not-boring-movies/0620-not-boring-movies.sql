# Write your MySQL query statement below
SELECT 
    *
FROM Cinema
WHERE 
    MOD(id, 2) = 1        -- only odd-numbered IDs
    AND description <> 'boring'   -- description not equal to 'boring'
ORDER BY 
    rating DESC;          -- highest rated first
