```
-- TODO 1: Create the ‘vote’ table.
CREATE TABLE vote (
    voter_id VARCHAR(10),
    constituency_id VARCHAR(10),
    candidate_id VARCHAR(10),
    date_of_voting DATE
);

--TODO 2: Insert records into the ‘vote’ table.
INSERT INTO vote VALUES(
    'SMO-009211',
    'CO-0000651',
    'CA-0012892',
    '98-3-01'
);

INSERT INTO vote VALUES(
    'SMO-009212',
    'CO-0000652',
    'CA-0012802',
    '98-3-01'
);
-- TODO 3: Fetch the records from the ‘vote’ table as Id for the record CA-0012802

CREATE TABLE voter (
    voter_id VARCHAR(10),
    voter_name VARCHAR(40)
);


CREATE TABLE constituency (
    constituency_id VARCHAR(10),
    constituency_name VARCHAR(40)
);


INSERT INTO voter VALUES(
    'SMO-009211',
    'Sachin Sharma'
);

INSERT INTO voter VALUES(
    'SMO-009212',
    'Rahul Verrma'
);

INSERT INTO constituency VALUES(
    'CO-0000651',
    'South Delhi'
);

INSERT INTO constituency VALUES(
    'CO-0000652',
    'North Delhi'
);



```

CREATE TABLE patient (
#id INT primary key auto_increment,
#patient_name VARCHAR(50),
#pr INT,
#bp_systolic INT,
#bp_diastolic INT,
#temp DECIMAL(8,4),
#rr INT,
#spo2 INT,
#o2 DECIMAL(8,4),
#fio2 DECIMAL(8,4),
#other VARCHAR(100),
#remarks VARCHAR(100),
#gcs DECIMAL(8,4),
#urine DECIMAL(8,4),
#inotrope VARCHAR(100),
#position VARCHAR(100),
#Intake VARCHAR(100),
#Steroids VARCHAR(100),
#Antibiotics VARCHAR(100),
#Clexane VARCHAR(100)
);
