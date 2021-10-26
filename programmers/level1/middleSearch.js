// 가운데 글자 가져오기

function solution(s) {
    const middle = Math.floor(s.length / 2);
    if (s.length % 2 === 0) {
        return s.slice(middle - 1, middle + 1);
    } else {
        return s.slice(middle, middle + 1);
    }
    return  null;
}

console.log(solution('abcde'))
console.log(solution('qwer'))