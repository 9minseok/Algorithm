let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let count = Number(input[0]);
let numbers = input[1].split(' ').map(x => parseInt(x));

let maxnumber = numbers[0];
let minnumber = numbers[0];

for (let i = 1; i < count; i++) {
    if (maxnumber < numbers[i]) {
        maxnumber = numbers[i];
    }

    if (minnumber > numbers[i]) {
        minnumber = numbers[i];
    }
}

console.log(`${minnumber} ${maxnumber}`);