## getController
this is a get api
```java
/**
 * this is a get api
 *
 * @param yearOfBirth first parameter
 * @return ResponseEntity this will return response entity
 */
@GetMapping("/customHeader")
ResponseEntity<String> getUser(@RequestParam("yearOfBirth") int yearOfBirth) {
    return ResponseEntity.ok()
            .header("Custom-Header", "foo")
            .body("Custom header set");
}
```

