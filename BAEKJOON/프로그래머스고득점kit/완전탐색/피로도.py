#1. 최소 피로도(던전을 돌기 위한 최소값), 소모 피로도(던전을 돈 후 소모되는 값)이 존재한다.
#2. 이건 모든 경우의 수를 확인해봐야 할듯(bfs 및 백트래킹을 통해서)
from itertools import permutations

def solution(k, dungeons):
    answer = 0
    for dungeon in permutations(dungeons):
        count = 0
        piro = k
        for d in dungeon:
            if piro >= d[0]:
                piro -= d[1]
                count += 1
        answer = max(answer, count)
    return answer

print(solution(80, [[80,20],[50,40],[30,10]]))