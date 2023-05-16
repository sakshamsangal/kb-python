# thymeleaf

**location** `src/main/resources/templates/hello.html`

**pom** `-thymeleaf`

| character | means                                                               |
|-----------|---------------------------------------------------------------------|
| @         | for writing url, uri e.g. in form action, for css @{/css/temp.css}` |
| $         | read data from controller                                           |
| *         | used in form input to bind the java object                          |

**show data from java controller** div th:text="${message}"

**to prevent html cache** `spring.thymeleaf.cache=false`

**show list**

```text
ul th:each="student:${students}"
    th:text="${student.name}"
    th:text="${student.score}"
```

**to get the data from html form** `@ModelAttribute`

**form data submit**

```text
form th:object="${student}" action="@{/insert-student}"
input th:field="*{name}"
input th:field="*{score}"
```