# Service design pattern

## Imports

```java
import org.springframework.stereotype.Service;
```

## Class

```java
@Service
public class LocationService { }
```

## Field

```java
private final LocationRepository repository;
```

## constructor

```java
public LocationService(LocationRepository repository) {
    this.repository = repository;
}
```

# Service methods

## insert

```java
public Location saveLocation(Location location) {
    return repository.save(location);
}
```

## display

``` java
public Location getLocationById(int id) {
    Optional<Location> optionalLocation = repository.findById(id);
    return optionalLocation.orElse(null);
}

public List<Location> getAllLocations() {
    return repository.findAll();
}
```

## delete

``` java
public void deleteLocation(Location location) {
    repository.delete(location);
}
```

## update

``` java
public void updateLocation(Location location) {
    repository.save(location);
}
```

```java
package com.example.war;

import org.springframework.stereotype.Service;

import javax.persistence.EntityManager;
import javax.persistence.ParameterMode;
import javax.persistence.PersistenceContext;
import javax.persistence.StoredProcedureQuery;

@Service
public class LoginServiceImpl {

    @PersistenceContext
    private EntityManager entityManager;

    public int checkUsernameAndPassword(String username, String password, int price) {

        //"login" this is the name of your procedure
        StoredProcedureQuery query = entityManager.createStoredProcedureQuery("product");

        //Declare the parameters in the same order
        query.registerStoredProcedureParameter(1, String.class, ParameterMode.IN);
        query.registerStoredProcedureParameter(2, String.class, ParameterMode.IN);
        query.registerStoredProcedureParameter(3, Integer.class, ParameterMode.IN);
        query.registerStoredProcedureParameter(4, Integer.class, ParameterMode.OUT);

        //Pass the parameter values
        query.setParameter(1, username);
        query.setParameter(2, password);
        query.setParameter(3, price);

        //Execute query
        query.execute();

        //Get output parameters
        return (int) query.getOutputParameterValue(4);
    }
}

```