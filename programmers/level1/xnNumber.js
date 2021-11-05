// x만큼 간격이 있는 n개의 숫자;

function solution(x, n) {
    var answer = [];
    if (x === 0) {
        const a = [];
        for (let i = 0; i < n; i++) {
            a.push(0);
        }
        return a;
    }
    for (let i = Math.abs(x); i <= Math.abs(x * n); i += Math.abs(x)) {
        if (x < 0) {
            answer.push(-i);
        } else {
            answer.push(i);
        }
    }
    return answer;
}

console.log(solution(0, 5));