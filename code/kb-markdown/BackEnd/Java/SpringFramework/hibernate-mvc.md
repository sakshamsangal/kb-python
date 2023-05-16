# Hibernate MVC

# UserController.java

``` java
package base.controller;

import base.model.pojo.User;
import base.model.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.*;

import java.util.List;

@Controller
public class UserController {
    @Autowired
    UserService userService;

    public UserService getUserService() {
        return userService;
    }

    public void setUserService(UserService userService) {
        this.userService = userService;
    }

    @RequestMapping("/req1")
    public String req1() {
        return "page1";
    }

    @RequestMapping("/loadAll")
    public String loadAll(ModelMap modelMap) {
        List<User> users = userService.loadAll();
        modelMap.addAttribute("users", users);
        return "page3";
    }

    @RequestMapping(value = "/req2", method = RequestMethod.POST)
    public String req2(@ModelAttribute("user") User user, ModelMap modelMap) {
        int id = userService.insert(user);
        modelMap.addAttribute("id", id);
        return "page1";
    }

    @RequestMapping("/req4")
    public @ResponseBody String req4(@RequestParam("id") int id) {
        User user = userService.findUser(id);
        String msg = "";
        if(user != null) msg = "already exist";
        return msg;
    }
}
```

# UserDao.java

``` java
package base.model.dao;

import base.model.pojo.User;

import java.util.List;

public interface UserDao {
    int insert(User user);
    List<User> loadAll();
    User findUser(Integer id);
}

```

# UserDaoImpl.java

``` java
package base.model.daoimpl;

import base.model.dao.UserDao;
import base.model.pojo.User;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.orm.hibernate5.HibernateTemplate;
import org.springframework.stereotype.Repository;

import java.util.List;

@Repository
public class UserDaoImpl implements UserDao {

    @Autowired
    private HibernateTemplate hibernateTemplate;

    public HibernateTemplate getHibernateTemplate() {
        return hibernateTemplate;
    }

    public void setHibernateTemplate(HibernateTemplate hibernateTemplate) {
        this.hibernateTemplate = hibernateTemplate;
    }

    @Override
    public int insert(User user) {
        int result = (int) hibernateTemplate.save(user);
        return result;
    }

    @Override
    public List<User> loadAll() {
        return hibernateTemplate.loadAll(User.class);

    }

    @Override
    public User findUser(Integer id) {
        return hibernateTemplate.get(User.class, id);
    }
}

```

# User

``` java
package base.model.pojo;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity
public class User implements Comparable<User>{

    @Id
    private Integer id;
    private String name;
    private String email;

    @Override
    public String toString() {
        return "User{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", email='" + email + '\'' +
                '}';
    }


    public Integer getId() {
        return id;
    }

    public void setId(Integer id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public int compareTo(User user) {
        return this.name.compareTo(user.name);
    }
}
```

# UserService.java

``` java
package base.model.service;

import base.model.pojo.User;

import java.util.List;

public interface UserService {
    int insert(User user);
    List<User> loadAll();
    User findUser(Integer id);
}

```

# UserServiceImpl.java

``` java
package base.model.serviceImpl;

import base.model.dao.UserDao;
import base.model.pojo.User;
import base.model.service.UserService;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Service;
import org.springframework.transaction.annotation.Transactional;

import java.util.Collection;
import java.util.Collections;
import java.util.List;

@Service
public class UserServiceImpl implements UserService {
    @Autowired
    private UserDao userDao;

    public UserDao getUserDao() {
        return userDao;
    }

    public void setUserDao(UserDao userDao) {
        this.userDao = userDao;
    }

    @Override
    @Transactional
    public int insert(User user) {
        return userDao.insert(user);
    }

    @Override
    public List<User> loadAll() {
        List<User> users = userDao.loadAll();
        Collections.sort(users);
        return users;
    }

    @Override
    public User findUser(Integer id) {
        return userDao.findUser(id);
    }
}
```

# pom.xml

