# Rest Controller

```java
package com.example.demo.controller;

import lombok.RequiredArgsConstructor;
import lombok.extern.slf4j.Slf4j;

import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;


import com.example.demo.service.UserService;


@RestController
@RequestMapping("/api")
@RequiredArgsConstructor
@Slf4j
public class UserController {
    private final UserService userService;



}
```

```java
package org.example.controller;

import org.example.model.request.PenRequest;
import org.example.model.response.PenResponse;
import io.swagger.v3.oas.annotations.Operation;
import io.swagger.v3.oas.annotations.media.Content;
import io.swagger.v3.oas.annotations.media.Schema;
import io.swagger.v3.oas.annotations.responses.ApiResponse;
import io.swagger.v3.oas.annotations.responses.ApiResponses;

import org.springframework.http.MediaType;
import org.springframework.http.ResponseEntity;

import org.springframework.web.bind.annotation.*;



public interface PenController {

    @Operation(description = "this is desc", summary = "this is summary")
    @ApiResponses(value = {
            @ApiResponse(responseCode = "200", description = "success", content = {@Content(mediaType = MediaType.APPLICATION_JSON_VALUE, schema = @Schema(implementation = Object.class))})
    })
    ResponseEntity<PenResponse> postPen(@RequestBody PenRequest penRequest) ;
}

```