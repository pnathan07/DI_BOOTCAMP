--Task1
--SELECT
--    production_company,
--    AVG(budget_growth_rate) AS average_budget_growth_rate
--FROM (
--    SELECT
--        production_company,
--        (budget - previous_budget) / previous_budget AS budget_growth_rate
--    FROM (
--        SELECT
--            production_company,
--            movie_title,
--            budget,
--            LAG(budget) OVER (PARTITION BY production_company ORDER BY release_date) AS previous_budget
--        FROM
--            movies
--    ) subquery
--    WHERE previous_budget IS NOT NULL
--) growth_rates
--GROUP BY
--    production_company;

--Task2
--WITH AverageRating AS (
--    SELECT AVG(rating) AS avg_rating
--    FROM movies
--),
--AboveAverageMovies AS (
--    SELECT m.movie_id, m.title, m.rating
--    FROM movies m, AverageRating ar
--    WHERE m.rating > ar.avg_rating
--),
--ActorMovieCount AS (
--    SELECT a.actor_id, a.actor_name, COUNT(am.movie_id) AS movie_count
--    FROM actors a
--    JOIN actor_movies am ON a.actor_id = am.actor_id
--    JOIN AboveAverageMovies aam ON am.movie_id = aam.movie_id
--    GROUP BY a.actor_id, a.actor_name
--)
--SELECT actor_name, movie_count
--FROM ActorMovieCount
--ORDER BY movie_count DESC
--LIMIT 1;

--Task3
--CREATE TABLE movies (
--    movie_id INT PRIMARY KEY,
--    title VARCHAR(255),
--    genre VARCHAR(100),
--    release_date DATE,
--    revenue DECIMAL(15, 2)
--);

--INSERT INTO movies (movie_id, title, genre, release_date, revenue) VALUES
--(1, 'Movie A', 'Action', '2022-01-01', 1000000),
--(2, 'Movie B', 'Action', '2022-02-01', 1500000),
--(3, 'Movie C', 'Action', '2022-03-01', 1200000),
--(4, 'Movie D', 'Drama', '2022-01-15', 800000),
--(5, 'Movie E', 'Drama', '2022-02-15', 900000),
--(6, 'Movie F', 'Drama', '2022-03-15', 950000),
--(7, 'Movie G', 'Action', '2022-04-01', 1300000),
--(8, 'Movie H', 'Drama', '2022-04-15', 1000000),
--(9, 'Movie I', 'Action', '2022-05-01', 1100000);
--SELECT
--    movie_id,
--    title,
--    genre,
--    release_date,
--    revenue,
--    AVG(revenue) OVER (
--        PARTITION BY genre
--        ORDER BY release_date
--        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
--    ) AS rolling_avg_revenue
--FROM
--    movies
--ORDER BY
--    genre,
--    release_date;

--Task4
--CREATE TABLE movies (
--    movie_id INT PRIMARY KEY,
--    title VARCHAR(255),
--    release_date DATE,
--    revenue DECIMAL(15, 2)
--);

--INSERT INTO movies (movie_id, title, release_date, revenue) VALUES
--(1, 'Avengers: Endgame', '2019-04-26', 2797800564),
--(2, 'Avengers: Infinity War', '2018-04-27', 2048359754),
--(3, 'Avengers: Age of Ultron', '2015-05-01', 1405403694),
--(4, 'Avengers', '2012-05-04', 1518812988),
--(5, 'Harry Potter and the Deathly Hallows: Part 2', '2011-07-15', 1341693157),
--(6, 'Harry Potter and the Sorcerer\'s Stone', '2001-11-16', 978087534),
--(7, 'Harry Potter and the Chamber of Secrets', '2002-11-15', 879536719);

--WITH movie_series AS (
--    SELECT
--        movie_id,
--        title,
--        revenue,
--        CASE
--            WHEN title LIKE 'Avengers%' THEN 'Avengers'
--            WHEN title LIKE 'Harry Potter%' THEN 'Harry Potter'
--            ELSE 'Other'
--        END AS series
--    FROM
--        movies
--),
--series_revenue AS (
--    SELECT
--        series,
--        SUM(revenue) AS total_revenue
--    FROM
--        movie_series
--    GROUP BY
--        series
--)
--SELECT
--    series,
--    total_revenue
--FROM
--    series_revenue
--ORDER BY
--    total_revenue DESC
--LIMIT 1;

--Conclusion
--CREATE TABLE movies (
--    movie_id INT PRIMARY KEY,
--    title VARCHAR(255),
--    release_date DATE,
--    revenue DECIMAL(15, 2),
--    genre_id INT
--);

--CREATE TABLE genres (
--    genre_id INT PRIMARY KEY,
--    genre_name VARCHAR(255)
--);

-- Sample data
--INSERT INTO genres (genre_id, genre_name) VALUES
--(1, 'Action'),
--(2, 'Adventure'),
--(3, 'Fantasy');

--INSERT INTO movies (movie_id, title, release_date, revenue, genre_id) VALUES
--(1, 'Avengers: Endgame', '2019-04-26', 2797800564, 1),
--(2, 'Avengers: Infinity War', '2018-04-27', 2048359754, 1),
--(3, 'Harry Potter and the Sorcerer\'s Stone', '2001-11-16', 978087534, 3),
--(4, 'Harry Potter and the Chamber of Secrets', '2002-11-15', 879536719, 3),
--(5, 'Avengers: Age of Ultron', '2015-05-01', 1405403694, 1),
--(6, 'Avengers', '2012-05-04', 1518812988, 1),
--(7, 'Harry Potter and the Deathly Hallows: Part 2', '2011-07-15', 1341693157, 3);
