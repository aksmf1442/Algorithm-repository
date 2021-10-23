// 2016년

function solution(a, b) {
    var answer = '';
    const month = [31, 29, 31, 30, 31, 30, 31, 31, 30 ,31, 30, 31];
    const day = ['THU', 'FRI', 'SAT', 'SUN', 'MON', 'TUE', 'WED'];
    let d = 0;
    for (let i = 0; i < a - 1; i++) {
        d += month[i];
    }
    d += b;
    answer = day[d % 7];
    return answer;
}

console.log(solution(5, 24));