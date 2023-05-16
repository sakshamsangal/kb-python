```

CREATE TABLE table1 (
    id int(5),
    name VARCHAR(10)
);

INSERT INTO table1 VALUES(
    1,
    'a'
);

INSERT INTO table1 VALUES(
    2,
    'b'
);
INSERT INTO table1 VALUES(
    3,
    'c'
);
INSERT INTO table1 VALUES(
    4,
    'd'
);




CREATE TABLE table2 (
    id int(5),
    salary int(10)
);

INSERT INTO table2 VALUES(
    2,
    100
);

INSERT INTO table2 VALUES(
    3,
    200
);

INSERT INTO table2 VALUES(
    5,
    600
);


SELECT table1.id, table1.name, table2.id, table2.salary
FROM table1
INNER JOIN table2 ON table1.id = table2.id;

// output
2	b	2	100
3	c	3	200


SELECT table1.id, table1.name, table2.id, table2.salary
FROM table1
LEFT JOIN table2 ON table1.id = table2.id;

// output
2	b	2	100
3	c	3	200
1	a		
4	d		

SELECT table1.id, table1.name, table2.id, table2.salary
FROM table1
// output
RIGHT JOIN table2 ON table1.id = table2.id;
2	b	2	100
3	c	3	200
		5	600


SELECT * 
FROM table1
LEFT JOIN table2 ON table1.id = table2.id
UNION
SELECT * 
FROM table1
RIGHT JOIN table2 ON table1.id = table2.id;
// output
2	b	2	100
3	c	3	200
1	a		
4	d		
		5	600
```