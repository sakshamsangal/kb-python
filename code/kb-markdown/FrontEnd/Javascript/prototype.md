```javascript
// TODO 1: Create an object named shape which has a key is2D having the value true
let shape = {
    is2D: true
}
// TODO 2: Create an object named circle which has a key radius having the value 3
let circle = {
    radius: 3
}
// TODO 3: Create an object named rectangle which has keys length and breadth having the values 1 and 2 respectively
let rectangle = {
    length: 1,
    breadth: 2
}
// TODO 4: Change the prototype of the circle object to the shape object
circle.__proto__ = shape;
// TODO 5: Print the values of the is2D and radius keys on the circle object
console.log("Is circle a 2D shape? " + shape.is2D);
console.log("Radius of circle = " + circle.radius);


// TODO 6: Change the prototype of the rectangle object to the shape object
rectangle.__proto__ = shape;
// TODO 7: Print the values of the is2D, length, and breadth keys on the rectangle object
console.log("is rectangle a 2D shape? " + shape.is2D);

console.log("Length of rectangle = " + rectangle.length,", Breadth of rectangle = " + rectangle.breadth);

```