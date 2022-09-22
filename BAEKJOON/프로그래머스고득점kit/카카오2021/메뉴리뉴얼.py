# 1. 이전에 각 손님들이 주문할 때 가장 많이 주문한 단품메뉴들을 코스요리 메뉴로 구성
# 2. 최소 2가지 이상의 단품메뉴로 코스요리 구성하며, 최소 2명이상의 손님으로부터 주문된 단품메뉴 조합에 대해서만 코스 요리 메뉴 후보 포함
# 3. 조합을 만들어서 딕셔너리 사용으로 2번 이상 주문 된 것을 찾아서 출력
from collections import defaultdict
from itertools import combinations


def solution(orders, course):
    answer = []
    menu = defaultdict(int)
    for c in course:
        for order in orders:
            for i in combinations(order, c):
                print(i)
                menu["".join(sorted(i))] += 1

    for c in course:
        currentCount = 0
        current = []
        for key, value in menu.items():
            if value >= 2 and len(key) == c and currentCount <= value:
                if currentCount < value:
                    currentCount = value
                    current = [key]
                else:
                    current.append(key)
        answer.extend(current)
    print(menu)

    return sorted(answer)


# print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2,3,4]))
print(solution(["XYZ", "XWY", "WXA"], [2, 3, 4]))
