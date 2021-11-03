// 평균 구하기

function solution(arr) {
    var answer = arr.reduce((a, b) => a += b);
    return answer / arr.length;
}

console.log(solution([1,2,3,4]));