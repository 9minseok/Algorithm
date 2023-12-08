const fs = require('fs');
const input = fs.readFileSync("./dev/stdin").toString().trim().split("\n").map(v=>v.trim()); 
const N = +input.shift()
const num = input[0].split(' ').map(v=>+v);
const answer = [...new Set(num)].sort((a,b)=>a-b)

console.log(answer.join(' '))