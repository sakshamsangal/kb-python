// sum of all elements

arr = [2, 1, 3]

let ans = arr.reduce((sum, element) => {
    return sum += element
}, 0)
console.log(ans)
