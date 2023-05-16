# Display page

```jsp 
<div class="container">
    <br><br>
    <h3>Locations:</h3>
    <table class="table table-dark table-striped table-sm">
        <tr>
            <th>id</th>
            <th>code</th>
            <th>name</th>
            <th>type</th>
            <th>Delete</th>
            <th>Edit</th>
        </tr>

        <c:forEach items="${locations}" var="location">
            <tr>
                <td>${location.id}</td>
                <td>${location.code}</td>
                <td>${location.name}</td>
                <td>${location.type}</td>
                <td><a class="btn btn-danger btn-sm" href="deleteLocation?id=${location.id}">delete</a></td>
                <td><a class="btn btn-info btn-sm" href="updateLocationPage?id=${location.id}">edit</a></td>
            </tr>
        </c:forEach>
    </table>
    <a href="insertLocationPage" class="btn btn-primary btn-sm float-right">Insert  Location</a>
</div>

```