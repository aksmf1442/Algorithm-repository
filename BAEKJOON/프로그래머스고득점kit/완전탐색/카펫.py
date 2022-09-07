# 1. brown yellow를 더하기
# 2. 더한 값에서 나올 수 있는 곱하기의 경우의 수를 구함
# 3. 경우의 수를 확인해보기
# 4. x는 최소 3, y도 최소 3(가로 길이는 세로 길이와 같거나 세로 길이보다 김 - sort(reverseTrue)하면 됌)
def solution(brown, yellow):
    answer = []
    total = brown + yellow
    x = 3
    while True:
        while total % x != 0:
            x += 1
        y = total // x
        brownCount = (x * 2) + (y * 2) - 4
        if brownCount == brown:
            answer = [x, y]
            answer.sort(key=lambda x:-x)
            break
        x += 1

    return answer

print(solution(10, 2))
print(solution(8, 1))
print(solution(24, 24))