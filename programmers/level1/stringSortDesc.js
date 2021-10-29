// 문자열 내림차순으로 배치하기

function solution(s) {
    var answer = s.split('');
    answer.sort((a, b) => b.charCodeAt() - a.charCodeAt());
    return answer.join('');
}

console.log(solution("Zbcdefg"));