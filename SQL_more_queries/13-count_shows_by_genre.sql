-- List genres and the number of shows linked to each genre

-- Count linked shows for each genre and order by the count
SELECT tv_genres.name AS genre,
       COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres
ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
