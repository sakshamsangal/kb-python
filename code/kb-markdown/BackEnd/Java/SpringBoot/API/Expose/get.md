
```java
    @GetMapping("/get")
    ResponseEntity<String> age() {

        return ResponseEntity.ok().body("Custom header set");
    }
    
    @GetMapping("/customHeader")
    ResponseEntity<String> age(@RequestParam("yearOfBirth") int yearOfBirth) {

        return ResponseEntity.ok()
                .header("Custom-Header", "foo")
                .body("Custom header set");
    }


    @GetMapping("/customHeader")
    ResponseEntity<String> age(@RequestParam("yearOfBirth") int yearOfBirth) {

        HttpHeaders headers = new HttpHeaders();
        headers.add("Custom-Header", "foo");
        return new ResponseEntity<>("Custom header set", headers, HttpStatus.OK);
    }


```
```java
@GetMapping("/users")
public List<User> getUsers() {
    return userService.findAll();
}

@GetMapping("/users/{id}")
public User getUserById(@PathVariable("id") int id) {
    return userService.findById(id).orElse(null);
}

```
```java
@GetMapping
public List<Location> getLocations() {
    return locationRepository.findAll();

}


@RequestMapping("/displayLocations")
public String displayLocations(ModelMap modelMap) {
    List<Location> locations = service.getAllLocations();
    modelMap.addAttribute("locations", locations);
    return "displayLocations";
}

// service
public List<Location> getAllLocations() {
    return repository.findAll();
}

@GetMapping("/{id}")
public Location getLocation(@PathVariable("id") int id) {
    Optional<Location> optionalLocation = locationRepository.findById(id);
    return optionalLocation.orElse(null);
}

public Location getLocationById(int id) {
    Optional<Location> optionalLocation = repository.findById(id);
    return optionalLocation.orElse(null);
}

```