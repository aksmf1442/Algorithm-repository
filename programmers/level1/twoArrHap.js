// 내적

function solution(a, b) {
    return a.reduce((arr, _, i) => arr += a[i] * b[i], 0);
}

console.log(solution([1,2,3,4], [-3,-1,0,2]));