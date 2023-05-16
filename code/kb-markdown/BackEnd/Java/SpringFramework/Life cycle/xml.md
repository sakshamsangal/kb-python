```
package com.spring.lifecyclexml;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {
	public static void main(String[] args) {
		AbstractApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/lifecyclexml/config.xml");
		Patient patient = (Patient) applicationContext.getBean("patient");
		
		System.out.println(patient.toString());
		applicationContext.registerShutdownHook();
	}
}
```

```
package com.spring.lifecyclexml;

public class Patient {
	private int id;

	public void init() {
		System.out.println("init()");
	}
	
	public void destroy() {
		System.out.println("destroy()");
	}
	
	public int getId() {
		return id;
	}

	public void setId(int id) {
		System.out.println("setId()");
		this.id = id;
	}

	@Override
	public String toString() {
		return "Patient [id=" + id + "]";
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

	<bean class="com.spring.lifecyclexml.Patient" name="patient" p:id="10" init-method="init" destroy-method="destroy" />
	
</beans>
```

```
Output:
setId()
init()
Patient [id=10]
destroy()
```