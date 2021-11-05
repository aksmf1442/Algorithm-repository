// 하샤드의 수

function solution(x) {
    let sum = 0;
    for (let i of String(x)) {
        sum += (+i);
    }
    if (x % sum === 0) {
        return true;
    }
    return false;
}