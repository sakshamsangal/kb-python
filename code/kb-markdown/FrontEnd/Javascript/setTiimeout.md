const startTimer = () => {
const now = new Date();
h = now.getHours();
m = prefixWithZero(now.getMinutes());
s = prefixWithZero(now.getSeconds());
console.log(h + ": " + m + ": " + s);
}

prefixWithZero = (i) => {
if(i < 10) i = "0" + i;
return i;
}

for (let i = 0; i < 3; i++) {
setTimeout(startTimer, i * 1000);
}