let inputs = require('fs').readFileSync('/dev/stdin').toString().trim();
inputs = Number(inputs);
let arr = [0, 1, 2];
if(inputs>2){
    for(let i=3; i<=inputs; i++){
    	arr[i] = (arr[i-1] + arr[i-2]) % 10007;
	}
}
console.log(arr[inputs]);