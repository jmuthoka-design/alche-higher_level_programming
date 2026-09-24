-- List records that have a name, ordered by score from highest to lowest
SELECT score, name
FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;
