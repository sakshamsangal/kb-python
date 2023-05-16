
## Spring Boot application.properties value not populating
- The way you are performing the injection of the property will not work,
- because the injection is done after the constructor is called.
```java
@Slf4j
@AllArgsConstructor
public class ConsumeUser {

    @Value("${endpoint.user}")
    private String userEndpoint;
```