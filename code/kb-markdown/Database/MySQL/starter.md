```
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.13</version>
</dependency>

desc orderdetails;

// check mysql version
SHOW VARIABLES LIKE "%version%";

-- drop table if already exists --
DROP TABLE OrderDetails;

-- table for the exercise --
CREATE TABLE OrderDetails (OrderId INT, ProductName VARCHAR(30), Price INT, Quantity INT, CustomerName VARCHAR(30));

-- initial data --
INSERT INTO OrderDetails (OrderId, ProductName, Price, Quantity, CustomerName) VALUES (1, 'LENOVO LAPTOP', 40000, 1, 'Bob');
INSERT INTO OrderDetails (OrderId, ProductName, Price, Quantity, CustomerName) VALUES (2, 'DELL LAPTOP', 50000, 1, 'Alex');
INSERT INTO OrderDetails (OrderId, ProductName, Price, Quantity, CustomerName) VALUES (3, 'HP LAPTOP', 45000, 1, 'John');
INSERT INTO OrderDetails (OrderId, ProductName, Price, Quantity, CustomerName) VALUES (4, 'SMART TV', 20000, 1, 'Bob');
INSERT INTO OrderDetails (OrderId, ProductName, Price, Quantity, CustomerName) VALUES (5, 'SONY HEADPHONES', 5000, 2, 'Bob');
INSERT INTO OrderDetails (OrderId, ProductName, Price, Quantity, CustomerName) VALUES (6, 'LENOVO LAPTOP', 40000, 1, 'Katie');
INSERT INTO OrderDetails (OrderId, ProductName, Price, Quantity, CustomerName) VALUES (7, 'LENOVO LAPTOP', 40000, 1, 'Joy');


```

```
-- drop table if already exists --
DROP TABLE Users;

-- table for the exercise --
CREATE TABLE Users (UserId INT, UserName VARCHAR(30), PhoneNumber VARCHAR(10));

-- initial data --
INSERT INTO Users (UserId, UserName, PhoneNumber) VALUES (1, 'Rahul', '9876543210');

INSERT INTO Users (UserId, UserName, PhoneNumber) VALUES (2, 'Nikita', '8776543201');

INSERT INTO Users (UserId, UserName, PhoneNumber) VALUES (3, 'Manoj', '8876543012');

INSERT INTO Users (UserId, UserName, PhoneNumber) VALUES (4, 'Rekha', '7896543210');
```

# mysql command

```
SET GLOBAL log_bin_trust_function_creators = 1;
SET SQL_SAFE_UPDATES = 0;
SET GLOBAL log_bin_trust_function_creators = 1;
```

```
-- table for the exercise --
CREATE TABLE posts (id INT primary key auto_increment, email_id VARCHAR(30), title VARCHAR(100),description VARCHAR(500), tag VARCHAR(10), timestamp VARCHAR(100));

-- initial data --
INSERT INTO Users (email_id, password) VALUES ('Rahul', '9876543210');
INSERT INTO Users (email_id, password) VALUES ('Nikita', '8776543201');
INSERT INTO Users (email_id, password) VALUES ('Manoj', '8876543012');
INSERT INTO Users (email_id, password) VALUES ('Rekha', '7896543210');




CREATE DATABASE school;
CREATE TABLE student (student_roll_number INT(10), student_name VARCHAR(30));
INSERT INTO student (student_roll_number, student_name) VALUES (98640, 'Rahul');
INSERT INTO student (student_roll_number, student_name) VALUES (87641, 'Nikita');
INSERT INTO student (student_roll_number, student_name) VALUES (88642, 'Manoj');
INSERT INTO student (student_roll_number, student_name) VALUES (78640, 'Rekha');

```