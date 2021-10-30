// 소수 찾기

function solution(n) {
    var answer = 0;
    const ck = Array(n+1).fill(0);
    for (let i = 2; i <= n; i++) {
        if (ck[i] === 1) {
            continue;
        }
        ck[i] = 1;
        answer += 1;
        for (let j = i * 2; j <= n; j += i)  {
            if (ck[j] === 1) {
                continue;
            }
            ck[j] = 1;
        }
        
    }
    return answer;
}
