# 1. 시간 복잡도는 n^2해도 남음 10000이라서
# 2. 하나씩 선을 제거해가면서 다 확인해보고 len(a) - len(b)의 값 중 가장 작은 수를 리턴
from collections import deque

def bfs(start, visited, graph):
    result = 1
    visited[start] = 1
    q = deque([start])

    while q:
        now = q.popleft()

        for i in graph[now]:
            if visited[i]:
                continue
            visited[i] = 1
            result += 1
            q.append(i)

    return result


def solution(n, wires):
    answer = n
    graph = [[] for _ in range(n + 1)]

    for i in wires:
        graph[i[0]].append(i[1])
        graph[i[1]].append(i[0])

    for start, not_visited in wires:
        visited = [0] * (n+1)
        visited[not_visited] = 1
        count = bfs(start, visited, graph)
        answer = min(answer, abs(count - (n - count)))

    return answer

print(solution(9, [[1,3],[2,3],[3,4],[4,5],[4,6],[4,7],[7,8],[7,9]]))