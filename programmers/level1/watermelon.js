// 수박수박수?

function solution(n) {
    let answer = Array(5001).join('수박');
    return answer.slice(0, n);
}

console.log(solution(1));