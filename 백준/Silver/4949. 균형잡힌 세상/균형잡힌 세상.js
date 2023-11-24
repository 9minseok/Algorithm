let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

let compareStr = [];
let compareArray = [];
let result = [];
let paArray = ['(', ')', '[', ']'];

for (let i = 0; i < input.length; i++) {
  compareStr = input[i].split('')
  for (let j = 0; j < compareStr.length; j++) {
    if (compareStr[0] === '.') {
      compareArray.push('.')
      break
    }

    paArray.includes(compareStr[j]) === true ? compareArray.push([compareStr[j]]) : null;

    if(compareArray[compareArray.length-2] + compareArray[compareArray.length-1] === "()" || compareArray[compareArray.length-2] + compareArray[compareArray.length-1] === "[]") {
      compareArray.pop()
      compareArray.pop()
    }
  }
  
  if(compareStr[0] != '.') {
    compareArray.length !== 0 ? result.push('no') : result.push('yes')
  }
  compareArray = []
}

console.log(result.join('\n'));