#!/usr/bin/python3

--  list all shows contained in hbtn_0d_tvshows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
WHERE tv_shows.id != tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
