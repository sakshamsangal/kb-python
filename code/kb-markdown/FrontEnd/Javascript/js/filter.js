// get adults
let age = [12, 8, 18, 22]

let adults = []
adults = age.filter((element) => {
    if(element < 18) {}
    else return element
})

console.log(adults)