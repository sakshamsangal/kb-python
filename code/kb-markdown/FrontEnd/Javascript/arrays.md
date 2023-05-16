/* TODO 1: Declare a variable with identifier itemsInCart in your code and initialize it with 0.*/
var itemsInCart = 0;

function addItem() { var numberOfItemsInCart = ++itemsInCart; console.log("Item added to cart!"); console.log("Item(s)
in cart =",numberOfItemsInCart );
}
function removeItem() { var numberOfItemsInCart = --itemsInCart; console.log("Item removed from cart!"); console.log("
Item(s) in cart =",numberOfItemsInCart );
}
// WARNING: DO NOT EDIT THE CODE GIVEN BELOW
console.log("Initially: Item(s) in cart = " + itemsInCart);
addItem();
addItem();
removeItem();