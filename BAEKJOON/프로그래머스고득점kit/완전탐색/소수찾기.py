from itertools import permutations

# 1. 소수인지 확인하는 함수를 만든다.
# 2. numbers의 길이만큼 조합을 다 만들어본다.
def validate(value):
    if value <= 1 or visited[value]:
        return False
    visited[value] = 1
    for i in range(2, value):
        if value % i == 0:
            return False
    return True

visited = [0] * 10000000
def solution(numbers):
    answer = 0
    numbers = list(numbers)
    for i in range(1, len(numbers) + 1):
        for arr in permutations(numbers, i):
            if validate(int("".join(arr))):
                answer += 1
    return answer

print(solution("011"))
print(solution("17"))