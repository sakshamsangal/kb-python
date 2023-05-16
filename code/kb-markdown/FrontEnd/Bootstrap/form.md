``` html 
<div class="row">
    <div class="col-md-8"></div>
    <div class="col-md-4">
    <br><br><br><br><br><br><br><br>
    <h3>Login</h3>
    <form action="/action_page.php">
        <div class="form-group">
        <label for="email">Email:</label>
        <input type="email" class="form-control form-control-sm" id="email" placeholder="Enter email" name="email">
        </div>
        <div class="form-group">
        <label for="pwd">Password:</label>
        <input type="password" class="form-control form-control-sm" id="pwd" placeholder="Enter password"
            name="pswd">
        </div>
        <div class="form-group form-check">
        <label class="form-check-label">
            <input class="form-check-input" type="checkbox" name="remember"> Remember me
        </label>
        </div>
        <button type="submit" class="btn btn-primary btn-block btn-sm">Submit</button>
    </form>
    </div>
</div>
```

## form

``` html
<form action="insert-[entity]" method="post">

</form>
```

## text

``` html
<div class="form-group">
    <label>Id</label>
    <input type="text"
            class="form-control form-control-sm"
            name="id"
    />
</div>
```

## radio

``` html 
<div class="form-check">
    <label class="form-check-label">
        <input type="radio"
                class="form-check-input"
                name="type"
                value="URBAN"
        />
        URBAN
    </label>
</div> 
```

## button

``` html
<button type="submit"
        class="btn btn-primary btn-block btn-sm">
    Submit
</button>
```