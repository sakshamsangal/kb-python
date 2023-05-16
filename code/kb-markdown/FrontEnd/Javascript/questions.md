```JavaScript
console.log(typeof typeof 9); // string

let arr = [1, 2, 3]
arr[10] = 12
console.log(arr[4]); // undefined

let a = typeof undefined == typeof NULL
console.log(a); // true because NULL is variable name, its not null, its NULL

console.log(3 > 2 > 1); // false
// true means 1
// 3 > 2 will give true
// true > 1
// means 1 > 1 

let students = {
    "ram": 22,
    "shyam": 25,
    "seeta": {
        age: 16
    }
};

var studentsClone = Object.assign({}, students);

students.ram = "25";
students.seeta.age = "18"

console.log('studentsClone ', studentsClone); 
// studentsClone  { ram: 22, shyam: 25, seeta: { age: '18' } }

// in cloning, nested objects are not clone.
// shallow copy is done 

let x = 25;
let priyanka = function () {
    console.log(x);
    var x = 22;
};
priyanka(); // undefined
// variable initialisation not hoisted
// it didnt went for global scope because 
// functions knews about local x not dont know its value
// if var x = 22 was absent then x = 25(func go for the global one)

// hoisting 
function raj(){ 
	a = 10; 
	var b = 50; 
} 
raj(); 
console.log(a); // 10
console.log(b); // ReferenceError : b is not defined 

// a is global because a is undeclared
// var scope is within function 

(function () {
    var x, y;
    try {
        throw new Error();
    } catch (x) {
        x = 10;
        y = 20;
        console.log(x);
    }
    console.log(x);
    console.log(y);
})();

// 10
// undefined
// 20 
// first preference goes to local variable than global variable
