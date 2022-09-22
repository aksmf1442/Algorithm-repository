from collections import defaultdict
from itertools import combinations
from bisect import bisect_left

rankDic = defaultdict(list)


def initRankDic(info):
    global rankDic

    for i in info:
        iArr = i.split(" ")

        category = iArr[:-1]
        score = int(iArr[-1])

        for idx in range(len(category) + 1):
            for arr in combinations(category, idx):
                str = "".join(arr)
                rankDic[str].append(score)

    for rank in rankDic:
        rankDic[rank].sort()


def searchQueryCount(q):
    str = q.split(" ")
    while "and" in str:
        str.remove("and")

    while "-" in str:
        str.remove("-")

    query = "".join(str[:-1])
    score = int(str[-1])
    left = 0
    if rankDic[query]:
        left = bisect_left(rankDic[query], score)

    return len(rankDic[query]) - left


def solution(info, query):
    answer = []
    initRankDic(info)
    for q in query:
        answer.append(searchQueryCount(q))
    return answer


print(solution(
    ["java backend junior pizza 150", "python frontend senior chicken 210", "python frontend senior chicken 150",
     "cpp backend senior pizza 260", "java backend junior chicken 80", "python backend senior chicken 50"],
    ["java and backend and junior and pizza 100", "python and frontend and senior and chicken 200",
     "cpp and - and senior and pizza 250", "- and backend and senior and - 150", "- and - and - and chicken 100",
     "- and - and - and - 150"]))
