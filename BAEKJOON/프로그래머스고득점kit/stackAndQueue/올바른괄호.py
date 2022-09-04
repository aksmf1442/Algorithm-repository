def solution(s):
    answer = True
    # 1. (로 열렸다면 반드시 )로 닫혀야 하는 조건
    # 2. 그렇다면 )가 먼저 나오거나 ()의 수가 서로 같지 않으면 false
    count = 0
    for i in s:
        if i == '(':
            count += 1
        if i == ')':
            count -= 1
        if count < 0:
            break

    if count != 0:
        answer = False

    return answer

print(solution("(())()"	))
print(solution(")()("))
