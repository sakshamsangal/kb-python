# Oracle database set up

```
Download and install OracleXE112_Win64.zip

Got to http://127.0.0.1:8080/apex/f?p=4950:1:3636606493993877

username = sys 
password = root

Go to application express >> object browser

CREATE table and insert data

CREATE maven-quickstart project

add oracle dependency

Download ojdbc6.jar 

Execute in the terminal: mvn install:install-file -DgroupId=com.oracle -DartifactId=ojdbc6 -Dversion=11.2.0.3 -Dpackaging=jar -Dfile=D:/Temporary/ojdbc6.jar -DgeneratePom=true

Write the jdbc oracle connectivity code.
```

CREATE TABLE customers(customer_id number(10) , customer_name varchar2(50)NOT NULL, city varchar2(50));

    create table customer(id number(2));