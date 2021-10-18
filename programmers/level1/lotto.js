function solution(lottos, win_nums) {
    var answer = [];
    result = 0;
    zero = 0;
    for (i = 0; i < 6; i++) {
        if (lottos[i] === 0) {
            zero += 1;
        }

        if (win_nums.includes(lottos[i])) {
            result += 1;
        }
        console.log(lottos[i], result);
    }

    maxResult = result + zero;
    
    if (maxResult === 6) {
        answer.push(1);
    }
    if (maxResult === 5) {
        answer.push(2);
    }
    if (maxResult === 4) {
        answer.push(3);
    }
    if (maxResult === 3) {
        answer.push(4);
    }
    if (maxResult === 2) {
        answer.push(5);
    }
    if (maxResult <= 1) {
        answer.push(6);
    }

    if (result === 6) {
        answer.push(1);
    }
    if (result === 5) {
        answer.push(2);
    }
    if (result === 4) {
        answer.push(3);
    }
    if (result === 3) {
        answer.push(4);
    }
    if (result === 2) {
        answer.push(5);
    }
    if (result <= 1) {
        answer.push(6);
    }
    
    return answer;
}

console.log(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]));