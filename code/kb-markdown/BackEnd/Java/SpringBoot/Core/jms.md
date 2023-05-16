# print message from sender to reciver using jms

## requirements

```text
download active mq
activemq start 
activemq stop 
http://localhost:8161/index.html 
Manage ActiveMQ broker
```

## pom

```xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-activemq</artifactId>
</dependency>

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-test</artifactId>
    <scope>test</scope>
</dependency>
```

## property

```java
spring.jms.myQueue=myQueue
spring.main.banner-mode=off

spring.activemq.broker-url=tcp://localhost:61616
spring.activemq.user=admin
spring.activemq.password=admin

#spring.jms.pub-sub-domain=true
```

## main

```java
@SpringBootApplication
@EnableJms
public class JarApplication {

	public static void main(String[] args) {
		SpringApplication.run(JarApplication.class, args);
	}

}

```

## MessageSender

```java
@Component
public class MessageSender{
    private final JmsTemplate jmsTemplate;

    @Autowired
    public MessageSender(JmsTemplate jmsTemplate) {
        this.jmsTemplate = jmsTemplate;
    }

    @Value("${spring.jms.myQueue}")
    private String queue;

    public void mySend(String message) {
        // MessageCreator messageCreator = new MessageCreator() {
        //     @Override
        //     public Message createMessage(Session session) throws JMSException {
        //         return session.createTextMessage(message);
        //     }
        // };

        MessageCreator messageCreator = session -> session.createTextMessage(message);

        jmsTemplate.send(queue, messageCreator);


        // jmsTemplate.convertAndSend(queue, message);
    }
}

```

## MyListener

```java
@Component
public class MyListener {

    @JmsListener(destination = "${spring.jms.myQueue}")
    public void myReceive(String message) {
        System.out.println("myReceive() " + message);
    }
}
```

## test

```java
@SpringBootTest
class JarApplicationTests {

	@Autowired
	MessageSender messageSender;

	@Test
	void test1() {

		messageSender.mySend("hello ");
	}

}
```

## output

```
myReceive() hello 

```
