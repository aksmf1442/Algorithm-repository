// 실패율

function solution(N, stages) {
    const answer = [];
    const ck = new Array(N + 1).fill(0);
    ck[0] = -1;
    let length = stages.length;
    for (let i = 1; i <= N; i++) {
        const a = stages.reduce((cnt, element) => cnt + (element === i), 0);
        ck[i] = a / length;
        length -= a;
        if (length === 0) break;
    }

    while (Math.max(...ck) >= 0) {
        const max_value = Math.max(...ck);
        for (let i = 1; i <= N; i++) {
            if (max_value === ck[i]) {
                answer.push(i);
                ck[i] = -1;
                break;
            }
        }
    }
    return answer;
}

console.log(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]));