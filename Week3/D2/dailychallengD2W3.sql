 --q1 SELECT COUNT(*) 
   -- FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NULL )
--output = 0 

--q2 SELECT COUNT(*) 
--FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id = 5 )
--output = 2

--q3 SELECT COUNT(*) 
--FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab )
--output = 0 

--q4 SELECT COUNT(*) 
--FROM FirstTab AS ft WHERE ft.id NOT IN ( SELECT id FROM SecondTab WHERE id IS NOT NULL )
--output = 2