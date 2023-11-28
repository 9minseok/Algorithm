function solution(n)
{
    var answer = 0;
    let str = String(n);
    
    for (let i = 0; i < str.length; i++) {
        answer += parseInt(str[i])
    }

    return answer;
}