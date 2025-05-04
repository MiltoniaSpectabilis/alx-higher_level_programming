--
SELECT
    tv_genres.name AS genre, tv_show_genres.show_id AS number_of_shows
FROM
    tv_genres, tv_show_genres
