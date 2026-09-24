-- List records with a score of 10 or higher, ordered from highest to lowest
SELECT score, name
FROM second_table
WHERE score >= 10
ORDER BY score DESC;
