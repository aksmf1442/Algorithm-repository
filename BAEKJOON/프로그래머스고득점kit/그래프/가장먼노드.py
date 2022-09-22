# 1. 1번 노드에서 최단 경로로 이동했을 때 가장 멀리 떨어진 노드의 갯수
# 2. 양방향 매핑
from collections import deque

def solution(n, edge):
    graph = [[] for _ in range((n + 1))]
    result = [-1] * (n + 1)
    result[1] = 0

    for v in edge:
        graph[v[0]].append(v[1])
        graph[v[1]].append(v[0])

    queue = deque([(1, 0)])
    while queue:
        node, count = queue.popleft()
        for n in graph[node]:
            if result[n] == -1 or result[n] > count + 1:
                result[n] = count + 1
                queue.append((n, count + 1))

    maxValue = max(result)
    answer = 0
    for value in result:
        if maxValue == value:
            answer += 1

    return answer


print(solution(6, [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]))
