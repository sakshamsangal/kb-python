## string to file object
```java

this.byteArrayResource = new ByteArrayResource(xmlString.getBytes()) {
            @Override
            public String getFilename() {
                return "temp.xml";
            }
        };
        new StreamSource(byteArrayResource.getInputStream());
```

```java

[
    {
        "id": 1,
        "name": "lavi",
        "description": null,
        "price": 0.0
    },
    {
        "id": 2,
        "name": "akshu",
        "description": null,
        "price": 0.0
    }
]
```

```java
String message = "{0} has to go to {1} in {2,date,dd/MM/yyyy} / {3}";
String formattedMessage = MessageFormat.format(message, "Richard", "School", new Date(), "1days");
System.out.println(formattedMessage);
```

## xml to pojo
```java
package org.example;
import com.fasterxml.jackson.databind.SerializationFeature;
import com.fasterxml.jackson.dataformat.xml.*;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlProperty;
import com.fasterxml.jackson.dataformat.xml.annotation.JacksonXmlRootElement;

import javax.xml.bind.annotation.XmlAttribute;
import java.io.BufferedWriter;
import java.io.File;
import java.io.FileWriter;

public class POJOToXmlTest {
    public static void main(String args[]) throws Exception {
        try {
            Person pojo = new Person();

            XmlMapper xmlMapper = new XmlMapper();
            xmlMapper.enable(SerializationFeature.INDENT_OUTPUT);
            String str = "Helwewewelo jhguhg\n";
            BufferedWriter writer = new BufferedWriter(new FileWriter("simple_bean.xml"));
            writer.write(str);
            xmlMapper.writeValue(writer, pojo);
            writer.close();



        } catch(Exception e) {
            e.printStackTrace();
        }
    }
}
// Person clas
//
@JacksonXmlRootElement( localName = "PersonData")
class Person {

    @JacksonXmlProperty(isAttribute = true)
    private final String xmlns = "urn:stackify:jacksonxml";

    @JacksonXmlProperty(isAttribute = true)
    private final String xmlns2 = "akshu2";

    @JacksonXmlProperty(localName="cc:myFN")
    private String firstName;

    @JacksonXmlProperty(localName = "cc:urn")
    private String lastName;

    @JacksonXmlProperty(isAttribute = true, localName = "_id")
    private String address;

    public void setFirstName(String firstName) {
        this.firstName = firstName;
    }

    public void setLastName(String lastName) {
        this.lastName = lastName;
    }

    public void setAddress(String address) {
        this.address = address;
    }
}
```

	
	
	
## xml validation
```java
package org.example;

import java.io.File;
import java.io.IOException;

import javax.xml.XMLConstants;
import javax.xml.transform.stream.StreamSource;
import javax.xml.validation.Schema;
import javax.xml.validation.SchemaFactory;
import javax.xml.validation.Validator;

import org.xml.sax.SAXException;

public class XMLValidation {

    public static void main(String[] args) {
        System.out.println(validateXMLSchema("src/main/java/org/example/person.xsd", "src/main/java/org/example/test.xml"));
    }
    public static boolean validateXMLSchema(String xsdPath, String xmlPath) {

        try {
            SchemaFactory factory =
                    SchemaFactory.newInstance(XMLConstants.W3C_XML_SCHEMA_NS_URI);
            Schema schema = factory.newSchema(new File(xsdPath));
            Validator validator = schema.newValidator();
            validator.validate(new StreamSource(new File(xmlPath)));
        } catch (IOException | SAXException e) {
            System.out.println("Exception: " + e.getMessage());
            return false;
        }
        return true;
    }
}

package org.example;

import javax.xml.bind.annotation.*;

@XmlRootElement(name = "Student")
@XmlAccessorType(XmlAccessType.FIELD)
class Student {

    @XmlAttribute
    private String type;

    @XmlElement(name="Name")
    private String name;

    public void setType(String type) {
        this.type = type;
    }

    public void setName(String name) {
        this.name = name;
    }
}
```
		
