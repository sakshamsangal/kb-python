# convert string[] to uppercase by spring batch

## pom

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-batch</artifactId>
</dependency>

<dependency>
    <groupId>com.h2database</groupId>
    <artifactId>h2</artifactId>
    <scope>runtime</scope>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

## property

```java
spring.batch.job.enabled=false
spring.main.banner-mode=off
# logging.level.root=ERROR
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

## MyReader

```java

public class MyReader implements ItemReader<String> {

    private String[] arr = {"saksham", "sahitya", "sakshi"};
    private int count = 0;

    @Override
    public String read() {
        if (count < arr.length) return arr[count++];
        return null;
    }
}
```

## MyWriter

```java

public class MyWriter implements ItemWriter<String> {

    @Override
    public void write(List<? extends String> list) throws Exception {

        System.out.println(list);
    }
}
```

## MyProcessor

```java

public class MyProcessor implements ItemProcessor<String, String> {


    @Override
    public String process(String s) {
        return s.toUpperCase();
    }
}
```

## MyJobExecutionListener

```java
public class MyJobExecutionListener implements JobExecutionListener {
    @Override
    public void beforeJob(JobExecution jobExecution) {
        System.out.println("beforeJob");
    }

    @Override
    public void afterJob(JobExecution jobExecution) {
        System.out.println("afterJob");
    }
}
```

## BatchConfig

```java
@Configuration
public class BatchConfig {


    private final StepBuilderFactory stepBuilderFactory;

    private final JobBuilderFactory jobBuilderFactory;

    @Autowired
    public BatchConfig(StepBuilderFactory stepBuilderFactory, JobBuilderFactory jobBuilderFactory) {
        this.stepBuilderFactory = stepBuilderFactory;
        this.jobBuilderFactory = jobBuilderFactory;
    }


    @Bean
    public Job myJob() {
        return jobBuilderFactory.get("j1")
                .incrementer(new RunIdIncrementer())
                .listener(myJobExecutionListener())
                .start(myStep())
                .build();
    }

    @Bean
    public Step myStep() {
        return stepBuilderFactory.get("s1")
                .<String, String>chunk(1)
                .reader(myReader())
                .processor(myProcessor())
                .writer(myWriter())
                .build();
    }


    @Bean
    public MyReader myReader() {
        return new MyReader();
    }

    @Bean
    public MyProcessor myProcessor() {
        return new MyProcessor();
    }

    @Bean
    public MyWriter myWriter() {
        return new MyWriter();
    }

    @Bean
    public MyJobExecutionListener myJobExecutionListener() {
        return new MyJobExecutionListener();
    }
}

```

## output

```
2020-12-27 21:32:29.841  INFO 3304 --- [           main] o.s.b.c.l.support.SimpleJobLauncher      : Job: [SimpleJob: [name=j1]] launched with the following parameters: [{time=1609084949733}]
beforeJob
2020-12-27 21:32:29.902  INFO 3304 --- [           main] o.s.batch.core.job.SimpleStepHandler     : Executing step: [s1]
[SAKSHAM]
[SAHITYA]
[SAKSHI]
2020-12-27 21:32:30.035  INFO 3304 --- [           main] o.s.batch.core.step.AbstractStep         : Step: [s1] executed in 131ms
afterJob
2020-12-27 21:32:30.040  INFO 3304 --- [           main] o.s.b.c.l.support.SimpleJobLauncher      : Job: [SimpleJob: [name=j1]] completed with the following parameters: [{time=1609084949733}] and the following status: [COMPLETED] in 166ms
```