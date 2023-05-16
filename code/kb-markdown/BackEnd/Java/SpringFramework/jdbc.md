# Spring JDBC

``` java
public class EmployeeDriver {
    public static void main(String[] args) {
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("config.xml");
        EmployeeDao employeeDao = (EmployeeDao) applicationContext.getBean("employeeDaoImpl");
        Employee employee = new Employee();
        employee.setId(1);
        employee.setFirstName("caring mummy");
        employee.setLastName("sangal");
        List<Employee> employeeList = employeeDao.selectAll();
        System.out.println(employeeList);
    }
}



public class EmployeeRowMapper implements RowMapper {
    @Override
    public Employee mapRow(ResultSet rs, int rowNum) throws SQLException {
        Employee employee = new Employee();
        employee.setId(rs.getInt(1));
        employee.setFirstName(rs.getString(2));
        employee.setLastName(rs.getString(3));
        return employee;
    }
}


@Component
public class EmployeeDaoImpl implements EmployeeDao {

    @Autowired
    private JdbcTemplate jdbcTemplate;

    public JdbcTemplate getJdbcTemplate() {
        return jdbcTemplate;
    }

    public void setJdbcTemplate(JdbcTemplate jdbcTemplate) {
        this.jdbcTemplate = jdbcTemplate;
    }

    @Override
    public int insert(Employee employee) {
        String sql = "insert into employee values(?, ?, ?)";
        int result = jdbcTemplate.update(sql, employee.getId(), employee.getFirstName(), employee.getLastName());
        return result;
    }

    @Override
    public int update(Employee employee) {
        String sql = "update employee set firstName=?, lastName=? where id=?";
        int result = jdbcTemplate.update(sql, employee.getFirstName(), employee.getLastName(), employee.getId());
        return result;
    }

    @Override
    public int delete(int id) {
        String sql = "delete from employee where id=?";
        int result = jdbcTemplate.update(sql, id);
        return result;
    }

    @Override
    public Employee select(int id) {
        String sql = "select * from employee where id=?";
        EmployeeRowMapper employeeRowMapper = new EmployeeRowMapper();
        Employee employee = (Employee) jdbcTemplate.queryForObject(sql, employeeRowMapper, id);
        return employee;
    }

    @Override
    public List<Employee> selectAll() {
        String sql = "select * from employee";
        EmployeeRowMapper employeeRowMapper = new EmployeeRowMapper();
        List<Employee> employeeList= (List<Employee>) jdbcTemplate.query(sql, employeeRowMapper);
        return employeeList;
    }
}



public interface EmployeeDao {
    int insert(Employee employee);
    int update(Employee employee);
    int delete(int id);
    Employee select(int id);
    List<Employee> selectAll();
}
```

```
Employee 
    int id;
    String firstName;
    String lastName;
```

## Database

use mydb;

create table passenger(id int,firstname varchar(20),lastname varchar(20));

select * from passenger;

drop table passanger;

``` xml
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.saksham</groupId>
    <artifactId>spring-jdbc-template</artifactId>
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
            <artifactId>spring-core</artifactId>
            <version>${springframework.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-context</artifactId>
            <version>${springframework.version}</version>
        </dependency>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-jdbc</artifactId>
            <version>${springframework.version}</version>
        </dependency>
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <version>8.0.13</version>
        </dependency>
    </dependencies>
    <build>
        <pluginManagement>
            <plugins>
                <plugin>
                    <groupId>org.apache.maven.plugins</groupId>
                    <artifactId>maven-compiler-plugin</artifactId>
                    <version>3.2</version>
                    <configuration>
                        <source>1.8</source>
                        <target>1.8</target>
                    </configuration>
                </plugin>
            </plugins>
        </pluginManagement>
    </build>
</project>
```

``` xml
<?xml version="1.0" encoding="UTF-8"?>
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xmlns:context="http://www.springframework.org/schema/context"
       xmlns:p="http://www.springframework.org/schema/p"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
    http://www.springframework.org/schema/beans/spring-beans.xsd
    http://www.springframework.org/schema/context
    http://www.springframework.org/schema/context/spring-context.xsd">

    <context:component-scan base-package="daoImpl" />
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

    <bean class="org.springframework.jdbc.core.JdbcTemplate" name="jdbcTemplate">
        <property name="dataSource">
            <ref bean="dataSource" />
        </property>
    </bean>

<!--    <bean class="daoImpl.EmployeeDaoImpl" name="employeeDaoImpl">-->
<!--        <property name="jdbcTemplate">-->
<!--            <ref bean="jdbcTemplate" />-->
<!--        </property>-->
<!--    </bean>-->


</beans>
```
