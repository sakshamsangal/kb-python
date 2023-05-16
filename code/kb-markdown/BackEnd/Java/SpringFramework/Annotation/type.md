```
package com.spring.autowire;

public class Employee {

	private Address address;
	
	public Address getAddress() {
		return address;
	}
	public void setAddress(Address address) {
		this.address = address;
	}
	@Override
	public String toString() {
		return "Employee [address=" + address + "]";
	}
	
	
}
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

	<bean class="com.spring.autowire.Address" name="address" p:hno="12" p:street="silicon valley" p:city="mumbai" />
	
	<bean class="com.spring.autowire.Employee" name="employee" autowire="byType" />	
	
</beans>
```

```
package com.spring.autowire;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {
	public static void main(String[] args) {

		ApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/autowire/config.xml");
		Employee employee = (Employee) applicationContext.getBean("employee");
		
		System.out.println(employee);

	}
}
```

```
Employee [address=Address [hno=12, street=silicon valley, city=mumbai]]
```

```
// error
package com.spring.autowire;

public class Employee {

	private Address address;
	
	public Address getAddress() {
		return address;
	}
	public void setAddress(Address address) {
		this.address = address;
	}
	@Override
	public String toString() {
		return "Employee [address=" + address + "]";
	}
	
	
}
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

	<bean class="com.spring.autowire.Address" name="address1" p:hno="12" p:street="silicon valley" p:city="mumbai" />
	<bean class="com.spring.autowire.Address" name="address2" p:hno="12" p:street="silicon valley" p:city="mumbai" />
	
	<bean class="com.spring.autowire.Employee" name="employee" autowire="byType" />	
	
</beans>
```

```
package com.spring.autowire;

import org.springframework.context.ApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {
	public static void main(String[] args) {

		ApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/autowire/config.xml");
		Employee employee = (Employee) applicationContext.getBean("employee");
		
		// because search by type, therefore there is error
		System.out.println(employee);

	}
}

```

> No qualifying bean of type 'com.spring.autowire.Address' available: expected single matching bean but found 2:
> address1,address2
