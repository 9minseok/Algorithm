const input = require('fs').readFileSync('/dev/stdin').toString().trim();

let isTag = false;
let result = '';
let currentWord = '';

for (let i = 0; i < input.length; i++) {
    const char = input[i];

    if (char === '<') {
        isTag = true;
        result += currentWord.split('').reverse().join('') + '<';
        currentWord = '';
    } else if (char === '>') {
        isTag = false;
        result += '>';
    } else if (isTag) {
        result += char;
    } else {
        if (char === ' ') {
            result += currentWord.split('').reverse().join('') + ' ';
            currentWord = '';
        } else {
            currentWord += char;
        }
    }
}

result += currentWord.split('').reverse().join('');
console.log(result);