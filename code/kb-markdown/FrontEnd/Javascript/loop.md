## for in loop is used to iterate over json

itemsToBuy is json array.
We are getting key of object in item of for in loop
Again we are iterating over json and once you get price as key hen we are storing the value of price in itemPricesArr
array.

```
	
var itemsToBuy = {
    milk: {
        quantity : 5,
        price: 20
    },
    bread: {
        quantity : 2,
        price: 15
    },
    potato: {
        quantity : 3,
        price: 10
    }
}

items = []
prices = []
for(i in itemsToBuy) {  // iterating over json array
    items.push(i);
    prices.push(itemsToBuy[i].price);
}


// Print the array consisting of the names of the items here
console.log(items);

// Print the array consisting of the prices of the items here
console.log(prices);
```