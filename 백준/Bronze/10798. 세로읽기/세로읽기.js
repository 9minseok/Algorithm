let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map(str => str.replace('\r',''));

let maxLength = Math.max(...input.map(i => i.length));

let result = [];

for (let i = 0; i < maxLength; i++) {
  for (let j = 0; j < input.length; j++) {
    input[j][i] === undefined ? null : result.push(input[j][i]);
  }
}

console.log(result.join(''));