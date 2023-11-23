let input = require('fs').readFileSync('/dev/stdin').toString().split('\n');

let num1 = input[0];
let num2 = input[1];

num1 = num1.toString().split('');
num2 = num2.toString().split('');

let num = 0;
let sum_array = [];

for (let i = 0; i <= 7; i ++) {
    sum_array.push(num1[i])
    sum_array.push(num2[i])
}

let cnt = 0;

let array_len = sum_array.length;
while (cnt < 14) {
    cnt++

    for (let i = 0; i < (array_len-1); i++) {
        num = (parseInt(sum_array[i]) + parseInt(sum_array[i+1])) % 10;

        sum_array.push(num)

        if (i == (array_len-2)) {
            sum_array.splice(0, array_len)
            array_len = sum_array.length;
        }
    }
}

console.log(`${sum_array[0]}${sum_array[1]}`)