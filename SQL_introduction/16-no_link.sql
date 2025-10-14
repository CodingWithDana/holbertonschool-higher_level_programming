#!/usr/bin/python3

-- list all records with certain conditions
    -- do not list rows where name column has no value
    -- score and name are outputed in this order
        -- score   name
        -- 18  Aria
        -- 12  Aria
        -- 10  John
        -- 10  Bob
    -- records are sorted by descending score
    -- database name will be passed in the command line (no action required in the code)

SELECT score, name FROM second_table
WHERE name IS NOT NULL
ORDER BY score DESC;