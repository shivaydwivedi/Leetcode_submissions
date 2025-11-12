# Write your MySQL query statement below
SELECT 
    name
FROM Customer
WHERE 
    referee_id <> 2      -- referred by someone other than customer with id = 2
    OR referee_id IS NULL;  -- or not referred by anyone
