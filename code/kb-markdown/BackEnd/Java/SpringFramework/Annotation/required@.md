> To make mandatory attribute using @Required
>
> @Required is applied only on setter method

# Patient.java

```
package com.spring.dependencycheck;

import java.util.List;

import org.springframework.beans.factory.annotation.Required;

public class Patient {

	private int id;
	private String name;
	private List<String> medicine;
	
	public int getId() {
		return id;
	}
	
	@Required
	public void setId(int id) {
		this.id = id;
	}
	
	public String getName() {
		return name;
	}
	
	public void setName(String name) {
		this.name = name;
	}
	
	public List<String> getMedicine() {
		return medicine;
	}
	
	public void setMedicine(List<String> medicine) {
		this.medicine = medicine;
	}
	
	@Override
	public String toString() {
		return "Patient [id=" + id + ", name=" + name + "]";
	}
	
}
```

# config.xml

<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:context="http://www.springframework.org/schema/context"
xmlns:p="http://www.springframework.org/schema/p"
xsi:schemaLocation="http://www.springframework.org/schema/beans
http://www.springframework.org/schema/beans/spring-beans.xsd
http://www.springframework.org/schema/context
http://www.springframework.org/schema/context/spring-context.xsd">

	<bean class="com.spring.dependencycheck.Patient" name="patient" p:id="12" />
	<bean class="org.springframework.beans.factory.annotation.RequiredAnnotationBeanPostProcessor" />

</beans>

# Test.java

```
package com.spring.dependencycheck;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {
	public static void main(String[] args) {		
		try {
			ApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/dependencycheck/config.xml");
			Patient patient = (Patient) applicationContext.getBean("patient");
			System.out.println(patient);
		} catch (Exception e) {
			System.err.println("\nError: " + e.getMessage());
		}
		
	}
}
```

```
Output:
Patient [id=12, name=null]
```
