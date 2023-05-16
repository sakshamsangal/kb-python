# spring aop

## step 1

- add dependency
    - aop
    - boot starter/web
    - lombok

## step 2

- make advice class with pointcut annotation

com/example/demo/advice/MilkAdvice.java

```java
package com.example.demo.advice;

import lombok.extern.slf4j.Slf4j;
import org.aspectj.lang.ProceedingJoinPoint;
import org.aspectj.lang.annotation.Around;
import org.aspectj.lang.annotation.Aspect;
import org.aspectj.lang.annotation.Pointcut;
import org.springframework.stereotype.Component;

import com.fasterxml.jackson.databind.ObjectMapper;

@Aspect
@Component
@Slf4j
public class MilkAdvice {


    @Pointcut(value = "execution(* com.example.demo.controller.*.*(..) )")
    public void myPointcut() {

    }

    @Around("myPointcut()")
    public Object applicationLogger(ProceedingJoinPoint pjp) throws Throwable {
        ObjectMapper mapper = new ObjectMapper();
        String methodName = pjp.getSignature().getName();
        String className = pjp.getTarget().getClass().toString();
        Object[] array = pjp.getArgs();
        log.info("=================================");
        log.info("Unified logging");
        log.info("methodName = " + methodName);
        log.info("className = " + className);
        log.info("Unified logging request: " + mapper.writeValueAsString(array));
        Object object = pjp.proceed();
        log.info("Unified logging response: " + mapper.writeValueAsString(object));
        log.info("=================================");
        return object;
    }

}
```




