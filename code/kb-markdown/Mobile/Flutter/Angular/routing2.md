## 1. Module Introduction

```javascript


```

## 2. Why do we need a Router

```javascript


```

## 4. Setting up and Loading Routes

```javascript
const appRoutes: Routes = [
  { path: '', component: HomeComponent },
  { path: 'users', component: UsersComponent},
  { path: 'servers', component: ServerssComponent}
];

@NgModule({
  imports: [
    RouterModule.forRoot(appRoutes)
  ],
})


```

## 5. Navigating with Router Links

```html
<!-- app comp ts  -->
<li role="presentation">
    <a routerLink="/">Home</a>
</li>
<li role="presentation"
    <a routerLink="servers">Servers</a>
</li>
<li role="presentation"
    <a [routerLink]="['users']">Users</a>
</li>

```

## 6. Understanding Navigation Paths

```html

<!-- servers html  -->

routerLink="servers" // localhost:4200/servers/servers 
routerLink="/servers" // abs, localhost:4200/servers 

```

## 7. Styling Active Router Links

```html
<li role="presentation"
    routerLinkActive="active"
    [routerLinkActiveOptions]="{exact: true}">
    <a routerLink="/">Home</a>
</li>
<li role="presentation"
    routerLinkActive="active">
    <a routerLink="servers">Servers</a>
</li>
<li role="presentation"
    routerLinkActive="active">
    <a [routerLink]="['users']">Users</a>
</li>

```

## 8. Navigating Programmatically

```javascript

Home html 
click onLoadServer()

inject router 
router.navigate(['/server']) // relative to root by default
```

## 9. Using Relative Paths in Programmatic Navigation

```javascript
 inject activatedRoute to refer current comp 

router.navigate(['/server'], {relativeTo: this.ar}) // relative to root by default

```

## 10. Passing Parameters to Routes

```javascript

  { path: 'users/:id', component: UsersComponent},

```

## 11. Fetching Route Parameters

```javascript
// we Fetching route Parameters using activatedRoute

ngoninit() {
    this.user = {
        id: ac.snapshot.params['id']
        id: ac.snapshot.params['name']
    }
}

```

## 12. Fetching Route Parameters Reactively

```javascript
[routerLink] = "['/users', 10, 'ana']"

ac.params.subs(
    (p) => {
        user.id = p['id'];
        user.id = p['name'];
    }
);

```

## 13. An Important Note about Route Observables

```javascript

ps = ac.params.subs(
    (p) => {
        user.id = p['id'];
        user.id = p['name'];
    }
);

destroy() {
    ps.unsubs();
}


```

## 14. Passing Query Parameters and Fragments

```javascript


```

## 15. Retrieving Query Parameters and Fragments

```javascript


```

## 16. Practicing and some Common Gotchas

```javascript


```

## 17. Setting up Child (Nested) Routes

```javascript


```

## 18. Using Query Parameters - Practice

```javascript


```

## 19. Configuring the Handling of Query Parameters

```javascript


```

## 20. Redirecting and Wildcard Routes

```javascript


```

## 22. Outsourcing the Route Configuration

```javascript


```

## 23. An Introduction to Guards

```javascript


```

## 24. Protecting Routes with canActivate

```javascript


```

## 25. Protecting Child (Nested) Routes with canActivateChild

```javascript


```

## 26. Using a Fake Auth Service

```javascript


```

## 27. Controlling Navigation with canDeactivate

```javascript


```

## 28. Passing Static Data to a Route

```javascript


```

## 29. Resolving Dynamic Data with the resolve Guard

```javascript


```

## 30. Understanding Location Strategies

```javascript


```