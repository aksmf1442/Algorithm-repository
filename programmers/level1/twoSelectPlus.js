// 두 개 뽑아서 더하기

function solution(numbers) {
    var answer = [];
    const ck = new Array((Math.max(...numbers) * 2) + 1).fill(0);
    console.log(ck);
    numbers.sort((a, b) => {
        return a - b;
    });
    for (let i = 0; i < numbers.length; i++) {
        for (let j = i + 1; j < numbers.length; j++) {
            const num = numbers[i] + numbers[j];
            if (ck[num] === 0) {
                answer.push(num);
                ck[num] = 1;
            }
        }
    }
    answer.sort((a, b) => {
        return a - b;
    })
    return answer;
}

console.log(solution( [0, 0, 0, 4, 3, 2, 1, 1]));