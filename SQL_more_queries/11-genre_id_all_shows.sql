#!/usr/bin/python3

-- lists all shows contained in the database
    -- if a show doesn’t have a genre, display NULL
    -- use only one SELECT statement
    -- each record should display: tv_shows.title - tv_show_genres.genre_id
    -- results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;