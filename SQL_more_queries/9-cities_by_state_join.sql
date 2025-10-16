#!/usr/bin/python3

-- list all cities in the database hbtn_0d_usa
SELECT id, cities.name, states.name
FROM hbtn_0d_usa
ORDER BY cities.id ASC;