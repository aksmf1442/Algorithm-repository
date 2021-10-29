// 문자열 다루기 기본

function solution(s) {
    var answer = true;
    let result = 0;
    for (let i of s) {
        if (!['1','2','3','4','5','6','7','8','9','0'].includes(i)) {
            answer = false;
            break;
        } else {
            result += 1;
        }
    }
    if (result % 2 != 0 || !answer || s.length < 4 || s.length > 6) {
        return false
    }
    return true;
}

console.log(solution("a234"));