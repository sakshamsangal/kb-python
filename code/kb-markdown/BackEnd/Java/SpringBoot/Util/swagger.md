# swagger

## pom

```xml
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger2</artifactId>
    <version>2.9.2</version>
</dependency>
<dependency>
    <groupId>io.springfox</groupId>
    <artifactId>springfox-swagger-ui</artifactId>
    <version>2.9.2</version>
</dependency>
```


## url

```text
http://localhost:8080/swagger-ui.html
http://localhost:8080/v2/api-docs
```

## SwaggerConfig

```java 

@Configuration
public class SwaggerConfig {
    @Bean
    public Docket api() {
        return new Docket(DocumentationType.SWAGGER_2).apiInfo(apiInfo())
                .select()
                .apis(RequestHandlerSelectors.basePackage("com.example.war.entity"))
                .paths(PathSelectors.regex("/products.*"))
                .build();
    }

    @Bean
    public ApiInfo apiInfo() {
        return new ApiInfoBuilder().title("Product API")
                .description("Product crud operations")
                .termsOfServiceUrl("open source")
                .license("Saksham license")
                .licenseUrl("www.google.com")
                .version("2.0")
                .build();
    }
}

```

## ApiOperation

```java 
@ApiOperation(value = "get all products provided by saksham",
        notes = "hello",
        response = Product.class,
        responseContainer = "List",
        produces = "application/json"

)
@GetMapping("/products")
public List<Product> getProducts() {
    return productRepository.findAll();
}
```

## Main

```java 
@SpringBootApplication
@EnableSwagger2
public class WarApplication {

	public static void main(String[] args) {
		SpringApplication.run(WarApplication.class, args);
	}

}
```
