```

  <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-server</artifactId>
        </dependency>

```


```

<properties>
        <java.version>17</java.version>
        <spring-cloud.version>2022.0.0</spring-cloud.version>
    </properties>

```


```

@SpringBootApplication
@EnableEurekaServer
public class SerRegApplication {

    public static void main(String[] args) {
        SpringApplication.run(SerRegApplication.class, args);
    }

}


```


```

server.port=8761
eureka.client.register-with-eureka=false
eureka.client.fetch-registry=false
spring.application.name=EUREKA-SERVER



```


