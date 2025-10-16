#!/usr/bin/python3

-- list all Comedy shows in the database hbtn_0d_tvshows
    -- tv_genres table contains only one record where name = Comedy (but the id can be different)
    -- each record should display: tv_shows.title
    -- results must be sorted in ascending order by the show title
    -- can use only one SELECT statement
SELECT tv_shows.title AS title
FROM tv_shows
INNER JOIN tv_show_genres ON tv_show_genres.show_id = tv_shows.id
INNER JOIN tv_genres ON tv_genres.id = tv_show_genres.genre_id
WHERE tv_genres.name = 'Comedy'
ORDER BY title ASC;
