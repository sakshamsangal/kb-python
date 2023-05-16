# single scope

```
Employee
	int id
	String name
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

	<bean class="com.spring.scope.Employee" name="employee" p:id="20" p:name="saksham" scope="singleton"/>

</beans>
```

```
public class Test {

	public static void main(String[] args) {
		// TODO Auto-generated method stub
		
		ApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/scope/config.xml");
		Employee employee1 = (Employee) applicationContext.getBean("employee");
		Employee employee2 = (Employee) applicationContext.getBean("employee");
		
		System.out.println(employee1.hashCode());
		System.out.println(employee2.hashCode());

	}

}
```

```
650023597
650023597
```
