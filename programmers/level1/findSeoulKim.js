// 서울에서 김서방 찾기

function solution(seoul) {
    var answer = '';
    for (let i = 0; i < seoul.length; i++) {
        if (seoul[i] === "Kim") {
            answer = i;
            break;
        }
    }
    return answer;
}