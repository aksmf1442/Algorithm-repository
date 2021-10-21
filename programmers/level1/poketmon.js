// 폰켓몬

function solution(nums) {
    const candidate = new Set(nums);
    return candidate.size < nums.length / 2 ? candidate.size : nums.length / 2;
}

console.log(solution([3,1,2,3]));