// 자릿수 더하기

function solution(n)
{
    var answer = 0;
    
    for (let i of String(n)) {
        answer += parseInt(i);
    }
    return answer;
}