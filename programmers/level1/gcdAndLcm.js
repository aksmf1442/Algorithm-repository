// 최대공약수와 최소공배수

function solution(n, m) {
    let answer = [];
    result = 0;
    for (let i = 2; i <= (n*m); i++) {
        if (n % i === 0 && m % i === 0) {
            result = i;
        }
    }
    answer.push(result);
    answer.push((n * m) / answer[0]);
    return answer;
}