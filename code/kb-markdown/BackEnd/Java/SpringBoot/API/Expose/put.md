```java

@PutMapping("/users")
public User putUser(@RequestBody User user) {
    return userService.save(user);
}

```


```java
@PutMapping
public Location updateLocation(@RequestBody Location location) {
return locationRepository.save(location);

}

@RequestMapping("/showUpdate")
public String showUpdate(@RequestParam("id") int id, ModelMap modelMap) {
Location location = service.getLocationById(id);
modelMap.addAttribute("location", location);
return "updateLocation";
}

@RequestMapping("/updateLoc")
public String updateLocation(@ModelAttribute("location") Location location, ModelMap modelMap) {
service.updateLocation(location);
List<Location> locations = service.getAllLocations();
modelMap.addAttribute("locations", locations);
return "displayLocations";
}

public void updateLocation(Location location) {
repository.save(location);
}


```

