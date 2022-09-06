def solution(prices):
    n = len(prices)
    answer = [0] * n

    stack = []
    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            top = stack.pop()
            answer[top] = i - top

        stack.append(i)

    while stack:
        top = stack.pop()
        answer[top] = n - 1 - top

    return answer

# [4, 3, 1, 1, 0]
print(solution([1, 2, 3, 2, 1]))