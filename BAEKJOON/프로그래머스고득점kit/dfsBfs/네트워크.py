# 1. 양방향 그래프
# 2. dfs
def dfs(idx, visited, graph):
    visited[idx] = 1
    for i in graph[idx]:
        if visited[i]:
            continue
        dfs(i, visited, graph)


def solution(n, computers):
    answer = 0
    graph = [[] for _ in range(n)]
    visited = [0] * n

    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1 and i != j:
                graph[i].append(j)

    for i in range(n):
        if visited[i] == 1:
            continue
        dfs(i, visited, graph)
        answer += 1

    return answer


print(solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]]))
