# async

## example 1

```javascript
const getData = async() => { 
	var data = "Hello World"; 
	return data; 
} 

getData().then(data => console.log(data)); 


const getData = async() => { 
	var y = await "Hello World"; 
	console.log(y); 
} 

console.log(1); 
getData(); 
console.log(2); 
```

## example 2

``` javascript
async function fun() {
    const resp = await fetch("https://jsonplaceholder.typicode.com/posts");
    const post = await resp.json();
    return post;
}

a = fun();
a.then((data) => {
    console.log(data);
});
console.log("saksham");
```