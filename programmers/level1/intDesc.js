// 정수 내림차순으로 배치하기

function solution(n) {
    let answer = String(n).split("").map(x => parseInt(x));
    answer.sort((a, b) => b - a);
    answer = parseInt(answer.join(""));
    return answer;
}

console.log(solution(12345678));