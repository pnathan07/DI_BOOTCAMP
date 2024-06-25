--create table students (
--id serial primary key,
--	first_name varchar (255),
--	last_name varchar (255),
--	birth_date date
--);



--insert into students (last_name, first_name, birth_date)
--values 
--('Marc',	'Benichou',	'1998-02-11'),
--('Yoan', 'Cohen', '2010-03-12'),
--('Lea',	'Benichou',	'1987-07-21'),
--('Amelia','Dux', '1996-07-04'),
--('David','Grez'	,'2006-09-06'),
--('Omer','Simpson',	'1980-10-07');

--select * from students ;
--select first_name, last_name from students;
--select * from students where id = 2 ;
--select * from students where last_name = 'Benichou' and first_name = 'Marc';
--SELECT * FROM students WHERE last_name = 'Benichou' OR first_name = 'Marc';
--SELECT * FROM students WHERE first_name LIKE '%a%';
--SELECT * FROM students WHERE first_name LIKE 'a%';
--SELECT * FROM students WHERE first_name LIKE '%a';
--SELECT * FROM students WHERE first_name LIKE '%a_';
--SELECT * FROM students WHERE id IN (1, 3);
--SELECT * FROM students WHERE birth_date >= '2000-01-01';