``` xml
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>org.example</groupId>
  <artifactId>spring-mvc-hibernate</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>war</packaging>

  <name>spring-mvc-hibernate Maven Webapp</name>
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
    <dependency>
      <groupId>org.springframework</groupId>
      <artifactId>spring-orm</artifactId>
      <version>${springframework.version}</version>
    </dependency>
    <dependency>
      <groupId>org.hibernate</groupId>
      <artifactId>hibernate-core</artifactId>
      <version>5.2.17.Final</version>
    </dependency>
    <dependency>
      <groupId>mysql</groupId>
      <artifactId>mysql-connector-java</artifactId>
      <version>8.0.13</version>
    </dependency>
    <dependency>
      <groupId>jstl</groupId>
      <artifactId>jstl</artifactId>
      <version>1.2</version>
    </dependency>
    <dependency>
      <groupId>taglibs</groupId>
      <artifactId>standard</artifactId>
      <version>1.1.2</version>
    </dependency>
  </dependencies>

  <build>
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

```

# config.xml

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

    <tx:annotation-driven/>

    <context:component-scan base-package="base" />

    <bean class="org.springframework.jdbc.datasource.DriverManagerDataSource" name="dataSource">
        <property name="driverClassName">
            <value>com.mysql.cj.jdbc.Driver</value>
        </property>

        <property name="url">
            <value>jdbc:mysql://localhost/mydb</value>
        </property>

        <property name="username">
            <value>root</value>
        </property>

        <property name="password">
            <value>root</value>
        </property>
    </bean>

    <bean class="org.springframework.orm.hibernate5.LocalSessionFactoryBean" name="localSessionFactoryBean">
        <property name="dataSource">
            <ref bean="dataSource"/>
        </property>
        <property name="hibernateProperties">
            <props>
                <prop key="hibernate.dialect">org.hibernate.dialect.MySQLDialect</prop>
                <prop key="hibernate.show_sql">true</prop>
            </props>
        </property>
        <property name="annotatedClasses">
            <list>
                <value>base.model.pojo.User</value>
            </list>
        </property>
    </bean>

    <bean class="org.springframework.orm.hibernate5.HibernateTemplate" name="hibernateTemplate">
        <property name="sessionFactory">
            <ref bean="localSessionFactoryBean"/>
        </property>
    </bean>

    <bean class="org.springframework.orm.hibernate5.HibernateTransactionManager" name="transactionManager">
        <property name="sessionFactory">
            <ref bean="localSessionFactoryBean"/>
        </property>
    </bean>

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

# web app xml

``` xml
<!DOCTYPE web-app PUBLIC
        "-//Sun Microsystems, Inc.//DTD Web Application 2.3//EN"
        "http://java.sun.com/dtd/web-app_2_3.dtd" >
<web-app>

  <display-name>Archetype Created Web Application</display-name>

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

```
web-app
	display-name
	servlet
		name
		class
	mapping
		name
		url-pattern

```

# ajax page .jsp

``` html
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ page isELIgnored="false" %>
<html>
   <head>
        <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.4.1/jquery.min.js"></script>
        <script>
            $(document).ready(() => {
                $("#id1").change(() => {
                    $.ajax({
                        url: "req4",
                        data: {id: $("#id1").val()},
                        success: function(response) {
                            $("#errorMessage").text(response);
                        }
                    });
                });
            });
        </script>
   </head>
   <body>
        <form action="req2" method="post">
            <input type="text" name="id" id="id1"/>
            <span id="errorMessage"></span><br/>
            <input type="text" name="name" />
            <input type="text" name="email" />
            <button type="submit">Submit</button>
        </form>
        ${id}
   </body>
</html>
```

# for each page .jsp

``` html
<%@ page language="java" contentType="text/html; charset=ISO-8859-1" pageEncoding="ISO-8859-1"%>
<%@ page isELIgnored="false"%>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<html>
   <body>
        <c:forEach items="${users}" var="user">
            ${user.id}
            ${user.name}
            ${user.email}<br/>
        </c:forEach>
   </body>
</html>

```

# Run

mvn clean install

mvn tomcat7:run

# Database

use mydb;

create table user(id int primary key,name varchar(20),email varchar(30));

drop table user;

select * from user;

