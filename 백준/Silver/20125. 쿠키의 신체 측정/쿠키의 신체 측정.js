const [info, ...board] = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');

const boardSize = Number(info);

const findHeart = () => {
    for (let i = 1; i < boardSize - 2; i += 1) {
        for (let j = 1; j < boardSize - 2; j +=1) {
            if (board[i][j] === '*' &&
                board[i-1][j] === '*' &&
                board[i+1][j] === '*' &&
                board[i][j - 1] === '*' &&
                board[i][j + 1] === '*') {
                    return [i, j]
                }
        }
    }
    return null;
};

const [heartR, heartC] = findHeart();

let leftArm = 0;
let rightArm = 0;
let waist = 0;
let leftLeg = 0;
let rightLeg = 0;


for (let i = heartC - 1; i >= 0 && board[heartR][i] === '*'; i -= 1) {
    leftArm += 1
}

for (let j = heartC + 1; j <= boardSize && board[heartR][j] === '*'; j += 1) {
    rightArm += 1
}

for (let k = heartR + 1; k < boardSize && board[k][heartC] === '*'; k += 1) {
    waist += 1
}

for (let m = heartR + waist + 1; m < boardSize && board[m][heartC - 1] === '*'; m += 1) {
    leftLeg += 1
}

for (let n = heartR + waist + 1; n < boardSize && board[n][heartC + 1] === '*'; n += 1) {
    rightLeg += 1
}

console.log(heartR + 1, heartC + 1);
console.log(leftArm, rightArm, waist, leftLeg, rightLeg);