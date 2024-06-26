--Exercice 1 
--Task 1 
--CREATE TEMPORARY TABLE temp_medalists (
--    competitor_id INT,
--    summer_medals INT,
--    winter_medals INT
--);
--INSERT INTO temp_medalists (competitor_id, summer_medals, winter_medals)
--SELECT 
--    summer_winners.competitor_id,
--    summer_winners.summer_medals,
--    winter_winners.winter_medals
--FROM 
--    (SELECT competitor_id, COUNT(*) AS summer_medals
--     FROM medals
--     WHERE season = 'Summer'
--     GROUP BY competitor_id) AS summer_winners
--JOIN 
--    (SELECT competitor_id, COUNT(*) AS winter_medals
--     FROM medals
--     WHERE season = 'Winter'
--     GROUP BY competitor_id) AS winter_winners
--ON 
--    summer_winners.competitor_id = winter_winners.competitor_id;
--SELECT * FROM temp_medalists;

--Task2
--CREATE TEMPORARY TABLE temp_two_sports_medalists (
--    competitor_id INT,
--    total_medals INT
--);
--INSERT INTO temp_two_sports_medalists (competitor_id, total_medals)
--SELECT competitor_id, COUNT(*)
--FROM medals
--WHERE competitor_id IN (
--    SELECT competitor_id
--    FROM medals
--    GROUP BY competitor_id
--    HAVING COUNT(DISTINCT sport_id) = 2
--)
--GROUP BY competitor_id
--HAVING COUNT(*) > 2;
--SELECT competitor_id, total_medals
--FROM temp_two_sports_medalists
--ORDER BY total_medals DESC
--LIMIT 3;
--SELECT * FROM temp_two_sports_medalists;

--Exercice 2
--Task1 
--WITH max_medals_per_event AS (
--    SELECT 
--        competitor_id, 
--        event_id, 
--        COUNT(*) AS medal_count
--    FROM 
--        medals
--    GROUP BY 
--        competitor_id, event_id
--),
--region_medals AS (
--    SELECT 
--        r.region_name,
--        SUM(m.medal_count) AS total_medals
--    FROM 
--        max_medals_per_event m
--    JOIN 
--       competitors c ON m.competitor_id = c.competitor_id
--    JOIN 
--        regions r ON c.region_id = r.region_id
--    GROUP BY 
--        r.region_name
--)
--SELECT 
--    region_name, 
--    total_medals
--FROM 
--    region_medals
--ORDER BY 
--    total_medals DESC
--LIMIT 5;

--Task 2
--WITH max_medals_per_event AS (
--    SELECT 
--        competitor_id, 
--        event_id, 
--        COUNT(*) AS medal_count
--    FROM 
--        medals
--    GROUP BY 
--        competitor_id, event_id
--),
--region_medals AS (
--    SELECT 
 --       r.region_name,
--        SUM(m.medal_count) AS total_medals
--    FROM 
--        max_medals_per_event m
--    JOIN 
--        competitors c ON m.competitor_id = c.competitor_id
--    JOIN 
--        regions r ON c.region_id = r.region_id
--    GROUP BY 
--        r.region_name
--)
--SELECT 
--    region_name, 
--    total_medals
--FROM 
--    region_medals
--ORDER BY 
--    total_medals DESC
--LIMIT 5;
