## global
```java
package com.example.demo.exception;

import com.example.demo.model.ApiError;
import lombok.RequiredArgsConstructor;
import org.springframework.context.MessageSource;
import org.springframework.context.annotation.Scope;
import org.springframework.http.ResponseEntity;
import org.springframework.web.bind.annotation.ExceptionHandler;
import org.springframework.web.bind.annotation.RestControllerAdvice;
import org.springframework.web.servlet.mvc.method.annotation.ResponseEntityExceptionHandler;

@RestControllerAdvice
@RequiredArgsConstructor
public final class GlobalExceptionHandler extends ResponseEntityExceptionHandler {

    private final MessageSource messageSource;



    @ExceptionHandler(Exception.class)
    public ResponseEntity<Object> handleAllException(final Exception e) {
        ApiError apiError = new ApiError();
        apiError.setCode("500 INTERNAL_SERVER_ERROR");
        apiError.addMessage(e.getMessage());
        return ResponseEntity.internalServerError().body(apiError);
    }


}
```