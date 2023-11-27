let input = require('fs').readFileSync('/dev/stdin').toString().trim().split('\n');


const T = input.shift(); // 테스트 케이스

for (let i = 0; i < T; i++) {
  const N = input.shift(); // 사람 수
  let teamNumbers = input.shift().split(' ').map(Number); // 팀 번호
  let team = {};
  let del = new Set();

  teamNumbers.forEach((num) => {
    (!team[num]) ? team[num] = 1 :team[num] ++;
    (team[num]) < 6 ? del.add(num) : del.delete(num);
  });

  let ranking = 1;
  let obj = {};
  teamNumbers.forEach((num) => {
    if (!del.has(num)) {
      if (!obj[num])
        obj[num] = [1, ranking, 0];
      else {
        if(obj[num][0] < 4) {
          obj[num][0]++;
          obj[num][1] += ranking;
        }
        else if (obj[num][0] === 4) {
          obj[num][0]++;
          obj[num][2] = ranking;
        }
      }
      ranking++;
    }
  });

  const sortedTeam = Object.entries(obj).sort((a, b) => {
    if (a[1][1] === b[1][1]) return a[1][2] - b[1][2];
    else return a[1][1] - b[1][1];
  });

  console.log(sortedTeam[0][0]);
}
