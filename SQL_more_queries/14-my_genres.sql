#!/usr/bin/python3

-- uses the hbtn_0d_tvshows database to lists all genres of the show Dexter
    -- tv_shows table contains only one record where title = Dexter (but the id can be different)
    -- each record should display: tv_genres.name
    -- results must be sorted in ascending order by the genre name
    -- can use only one SELECT statement
SELECT tv_genres.name, tv_shows.title
FROM tv_genres
LEFT JOIN tv_shows ON tv_shows.id = tv_genres.id
WHERE tv_shows.id = 8
ORDER BY tv_genres.name ASC;