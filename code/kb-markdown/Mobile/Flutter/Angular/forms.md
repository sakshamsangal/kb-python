# Template driven form

## Create form and register controls

``` html
<div class="container">
  <div class="row">
    <div class="col-xs-12 col-sm-10 col-md-8 col-sm-offset-1 col-md-offset-2">
      <form (ngSubmit)="save()" #f="ngForm">
        <div
          #userData="ngModelGroup"
          id="user-data" ngModelGroup="userData">
          <div class="form-group">
            <label for="username">Username</label>
            <input
              required
              ngModel
              name="username"
              type="text" id="username" class="form-control">
          </div>
          <button
            (click)="suggestUserName()"
            class="btn btn-default" type="button">Suggest an Username</button>
          <div class="form-group">
            <label for="email">Mail</label>
            <input
              required
              email
              #email="ngModel"
              ngModel
              name="email"
              type="email" id="email" class="form-control">
            <span *ngIf="!email.valid && email.touched" class="help-block">Enter email</span>
          </div>
        </div>

        <p *ngIf="!userData.valid && userData.touched">user data is invalid</p>
        <div class="form-group">
          <label for="secret">Secret Questions</label>
          <select
            [ngModel]="defaultQues"
            name="secret"
            id="secret" class="form-control">
            <option value="pet">Your first Pet?</option>
            <option value="teacher">Your first teacher?</option>
          </select>
        </div>
        <div *ngFor="let g of genders">
          <label for="">
            <input
              ngModel
              [value]="g"
              name="g"
              type="radio"> {{ g }}
          </label>
        </div>
        <button
          [disabled]="!f.valid"
          class="btn btn-primary" type="submit">Submit</button>
      </form>
    </div>
  </div>
</div>

```

## register controls

```ts
ngModel
name="username"
```

## Submit form

```ts
<form (ngSubmit)="save()" #f="ngForm">
  save(f: NgForm): void {
    console.log(f);
  }
```

## State

```ts

```

## Accessing form with @ViewChild

```ts
@ViewChild('f') f: NgForm;
  save(): void {
    console.log(this.f);
    this.f.reset();
  }
```

## Validation

```ts
required 
email

```

## Output error Validation msg

```ts
<span *ngIf="!email.valid && email.touched" class="help-block">Enter email</span>
[disabled]="!f.valid"
```

## Set default values with ngModel property

```ts
            [ngModel]="defaultQues"
  defaultQues = 'pet';

```

## ngModel with 2 way binding

```ts
[(ngModel)]
```

## Grouping form control

```ts
ngModelGroup="userData"
#userData="ngModelGroup"
<p *ngIf="!userData.valid && userData.touched">user data is invalid</p>
```

## Radio buttons

```ts
genders = ['male', 'female'];
<div *ngFor="let g of genders">
    <label for="">
    <input
        ngModel
        [value]="g"
        name="g"
        type="radio"> {{ g }}
    </label>
</div>
```

## Set and patch

```ts
this.f.setValue({
    userData: {
    username: suggestedName,
    email: ''
    },
    secret: 'pet',
    g: 'male'
});

this.f.form.patchValue({
    userData: {
    username: suggestedName
    }
});
```

## Form data

```ts

```

## Reset forms

```ts
save(): void {
    console.log(this.f);
    this.f.reset();
}
```