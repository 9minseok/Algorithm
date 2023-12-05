let input = require('fs').readFileSync('/dev/stdin').toString().trim();
input = Number(input);
let end = 1;
let sum = 1;
let count = 0;

for (let start = 1; start <= input; start++) {
  while (sum < input && end < input) {
    end += 1;
    sum += end;
  }

  if (sum === input) {
    count += 1;
  }

  sum -= start;
}
console.log(count);