let x = 2; 
function fun(x) {
    x = 12;   // new x is made
}
// primitive type is call by value


let car = {
    "name": "swift"
}
// if we pass object to th func and change its value then its
// call by reference
function fun(car) {
    car.name = "celerio";
}
fun(car);
console.log(car);

arr = [1, 2, 3] // arrays are also call by reference
function fun(arr) {
    arr[0] = 10;
}
fun(arr)
console.log(arr);

/**
 * if object manupulation
 *      call by reference
 * else if object insertion
 *      call by value
 * else if primitive
 *      call by value
 */

arr = [1, 2, 3] // arrays are also call by reference
function fun(arr) {
    arr = [3, 4, 5]
}
fun(arr)
console.log(arr);

/**
 * if object
 *      call by reference
 * else
 *      call by value
 */





