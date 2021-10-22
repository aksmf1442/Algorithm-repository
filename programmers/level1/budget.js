// 예산

function solution(d, budget) {
    var answer = 0;
    d.sort((a, b) => {
        return a - b;
    });
    for (let i of d) {
        if (i > budget) {
            break;
        }
        answer += 1;
        budget -= i;
    }
    return answer;
}

console.log(solution([1,3,2,5,4], 9));