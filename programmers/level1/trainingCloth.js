// 체육복

function solution(n, lost, reserve) {
    let answer = n - lost.length;
    lost.sort((a, b) => a - b);
    reserve.sort((a, b) => a - b);
    
    const candidate = [];
    for (let i = 0; i < lost.length; i++) {
        if (reserve.includes(lost[i])) {
            idx = reserve.indexOf(lost[i]);
            reserve.splice(idx, 1);
            answer += 1;
            candidate.push(i);
        }
    }

    candidate.reverse();

    for (let i of candidate) {
        lost.splice(i, 1);
    }

    console.log(lost, reserve);

    for (let sd of lost) {
        let idx;

        if (reserve.includes(sd - 1)) {
            idx = reserve.indexOf(sd - 1);
            reserve.splice(idx, 1);
            answer += 1;
            continue;
        }

        if (reserve.includes(sd + 1)) {
            idx = reserve.indexOf(sd + 1);
            reserve.splice(idx, 1);
            answer += 1;
        }
    }

    return answer;
}

console.log(solution(5, [2, 3, 4], [1, 2, 3]))
console.log(solution(5,[1, 2, 3],[2, 3, 4]))