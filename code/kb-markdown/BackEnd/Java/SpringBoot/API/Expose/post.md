```java
@PostMapping("/users")
public User postUser(@RequestBody User user) {
    return userService.save(user);
}

```
```java

@PostMapping
public Location createLocation(@RequestBody Location location) {
return locationRepository.save(location);
}

@RequestMapping("/saveLoc")
public String saveLocation(@ModelAttribute("location") Location location, ModelMap modelMap) {
Location locationSaved = service.saveLocation(location);
String msg = "Location saved with id: " + locationSaved.getId();
modelMap.addAttribute("msg", msg);

    // email sending
    // email.sendEmail("sakshamsangal111@gmail.com", "Location saved", "Hi, Location saved");
    return "createLocation";

}

public Location saveLocation(Location location) {
return repository.save(location);
}
```