// 같은 숫자는 싫어

function solution(arr)
{
    let answer = [];
    for (let i of arr) {
        if (answer.length === 0 || answer[answer.length -1 ] !== i) {
            answer.push(i);
        }
        
    }
    
    return answer;
}

console.log(solution([1,1,3,3,0,1,1]));