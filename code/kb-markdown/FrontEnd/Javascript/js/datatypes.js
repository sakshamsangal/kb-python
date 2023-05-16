// null == undefined // true
// Primitive       Non-Primitive/Reference
// Number          Arrays
// String          Objects
// Boolean
// Undefined
// Null

console.log("typeof x = " + typeof x); // undefined
console.log("typeof \"saksham\" = " + typeof "saksham"); // string
console.log("typeof \"12\" = " + typeof "12"); // string
console.log("typeof 12.3 = " + typeof 12.3); // number
console.log("typeof 12 = " + typeof 12); // number
console.log("typeof NaN = " + typeof NaN); // number
console.log("typeof null = " + typeof null); // number
console.log("typeof [1, 2, 3] = " + typeof [1, 2, 3]); // object
console.log("typeof {}= " + typeof {}); // object
console.log("typeof undefined = " + typeof undefined); // undefined
console.log("typeof true = " + typeof true); // boolean



// seperate allocation of memery
// primitive types are not pointer
let x = 12;
let y = x;
y = 121;
console.log(x);
console.log(y);

var x = null;
console.log(typeof x); // object
// === check data type also