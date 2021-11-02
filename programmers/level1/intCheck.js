//정수 제곱근 판별

function solution(n) {
    var answer = 0;
    for (let i = 1; i <= n; i++) {
        if (i ** 2 === n) {
            answer = (i + 1) ** 2;
        }
        
        if (i ** 2 >= n) {
            break;
        }
    }
    return answer;
}