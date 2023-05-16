```java
package com.example.demo.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import org.springframework.web.bind.annotation.*;

import com.example.demo.service.UserService;


import org.springframework.http.HttpStatus;
import org.springframework.http.ResponseEntity;
import org.springframework.web.multipart.MultipartFile;


import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;


@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
@Slf4j
public class UserController {
    private final UserService userService;

    //    upload:
//    dir: D:/Temporary/upload
    @PostMapping("/uploadFiles")
    public ResponseEntity<List<String>> uploadFiles(@RequestParam("files") MultipartFile[] files) {

        List<String> list = new ArrayList<>();
        Arrays.stream(files).forEach(file -> {
            String url = userService.uploadFiles(file);
            list.add(url);
        });
        return new ResponseEntity<>(list, HttpStatus.OK);
    }
}

package com.example.demo.service;

import org.springframework.web.multipart.MultipartFile;


public interface UserService {
    String uploadFiles(MultipartFile file);
}

package com.example.demo.service;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;


import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;

import org.springframework.beans.factory.annotation.Value;

import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.io.IOException;
import java.nio.file.FileAlreadyExistsException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.Objects;


@Service
@Slf4j
@RequiredArgsConstructor
public class UserServiceImpl implements UserService {


    @Value("${upload.dir}")
    public String uploadDir;

    @Override
    public String uploadFiles(MultipartFile file) {
        Path copyLocation;

        String fileName = file.getOriginalFilename();
        copyLocation = Paths.get(uploadDir + File.separator + StringUtils.cleanPath(Objects.requireNonNull(fileName)));

        try {
            Files.copy(file.getInputStream(), copyLocation);
            return copyLocation.toString();
        } catch (FileAlreadyExistsException e) {
            String[] arr = fileName.split("\\.");
            String finalFileName = arr[0] + "_" + System.currentTimeMillis() + "." + arr[1];
            copyLocation = Paths.get(uploadDir + File.separator + StringUtils.cleanPath(finalFileName));

            try {
                Files.copy(file.getInputStream(), copyLocation);
            } catch (IOException ioException) {
                ioException.printStackTrace();
            }
            return copyLocation.toString();
        } catch (Exception e) {
            e.printStackTrace();
            throw new RuntimeException("Could not store file " + file.getOriginalFilename() + ". Please try again!");
        }


    }
}


```


``` java
package com.example.myupload811;

import org.springframework.web.bind.annotation.ControllerAdvice;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.servlet.ModelAndView;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

@ControllerAdvice
public class AppExceptionHandler {

	@ExceptionHandler(FileStorageException.class)
	public ModelAndView handleException(FileStorageException exception, RedirectAttributes redirectAttributes) {

		ModelAndView mav = new ModelAndView();
		mav.addObject("message", exception.getMsg());
		mav.setViewName("error");
		return mav;

	}
}
```

``` java
package com.example.myupload811;

import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import org.springframework.web.multipart.MultipartFile;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;

@Service
public class FileService {

	// @Value("${app.upload.dir:${user.home}}")
	public String uploadDir = "D:/Temporary/upload";

	public void uploadFile(MultipartFile file) {

		try {
			Path copyLocation = Paths.get(uploadDir + File.separator + StringUtils.cleanPath(file.getOriginalFilename()));
			Files.copy(file.getInputStream(), copyLocation, StandardCopyOption.REPLACE_EXISTING);
		} catch (Exception e) {
			e.printStackTrace();
			throw new FileStorageException("Could not store file " + file.getOriginalFilename() + ". Please try again!");
		}
	}
}
```

``` java
package com.example.myupload811;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.stereotype.Controller;
import org.springframework.stereotype.Service;
import org.springframework.util.StringUtils;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PostMapping;
import org.springframework.web.bind.annotation.RequestParam;
import org.springframework.web.multipart.MultipartFile;
import org.springframework.web.servlet.mvc.support.RedirectAttributes;

import java.io.File;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.nio.file.StandardCopyOption;
import java.util.Arrays;

@Controller
public class FileController {

    @Autowired
    FileService fileService;

    @GetMapping("/")
    public String index() {
        return "upload";
    }

    @PostMapping("/uploadFile")
    public String uploadFile(@RequestParam("file") MultipartFile file, RedirectAttributes redirectAttributes) {

        fileService.uploadFile(file);

        redirectAttributes.addFlashAttribute("message",
                "You successfully uploaded " + file.getOriginalFilename() + "!");

        return "redirect:/";
    }

    @PostMapping("/uploadFiles")
    public String uploadFiles(@RequestParam("files") MultipartFile[] files, RedirectAttributes redirectAttributes) {

        Arrays.asList(files)
                .stream()
                .forEach(file -> fileService.uploadFile(file));

        redirectAttributes.addFlashAttribute("message",
                "You successfully uploaded all files!");

        return "redirect:/";
    }
}
```

``` java
package com.example.myupload811;

public class FileStorageException extends RuntimeException {

	private static final long serialVersionUID = 1L;
	private String msg;

	public FileStorageException(String msg) {
		this.msg = msg;

	}

	public String getMsg() {
		return msg;
	}
}
```

``` html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<head>
    <meta charset="UTF-8">
    <title>ERROR</title>
</head>
<body>

<h1>Error!!!</h1>

<div th:if="${message}">
    <h2 th:text="${message}"/>
</div>


</body>
</html>
```

``` html
<!DOCTYPE html>
<html xmlns:th="http://www.thymeleaf.org">
<body>

<h1>Spring Boot File Upload Example</h1>

<hr/>

<h4>Upload Single File:</h4>
<form method="POST" th:action="@{/uploadFile}" enctype="multipart/form-data">
    <input type="file" name="file"/> <br/><br/>
    <button type="submit">Submit</button>
</form>

<hr/>

<h4>Upload Multiple Files:</h4>
<form method="POST" th:action="@{/uploadFiles}" enctype="multipart/form-data">
    <input type="file" name="files" multiple/> <br/><br/>
    <button type="submit">Submit</button>
</form>

<hr/>

<div th:if="${message}">
    <h2 th:text="${message}"/>
</div>

</body>
</html>
```

``` xml
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-thymeleaf</artifactId>
</dependency>
<dependency>
    <groupId>org.springframework.boot</groupId>
    <artifactId>spring-boot-starter-web</artifactId>
</dependency>

```
