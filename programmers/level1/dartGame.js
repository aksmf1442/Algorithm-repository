// 다트게임

function solution(dartResult) {
    const answer = new Array(3).fill(0);
    let number = "";
    let idx = 0;
    for (let i of dartResult) {
        if (parseInt(i) >= 0 && parseInt(i) <= 10) {
            number += i;
        }

        if (i === "S") {
            number = parseInt(number);
            number = number ** 1;
            answer[idx] = number;
            idx++;
            number = "";
        }

        if (i === "D") {
            number = parseInt(number);
            number = number ** 2;
            answer[idx] = number;
            idx++;
            number = "";
        }

        if (i === "T") {
            number = parseInt(number);
            number = number ** 3;
            answer[idx] = number;
            idx++;
            number = "";
        }

        if (i === "*") {
            answer[idx - 1] *= 2;
            if (idx >= 2) {
                answer[idx - 2] *= 2;
            }

        }

        if (i === "#") {
            answer[idx - 1] *= (-1);
        }
    }
    console.log(answer);

    return answer.reduce((a, b) => a += b);
}

console.log(solution("1D2S#10S"));