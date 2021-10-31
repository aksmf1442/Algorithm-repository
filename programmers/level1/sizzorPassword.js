// 시저 암호

function solution(s, n) {
    var answer = '';
    const lowerString = "abcdefghijklmnopqrstuvwxyz";
    const upperString = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
    const length = 26;
    for (let i = 0; i < s.length; i++) {
        if (s[i] === s[i].toUpperCase() && s[i] !== " ") {
            let idx = (upperString.indexOf(s[i]) + n) % length;
            answer += upperString[idx];
        }

        if (s[i] === s[i].toLowerCase() && s[i] !== " ") {
            let idx = (lowerString.indexOf(s[i]) + n) % length;
            answer += lowerString[idx];
        }

        if (s[i] === " ") {
            answer += " ";
        }
    
    }
    return answer;
}

console.log(solution("a B z", 4))