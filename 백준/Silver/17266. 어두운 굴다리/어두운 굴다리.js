const input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const [N, M] = [input[0], input[1]]; // 굴다리길이 N, 가로등 개수 M
const positions = input[2].split(' ').map(Number); // 설치 지역
const candidates = [];

for (let i = 0; i < M - 1; i++) {
  candidates.push(Math.ceil((positions[i + 1] - positions[i]) / 2 ));
} // Math.ceil -> 주어진 수보다 크거거나 같은 숫자 integer로 반환

console.log(Math.max(positions[0], Math.max(...candidates), N - positions.at(-1)));
