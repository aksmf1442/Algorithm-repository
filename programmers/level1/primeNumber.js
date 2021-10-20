// 소수 만들기

function solution(nums) {
    var answer = 0;
    const length = nums.length;
    
    const primeCheck = (num) => {
        for (let i = 2; i < num; i++) {
            if (num % i == 0) {
                return false;  
            }
        }
        return true;
    }
    
    for (let i = 0; i < length; i++) {
        for (let j = i + 1; j < length; j++) {
            for (let z = j + 1; z < length; z++) {
                if (primeCheck(nums[i] + nums[j] + nums[z])) {
                    answer += 1;
                }
            }
        }
    }
    
    return answer;
}
console.log(solution([1,2,3,4]));