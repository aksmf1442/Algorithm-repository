def solution(answers):
    answer = []
    candidate = [0] * 3
    a = [1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    for i in range(len(answers)):
        if a[i % len(a)] == answers[i]:
            candidate[0] += 1

        if b[i % len(b)] == answers[i]:
            candidate[1] += 1

        if c[i % len(c)] == answers[i]:
            candidate[2] += 1

    maxValue = max(candidate)

    for idx, value in enumerate(candidate):
        if value == maxValue:
            answer.append(idx + 1)
    return answer


print(solution([1, 3, 2, 4, 2]))
print(solution([1, 2, 3, 4, 5]))
