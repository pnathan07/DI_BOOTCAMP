--Exercice1
--Task1
--select medal, AVG(age) as avg_age from competitors as c1 where exist
--(select 1 from competitos as c2 where c1.competito_id = c2.competitor_id
--and c2.medal is not null)
--group by medal;

--Task2
--select region count(distinct competitor_id) as unique_competitors from competitors
--where competitor_id in ( select competitor_id from events group by competitor_id having count(distinct event_id)>3)
--group by region order by unique_competitors desc
--limit 5 ;

--Task 3
-- create temporary table temp_competitor_medald as select competitor_id, count(medal) as total
--from competitors where medal is not null group by competitor_id ;
--select competitor-id total_medals from temp_competitor_medals where total_medals > 2;

--Task 4 
--create temporary table temp_competitors_analysis as select competitor_id, competitor-name, medal from competitors;
--delete from temp_competitors_analysis where competitor_id in ( select competitor_id from temp_competitors_analysis where medal is null
--);

--Exercice 2 
--Task1
-- update competitors as c1 set height = ( slect avg(c2.height) from competitors as c2 where c2.region = c1.region)
--where height is not null ;

--Task2
--create temporary table temp-competitors_events( 
--competitor-id int,competitor-name varchar(255), games varchar(255), total_events int);
--insert into temp_competitors_events (competitor_id, competitor_name, games, total_events)
-- select  c.competitor_id, c.competitor_name, ce.games, count(ce.event_id) as total_events from competitors as c
--join competitor_events AS ce ON c.competitor_id = ce.competitor_id where ce.games in ( select games from competitor_events as ce_inner where ce_inner.competitor_id = ce.competitor_id
--group by games having count(ce_inner.event-id) >1)
--group by  c.competitor_id, c.competitor_name, ce.games;

--Task3
--SELECT AVG(total_medals) AS overall_avg_medals FROM (SELECT competitor_id, COUNT(medal) AS total_medals
--FROM medals GROUP BY competitor_id) AS avg_medals_per_competitor;
--SELECT region, AVG(total_medals) AS avg_medals_per_competitor FROM (SELECT competitor_id, region, COUNT(medal) AS total_medals
--FROM competitors JOIN medals ON competitors.competitor_id = medals.competitor_id GROUP BY competitor_id, region
--) AS region_medalsGROUP BY region HAVING AVG(total_medals) > (SELECT AVG(total_medals)
--FROM (SELECT competitor_id, COUNT(medal) AS total_medals FROM medals GROUP BY competitor_id
--    ) AS avg_medals_per_competitor );

--Task4
-- CREATE TEMPORARY TABLE temp_competitor_participation (competitor_id INT,
-- season VARCHAR(10));
-- insert into temp_competitor_participation (competitor_id, season)
-- select competitor_id, season from olympic_events where season in ('Summer', 'winter');
-- select competitor_id from temp_competitor_participation where season = 'Summer' and competitor_id
--from temp_competitor_participation where season = 'Winter' ); 
