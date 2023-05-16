```

demo2

```


```

 <properties>
        <java.version>17</java.version>
        <spring-cloud.version>2022.0.0</spring-cloud.version>
    </properties>

```


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

   <!-- for crud operations-->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-data-jpa</artifactId>
        </dependency>

        <!-- for mysql connection-->
        <dependency>
            <groupId>mysql</groupId>
            <artifactId>mysql-connector-java</artifactId>
            <scope>runtime</scope>
        </dependency>

```


```

# database connection
spring.datasource.url=jdbc:mysql://localhost:3306/mydb
spring.datasource.username=root
spring.datasource.password=root

spring.jpa.hibernate.ddl-auto=update
spring.main.banner-mode=off
#logging.level.root=ERROR


spring.application.name=INVOICE-SERVICE

server.port=8080
eureka.client.register-with-eureka=true
eureka.client.fetch-registry=true
eureka.client.service-url.defaultZone=http://localhost:8761/eureka/
eureka.instance.hostname=localhost



```


```

import com.example.war.model.Invoice;
import org.springframework.data.jpa.repository.JpaRepository;

public interface InvoiceRepository extends JpaRepository<Invoice, Integer> {

}


```


```

@Entity
public class Invoice {
	@Id
	@GeneratedValue(strategy = GenerationType.IDENTITY)
	private int invoice_no;
	private String ship_add;
	private String prod_name;
	private double price;

```


```

    @Autowired
    public InvoiceRestController(InvoiceRepository invoiceRepository, RestTemplate restTemplate) {
        this.invoiceRepository = invoiceRepository;
        this.restTemplate = restTemplate;
    }



```


```

@CrossOrigin(origins = "*")
@RestController
public class InvoiceRestController {
    private final InvoiceRepository invoiceRepository;
    private final RestTemplate restTemplate;


```


```

    @PostMapping("/invoice")
    public Invoice postProduct(@RequestBody Invoice invoice) {
        System.out.println("hello");
        Object p = restTemplate.getForObject("http://PRODUCT-SERVICE/prod", Object.class);
        System.out.println(p);
        return invoiceRepository.save(invoice);
    }


```



```

@SpringBootApplication
@EnableDiscoveryClient
public class WarApplication {
	public static void main(String[] args) {
		SpringApplication.run(WarApplication.class, args);
	}

	@Bean
	@LoadBalanced
	public RestTemplate restTemplate(){
		return new RestTemplate();
	}
}

```
