# Insert page

## include

```jsp
<%@ page contentType="text/html; charset=UTF-8" pageEncoding="UTF-8" %>
<%@ page isELIgnored="false" %>
<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c" %>
```

## HTML format

```jsp

```

## custom css

```jsp
<link rel="stylesheet" href="css/styles.css">
```

## Form

```jsp
<div class="container">
    <div class="row">
        <div class="col-md-8"></div>
        <div class="col-md-4">
            <br><br><br><br><br><br>
            <h3>Insert location</h3>
            <form action="insertLocation" method="post">
                <div class="form-group">
                    <label>Id</label>
                    <input type="text" class="form-control form-control-sm" name="id">
                </div>
                <div class="form-group">
                    <label>Code</label>
                    <input type="text" class="form-control form-control-sm" name="code">
                </div>

                <div class="form-group">
                    <label>Name</label>
                    <input type="text" class="form-control form-control-sm" name="name">
                </div>
                <div class="form-check">
                    <label class="form-check-label">
                        <input type="radio" class="form-check-input" name="type" value="URBAN">URBAN
                    </label>
                </div>
                <div class="form-check">
                    <label class="form-check-label">
                        <input type="radio" class="form-check-input" name="type" value="RURAL">RURAL
                    </label>
                </div>
                <button type="submit" class="btn btn-primary btn-block btn-sm">Submit</button>
            </form>
            <p>${msg}</p>
            <a class="btn btn-primary btn-sm float-right" href="displayLocations">View All</a>
        </div>
    </div>
</div>
```