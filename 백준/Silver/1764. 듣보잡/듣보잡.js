let input = require('fs').readFileSync('dev/stdin').toString().trim().split('\n');

const [N, M] = input.shift().split(' '); // shift 는 배열의 첫번째값 제거 후 반환

let n_set = new Set();
let m_set = new Set();

for (let i = 0; i < input.length; i++) {
    if (i < N) {
        n_set.add(input[i]); // 듣도
    } else {
        m_set.add(input[i]); // 보도
    }
}

const intersect = [...n_set].filter(data => m_set.has(data)).sort();

console.log(intersect.length);
intersect.forEach(element => {
    console.log(element)
});
