let [N, ...input] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n').map((line) => line.replace('\r',''));

let diffstr = '';
for (let i = 0; i <input[0].length; i++) {
  const char = input[0][i];
  if (input.some((str) => str[i] !== char)) {
    diffstr += '?';
  } else {
    diffstr += char;
  }
}

console.log(diffstr);