let input = require('fs').readFileSync('/dev/stdin').toString().trim();

let sepinput = input.split('').sort();
let result = input.split('').sort((a, b) => (b - a)).join('');

sepinput[0] != 0 ? console.log(-1) : sortArray(sepinput);

function sortArray(num) {
  let arr_sum = 0

  num.forEach((element,index) => {
    arr_sum  += parseInt(num[index])
  });
  arr_sum % 3 === 0 ? console.log(result) : console.log(-1);
}
