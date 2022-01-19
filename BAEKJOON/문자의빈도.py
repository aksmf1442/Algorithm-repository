# 문자의 빈도

string = input()
alpha_cnt = {}

string = str.lower(string)# TODO : 문자열의 모든 문자를 소문자로 변환합니다
for char in string:
    # TODO : 글자가 알파벳이라면 alpha_cnt 딕셔너리 이용하여 그 횟수를 기록
    if char not in alpha_cnt:
        alpha_cnt[char] = 1
    else:
        alpha_cnt[char] += 1

#TODO: string의 첫 번째 문자가 등장한 횟수를 출력


print(alpha_cnt[string[0]])