// 나누어 떨어지는 숫자 배열

function solution(arr, divisor) {
    var answer = [];
    for (let i of arr) {
        if (i % divisor === 0) {
            answer.push(i);
        }
    }
    answer.sort((a, b) => a - b);
    if (answer.length === 0) {
        answer.push(-1);
    }
    return answer;
}