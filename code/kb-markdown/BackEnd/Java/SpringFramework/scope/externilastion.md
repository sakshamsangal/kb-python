# externalization

```
# details
dbServer=sakshamServer
dbPort=8080
dbUser=root
dbPass=pass
```

```
package com.spring.externalization;

public class MyDAO {
	private String dbServer;

	public MyDAO(String dbServer) {
		super();
		this.dbServer = dbServer;
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

	<context:property-placeholder location="com/spring/externalization/database.properties"/>
	<bean class="com.spring.externalization.MyDAO" name="myDAO" >
		<constructor-arg value="${dbServer}" />
	</bean>
		

</beans>
```

```
package com.spring.externalization;

import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {

	public static void main(String[] args) {
		
		
		ClassPathXmlApplicationContext classPathXmlApplicationContext = new ClassPathXmlApplicationContext("com/spring/externalization/config.xml");
		MyDAO myDAO = (MyDAO) classPathXmlApplicationContext.getBean("myDAO");
		
		System.out.println(myDAO);
	
		

	}

}
```

```
MyDAO [dbServer=sakshamServer]
