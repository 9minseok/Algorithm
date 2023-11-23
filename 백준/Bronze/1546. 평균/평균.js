let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let count = Number(input[0]);
let numbers = input[1].split(' ');

let max = Math.max(...numbers);
let score = 0;

for (let i = 0; i < count; i++){
    score += numbers[i] / max * 100
}

console.log(score / count);