## file system

```
main
    webapp
        WEB-INF 
            web.xml
        index.jsp
```

## web.xml

```
<servlet>
    <servlet-name>employeeRegisterServlet</servlet-name>
    <servlet-class>com.upgrad.controllers.EmployeeRegisterServlet</servlet-class>
</servlet>

<servlet-mapping>
    <servlet-name>employeeRegisterServlet</servlet-name>
    <url-pattern>/register</url-pattern>
</servlet-mapping>
```

## index.jsp

```
<form action="/register" method="post">
    <input type="text" placeholder="name" name="name"/>
    <input type="text" placeholder="department" name="department">
    <input type="text" placeholder="company" name="company">
    <button type="submit">submit</button>
</form>
```

## servlet class

```
import javax.servlet.ServletException;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

public class UserServlet extends HttpServlet {
    // Override doGet, doPost
}
```

## servlet method

```
// doGet method
@Override
protected void doGet(HttpServletRequest req, HttpServletResponse resp) throws IOException {

}


// doPost method
@Override
protected void doPost(HttpServletRequest req, HttpServletResponse resp) throws IOException {

}
```

## get value from web page

```
req.getParameter("department") // <input type="text" name="department">
```

## print to browser

```
PrintWriter printWriter = resp.getWriter();
printWriter.println("saksham"); // saksham
```

## setting and getting value in req object

```
// setting value in req object
req.setAttribute("username", "saksham");

// getting value in req object
req.getAttribute("username"); // saksham
```

## navigation using RequestDispatcher

```
RequestDispatcher requestDispatcher = req.getRequestDispatcher("/square"); // this path is defined in web.xml
requestDispatcher.forward(req, resp); // send us to other servlet
```

## navigation using sendRedirect

```
// redirecting to another servlet
resp.sendRedirect("/square"); // reciever should be doGet

// sending data in sendRedirect
resp.sendRedirect("/square?id=" + id); // reciever should be doGet
```

## session

```
// make session object
    // create session if not pressent
    // if session present return the value / null
    HttpSession httpSession = req.getSession(); 
    
    // does not create session
    // if session present return the value / null
    HttpSession httpSession = req.getSession(false);

// set value in session object
httpSession.setAttribute("username", "saksham");

// to receive session 
httpSession.getAttribute("username")

// removing session
httpSession.removeAttribute("username");

// never expire session
<web-app>
    <session-config>
        <session-timeout>-1</session-timeout>
    </session-config>
</web-app>

// expire session after 10 minutes
<web-app>
    <session-config>
        <session-timeout>10</session-timeout>
    </session-config>
</web-app>


// session timeout after 600 seconds
httpSession.setMaxInactiveInterval(10*60); // 10 minutes


```

## cookie

```
// cookie object
Cookie cookie = new Cookie("username", "saksham");

// add cookie
resp.addCookie(cookie);

// receive cookie
Cookie[] cookies = req.getCookies();
for (Cookie cookie : cookies) {
    if (cookie.getName().equals("username")) System.out.println(cookie.getValue());
}

```