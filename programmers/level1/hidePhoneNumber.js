// 핸드폰 번호 가리기

function solution(phone_number) {
    var answer = '';
    const len = phone_number.length;
    for (let i = 0; i < len; i++) {
        if (len - i <= 4) {
            answer += phone_number[i];
        } else {
            answer += '*';
        }
    }
    return answer;
}