let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = input[0].split(' ').map(Number);
const N_data = input.slice(1, 1 + N);
const M_data = input.slice(1 + N);

let count = 0;

const resultObject = {};

N_data.forEach((ele) => (resultObject[ele] = true));

M_data.forEach((ele) => {
  if (resultObject[ele]) count++;
}); 

console.log(count)