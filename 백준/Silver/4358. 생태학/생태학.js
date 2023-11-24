const input = require('fs').readFileSync('/dev/stdin').toString().trim().split(/\r?\n/);

let countObject = {};

input.forEach(ele => {
    countObject[ele] == null ? countObject[ele] = 1 : countObject[ele] += 1
});

console.log(Object.keys(countObject).sort().map(key => `${key} ${(countObject[key] / input.length * 100).toFixed(4)}`).join('\n'));