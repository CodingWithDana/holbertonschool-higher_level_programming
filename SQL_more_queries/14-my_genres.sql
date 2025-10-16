#!/usr/bin/python3

-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
    -- tv_shows table contains only one record where title = Dexter (but the id can be different)
    -- each record should display: tv_genres.name
    -- results must be sorted in ascending order by the genre name
    -- can use only one SELECT statement
SELECT DISTINCT tv_genres.name AS name
FROM tv_genres
INNER JOIN tv_show_genres ON tv_show_genres.genre.id = tv_genres.id
ORDER BY name ASC;
