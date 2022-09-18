#1. 일단 안에 target word가 있는지 확인 없으면 0으로 종료
#2. 사용한 단어는 다시 사용 X
#3. 딕셔너리를 사용하면 될거 같은데, 하나 빼고 같은 단어이면 자신의 그래프에 추가(한 번에 하나의 알파벳만 바꿀 수 있기 때문)

from collections import deque

def solution(begin, target, words):
    answer = 0
    q = deque()
    q.append([begin, 0])
    V = [0 for i in range(len(words))]
    while q:
        word, cnt = q.popleft()
        if word == target:
            answer = cnt
            break
        for i in range(len(words)):
            temp_cnt = 0
            if not V[i]:
                for j in range(len(word)):
                    if word[j] != words[i][j]:
                        temp_cnt += 1
                if temp_cnt == 1:
                    q.append([words[i], cnt + 1])
                    V[i] = 1

    return answer

print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))
