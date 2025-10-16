#!/usr/bin/python3

-- look up specfied data
SELECT *
FROM CITIES
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;