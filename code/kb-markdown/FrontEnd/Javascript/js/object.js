// object shared same memory
var obj = new Object();
var obj1 = obj
obj.name = "saksham"
console.log(obj1);



// to free memory
obj = null

// using reference types
var products = new Array();
var date = new Date();
var error = new Error("oops!");
var fun = new Function("console.log('hii')");
var reg = new RegExp("//d+");

var obj = new Object();
obj.name = "saksham";

// using literals
let obj = {
    name: "saksham"
}

var arr = new Array(1, 2, 3); // reference
var arr = [1, 2, 3] // literal

var reg = new RegExp("\\d+");
var reg = /\d+/;


course1 = {
    name: "ram" // put
}

course2 = new Object() 
course2.name = "sagal" // put

course1.name = "shyam" //set
course1.des = "hii" // put

course1 = {
    name: "ram" // put
}
console.log("name" in course1); // true
console.log("name1" in course1); // false

course1 = {
    name: "ram" // put
}
console.log("toString" in course1); // true
console.log(course1.hasOwnProperty("toString")); // false
console.log(course1.hasOwnProperty("name")); // true


course1 = {
    name: "ram" // put
}
delete course1.name
console.log(course1.hasOwnProperty("name")); // true


course1 = {
    name: "ram", // put
    age: 12
}

for(var eachProp in course1) {
    console.log(eachProp);
}
// retrieving keys
var myKeys = Object.keys(course1)
console.log(myKeys);


course1 = {
    name: "ram", // put
    age: 12
}

console.log(course1.propertyIsEnumerable("name"));

course1 = {
    _name: "ram", // put
    get name() {
        return this._name;
    },
    set name(value) {
        this._name = value
    }
}

console.log(course1._name);
console.log(course1.name);

course1 = {
    name: "ram", // put
}
console.log(course1.propertyIsEnumerable("name"));
Object.defineProperty(course1, "name", {
    enumerable: false
})

console.log(course1.hasOwnProperty("name"));
console.log(course1.propertyIsEnumerable("name"));

course1 = {
    name: "ram", // put
}
Object.defineProperty(course1, "name", {
    configurable: false
})

delete course1.name
course1.name = "saksham"
console.log(course1.hasOwnProperty("name"));
console.log(course1.name);


//
var testObject = {
    testKey1 : 'testValue1',
    'test-Key2' : 'testValue2'
  }
  
  testObject.testKey1 = 'newValue1';
  testObject['test-Key2'] = 'newValue2';
  
  console.log(testObject);