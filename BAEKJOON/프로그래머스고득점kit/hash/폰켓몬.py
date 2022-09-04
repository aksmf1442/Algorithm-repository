def solution(nums):
    maxNum = len(nums) // 2
    setLength = len(set(nums))
    return maxNum if setLength > maxNum else setLength

print(solution([3,3,3,2,2,4]))