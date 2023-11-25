let input = require('fs').readFileSync('/dev/stdin').toString().trim();

while(input.length) {
    console.log(input.slice(0, 10));
    input = input.slice(10);
}