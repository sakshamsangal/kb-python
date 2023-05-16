# innerBean

```
Address 
	int hno
	String street
	String city


Employee 
	int id
	Address address
```

```
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context.xsd">

	<bean class="com.spring.innerbean.Employee" name="employee" p:id="10" >
		<property name="address">
			<bean class="com.spring.innerbean.Address" p:hno="12" p:street="silicon valley" p:city="mumbai" />
		</property>
	</bean>
	
</beans>
```

```
public class Test {
	public static void main(String[] args) {

		ApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/innerbean/config.xml");
		Employee employee = (Employee) applicationContext.getBean("employee");
		
		System.out.println(employee.toString());

	}
}
```

```
Employee [id=10, address=Address [hno=12, street=silicon valley, city=mumbai]]
```