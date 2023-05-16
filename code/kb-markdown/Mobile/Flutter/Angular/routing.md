# import

import { Router, ActivatedRoute } from '@angular/router'
constructor(
private quesService: QuesService,
private router: Router,
private route: ActivatedRoute
) {}

ng generate module app-routing --module app --flat

# html

<a routerLink="/home">Home</a>
<router-outlet></router-outlet> <!-- in app html file -->

# routing module

```javascript
const routes: Routes = [
  {
    path: "",
    redirectTo: "/home",
    pathMatch: "full"
  },
  {
    path: "home",
    component: HomeComponent,
    children: [
      {
        path: "display",
        component: DisplayComponent
      },
      {
        path: "insert",
        component: InsertComponent
      },
      {
        path: "delete",
        component: DeleteComponent
      },
      {
        path: "update",
        component: UpdateComponent
      }
    ]
  },
  {
    path: "**",
    component: PageNotFoundComponent
  }
];
const routes: Routes = [
  {
    path: '',
    redirectTo: '/home',
    pathMatch: 'full'
  },
  {
    path: 'home',
    component: HomeComponent
  }
];


import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';

const routes: Routes = [];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
