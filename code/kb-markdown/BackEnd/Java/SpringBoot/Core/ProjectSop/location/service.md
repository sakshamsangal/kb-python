## LocationService

``` java 
package com.mylocation.modal.service;

import com.mylocation.modal.dao.LocationRepository;
import com.mylocation.modal.dto.Location;
import org.springframework.stereotype.Service;

import java.util.List;
import java.util.Optional;


@Service
public class LocationService {

    private final LocationRepository repository;

    public LocationService(LocationRepository repository) {
        this.repository = repository;
    }

    public Location saveLocation(Location location) {
        return repository.save(location);
    }

    public void updateLocation(Location location) {
        repository.save(location);
    }

    public void deleteLocation(Location location) {
        repository.delete(location);
    }

    public Location getLocationById(int id) {
        Optional<Location> optionalLocation = repository.findById(id);
        return optionalLocation.orElse(null);
    }

    public List<Location> getAllLocations() {
        return repository.findAll();
    }
}
    
```
