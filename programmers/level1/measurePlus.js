function solution(left, right) {
    var answer = 0;

    const a = (number)=> {
        let result = 0;
        for (let i = 1; i <= number; i++) {
            result += number % i === 0 ? 1 : 0;
        }
        return result;
    };

    for (let i = left; i <= right; i++) {
        const num = a(i);
        answer += num % 2 === 0 ? i : (-i);
    }

    return answer;
}

console.log(solution(13, 17));