// a is not inside function therefore, a is global and var is used
{
  var a = 10;
  console.log(a);
} //block 1
{
  a++;
  console.log(a);
} //block 2

function sum() {
    var a = 10;
}
console.log(a); // ReferenceError: a is not defined


// a is not inside function therefore, a is global and let is used
// let scope is within block
{
  let a = 10;
  console.log(a);
} //block 1
{
  a++; // error a is not defined
  console.log(a);
} //block 2

// var scope = inside function
// let  and const scope = inside block
// let was introduced as part of ES6
// const value cannot change

// let , var const global
let a = 4;
function myFunction() {
  return a * a;
}

console.log(myFunction());