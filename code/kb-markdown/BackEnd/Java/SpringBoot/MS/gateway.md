```

 <properties>
        <java.version>17</java.version>
        <spring-cloud.version>2022.0.0</spring-cloud.version>
    </properties>

```


```

<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-actuator</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-gateway</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.cloud</groupId>
    <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
</dependency>

```


```

spring:
  cloud:
    gateway:
      default-filters:
        - DedupeResponseHeader=Access-Control-Allow-Credentials Access-Control-Allow-Origin
      globalcors:
          corsConfigurations:
            '[/**]':
              allowedOrigins: "*"
              allowedMethods: "*"
              allowedHeaders: "*"

```


```

server.port=9090
spring.application.name=API-GATEWAY
eureka.instance.client.serviceUrl.defaultZone=http://localhost:8761/eureka/
management.endpoints.web.exposure.include=*

spring.cloud.gateway.routes[0].id=PRODUCT-SERVICE
spring.cloud.gateway.routes[0].uri=lb://PRODUCT-SERVICE
spring.cloud.gateway.routes[0].predicates[0]=Path=/prod

spring.cloud.gateway.routes[1].id=INVOICE-SERVICE
spring.cloud.gateway.routes[1].uri=lb://INVOICE-SERVICE
spring.cloud.gateway.routes[1].predicates[0]=Path=/invoice



```


```

@SpringBootApplication
@EnableDiscoveryClient
public class ApiGatewayApplication {

    public static void main(String[] args) {
        SpringApplication.run(ApiGatewayApplication.class, args);
    }

}


```


