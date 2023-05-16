## LocationController

``` java 
package com.mylocation.controller;

import com.mylocation.modal.dao.LocationRepository;
import com.mylocation.modal.dto.Location;
import com.mylocation.modal.service.LocationService;
import com.mylocation.modal.utility.Email;
import com.mylocation.modal.utility.Report;
import org.springframework.stereotype.Controller;
import org.springframework.ui.ModelMap;
import org.springframework.web.bind.annotation.ModelAttribute;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RequestParam;

import javax.servlet.ServletContext;
import java.util.List;

@Controller
public class LocationController {

    final LocationRepository locationRepository;
    final LocationService service;
    final Email email;
    final Report report;
    final ServletContext servletContext;

    public LocationController(LocationRepository locationRepository, LocationService service, Email email, Report report, ServletContext servletContext) {
        this.locationRepository = locationRepository;
        this.service = service;
        this.email = email;
        this.report = report;
        this.servletContext = servletContext;
    }


    @RequestMapping("/insertLocationPage")
    public String showCreate() {
        return "insertLocation";
    }

    @RequestMapping("/insertLocation")
    public String saveLocation(@ModelAttribute("location") Location location, ModelMap modelMap) {
        Location locationSaved = service.saveLocation(location);
        String msg = "Location saved with id: " + locationSaved.getId();
        modelMap.addAttribute("msg", msg);

        // email sending
        // email.sendEmail("sakshamsangal111@gmail.com", "Location saved", "Hi, Location saved");
        return "insertLocation";
    }

    @RequestMapping("/displayLocations")
    public String displayLocations(ModelMap modelMap) {
        List<Location> locations = service.getAllLocations();
        modelMap.addAttribute("locations", locations);
        return "displayLocations";
    }

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

    @RequestMapping("/updateLocationPage")
    public String showUpdate(@RequestParam("id") int id, ModelMap modelMap) {
        Location location = service.getLocationById(id);
        modelMap.addAttribute("location", location);
        return "updateLocation";
    }

    @RequestMapping("/updateLocation")
    public String updateLocation(@ModelAttribute("location") Location location, ModelMap modelMap) {
        service.updateLocation(location);
        List<Location> locations = service.getAllLocations();
        modelMap.addAttribute("locations", locations);
        return "displayLocations";
    }

    @RequestMapping("/generateReport")
    public String generateReport() {
        String path = servletContext.getRealPath("/");
        List<Object[]> data = locationRepository.findTypeAndTypeCount();
        report.generatePieChart(path, data);
        return "report";

    }
}
```

## LocationRestController

``` java 
package com.mylocation.controller;

import com.mylocation.modal.dao.LocationRepository;
import com.mylocation.modal.dto.Location;
import org.springframework.web.bind.annotation.*;

import java.util.List;
import java.util.Optional;

@RestController
@RequestMapping("/locations")
public class LocationRestController {

    final LocationRepository locationRepository;

    public LocationRestController(LocationRepository locationRepository) {
        this.locationRepository = locationRepository;
    }

    @GetMapping
    public List<Location> getLocations() {
        return locationRepository.findAll();
    }

    @PostMapping
    public Location createLocation(@RequestBody Location location) {
        return locationRepository.save(location);
    }

    @PutMapping
    public Location updateLocation(@RequestBody Location location) {
        return locationRepository.save(location);

    }

    @DeleteMapping("/{id}")
    public void deleteLocation(@PathVariable("id") int id) {
        locationRepository.deleteById(id);
    }

    @GetMapping("/{id}")
    public Location getLocation(@PathVariable("id") int id) {
        Optional<Location> optionalLocation = locationRepository.findById(id);
        return optionalLocation.orElse(null);
    }
}
```

