# Constructor

## POJO

``` 
Employee
	int id
	String name
```

## c schema

```
xmlns:c="http://www.springframework.org/schema/c"
<bean class="com.spring.constructor.Employee" name="employee" c:id="20" c:name="saksham" />
```

```
<bean id = "onlineBakery" class = "com.upgrad.course.bakery.OnlineBakery">
	<constructor-arg ref = "cakeInventory"/>
	<property name = "breadInventory" ref = "breadInventory"/>
</bean>
```

## constructor-arg tag

``` xml
<bean class="com.spring.constructor.Employee" name="employee">
	<constructor-arg>
		<value>20</value>
	</constructor-arg>
	<constructor-arg>
		<value>saksham</value>
	</constructor-arg>
</bean>

<!-- OR -->
<bean class="com.spring.constructor.Employee" name="employee">
	<constructor-arg value="20" />
	<constructor-arg value="saksham" />
</bean>

```

# Passing int value in method but spring taking as String

## POJO

``` java
public class Addition {
	public Addition(int a, int b) {
		System.out.println("int");
	}
	public Addition(double a, double b) {
		System.out.println("double");
	}
	// default is string
	public Addition(String a, String b) {
		System.out.println("string");
	}
}
```

## config.xml

``` xml
<bean class="com.spring.ambuigity.Addition" name="addition" >
	<constructor-arg value="10" />
	<constructor-arg value="20" />
</bean>
```

## Output

```
string
```

## Solution

```
<constructor-arg value="10" type="int" />
<constructor-arg value="20" type="int" />

Now the output will be int
```

# Insert order of setting values is not followed

## POJO

``` java
public class Addition {

	public Addition(int a, double b) {
		System.out.println("int double");
		System.out.println("a = " + a + " b = " + b);
	}

}
```

## config.xml

``` xml
<bean class="com.spring.ambuigity.Addition" name="addition" >
	<!-- first parameter -->
	<constructor-arg value="10.56" type="double" /> 

	<!-- second parameter -->
	<constructor-arg value="20" type="int" />
</bean>

```

## Output

```
int double
a = 20 b = 10.56
```

## Solution

```
<constructor-arg value="10.56" type="double" index="0"/>
<constructor-arg value="20" type="int" index="1"/>

It is make suring insertion order is preserved thats why error
Unsatisfied dependency expressed through constructor parameter 0: Ambiguous argument values for parameter of type [int]
```

***
[Back](./index.md)