## jwt
```java
package com.example.jwt;

import jakarta.servlet.FilterChain;
import jakarta.servlet.ServletException;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.authentication.AuthenticationManager;
import org.springframework.security.authentication.UsernamePasswordAuthenticationToken;
import org.springframework.security.config.annotation.authentication.configuration.AuthenticationConfiguration;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.config.annotation.web.configuration.EnableWebSecurity;
import org.springframework.security.config.http.SessionCreationPolicy;
import org.springframework.security.core.context.SecurityContextHolder;
import org.springframework.security.core.userdetails.User;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.security.core.userdetails.UserDetailsService;
import org.springframework.security.core.userdetails.UsernameNotFoundException;
import org.springframework.security.crypto.password.NoOpPasswordEncoder;
import org.springframework.security.crypto.password.PasswordEncoder;
import org.springframework.security.web.SecurityFilterChain;
import org.springframework.security.web.authentication.UsernamePasswordAuthenticationFilter;
import org.springframework.security.web.authentication.WebAuthenticationDetailsSource;
import org.springframework.stereotype.Component;
import org.springframework.stereotype.Service;
import org.springframework.web.bind.annotation.*;
import org.springframework.web.filter.OncePerRequestFilter;

import java.io.IOException;
import java.util.ArrayList;

@RestController
public class MyController {
    @GetMapping("/")
    public String welcome() {
        return "welcome";
    }

    @Autowired
    private JwtUtil jwtUtil;


    @Autowired
    private CustomUserDetailService customUserDetailService;

    @Autowired
    private AuthenticationManager authenticationManager;


    @PostMapping("/token")
    public String getToken(@RequestBody JWTRequest jwtRequest) throws Exception {
        try {
            System.out.println(jwtRequest);
            authenticationManager.authenticate(new UsernamePasswordAuthenticationToken(jwtRequest.getUsername(), jwtRequest.getPassword()));
        } catch (Exception e){
            e.printStackTrace();
            throw new Exception("bad credentials");
        }

        UserDetails userDetail = customUserDetailService.loadUserByUsername(jwtRequest.getUsername());
        return jwtUtil.generateToken(userDetail);
    }
}


@Configuration
@EnableWebSecurity
class SecurityConfig {
    @Autowired
    private JwtFilter jwtFilter;

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http.csrf()
                .disable()
                .cors()
                .disable()
                .authorizeHttpRequests()
                .requestMatchers("/token").permitAll()
                .anyRequest().authenticated()
                .and().sessionManagement().sessionCreationPolicy(SessionCreationPolicy.STATELESS);

                http.addFilterAfter(jwtFilter, UsernamePasswordAuthenticationFilter.class);
        return http.build();
    }

    @Bean
    public AuthenticationManager authenticationManager(AuthenticationConfiguration authenticationConfiguration) throws Exception {
        return authenticationConfiguration.getAuthenticationManager();
    }

    @Bean
    public PasswordEncoder passwordEncoder(){
        return NoOpPasswordEncoder.getInstance();
    }

}


@Service
class CustomUserDetailService implements UserDetailsService {

    @Override
    public UserDetails loadUserByUsername(String username) throws UsernameNotFoundException {
        if (username.equals("sak")) {
            return new User("sak", "123", new ArrayList<>());
        } else {
            throw new UsernameNotFoundException("User name not found");
        }
    }
}

class JWTRequest {
    private String username;
    private String password;

    @Override
    public String toString() {
        return "JWTRequest{" +
                "username='" + username + '\'' +
                ", password='" + password + '\'' +
                '}';
    }

    public String getUsername() {
        return username;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public String getPassword() {
        return password;
    }

    public void setPassword(String password) {
        this.password = password;
    }
}

@Component
class JwtFilter extends OncePerRequestFilter {

    @Autowired
    private JwtUtil jwtUtil;

    @Autowired
    private CustomUserDetailService customUserDetailService;

    @Override
    protected void doFilterInternal(HttpServletRequest request, HttpServletResponse response, FilterChain filterChain) throws ServletException, IOException {
        String header = request.getHeader("Authorization");
        if (header != null && header.startsWith("Bearer ")){
            String token = header.substring(7);
            String username = "";
            try {
                username = jwtUtil.extractUsername(token);
            } catch (Exception e){
                e.printStackTrace();
            }
            UserDetails userDetails = customUserDetailService.loadUserByUsername(username);
            if (SecurityContextHolder.getContext().getAuthentication() == null){
                UsernamePasswordAuthenticationToken tok = new UsernamePasswordAuthenticationToken(userDetails, null, userDetails.getAuthorities());
                tok.setDetails(new WebAuthenticationDetailsSource().buildDetails(request));
                SecurityContextHolder.getContext().setAuthentication(tok);
            }
        }
        filterChain.doFilter(request,response);
    }


}

package com.example.jwt;

import io.jsonwebtoken.Claims;
import io.jsonwebtoken.Jwts;
import io.jsonwebtoken.SignatureAlgorithm;
import org.springframework.security.core.userdetails.UserDetails;
import org.springframework.stereotype.Service;

import java.util.Date;
import java.util.HashMap;
import java.util.Map;
import java.util.function.Function;

@Service
public class JwtUtil {

    private String SECRET_KEY = "secret";

    public String extractUsername(String token) {
        return extractClaim(token, Claims::getSubject);
    }

    public Date extractExpiration(String token) {
        return extractClaim(token, Claims::getExpiration);
    }

    public <T> T extractClaim(String token, Function<Claims, T> claimsResolver) {
        final Claims claims = extractAllClaims(token);
        return claimsResolver.apply(claims);
    }
    private Claims extractAllClaims(String token) {
        return Jwts.parser().setSigningKey(SECRET_KEY).parseClaimsJws(token).getBody();
    }

    private Boolean isTokenExpired(String token) {
        return extractExpiration(token).before(new Date());
    }

    public String generateToken(UserDetails userDetails) {
        Map<String, Object> claims = new HashMap<>();
        return createToken(claims, userDetails.getUsername());
    }

    private String createToken(Map<String, Object> claims, String subject) {

        return Jwts.builder().setClaims(claims).setSubject(subject).setIssuedAt(new Date(System.currentTimeMillis()))
                .setExpiration(new Date(System.currentTimeMillis() + 1000 * 60 * 60 * 10))
                .signWith(SignatureAlgorithm.HS256, SECRET_KEY).compact();
    }

    public Boolean validateToken(String token, UserDetails userDetails) {
        final String username = extractUsername(token);
        return (username.equals(userDetails.getUsername()) && !isTokenExpired(token));
    }
}

```