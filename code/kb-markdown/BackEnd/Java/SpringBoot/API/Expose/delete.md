```java
@DeleteMapping("/users/{id}")
public void deleteUser(@PathVariable("id") int id) {
    userService.deleteById(id);
}
```

```java


// rest controller
@DeleteMapping("/{id}")
public void deleteLocation(@PathVariable("id") int id) {
locationRepository.deleteById(id);
}

// controller
@RequestMapping("deleteLocation")
public String deleteLocation(@RequestParam("id") int id, ModelMap modelMap) {
// Location location = service.getLocationById(id);
Location location = new Location();
location.setId(id);
service.deleteLocation(location);
List<Location> locations = service.getAllLocations();
modelMap.addAttribute("locations", locations);
return "displayLocations";
}

// service
public void deleteLocation(Location location) {
repository.delete(location);
}
```