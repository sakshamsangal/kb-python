```
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
	xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
	<modelVersion>4.0.0</modelVersion>

	<groupId>com.bharath.springdata.customer</groupId>
	<artifactId>customerdata</artifactId>
	<version>0.0.1-SNAPSHOT</version>
	<packaging>jar</packaging>

	<name>customerdata</name>
	<description>Assignment Solution</description>

	<parent>
		<groupId>org.springframework.boot</groupId>
		<artifactId>spring-boot-starter-parent</artifactId>
		<version>1.5.8.RELEASE</version>
		<relativePath/> <!-- lookup parent from repository -->
	</parent>

	<properties>
		<project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
		<project.reporting.outputEncoding>UTF-8</project.reporting.outputEncoding>
		<java.version>1.8</java.version>
	</properties>

	<dependencies>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-data-jpa</artifactId>
		</dependency>

		<dependency>
			<groupId>mysql</groupId>
			<artifactId>mysql-connector-java</artifactId>
			<scope>runtime</scope>
		</dependency>
		<dependency>
			<groupId>org.springframework.boot</groupId>
			<artifactId>spring-boot-starter-test</artifactId>
			<scope>test</scope>
		</dependency>
	</dependencies>

	<build>
		<plugins>
			<plugin>
				<groupId>org.springframework.boot</groupId>
				<artifactId>spring-boot-maven-plugin</artifactId>
			</plugin>
		</plugins>
	</build>


</project>

package com.bharath.springdata.customer.entities;

import javax.persistence.Embeddable;

@Embeddable
public class Address {

	private String streetAddress;
	private String city;
	private String state;
	private String zipcode;
	private String country;

	public String getCity() {
		return city;
	}

	public void setCity(String city) {
		this.city = city;
	}

	public String getState() {
		return state;
	}

	public void setState(String state) {
		this.state = state;
	}

	public String getZipcode() {
		return zipcode;
	}

	public void setZipcode(String zipcode) {
		this.zipcode = zipcode;
	}

	public String getCountry() {
		return country;
	}

	public void setCountry(String country) {
		this.country = country;
	}

	public String getStreetAddress() {
		return streetAddress;
	}

	public void setStreetAddress(String streetAddress) {
		this.streetAddress = streetAddress;
	}

}

package com.bharath.springdata.customer.entities;

import javax.persistence.Embedded;
import javax.persistence.Entity;
import javax.persistence.GeneratedValue;
import javax.persistence.GenerationType;
import javax.persistence.Id;

@Entity
public class Customer {

	@Id
	@GeneratedValue(strategy = GenerationType.AUTO)
	private int id;
	private String name;
	private String email;
	@Embedded
	private Address address;

	public int getId() {
		return id;
	}

	public void setId(int id) {
		this.id = id;
	}

	public String getName() {
		return name;
	}

	public void setName(String name) {
		this.name = name;
	}

	public String getEmail() {
		return email;
	}

	public void setEmail(String email) {
		this.email = email;
	}

	public Address getAddress() {
		return address;
	}

	public void setAddress(Address address) {
		this.address = address;
	}

	@Override
	public String toString() {
		return "Customer [id=" + id + ", name=" + name + ", email=" + email + "]";
	}

}


package com.bharath.springdata.customer.repository;

import org.springframework.data.jpa.repository.Modifying;
import org.springframework.data.jpa.repository.Query;
import org.springframework.data.repository.CrudRepository;
import org.springframework.data.repository.query.Param;

import com.bharath.springdata.customer.entities.Customer;
import java.lang.String;
import java.util.List;

public interface CustomerRepository extends CrudRepository<Customer, Integer> {

	List<Customer> findByNameAndEmail(String name, String email);

	List<Customer> findByEmailLike(String email);

	List<Customer> findByIdIn(List<Integer> ids);

	@Modifying
	@Query("update Customer cust set cust.email = :email where cust.id=:id")
	void updateEmail(@Param("id") int id, @Param("email") String email);

}


package com.bharath.springdata.customer;

import org.springframework.boot.SpringApplication;
import org.springframework.boot.autoconfigure.SpringBootApplication;

@SpringBootApplication
public class CustomerdataApplication {

	public static void main(String[] args) {
		SpringApplication.run(CustomerdataApplication.class, args);
	}
}


spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=test

spring.jpa.show-sql=true


package com.bharath.springdata.customer;

import java.util.Arrays;

import org.junit.Test;
import org.junit.runner.RunWith;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.boot.test.context.SpringBootTest;
import org.springframework.test.annotation.Rollback;
import org.springframework.test.context.junit4.SpringRunner;
import org.springframework.transaction.annotation.Transactional;

import com.bharath.springdata.customer.entities.Address;
import com.bharath.springdata.customer.entities.Customer;
import com.bharath.springdata.customer.repository.CustomerRepository;

@RunWith(SpringRunner.class)
@SpringBootTest
public class CustomerdataApplicationTests {

	@Autowired
	private CustomerRepository customerRepository;

	@Test
	public void testCreateCustomer() {
		Customer customer = new Customer();
		customer.setName("John");
		customer.setEmail("john@gmail.com");
		customerRepository.save(customer);
	}

	@Test
	public void testReadCustomer() {
		Customer customer = customerRepository.findOne(1);
		System.out.println(customer);
	}

	@Test
	public void testUpdateCustomer() {
		Customer customer = customerRepository.findOne(1);
		customer.setName("John Reddy");
		customerRepository.save(customer);
	}

	@Test
	public void testDeleteCustomer() {
		customerRepository.delete(1);
	}
	
	@Test
	public void testCreateCustomerWithAddress() {
		Customer customer = new Customer();
		customer.setName("John");
		customer.setEmail("john@gmail.com");
		
		Address address = new Address();
		address.setCity("Austin");
		address.setState("Texas");
		address.setStreetAddress("Spice Wood Springs");
		address.setCountry("USA");
		address.setZipcode("78755");
		customer.setAddress(address);
		
		customerRepository.save(customer);
		
	}
	
	@Test
	public void testFindByNameAndEmail() {
		System.out.println(customerRepository.findByNameAndEmail("John","john@gmail.com"));
	}
	
	@Test
	public void testFindByEmailLike() {
		System.out.println(customerRepository.findByEmailLike("%john@g%"));
	}
	
	@Test
	public void testFindByIdIn() {
		System.out.println(customerRepository.findByIdIn(Arrays.asList(2)));
	}
	
	@Test
	@Transactional
	@Rollback(false)
	public void testUpdateEmail() {
		customerRepository.updateEmail(2, "john@bharathmail.com");
	}

}

```