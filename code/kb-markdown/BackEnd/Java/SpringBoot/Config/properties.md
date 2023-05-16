## database connection

```
# database connection
spring.datasource.url=jdbc:mysql://localhost:3306/projectdb
spring.datasource.username=root
spring.datasource.password=root
```

## show sql query on console

```
spring.jpa.show-sql=true
```

## set prefix and suffix for view resolve

```
spring.mvc.view.prefix=/WEB-INF/view/
spring.mvc.view.suffix=.jsp
```

## make root = error and banner = off

```
spring.main.banner-mode=off
logging.level.root=ERROR
```

