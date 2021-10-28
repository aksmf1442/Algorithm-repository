// 문자열 내 p와y의 개수

function solution(s){
    var answer = false;
    s = s.toLowerCase();
    let pNumber = 0;
    let yNumber = 0;
    for (let i of s) {
        if (i === "p") {
            pNumber += 1;
        }

        if (i === "y") {
            yNumber += 1;
        }
    }

    if (pNumber === yNumber) {
        answer = true;
    }

    return answer;
}

console.log(solution('aA'))