# @Autowired

## POJO

```
Employee
	@Autowired
	Address
```

## config.xml

``` xml
<context:annotation-config />

<bean 
	class="com.spring.annotation.Address" 
	name="address" 
	p:hno="12" 
	p:street="silicon valley" 
	p:city="mumbai"/>	
<bean 
	class="com.spring.annotation.Employee" 
	name="employee"/>		
```

## Autowire using constructor

### POJO

``` 
Employee
	Address address
```

### config.xml

``` xml
<bean 
	class="com.spring.autowire.Address" 
	name="address" 
	p:hno="12" 
	p:street="silicon valley" 
	p:city="mumbai" />	
<bean 
	class="com.spring.autowire.Employee" 
	name="employee" 
	autowire="constructor" />
```

## Autowire by name

``` xml
<bean class="com.spring.autowire.Address" name="address" p:hno="12" p:street="silicon valley" p:city="mumbai" />
<bean class="com.spring.autowire.Address" name="address2" p:hno="32" p:street="silicon valley" p:city="mumbai" />
<bean class="com.spring.autowire.Employee" name="employee" autowire="byName" />	
```

### POJO

```
Employee
	@Autowired
	@Qualifier("a1")
	Address
```

### config.xml

``` xml
<context:annotation-config />
<bean class="com.spring.annotation.Address" name="a1" p:hno="12" p:street="silicon valley" p:city="mumbai" />
<bean class="com.spring.annotation.Employee" name="employee" />	

```

# @Component

## POJO

```
// default is instructor
@Component("instructor")
Instructor
	int id
	String name
```

## config.xml

``` xml
<context:component-scan base-package="com.spring.stereotype" />	
```

# @Required

```
Patient

	private int id;
	private String name;
	
	@Required
	public void setId(int id) {
		this.id = id;
	}

```	
***
[Back](./index.md)
