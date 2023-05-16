# CSV to MySQL

## sql

```sql
create database mydb;
use mydb;

create table product(
id int auto_increment PRIMARY KEY,
name varchar(20),
description varchar(100),
price decimal(8,3)
);

select * from product;
```

## pom

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-batch</artifactId>
</dependency>

<dependency>
    <groupId>mysql</groupId>
    <artifactId>mysql-connector-java</artifactId>
    <scope>runtime</scope>
</dependency>
```

## property

```java
spring.batch.job.enabled=false
spring.main.banner-mode=off
#logging.level.root=ERROR

spring.batch.initialize-schema=ALWAYS
```

## Main

```java
@SpringBootApplication
@EnableBatchProcessing
public class JarApplication {

	public static void main(String[] args) {
		SpringApplication.run(JarApplication.class, args);
	}

}
```

## Test

```java
@SpringBootTest
class JarApplicationTests {

	@Autowired
	JobLauncher jobLauncher;

	@Autowired
	Job job;

	@Test
	void test1() throws Exception {
		JobParameters jobParameters = new JobParametersBuilder().addLong("time", System.currentTimeMillis())
				.toJobParameters();

		jobLauncher.run(job, jobParameters);
	}
}
```

## BatchConfig

```java
@Configuration
public class BatchConfig{

    final StepBuilderFactory stepBuilderFactory;

    final JobBuilderFactory jobBuilderFactory;

    public BatchConfig(@Lazy StepBuilderFactory stepBuilderFactory,@Lazy JobBuilderFactory jobBuilderFactory) {
        this.stepBuilderFactory = stepBuilderFactory;
        this.jobBuilderFactory = jobBuilderFactory;
    }


    @Bean
    public Job myJob() {
        return jobBuilderFactory.get("j1")
                .incrementer(new RunIdIncrementer())
                .start(myStep())
                .build();
    }

    @Bean
    public Step myStep() {
        return stepBuilderFactory.get("s1")
                .<Product, Product>chunk(1)
                .reader(productItemReader())
                .processor(productItemProcessor())
                .writer(productItemWriter())
                .build();
    }

    @Bean
    public ItemReader<Product> productItemReader() {
        FlatFileItemReader<Product> productFlatFileItemReader = new FlatFileItemReader<>();
        productFlatFileItemReader.setResource(new ClassPathResource("products.csv"));

        DefaultLineMapper<Product> productDefaultLineMapper = new DefaultLineMapper<>();
        DelimitedLineTokenizer delimitedLineTokenizer = new DelimitedLineTokenizer();

        delimitedLineTokenizer.setNames("id", "name", "description", "price");
        BeanWrapperFieldSetMapper<Product> productBeanWrapperFieldSetMapper = new BeanWrapperFieldSetMapper<>();
        productBeanWrapperFieldSetMapper.setTargetType(Product.class);

        productDefaultLineMapper.setLineTokenizer(delimitedLineTokenizer);
        productDefaultLineMapper.setFieldSetMapper(productBeanWrapperFieldSetMapper);

        productFlatFileItemReader.setLineMapper(productDefaultLineMapper);

        return productFlatFileItemReader;
    }


    @Bean
    public ItemProcessor<Product, Product> productItemProcessor() {
        return (product) -> {
            product.setPrice(0.90 * product.getPrice());
            return product;
        };
    }

    @Bean
    public ItemWriter<Product> productItemWriter(){
        JdbcBatchItemWriter<Product> productJdbcBatchItemWriter = new JdbcBatchItemWriter<>();
        productJdbcBatchItemWriter.setDataSource(dataSource());
        productJdbcBatchItemWriter.setItemSqlParameterSourceProvider(new BeanPropertyItemSqlParameterSourceProvider<>());
        productJdbcBatchItemWriter.setSql("INSERT INTO product(id,name,description,price) VALUES(:id,:name,:description,:price)");
        return  productJdbcBatchItemWriter;
    }

    @Bean
    public DataSource dataSource() {
        DriverManagerDataSource driverManagerDataSource = new DriverManagerDataSource();
        driverManagerDataSource.setDriverClassName("com.mysql.cj.jdbc.Driver");
        driverManagerDataSource.setUrl("jdbc:mysql://localhost:3306/mydb");
        driverManagerDataSource.setUsername("root");
        driverManagerDataSource.setPassword("root");
        return driverManagerDataSource;
    }

}

```

## Pojo

```java
public class Product{
    private int id;
    private String name;
    private String description;
    private double price;

    @Override
    public String toString() {
        return "Product{" +
                "id=" + id +
                ", name='" + name + '\'' +
                ", description='" + description + '\'' +
                ", price=" + price +
                '}';
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public String getDescription() {
        return description;
    }

    public void setDescription(String description) {
        this.description = description;
    }

    public double getPrice() {
        return price;
    }

    public void setPrice(double price) {
        this.price = price;
    }
}

```

## csv

```csv
main/resources/products.csv
10,pen,awesome,100
20,pencil,poor,200
30,cat,good,300
40,dog,nice,400
```

## Output

```text 
// in the database
SELECT * FROM mydb.product;

10	pen	awesome	90.000
20	pencil	poor	180.000
30	cat	good	270.000
40	dog	nice	360.000
```			