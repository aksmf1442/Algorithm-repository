def solution(s):
    answer = len(s)
    mid = len(s) // 2

    for i in range(1, mid + 1):
        candidate = ""
        value = s[0:i]
        count = 1

        for j in range(0, len(s), i):
            if s[j:j + i] == s[j + i:j + (2 * i)]:
                value = s[j:j + i]
                count += 1
            else:
                if count != 1:
                    candidate += str(count)
                candidate += value
                value = s[j + i:j + (2 * i)]
                count = 1

        if value:
            candidate += (str(count) + value)
        answer = min(answer, len(candidate))

    return answer

print(solution("aabbaccc"))