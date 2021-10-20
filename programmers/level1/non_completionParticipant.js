// 완주하지 못한 선수

function solution(participant, completion) {
    var answer = '';
    participant.sort();
    completion.sort();
    for (i = 0; i < participant.length; i++) {
        if (participant[i] != completion[i]) {
            return participant[i];
        }
    }
    return false;
}

console.log(solution(["leo", "kiki", "eden"], ["eden", "kiki"]))