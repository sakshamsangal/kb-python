```java
package com.example.demo.config;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.web.client.RestTemplate;

@Configuration
public class BeanConfig {
    @Bean
    public RestTemplate restTemplate() {
        return new RestTemplate();
    }
}


package com.example.demo.util;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.http.*;
import org.springframework.stereotype.Component;
import org.springframework.util.LinkedMultiValueMap;
import org.springframework.util.MultiValueMap;
import org.springframework.web.client.RestTemplate;

@Component
@Slf4j
@RequiredArgsConstructor
public class ConsumeUser {

    @Value("${endpoint.user}")
    private String userEndpoint;
    private final RestTemplate restTemplate;


    public void user() {
        // set headers
        HttpHeaders headers = new HttpHeaders();
        headers.setContentType(MediaType.APPLICATION_FORM_URLENCODED);
        headers.add("Authorization", "Bearer 623c0324-4395-3769-a8b9-49d3c8be91e9");

        // set the payload
        MultiValueMap<String, String> map = new LinkedMultiValueMap<>();
        map.add("title", "john");
        map.add("body", "body test");

        HttpEntity<MultiValueMap<String, String>> entity = new HttpEntity<>(map, headers);
        log.info(String.valueOf(entity));

        // String userEndpoint = "https://jsonplaceholder.typicode.com/posts/2";

        ResponseEntity<String> response = restTemplate.exchange(userEndpoint, HttpMethod.POST, entity, String.class);
        log.info(String.valueOf(response));
    }

}

```