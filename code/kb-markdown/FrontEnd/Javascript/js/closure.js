// A closure is the combination of a function bundled together (enclosed) with references to its surrounding state (the lexical environment). In other words, a closure gives you access to an outer function’s scope from an inner function. In JavaScript, closures are created every time a function is created, at function creation time.

// we want to make a counter that is available for all the function calls
var counter = 0;

// Function to increment counter
function add() {
  counter += 1;
}

// Call add() 3 times
add();
add();
add();
console.log(counter);
// the problem in this we can change counter any where in the code.
// ------------------------------------
function add() {
  var counter = 0;
  counter += 1;
  return counter;
}

// Call add() 3 times
add();
add();
add();
console.log(add());

// the problem with this every time the counter is getting 0 which is not desirable.

// ------------------------------------
// solution is closure
var add = (function () {
  var counter = 0;
  return function () {
    counter += 1;
    return counter;
  };
})();

add();
add();
add();

console.log(add());

// ------------------------------------
let multiple = function (x) {
  return function(y) {
      console.log(x);
      console.log(y);
      y = x;
  }
}

let sum = multiple(2)
sum(3);
sum(5);