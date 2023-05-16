## index.jsp

```
<%@ page import="com.saksham.Crud" %>
<%@ page import="com.saksham.Student" %>
<%@ page import="java.util.List" %>
<%@ page contentType="text/html;charset=UTF-8" language="java" %>
<html>
<header>
    <style>
        input, button {
            background-color: black;
            color: #c4c4c4;
        }

        body {
            margin: 50px auto;
            width: 60%;
            background-color: #222;
            color: #aaa;
        }
    </style>
</header>
<body>
<h2>Welcome to student management system!</h2>
<%
    Student student= (Student) request.getAttribute("student");
    String studentRollNumber = "";
    String studentName = "";
    if (student != null) {
        studentRollNumber = String.valueOf(student.getRollNumber());
        studentName = student.getStudentName();
    }
%>

<form action="/crud" method="post">
    <input value="<%=studentRollNumber%>" type="number" name="studentRollNumber" placeholder="studentRollNumber"><br><br>
    <input value="<%=studentName%>"  type="text" name="studentName" placeholder="studentName">
    <button name="save" value="save">Save</button>
    <button name="search" value="search">Search</button>
    <button name="edit" value="edit">Edit</button>
    <button name="delete" value="delete">Delete</button>
</form>
<table border="1">
    <tr>
        <th>Roll number</th>
        <th>Student name</th>
    </tr>
    <%
            List<Student> students = Crud.view();
            for (int i = 0; i < students.size(); i++) { %>
    <tr>
        <td><%=students.get(i).getRollNumber()%>
        </td>
        <td><%=students.get(i).getStudentName()%>
        </td>
    </tr>
    <%
            }
            if (students.size() < 1) {
                out.print("No records available");
            }
    %>
</table>
</body>
</html>

```

## StudentServlet.java

```
package com.saksham;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.sql.SQLException;

@WebServlet("/crud")
public class StudentServlet extends HttpServlet {
    @Override
    protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws ServletException, IOException {
        try {
            if (req.getParameter("save") != null) {
                int studentRollNumber = Integer.parseInt(req.getParameter("studentRollNumber"));
                String studentName = req.getParameter("studentName");
                Crud.insert(studentRollNumber, studentName);
            } else if (req.getParameter("search") != null) {

                int studentRollNumber = Integer.parseInt(req.getParameter("studentRollNumber"));
                Student student= Crud.search(studentRollNumber);
                req.setAttribute("student", student);

            } else if (req.getParameter("edit") != null) {
                int studentRollNumber = Integer.parseInt(req.getParameter("studentRollNumber"));
                String studentName = req.getParameter("studentName");
                Crud.update(studentRollNumber, studentName);
            } else if (req.getParameter("delete") != null) {
                int studentRollNumber = Integer.parseInt(req.getParameter("studentRollNumber"));
                Crud.delete(studentRollNumber);
            }
            req.getRequestDispatcher("index.jsp").forward(req, resp);
        } catch (SQLException e) {
            e.printStackTrace();
        }

    }
}

```

## Database.java

```
package com.saksham;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Database {
    public static Connection getConnection() {
        Connection connection = null;
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            String url = "jdbc:mysql://localhost:3306/school";
            String username = "root";
            String password = "root";
            connection = DriverManager.getConnection(url, username, password);
            System.out.println("database connection established");
        } catch (ClassNotFoundException e) {
            System.err.println("ClassNotFoundException: " + e.getMessage());
        } catch(SQLException e){
            System.err.println("SQLException: " + e.getMessage());
        }
        return connection;
    }
}
```

## Student.java

```

package com.saksham;

public class Student {
    private int rollNumber;
    private String studentName;

    public int getRollNumber() {
        return rollNumber;
    }

    public void setRollNumber(int rollNumber) {
        this.rollNumber = rollNumber;
    }

    public String getStudentName() {
        return studentName;
    }

    public void setStudentName(String studentName) {
        this.studentName = studentName;
    }

    @Override
    public String toString() {
        return "Student{" +
                "rollNumber=" + rollNumber +
                ", studentName='" + studentName + '\'' +
                '}';
    }
}
```

## Crud.java

```

package com.saksham;

import java.sql.ResultSet;
import java.sql.SQLException;
import java.sql.Statement;
import java.util.ArrayList;
import java.util.List;

public class Crud {

    public static Statement statement;

    public static void delete(int studentRollNumber) throws SQLException {
        String sql = "DELETE FROM student WHERE student_roll_number = " + studentRollNumber;
        statement.executeUpdate(sql);
    }

    public static void insert(long studentRollNumber, String studentName) throws SQLException {
        String sql = "INSERT INTO student VALUES (" + studentRollNumber + ", '" + studentName + "')";
        statement.executeUpdate(sql);
    }

    public static void update(int studentRollNumber, String studentName) throws SQLException {
        String sql = "UPDATE student SET student_name = '" + studentName + "' " + " WHERE student_roll_number = " + studentRollNumber;
        statement.executeUpdate(sql);
    }

    public static Student search(int studentRollNumber) throws SQLException {
        String sql = "SELECT * FROM student WHERE student_roll_number = " + studentRollNumber;
        ResultSet resultSet = statement.executeQuery(sql);

        Student student = new Student();
        if (resultSet.next()) {
            student.setRollNumber(resultSet.getInt(1));
            student.setStudentName(resultSet.getString(2));
        }
        return student;
    }

    public static List<Student> view() throws Exception {
        String sql = "SELECT * FROM student";
        ResultSet resultSet = statement.executeQuery(sql);

        List<Student> students = new ArrayList<>();
        while (resultSet.next()) {
            Student student = new Student();
            student.setRollNumber(resultSet.getInt(1));
            student.setStudentName(resultSet.getString(2));
            students.add(student);
        }
        return students;
    }

    static {
        try {
            Crud.statement = Database.getConnection().createStatement();
        } catch (SQLException e) {
            System.err.println(e.getMessage());
        }
    }

}
```

## pom.xml

```
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
  xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
  <modelVersion>4.0.0</modelVersion>

  <groupId>org.example</groupId>
  <artifactId>JustToLearn2</artifactId>
  <version>1.0-SNAPSHOT</version>
  <packaging>war</packaging>

  <name>JustToLearn2 Maven Webapp</name>
  <!-- FIXME change it to the project's website -->
  <url>http://www.example.com</url>

  <properties>
    <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    <maven.compiler.source>1.7</maven.compiler.source>
    <maven.compiler.target>1.7</maven.compiler.target>
  </properties>

  <dependencies>
    <dependency>
      <groupId>mysql</groupId>
      <artifactId>mysql-connector-java</artifactId>
      <version>8.0.13</version>
    </dependency>
    <dependency>
      <groupId>javax</groupId>
      <artifactId>javaee-api</artifactId>
      <version>8.0.1</version>
      <scope>provided</scope>
    </dependency>
  </dependencies>

  <build>
    <finalName>JustToLearn2</finalName>
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
          <groupId>org.apache.tomcat.maven</groupId>
          <artifactId>tomcat7-maven-plugin</artifactId>
          <version>2.2</version>
          <configuration>
            <port>8080</port>
            <path>/</path>
          </configuration>
        </plugin>
      </plugins>
    </pluginManagement>
  </build>
</project>

```

## run

```
tomcat7:run
```