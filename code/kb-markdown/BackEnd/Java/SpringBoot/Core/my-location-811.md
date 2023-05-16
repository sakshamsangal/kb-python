my-[Entity]-811
// download with no dependency

// test the code
run hello world

## create insert view

```
create bootstrap starter
insert form accordingly
```

```
there is no webapp support in jar packaging
for webapp support packaging should be war

main
    webapp
        WEB-INF
            insert[Entity]View.jsp
```

## controller

```
[Entity]Controller
    send insert[Entity]View.jsp view 
    insert data and send view with [Entity] object
```

## my-[Entity]-811.iml

```
<configuration>
    <webroots>
        <root url="file://$MODULE_DIR$/src/main/webapp" relative="/" />
    </webroots>
    <sourceRoots>
        <root url="file://$MODULE_DIR$/src/main/java" />
        <root url="file://$MODULE_DIR$/src/main/resources" />
    </sourceRoots>
</configuration>
```

## send insert[Entity]View.jsp view

return view

## insert data and send view with [Entity] object

```
transfer data from UI to java object 
get the service object using autowire by constructor injection
pass the [Entity] object to service and get the saved object 
add object to view using modal map 
retun view
```

## insert service

```
create a [Entity]Service interface
create its implementation [Entity]ServiceImpl
get repo object using autowire by constructor injection
pass the [Entity] object to repo and get the saved object 
return saved object
```

## repo

```
create an interface [Entity]Repo which extends JpaRepository
1st parameter is entity class,
2nd parameter is data type of ID of entity
```

## pom

```
<!-- for @Controller, @RequestMapping-->
<!-- for view support -->
<!-- for crud operations-->
<!-- for mysql connection-->
```

## for view resolving

```
spring.mvc.view.prefix=/WEB-INF/
spring.mvc.view.suffix=.jsp
``` 

## to connect with database

```
spring.datasource.url=jdbc:mysql://localhost:3306/projectdb
spring.datasource.username=root
spring.datasource.password=root
``` 
