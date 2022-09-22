# 1. 알파벳 소문자, 숫자, -, _, .만 가능
# 2. .는 처음과 끝에서는 사용 불가하고 연속으로 사용 불가
def parseId(new_id):
    # 1. 소문자로 치환
    new_id = new_id.lower()

    result = ""
    possibleStr = [".", "_", "-", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

    #2. 가능한 문자 뺴고 다 제거
    for c in new_id:
        if 97 <= ord(c) <= 122:
            result += c

        if c in possibleStr:
            result += c


    #3. ..두번 이상을 .로 변환
    while ".." in result:
        result = result.replace("..", ".")

    #4-1. 맨 앞의 .제거
    if len(result) >= 1 and result[0] == ".":
        result = result[1:]

    #4-2 만 뒤의 .제거
    if len(result) >= 1 and result[-1] == ".":
        result = result[:-1]

    #5. new_id가 빈 문자열일 시 a 대입
    if len(result) == 0:
        result = "a"

    # 6. 길이가 16이상이면 앞의 15까지만 출력
    if len(result) >= 16:
        result = result[:15]

    #7. 길이가 2자 이하면 마지막 문자를 길이가 3이 될때까지 반복해서 끝에 넣기
    while len(result) <= 2:
        result += result[-1]

    #8. 처음이나 마지막에 .이 있으면 다시 처음부터
    if result[0] == "." or result[-1] == ".":
        return parseId(result)

    return result

def solution(new_id):
    return parseId(new_id)


# print(solution("...!@BaT#*..y.abcdefghijklm"))
# print(solution("z-+.^."))
# print(solution("=.="))
print(solution("abcdefghijklmn.p"))