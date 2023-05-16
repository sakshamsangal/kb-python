```bash
npm install firebase --save
npm install @angular/fire --save 
```

===========================================================================

# environment.ts

```javascript
export const environment = {
  production: false,
  firebase: {
    apiKey: "AIzaSyB7s9s9uVgiZ1w1X2lMqMPaSDRvj7uEv2c",
    authDomain: "project2-2092a.firebaseapp.com",
    databaseURL: "https://project2-2092a.firebaseio.com",
    projectId: "project2-2092a",
    storageBucket: "project2-2092a.appspot.com",
    messagingSenderId: "641766531722"
  }
};

===========================================================================
# component file
import { HttpClient } from '@angular/common/http';
import { AngularFirestore } from '@angular/fire/firestore';
constructor(private angularFirestore: AngularFirestore) { }

===========================================================================
# module
import { AngularFireModule } from "@angular/fire";   
import { AngularFirestoreModule } from "@angular/fire/firestore";
import { environment } from './../environments/environment';


AngularFireModule.initializeApp(environment.firebase),
AngularFirestoreModule

===========================================================================
# service 
import { AngularFirestore } from '@angular/fire/firestore';
constructor(private angularFirestore: AngularFirestore) { }

insert(data) {
	this.angularFirestore.collection("employees").add(data)
	console.log('insert')
}

display() {
	return this.angularFirestore.collection("employees").snapshotChanges();
	console.log('display')
}

update(id, data) {
	this.angularFirestore.doc("employees/" + id).update(data)
	console.log('update')
}

delete(id) {
	this.angularFirestore.doc("employees/" + id).delete()
	console.log('delete')
}

private subject = new Subject()
b$ = this.subject.asObservable()

sendData(obj){
this.subject.next(obj)
}

===========================================================================
# component 
insert() {
	this.generalService.insert(this.arr)
}


display() {
	this.generalService.display()
		.subscribe(
			data => {

				this.main = data.map(item => {
					return {
						id: item.payload.doc.id,
						...item.payload.doc.data()
					}
					as Employees
				})
				console.log(this.main)
			}
		)
	// console.log(this.main)
}

id = "fUtH2jdXnZdX4jpxCYyo"
update() {
	this.generalService.update(this.id, this.arr)
}


delete() {
	this.generalService.delete(this.id)
}

===========================================================================
```

# html

<button (click)="insert()">Insert</button>
<button (click)="update()">Update</button>
<button (click)="delete()">Delete</button>

```
https://my-fire-904e5-default-rtdb.firebaseio.com/

{
  "rules": {
    ".read": "now < 1614796200000",  // 2021-3-4
    ".write": "now < 1614796200000",  // 2021-3-4
  }
}

```