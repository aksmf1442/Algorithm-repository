# goal: 신규회원이 사용하기를 원하는 아이디가 이미 기존 회원 목록에 있다면
# 규칙에 맞게 추천해주기
# 조건
# 1. 모든 아이디는 알파벳 소문자(len3~6) + 숫자(0~9, len0~6)
# 2. n의 길이가 1이상이면 첫 자리가 0이 될 수 없다.

def solution(registered_list, new_id):
    S = ""
    N = ""
    for i in new_id:
        if 97 <= ord(i) <= 122:
            S += i

        if 48 <= ord(i) <= 57:
            N += i

    listDic = {}
    for i in registered_list:
        listDic[i] = 1

    while new_id in listDic:
        n = 0 if N == "" or int(N) == 0 else int(N)
        N = str(n + 1)
        new_id = S + N

    return new_id


# print(solution(["card", "ace13", "ace16", "banker", "ace17", "ace14"], "ace15"))
# print(solution(["bird99", "bird98", "bird101", "gotoxy"], "bird98"))
print(solution(
["cow", "cow1", "cow2", "cow3", "cow4", "cow9", "cow8", "cow7", "cow6", "cow5"], "cow"))