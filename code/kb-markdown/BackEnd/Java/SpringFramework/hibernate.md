## Product

```
@Entity
Product
    @Id
    int id;
    String name;
    String description;
    double price;
```

## ProductDao

``` java
public interface ProductDao {
    int insert(Product product);
    void update(Product product);
    void delete(Product product);
    Product select(int id);
    List<Product> selectAll();
}
```

## ProductDaoImpl

``` java
@Component
public class ProductDaoImpl implements ProductDao {

    @Autowired
    HibernateTemplate hibernateTemplate;

    @Override
    @Transactional
    public int insert(Product product) {
        Serializable save = hibernateTemplate.save(product);
        return (int) save;
    }

    @Override
    @Transactional
    public void update(Product product) {
        hibernateTemplate.update(product);
    }

    @Override
    @Transactional
    public void delete(Product product) {
        hibernateTemplate.delete(product);
    }

    @Override
    public Product select(int id) {
        Product product = hibernateTemplate.get(Product.class, id);
        return product;
    }

    @Override
    public List<Product> selectAll() {
        List<Product> products = hibernateTemplate.loadAll(Product.class);
        return products;
    }
}
```

## ProductDriver

``` java
public class ProductDriver {
    public static void main(String[] args) {
        ApplicationContext applicationContext = new ClassPathXmlApplicationContext("config.xml");
        ProductDao productDao = (ProductDao) applicationContext.getBean("productDaoImpl");
        Product product = new Product();
        product.setId(2);
        product.setName("asus");
        product.setDescription("nice");
        product.setPrice(15.23);
//        Product select = productDao.select(1);
//        System.out.println(select);
        List<Product> products = productDao.selectAll();
        System.out.println(products);

    }
}
``` 

## Database

use springHibernateTemplate;

create table product(id int primary key,name varchar(20),description varchar(100),price decimal(8,3));

select * from product;

## pom.xml

``` xml
<?xml version="1.0" encoding="UTF-8"?>

<project xmlns="http://maven.apache.org/POM/4.0.0" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>org.example</groupId>
    <artifactId>spring-orm</artifactId>
    <version>1.0-SNAPSHOT</version>
    <packaging>war</packaging>

    <name>spring-orm Maven Webapp</name>
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
            <artifactId>spring-orm</artifactId>
            <version>${springframework.version}</version>
        </dependency>
        <dependency>
            <groupId>org.hibernate</groupId>
            <artifactId>hibernate-core</artifactId>
            <version>5.2.5.Final</version>
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

## config.xml

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

    <context:component-scan base-package="daoimpl"/>

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
                <value>pojo.Product</value>
                <value>pojo.Passenger</value>
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


</beans>
```