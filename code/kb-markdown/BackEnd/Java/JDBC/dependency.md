```
// default is get

// embedded tomcat
<plugin>
    <groupId>org.apache.tomcat.maven</groupId>
    <artifactId>tomcat7-maven-plugin</artifactId>
    <version>2.2</version>
    <configuration>
    <port>8080</port>
    <path>/</path>
    </configuration>
</plugin>

// mysql
<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <version>8.0.13</version>
</dependency>

// servlet
<dependency>
    <groupId>javax</groupId>
    <artifactId>javaee-api</artifactId>
    <version>8.0.1</version>
    <scope>provided</scope>
</dependency>
```

## DateTimeFormatter

```
<%=DateTimeFormatter.format((postDTOS.get(i).getTimestamp()))%>
```