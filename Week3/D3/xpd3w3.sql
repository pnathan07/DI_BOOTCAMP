--Exercice 1

--select * from language ;
-- slect film.title, film.description, language.name as language_name from film
--join language on film.language_id = language.language_id ;
--select film.title, film.description, language.name as language_name from language
--left join film on language.language_id = film.language_id;
--create table new_table (
--	id int serial primary key
--	name varchar (255)
--);
--create table customer_review (
--	review_id int serial primary key,
--	film_id int not null,
--	language_id int not null,
--	title varchar(255) not null,
--	score int check (score between 1 and 10) not null,
--	review_text TEXT,
--	 last_update TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
--	FOREIGN KEY (film_id) REFERENCES new_film(id) ON DELETE CASCADE,
--  FOREIGN KEY (language_id) REFERENCES language(language_id)
--);
-- select * from new_film;
--select * from language ;
-- insert into customer_review(film-id, language_id, title, score, review_text) Values
--(1,1 'amazing movie', 9,'inception is the best action movie')
--(2,2 'classic movie', 10,'007 is a classic film');
-- select * from new_film;
--select *from customer_ review;
--select from new_film where id = 1;
--select *from new_film;
--select *from customer_review;

--Exercice 2

-- select *from new_film;
-- select * from language;
--update new_film;
-- set language_id = 3;
--where id = 1 ;
-- select * from new_film ; 
-- insert into customer (name, email, store_id, address_id,city_id)
--values ('Jon Statement', 'j@gmail,com', 1,10,7);
-- show tables like 'customer_review'
-- drop table customer_review;
-- select count (*) as outstanding_rentals
--from rental
--where returns_date is null;
--select f.film_id, f.title, f.rental_rate
--from film f 
--join inventory i on f.film_id = i.fillm_id
--join rental r on i.inventory_id = r.inventory_id
--where r.return_date is null
--order by f.rental_rate desc
--limit 30
--SELECT f.film_id, f.title, f.description
--FROM film f
--JOIN film_actor fa ON f.film_id = fa.film_id
--JOIN actor a ON fa.actor_id = a.actor_id
--WHERE f.description LIKE '%sumo wrestler%'
--AND a.actor_name = 'Penelope Monroe';
--SELECT f.film_id, f.title, f.rental_rate, r.rental_date, r.return_date
--FROM film f
--JOIN inventory i ON f.film_id = i.film_id
--JOIN rental r ON i.inventory_id = r.inventory_id
--JOIN customer c ON r.customer_id = c.customer_id
--WHERE c.last_name = 'Mahan'  -- Assuming Matthew Mahan's last name is 'Mahan'
--AND f.rental_rate > 4.00
--AND r.rental_date >= '2005-07-28' AND r.rental_date <= '2005-08-01';
--SELECT f.film_id, f.title, f.description, f.replacement_cost
--FROM film f
--JOIN inventory i ON f.film_id = i.film_id
--JOIN rental r ON i.inventory_id = r.inventory_id
--JOIN customer c ON r.customer_id = c.customer_id
--WHERE (f.title LIKE '%boat%' OR f.description LIKE '%boat%')
--AND f.replacement_cost > 20.00  -- Adjust the cost threshold as needed
--AND c.last_name = 'Mahan';  -- Assuming Matthew Mahan's last name is 'Mahan'
