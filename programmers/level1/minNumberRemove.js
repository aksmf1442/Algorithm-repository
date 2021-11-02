// 제일 작은 수 제거하기

function solution(arr) {
    let idx = arr.indexOf(Math.min(...arr));
    arr.splice(idx, 1);
    if (arr.length === 0) {
        arr.push(-1);
    }
    return arr;
}

console.log(solution([23,123,32]));