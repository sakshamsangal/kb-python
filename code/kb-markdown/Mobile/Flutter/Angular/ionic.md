```bash
ionic -v
cordova -v

npm install ionic -g
npm install cordova -g


ionic start todo blank 
ionic lab
ionic serve


```

======================
./home.html
<ion-buttons end>

</ion-buttons>
<button ion-button (click)="fun1()">
    <ion-icon name="add"></ion-icon>
</button>

```javascript
fun1(){
    let x = this.alertController
    .create({
        "title": "add",
        "msg": "enter todo"
        "inputs": [
            {
                "type": "text",
                "name": "addInput"
            }
        ]
        "buttons": [
            {
                "text": "cancel"
            },
            {
                "text": "add"

            }
        ]
    })
    x.present()
}

import { AlertController } from 'ionic-angular'
alertController AlertController

public arr = []

handler: (data) => {
    let y 
    y = data.addInput
    this.arr.push(y)
}
