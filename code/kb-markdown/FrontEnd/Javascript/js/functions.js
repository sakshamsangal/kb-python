// simple functions
function sum(a, b) {
    return a + b;
}
sum(2, 3) // 5

// arrow functions    
const sum = (a, b) => {
    return a + b;
}
sum(2, 3) // 5

const getValue = a => a; // if single argument and single statement
const get12 = () => 12; // if no argument and single statement

getValue(4) // 4
get12() // 12


// anonymous/callback
// (a, b) => {
//     return a + b;
// }

// self invoking
((a, b) => {
    return a + b;
})();

let s = "Saksham";
let x = 123;
console.log(s.toLowerCase());
console.log(s.substring(2, 5));
console.log(s.charAt(5));
console.log(typeof x.toString());

// instanceof is used to check whether variable is Array, Object EventSource. 
function fun(x, y) {
    console.log(fun.length);
}
fun(10, 20, 30, 40);