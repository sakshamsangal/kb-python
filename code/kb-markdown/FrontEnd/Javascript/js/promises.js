// Promises are used to handle asynchronous operations in JavaScript

// A Promise has four states:
// fulfilled: Action related to the promise succeeded
// rejected: Action related to the promise failed
// pending: Promise is still pending i.e not fulfilled or rejected yet
// settled: Promise has fulfilled or rejected

// var promise = new Promise(function(resolve, reject){
//     //do something
// });

let promise = new Promise(function(resolve, reject) {
  const x = "geeksforgeeks";
  const y = "geeksforgeeks";
  if (x === y) {
    resolve();
  } else {
    reject();
  }
});

promise
  .then(function() {
    console.log("Success, You are a GEEK");
  })
  .catch(function() {
    console.log("Some error has occured");
  });

// Promise Rejected

var promise = new Promise(function(resolve, reject) {
  reject("Promise Rejected");
});

promise.then(
  function(successMessage) {
    console.log(successMessage);
  },
  function(errorMessage) {
    //error handler function is invoked
    console.log(errorMessage);
  }
);

// Promise reject
var promise = new Promise(function(resolve, reject) {
  throw new Error("Some error has occured");
});

promise
  .then(function(successMessage) {
    console.log(successMessage);
  })
  .catch(function(errorMessage) {
    //error handler function is invoked
    console.log(errorMessage);
  });
