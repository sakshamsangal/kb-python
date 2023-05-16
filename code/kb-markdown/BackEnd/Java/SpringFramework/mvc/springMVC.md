# Spring MVC

## controller

``` java
@Controller
public class ListController {

    @RequestMapping("select-list")
    public ModelAndView sendList() {
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.setViewName("selectList");

        Employee employee1 = new Employee();
        employee1.setId(111);
        employee1.setName("sahitya");
        employee1.setSalary("4565");


        Employee employee2 = new Employee();
        employee2.setId(121);
        employee2.setName("sahitya2");
        employee2.setSalary("45656575");

        List<Employee> employees = new ArrayList<>();
        employees.add(employee1);
        employees.add(employee2);

        modelAndView.addObject("employees", employees);
        return modelAndView;
    }

}




@Controller
public class ObjectController {

    @RequestMapping("select-object")
    public ModelAndView sendObject() {
        ModelAndView modelAndView = new ModelAndView();
        modelAndView.setViewName("selectObject");

        Employee employee = new Employee();
        employee.setId(111);
        employee.setName("sahitya");
        employee.setSalary("4565");

        modelAndView.addObject(employee);

        return modelAndView;
    }

}



@Controller
public class PrimitiveController {

    @RequestMapping("select-primitive")
    public ModelAndView selectPrimitive() {

        ModelAndView modelAndView = new ModelAndView();
        modelAndView.setViewName("selectPrimitive");

        modelAndView.addObject("id", 12);
        modelAndView.addObject("name", "sak");
        modelAndView.addObject("salary", "123");

        return modelAndView;
    }
}


@Controller
public class RequestParamController {

    @RequestMapping("select-user-request-param")
    public ModelAndView insertUser(@RequestParam(value = "id", required = false, defaultValue = "12") int id, @RequestParam("userName") String userName) {
        ModelAndView modelAndView = new ModelAndView("selectUser");
        System.out.println(id);
        System.out.println(userName);
        return modelAndView;
    }
}


@Controller
public class UserController {

    @RequestMapping("insert-user")
    public String insertUser() {
        return "insertUser";
    }

    @RequestMapping(value = "select-user", method = RequestMethod.POST)
    public String selectUser(@ModelAttribute("user") User user, ModelMap modelMap) {
        System.out.println(user);
        modelMap.addAttribute("user", user);
        return "selectUser";
    }
}
```

## front-servelet.xml

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:context="http://www.springframework.org/schema/context"
       xmlns:p="http://www.springframework.org/schema/p"
       xmlns:tx="http://www.springframework.org/schema/tx"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context.xsd
    http://www.springframework.org/schema/tx
    http://www.springframework.org/schema/tx/spring-tx.xsd">

    <context:component-scan base-package="com.google" />

    <bean class="org.springframework.web.servlet.view.InternalResourceViewResolver" name="internalResourceViewResolver">
        <property name="prefix">
            <value>/WEB-INF/view/</value>
        </property>
        <property name="suffix">
            <value>.jsp</value>
        </property>
        
    </bean>

</beans>
```

## pojo

```
Employee 
    int id
    String name
    String salary



User 
    int id
    String userName

```

## JSP pages

``` html
<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1" isELIgnored="false"%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Hello World Java EE</title>
</head>
<body>
    <pre>
        <form action="select-user" method="post">
            <input type="text" name="id" />
            <input type="text" name="userName" />
            <button type="submit">Submit</button>
        </form>
    </pre>
    
</body>
</html>


<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1" isELIgnored="false"
    import="com.google.model.pojo.Employee, java.util.List"
    %>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Hello World Java EE</title>
</head>
<body>
<%
    List<Employee> employees = (List<Employee>) request.getAttribute("employees");
    for(Employee employee: employees) {
        out.println(employee.getId());
    }
%>
</body>
</html>


<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1" isELIgnored="false" %>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Hello World Java EE</title>
</head>
<body>
    <h1>selectObject</h1>
    <%= request.getAttribute("employee") %>

</body>
</html>

<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1" isELIgnored="false"%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>selectPrimitive</title>
</head>
<body>
    <h1>selectPrimitive</h1>

    <h3>Using servlet </h3>
    <%
        Integer id = (Integer)request.getAttribute("id");
        String name = (String)request.getAttribute("name");
        String salary = (String)request.getAttribute("salary");
        out.println(id);
        out.println(name);
        out.println(salary);
    %>

    <h3>Using EL </h3>
    <ul>
        <li>${id}</li>
        <li>${name}</li>
        <li>${salary}</li>
    </ul>
</body>
</html>


<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1" isELIgnored="false"%>
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Hello World Java EE</title>
</head>
<body>
   <%= request.getAttribute("user") %>
</body>
</html>
```

## pom and config

``` xml 
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.example</groupId>
    <artifactId>spring-mvc</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <name>spring-mvc Maven Webapp</name>
    <!-- FIXME change it to the project's website -->
    <url>http://www.example.com</url>

    <properties>
        <springframework.version>4.3.6.RELEASE</springframework.version>
    </properties>

    <dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-webmvc</artifactId>
            <version>${springframework.version}</version>
        </dependency>

    </dependencies>

    <build>
        <finalName>spring-mvc</finalName>
        <pluginManagement><!-- lock down plugins versions to avoid using Maven defaults (may be moved to parent pom) -->
            <plugins>
                <plugin>
                    <artifactId>maven-clean-plugin</artifactId>
                    <version>3.1.0</version>
                </plugin>
                <!-- see http://maven.apache.org/ref/current/maven-core/default-bindings.html#Plugin_bindings_for_war_packaging -->
                <plugin>
                    <artifactId>maven-resources-plugin</artifactId>
                    <version>3.0.2</version>
                </plugin>
                <plugin>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>3.8.0</version>
                </plugin>
                <plugin>
                    <artifactId>maven-surefire-plugin</artifactId>
                    <version>2.22.1</version>
                </plugin>
                <plugin>
                    <artifactId>maven-war-plugin</artifactId>
                    <version>3.2.2</version>
                </plugin>
                <plugin>
                    <artifactId>maven-install-plugin</artifactId>
                    <version>2.5.2</version>
                </plugin>
                <plugin>
                    <artifactId>maven-deploy-plugin</artifactId>
                    <version>2.8.2</version>
                </plugin>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>3.2</version>
                    <configuration>
                        <source>1.8</source>
                        <target>1.8</target>
                    </configuration>
                </plugin>
                <plugin>
                    <groupId>org.apache.tomcat.maven</groupId>
                    <artifactId>tomcat7-maven-plugin</artifactId>
                    <version>2.2</version>
                    <configuration>
                        <port>9090</port>
                    </configuration>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>

<!DOCTYPE web-app PUBLIC
 "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"
 "http://java.sun.com/dtd/web-app_2_3.dtd" >

<web-app>
  <display-name>spring-mvc</display-name>
  
  <servlet>
    <servlet-name>front</servlet-name>
    <servlet-class>org.springframework.web.servlet.DispatcherServlet</servlet-class>
  </servlet>
  <servlet-mapping>
    <servlet-name>front</servlet-name>
    <url-pattern>/</url-pattern>
  </servlet-mapping>
</web-app>

```