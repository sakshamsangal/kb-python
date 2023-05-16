# Standalone

```
ProductList 
	List<String> productNames
```

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
	xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:context="http://www.springframework.org/schema/context"
	xmlns:p="http://www.springframework.org/schema/p"
	xmlns:util="http://www.springframework.org/schema/util"
	xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context.xsd
    http://www.springframework.org/schema/util
    http://www.springframework.org/schema/util/spring-util.xsd">

	<util:list list-class="java.util.LinkedList" id="productNames">
		<value>macbook</value>
		<value>iphone</value>
	</util:list>
	
	
	<bean class="com.spring.standalone.ProductList" name="productList" p:productNames-ref="productNames" />
		
</beans>
```

``` java
public class Test {
	public static void main(String[] args) {

		ApplicationContext applicationContext = new ClassPathXmlApplicationContext("com/spring/standalone/config.xml");
		ProductList productList = (ProductList) applicationContext.getBean("productList");
		
		// because search by type, therefore there is error
		System.out.println(productList);

	}
}
```

## Output

```
ProductList [productNames=[macbook, iphone]]
```