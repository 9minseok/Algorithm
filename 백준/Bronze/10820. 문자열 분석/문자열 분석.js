const input = require('fs').readFileSync('dev/stdin').toString().split("\n");

const inputLength = input.length;

for (let i = 0; i < inputLength; i++) {
    let inputs = input[i].split("");

    if (inputs.length === 0) continue;

    const counts = [0, 0, 0, 0];

    for (let j = 0; j < inputs.length; j++) {
        const char = inputs[j];

        if (char >= 'a' && char <= 'z') {
            counts[0]++;
        } else if (char >= 'A' && char <= 'Z') {
            counts[1]++;
        } else if (char >= '0' && char <= '9') {
            counts[2]++;
        } else if (char === ' ') {
            counts[3]++;
        }
    }
    console.log(`${counts[0]} ${counts[1]} ${counts[2]} ${counts[3]}`);
}