# Generators

## 1. Introduction

```

```

## 2. Create the database schema

```

```

## 2.1 ID Gen-employee.sql

```sql
use mydb

create table employee(
id int,
name varchar(20)
)

drop table employee
```

## 3. Create a Spring Data Project

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-data-jpa</artifactId>
</dependency>

<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <scope>runtime</scope>
</dependency>
```

## 4. Create an Entity

```java
package com.bharath.springdata.idgenerators.entities;

import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.Id;

import org.hibernate.annotations.GenericGenerator;

@Entity
public class Employee {

	//@TableGenerator(name = "employee_gen", table = "id_gen", pkColumnName = "gen_name", valueColumnName = "gen_val",allocationSize=100)
	@GenericGenerator(name="emp_id",strategy="com.bharath.springdata.idgenerators.CustomRandomIDGenerator")
	@GeneratedValue(generator="emp_id")
	@Id
	//@GeneratedValue(strategy = GenerationType.TABLE,generator="employee_gen")
	private Long id;
	private String name;

	public Long getId() {
		return id;
	}

	public void setId(Long id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

}
```

## 5. Create the repository

```java
package com.bharath.springdata.idgenerators.repos;

import org.springframework.data.repository.CrudRepository;

import com.bharath.springdata.idgenerators.entities.Employee;


public interface EmployeeRepository extends CrudRepository<Employee, Long> {

}
```

## 6. Configure the data source

```java
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=test

spring.jpa.show-sql=true
```

## 7. Save Employee

```java
package com.bharath.springdata.idgenerators;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.context.junit4.SpringRunner;

import com.bharath.springdata.idgenerators.entities.Employee;
import com.bharath.springdata.idgenerators.repos.EmployeeRepository;

@RunWith(SpringRunner.class)
@SpringBootTest
public class IdgeneratorsApplicationTests {

	@Autowired
	EmployeeRepository er;

	@Test
	public void testCreateEployee() {

		Employee employee = new Employee();
		employee.setName("John");

		er.save(employee);
	}

}
```

## 8. Use the identity generator type

```

```

## 9. Update the DB Schema for Table Strategy

```

```

## 9.1 IG GEN TABLE.sql

```sql
create table id_gen(
    gen_name varchar(60) PRIMARY KEY,
    gen_val int(20)
)
```

## 10. Configure the Table Strategy

```

```

## 11. Develop Custom Generator

```

```

## 12. Configure and Use the Custom Generator

```

```

## 13. Generators.html

```

```

## 14. ID Generation.html

```

```
