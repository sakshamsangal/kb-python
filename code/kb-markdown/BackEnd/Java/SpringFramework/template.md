## JSP template in servlet

```
<%@ page language="java" contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
<%@page isELIgnored="false" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link rel="stylesheet" href="<%=request.getContextPath()%>/css/styles.css">
</head>
<body>



</body>
</html>
```

## scriptlets

```
<%!   
 // java code 
%>  

<%= // direct print %>  

<% out.print("Today is:"+java.util.Calendar.getInstance().getTime()); %>  

<%   
  // used for writing servlet code.
%>  
```

## for loop in JSP using JSTL

```
<table>
    <tr>
        <th>Airlines</th>
        <th>Departure City</th>
        <th>Arrival City</th>
        <th>Departure Time</th>

    </tr>

    <c:forEach items="${flights}" var="flight">
        <tr>
            <td>${flight.operatingAirlines}</td>
            <td>${flight.departureCity}</td>
            <td>${flight.arrivalCity}</td>
            <td>${flight.estimatedDepartureTime}</td>
            <td><a href="showCompleteReservation?flightId=${flight.id}">Select</a></td>
        </tr>

    </c:forEach>
</table>
```

```
${msg} // direct print variable in jsp

request.getContextPath() // return root directory of project
```

## If user is not logged in then redirect him to default page i.e index.jsp

```
try {
    if (session.getAttribute("emailId").equals(null)) {
        response.sendRedirect(request.getContextPath());
    }
} catch (NullPointerException e) {
    response.sendRedirect(request.getContextPath());
}
```

## Logged In as

```
Logged In as <%
try {
    out.print(session.getAttribute("emailId").toString().split("@")[0]);
} catch (NullPointerException e) {}
%>
```

```
<form id="post_form" method="post" action="<%=request.getContextPath()%>/blog/post">
<span><%=session.getAttribute("emailId")%></span>
```

## @WebServlet("/blog/post")

```
public class PostServlet extends HttpServlet 
```

## log out

```
<%
    session.invalidate();
    response.sendRedirect(request.getContextPath());
%>
```

## Write java code to populate all the tag options in the drop down menu.

```
<%
    HashSet<String> tagList = new DAOFactory().getPostCRUDS().findAllTags();
    Object[] array = tagList.toArray();
    for (int i = 0; i < array.length; i++) { %>
<option value="<%=array[i]%>"><%=array[i]%>
</option>
<%
    }
%>
```

## TODO: 7.15. Write code to get posts for the selected "tag" and render the search result on the web page.

```

<%
    if (request.getMethod().equals("POST")) {
        List<PostDTO> postDTOS = new DAOFactory().getPostCRUDS().findByTag(request.getParameter("tag"));
        for (int i = 0; i < postDTOS.size(); i++) { %>
            <div class="post-list">
                <div>Post Id: <%=postDTOS.get(i).getPostId()%>
                </div>
                <div>Email Id: <%=postDTOS.get(i).getEmailId()%>
                </div>
                <div>Title: <%=postDTOS.get(i).getTitle()%></div>
                <div>Tag: <%=postDTOS.get(i).getTag()%>
                </div>
                <div>Description: <%=postDTOS.get(i).getDescription()%>
                </div>
                <div>Time: <%=DateTimeFormatter.format(postDTOS.get(i).getTimestamp())%>
                </div>
            </div>
<%
        }
        if (postDTOS.size() < 1) {
            out.print("Sorry no posts exists for this tag");
        }

    }
%>
```

## If user tries to click on browser bac k button then he/ she should not be able to access this page*/

```
response.setHeader("Cache-Control", "no-cache");
response.setHeader("Cache-Control", "no-store");
response.setHeader("Pragma", "no-cache");
response.setDateHeader("Expires", 0);
```