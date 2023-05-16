```

 <dependency>
            <groupId>org.springframework.cloud</groupId>
            <artifactId>spring-cloud-starter-netflix-eureka-client</artifactId>
        </dependency>
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
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
@EnableDiscoveryClient
public class ProductApplication {

    public static void main(String[] args) {
        SpringApplication.run(ProductApplication.class, args);
    }

}


```


```

@CrossOrigin(origins = "*")
@RestController
public class ProductRestController {

    @GetMapping("/prod")
    public Object postProduct() {
        Map<String, String> map = new HashMap<>();
        map.put("name", "akshu");
        map.put("gender", "female");
        return map;
    }


}


```


```

server.port=8081

spring.application.name=PRODUCT-SERVICE

eureka.client.register-with-eureka=true
eureka.client.fetch-registry=true
eureka.client.service-url.defaultZone=http://localhost:8761/eureka/
eureka.instance.hostname=localhost



```


