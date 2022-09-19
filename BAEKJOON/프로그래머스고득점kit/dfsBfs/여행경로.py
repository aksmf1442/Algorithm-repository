#1. ICN공항에서 항상 출발
#2. tickets는 A->B 단방향 매핑
#3. 항공권은 모두 사용해야 함
#4. 경로가 두 개 이상이라면 알파벳 순서가 앞서는 경로 return(정렬하라는 의미)
#5. 그래프를 딕셔너리 형식으로 만들고 안에는 튜플로 (알바펫, 방문확인)처럼 만든다.
#6. 어떤 경우는 안되는 경우도 있기 떄문에 다시 돌아와야 함

from collections import defaultdict


def solution(tickets):
    answer = []
    tickets.sort(key=lambda x: (x[1], x[0]))
    dic = defaultdict(list)
    for [start, end] in tickets:
        dic[start].append(end)
    for k in dic.keys():
        dic[k].sort(reverse=True)

    def DFS():
        stack = ["ICN"]
        while stack:
            start = stack[-1]
            if not dic[start]:  # start에서 출발하는 항공편이 없는경우 바로 답에 넣기
                answer.append(stack.pop())
            else:
                stack.append(dic[start].pop())

    DFS()
    return answer[::-1]

print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]	))
print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]))