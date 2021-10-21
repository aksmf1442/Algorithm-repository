// 모의고사
// 1번 : 12345 2번 : 21232425 3번 : 3311224455


function solution(answers) {
    const a = [1, 2, 3, 4, 5];
    const b = [2, 1, 2, 3, 2, 4, 2, 5];
    const c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5];
    const result = [0, 0, 0];
    for (let i = 0; i < answers.length; i++) {
        let aIdx = i % a.length;
        let bIdx = i % b.length;
        let cIdx = i % c.length;
        if (answers[i] === a[aIdx]) {
            result[0] += 1;
        }

        if (answers[i] === b[bIdx]) {
            result[1] += 1;
        }

        if (answers[i] === c[cIdx]) {
            result[2] += 1;
        }
    }

    const answer = [];
    for (let i = 0; i < result.length; i++) {
        if (Math.max(...result) === result[i]) {
            answer.push(i+1);
        } 
    } 

    return answer;
}

console.log(solution([1,3,2,4,2]))