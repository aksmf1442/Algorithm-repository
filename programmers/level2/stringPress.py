# 문자열 압축

def solution(s):
    if (len(s) == 1):
        return 1;
    answer = 1001;
    length = len(s) // 2 + 1
    for i in range(1, length):
        string = '';
        num = 1;
        j = 0;
        while j + (i * 2) <= len(s):
            idx = j + i;
            if s[j: idx] == s[idx : idx + i]:
                num += 1;
            else:
                if (num != 1):
                    string += str(num);
                string += s[j:idx]
                num = 1;
            j += i
        if (num != 1):
            string += str(num);
        string += s[j: len(s)];
        answer = min(answer, len(string))
    return answer

print(solution("a"))
print(solution("ababcdcdababcdcd"))