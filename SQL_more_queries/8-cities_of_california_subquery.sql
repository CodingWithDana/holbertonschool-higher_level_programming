#!/usr/bin/python3

-- look up specfied data
USE hbtn_0d_usa;

SELECT *
FROM CITIES
WHERE state_id = (
    SELECT id
    FROM states
    WHERE name = 'California'
)
ORDER BY id ASC;