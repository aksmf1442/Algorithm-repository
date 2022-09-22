# 1. logn 이하로 풀어야 할듯(이진탐색)

def solution(n, times):
    answer = 0
    left = min(times)
    right = max(times) * n
    times.sort()
    while left <= right:
        mid = (left + right) // 2
        checked = 0
        for time in times:
            checked += mid // time

            if checked >= n:
                break

        if checked >= n:
            right = mid - 1
            answer = mid
        else:
            left = mid + 1

    return answer


print(solution(6, [7, 10]))
