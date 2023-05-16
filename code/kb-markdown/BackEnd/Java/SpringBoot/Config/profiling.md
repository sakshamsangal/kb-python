# profiling

used to switch among properties file

`src/main/resources/application.properties`

## switch by application.properties

```
application-dev.properties

application-test.properties

application.properties
    spring.profiles.active=dev // active properties file 
```

## switch by VM arguments

```
delete spring.profiles.active=dev

VM arguments:
-Dspring.profiles.active=dev
```