```yml
#logging:
#  level:
#    root: INFO
#    tests: INFO
server:
  port: 8080
spring:
  datasource:
    password: root
    url: jdbc:mysql://localhost:3306/mydb
    username: root
  jpa:
    hibernate:
      ddl-auto: update

endpoint:
  token: https://jsonplaceholder.typicode.com/posts

#upload:
#  dir: D:/Temporary/upload

```