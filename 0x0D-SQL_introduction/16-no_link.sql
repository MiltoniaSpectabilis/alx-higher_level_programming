-- Lists all rows in descending score except the ones with empty name
SELECT
    score,
    name
FROM
    second_table
WHERE
    name != ''
ORDER BY score DESC;
