// 이상한 문자 만들기

function solution(s) {
    var answer = '';
    const candidate = s.split(" ");
    for (let can of candidate) {
        for (let i = 0; i < can.length; i++) {
            if (i % 2 === 0) {
                answer += can[i].toUpperCase();
            } else {
                answer += can[i].toLowerCase();
            }
        }
        answer += " ";
    }

    return answer.slice(0, s.length);
}

console.log(solution("try hello world"));