# Const in arrow function

## Note

```
Since we don't want to reassign arrow functions, that's why we use const keyword. We want a variable should hold one particular function only not anything else.

Although it's not compulsory to use const, it is a good programming practice.
```

## without const reassignment is possible

``` javascript
fun = () => {
      return "Hello World!";
}

fun = () => { 
      return "Tejashri";
}
console.log(fun()); // Tejashri
```

## with const reassignment is impossible

``` javascript
const fun = () => {
      return "Hello World!";
}

fun = () => { // TypeError: Assignment to constant variable.
      return "Tejashri";
}
console.log(fun()); // error
```