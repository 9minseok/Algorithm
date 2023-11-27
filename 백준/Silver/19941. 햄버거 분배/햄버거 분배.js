let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');
const [table_length, diff] = input.shift().split(' ').map(Number);

let answer = 0;
input = input[0].split('');
for (let i = 0; i < table_length; i++) {
  if (input[i] === 'P') {
    const start = i - diff;
    const end = i + diff;

    for (let j = start; j <= end; j++) {
      if (input[j] === 'H') {
        answer += 1;
        input[j] = 'D';
        break;
      }
    }
  }
}
console.log(answer)