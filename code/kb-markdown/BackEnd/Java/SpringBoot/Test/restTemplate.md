```java
@SpringBootTest
class WarApplicationTests {

	@Test
	void test1() {
		RestTemplate restTemplate = new RestTemplate();
		String url = "http://localhost:8080/products/30";
		Product product = restTemplate.getForObject(url, Product.class);
		assertNotNull(product);
		assertEquals("dog",product.getName());
	}

}

```

## output

```
org.opentest4j.AssertionFailedError: 
Expected :dog
Actual   :cat
```

```java
@Test
void testPost() {
    RestTemplate restTemplate = new RestTemplate();
    String url = "http://localhost:8080/products/";
    Product product = new Product();
    product.setId(50);
    product.setName("saksham");
    product.setDescription("hello");
    product.setPrice(500d);
    Product savedProduct = restTemplate.postForObject(url, product, Product.class);

    assertNotNull(savedProduct);
    assertEquals("saksham",savedProduct.getName());
}

@Test
void testPut() {
    RestTemplate restTemplate = new RestTemplate();
    String url = "http://localhost:8080/products/30";
    Product product = restTemplate.getForObject(url, Product.class);
    assert product != null;
    product.setPrice(600d);
    restTemplate.put("http://localhost:8080/products", product);
}
```