```
package com.spring.lifecycleinterface;

import org.springframework.beans.factory.DisposableBean;
import org.springframework.beans.factory.InitializingBean;

public class Patient implements InitializingBean, DisposableBean{
	private int id;
	
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

	@Override
	public void afterPropertiesSet() throws Exception {
		System.out.println("afterPropertiesSet()");
	}

	@Override
	public void destroy() throws Exception {
		System.out.println("destroy()");
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

	<bean class="com.spring.lifecycleinterface.Patient" name="patient" p:id="10" />
	
</beans>
```

```

package com.spring.lifecycleinterface;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {
	public static void main(String[] args) {
		AbstractApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/lifecycleinterface/config.xml");
		Patient patient = (Patient) applicationContext.getBean("patient");
		
		System.out.println(patient.toString());
		applicationContext.registerShutdownHook();
				
	}
}
```

```

setId()
afterPropertiesSet()
Patient [id=10]
destroy()
```

```
 package com.spring.annotation;

import javax.annotation.PostConstruct;
import javax.annotation.PreDestroy;

public class Patient {

	private int id;

	@PostConstruct
	public void init() {
		System.out.println("init()");
	}
	
	@PreDestroy
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

	<bean class="com.spring.annotation.Patient" name="patient" p:id="10" />
	<bean class="org.springframework.context.annotation.CommonAnnotationBeanPostProcessor" />
	
</beans>
```

```

package com.spring.annotation;

import org.springframework.context.support.AbstractApplicationContext;
import org.springframework.context.support.ClassPathXmlApplicationContext;

public class Test {

	public static void main(String[] args) {
		AbstractApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/annotation/config.xml");
		Patient patient = (Patient) applicationContext.getBean("patient");
		
		System.out.println(patient.toString());
		applicationContext.registerShutdownHook();

	}
	
	
	

}
```

```
setId()
init()
Patient [id=10]
destroy()

```

```
<bean class="com.spring.annotation.Patient" name="patient" p:id="10" />
<context:annotation-config />
```