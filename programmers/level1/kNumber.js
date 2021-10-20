// k번째 수

function solution(array, commands) {
    var answer = [];
    
    for (let c of commands) {
        const arr = array.slice(c[0]-1, c[1]);
        // 숫자를 오름차순 정렬할 때는 안에 콜백 함수를 넣어줘야함.
        arr.sort((a, b) => a - b );
        answer.push(arr[c[2]-1]);
    }
    return answer;
}

console.log(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))