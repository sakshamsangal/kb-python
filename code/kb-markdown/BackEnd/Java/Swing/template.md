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

```
package com.company.view;

import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;

public class AddView implements ActionListener {
    JTextField tf1, tf2, tf3;
    JButton b1, b2;

    public AddView() {
        JFrame f = new JFrame();
        f.getContentPane().setLayout(new BorderLayout());
        f.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        f.setSize(500, 500);
        f.setLocationRelativeTo(null);
        f.setVisible(true);

        tf1 = new JTextField();
        tf1.setBounds(50, 50, 150, 20);
        tf2 = new JTextField();
        tf2.setBounds(50, 100, 150, 20);
        tf3 = new JTextField();
        tf3.setBounds(50, 150, 150, 20);
        tf3.setEditable(false);
        b1 = new JButton("+");
        b1.setBounds(50, 200, 50, 50);
        b2 = new JButton("-");
        b2.setBounds(120, 200, 50, 50);
        b1.addActionListener(this);
        b2.addActionListener(this);

        f.add(tf1);
        f.add(tf2);
        f.add(tf3);
        f.add(b1);
        f.add(b2);
    }
    public void actionPerformed(ActionEvent e) {
        String s1 = tf1.getText();
        String s2 = tf2.getText();
        int a = Integer.parseInt(s1);
        int b = Integer.parseInt(s2);
        int c = 0;
        if (e.getSource() == b1) {
            c = a + b;
        } else if (e.getSource() == b2) {
            c = a - b;
        }
        String result = String.valueOf(c);
        tf3.setText(result);
    }
}

```