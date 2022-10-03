#goal: 성냥개비 k를 이용해서 숫자 만들기
#1. 숫자마다 성냥개비 개수: [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
#2. 5 -> 2, 2+3, 5, 5, 3 + 2
from itertools import permutations
def solution(k):
    lst = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]
    candidate = set()
    for i in range(1, 11):
        for c in permutations(lst, i):
            if sum(c) == k:
                candidate.add(c)

    return len(candidate)

print(solution(11))