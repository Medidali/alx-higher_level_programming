-- script that lists all records of the table second_table

-- ListRecords
SELECT score, name
FROM second_table
WHERE name != ''
ORDER BY score DESC;

