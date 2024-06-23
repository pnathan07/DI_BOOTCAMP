--Create a database called bootcamp.
--Create a table called students.
--Add the following columns:
--id
--last_name
--first_name
--birth_date
--The id must be auto_incremented.
--Make sure to choose the correct data type for each column.
--To help, here is the data that you will have to insert. (How do we insert a date to a table?)

create table students (
     id serial primary key,
	  "first_name" varchar (20),
	  "last_name" varchar (20),
	  "birth_date" date 
);
insert into students (first_name, last_name, birthday)
values 
 ('Marc','Benichou','1998-02-11')
('Yoan','Cohen'	,'2010-03-12')
('Lea',	'Benichou','1987-27-07')
('Amelia',	'Dux',	'1996-07-04')
('David','Grez'	,'2003-14-06')
('Omer',	'Simpson',	'1980-03-10')
('Nathan', 'Partouche', '2000-06-07')


--Fetch all of the data from the table.
--Fetch all of the students first_names and last_names.
--For the following questions, only fetch the first_names and last_names of the students.
--Fetch the student which id is equal to 2.
--Fetch the student whose last_name is Benichou AND first_name is Marc.
--Fetch the students whose last_names are Benichou OR first_names are Marc.
--6Fetch the students whose first_names contain the letter a.
--5Fetch the students whose first_names start with the letter a.
--4Fetch the students whose first_names end with the letter a.
--3Fetch the students whose second to last letter of their first_names are a (Example: Leah).
--2Fetch the students whose id’s are equal to 1 AND 3 .
1--Fetch the students whose birth_dates are equal to or come after 1/01/2000. (show all their info).
	   
--select * from students ; 
--select firsts_names, lasts_names from students;
--select firsts_names, lasts_names from students where id =2; 
--select  frists_names, lasts_names from students where lasts_names = 'Benichou' or first_name = 'Marc'; 
--select firsts_names, lasts_names from students where lasts_names = 'Benichou' or first_name = 'Marc';
--select firsts_names from students where firsts_names like '%a%' or last_name like '%a%' ;
--select firsts_names from students where firsts_names like 'A%';
--select firsts_names from students where firsts_names like '%a';
--select firsts_names, from students where right(first_name, 2) like '_a';
--select * from students where id =1 or id =3; 
--select * from students where birth_date >= '2000-01-01';
