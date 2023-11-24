let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('');

let arr0 = [];
let arr1 = [];
let string = '';

function solution(min_num, max_num, array) {
  for (let i = 0; i < input.length; i++) {
    if (input[i] === min_num) {
      string += input[i];
      if (input[i + 1] === max_num || input[i + 1] === undefined) {
        array.push(string);
        string = '';
      }
    }
  }
}

solution('0', '1', arr0);
solution('1', '0', arr1);

console.log(Math.min(arr0.length, arr1.length));