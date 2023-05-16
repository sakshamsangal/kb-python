## car
```html

<style>
    .btn {
        margin: 0.2em;
    }
</style>

<div>
    <h2>{{car[0]}}</h2>
    <h2>{{car[1]}}</h2>


</div>
```

## create
```html
{% include 'header.html' %}
{% include 'navbar.html' %}
<div class="container" style="margin-top: 1em;">
    <form action="/cars" method="POST">
        <div class="row">
            <div class="col-md-6">

                <div class="mb-3">
                    <label class="form-label">Input location of stefan excel</label>
                    <input type="text" class="form-control" name="year"
                           value="C:/Users/saksangal/Documents/Zoom/Book1.xlsx">
                </div>

                                <div class="mb-3">
                    <label class="form-label">Sheet name</label>
                    <input type="text" class="form-control" name="sn"
                           value="Sheet1">
                </div>
            </div>
            <div class="col-md-6">

                <div class="mb-3">
                    <label class="form-label">Output location of java file</label>
                    <input type="text" class="form-control" name="java"
                           value="C:/Users/saksangal/Documents/Zoom/out.txt">
                </div>

                <button type="submit" class="btn btn-primary block">Submit</button>
            </div>
        </div>


    </form>
</div>
{% include 'footer.html' %}
```

## footer
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-ka7Sk0Gln4gmtz2MlQnikT1wXgYsOg+OMhuP+IlRH9sENBO0LRn5q+8nbTov4+1p" crossorigin="anonymous"></script>
</body>
</html>
```

## header
```html
<!DOCTYPE html>
<html lang="en">
<head>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <link rel="stylesheet" href="{{url_for('static', path='/style.css')}}" type="text/css">
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{title|default("Document")}}</title>
</head>
<body>
```

## home
```html
{% include 'header.html' %}
{% include 'navbar.html' %}
<h1>Welcome to your first app in FastAPI!</h1>
{% include 'footer.html' %}
```

## index.html
```html
{% include 'header.html' %}
{% include 'navbar.html' %}
<div class="container-fluid">
    {% for car in cars %}
        <div class="row justify-content-center" style="text-align: center;">
            <div class="col col-sm-6" style="border: 1px solid black; margin: 1em 0.5em; border-radius: 10px;">
                {% include 'car.html' %}
            </div>
        </div>
    {% endfor %}
</div>
{% include 'footer.html' %}
```

## navbar
```html
<nav class="navbar navbar-expand-md navbar-dark fixed-top bg-dark">
    <div class="container-fluid">
        <a class="navbar-brand" href="#">Util</a>
        <button class="navbar-toggler" type="button" data-bs-toggle="collapse" data-bs-target="#navbarCollapse"
                aria-controls="navbarCollapse" aria-expanded="false" aria-label="Toggle navigation">
            <span class="navbar-toggler-icon"></span>
        </button>
        <div class="collapse navbar-collapse" id="navbarCollapse">
            <ul class="navbar-nav me-auto mb-2 mb-md-0">
                <li class="nav-item">
                    <a class="nav-link active" aria-current="page" href="#">Home</a>
                </li>

            </ul>
        </div>
    </div>
</nav>
<br><br>
<br>
```

## style
```html
.navbar-brand {
    font-weight: 600;
    font-size: 1.5em;
}

.navbar-dark .navbar-nav .nav-link {
    color: white;
}
```