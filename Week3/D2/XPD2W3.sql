--Exercice 1
--select * from items order by price asc  ;
--SELECT * FROM itemsWHERE price >= 80 ORDER BY price DESC;
--SELECT first_name, last_name, email, create_date FROM customer ORDER BY first_name LIMIT 3;
--SELECT last_name FROM customer ORDER BY last_name DESC;



--Exercice 2

--select * from customer;
--select first_name || ' ' || last_name as full_name from customer ; 
--select create_date from customer group by create_date ;
--select * from customer order by first_name desc ;
--SELECT film_id AS "Film ID", title AS "Title", description AS "Description", release_year AS "Year of Release", rental_rate AS "Rental Rate" FROM film ORDER BY rental_rate ASC;
--SELECT address.address, address.phone FROM customer JOIN address ON customer.address_id = address.address_id WHERE address.district = 'Texas';
-- select * from film where film_id in (15, 150);
--select film_id, title, description, length, rental_rate from film where title = 'Your favorite movie';
--select film_id, title, description, length, rental_rate from film where lower(left(title, 2)) = lower('Your favorite movie title') order by title ;
--select film_id, rental_rate from film order by rental_rate limit 10 ;
--select film_id, title, rental_rate from film order by rental_rate offset 10 limit 10 ;
--SELECT c.first_name, c.last_name, p.amount, p.payment_date FROM customer c JOIN payment p ON c.customer_id = p.customer_id ORDER BY c.customer_id;
--SELECT f.film_id, f.title, f.description, f.release_year, f.rental_rate FROM film f LEFT JOIN inventory i ON f.film_id = i.film_id WHERE i.film_id IS NULL;
--SELECT ci.city, co.country FROM city ci JOIN country co ON ci.country_id = co.country_id;
