let [n, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').sort();

let countObject = []

input.forEach( ele => {
  countObject[ele] == null ? countObject[ele] = 1 : countObject[ele] += 1
});

let max = Math.max(...Object.values(countObject));

console.log(Object.keys(countObject).find(key => countObject[key] === max));