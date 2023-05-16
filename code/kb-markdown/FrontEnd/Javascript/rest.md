```
function sum(...items) {
  return items.reduce((previous, current) => {
    return previous + current;
  });
}

console.log(sum(10, 10, 20, 30));
// expected output: 77



```