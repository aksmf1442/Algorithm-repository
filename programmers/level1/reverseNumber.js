// 자연수 뒤집어 배열로 만들기

function solution(n) {
    var answer = String(n).split("").map(x => parseInt(x));
    answer.reverse();
    return answer;
}

console.log(solution(12345));