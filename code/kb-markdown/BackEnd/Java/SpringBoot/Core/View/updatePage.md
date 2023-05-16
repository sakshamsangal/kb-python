# Update page

```jsp 
<div class="container">
    <div class="row">
        <div class="col-md-8"></div>
        <div class="col-md-4">
            <br><br><br><br><br><br>
            <h3>Update location</h3>
            <form action="updateLocation" method="post">
                <div class="form-group">
                    <label>Id</label>
                    <input type="text" class="form-control form-control-sm" name="id" value="${location.id}" readonly>
                </div>
                <div class="form-group">
                    <label>Code</label>
                    <input type="text" class="form-control form-control-sm" name="code" value="${location.code}">
                </div>

                <div class="form-group">
                    <label>Name</label>
                    <input type="text" class="form-control form-control-sm" name="name" value="${location.name}">
                </div>
                <div class="form-check">
                    <label class="form-check-label">
                        <input type="radio" class="form-check-input" name="type" value="URBAN" ${location.type=='URBAN'?'checked':''}>URBAN
                    </label>
                </div>
                <div class="form-check">
                    <label class="form-check-label">
                        <input type="radio" class="form-check-input" name="type" value="RURAL" ${location.type=='RURAL'?'checked':''}>RURAL
                    </label>
                </div>
                <button type="submit" class="btn btn-primary btn-block btn-sm">Submit</button>
            </form>
        </div>
    </div>
</div>

```