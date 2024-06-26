-- Part 1 
--CREATE TABLE CustomerProfile (
--   id SERIAL PRIMARY KEY,
--isLoggedIn BOOLEAN DEFAULT FALSE,
--  customer_id INTEGER UNIQUE,
 --CONSTRAINT fk_customer
 --FOREIGN KEY(customer_id) 
  --REFERENCES Customer(id)
 -- ON DELETE CASCADE
--);
---- Insert profile for John, who is logged in
--INSERT INTO CustomerProfile (isLoggedIn, customer_id)
--VALUES 
--    (TRUE, (SELECT id FROM Customer WHERE first_name = 'John' AND last_name = 'Doe'));

-- Insert profile for Jerome, who is not logged in
--INSERT INTO CustomerProfile (isLoggedIn, customer_id)
--VALUES 
--    (FALSE, (SELECT id FROM Customer WHERE first_name = 'Jerome' AND last_name = 'Lalu'));

-- Insert profile for Lea, who is not logged in (default isLoggedIn to FALSE)
--INSERT INTO CustomerProfile (customer_id)
--VALUES 
--    ((SELECT id FROM Customer WHERE first_name = 'Lea' AND last_name = 'Rive'));
-- Query 1: LoggedIn customers
--SELECT c.first_name
--FROM Customer c
--JOIN CustomerProfile cp ON c.id = cp.customer_id
--WHERE cp.isLoggedIn = TRUE;

-- Query 2: All customers and their isLoggedIn status
--SELECT c.first_name, cp.isLoggedIn
--FROM Customer c
--LEFT JOIN CustomerProfile cp ON c.id = cp.customer_id;

-- Query 3: Number of customers not logged in
--SELECT COUNT(*)
--FROM Customer c
--JOIN CustomerProfile cp ON c.id = cp.customer_id
--WHERE cp.isLoggedIn = FALSE;

--Part 2

--CREATE TABLE Student (
--    student_id SERIAL PRIMARY KEY,
--    name VARCHAR(255) NOT NULL UNIQUE,
--    age INTEGER CHECK (age <= 15)
--);

--INSERT INTO Student (name, age)
--VALUES
--    ('John', 12),
--   ('Lera', 11),
--    ('Patrick', 10),
--   ('Bob', 14);
--CREATE TABLE Library (
--    book_fk_id INTEGER,
--    student_fk_id INTEGER,
--    borrowed_date DATE,
--    PRIMARY KEY (book_fk_id, student_fk_id),
--   CONSTRAINT fk_book
--        FOREIGN KEY(book_fk_id)
--        REFERENCES Book(book_id)
--        ON DELETE CASCADE
--        ON UPDATE CASCADE,
--    CONSTRAINT fk_student
--        FOREIGN KEY(student_fk_id)
--       REFERENCES Student(student_id)
--        ON DELETE CASCADE
--        ON UPDATE CASCADE
--);
-- John borrowed Alice In Wonderland on 15/02/2022
--INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
--VALUES (
--    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--    (SELECT student_id FROM Student WHERE name = 'John'),
    '2022-02-15'
--);

-- Bob borrowed To Kill a Mockingbird on 03/03/2021
--INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
--VALUES (
--    (SELECT book_id FROM Book WHERE title = 'To Kill a Mockingbird'),
--    (SELECT student_id FROM Student WHERE name = 'Bob'),
--    '2021-03-03'
--);

-- Lera borrowed Alice In Wonderland on 23/05/2021
--INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
--VALUES (
--    (SELECT book_id FROM Book WHERE title = 'Alice In Wonderland'),
--    (SELECT student_id FROM Student WHERE name = 'Lera'),
--    '2021-05-23'
--);

-- Bob borrowed Harry Potter on 12/08/2021
--INSERT INTO Library (book_fk_id, student_fk_id, borrowed_date)
--VALUES (
--    (SELECT book_id FROM Book WHERE title = 'Harry Potter'),
--    (SELECT student_id FROM Student WHERE name = 'Bob'),
--    '2021-08-12'
--);
-- Display all columns from the Library junction table
--SELECT * FROM Library;

-- Display the name of the student and the title of the borrowed books
--SELECT s.name, b.title
--FROM Library l
--JOIN Student s ON l.student_fk_id = s.student_id
--JOIN Book b ON l.book_fk_id = b.book_id;

-- Display the average age of the children who borrowed the book "Alice In Wonderland"
--SELECT AVG(s.age) AS average_age
--FROM Library l
--JOIN Student s ON l.student_fk_id = s.student_id
--JOIN Book b ON l.book_fk_id = b.book_id
--WHERE b.title = 'Alice In Wonderland';

-- Delete a student from the Student table (e.g., John)
--DELETE FROM Student WHERE name = 'John';

-- Check the Library table after the deletion
--SELECT * FROM Library;
