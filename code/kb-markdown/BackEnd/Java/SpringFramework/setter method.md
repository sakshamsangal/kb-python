# Setter method

setGender = `<property name="gender">`

## Primitive field POJO

```
Employee
    int id
    String name
```

### Using value as tag and attribute

``` xml
<bean 
    class="com.spring.primitive.Employee" 
    name="employee">

    <!-- value as tag -->
    <property name="id">
        <value>20</value>
    </property>
    
    <!-- value as attribute -->
    <property 
        name="name" 
        value="saksham"/> 

</bean>
```

### Using p schema

``` xml
<bean 
    class="com.spring.primitive.Employee" 
    name="employee" 
    p:id="20" 
    p:name="saksham"/>
```

## List field POJO

```
Hospital 
	String name
	List<String> departments
```

``` xml
<property name="departments">
    <!-- empty list -->
    <list /> 
</property>
	
<property name="departments">
    <!-- single element -->
    <value>1</value>
</property>

<property name="departments">
    <list>
        <value>1</value>
        <value>2</value>
        <value>3</value>
    </list>
</property>
```

## Map field POJO

```
Customer
	int id;
	Map<Integer, String> products;
```

``` xml
<property name="products">
    <map>
        <entry key="100" value="asus"></entry>
        <entry key="200">
            <value>moto</value>
        </entry>
        <entry value="mi">
            <key>
                <value>300</value>
            </key>
        </entry>
        <entry>
            <key>
                <value>400</value>
            </key>
            <value>iphone</value>
        </entry>
    </map>
</property>
```

## Properties field POJO

```
Language 
	Properties countryAndLanguage
```

``` xml
<property name="countryAndLanguage">
    <props>
        <prop key="India">Hindi</prop>
        <prop key="USA">English</prop>
    </props>
</property>
``` 

## Reference field POJO

```
Score
	Double maths
	Double physics
	Double chemistry


Student
	Score score
``` 

``` xml
<bean class="com.spring.reference.Score" name="score" p:maths="67" p:physics="78" p:chemistry="89"/>

<bean class="com.spring.reference.Student" name="student">

    <property name="score">
        <ref bean="score"/>
    </property>
</bean>

<!-- OR -->
<bean class="com.spring.reference.Student" name="student">	
    <property name="score" ref="score" />
</bean>

<!-- OR -->
<bean class="com.spring.reference.Student" name="student" p:score-ref="score" />
```

## Set field POJO

```
CarDealer
	String name
	Set<String> models
```

``` xml
<property name="models">
    <set>
        <value>1</value>
        <value>2</value>
        <value>3</value>
    </set>
</property>
```

***
[Back](./index.md)
